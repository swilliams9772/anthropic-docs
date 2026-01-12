import os
import time
import random
import requests
from urllib.parse import urljoin, urlparse
import logging
import sys

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15',
]

def check_url(url):
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
    }
    
    try:
        print(f"\nChecking {url}...")
        response = requests.get(url, headers=headers, timeout=30, allow_redirects=True)
        
        print(f"Status Code: {response.status_code}")
        print(f"Final URL: {response.url}")
        
        # Check for specific terms
        content = response.text.lower()
        terms = ["sonnet 4.5", "claude 4.5", "september"]
        
        found = False
        for term in terms:
            if term in content:
                print(f"✅ Found '{term}' in content")
                found = True
            else:
                print(f"❌ Did NOT find '{term}' in content")
                
        if not found:
            # Save content for inspection if nothing found
            filename = f"debug_{urlparse(url).path.strip('/').replace('/', '_')}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"Saved content to {filename}")
            
    except Exception as e:
        print(f"Error fetching {url}: {e}")

# URLs to check
urls_to_check = [
    "https://docs.anthropic.com/en/release-notes/api",
    "https://docs.anthropic.com/en/release-notes/overview",
    "https://docs.anthropic.com/en/docs/about-claude/models/overview",
    "https://platform.claude.com/docs/en/release-notes/api", # Direct new domain
]

if __name__ == "__main__":
    for url in urls_to_check:
        check_url(url)
        time.sleep(2)




