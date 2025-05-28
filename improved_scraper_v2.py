#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Improved Anthropic Documentation Scraper v2
-------------------------------------------
This script scrapes the Anthropic API documentation with improved content extraction,
better URL handling, and more robust error recovery.

Key improvements:
- Better content extraction for Anthropic's documentation structure
- Improved filename generation
- More robust URL filtering and validation
- Enhanced markdown conversion
- Better handling of navigation and duplicate content
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
from urllib.parse import urljoin, urlparse, unquote
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert
from PIL import Image, UnidentifiedImageError

# User agents for rotation
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
]

# Global configuration variables
CONFIG = {}
ROOT_URL = "https://docs.anthropic.com"
BASE_URL = "https://docs.anthropic.com"
API_DOMAIN = "docs.anthropic.com"
OUTPUT_DIR = "anthropic_docs"
HTML_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_html")
MD_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_md")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_images")
FULL_HTML_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_full_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "page_metadata.json")
WORKER_THREADS = 6
IMAGE_THREADS = 4
REQUEST_DELAY = 0.8
MAX_CRAWL_DEPTH = 8
LOG_FILE = "scraper_v2.log"
MAX_IMAGE_SIZE = 800
IMAGE_QUALITY = 85

# Excluded paths and patterns
EXCLUDED_EXTENSIONS = ['.pdf', '.zip', '.tar', '.gz', '.mp4', '.avi', '.mov', '.mpg', '.exe', '.dmg', '.pkg', '.js', '.css']
EXCLUDED_PATTERNS = [
    '/feedback', '/legal', '/privacy', '/terms', '/search', '/404',
    '?q=', '/api/v1/', 'twitter.com', 'github.com', 'linkedin.com',
    'facebook.com', 'instagram.com', 'youtube.com', 'mailto:',
    'discord.com', 'support.anthropic.com', 'console.anthropic.com',
    'claude.ai', 'anthropic.com/news', 'anthropic.com/legal',
    'anthropic.com/careers', 'anthropic.com/about'
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

def setup_directories():
    """Create necessary directories"""
    for directory in [OUTPUT_DIR, HTML_DIR, MD_DIR, IMAGES_DIR, FULL_HTML_DIR]:
        os.makedirs(directory, exist_ok=True)

def setup_logging(log_level="INFO"):
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def signal_handler(sig, frame):
    """Handle interrupt signals gracefully"""
    logging.info("Interrupt received, stopping scraper...")
    stop_event.set()

def fetch_url(url, max_retries=3, retry_delay=1, timeout=30):
    """Fetch URL with retries and rate limiting"""
    global last_request_time
    
    # Rate limiting
    with request_lock:
        current_time = time.time()
        time_since_last = current_time - last_request_time
        if time_since_last < REQUEST_DELAY:
            time.sleep(REQUEST_DELAY - time_since_last)
        last_request_time = time.time()
    
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
            
            if response.status_code == 200:
                return response.text
            elif response.status_code == 429:  # Rate limited
                wait_time = retry_delay * (2 ** attempt) + random.uniform(0, 1)
                logging.warning(f"Rate limited for {url}, waiting {wait_time:.2f}s")
                time.sleep(wait_time)
            elif response.status_code in [403, 404]:
                logging.warning(f"Access denied or not found for {url}: {response.status_code}")
                return None
            else:
                logging.warning(f"HTTP {response.status_code} for {url}")
                
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout for {url} (attempt {attempt + 1})")
        except requests.exceptions.RequestException as e:
            logging.warning(f"Request error for {url}: {e} (attempt {attempt + 1})")
        
        if attempt < max_retries - 1:
            wait_time = retry_delay * (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait_time)
    
    logging.error(f"Failed to fetch {url} after {max_retries} attempts")
    return None

def clean_filename(url):
    """Convert URL to a clean, descriptive filename"""
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    
    # Handle root URL
    if not path:
        return "index"
    
    # Remove common prefixes to make filenames cleaner
    prefixes_to_remove = [
        'en/api/',
        'en/docs/',
        'api/',
        'docs/',
    ]
    
    for prefix in prefixes_to_remove:
        if path.startswith(prefix):
            path = path[len(prefix):]
            break
    
    # Convert path to filename
    filename = path.replace('/', '_')
    
    # Remove query parameters and fragments
    filename = filename.split('?')[0].split('#')[0]
    
    # Clean up filename
    filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
    filename = re.sub(r'_+', '_', filename)  # Remove multiple underscores
    filename = filename.strip('_')
    
    # Ensure we have a valid filename
    if not filename or filename == '_':
        # Use a hash of the URL as fallback
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
        filename = f"page_{url_hash}"
    
    # Limit filename length
    if len(filename) > 100:
        filename = filename[:100]
    
    return filename

def is_valid_url(url):
    """Check if a URL should be crawled"""
    parsed_url = urlparse(url)
    
    # Only crawl URLs on the target domain
    if parsed_url.netloc != API_DOMAIN:
        return False
    
    # Skip excluded extensions
    path = parsed_url.path.lower()
    for ext in EXCLUDED_EXTENSIONS:
        if path.endswith(ext):
            return False
    
    # Skip URLs matching excluded patterns
    for pattern in EXCLUDED_PATTERNS:
        if pattern in url.lower():
            return False
    
    # Include documentation and API paths
    valid_paths = [
        '/en/docs/',
        '/en/api/',
        '/en/home',
        '/en/resources/',
        '/en/release-notes/',
    ]
    
    # Check if URL matches any valid path or is the root
    if path == '/' or path == '':
        return True
        
    return any(path.startswith(valid_path) for valid_path in valid_paths)

def extract_main_content(soup, url):
    """Extract the main content from the page with improved selectors for Anthropic docs"""
    
    # Remove unwanted elements first
    unwanted_selectors = [
        'nav', 'header', 'footer',
        '.navbar', '.navigation', '.nav-wrapper', '.top-bar',
        '.sidebar', '.aside', '.toc', '.table-of-contents',
        '.breadcrumb', '.pagination', '.edit-page-link',
        '.on-this-page', '.page-nav', '.prev-next-nav',
        '.cookie-banner', '.announcement', '.banner',
        '.social-share', '.related-articles',
        'script', 'style', 'noscript',
        # Anthropic-specific selectors
        '.navbar-sidebar', '.theme-doc-sidebar-container',
        '.sidebar-container', '.doc-sidebar',
        '[data-theme="navbar"]', '[data-theme="sidebar"]'
    ]
    
    for selector in unwanted_selectors:
        for element in soup.select(selector):
            element.decompose()
    
    # Try to find main content using various selectors
    content_selectors = [
        # Anthropic/Docusaurus specific
        '.theme-doc-markdown',
        '.markdown',
        'article[role="main"]',
        'main[role="main"]',
        '.main-wrapper main',
        '.docMainContainer',
        '.container .row .col',
        
        # Generic content selectors
        'main',
        'article',
        '.content',
        '.main-content',
        '.page-content',
        '.documentation',
        '.doc-content',
        '#main-content',
        '.post-content',
        '.entry-content',
        
        # Fallback selectors
        '.container',
        '#content',
        'body'
    ]
    
    content = None
    for selector in content_selectors:
        elements = soup.select(selector)
        for element in elements:
            text_content = element.get_text(strip=True)
            # Look for substantial content (more than just navigation)
            if len(text_content) > 200:
                content = element
                logging.debug(f"Found content using selector: {selector}")
                break
        if content:
            break
    
    if not content:
        # Last resort: use body but try to clean it up
        content = soup.body if soup.body else soup
        logging.debug("Using body as content (last resort)")
    
    # Additional cleanup within the content
    if content:
        # Remove any remaining navigation elements
        for element in content.select('.nav, .menu, .navigation'):
            element.decompose()
        
        # Remove empty elements
        for element in content.find_all():
            if not element.get_text(strip=True) and not element.find_all(['img', 'video', 'audio', 'iframe']):
                element.decompose()
        
        # Improve code blocks
        for pre in content.find_all('pre'):
            # Add language detection for better markdown conversion
            code_text = pre.get_text()
            if 'curl' in code_text.lower() or code_text.strip().startswith('curl'):
                pre['class'] = pre.get('class', []) + ['language-bash']
            elif code_text.strip().startswith('{') and code_text.strip().endswith('}'):
                pre['class'] = pre.get('class', []) + ['language-json']
            elif 'import ' in code_text or 'def ' in code_text:
                pre['class'] = pre.get('class', []) + ['language-python']
    
    return content

def improve_markdown(markdown_content, url):
    """Improve the markdown formatting"""
    if not markdown_content:
        return ""
    
    # Add page identifier at the top
    filename = clean_filename(url)
    markdown_content = f'<a id="{filename}.html"></a>\n\n{markdown_content}'
    
    # Fix multiple consecutive newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    # Fix header formatting
    markdown_content = re.sub(r'^#+\s*#+\s*', '# ', markdown_content, flags=re.MULTILINE)
    
    # Ensure proper spacing around headers
    markdown_content = re.sub(r'\n(#{1,6}\s+[^\n]+)\n(?!\n)', r'\n\1\n\n', markdown_content)
    
    # Fix list formatting
    markdown_content = re.sub(r'^\s{4,}([*\-+])', r'  \1', markdown_content, flags=re.MULTILINE)
    
    # Clean up any remaining HTML comments
    markdown_content = re.sub(r'<!--.*?-->', '', markdown_content, flags=re.DOTALL)
    
    # Remove excessive whitespace
    markdown_content = re.sub(r'[ \t]+\n', '\n', markdown_content)
    
    # Ensure the content ends with a single newline
    markdown_content = markdown_content.rstrip() + '\n'
    
    return markdown_content

def process_page(url, depth=0):
    """Process a single page"""
    global processed_pages, error_pages
    
    if stop_event.is_set():
        return False, []
    
    if depth > MAX_CRAWL_DEPTH:
        logging.debug(f"Maximum depth reached for URL: {url}")
        return False, []
        
    if url in visited_urls:
        logging.debug(f"URL already visited: {url}")
        return True, []
        
    if not is_valid_url(url):
        skipped_urls.add(url)
        logging.debug(f"Skipping URL: {url}")
        return False, []
    
    visited_urls.add(url)
    
    # Fetch the content
    html_content = fetch_url(url)
    if not html_content:
        error_pages += 1
        logging.error(f"Failed to fetch content for URL: {url}")
        return False, []
    
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract title
        title = "Untitled"
        if soup.title:
            title = soup.title.get_text().strip()
        elif soup.find('h1'):
            title = soup.find('h1').get_text().strip()
        
        # Generate filename
        filename = clean_filename(url)
        
        # Extract main content
        content = extract_main_content(soup, url)
        
        if not content or len(content.get_text(strip=True)) < 50:
            logging.warning(f"No substantial content found for {url}")
            error_pages += 1
            return False, []
        
        # Save full HTML
        full_html_file = os.path.join(FULL_HTML_DIR, f"{filename}.html")
        with open(full_html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        # Save processed HTML
        html_file = os.path.join(HTML_DIR, f"{filename}.html")
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(str(content))
        
        # Convert to Markdown
        markdown_content = md_convert(str(content), heading_style="ATX")
        improved_markdown_content = improve_markdown(markdown_content, url)
        
        # Save Markdown
        md_file = os.path.join(MD_DIR, f"{filename}.html.md")
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(improved_markdown_content)
        
        # Find new links
        new_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if not href or href.startswith('#') or href.startswith('mailto:'):
                continue
            
            absolute_url = urljoin(url, href)
            if is_valid_url(absolute_url) and absolute_url not in visited_urls and absolute_url not in queued_urls:
                new_links.append(absolute_url)
                queued_urls.add(absolute_url)
        
        # Update metadata
        with metadata_lock:
            page_metadata[url] = {
                'title': title,
                'filename': filename,
                'url': url,
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'content_length': len(improved_markdown_content),
                'depth': depth,
                'links_found': len(new_links)
            }
        
        processed_pages += 1
        logging.info(f"Processed page {processed_pages}: {title} ({url})")
        
        return True, new_links
        
    except Exception as e:
        error_pages += 1
        logging.error(f"Error processing page {url}: {e}")
        import traceback
        logging.error(traceback.format_exc())
        return False, []

def worker():
    """Worker thread function"""
    while not stop_event.is_set():
        try:
            url, depth = page_queue.get(timeout=1)
            success, new_links = process_page(url, depth)
            
            # Add new links to queue
            for link in new_links:
                if not stop_event.is_set():
                    page_queue.put((link, depth + 1))
            
            page_queue.task_done()
            
        except queue.Empty:
            continue
        except Exception as e:
            logging.error(f"Worker error: {e}")

def save_metadata():
    """Save metadata to file"""
    try:
        with open(METADATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(page_metadata, f, indent=2, ensure_ascii=False)
        logging.info(f"Saved metadata for {len(page_metadata)} pages")
    except Exception as e:
        logging.error(f"Error saving metadata: {e}")

def main():
    """Main function"""
    # Setup
    setup_directories()
    setup_logging()
    signal.signal(signal.SIGINT, signal_handler)
    
    # Starting URLs - comprehensive list for Anthropic docs
    start_urls = [
        "https://docs.anthropic.com/",
        "https://docs.anthropic.com/en/home",
        "https://docs.anthropic.com/en/docs/welcome",
        "https://docs.anthropic.com/en/api/getting-started",
        "https://docs.anthropic.com/en/api/messages",
        "https://docs.anthropic.com/en/docs/about-claude/models/overview",
        "https://docs.anthropic.com/en/docs/build-with-claude/overview",
        "https://docs.anthropic.com/en/docs/agents-and-tools/computer-use",
        "https://docs.anthropic.com/en/docs/test-and-evaluate/define-success",
        "https://docs.anthropic.com/en/docs/claude-code/overview",
        "https://docs.anthropic.com/en/release-notes/overview",
    ]
    
    # Add starting URLs to queue
    for url in start_urls:
        if url not in queued_urls:
            queued_urls.add(url)
            page_queue.put((url, 0))
    
    logging.info(f"Starting scraper with {len(start_urls)} initial URLs")
    logging.info(f"Using {WORKER_THREADS} worker threads")
    
    # Start worker threads
    threads = []
    for i in range(WORKER_THREADS):
        t = threading.Thread(target=worker, name=f"Worker-{i}")
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Monitor progress
    try:
        while not stop_event.is_set():
            queue_size = page_queue.qsize()
            if queue_size == 0 and all(not t.is_alive() for t in threads):
                break
            
            logging.info(f"Progress: {processed_pages} pages processed, {queue_size} in queue, {error_pages} errors")
            time.sleep(10)
            
    except KeyboardInterrupt:
        logging.info("Interrupted by user")
        stop_event.set()
    
    # Wait for completion
    logging.info("Waiting for workers to finish...")
    for t in threads:
        t.join(timeout=5)
    
    # Save final metadata
    save_metadata()
    
    # Final statistics
    logging.info(f"Scraping completed!")
    logging.info(f"Pages processed: {processed_pages}")
    logging.info(f"Pages with errors: {error_pages}")
    logging.info(f"URLs skipped: {len(skipped_urls)}")
    logging.info(f"Total URLs visited: {len(visited_urls)}")

if __name__ == "__main__":
    main() 