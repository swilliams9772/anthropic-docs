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

## Latest Improvements

- **Clean Markdown Structure**: Headers, sidebars, and navigation elements are removed from each file
- **Separate Navigation System**: Table of contents and sidebar navigation files for better organization
- **Enhanced API Parameter Formatting**: More readable formatting of parameters in documentation
- **Improved Content Extraction**: Better detection and isolation of main content
- **Adaptive Rate Limiting**: Intelligently backs off when rate limits are encountered
- **Clean File Names**: No more `.html.md` extensions or encoded characters in filenames
- **Quality Content Filtering**: Only substantial documentation content is included

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

### Main Scraper (Recommended)

Run the Anthropic documentation scraper with enhanced error handling, image optimization, and clean output:

```bash
python anthropic_scraper.py
```

Or use the convenient shell script to run everything in one step:

```bash
chmod +x run_scraper.sh
./run_scraper.sh
```

The scraper includes:

1. **Enhanced Content Quality**: Filters out navigation-heavy pages, ensuring substantial content
2. **Clean File Names**: Proper `.md` extensions without encoded characters
3. **Professional Formatting**: Clean markdown with titles and source URLs
4. **Better Image Handling**: Properly detects and handles image formats
5. **Robust URL Processing**: Improved normalization and validation of URLs  
6. **Enhanced Error Recovery**: Better handling of errors and retries for failed requests
7. **Adaptive Rate Limiting**: Intelligently backs off when rate limits are encountered

### Table of Contents Generation

Generate a table of contents and sidebar navigation to make browsing the documentation easier:

```bash
python generate_toc.py
```

This creates:
- `anthropic_docs/table_of_contents.md`: Main table of contents organized by category
- `anthropic_docs/sidebar.md`: Sidebar navigation for use with documentation viewers

### Options and Configurations

You can customize the scraper behavior using command-line arguments:

```bash
python anthropic_scraper.py --start-url https://docs.anthropic.com/en/api --threads 4 --image-threads 4 --delay 1.0
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
- `anthropic_docs_md/`: Markdown versions of the documentation (clean `.md` files)
- `anthropic_docs_images/`: Downloaded and optimized images
- `anthropic_docs_full_html/`: Original HTML content
- `page_metadata.json`: Comprehensive metadata about all scraped pages

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

## Quality Assurance

The current scraper ensures:

- ✅ **Clean filenames** - All files have proper `.md` extensions
- ✅ **Substantial content** - Minimum 200 characters of actual documentation content
- ✅ **Professional formatting** - Proper markdown structure with titles and source URLs
- ✅ **Navigation filtering** - Removes sidebar and navigation clutter
- ✅ **Error-free processing** - Robust error handling and recovery

## Troubleshooting

If you encounter issues with the scraper:

1. Check the `scraper_run.log` file for detailed error messages
2. Try increasing the delay between requests (`--delay 2.0`)
3. For image issues, try the `--no-images` flag to skip image processing

## Files in this Repository

### Main Tools
- `anthropic_scraper.py` - Main scraper with all improvements
- `run_scraper.sh` - Convenient shell script to run the scraper
- `generate_toc.py` - Generates table of contents and navigation
- `build_documentation.py` - Additional documentation processing
- `convert_to_pdf.py` - Converts documentation to PDF format

### Configuration
- `config.yaml` - Main configuration file
- `requirements.txt` - Python dependencies

### Documentation
- `README.md` - This file
- `SCRAPER_V3_RESULTS_SUMMARY.md` - Results summary of the latest scraper improvements
- `SCRAPER_ANALYSIS_AND_IMPROVEMENTS_V3.md` - Technical details of improvements
- `FINAL_REPORT.md` - Comprehensive analysis report

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Anthropic for their excellent API documentation
- Beautiful Soup library for HTML parsing
- Markdownify for HTML to Markdown conversion 