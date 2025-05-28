#!/bin/bash

# Improved Anthropic Documentation Scraper Runner v3
# This script cleans up old files and runs the significantly improved scraper

echo "🚀 Starting Improved Anthropic Documentation Scraper v3"
echo "=================================================="
echo "Key improvements in v3:"
echo "  ✅ Clean filenames (no .html.md extensions)"
echo "  ✅ Better content extraction (removes navigation)"
echo "  ✅ Enhanced markdown formatting"
echo "  ✅ Improved URL handling"
echo ""

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
rm -f scraper.log scraper_run.log scraper_stdout.log scraper_v2.log scraper_v3.log scraper_v2_run.log scraper_v3_run.log

# Create fresh directories
echo "📁 Creating fresh directories..."
mkdir -p anthropic_docs/{anthropic_docs_html,anthropic_docs_md,anthropic_docs_images,anthropic_docs_full_html}

# Run the improved scraper v3
echo "🔄 Running improved scraper v3..."
echo "   Start time: $(date)"
echo "   Log file: scraper_v3.log"
echo ""

# Run with output to both console and log file
python3 improved_scraper_v3.py 2>&1 | tee scraper_v3_run.log

# Check if scraper completed successfully
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Scraper v3 completed successfully!"
    
    # Show statistics
    echo ""
    echo "📊 Scraping Statistics:"
    echo "======================"
    
    if [ -d "anthropic_docs/anthropic_docs_md" ]; then
        md_count=$(find anthropic_docs/anthropic_docs_md -name "*.md" | wc -l)
        echo "   Markdown files (.md): $md_count"
        
        # Show some example filenames
        echo ""
        echo "📄 Example filenames (first 10):"
        find anthropic_docs/anthropic_docs_md -name "*.md" | head -10 | while read file; do
            basename "$file"
        done | sed 's/^/     /'
    fi
    
    if [ -d "anthropic_docs/anthropic_docs_html" ]; then
        html_count=$(find anthropic_docs/anthropic_docs_html -name "*.html" | wc -l)
        echo ""
        echo "   HTML files: $html_count"
    fi
    
    if [ -d "anthropic_docs/anthropic_docs_full_html" ]; then
        full_html_count=$(find anthropic_docs/anthropic_docs_full_html -name "*.html" | wc -l)
        echo "   Full HTML files: $full_html_count"
    fi
    
    if [ -f "anthropic_docs/page_metadata.json" ]; then
        echo "   Metadata file: ✅ Created"
        
        # Show content quality stats from metadata
        if command -v python3 >/dev/null 2>&1; then
            echo ""
            echo "📈 Content Quality Stats:"
            python3 -c "
import json
try:
    with open('anthropic_docs/page_metadata.json', 'r') as f:
        data = json.load(f)
    
    lengths = [item['content_text_length'] for item in data.values()]
    if lengths:
        avg_length = sum(lengths) / len(lengths)
        min_length = min(lengths)
        max_length = max(lengths)
        print(f'   Average content length: {avg_length:.0f} characters')
        print(f'   Min content length: {min_length} characters')
        print(f'   Max content length: {max_length} characters')
        print(f'   Total pages with substantial content: {len(lengths)}')
except:
    pass
"
        fi
    fi
    
    # Show total size
    if [ -d "anthropic_docs" ]; then
        total_size=$(du -sh anthropic_docs | cut -f1)
        echo ""
        echo "   Total size: $total_size"
    fi
    
    echo ""
    echo "📁 Output directories:"
    echo "   📄 Markdown (.md files): anthropic_docs/anthropic_docs_md/"
    echo "   🌐 HTML: anthropic_docs/anthropic_docs_html/"
    echo "   📋 Full HTML: anthropic_docs/anthropic_docs_full_html/"
    echo "   🖼️  Images: anthropic_docs/anthropic_docs_images/"
    echo "   📊 Metadata: anthropic_docs/page_metadata.json"
    
    echo ""
    echo "🎉 Documentation scraping v3 completed successfully!"
    echo "   Key improvements:"
    echo "   ✅ Clean filenames without .html.md extensions"
    echo "   ✅ Better content quality (navigation filtered out)"
    echo "   ✅ Enhanced markdown formatting with titles and sources"
    echo "   ✅ Improved URL handling and validation"
    echo ""
    echo "   End time: $(date)"
    
else
    echo ""
    echo "❌ Scraper v3 failed with exit code $?"
    echo "   Check scraper_v3.log and scraper_v3_run.log for details"
    exit 1
fi 