#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Improved Anthropic Documentation Scraper
----------------------------------------
This script scrapes the Anthropic API documentation and saves it in HTML and Markdown formats.
It includes fixes for image optimization, URL handling, and better error recovery.
"""

import os
import re
import time
import json
import queue
import signal
import logging
import hashlib
import threading
import concurrent.futures
import argparse
import yaml
import random
from io import BytesIO
from urllib.parse import urljoin, urlparse
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert
from PIL import Image, UnidentifiedImageError

# User agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41'
]

# Global configuration variables
CONFIG = {}
ROOT_URL = "https://docs.anthropic.com"
BASE_URL = "https://docs.anthropic.com/en/api"
API_DOMAIN = "docs.anthropic.com"
API_PATH_PREFIX = "/en/api/"
OUTPUT_DIR = "anthropic_docs"
HTML_DIR = os.path.join(OUTPUT_DIR, "html")
MD_DIR = os.path.join(OUTPUT_DIR, "md")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
FULL_HTML_DIR = os.path.join(OUTPUT_DIR, "full_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "page_metadata.json")
WORKER_THREADS = 4
IMAGE_THREADS = 4
REQUEST_DELAY = 1.0  # 1 second between requests
MAX_CRAWL_DEPTH = 5
LOG_FILE = "scraper.log"
MAX_IMAGE_SIZE = 800
IMAGE_QUALITY = 85

# Excluded paths and patterns
EXCLUDED_EXTENSIONS = ['.pdf', '.zip', '.tar', '.gz', '.mp4', '.avi', '.mov', '.mpg', '.exe', '.dmg', '.pkg', '.js', '.css']
EXCLUDED_PATTERNS = [
    '/feedback', '/legal', '/privacy', '/terms', '/search',
    '?q=', '/api/v1/', 'twitter.com', 'github.com', 'linkedin.com',
    'facebook.com', 'instagram.com', 'youtube.com', 'mailto:'
]

# Global state
visited_urls = set()
queued_urls = set()
skipped_urls = set()
url_to_filename = {}
page_metadata = {}
processed_pages = 0
image_counter = 0
total_images = 0
error_pages = 0
failed_images = 0

# Queues and threading
page_queue = queue.Queue()
image_queue = queue.Queue()
stop_event = threading.Event()
metadata_lock = threading.Lock()
request_lock = threading.Lock()
last_request_time = 0

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Improved Anthropic Documentation Scraper")
    parser.add_argument(
        "--config", 
        default="config.yaml", 
        help="Path to configuration file (default: config.yaml)"
    )
    parser.add_argument(
        "--start-url", 
        help="Starting URL to scrape (overrides config)"
    )
    parser.add_argument(
        "--output-dir", 
        help="Base directory for all output files"
    )
    parser.add_argument(
        "--threads", 
        type=int, 
        help="Number of worker threads"
    )
    parser.add_argument(
        "--image-threads", 
        type=int, 
        help="Number of image download threads"
    )
    parser.add_argument(
        "--delay", 
        type=float, 
        help="Minimum delay between requests in seconds"
    )
    parser.add_argument(
        "--depth", 
        type=int, 
        help="Maximum crawl depth"
    )
    parser.add_argument(
        "--log-level", 
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Logging level"
    )
    parser.add_argument(
        "--no-images", 
        action="store_true", 
        help="Skip downloading images"
    )
    parser.add_argument(
        "--test", 
        action="store_true", 
        help="Run in test mode (limited pages)"
    )
    
    return parser.parse_args()

def load_config(config_path):
    """Load configuration from YAML file"""
    global CONFIG, ROOT_URL, BASE_URL, API_DOMAIN, API_PATH_PREFIX
    global OUTPUT_DIR, HTML_DIR, MD_DIR, IMAGES_DIR, FULL_HTML_DIR, METADATA_FILE
    global WORKER_THREADS, IMAGE_THREADS, REQUEST_DELAY, MAX_CRAWL_DEPTH, LOG_FILE
    global MAX_IMAGE_SIZE, IMAGE_QUALITY, EXCLUDED_PATTERNS
    
    try:
        if not os.path.exists(config_path):
            logging.warning(f"Config file {config_path} not found, using defaults")
            return
            
        with open(config_path, 'r') as f:
            CONFIG = yaml.safe_load(f)
            
        # URLs and paths
        if 'urls' in CONFIG:
            ROOT_URL = CONFIG['urls'].get('root', ROOT_URL)
            BASE_URL = CONFIG['urls'].get('base', BASE_URL)
            API_DOMAIN = CONFIG['urls'].get('domain', API_DOMAIN)
            API_PATH_PREFIX = CONFIG['urls'].get('path_prefix', API_PATH_PREFIX)
        
        # Excluded patterns
        if 'excluded_patterns' in CONFIG:
            EXCLUDED_PATTERNS = CONFIG['excluded_patterns']
        
        # Output directories
        if 'directories' in CONFIG:
            OUTPUT_DIR = CONFIG['directories'].get('output_dir', OUTPUT_DIR)
            HTML_DIR = os.path.join(OUTPUT_DIR, CONFIG['directories'].get('html', 'html'))
            MD_DIR = os.path.join(OUTPUT_DIR, CONFIG['directories'].get('markdown', 'md'))
            IMAGES_DIR = os.path.join(OUTPUT_DIR, CONFIG['directories'].get('images', 'images'))
            FULL_HTML_DIR = os.path.join(OUTPUT_DIR, CONFIG['directories'].get('full_html', 'full_html'))
            METADATA_FILE = os.path.join(OUTPUT_DIR, CONFIG['directories'].get('metadata_file', 'page_metadata.json'))
        
        # Thread configuration
        if 'threading' in CONFIG:
            WORKER_THREADS = CONFIG['threading'].get('worker_threads', WORKER_THREADS)
            IMAGE_THREADS = CONFIG['threading'].get('image_threads', IMAGE_THREADS)
            MAX_CRAWL_DEPTH = CONFIG['threading'].get('max_crawl_depth', MAX_CRAWL_DEPTH)
        
        # Rate limiting
        if 'rate_limiting' in CONFIG:
            REQUEST_DELAY = CONFIG['rate_limiting'].get('min_delay_between_requests', REQUEST_DELAY)
            MAX_REQUESTS_PER_SECOND = CONFIG['rate_limiting'].get('max_requests_per_second', 10)
            ADAPTIVE_RATE_LIMITING = CONFIG['rate_limiting'].get('adaptive', True)
            MAX_RETRIES = CONFIG['rate_limiting'].get('max_retries', 3)
            BASE_RETRY_DELAY = CONFIG['rate_limiting'].get('base_retry_delay', 1.0)
            MAX_RETRY_DELAY = CONFIG['rate_limiting'].get('max_retry_delay', 15.0)
        
        # Logging
        if 'logging' in CONFIG:
            LOG_FILE = CONFIG['logging'].get('log_file', LOG_FILE)
        
        # Image processing
        if 'images' in CONFIG:
            MAX_IMAGE_SIZE = CONFIG['images'].get('max_size', MAX_IMAGE_SIZE)
            IMAGE_QUALITY = CONFIG['images'].get('quality', IMAGE_QUALITY)
        
        logging.info(f"Configuration loaded from {config_path}")
        
    except Exception as e:
        logging.error(f"Error loading config file: {e}")

def apply_command_line_overrides(args):
    """Override configuration with command line arguments"""
    global OUTPUT_DIR, HTML_DIR, MD_DIR, IMAGES_DIR, FULL_HTML_DIR, METADATA_FILE
    global WORKER_THREADS, IMAGE_THREADS, REQUEST_DELAY, MAX_CRAWL_DEPTH
    
    if args.output_dir:
        OUTPUT_DIR = args.output_dir
        HTML_DIR = os.path.join(OUTPUT_DIR, "html")
        MD_DIR = os.path.join(OUTPUT_DIR, "md")
        IMAGES_DIR = os.path.join(OUTPUT_DIR, "images")
        FULL_HTML_DIR = os.path.join(OUTPUT_DIR, "full_html")
        METADATA_FILE = os.path.join(OUTPUT_DIR, "page_metadata.json")
    
    if args.threads:
        WORKER_THREADS = args.threads
    
    if args.image_threads:
        IMAGE_THREADS = args.image_threads
    
    if args.delay:
        REQUEST_DELAY = args.delay
    
    if args.depth:
        MAX_CRAWL_DEPTH = args.depth

def setup_directories():
    """Create output directories if they don't exist"""
    for directory in [OUTPUT_DIR, HTML_DIR, MD_DIR, IMAGES_DIR, FULL_HTML_DIR]:
        os.makedirs(directory, exist_ok=True)
    logging.info(f"Created output directories")

def setup_logging(log_level=None):
    """Configure logging"""
    level = getattr(logging, log_level if log_level else "INFO")
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging configured")

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    logging.info("Interrupt received, shutting down...")
    stop_event.set()
    sys.exit(0)

def fetch_url(url, max_retries=3, retry_delay=1, timeout=30):
    """Fetch a URL with rate limiting and retries"""
    global last_request_time, REQUEST_DELAY
    
    headers = {
        'User-Agent': random.choice(USER_AGENTS) if USER_AGENTS else 'Anthropic Documentation Scraper',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'max-age=0',
    }
    
    # Rate limiting
    with request_lock:
        current_time = time.time()
        elapsed = current_time - last_request_time
        
        if elapsed < REQUEST_DELAY:
            sleep_time = REQUEST_DELAY - elapsed
            logging.debug(f"Rate limiting: sleeping for {sleep_time:.2f}s")
            time.sleep(sleep_time)
        
        last_request_time = time.time()
    
    retry_count = 0
    current_retry_delay = retry_delay
    
    while retry_count < max_retries:
        try:
            response = requests.get(url, headers=headers, timeout=timeout)
            
            # Handle rate limiting response
            if response.status_code == 429:
                retry_count += 1
                # Exponential backoff with jitter for retry delay
                current_retry_delay = min(current_retry_delay * 2 + random.uniform(0.1, 1.0), MAX_RETRY_DELAY)
                
                if retry_count < max_retries:
                    logging.warning(f"Error 429 for URL: {url}, retrying in {current_retry_delay:.1f}s (attempt {retry_count}/{max_retries})")
                    time.sleep(current_retry_delay)
                    
                    # Increase the global request delay if adaptive rate limiting is enabled
                    if ADAPTIVE_RATE_LIMITING:
                        REQUEST_DELAY = min(REQUEST_DELAY * 1.5, 2.0)
                        logging.info(f"Adaptive rate limiting: increased delay to {REQUEST_DELAY:.2f}s")
                    
                    continue
                else:
                    logging.error(f"Failed to fetch page due to rate limiting: {url}")
                    return None
            
            # If we got a 200 response and we previously increased the delay, we can slightly decrease it
            if response.status_code == 200 and ADAPTIVE_RATE_LIMITING and REQUEST_DELAY > CONFIG['rate_limiting'].get('min_delay_between_requests', 0.25):
                REQUEST_DELAY = max(REQUEST_DELAY * 0.9, CONFIG['rate_limiting'].get('min_delay_between_requests', 0.25))
                logging.debug(f"Adaptive rate limiting: decreased delay to {REQUEST_DELAY:.2f}s")
            
            response.raise_for_status()
            return response.text
            
        except requests.exceptions.RequestException as e:
            retry_count += 1
            
            if retry_count < max_retries:
                logging.warning(f"Error fetching URL: {url}, retrying in {current_retry_delay:.1f}s (attempt {retry_count}/{max_retries})")
                time.sleep(current_retry_delay)
                # Exponential backoff
                current_retry_delay = min(current_retry_delay * 2, MAX_RETRY_DELAY)
            else:
                logging.error(f"Failed to fetch page: {url}")
                return None

def clean_filename(url, is_image=False):
    """Convert URL to a clean filename"""
    # Extract path from the URL
    parsed_url = urlparse(url)
    path = parsed_url.path
    
    # Handle root URL
    if path == "" or path == "/":
        return "index" + (".jpg" if is_image else ".html")
    
    # Remove API path prefix if present
    if path.startswith(API_PATH_PREFIX):
        path = path[len(API_PATH_PREFIX):]
    elif path.startswith("/en/docs/"):
        path = path[len("/en/docs/"):]
    
    # Remove leading/trailing slashes
    path = path.strip('/')
    
    # Replace slashes with underscores
    filename = path.replace('/', '_')
    
    # Remove query parameters
    filename = filename.split('?', 1)[0]
    
    # Remove fragment identifiers
    filename = filename.split('#', 1)[0]
    
    # Handle file extensions
    if is_image:
        # Preserve original extension if it exists and is valid
        if '.' in filename and filename.split('.')[-1].lower() in ('jpg', 'jpeg', 'png', 'gif', 'svg'):
            pass
        else:
            filename += '.jpg'  # Default to jpg for images
    else:
        # Make sure HTML files have .html extension
        if not filename.endswith('.html'):
            filename += '.html'
    
    # Clean up any remaining invalid characters
    filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
    
    # Ensure filename isn't too long
    if len(filename) > 150:
        ext = filename.split('.')[-1]
        filename = filename[:146-len(ext)] + '.' + ext
    
    # If we end up with an empty filename, use a hash of the URL
    if not filename or filename == '.html' or filename == '.jpg':
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
        filename = f"page_{url_hash}" + (".jpg" if is_image else ".html")
    
    return filename

def optimize_image(img_data, max_size=800):
    """Optimize an image for size and quality"""
    try:
        img = Image.open(BytesIO(img_data))
        
        # Convert to RGB if image has transparency (except for SVG)
        if img.mode == 'RGBA':
            # Create a white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            # Paste the image onto the background, using alpha channel as mask
            background.paste(img, mask=img.split()[3])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Resize if necessary
        width, height = img.size
        if width > max_size or height > max_size:
            if width > height:
                new_width = max_size
                new_height = int(height * (max_size / width))
            else:
                new_height = max_size
                new_width = int(width * (max_size / height))
            img = img.resize((new_width, new_height), Image.LANCZOS)
            
        # Save the optimized image
        output = BytesIO()
        img.save(output, format='JPEG', quality=IMAGE_QUALITY, optimize=True)
        return output.getvalue()
        
    except (UnidentifiedImageError, OSError) as e:
        logging.warning(f"Image optimization failed: {e}")
        return img_data
    except Exception as e:
        logging.warning(f"Image optimization failed, saving raw: {e}")
        return img_data

def process_images(soup, base_url, page_url):
    """Find all images on the page, add them to the download queue, and fix links"""
    global total_images
    image_links = []
    
    # Find all img tags
    for img in soup.find_all('img'):
        # Skip images without src
        if not img.get('src'):
            continue
            
        # Skip SVG and Base64 encoded images
        img_src = img.get('src', '')
        if img_src.startswith('data:'):
            continue
            
        # Normalize the image URL
        img_url = urljoin(base_url, img_src)
        
        # Skip external images
        if API_DOMAIN not in img_url:
            continue
            
        # Generate a local path for the image
        img_filename = clean_filename(img_url, is_image=True)
        local_path = os.path.join(IMAGES_DIR, img_filename)
        
        # Update the image src attribute to point to the local file
        rel_path = os.path.relpath(IMAGES_DIR, os.path.dirname(os.path.join(HTML_DIR, clean_filename(page_url))))
        img['src'] = os.path.join(rel_path, img_filename)
        
        # Add to download queue
        image_queue.put((img_url, local_path))
        image_links.append(img_url)
        total_images += 1
        
    return image_links

def download_image(img_url, local_path):
    """Download an image and save it to disk"""
    global failed_images
    
    # Skip if already downloaded
    if os.path.exists(local_path):
        logging.debug(f"Image already exists: {local_path}")
        return True
        
    try:
        # Set shorter timeout for image downloads
        response = fetch_url(img_url, max_retries=2, retry_delay=1, timeout=15)
        if not response:
            with metadata_lock:
                failed_images += 1
            logging.warning(f"Failed to download image: {img_url}")
            return False
            
        # Try to optimize the image
        try:
            img_data = optimize_image(response.content, MAX_IMAGE_SIZE)
        except Exception as e:
            logging.warning(f"Image optimization failed, saving raw: {e}")
            img_data = response.content
            
        # Save the image
        with open(local_path, 'wb') as f:
            f.write(img_data)
            
        logging.debug(f"Downloaded image: {img_url} -> {local_path}")
        return True
        
    except Exception as e:
        with metadata_lock:
            failed_images += 1
        logging.error(f"Error downloading image {img_url}: {e}")
        return False

def normalize_url(url):
    """Normalize a URL to avoid duplicates"""
    # Convert to lowercase (for domain part only)
    parsed_url = urlparse(url)
    normalized = parsed_url._replace(netloc=parsed_url.netloc.lower())
    url = normalized.geturl()
    
    # Remove fragment identifiers
    url = url.split('#')[0]
    
    # Handle trailing slashes consistently
    if not url.endswith('/') and '.' not in url.split('/')[-1]:
        url += '/'
    
    return url

def is_valid_api_url(url):
    """Check if a URL should be crawled"""
    parsed_url = urlparse(url)
    
    # Only crawl URLs on the API domain
    if parsed_url.netloc != API_DOMAIN:
        return False
    
    # Skip excluded extensions
    path = parsed_url.path.lower()
    for ext in EXCLUDED_EXTENSIONS:
        if path.endswith(ext):
            return False
    
    # Skip URLs matching excluded patterns
    for pattern in EXCLUDED_PATTERNS:
        if pattern in url:
            return False
    
    # Only follow URLs in the API path or docs path
    return API_PATH_PREFIX in url or '/en/docs/' in url

def process_links(soup, current_url):
    """Find all links on the page, filter them, and update URLs to point to local files"""
    new_links = []
    base_url = urljoin(current_url, '/')
    
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Skip empty links
        if not href or href == '#':
            continue
            
        # Skip excluded extensions
        if any(href.endswith(ext) for ext in EXCLUDED_EXTENSIONS):
            continue
            
        # Skip excluded patterns
        if any(pattern in href for pattern in EXCLUDED_PATTERNS):
            continue
            
        # Normalize URL
        absolute_url = urljoin(current_url, href)
        
        # Skip URLs outside our domain
        if not is_valid_api_url(absolute_url):
            # Update external links to have target="_blank"
            a_tag['target'] = '_blank'
            a_tag['rel'] = 'noopener noreferrer'
            continue
            
        # Skip URLs that have already been visited or queued
        if absolute_url in visited_urls or absolute_url in queued_urls:
            continue
            
        # Check if the URL is valid
        if not absolute_url.startswith(('http://', 'https://')):
            continue
            
        # Add to the list of new links
        new_links.append(absolute_url)
        
        # Update the href to point to local file
        if normalized_url := normalize_url(absolute_url):
            local_filename = clean_filename(normalized_url)
            a_tag['href'] = f"{local_filename}.html"
    
    return new_links

def process_page(url, depth):
    """Process a single page, extract content, and queue new links"""
    global processed_pages
    
    if stop_event.is_set():
        return
    
    if depth > MAX_CRAWL_DEPTH:
        logging.debug(f"Maximum depth reached for URL: {url}")
        return
        
    if url in visited_urls:
        logging.debug(f"URL already visited: {url}")
        return
        
    if not is_valid_api_url(url):
        skipped_urls.add(url)
        logging.debug(f"Skipping URL (not in API domain or path): {url}")
        return
    
    visited_urls.add(url)
    
    # Get the content
    html_content = fetch_url(url)
    if not html_content:
        return
        
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Process any images found on the page
    image_links = process_images(soup, url, url)
    logging.info(f"Queued {len(image_links)} images from {url}")
    
    # Process any new links
    new_links = process_links(soup, url)
    logging.info(f"Found {len(new_links)} new links on page {url}")
    
    # Extract the main content
    extracted_soup = extract_api_doc_content(soup, url)
    
    # Save the full HTML
    filename = clean_filename(url)
    full_html_file = os.path.join(FULL_HTML_DIR, f"{filename}.html")
    with open(full_html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    logging.info(f"Saved full HTML: {full_html_file}")
    
    # Save the processed HTML
    html_file = os.path.join(HTML_DIR, f"{filename}.html")
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(extracted_soup))
    logging.info(f"Saved HTML: {html_file}")
    
    # Convert to Markdown
    markdown_content = md_convert(str(extracted_soup), heading_style="ATX")
    
    # Improve the markdown formatting
    improved_markdown = improve_markdown_format(markdown_content, url)
    
    # Save the Markdown
    md_file = os.path.join(MD_DIR, f"{filename}.md")
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(improved_markdown)
    logging.info(f"Saved Markdown: {md_file}")
    
    # Update page metadata
    with metadata_lock:
        title = soup.title.text.strip() if soup.title else os.path.basename(url)
        page_metadata[url] = {
            'title': title,
            'filename': filename,
            'url': url,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'html_size': os.path.getsize(html_file),
            'md_size': os.path.getsize(md_file),
            'full_html_size': os.path.getsize(full_html_file),
            'image_count': len(image_links),
            'depth': depth
        }
    
    processed_pages += 1
    logging.info(f"Processed page {processed_pages}: {url}")
    
    # Add new links to the queue for crawling
    for link in new_links:
        if link not in visited_urls and link not in queued_urls:
            queued_urls.add(link)
            page_queue.put((link, depth + 1))
    
    return True

def extract_api_doc_content(soup, url):
    """Extract and clean API documentation content from HTML"""
    # Try to identify if this is an API reference page
    is_api_reference = API_PATH_PREFIX in url or any(keyword in url for keyword in ['api', 'reference', 'messages', 'authentication'])
    
    # Strategy #1: Try to find main content container using common selectors
    content_selectors = [
        'main',                      # Common main content wrapper
        'article',                   # Article content
        '.article-content',          # Article content class
        '.content',                  # General content class
        '.main-content',             # Main content class
        '.doc-content',              # Documentation content class
        '#main-content',             # Main content ID
        '.documentation',            # Documentation class
        '.api-content',              # API content class
        '.markdown-section',         # Markdown section (common in docs)
        '.page-content',             # Page content class
        '.post-content',             # Post content class
    ]
    
    content = None
    
    # Try each selector until we find content
    for selector in content_selectors:
        content_element = soup.select_one(selector)
        if content_element and len(content_element.get_text(strip=True)) > 100:
            content = content_element
            logging.debug(f"Found content using selector: {selector}")
            break
    
    # Strategy #2: If we still don't have content, try identifying the largest text block
    if not content:
        candidates = []
        for div in soup.find_all(['div', 'section']):
            text_length = len(div.get_text(strip=True))
            if text_length > 200:  # Only consider substantial blocks of text
                candidates.append((div, text_length))
        
        if candidates:
            # Sort by text length (descending)
            candidates.sort(key=lambda x: x[1], reverse=True)
            content = candidates[0][0]
            logging.debug(f"Found content using text length heuristic")
    
    # Strategy #3: If we still don't have content, use the body element
    if not content:
        content = soup.body
        logging.debug("Using body element as content")
    
    # Clean up the content
    if content:
        # Remove navigation, footer, header, and sidebar elements
        for element in content.select('nav, .navigation, .navbar, .nav, .menu, header, .header, footer, .footer, .sidebar, aside, .aside'):
            element.decompose()
        
        # Remove elements typically used for UI components rather than content
        for element in content.select('.pagination, .breadcrumb, .tabs, .tab, .ad, .advertisement, .cookie-banner, .social-share, .related-articles'):
            element.decompose()
        
        # Remove empty elements
        for element in content.find_all():
            if not element.get_text(strip=True) and not element.find_all('img'):
                element.decompose()
    
    # Special handling for API reference pages
    if is_api_reference:
        # Improve code examples
        for pre in content.find_all('pre'):
            # Try to determine the language
            code_class = pre.get('class', [])
            language = None
            
            # Look for language indicators in the class
            for cls in code_class:
                if cls.startswith('language-') or cls.startswith('lang-'):
                    language = cls.split('-')[1]
                    break
                elif cls in ['python', 'json', 'bash', 'javascript', 'typescript', 'js', 'ts', 'curl']:
                    language = cls
                    break
            
            # If no language was found in the class, try to determine it from content
            if not language:
                code_content = pre.get_text()
                if 'curl' in code_content.lower():
                    language = 'bash'
                elif 'import' in code_content and ('from' in code_content or ';' not in code_content):
                    language = 'python'
                elif '{' in code_content and '}' in code_content and '"' in code_content:
                    language = 'json'
                elif 'function' in code_content or 'const' in code_content:
                    language = 'typescript' if 'interface' in code_content else 'javascript'
            
            # Add a code tag with the language if we identified one
            if language and not pre.find('code'):  # Only if there's no code tag already
                code = soup.new_tag('code')
                code.string = pre.string
                pre.string = ''
                pre['class'] = pre.get('class', []) + [f'language-{language}']
                code['class'] = [f'language-{language}']
                pre.append(code)
        
        # Improve parameter tables
        for table in content.find_all('table'):
            # Check if this looks like a parameters table
            headers = [th.get_text(strip=True).lower() for th in table.find_all('th')]
            if headers and ('parameter' in headers or 'name' in headers or 'field' in headers):
                # Make sure parameter names are in code format
                for row in table.find_all('tr'):
                    cells = row.find_all('td')
                    if cells:
                        # First cell is usually the parameter name
                        param_cell = cells[0]
                        param_text = param_cell.get_text(strip=True)
                        
                        # If it's not already in code tags, wrap it
                        if not param_cell.find('code') and param_text:
                            # Clear the cell
                            param_cell.clear()
                            
                            # Create and add a code tag
                            code = soup.new_tag('code')
                            code.string = param_text
                            param_cell.append(code)
    
    return content

def improve_markdown_format(markdown_content, url):
    """Improve the formatting of generated markdown"""
    # Fix code blocks - ensure proper language detection
    def fix_code_blocks(match):
        code_content = match.group(2).strip()
        
        # Detect language
        language = "bash"  # Default language
        
        # Check for common language patterns in the code
        if re.search(r'import\s+[a-zA-Z0-9_]+\s+from|const\s+[a-zA-Z0-9_]+\s+=|let\s+[a-zA-Z0-9_]+\s+=|var\s+[a-zA-Z0-9_]+\s+=', code_content):
            if "import" in code_content and "from" in code_content and ";" not in code_content:
                language = "python"
            elif "const" in code_content or "let" in code_content or "var" in code_content:
                language = "javascript"
        elif re.search(r'function\s+[a-zA-Z0-9_]+\s*\(|class\s+[a-zA-Z0-9_]+\s*[\{:]', code_content):
            if "{" in code_content and ";" in code_content:
                language = "javascript"
            else:
                language = "python"
        elif re.search(r'#include|int\s+main\(|void\s+[a-zA-Z0-9_]+\s*\(', code_content):
            language = "cpp"
        elif re.search(r'public\s+static\s+void\s+main|public\s+class', code_content):
            language = "java"
        elif re.search(r'curl\s+', code_content):
            language = "bash"
        elif re.search(r'SELECT|INSERT|UPDATE|DELETE|CREATE\s+TABLE', code_content, re.IGNORECASE):
            language = "sql"
        elif re.search(r'<?php', code_content):
            language = "php"
        elif re.search(r'<html>|<div>|<body>', code_content):
            language = "html"
        elif re.search(r'^\s*{', code_content) and re.search(r'}\s*$', code_content):
            language = "json"
        
        return f"```{language}\n{code_content}\n```"
    
    # Fix tables - ensure proper alignment
    def fix_tables(match):
        table_content = match.group(0)
        lines = table_content.split('\n')
        processed_lines = []
        
        # Process header row
        if '|' in lines[0]:
            headers = [h.strip() for h in lines[0].split('|')]
            headers = [h for h in headers if h]  # Remove empty strings
            
            col_widths = [len(h) for h in headers]
            
            # Process separator row
            if len(lines) > 1 and '---' in lines[1]:
                separators = [s.strip() for s in lines[1].split('|')]
                separators = [s for s in separators if s]  # Remove empty strings
                
                for i, sep in enumerate(separators):
                    if i < len(col_widths):
                        if ':' in sep:
                            if sep.startswith(':') and sep.endswith(':'):
                                # Center alignment
                                separators[i] = ':' + '-' * (col_widths[i]) + ':'
                            elif sep.startswith(':'):
                                # Left alignment
                                separators[i] = ':' + '-' * (col_widths[i])
                            elif sep.endswith(':'):
                                # Right alignment
                                separators[i] = '-' * (col_widths[i]) + ':'
                        else:
                            # Default left alignment
                            separators[i] = '-' * (col_widths[i])
                
                processed_lines.append('| ' + ' | '.join(headers) + ' |')
                processed_lines.append('| ' + ' | '.join(separators) + ' |')
                
                # Process data rows
                for line in lines[2:]:
                    if '|' in line:
                        cells = [c.strip() for c in line.split('|')]
                        cells = [c for c in cells if c != '']  # Remove empty cells from start/end
                        if cells:
                            processed_lines.append('| ' + ' | '.join(cells) + ' |')
            else:
                # This might not be a proper table, return as is
                return table_content
                
            return '\n'.join(processed_lines)
        
        return table_content
    
    # Fix API parameters - improve formatting of parameter tables
    def fix_api_parameters(match):
        params_content = match.group(0)
        
        # Convert bullet lists of parameters to tables if they match API parameter patterns
        if re.search(r'[*-]\s+`[a-zA-Z0-9_]+`\s+-\s+', params_content):
            lines = params_content.split('\n')
            param_pattern = re.compile(r'[*-]\s+`([a-zA-Z0-9_]+)`\s+-\s+(.*)')
            
            # Check if enough lines match the parameter pattern
            param_matches = [param_pattern.match(line) for line in lines]
            if sum(1 for m in param_matches if m) >= 2:  # At least 2 parameters
                # Create a table
                table_lines = ['| Parameter | Description |', '| --- | --- |']
                
                current_param = None
                current_desc = []
                
                for i, line in enumerate(lines):
                    param_match = param_pattern.match(line)
                    if param_match:
                        # Save previous parameter if exists
                        if current_param:
                            table_lines.append(f"| `{current_param}` | {' '.join(current_desc)} |")
                        
                        # Start new parameter
                        current_param = param_match.group(1)
                        current_desc = [param_match.group(2)]
                    elif current_param and line.strip() and not param_pattern.match(line):
                        # Continue description on next line
                        current_desc.append(line.strip())
                
                # Add the last parameter
                if current_param:
                    table_lines.append(f"| `{current_param}` | {' '.join(current_desc)} |")
                
                return '\n'.join(table_lines)
        
        return params_content
    
    # Fix headers - ensure proper spacing
    def fix_headers(match):
        level = len(match.group(1))
        text = match.group(2).strip()
        return f"{'#' * level} {text}\n"
    
    # Fix lists - ensure proper indentation
    def fix_lists(match):
        list_content = match.group(0)
        lines = list_content.split('\n')
        processed_lines = []
        
        for line in lines:
            # Handle unordered lists
            if re.match(r'^[\s]*[*-]', line):
                indent_level = len(re.match(r'^[\s]*', line).group(0))
                content = line.strip()
                processed_lines.append('  ' * (indent_level // 2) + content)
            # Handle ordered lists
            elif re.match(r'^[\s]*\d+\.', line):
                indent_level = len(re.match(r'^[\s]*', line).group(0))
                content = line.strip()
                processed_lines.append('  ' * (indent_level // 2) + content)
            else:
                processed_lines.append(line)
        
        return '\n'.join(processed_lines)
    
    # Apply all the fixes
    
    # First, handle code blocks to avoid interference with other patterns
    markdown_content = re.sub(r'```(.*?)\n(.*?)```', fix_code_blocks, markdown_content, flags=re.DOTALL)
    
    # Fix other elements
    markdown_content = re.sub(r'^(#+)\s*(.*?)$', fix_headers, markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'(\|.*\|\n\|[-|:]*\|\n(\|.*\|\n)*)', fix_tables, markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'((?:^[*-].*\n)+)', fix_api_parameters, markdown_content, flags=re.MULTILINE)
    markdown_content = re.sub(r'((?:^[\s]*[*-].*\n)+|(?:^[\s]*\d+\..*\n)+)', fix_lists, markdown_content, flags=re.MULTILINE)
    
    # Fix consecutive newlines (max 2)
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    # Add a front matter section with title and source URL
    title = url.split('/')[-1].replace('-', ' ').title()
    front_matter = f"""---
title: {title}
source_url: {url}
---

"""
    
    return front_matter + markdown_content

def page_scraper_worker():
    """Worker thread for page scraping"""
    while not stop_event.is_set():
        try:
            # Get a page from the queue with a timeout
            url, depth = page_queue.get(timeout=1)
            
            # Process the page
            process_page(url, depth)
            
            # Mark task as done
            page_queue.task_done()
            
        except queue.Empty:
            # Queue is empty, check if all URLs have been processed
            if queued_urls <= visited_urls and page_queue.empty():
                logging.info("No more pages to process, exiting worker")
                break
        except Exception as e:
            logging.error(f"Error in page scraper worker: {e}")

def image_downloader_worker():
    """Worker thread for image downloading"""
    global image_counter
    
    while not stop_event.is_set():
        # Use a timeout when getting from the queue
        try:
            # Get an image from the queue with a timeout
            try:
                img_url, local_path = image_queue.get(timeout=1)
            except queue.Empty:
                # If queue is empty and no more pages are being processed,
                # we can exit this worker
                if page_queue.empty() and all(not t.is_alive() for t in page_workers):
                    logging.info("No more images to download, exiting worker")
                    break
                continue
                
            success = False
            try:
                # Download the image with timeout
                success = download_image(img_url, local_path)
                
                # Update counter
                with metadata_lock:
                    image_counter += 1
                    if image_counter % 10 == 0 or image_counter == total_images:
                        logging.info(f"Downloaded {image_counter}/{total_images} images")
                
            except Exception as e:
                # Catch any exception to ensure task_done() is called
                logging.error(f"Unexpected error downloading image {img_url}: {e}")
                with metadata_lock:
                    failed_images += 1
            finally:
                # Always mark the task as done, even on failure
                image_queue.task_done()
                
        except Exception as e:
            logging.error(f"Error in image downloader worker: {e}")
            # Don't break the loop on a single error

def save_metadata():
    """Save metadata to disk"""
    try:
        # Save URL to filename mapping
        with open(os.path.join(OUTPUT_DIR, 'url_to_filename.json'), 'w', encoding='utf-8') as f:
            json.dump(url_to_filename, f, indent=2)
        
        # Save page metadata
        with open(METADATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(page_metadata, f, indent=2)
        
        # Save skipped URLs
        with open(os.path.join(OUTPUT_DIR, 'skipped_urls.txt'), 'w', encoding='utf-8') as f:
            f.write("The following URLs were skipped during crawling:\n\n")
            for url in sorted(skipped_urls):
                f.write(f"{url}\n")
        
        logging.info(f"Saved metadata to {METADATA_FILE}")
    except Exception as e:
        logging.error(f"Error saving metadata: {e}")

def create_toc():
    """Create a table of contents file with better organization"""
    try:
        # Sort pages by filename for a consistent order
        sorted_pages = sorted(page_metadata.values(), key=lambda x: x['filename'])
        
        # Group pages by categories
        categories = {
            'Getting Started': [],
            'Authentication': [],
            'Messages API': [],
            'Models': [],
            'Parameters': [],
            'Streaming': [],
            'Error Handling': [],
            'Tools': [],
            'Content Filtering': [],
            'Embeddings': [],
            'Client Libraries': [],
            'Pricing': [],
            'Reference': []
        }
        
        # Assign pages to categories based on keywords in title or URL
        for page in sorted_pages:
            title = page['title'].lower()
            url = page['url'].lower()
            filename = page['filename'].lower()
            
            # Determine the appropriate category
            if any(kw in url or kw in title or kw in filename for kw in ['getting-started', 'welcome', 'introduction', 'overview']):
                categories['Getting Started'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['authentication', 'auth', 'api-key']):
                categories['Authentication'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['messages', 'completions']):
                categories['Messages API'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['model', 'claude', 'versions']):
                categories['Models'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['parameter', 'request', 'response']):
                categories['Parameters'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['stream', 'streaming']):
                categories['Streaming'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['error', 'exception', 'troubleshoot']):
                categories['Error Handling'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['tool', 'function']):
                categories['Tools'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['content-filter', 'moderation']):
                categories['Content Filtering'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['embed', 'embedding', 'vector']):
                categories['Embeddings'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['client', 'library', 'sdk']):
                categories['Client Libraries'].append(page)
            elif any(kw in url or kw in title or kw in filename for kw in ['price', 'pricing', 'cost', 'billing']):
                categories['Pricing'].append(page)
            else:
                categories['Reference'].append(page)
        
        # Create the table of contents in Markdown format
        toc_content = "# Anthropic API Documentation\n\n"
        toc_content += "This is a comprehensive guide to the Anthropic API, providing access to Claude and other AI models.\n\n"
        
        # Add a table of contents
        toc_content += "## Table of Contents\n\n"
        
        # Add links to categories
        for category in categories:
            if categories[category]:  # Only include categories with pages
                anchor = category.lower().replace(' ', '-')
                toc_content += f"- [{category}](#{anchor})\n"
        
        toc_content += "\n"
        
        # Add sections for each category with their pages
        for category, pages in categories.items():
            if not pages:  # Skip empty categories
                continue
                
            toc_content += f"## {category}\n\n"
            
            for page in pages:
                title = page['title']
                filename = page['filename'].replace('.html', '.md')
                toc_content += f"- [{title}]({filename})\n"
            
            toc_content += "\n"
        
        # Add a note about the scraper
        toc_content += "---\n\n"
        toc_content += "*This documentation was automatically generated by the Anthropic Documentation Scraper.*\n"
        
        # Save TOC to file
        toc_path = os.path.join(MD_DIR, 'index.md')
        with open(toc_path, 'w', encoding='utf-8') as f:
            f.write(toc_content)
        
        # Create a sidebar file for navigation
        sidebar_content = "# Anthropic API Docs\n\n"
        
        # Add sections for categories in the sidebar
        for category, pages in categories.items():
            if not pages:  # Skip empty categories
                continue
                
            sidebar_content += f"## {category}\n\n"
            
            for page in pages:
                title = page['title']
                filename = page['filename'].replace('.html', '')
                sidebar_content += f"- [{title}]({filename})\n"
            
            sidebar_content += "\n"
        
        # Save sidebar to file
        sidebar_path = os.path.join(MD_DIR, 'sidebar.md')
        with open(sidebar_path, 'w', encoding='utf-8') as f:
            f.write(sidebar_content)
        
        logging.info(f"Created table of contents at {toc_path}")
        logging.info(f"Created sidebar navigation at {sidebar_path}")
    except Exception as e:
        logging.error(f"Error creating table of contents: {e}")

def main():
    """Main entry point for the scraper"""
    global page_workers, image_workers
    
    start_time = time.time()
    
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    
    # Parse command line arguments
    args = parse_arguments()
    
    # Configure logging
    setup_logging(args.log_level)
    
    # Load configuration
    load_config(args.config)
    
    # Apply command line overrides
    apply_command_line_overrides(args)
    
    # Create directories
    setup_directories()
    
    # Set up starting URL
    start_url = args.start_url or BASE_URL
    logging.info(f"Starting URL: {start_url}")
    
    # Add starting URL to queue
    page_queue.put((start_url, 0))
    queued_urls.add(start_url)
    
    # Create workers
    page_workers = []
    for i in range(WORKER_THREADS):
        worker = threading.Thread(target=page_scraper_worker, name=f"page-worker-{i}")
        worker.daemon = True
        worker.start()
        page_workers.append(worker)
    
    # Create image workers if not disabled
    image_workers = []
    if not args.no_images:
        for i in range(IMAGE_THREADS):
            worker = threading.Thread(target=image_downloader_worker, name=f"image-worker-{i}")
            worker.daemon = True
            worker.start()
            image_workers.append(worker)
    
    # Monitor progress
    def monitor_progress():
        last_processed = 0
        last_image_count = 0
        last_image_update_time = time.time()
        stalled_time = 0
        
        while not stop_event.is_set():
            try:
                time.sleep(10)  # Update every 10 seconds
                current_time = time.time()
                
                with metadata_lock:
                    current_processed = processed_pages
                    current_image_count = image_counter
                    new_pages = current_processed - last_processed
                    new_images = current_image_count - last_image_count
                    last_processed = current_processed
                    
                    if new_pages > 0:
                        pages_per_second = new_pages / 10
                        logging.info(f"Progress: {current_processed} pages processed " +
                                    f"({pages_per_second:.2f} pages/sec)")
                    
                    # Log active threads for debugging
                    active_page_workers = sum(1 for t in page_workers if t.is_alive())
                    active_image_workers = sum(1 for t in image_workers if t.is_alive())
                    logging.info(f"Active workers: {active_page_workers} page, {active_image_workers} image")
                    
                    # Report queue status
                    logging.info(f"Queue stats: Pages={page_queue.qsize()}, Images={image_queue.qsize()}")
                    logging.info(f"Images: {image_counter}/{total_images} downloaded, {failed_images} failed")
                    
                    # Check for stalled image downloads
                    if current_image_count > 0 and current_image_count < total_images:
                        if new_images > 0:
                            # Reset stalled time if making progress
                            last_image_count = current_image_count
                            last_image_update_time = current_time
                            stalled_time = 0
                        else:
                            # Calculate stalled time
                            stalled_time = int(current_time - last_image_update_time)
                            
                            # If stalled for more than 5 minutes and we've downloaded at least 90% of images
                            if stalled_time > 300 and current_image_count >= (total_images * 0.9):
                                logging.warning(f"Image downloading stalled for {stalled_time} seconds")
                                logging.warning(f"Downloaded {current_image_count}/{total_images} images ({current_image_count/total_images:.1%})")
                                logging.warning("More than 90% of images downloaded, continuing with processing")
                                # Force completion by setting stop event
                                stop_event.set()
                                break
                            elif stalled_time > 600:  # 10 minutes
                                logging.warning(f"Image downloading stalled for {stalled_time} seconds")
                                logging.warning("Forcing completion after 10 minutes of no progress")
                                stop_event.set()
                                break
                
                # Check if all processing is complete
                if current_processed > 0:
                    # All page workers done and either all images done or close enough
                    if (all(not t.is_alive() for t in page_workers) and 
                            (current_image_count >= total_images * 0.95 or 
                             all(not t.is_alive() for t in image_workers))):
                        logging.info("All workers finished or sufficient progress made")
                        stop_event.set()
                        break
                    
                    # Page queue empty and image queue empty or almost done with images
                    elif (page_queue.empty() and
                          (image_queue.empty() or current_image_count >= total_images * 0.95)):
                        logging.info("All queues empty or near completion, finishing up...")
                        stop_event.set()
                        break
                    
            except Exception as e:
                logging.error(f"Error in monitor thread: {e}")
    
    # Start progress monitor
    monitor_thread = threading.Thread(target=monitor_progress, name="monitor-thread")
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        # Wait for all tasks to complete or timeout
        completion_timeout = 3600  # 1 hour max
        completion_start = time.time()
        
        if not args.test:
            try:
                # Wait for page workers to finish with timeout
                while any(t.is_alive() for t in page_workers) and time.time() - completion_start < completion_timeout:
                    # Check every 5 seconds
                    for t in page_workers:
                        t.join(timeout=5)
                        if stop_event.is_set():
                            break
                    if stop_event.is_set():
                        break
                
                # Wait for image workers with timeout, but only if we have a reasonable number of pages
                if not args.no_images and processed_pages > 0:
                    image_timeout = min(600, completion_timeout - (time.time() - completion_start))  # Max 10 minutes or remaining time
                    image_timeout_start = time.time()
                    
                    while (any(t.is_alive() for t in image_workers) and 
                           time.time() - image_timeout_start < image_timeout and
                           not stop_event.is_set()):
                        # Check every 5 seconds
                        for t in image_workers:
                            t.join(timeout=5)
                            if stop_event.is_set():
                                break
                        if stop_event.is_set():
                            break
            except KeyboardInterrupt:
                logging.info("Keyboard interrupt received, stopping gracefully...")
                stop_event.set()
        else:
            # In test mode, just process a few pages then stop
            time.sleep(30)
            stop_event.set()
        
        # Signal all queues to finish for any remaining workers
        if not stop_event.is_set():
            stop_event.set()
        
        # Try to finalize the TOC and metadata
        try:
            # Create table of contents
            create_toc()
            
            # Save metadata
            save_metadata()
        except Exception as e:
            logging.error(f"Error finalizing: {e}")
        
        # Report results
        duration = time.time() - start_time
        logging.info(f"Scraper completed in {duration:.2f} seconds")
        logging.info(f"Pages: {processed_pages} processed, {error_pages} errors")
        logging.info(f"Images: {image_counter}/{total_images} downloaded, {failed_images} failed")
        logging.info(f"Skipped URLs: {len(skipped_urls)}")
        
    except KeyboardInterrupt:
        logging.info("Keyboard interrupt received, shutting down...")
        stop_event.set()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        # Make sure stop event is set
        stop_event.set()
        
        # Save current progress
        try:
            save_metadata()
            # Create TOC even if we had an error
            create_toc()
        except Exception as e:
            logging.error(f"Error in final cleanup: {e}")
            
        logging.info("Scraper finished")

if __name__ == "__main__":
    main() 