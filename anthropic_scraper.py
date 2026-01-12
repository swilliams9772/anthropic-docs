#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Anthropic Documentation Scraper v4 (Playwright Edition)
--------------------------------------------------------
This script scrapes the Anthropic API documentation using Playwright
for full JavaScript/React support on the new platform.claude.com site.

Key features:
- Playwright for JavaScript rendering
- Clean filename generation
- Better content extraction
- Enhanced markdown formatting
- Multi-language support (English focus)
"""

import os
import re
import time
import json
import asyncio
import logging
import hashlib
import urllib.parse
from urllib.parse import urljoin, urlparse
import sys
from datetime import datetime

from bs4 import BeautifulSoup
from markdownify import markdownify as md_convert

# Check for Playwright
try:
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    print("Playwright not installed. Installing...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "playwright"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
    from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout

# Configuration
ROOT_URL = "https://platform.claude.com"
BASE_URL = "https://platform.claude.com"
ALLOWED_DOMAINS = ["platform.claude.com", "support.claude.com"]
OUTPUT_DIR = "anthropic_docs"
HTML_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_html")
MD_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_md")
IMAGES_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_images")
FULL_HTML_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_full_html")
METADATA_FILE = os.path.join(OUTPUT_DIR, "page_metadata.json")
LOG_FILE = "scraper_v4.log"

# Scraping settings
MAX_CONCURRENT = 3  # Concurrent browser pages
REQUEST_DELAY = 1.0  # Delay between requests
PAGE_TIMEOUT = 30000  # 30 seconds
MAX_CRAWL_DEPTH = 10
LANGUAGES = ["en"]  # Focus on English only, add "es", "de", etc. if needed

# Excluded patterns
EXCLUDED_PATTERNS = [
    '/login', '/signup', '/feedback', '/legal', '/privacy', '/terms',
    'twitter.com', 'github.com', 'linkedin.com', 'facebook.com',
    'instagram.com', 'youtube.com', 'mailto:', 'discord.com',
    'console.anthropic.com', 'claude.ai/chat', '/settings',
]

# Global state
visited_urls = set()
queued_urls = set()
page_metadata = {}
processed_pages = 0
error_pages = 0


def setup_directories():
    """Create necessary directories"""
    for directory in [OUTPUT_DIR, HTML_DIR, MD_DIR, IMAGES_DIR, FULL_HTML_DIR]:
        os.makedirs(directory, exist_ok=True)


def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )


def clean_filename(url):
    """Convert URL to a clean, descriptive filename"""
    parsed_url = urlparse(url)
    path = parsed_url.path.strip('/')
    
    if not path:
        return "index"
    
    # Remove /docs/ prefix and language codes for cleaner names
    path = re.sub(r'^docs/', '', path)
    
    # Convert path to filename
    filename = path.replace('/', '_')
    
    # Remove query parameters and fragments
    filename = filename.split('?')[0].split('#')[0]
    
    # Decode URL encoding
    filename = urllib.parse.unquote(filename)
    
    # Clean up filename
    filename = re.sub(r'[^a-zA-Z0-9_.-]', '_', filename)
    filename = re.sub(r'_+', '_', filename)
    filename = filename.strip('_')
    
    if not filename or filename == '_':
        url_hash = hashlib.md5(url.encode('utf-8')).hexdigest()[:8]
        filename = f"page_{url_hash}"
    
    if len(filename) > 100:
        filename = filename[:100]
    
    return filename


def is_valid_url(url):
    """Check if a URL should be crawled"""
    parsed_url = urlparse(url)
    
    # Only crawl URLs on allowed domains
    if parsed_url.netloc not in ALLOWED_DOMAINS:
        return False
    
    # Skip excluded patterns
    for pattern in EXCLUDED_PATTERNS:
        if pattern in url.lower():
            return False
    
    path = parsed_url.path.lower()
    
    # For platform.claude.com, focus on /docs/ paths
    if parsed_url.netloc == "platform.claude.com":
        if not path.startswith('/docs/'):
            return False
        # Focus on specified languages
        lang_match = re.match(r'^/docs/([a-z]{2})/', path)
        if lang_match and lang_match.group(1) not in LANGUAGES:
            return False
    
    # For support.claude.com, include /en/ paths
    if parsed_url.netloc == "support.claude.com":
        if not path.startswith('/en/'):
            return False
    
    return True


def extract_main_content(soup, url):
    """Extract the main content from the page"""
    
    # Remove unwanted elements
    unwanted_selectors = [
        'nav', 'header', 'footer',
        '.navbar', '.navigation', '.nav-wrapper',
        '.sidebar', '.aside', '.toc',
        '.breadcrumb', '.pagination',
        '.cookie-banner', '.announcement',
        'script', 'style', 'noscript',
        '[data-testid="sidebar"]',
        '[data-testid="navbar"]',
        '.DocSearch',
        '.intercom-lightweight-app',
    ]
    
    for selector in unwanted_selectors:
        for element in soup.select(selector):
            element.decompose()
    
    # Try to find main content
    content_selectors = [
        'main article',
        'main .prose',
        'main [data-testid="doc-content"]',
        'main .markdown',
        'main .content',
        '[role="main"]',
        'main',
        'article',
        '.content',
        '.main-content',
    ]
    
    content = None
    for selector in content_selectors:
        elements = soup.select(selector)
        for element in elements:
            text_content = element.get_text(strip=True)
            if len(text_content) > 200:
                content = element
                break
        if content:
            break
    
    if not content:
        content = soup.body if soup.body else soup
    
    return content


def improve_markdown(markdown_content, url, title=""):
    """Improve the markdown formatting"""
    if not markdown_content:
        return ""
    
    # Add page header
    header = f"# {title}\n\n" if title and title != "Untitled" else ""
    header += f"**Source:** {url}\n\n"
    
    markdown_content = header + markdown_content
    
    # Fix multiple consecutive newlines
    markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)
    
    # Fix header formatting
    markdown_content = re.sub(r'^#+\s*#+\s*', '# ', markdown_content, flags=re.MULTILINE)
    
    # Clean up HTML comments
    markdown_content = re.sub(r'<!--.*?-->', '', markdown_content, flags=re.DOTALL)
    
    # Remove excessive whitespace
    markdown_content = re.sub(r'[ \t]+\n', '\n', markdown_content)
    
    # Ensure single newline at end
    markdown_content = markdown_content.rstrip() + '\n'
    
    return markdown_content


async def fetch_page_with_playwright(page, url, retries=2):
    """Fetch a page using Playwright with retries"""
    for attempt in range(retries + 1):
        try:
            # Navigate to the page
            response = await page.goto(url, wait_until='networkidle', timeout=PAGE_TIMEOUT)
            
            if response is None:
                logging.warning(f"No response for {url}")
                return None
            
            if response.status >= 400:
                logging.warning(f"HTTP {response.status} for {url}")
                return None
            
            # Wait for content to load
            await page.wait_for_load_state('networkidle')
            
            # Additional wait for React/JS content
            await asyncio.sleep(1)
            
            # Try to wait for main content
            try:
                await page.wait_for_selector('main', timeout=5000)
            except:
                pass
            
            # Get the rendered HTML
            html_content = await page.content()
            return html_content
            
        except PlaywrightTimeout:
            logging.warning(f"Timeout for {url} (attempt {attempt + 1})")
            if attempt < retries:
                await asyncio.sleep(2)
        except Exception as e:
            logging.warning(f"Error fetching {url}: {e} (attempt {attempt + 1})")
            if attempt < retries:
                await asyncio.sleep(2)
    
    return None


async def process_page(page, url, depth=0):
    """Process a single page"""
    global processed_pages, error_pages
    
    if depth > MAX_CRAWL_DEPTH:
        return False, []
    
    if url in visited_urls:
        return True, []
    
    if not is_valid_url(url):
        return False, []
    
    visited_urls.add(url)
    
    # Fetch the content
    html_content = await fetch_page_with_playwright(page, url)
    if not html_content:
        error_pages += 1
        return False, []
    
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Extract title
        title = "Untitled"
        if soup.title:
            title = soup.title.get_text().strip()
            title = re.sub(r'\s*[-|]\s*.*$', '', title).strip()
        elif soup.find('h1'):
            title = soup.find('h1').get_text().strip()
        
        # Generate filename
        filename = clean_filename(url)
        
        # Extract main content
        content = extract_main_content(soup, url)
        
        if not content:
            logging.warning(f"No content found for {url}")
            error_pages += 1
            return False, []
        
        content_text = content.get_text(strip=True)
        if len(content_text) < 100:
            logging.warning(f"Insufficient content for {url} ({len(content_text)} chars)")
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
        improved_markdown = improve_markdown(markdown_content, url, title)
        
        # Save Markdown
        md_file = os.path.join(MD_DIR, f"{filename}.md")
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(improved_markdown)
        
        # Find new links
        new_links = []
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if not href or href.startswith('#') or href.startswith('mailto:'):
                continue
            
            absolute_url = urljoin(url, href)
            # Normalize URL (remove trailing slash, fragments)
            absolute_url = absolute_url.split('#')[0].rstrip('/')
            
            if is_valid_url(absolute_url) and absolute_url not in visited_urls and absolute_url not in queued_urls:
                new_links.append(absolute_url)
                queued_urls.add(absolute_url)
        
        # Update metadata
        page_metadata[url] = {
            'title': title,
            'filename': filename,
            'url': url,
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'content_length': len(improved_markdown),
            'content_text_length': len(content_text),
            'depth': depth,
            'links_found': len(new_links)
        }
        
        processed_pages += 1
        logging.info(f"[{processed_pages}] {title} -> {filename}.md ({len(content_text)} chars)")
        
        return True, new_links
        
    except Exception as e:
        error_pages += 1
        logging.error(f"Error processing {url}: {e}")
        import traceback
        logging.error(traceback.format_exc())
        return False, []


async def crawl_with_playwright():
    """Main crawl function using Playwright"""
    global processed_pages, error_pages
    
    # Starting URLs for platform.claude.com
    start_urls = [
        # Main documentation sections
        "https://platform.claude.com/docs/en/home",
        "https://platform.claude.com/docs/en/intro",
        "https://platform.claude.com/docs/en/api/overview",
        "https://platform.claude.com/docs/en/api/messages",
        "https://platform.claude.com/docs/en/api/messages/create",
        "https://platform.claude.com/docs/en/api/messages/count_tokens",
        "https://platform.claude.com/docs/en/api/messages-batches",
        "https://platform.claude.com/docs/en/api/admin-api",
        "https://platform.claude.com/docs/en/about-claude/models/overview",
        "https://platform.claude.com/docs/en/about-claude/pricing",
        "https://platform.claude.com/docs/en/about-claude/glossary",
        # Build with Claude
        "https://platform.claude.com/docs/en/build-with-claude/overview",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-caching",
        "https://platform.claude.com/docs/en/build-with-claude/vision",
        "https://platform.claude.com/docs/en/build-with-claude/pdf-support",
        "https://platform.claude.com/docs/en/build-with-claude/extended-thinking",
        "https://platform.claude.com/docs/en/build-with-claude/streaming",
        "https://platform.claude.com/docs/en/build-with-claude/batch-processing",
        "https://platform.claude.com/docs/en/build-with-claude/citations",
        "https://platform.claude.com/docs/en/build-with-claude/token-counting",
        "https://platform.claude.com/docs/en/build-with-claude/embeddings",
        "https://platform.claude.com/docs/en/build-with-claude/files",
        # Prompt Engineering
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/system-prompts",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/multishot-prompting",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-of-thought",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/chain-prompts",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/extended-thinking-tips",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prefill-claudes-response",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/be-clear-and-direct",
        "https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/use-xml-tags",
        # Agents and Tools
        "https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview",
        "https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use",
        "https://platform.claude.com/docs/en/agents-and-tools/computer-use",
        "https://platform.claude.com/docs/en/agents-and-tools/mcp",
        "https://platform.claude.com/docs/en/agents-and-tools/mcp-connector",
        "https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers",
        "https://platform.claude.com/docs/en/agents-and-tools/claude-for-sheets",
        "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview",
        # Agent SDK
        "https://platform.claude.com/docs/en/agent-sdk/quickstart",
        "https://platform.claude.com/docs/en/agent-sdk/overview",
        "https://platform.claude.com/docs/en/agent-sdk/python",
        "https://platform.claude.com/docs/en/agent-sdk/typescript",
        # Claude Code
        "https://platform.claude.com/docs/en/claude-code/overview",
        "https://platform.claude.com/docs/en/claude-code/quickstart",
        "https://platform.claude.com/docs/en/claude-code/cli-reference",
        "https://platform.claude.com/docs/en/claude-code/ide-integrations",
        "https://platform.claude.com/docs/en/claude-code/memory",
        "https://platform.claude.com/docs/en/claude-code/settings",
        "https://platform.claude.com/docs/en/claude-code/mcp",
        "https://platform.claude.com/docs/en/claude-code/hooks",
        "https://platform.claude.com/docs/en/claude-code/sdk",
        "https://platform.claude.com/docs/en/claude-code/github-actions",
        "https://platform.claude.com/docs/en/claude-code/amazon-bedrock",
        "https://platform.claude.com/docs/en/claude-code/google-vertex-ai",
        # Test and Evaluate
        "https://platform.claude.com/docs/en/test-and-evaluate/overview",
        "https://platform.claude.com/docs/en/test-and-evaluate/define-success",
        "https://platform.claude.com/docs/en/test-and-evaluate/develop-tests",
        "https://platform.claude.com/docs/en/test-and-evaluate/eval-tool",
        "https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations",
        # Resources
        "https://platform.claude.com/docs/en/resources/overview",
        "https://platform.claude.com/docs/en/resources/glossary",
        "https://platform.claude.com/docs/en/resources/model-card",
        "https://platform.claude.com/docs/en/resources/system-status",
        "https://platform.claude.com/docs/en/resources/prompt-library/library",
        # Release Notes
        "https://platform.claude.com/docs/en/release-notes/overview",
        "https://platform.claude.com/docs/en/release-notes/api",
        "https://platform.claude.com/docs/en/release-notes/claude-apps",
        "https://platform.claude.com/docs/en/release-notes/claude-code",
        "https://platform.claude.com/docs/en/release-notes/system-prompts",
        # Third-party platforms
        "https://platform.claude.com/docs/en/third-party-platforms/claude-on-amazon-bedrock",
        "https://platform.claude.com/docs/en/third-party-platforms/claude-on-vertex-ai",
    ]
    
    logging.info(f"Starting Playwright-based scraper with {len(start_urls)} seed URLs")
    
    async with async_playwright() as p:
        # Launch browser
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )
        
        # Create pages for concurrent processing
        pages = [await context.new_page() for _ in range(MAX_CONCURRENT)]
        
        # Initialize queue with start URLs
        url_queue = [(url, 0) for url in start_urls]  # (url, depth)
        for url in start_urls:
            queued_urls.add(url)
        
        try:
            while url_queue:
                # Process batch of URLs
                batch = []
                while url_queue and len(batch) < MAX_CONCURRENT:
                    batch.append(url_queue.pop(0))
                
                # Process batch concurrently
                tasks = []
                for i, (url, depth) in enumerate(batch):
                    page = pages[i % len(pages)]
                    tasks.append(process_page(page, url, depth))
                
                results = await asyncio.gather(*tasks)
                
                # Add new links to queue
                for success, new_links in results:
                    for link in new_links:
                        url_queue.append((link, depth + 1))
                
                # Progress update
                queue_size = len(url_queue)
                logging.info(f"Progress: {processed_pages} processed, {queue_size} queued, {error_pages} errors")
                
                # Rate limiting
                await asyncio.sleep(REQUEST_DELAY)
                
        except KeyboardInterrupt:
            logging.info("Interrupted by user")
        finally:
            await browser.close()
    
    # Save metadata
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(page_metadata, f, indent=2, ensure_ascii=False)
    
    logging.info(f"Scraping completed!")
    logging.info(f"Pages processed: {processed_pages}")
    logging.info(f"Pages with errors: {error_pages}")
    logging.info(f"Total URLs visited: {len(visited_urls)}")


def main():
    """Main function"""
    setup_directories()
    setup_logging()
    
    logging.info("=" * 60)
    logging.info("Anthropic Documentation Scraper v4 (Playwright Edition)")
    logging.info("=" * 60)
    
    # Run the async crawler
    asyncio.run(crawl_with_playwright())


if __name__ == "__main__":
    main()
