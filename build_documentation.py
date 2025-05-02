#!/usr/bin/env python3
import os
import argparse
import subprocess
import time
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("build_docs.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Build Anthropic documentation",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--output-dir", 
        default="anthropic_docs_standalone_html",
        help="Output directory for final documentation"
    )
    parser.add_argument(
        "--scrape", 
        action="store_true", 
        help="Scrape the documentation from the web"
    )
    parser.add_argument(
        "--theme", 
        choices=["light", "dark", "auto"], 
        default="auto",
        help="Theme for the generated documentation"
    )
    parser.add_argument(
        "--optimize-images", 
        action="store_true", 
        help="Optimize images for web"
    )
    parser.add_argument(
        "--skip-convert", 
        action="store_true", 
        help="Skip conversion to HTML (only scrape)"
    )
    parser.add_argument(
        "--workers", 
        type=int, 
        default=4,
        help="Number of worker threads"
    )
    return parser.parse_args()

def run_scraper():
    """Run the web scraper script"""
    logger.info("Starting documentation scraper...")
    start_time = time.time()
    
    try:
        result = subprocess.run(
            ["python3", "scrape_anthropic_docs.py"],
            check=True,
            capture_output=True,
            text=True
        )
        logger.info(f"Scraper output: {result.stdout}")
        
        if result.stderr:
            logger.warning(f"Scraper warnings/errors: {result.stderr}")
            
        duration = time.time() - start_time
        logger.info(f"Scraping completed in {duration:.2f} seconds")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Scraper failed with exit code {e.returncode}: {e.stderr}")
        return False
    except Exception as e:
        logger.error(f"Error running scraper: {e}")
        return False

def run_converter(args):
    """Run the HTML converter script"""
    logger.info("Starting documentation converter...")
    start_time = time.time()
    
    cmd = [
        "python3", 
        "convert_to_pdf.py",
        "--output", args.output_dir,
        "--theme", args.theme,
        "--workers", str(args.workers)
    ]
    
    if args.optimize_images:
        cmd.append("--optimize-images")
    
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        logger.info(f"Converter output: {result.stdout}")
        
        if result.stderr:
            logger.warning(f"Converter warnings/errors: {result.stderr}")
            
        duration = time.time() - start_time
        logger.info(f"Conversion completed in {duration:.2f} seconds")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Converter failed with exit code {e.returncode}: {e.stderr}")
        return False
    except Exception as e:
        logger.error(f"Error running converter: {e}")
        return False

def check_requirements():
    """Check if required scripts and dependencies exist"""
    if not os.path.exists("scrape_anthropic_docs.py"):
        logger.error("scrape_anthropic_docs.py not found!")
        return False
        
    if not os.path.exists("convert_to_pdf.py"):
        logger.error("convert_to_pdf.py not found!")
        return False
    
    try:
        # Check if required packages are installed
        import requests
        import bs4
        import markdownify
        import jinja2
        import PIL
        import markdown
        import tqdm
        return True
    except ImportError as e:
        logger.error(f"Missing required package: {e}")
        logger.error("Please install required packages with: pip install requests beautifulsoup4 markdownify jinja2 pillow markdown tqdm")
        return False

def main():
    """Main function to run the documentation build process"""
    args = parse_args()
    
    logger.info("Starting Anthropic documentation build process...")
    
    if not check_requirements():
        return
    
    total_start_time = time.time()
    
    if args.scrape:
        if not run_scraper():
            logger.error("Documentation scraping failed. Stopping.")
            return
    else:
        logger.info("Skipping documentation scraping (use --scrape to enable)")
    
    if not args.skip_convert:
        if not run_converter(args):
            logger.error("Documentation conversion failed.")
            return
    else:
        logger.info("Skipping documentation conversion (--skip-convert flag used)")
    
    total_duration = time.time() - total_start_time
    logger.info(f"Documentation build completed in {total_duration:.2f} seconds")
    
    if not args.skip_convert:
        logger.info(f"Documentation is available at: {args.output_dir}/index.html")

if __name__ == "__main__":
    main() 