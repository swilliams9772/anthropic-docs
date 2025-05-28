#!/bin/bash

# Improved Anthropic Documentation Scraper Runner v2
# This script cleans up old files and runs the improved scraper

echo "🚀 Starting Improved Anthropic Documentation Scraper v2"
echo "=================================================="

# Check if Python dependencies are installed
echo "📦 Checking dependencies..."
python3 -c "import requests, bs4, markdownify, PIL" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Missing dependencies. Installing..."
    pip3 install requests beautifulsoup4 markdownify pillow pyyaml
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies. Please install manually:"
        echo "   pip3 install requests beautifulsoup4 markdownify pillow pyyaml"
        exit 1
    fi
fi

# Clean up old documentation files
echo "🧹 Cleaning up old documentation files..."
if [ -d "anthropic_docs" ]; then
    echo "   Removing old anthropic_docs directory..."
    rm -rf anthropic_docs
fi

# Remove old log files
echo "   Removing old log files..."
rm -f scraper.log scraper_run.log scraper_stdout.log scraper_v2.log

# Create fresh directories
echo "📁 Creating fresh directories..."
mkdir -p anthropic_docs/{anthropic_docs_html,anthropic_docs_md,anthropic_docs_images,anthropic_docs_full_html}

# Run the improved scraper
echo "🔄 Running improved scraper..."
echo "   Start time: $(date)"
echo "   Log file: scraper_v2.log"
echo ""

# Run with output to both console and log file
python3 improved_scraper_v2.py 2>&1 | tee scraper_v2_run.log

# Check if scraper completed successfully
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Scraper completed successfully!"
    
    # Show statistics
    echo ""
    echo "📊 Scraping Statistics:"
    echo "======================"
    
    if [ -d "anthropic_docs/anthropic_docs_md" ]; then
        md_count=$(find anthropic_docs/anthropic_docs_md -name "*.md" | wc -l)
        echo "   Markdown files: $md_count"
    fi
    
    if [ -d "anthropic_docs/anthropic_docs_html" ]; then
        html_count=$(find anthropic_docs/anthropic_docs_html -name "*.html" | wc -l)
        echo "   HTML files: $html_count"
    fi
    
    if [ -d "anthropic_docs/anthropic_docs_full_html" ]; then
        full_html_count=$(find anthropic_docs/anthropic_docs_full_html -name "*.html" | wc -l)
        echo "   Full HTML files: $full_html_count"
    fi
    
    if [ -f "anthropic_docs/page_metadata.json" ]; then
        echo "   Metadata file: ✅ Created"
    fi
    
    # Show total size
    if [ -d "anthropic_docs" ]; then
        total_size=$(du -sh anthropic_docs | cut -f1)
        echo "   Total size: $total_size"
    fi
    
    echo ""
    echo "📁 Output directories:"
    echo "   📄 Markdown: anthropic_docs/anthropic_docs_md/"
    echo "   🌐 HTML: anthropic_docs/anthropic_docs_html/"
    echo "   📋 Full HTML: anthropic_docs/anthropic_docs_full_html/"
    echo "   🖼️  Images: anthropic_docs/anthropic_docs_images/"
    echo "   📊 Metadata: anthropic_docs/page_metadata.json"
    
    echo ""
    echo "🎉 Documentation scraping completed successfully!"
    echo "   End time: $(date)"
    
else
    echo ""
    echo "❌ Scraper failed with exit code $?"
    echo "   Check scraper_v2.log and scraper_v2_run.log for details"
    exit 1
fi 