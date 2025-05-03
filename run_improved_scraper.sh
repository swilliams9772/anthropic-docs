#!/bin/bash

# run_improved_scraper.sh
# A script to run the improved Anthropic documentation scraper with enhanced markdown formatting
# Now with added timeout handling and better error recovery

# Set up colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Set timeout values (in seconds)
MAX_SCRAPER_RUNTIME=3600  # 1 hour max runtime
IMAGE_PROGRESS_TIMEOUT=300  # 5 minutes with no progress on images before force continue
STALL_CHECK_INTERVAL=30  # Check for stalls every 30 seconds

echo -e "${BLUE}===== Anthropic Documentation Scraper =====${NC}"
echo -e "${BLUE}This script will scrape the Anthropic API documentation and save it in HTML and Markdown formats.${NC}"
echo -e "${YELLOW}Enhanced features include improved markdown formatting, better code block detection, and organized navigation.${NC}"
echo -e "${YELLOW}Added timeout handling to prevent hanging on problematic image downloads.${NC}"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    exit 1
fi

# Check if required packages are installed
echo -e "${BLUE}Checking required packages...${NC}"
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo -e "${RED}Error installing required packages.${NC}"
    exit 1
fi

echo -e "${GREEN}All required packages are installed.${NC}"
echo ""

# Create directories if they don't exist
echo -e "${BLUE}Setting up directories...${NC}"
mkdir -p anthropic_docs/html anthropic_docs/md anthropic_docs/images anthropic_docs/full_html
echo -e "${GREEN}Directories created.${NC}"
echo ""

# Run the scraper in background so we can monitor it
echo -e "${BLUE}Starting the scraper...${NC}"
echo -e "${BLUE}(This may take several minutes depending on the size of the documentation)${NC}"
echo -e "${YELLOW}Timeout is set to ${MAX_SCRAPER_RUNTIME} seconds (${MAX_SCRAPER_RUNTIME/60} minutes)${NC}"
echo ""

# Start the scraper process
python3 improved_scraper.py --start-url https://docs.anthropic.com/en/api --threads 4 --image-threads 4 --delay 1.0 > scraper_stdout.log 2>&1 &
SCRAPER_PID=$!

# Track progress variables
start_time=$(date +%s)
last_line=""
last_image_count=0
last_image_progress_time=$(date +%s)
stalled=false

# Monitor progress function
monitor_progress() {
    local current_time=$(date +%s)
    local elapsed=$((current_time - start_time))
    local latest_log
    
    # Attempt to get the last few lines of the log
    if [ -f "scraper.log" ]; then
        latest_log=$(tail -n 1 scraper.log)
        
        # Check if we have a new log line
        if [ "$latest_log" != "$last_line" ] && [ -n "$latest_log" ]; then
            echo -e "${BLUE}$latest_log${NC}"
            last_line="$latest_log"
            
            # Check for image progress
            if [[ "$latest_log" =~ "Images: "([0-9]+)"/"([0-9]+) ]]; then
                local current_image_count=${BASH_REMATCH[1]}
                local total_image_count=${BASH_REMATCH[2]}
                
                # If image count changed, update the progress timestamp
                if [ "$current_image_count" != "$last_image_count" ]; then
                    last_image_count=$current_image_count
                    last_image_progress_time=$(date +%s)
                    stalled=false
                    echo -e "${GREEN}Image download progress: $current_image_count/$total_image_count${NC}"
                else
                    # Calculate time since last image progress
                    local stall_time=$((current_time - last_image_progress_time))
                    if [ $stall_time -gt $IMAGE_PROGRESS_TIMEOUT ] && [ "$stalled" = false ]; then
                        # Mark as stalled so we only warn once
                        stalled=true
                        echo -e "${YELLOW}WARNING: Image downloading appears to be stalled for over 5 minutes.${NC}"
                        echo -e "${YELLOW}Will continue with processing if no progress in the next few minutes.${NC}"
                        
                        # Check if we're substantially done with images (over 90%)
                        if [ $current_image_count -gt $((total_image_count * 9 / 10)) ]; then
                            echo -e "${YELLOW}Most images (${current_image_count}/${total_image_count}) have been downloaded.${NC}"
                            echo -e "${YELLOW}Continuing with processing...${NC}"
                            
                            # Send SIGINT to scraper to trigger graceful shutdown
                            kill -s SIGINT $SCRAPER_PID
                        fi
                    fi
                fi
            fi
        fi
    fi
    
    # Check if the runtime exceeds the maximum
    if [ $elapsed -gt $MAX_SCRAPER_RUNTIME ]; then
        echo -e "${RED}Maximum runtime exceeded. Stopping scraper...${NC}"
        kill -s SIGINT $SCRAPER_PID
    fi
}

# Monitor the process until it completes or times out
while kill -0 $SCRAPER_PID 2>/dev/null; do
    monitor_progress
    sleep $STALL_CHECK_INTERVAL
done

# Wait for the scraper to finish
wait $SCRAPER_PID
SCRAPER_EXIT_CODE=$?

# Generate table of contents and navigation
echo -e "${BLUE}Generating table of contents and navigation...${NC}"
python3 generate_toc.py

# Check if scraper completed successfully
if [ $SCRAPER_EXIT_CODE -eq 0 ] || [ -d "anthropic_docs/anthropic_docs_md" ]; then
    echo ""
    echo -e "${GREEN}Scraper completed with exit code: $SCRAPER_EXIT_CODE${NC}"
    echo -e "${GREEN}The documentation has been saved to the anthropic_docs directory:${NC}"
    echo -e "${GREEN}- HTML files: anthropic_docs/anthropic_docs_html/${NC}"
    echo -e "${GREEN}- Markdown files: anthropic_docs/anthropic_docs_md/${NC}"
    echo -e "${GREEN}- Full HTML files: anthropic_docs/anthropic_docs_full_html/${NC}"
    echo -e "${GREEN}- Images: anthropic_docs/anthropic_docs_images/${NC}"
    echo ""
    echo -e "${BLUE}Table of contents can be found at:${NC}"
    echo -e "${BLUE}- anthropic_docs/table_of_contents.md${NC}"
    echo -e "${BLUE}- anthropic_docs/sidebar.md${NC}"
    echo ""
    echo -e "${YELLOW}Markdown Features:${NC}"
    echo -e "${YELLOW}- Improved code block detection and language identification${NC}"
    echo -e "${YELLOW}- Clean header spacing and list indentation${NC}"
    echo -e "${YELLOW}- Removed headers, footers, sidebars, and navigation elements${NC}"
    echo -e "${YELLOW}- Separate navigation via table of contents${NC}"
    echo -e "${YELLOW}- API parameters converted to organized lists${NC}"
else
    echo ""
    echo -e "${RED}Scraper encountered errors (exit code: $SCRAPER_EXIT_CODE).${NC}"
    echo -e "${RED}Please check the scraper.log file for details.${NC}"
fi

# Count files to show summary
echo ""
echo -e "${BLUE}=== Summary ===${NC}"
HTML_COUNT=$(find anthropic_docs/anthropic_docs_html -type f -name "*.html" 2>/dev/null | wc -l)
MD_COUNT=$(find anthropic_docs/anthropic_docs_md -type f -name "*.md" 2>/dev/null | wc -l)
IMG_COUNT=$(find anthropic_docs/anthropic_docs_images -type f 2>/dev/null | wc -l)

echo -e "${GREEN}HTML files: $HTML_COUNT${NC}"
echo -e "${GREEN}Markdown files: $MD_COUNT${NC}"
echo -e "${GREEN}Images: $IMG_COUNT${NC}"
echo ""
echo -e "${BLUE}Log files:${NC}"
echo -e "${BLUE}- scraper.log${NC}"
echo -e "${BLUE}- scraper_stdout.log${NC}"
echo -e "${BLUE}===== Scraper Finished =====${NC}"

# Create a ZIP archive of the markdown documentation
echo -e "${BLUE}Creating ZIP archive of documentation...${NC}"
zip -r anthropic_docs_markdown.zip anthropic_docs/anthropic_docs_md anthropic_docs/table_of_contents.md anthropic_docs/sidebar.md

# Final cleanup - add timestamp to logs
current_date=$(date +"%Y%m%d_%H%M%S")
if [ -f "scraper.log" ]; then
    cp "scraper.log" "scraper_${current_date}.log"
fi
if [ -f "scraper_stdout.log" ]; then
    cp "scraper_stdout.log" "scraper_stdout_${current_date}.log"
fi 