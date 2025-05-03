#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Table of Contents
-------------------------
Generates a table of contents file from the markdown documentation files.
This helps with navigation without needing to include headers in each file.
"""

import os
import re
import json
from collections import defaultdict

OUTPUT_DIR = "anthropic_docs"
MD_DIR = os.path.join(OUTPUT_DIR, "anthropic_docs_md")
TOC_OUTPUT = os.path.join(OUTPUT_DIR, "table_of_contents.md")
NAV_OUTPUT = os.path.join(OUTPUT_DIR, "sidebar.md")
METADATA_FILE = os.path.join(OUTPUT_DIR, "page_metadata.json")

def extract_title(file_path):
    """Extract the title (first h1) from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for the first h1 header
    title_match = re.search(r'^# (.*?)$', content, re.MULTILINE)
    if title_match:
        return title_match.group(1).strip()
    
    # If no h1 header is found, use the filename
    return os.path.basename(file_path).replace('.md', '').replace('_', ' ').title()

def is_ignored_file(filename):
    """Check if a file should be ignored in TOC"""
    ignored = ['sidebar.md', 'index.md', 'table_of_contents.md']
    return filename in ignored

def get_category(filename):
    """Determine the category from the filename"""
    if '_' not in filename:
        return "General"
    
    # Extract the first part before underscore as category
    category = filename.split('_')[0]
    
    # Map common prefixes to better category names
    category_map = {
        'admin': 'Administration',
        'api': 'API Reference',
        'messages': 'Messages API',
        'models': 'Models',
        'build': 'Building with Claude',
        'about': 'About Claude',
        'agents': 'Agents & Tools',
        'resources': 'Resources',
        'test': 'Testing & Evaluation'
    }
    
    return category_map.get(category, category.capitalize())

def sort_files(files):
    """Sort files in a logical documentation order"""
    # Define priority order for certain files
    priority_files = {
        'welcome.md': 0,
        'intro-to-claude.md': 1,
        'getting-started.md': 2,
        'quickstart.md': 3,
        'models.md': 4,
        'messages.md': 5,
    }
    
    # Sort files by priority first, then alphabetically
    return sorted(files, key=lambda f: (priority_files.get(f, 100), f))

def parse_page_metadata():
    """Load page metadata to get additional information"""
    if not os.path.exists(METADATA_FILE):
        return {}
    
    with open(METADATA_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def generate_toc():
    """Generate a table of contents from markdown files"""
    if not os.path.exists(MD_DIR):
        print(f"Markdown directory not found: {MD_DIR}")
        return
    
    # Get all markdown files
    md_files = [f for f in os.listdir(MD_DIR) if f.endswith('.md') and not is_ignored_file(f)]
    
    # Group files by category
    categories = defaultdict(list)
    for filename in md_files:
        category = get_category(filename)
        categories[category].append(filename)
    
    # Sort categories and files
    sorted_categories = sorted(categories.keys())
    for category in categories:
        categories[category] = sort_files(categories[category])
    
    # Load metadata for additional information
    metadata = parse_page_metadata()
    
    # Generate TOC
    toc = []
    toc.append("# Anthropic API Documentation")
    toc.append("\nThis documentation was scraped from the Anthropic website and converted to markdown format.\n")
    
    # Add a table of all sections
    toc.append("## Contents\n")
    for category in sorted_categories:
        toc.append(f"- [{category}](#{category.lower().replace(' ', '-')})")
    
    # Add each category and its files
    for category in sorted_categories:
        toc.append(f"\n## {category}\n")
        
        for filename in categories[category]:
            filepath = os.path.join(MD_DIR, filename)
            title = extract_title(filepath)
            
            # Create link to the file
            file_link = filename.replace(' ', '%20')
            toc.append(f"- [{title}](anthropic_docs_md/{file_link})")
    
    # Generate sidebar navigation
    sidebar = []
    sidebar.append("# Navigation\n")
    
    for category in sorted_categories:
        sidebar.append(f"## {category}\n")
        
        for filename in categories[category]:
            filepath = os.path.join(MD_DIR, filename)
            title = extract_title(filepath)
            
            # Create link to the file
            file_link = filename.replace(' ', '%20')
            sidebar.append(f"- [{title}]({file_link})")
    
    # Write TOC to file
    with open(TOC_OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(toc))
    
    # Write sidebar navigation to file
    with open(NAV_OUTPUT, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sidebar))
    
    print(f"Generated table of contents at {TOC_OUTPUT}")
    print(f"Generated sidebar navigation at {NAV_OUTPUT}")

if __name__ == "__main__":
    generate_toc() 