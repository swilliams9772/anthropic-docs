# Anthropic Documentation Scraper

A Python tool to scrape and convert the Anthropic API documentation into markdown and HTML formats.

## Features

- Scrapes the Anthropic API documentation website
- Converts HTML to clean, structured Markdown
- Downloads and optimizes images
- Handles code blocks with proper syntax highlighting
- Preserves API reference structure and formatting
- Supports multiple code examples (curl, Python, TypeScript)
- Properly extracts API parameters and their descriptions
- Multi-threaded for efficient downloading

## Installation

1. Clone this repository:
```bash
git clone https://github.com/swilliams9772/anthropic-docs.git
cd anthropic-docs
```

2. Install the requirements:
```bash
pip install -r requirements.txt
```

## Usage

### Improved Scraper (Recommended)

Run the improved scraper with better error handling, image optimization, and URL management:

```bash
python improved_scraper.py
```

Or use the convenient shell script to run everything in one step:

```bash
chmod +x run_improved_scraper.sh
./run_improved_scraper.sh
```

The improved scraper includes:

1. **Better Image Handling**: Properly detects and handles image formats
2. **More Robust URL Processing**: Improved normalization and validation of URLs  
3. **Enhanced Error Recovery**: Better handling of errors and retries for failed requests
4. **Smarter Content Extraction**: Improved detection of main content areas
5. **Cleaner Markdown Output**: Better conversion from HTML to Markdown
6. **Adaptive Rate Limiting**: Intelligently backs off when rate limits are encountered

### Options and Configurations

You can customize the scraper behavior using command-line arguments:

```bash
python improved_scraper.py --start-url https://docs.anthropic.com/en/api --threads 4 --image-threads 4 --delay 1.0
```

Available options:
- `--config`: Path to configuration file (default: config.yaml)
- `--start-url`: Starting URL to scrape (overrides config)
- `--output-dir`: Base directory for all output files
- `--threads`: Number of worker threads
- `--image-threads`: Number of image download threads
- `--delay`: Minimum delay between requests in seconds
- `--depth`: Maximum crawl depth
- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `--no-images`: Skip downloading images
- `--test`: Run in test mode (limited pages)

## Output Structure

The scraper generates the following directories:

- `anthropic_docs_html/`: Processed HTML files
- `anthropic_docs_md/`: Markdown versions of the documentation
- `anthropic_docs_images/`: Downloaded and optimized images
- `anthropic_docs_full_html/`: Original HTML content

## Configuration

The scraper's behavior can be customized by editing the `config.yaml` file:

```yaml
# URLs and paths
urls:
  root: "https://docs.anthropic.com"
  base: "https://docs.anthropic.com/en/api"
  domain: "docs.anthropic.com"
  path_prefix: "/en/api/"
  sections:
    - "/en/api/getting-started"
    - "/en/api/messages"
    # ...other sections...

# Rate limiting settings to avoid overloading the server
rate_limiting:
  max_requests_per_second: 5
  min_delay_between_requests: 0.5
  respect_robots_txt: true
  adaptive: true
  max_retries: 5
  base_retry_delay: 2.0
  max_retry_delay: 20.0
```

## Troubleshooting

If you encounter issues with the scraper:

1. Check the `scraper.log` file for detailed error messages
2. Try increasing the delay between requests (`--delay 2.0`)
3. Look at `skipped_urls.txt` to see which URLs were skipped
4. For image issues, try the `--no-images` flag to skip image processing

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Anthropic for their excellent API documentation
- Beautiful Soup library for HTML parsing
- Markdownify for HTML to Markdown conversion 