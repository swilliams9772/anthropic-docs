#!/usr/bin/env python3
import os
import json
import shutil
import sys
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader
import base64
import re
from PIL import Image
from io import BytesIO
import logging
import argparse
import markdown
import concurrent.futures
import time
from datetime import datetime
from tqdm import tqdm
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conversion.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Configuration
HTML_DIR = "anthropic_docs_html"
MD_DIR = "anthropic_docs_md"
IMAGES_DIR = "anthropic_docs_images"
OUTPUT_DIR = "anthropic_docs_standalone_html"
METADATA_FILE = "page_metadata.json"
CSS_FILE = "style.css"
JS_FILE = "script.js"
MAX_WORKERS = 4  # Number of concurrent workers for processing

def parse_arguments():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Convert Anthropic documentation to standalone HTML")
    parser.add_argument("--output", "-o", help="Output directory", default=OUTPUT_DIR)
    parser.add_argument("--metadata", "-m", help="Metadata file", default=METADATA_FILE)
    parser.add_argument("--html-dir", help="HTML directory", default=HTML_DIR)
    parser.add_argument("--md-dir", help="Markdown directory", default=MD_DIR)
    parser.add_argument("--images-dir", help="Images directory", default=IMAGES_DIR)
    parser.add_argument("--workers", "-w", type=int, help="Number of worker threads", default=MAX_WORKERS)
    parser.add_argument("--theme", "-t", choices=["light", "dark", "auto"], default="auto", 
                      help="Theme for the documentation (light, dark, or auto)")
    parser.add_argument("--optimize-images", action="store_true", help="Optimize images for web")
    parser.add_argument("--md-source", action="store_true", 
                      help="Use Markdown files as source instead of HTML files")
    return parser.parse_args()

def load_metadata(metadata_file):
    """Load metadata from JSON file"""
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
            logger.info(f"Loaded metadata for {len(metadata)} pages")
            return metadata
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logger.error(f"Error loading metadata: {e}")
        return {}

def create_output_dir(output_dir):
    """Create output directory structure"""
    # Remove existing directory if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    
    # Create output directories
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "css"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "js"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "fonts"), exist_ok=True)
    
    logger.info(f"Created output directory structure at {output_dir}")

def build_navigation(metadata):
    """Build navigation structure from metadata"""
    # Sort pages by title for the navigation
    nav_items = []
    
    # Group pages by path segments to create a hierarchical structure
    path_groups = {}
    
    for url, data in metadata.items():
        parts = url.split('/')
        if len(parts) > 4:
            section = parts[4]
            subsection = parts[5] if len(parts) > 5 else None
        else:
            section = "main"
            subsection = None
            
        if section not in path_groups:
            path_groups[section] = {}
            
        if subsection and subsection not in path_groups[section]:
            path_groups[section][subsection] = []
            
        if subsection:
            path_groups[section][subsection].append({
                'title': data['title'],
                'url': data['html_file'],
                'level': 2
            })
        else:
            if 'items' not in path_groups[section]:
                path_groups[section]['items'] = []
                
            path_groups[section]['items'].append({
                'title': data['title'],
                'url': data['html_file'],
                'level': 1
            })
    
    # Convert the hierarchical structure to a flat list for navigation
    for section_name, section_data in sorted(path_groups.items()):
        # Format section name
        section_title = ' '.join(word.capitalize() for word in section_name.replace('-', ' ').split())
        
        # Add section header
        if section_name != "main":
            nav_items.append({
                'title': section_title,
                'url': '#',
                'level': 0,
                'is_header': True,
                'section': section_name
            })
        
        # Add section items
        if 'items' in section_data:
            for item in sorted(section_data['items'], key=lambda x: x['title']):
                item['section'] = section_name
                nav_items.append(item)
        
        # Add subsections
        for subsection_name, subsection_items in sorted(
            {k: v for k, v in section_data.items() if k != 'items'}.items()
        ):
            # Format subsection name
            subsection_title = ' '.join(
                word.capitalize() for word in subsection_name.replace('-', ' ').split()
            ) if subsection_name else ""
            
            if subsection_title:
                nav_items.append({
                    'title': subsection_title,
                    'url': '#',
                    'level': 1,
                    'is_header': True,
                    'section': section_name,
                    'subsection': subsection_name
                })
            
            # Add subsection items
            for item in sorted(subsection_items, key=lambda x: x['title']):
                item['section'] = section_name
                item['subsection'] = subsection_name
                nav_items.append(item)
    
    return nav_items

def create_css(theme="auto"):
    """Create CSS file for styling with theme support"""
    css_content = """
    @font-face {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 400;
        font-display: swap;
        src: url('../fonts/Inter-Regular.woff2') format('woff2');
    }
    
    @font-face {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 500;
        font-display: swap;
        src: url('../fonts/Inter-Medium.woff2') format('woff2');
    }
    
    @font-face {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 600;
        font-display: swap;
        src: url('../fonts/Inter-SemiBold.woff2') format('woff2');
    }
    
    @font-face {
        font-family: 'Inter';
        font-style: normal;
        font-weight: 700;
        font-display: swap;
        src: url('../fonts/Inter-Bold.woff2') format('woff2');
    }
    
    @font-face {
        font-family: 'Fira Code';
        font-style: normal;
        font-weight: 400;
        font-display: swap;
        src: url('../fonts/FiraCode-Regular.woff2') format('woff2');
    }
    """
    
    # Add root variables with theme support
    if theme == "light":
        css_content += """
        :root {
            --primary-color: #5D49F2;
            --primary-dark: #4430DE;
            --primary-light: #8F7FF7;
            --secondary-color: #0E0F3B;
            --secondary-light: #3B3D9B;
            --text-color: #333333;
            --text-light: #666666;
            --bg-color: #FFFFFF;
            --nav-bg: #F5F5F7;
            --code-bg: #F6F8FA;
            --border-color: #E8E8E8;
            --hover-bg: rgba(93, 73, 242, 0.1);
            --active-bg: rgba(93, 73, 242, 0.2);
            --shadow-color: rgba(0, 0, 0, 0.1);
            --card-bg: #FFFFFF;
            --scrollbar-track: #F1F1F1;
            --scrollbar-thumb: #C1C1C1;
            color-scheme: light;
        }
        """
    elif theme == "dark":
        css_content += """
        :root {
            --primary-color: #7C6AF5;
            --primary-dark: #6450F0;
            --primary-light: #A295F8;
            --secondary-color: #A8ABFF;
            --secondary-light: #5D61FF;
            --text-color: #E0E0E0;
            --text-light: #B0B0B0;
            --bg-color: #121212;
            --nav-bg: #1E1E1E;
            --code-bg: #2D2D2D;
            --border-color: #3D3D3D;
            --hover-bg: rgba(124, 106, 245, 0.2);
            --active-bg: rgba(124, 106, 245, 0.3);
            --shadow-color: rgba(0, 0, 0, 0.3);
            --card-bg: #1E1E1E;
            --scrollbar-track: #2D2D2D;
            --scrollbar-thumb: #555555;
            color-scheme: dark;
        }
        """
    else:  # Auto theme
        css_content += """
        :root {
            --primary-color: #5D49F2;
            --primary-dark: #4430DE;
            --primary-light: #8F7FF7;
            --secondary-color: #0E0F3B;
            --secondary-light: #3B3D9B;
            --text-color: #333333;
            --text-light: #666666;
            --bg-color: #FFFFFF;
            --nav-bg: #F5F5F7;
            --code-bg: #F6F8FA;
            --border-color: #E8E8E8;
            --hover-bg: rgba(93, 73, 242, 0.1);
            --active-bg: rgba(93, 73, 242, 0.2);
            --shadow-color: rgba(0, 0, 0, 0.1);
            --card-bg: #FFFFFF;
            --scrollbar-track: #F1F1F1;
            --scrollbar-thumb: #C1C1C1;
            --font-main: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            --font-code: 'Fira Code', 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            --header-height: 60px;
            --sidebar-width: 280px;
            color-scheme: light;
        }
        
        @media (prefers-color-scheme: dark) {
            :root {
                --primary-color: #7C6AF5;
                --primary-dark: #6450F0;
                --primary-light: #A295F8;
                --secondary-color: #A8ABFF;
                --secondary-light: #5D61FF;
                --text-color: #E0E0E0;
                --text-light: #B0B0B0;
                --bg-color: #121212;
                --nav-bg: #1E1E1E;
                --code-bg: #2D2D2D;
                --border-color: #3D3D3D;
                --hover-bg: rgba(124, 106, 245, 0.2);
                --active-bg: rgba(124, 106, 245, 0.3);
                --shadow-color: rgba(0, 0, 0, 0.3);
                --card-bg: #1E1E1E;
                --scrollbar-track: #2D2D2D;
                --scrollbar-thumb: #555555;
                color-scheme: dark;
            }
        }
        """
        
    # Add the rest of the CSS
    css_content += """
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth;
        scroll-padding-top: calc(var(--header-height) + 20px);
    }

    body {
        font-family: var(--font-main);
        color: var(--text-color);
        background-color: var(--bg-color);
        line-height: 1.6;
        display: flex;
        flex-direction: column;
        min-height: 100vh;
        overflow-x: hidden;
    }

    /* Scrollbar styling */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: var(--scrollbar-track);
    }

    ::-webkit-scrollbar-thumb {
        background: var(--scrollbar-thumb);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: var(--primary-color);
    }

    /* Header */
    header {
        background-color: var(--primary-color);
        color: white;
        padding: 0 20px;
        height: var(--header-height);
        display: flex;
        align-items: center;
        justify-content: space-between;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: 100;
        box-shadow: 0 2px 10px var(--shadow-color);
        transition: background-color 0.3s ease;
    }

    .logo {
        font-size: 1.5rem;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .logo img {
        height: 32px;
        margin: 0;
    }

    .header-actions {
        display: flex;
        align-items: center;
        gap: 15px;
    }

    #theme-toggle {
        background: none;
        border: none;
        color: white;
        font-size: 1.2rem;
        cursor: pointer;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: background-color 0.2s;
    }

    #theme-toggle:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }

    #nav-toggle {
        background: none;
        border: none;
        color: white;
        font-size: 1.5rem;
        cursor: pointer;
        display: none;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        transition: background-color 0.2s;
    }

    #nav-toggle:hover {
        background-color: rgba(255, 255, 255, 0.2);
    }

    /* Main container */
    .container {
        display: flex;
        margin-top: var(--header-height);
        flex: 1;
    }

    /* Sidebar */
    .sidebar {
        width: var(--sidebar-width);
        background-color: var(--nav-bg);
        overflow-y: auto;
        padding: 20px;
        position: fixed;
        top: var(--header-height);
        bottom: 0;
        transition: transform 0.3s ease, background-color 0.3s;
        z-index: 90;
        border-right: 1px solid var(--border-color);
    }

    .search-container {
        margin-bottom: 20px;
        position: relative;
    }

    #search-input {
        width: 100%;
        padding: 10px 12px;
        padding-left: 36px;
        border: 1px solid var(--border-color);
        border-radius: 6px;
        font-size: 0.95rem;
        background-color: var(--bg-color);
        color: var(--text-color);
        transition: all 0.2s;
    }

    #search-input:focus {
        outline: none;
        box-shadow: 0 0 0 2px var(--primary-light);
        border-color: var(--primary-color);
    }

    .search-icon {
        position: absolute;
        left: 12px;
        top: 50%;
        transform: translateY(-50%);
        color: var(--text-light);
        pointer-events: none;
    }

    .sidebar-section {
        margin-bottom: 25px;
    }

    .sidebar-section-title {
        font-weight: 600;
        color: var(--text-light);
        text-transform: uppercase;
        font-size: 0.8rem;
        letter-spacing: 0.5px;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .sidebar-section-title button {
        background: none;
        border: none;
        font-size: 1rem;
        color: var(--text-light);
        cursor: pointer;
    }

    .sidebar ul {
        list-style: none;
    }

    .sidebar li {
        margin-bottom: 2px;
    }

    .nav-header {
        color: var(--text-light);
        font-weight: 600;
        font-size: 0.9rem;
        padding: 8px 10px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-top: 10px;
    }

    .sidebar a {
        text-decoration: none;
        color: var(--text-color);
        font-size: 0.95rem;
        display: block;
        padding: 8px 12px;
        border-radius: 6px;
        transition: all 0.2s;
        position: relative;
    }

    .sidebar a:hover {
        background-color: var(--hover-bg);
        color: var(--primary-color);
    }

    .sidebar a.active {
        background-color: var(--active-bg);
        color: var(--primary-color);
        font-weight: 500;
    }

    .sidebar a.active::before {
        content: '';
        position: absolute;
        left: 0;
        top: 0;
        height: 100%;
        width: 4px;
        background-color: var(--primary-color);
        border-radius: 0 2px 2px 0;
    }

    .nav-level-0 {
        font-weight: 600;
        margin-top: 15px;
    }

    .nav-level-1 {
        margin-left: 10px;
    }

    .nav-level-2 {
        margin-left: 20px;
        font-size: 0.9rem;
    }

    /* Content area */
    .content {
        flex: 1;
        padding: 40px 60px;
        margin-left: var(--sidebar-width);
        max-width: calc(100% - var(--sidebar-width));
        transition: margin-left 0.3s ease;
    }

    .content-container {
        max-width: 900px;
        margin: 0 auto;
    }

    /* Typography */
    h1, h2, h3, h4, h5, h6 {
        margin-top: 1.5em;
        margin-bottom: 0.5em;
        color: var(--secondary-color);
        font-weight: 600;
        line-height: 1.3;
    }

    h1 {
        font-size: 2.2rem;
        margin-top: 0;
        border-bottom: 1px solid var(--border-color);
        padding-bottom: 10px;
    }

    h2 {
        font-size: 1.8rem;
        margin-top: 2em;
        padding-bottom: 5px;
        border-bottom: 1px solid var(--border-color);
    }

    h3 {
        font-size: 1.5rem;
    }

    h4 {
        font-size: 1.3rem;
    }

    h2 .anchor, h3 .anchor, h4 .anchor, h5 .anchor, h6 .anchor {
        visibility: hidden;
        text-decoration: none;
        color: var(--text-light);
        margin-left: 8px;
        font-size: 0.8em;
    }

    h2:hover .anchor, h3:hover .anchor, h4:hover .anchor, h5:hover .anchor, h6:hover .anchor {
        visibility: visible;
    }

    p, ul, ol {
        margin-bottom: 1.5em;
    }

    ul, ol {
        padding-left: 2em;
    }

    li {
        margin-bottom: 0.5em;
    }

    a {
        color: var(--primary-color);
        text-decoration: none;
        transition: color 0.2s;
    }

    a:hover {
        text-decoration: underline;
        color: var(--primary-dark);
    }

    /* Code formatting */
    pre {
        background-color: var(--code-bg);
        padding: 16px;
        border-radius: 8px;
        overflow-x: auto;
        margin: 20px 0;
        border: 1px solid var(--border-color);
        position: relative;
    }

    code {
        font-family: var(--font-code);
        font-size: 0.9em;
        background-color: var(--code-bg);
        padding: 2px 5px;
        border-radius: 4px;
        border: 1px solid var(--border-color);
    }

    pre code {
        background-color: transparent;
        padding: 0;
        font-size: 0.9rem;
        display: block;
        line-height: 1.6;
        border: none;
    }

    .code-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: var(--code-bg);
        border: 1px solid var(--border-color);
        border-bottom: none;
        border-top-left-radius: 8px;
        border-top-right-radius: 8px;
        padding: 8px 16px;
        font-family: var(--font-code);
        font-size: 0.85rem;
        color: var(--text-light);
    }

    .code-header + pre {
        margin-top: 0;
        border-top-left-radius: 0;
        border-top-right-radius: 0;
    }

    .copy-button {
        position: absolute;
        right: 10px;
        top: 10px;
        padding: 5px 10px;
        font-size: 12px;
        border: none;
        border-radius: 4px;
        background-color: var(--bg-color);
        color: var(--text-color);
        cursor: pointer;
        opacity: 0;
        transition: opacity 0.2s, background-color 0.2s;
    }

    pre:hover .copy-button {
        opacity: 1;
    }

    .copy-button:hover {
        background-color: var(--primary-color);
        color: white;
    }

    /* More styling for specific elements */
    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 0 0 1px var(--border-color);
    }

    th, td {
        padding: 12px 15px;
        text-align: left;
    }

    th {
        background-color: var(--nav-bg);
        font-weight: 600;
        color: var(--secondary-color);
    }

    tr {
        border-bottom: 1px solid var(--border-color);
    }

    tr:last-child {
        border-bottom: none;
    }

    tr:nth-child(even) {
        background-color: rgba(0,0,0,0.02);
    }

    /* Blockquotes & admonitions */
    blockquote {
        margin: 20px 0;
        padding: 15px 20px;
        border-left: 5px solid var(--primary-color);
        background-color: var(--hover-bg);
        border-radius: 0 8px 8px 0;
    }

    .admonition {
        margin: 25px 0;
        padding: 15px 20px;
        border-left: 5px solid var(--primary-color);
        background-color: var(--hover-bg);
        border-radius: 0 8px 8px 0;
    }

    .admonition-title {
        font-weight: 600;
        margin-bottom: 10px;
        color: var(--primary-color);
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .admonition-title::before {
        content: 'ℹ️';
    }

    .admonition.warning {
        border-left-color: #e6a700;
        background-color: rgba(230, 167, 0, 0.05);
    }

    .admonition.warning .admonition-title {
        color: #e6a700;
    }

    .admonition.warning .admonition-title::before {
        content: '⚠️';
    }

    .admonition.danger {
        border-left-color: #e63c3c;
        background-color: rgba(230, 60, 60, 0.05);
    }

    .admonition.danger .admonition-title {
        color: #e63c3c;
    }

    .admonition.danger .admonition-title::before {
        content: '🛑';
    }

    /* Images */
    img {
        max-width: 100%;
        border-radius: 8px;
        margin: 20px 0;
        transition: transform 0.3s ease;
        box-shadow: 0 4px 20px var(--shadow-color);
    }

    .zoomable {
        cursor: zoom-in;
    }

    .zoomed {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%) scale(1.5);
        max-width: 90vw;
        max-height: 90vh;
        z-index: 1000;
        cursor: zoom-out;
        box-shadow: 0 10px 40px var(--shadow-color);
    }

    .overlay {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.8);
        z-index: 999;
        display: none;
    }

    /* Cards for index pages */
    .card-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }

    .card {
        background-color: var(--card-bg);
        border-radius: 8px;
        border: 1px solid var(--border-color);
        padding: 20px;
        transition: transform 0.2s, box-shadow 0.2s;
        position: relative;
        overflow: hidden;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px var(--shadow-color);
    }

    .card:hover::before {
        opacity: 1;
    }

    .card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 4px;
        background: linear-gradient(90deg, var(--primary-color), var(--primary-light));
        opacity: 0;
        transition: opacity 0.2s;
    }

    .card h3 {
        margin-top: 0;
        font-size: 1.3rem;
    }

    .card p {
        color: var(--text-light);
        margin-bottom: 0;
        font-size: 0.95rem;
    }

    /* Table of contents */
    .toc {
        background-color: var(--nav-bg);
        border-radius: 8px;
        padding: 20px;
        margin: 30px 0;
        border: 1px solid var(--border-color);
    }

    .toc-title {
        font-weight: 600;
        margin-bottom: 15px;
        color: var(--secondary-color);
    }

    .toc ul {
        list-style: none;
        padding-left: 0;
    }

    .toc li {
        margin-bottom: 8px;
    }

    .toc a {
        color: var(--text-color);
        text-decoration: none;
        transition: color 0.2s;
    }

    .toc a:hover {
        color: var(--primary-color);
    }

    .toc-level-1 {
        margin-left: 0;
    }

    .toc-level-2 {
        margin-left: 15px;
        font-size: 0.95rem;
    }

    .toc-level-3 {
        margin-left: 30px;
        font-size: 0.9rem;
    }

    /* Footer */
    footer {
        background-color: var(--nav-bg);
        padding: 20px;
        text-align: center;
        border-top: 1px solid var(--border-color);
        margin-top: auto;
        margin-left: var(--sidebar-width);
        transition: margin-left 0.3s ease;
    }

    footer p {
        margin-bottom: 0;
        color: var(--text-light);
    }

    .footer-links {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 10px;
    }

    .footer-links a {
        color: var(--text-light);
        text-decoration: none;
        font-size: 0.9rem;
    }

    .footer-links a:hover {
        color: var(--primary-color);
    }

    /* Back to top button */
    #back-to-top {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        background-color: var(--primary-color);
        color: white;
        border: none;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s, visibility 0.3s, background-color 0.2s;
        z-index: 99;
        box-shadow: 0 2px 10px var(--shadow-color);
    }

    #back-to-top.visible {
        opacity: 1;
        visibility: visible;
    }

    #back-to-top:hover {
        background-color: var(--primary-dark);
    }

    /* Media queries for responsive design */
    @media (max-width: 768px) {
        :root {
            --sidebar-width: 260px;
        }

        #nav-toggle {
            display: block;
        }

        .sidebar {
            transform: translateX(-100%);
            box-shadow: 2px 0 10px var(--shadow-color);
        }

        .sidebar.active {
            transform: translateX(0);
        }

        .content {
            margin-left: 0;
            max-width: 100%;
            padding: 20px;
        }

        footer {
            margin-left: 0;
        }

        h1 {
            font-size: 2rem;
        }

        h2 {
            font-size: 1.6rem;
        }

        .card-container {
            grid-template-columns: 1fr;
        }
    }

    @media (max-width: 480px) {
        .content {
            padding: 15px;
        }

        h1 {
            font-size: 1.8rem;
        }

        pre {
            padding: 10px;
        }

        .copy-button {
            opacity: 1;
        }
    }
    """
    
    return css_content

def create_js():
    """Create JavaScript file for enhanced interactivity"""
    js_content = """
    document.addEventListener('DOMContentLoaded', function() {
        // Mobile navigation toggle
        const navToggle = document.getElementById('nav-toggle');
        const sidebar = document.querySelector('.sidebar');
        const overlay = document.createElement('div');
        overlay.classList.add('nav-overlay');
        overlay.style.position = 'fixed';
        overlay.style.top = '0';
        overlay.style.left = '0';
        overlay.style.right = '0';
        overlay.style.bottom = '0';
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
        overlay.style.zIndex = '80';
        overlay.style.display = 'none';
        document.body.appendChild(overlay);
        
        function toggleSidebar() {
            sidebar.classList.toggle('active');
            if (sidebar.classList.contains('active')) {
                overlay.style.display = 'block';
                document.body.style.overflow = 'hidden';
            } else {
                overlay.style.display = 'none';
                document.body.style.overflow = '';
            }
        }
        
        if (navToggle) {
            navToggle.addEventListener('click', toggleSidebar);
        }
        
        overlay.addEventListener('click', toggleSidebar);
        
        // Theme toggle functionality
        const themeToggle = document.getElementById('theme-toggle');
        
        if (themeToggle) {
            themeToggle.addEventListener('click', function() {
                // Check current color scheme
                const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
                
                if (isDark) {
                    document.documentElement.setAttribute('data-theme', 'light');
                    themeToggle.innerHTML = '🌙'; // Moon icon for dark mode toggle
                    localStorage.setItem('theme', 'light');
                } else {
                    document.documentElement.setAttribute('data-theme', 'dark');
                    themeToggle.innerHTML = '☀️'; // Sun icon for light mode toggle
                    localStorage.setItem('theme', 'dark');
                }
            });
            
            // Set initial theme based on localStorage or system preference
            const savedTheme = localStorage.getItem('theme');
            const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            
            if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
                document.documentElement.setAttribute('data-theme', 'dark');
                themeToggle.innerHTML = '☀️';
            } else {
                document.documentElement.setAttribute('data-theme', 'light');
                themeToggle.innerHTML = '🌙';
            }
        }
        
        // Highlight active page in navigation
        const currentPage = window.location.pathname.split('/').pop();
        const navLinks = document.querySelectorAll('.sidebar a');
        
        navLinks.forEach(link => {
            if (link.getAttribute('href') === currentPage) {
                link.classList.add('active');
                
                // Expand section if needed
                const section = link.closest('.sidebar-section');
                if (section) {
                    const content = section.querySelector('.section-content');
                    const toggle = section.querySelector('.section-toggle');
                    if (content && toggle) {
                        content.style.display = 'block';
                        toggle.textContent = '-';
                    }
                }
            }
        });
        
        // Section toggles in sidebar
        const sectionToggles = document.querySelectorAll('.section-toggle');
        
        sectionToggles.forEach(toggle => {
            toggle.addEventListener('click', function() {
                const section = this.closest('.sidebar-section');
                const content = section.querySelector('.section-content');
                
                if (content.style.display === 'none' || content.style.display === '') {
                    content.style.display = 'block';
                    this.textContent = '-';
                } else {
                    content.style.display = 'none';
                    this.textContent = '+';
                }
            });
        });
        
        // Enhanced search functionality
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            const allNavItems = document.querySelectorAll('.sidebar a');
            searchInput.addEventListener('input', function() {
                const query = this.value.toLowerCase().trim();
                
                if (query.length < 2) {
                    // Reset everything visible if query is too short
                    allNavItems.forEach(item => {
                        item.style.display = '';
                        const parent = item.parentElement;
                        if (parent) {
                            parent.style.display = '';
                        }
                    });
                    
                    // Show section headers
                    document.querySelectorAll('.nav-header').forEach(header => {
                        header.style.display = '';
                    });
                    
                    return;
                }
                
                // Hide all section headers first
                document.querySelectorAll('.nav-header').forEach(header => {
                    header.style.display = 'none';
                });
                
                // Filter navigation items
                let matchFound = false;
                allNavItems.forEach(item => {
                    if (item.classList.contains('nav-header')) return;
                    
                    const text = item.textContent.toLowerCase();
                    const isMatch = text.includes(query);
                    
                    if (isMatch) {
                        item.style.display = '';
                        const parent = item.parentElement;
                        if (parent) parent.style.display = '';
                        matchFound = true;
                        
                        // Highlight matching text
                        const regex = new RegExp(`(${query})`, 'gi');
                        item.innerHTML = item.textContent.replace(
                            regex, 
                            '<span style="background-color: var(--primary-color); color: white; padding: 0 2px; border-radius: 2px;">$1</span>'
                        );
                    } else {
                        item.style.display = 'none';
                    }
                });
                
                // Show message if no matches
                let noResultsMsg = document.getElementById('no-search-results');
                if (!matchFound) {
                    if (!noResultsMsg) {
                        noResultsMsg = document.createElement('div');
                        noResultsMsg.id = 'no-search-results';
                        noResultsMsg.style.padding = '10px';
                        noResultsMsg.style.color = 'var(--text-light)';
                        noResultsMsg.style.fontStyle = 'italic';
                        searchInput.parentNode.after(noResultsMsg);
                    }
                    noResultsMsg.textContent = `No results found for "${query}"`;
                    noResultsMsg.style.display = 'block';
                } else if (noResultsMsg) {
                    noResultsMsg.style.display = 'none';
                }
            });
            
            // Clear search when ESC is pressed
            searchInput.addEventListener('keydown', function(e) {
                if (e.key === 'Escape') {
                    this.value = '';
                    // Trigger the input event to reset the navigation
                    this.dispatchEvent(new Event('input'));
                    this.blur();
                }
            });
        }
        
        // Add copy buttons to code blocks
        document.querySelectorAll('pre code').forEach((block) => {
            const copyButton = document.createElement('button');
            copyButton.className = 'copy-button';
            copyButton.textContent = 'Copy';
            
            const pre = block.parentNode;
            
            copyButton.addEventListener('click', () => {
                // Get text content with proper line breaks
                const code = block.textContent;
                
                navigator.clipboard.writeText(code)
                    .then(() => {
                        copyButton.textContent = 'Copied!';
                        copyButton.style.backgroundColor = 'var(--primary-color)';
                        copyButton.style.color = 'white';
                        
                        setTimeout(() => {
                            copyButton.textContent = 'Copy';
                            copyButton.style.backgroundColor = '';
                            copyButton.style.color = '';
                        }, 2000);
                    })
                    .catch(err => {
                        console.error('Could not copy text: ', err);
                        copyButton.textContent = 'Error!';
                        
                        setTimeout(() => {
                            copyButton.textContent = 'Copy';
                        }, 2000);
                    });
            });
            
            pre.appendChild(copyButton);
        });
        
        // Add anchors to headings for easier linking
        document.querySelectorAll('h2, h3, h4, h5, h6').forEach((heading) => {
            if (!heading.id) {
                // Generate ID from text content
                const id = heading.textContent
                    .toLowerCase()
                    .replace(/[^\\w\\s-]/g, '')
                    .replace(/[\\s_-]+/g, '-')
                    .replace(/^-+|-+$/g, '');
                
                heading.id = id;
            }
            
            const anchor = document.createElement('a');
            anchor.className = 'anchor';
            anchor.href = `#${heading.id}`;
            anchor.textContent = '#';
            anchor.title = 'Link to this section';
            
            heading.appendChild(anchor);
        });
        
        // Make images zoomable
        document.querySelectorAll('.content img').forEach((img) => {
            img.classList.add('zoomable');
            
            img.addEventListener('click', function() {
                if (this.classList.contains('zoomed')) {
                    this.classList.remove('zoomed');
                    document.querySelector('.overlay').style.display = 'none';
                } else {
                    this.classList.add('zoomed');
                    
                    // Create overlay if it doesn't exist
                    let overlay = document.querySelector('.overlay');
                    if (!overlay) {
                        overlay = document.createElement('div');
                        overlay.className = 'overlay';
                        document.body.appendChild(overlay);
                        
                        overlay.addEventListener('click', function() {
                            document.querySelector('.zoomed').classList.remove('zoomed');
                            this.style.display = 'none';
                        });
                    }
                    
                    overlay.style.display = 'block';
                }
            });
        });
        
        // Back to top button
        const backToTopButton = document.createElement('button');
        backToTopButton.id = 'back-to-top';
        backToTopButton.innerHTML = '&uarr;';
        backToTopButton.title = 'Back to top';
        document.body.appendChild(backToTopButton);
        
        backToTopButton.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
        
        // Show/hide back to top button based on scroll position
        window.addEventListener('scroll', function() {
            if (window.pageYOffset > 300) {
                backToTopButton.classList.add('visible');
            } else {
                backToTopButton.classList.remove('visible');
            }
        });
        
        // Add syntax highlighting to code blocks
        document.querySelectorAll('pre code').forEach((block) => {
            highlightSyntax(block);
        });
        
        // Table of contents generation for long articles
        const headings = document.querySelectorAll('.content h2, .content h3');
        if (headings.length > 3) {
            const toc = document.createElement('div');
            toc.className = 'toc';
            toc.innerHTML = '<div class="toc-title">Table of Contents</div><ul></ul>';
            
            const tocList = toc.querySelector('ul');
            
            headings.forEach((heading) => {
                const li = document.createElement('li');
                const a = document.createElement('a');
                
                a.href = `#${heading.id}`;
                a.textContent = heading.textContent.replace('#', '');
                
                if (heading.tagName === 'H2') {
                    li.className = 'toc-level-1';
                } else if (heading.tagName === 'H3') {
                    li.className = 'toc-level-2';
                }
                
                li.appendChild(a);
                tocList.appendChild(li);
            });
            
            // Insert TOC after the first h1 or at the beginning of content
            const h1 = document.querySelector('.content h1');
            if (h1) {
                h1.after(toc);
            } else {
                const content = document.querySelector('.content');
                content.prepend(toc);
            }
        }
    });

    // Function to highlight syntax in code blocks
    function highlightSyntax(block) {
        // Simple syntax highlighting
        let html = block.innerHTML;
        
        // Escape HTML entities to prevent breaking the markup
        html = html.replace(/</g, '&lt;').replace(/>/g, '&gt;');
        
        // Highlight strings
        html = html.replace(/(["'])(?:(?=(\\?))\2.)*?\1/g, '<span class="hljs-string">$&</span>');
        
        // Highlight numbers
        html = html.replace(/\\b(\\d+(\\.\\d+)?|0x[\\da-fA-F]+)\\b/g, '<span class="hljs-number">$&</span>');
        
        // Language-specific keywords
        const keywords = {
            // JavaScript, TypeScript
            js: ['function', 'const', 'let', 'var', 'return', 'if', 'else', 'for', 'while', 'class', 'import', 'export', 'from', 'async', 'await', 'try', 'catch', 'new', 'typeof', 'instanceof'],
            // Python
            py: ['def', 'class', 'import', 'from', 'as', 'return', 'if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally', 'with', 'lambda', 'self', 'None', 'True', 'False'],
            // HTML
            html: ['html', 'head', 'body', 'div', 'span', 'p', 'a', 'img', 'script', 'style', 'link', 'meta', 'title', 'header', 'footer', 'main', 'section', 'article', 'aside', 'nav', 'ul', 'ol', 'li', 'form', 'input', 'button'],
            // CSS
            css: ['body', 'div', 'span', 'class', 'id', 'margin', 'padding', 'border', 'color', 'background', 'font', 'display', 'position', 'width', 'height', 'top', 'left', 'right', 'bottom', 'flex', 'grid']
        };
        
        // Try to detect language from class or nearest header
        let lang = 'js';  // Default to JavaScript
        const codeClass = block.className;
        
        if (codeClass.includes('language-python') || codeClass.includes('language-py')) {
            lang = 'py';
        } else if (codeClass.includes('language-html')) {
            lang = 'html';
        } else if (codeClass.includes('language-css')) {
            lang = 'css';
        }
        
        // Apply language-specific highlighting
        keywords[lang].forEach(keyword => {
            const regex = new RegExp(`\\\\b${keyword}\\\\b`, 'g');
            html = html.replace(regex, `<span class="hljs-keyword">${keyword}</span>`);
        });
        
        // Highlight comments based on language
        if (lang === 'js') {
            // JavaScript single-line and multi-line comments
            html = html.replace(/(\\/\\/.*$)/gm, '<span class="hljs-comment">$&</span>');
            html = html.replace(/(\\/\\*[\\s\\S]*?\\*\\/)/g, '<span class="hljs-comment">$&</span>');
        } else if (lang === 'py') {
            // Python comments
            html = html.replace(/(#.*$)/gm, '<span class="hljs-comment">$&</span>');
        } else if (lang === 'html') {
            // HTML comments
            html = html.replace(/(<!--[\\s\\S]*?-->)/g, '<span class="hljs-comment">$&</span>');
        } else if (lang === 'css') {
            // CSS comments
            html = html.replace(/(\\/\\*[\\s\\S]*?\\*\\/)/g, '<span class="hljs-comment">$&</span>');
        }
        
        block.innerHTML = html;
    }
    """
    
    return js_content

def create_template():
    """Create Jinja2 template for HTML pages"""
    template_content = """
    <!DOCTYPE html>
    <html lang="en" data-theme="auto">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="{{ description|default('Anthropic Documentation - ' ~ title) }}">
        <title>{{ title }} - Anthropic Documentation</title>
        <link rel="stylesheet" href="css/{{ css_file }}">
        <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🧠</text></svg>">
        <meta name="theme-color" content="#5D49F2">
    </head>
    <body>
        <header>
            <div class="logo">
                <img src="data:image/svg+xml;base64,{{ logo_base64 }}" alt="Anthropic Logo">
                <span>Documentation</span>
            </div>
            <div class="header-actions">
                <button id="theme-toggle" title="Toggle theme">🌙</button>
                <button id="nav-toggle" title="Toggle navigation">☰</button>
            </div>
        </header>
        
        <div class="container">
            <nav class="sidebar">
                <div class="search-container">
                    <div class="search-icon">🔍</div>
                    <input type="text" id="search-input" placeholder="Search documentation...">
                </div>
                
                {% for section in nav_sections %}
                <div class="sidebar-section">
                    <div class="sidebar-section-title">
                        {{ section.title }}
                        <button class="section-toggle">{% if section.expanded %}−{% else %}+{% endif %}</button>
                    </div>
                    <div class="section-content" style="{% if not section.expanded %}display: none;{% endif %}">
                        <ul>
                            {% for item in section.items %}
                            <li>
                                {% if item.is_header %}
                                <div class="nav-header nav-level-{{ item.level }}">{{ item.title }}</div>
                                {% else %}
                                <a href="{{ item.url }}" class="nav-level-{{ item.level }}">{{ item.title }}</a>
                                {% endif %}
                            </li>
                            {% endfor %}
                        </ul>
                    </div>
                </div>
                {% endfor %}
            </nav>
            
            <main class="content">
                <div class="content-container">
                    {{ content|safe }}
                </div>
            </main>
        </div>
        
        <footer>
            <p>Documentation generated from <a href="https://docs.anthropic.com">Anthropic Documentation</a></p>
            <div class="footer-links">
                <a href="index.html">Home</a>
                <a href="index.html">Table of Contents</a>
                <a href="https://anthropic.com" target="_blank" rel="noopener">Anthropic Website</a>
            </div>
            <p class="generation-time">Generated on {{ generation_date }}</p>
        </footer>
        
        <button id="back-to-top" title="Back to top">↑</button>
        
        <script src="js/{{ js_file }}"></script>
    </body>
    </html>
    """
    
    return template_content

def create_anthropic_logo_base64():
    """Create a base64 encoded SVG of the Anthropic logo"""
    # Simple representation of the Anthropic logo
    svg = """
    <svg width="32" height="32" viewBox="0 0 250 250" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M125 25C69.8 25 25 69.8 25 125C25 180.2 69.8 225 125 225C180.2 225 225 180.2 225 125C225 69.8 180.2 25 125 25ZM125 50C166.4 50 200 83.6 200 125C200 166.4 166.4 200 125 200C83.6 200 50 166.4 50 125C50 83.6 83.6 50 125 50Z" fill="white"/>
    </svg>
    """
    return base64.b64encode(svg.encode('utf-8')).decode('utf-8')

def process_html_content(html_content, page_name, args):
    """Process HTML content to improve structure and fix links"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Fix internal links
    for a in soup.find_all('a', href=True):
        href = a['href']
        
        # Skip anchor links
        if href.startswith('#'):
            continue
        
        # Skip external links that are explicitly meant to be external
        if href.startswith(('http://', 'https://')) and not ('docs.anthropic.com' in href or a.get('data-internal') == 'true'):
            # Add external link indicator and target blank
            a['target'] = '_blank'
            a['rel'] = 'noopener'
            continue
            
        # Handle internal links
        if a.get('data-internal') == 'true' or 'docs.anthropic.com' in href or not href.startswith(('http://', 'https://')):
            # Convert to local file reference
            if href.endswith('/'):
                href = href[:-1]
                
            # Extract the final part of the path for the filename
            if '/' in href:
                base_name = href.split('/')[-1]
            else:
                base_name = href
                
            # Add .html extension if missing
            if not base_name.endswith('.html'):
                base_name = f"{base_name}.html"
                
            # Update the href
            a['href'] = base_name
            a['data-internal'] = 'true'
    
    # Add classes to elements for better styling
    for pre in soup.find_all('pre'):
        pre['class'] = pre.get('class', []) + ['code-block']
        # Add language detection
        code = pre.find('code')
        if code and code.get('class'):
            for cls in code.get('class', []):
                if cls.startswith('language-'):
                    lang = cls.replace('language-', '')
                    # Add a code header with language info
                    header = soup.new_tag('div')
                    header['class'] = 'code-header'
                    header.string = lang.upper()
                    pre.insert_before(header)
                    break
        
    # Process blockquotes as admonitions
    for blockquote in soup.find_all('blockquote'):
        blockquote['class'] = blockquote.get('class', []) + ['admonition']
        
        # Check first paragraph for admonition title patterns
        first_p = blockquote.find('p')
        title_text = "Note"
        admonition_type = ""
        
        if first_p:
            text = first_p.get_text().lower()
            if text.startswith('note:') or text.startswith('info:'):
                title_text = "Note"
                first_p.extract()  # Remove the title line
            elif text.startswith('warning:') or text.startswith('caution:'):
                title_text = "Warning"
                admonition_type = "warning"
                blockquote['class'] = blockquote.get('class', []) + ['warning']
                first_p.extract()
            elif text.startswith('danger:') or text.startswith('important:'):
                title_text = "Important"
                admonition_type = "danger"
                blockquote['class'] = blockquote.get('class', []) + ['danger']
                first_p.extract()
        
        # Add title if not already present
        if not blockquote.find('p', class_='admonition-title'):
            title = soup.new_tag('p')
            title['class'] = 'admonition-title'
            title.string = title_text
            blockquote.insert(0, title)
    
    # Add anchor links to headings
    for heading in soup.find_all(['h2', 'h3', 'h4', 'h5', 'h6']):
        if not heading.get('id'):
            # Generate ID from text content
            heading_id = re.sub(r'[^\w\s-]', '', heading.get_text().lower())
            heading_id = re.sub(r'[\s_-]+', '-', heading_id).strip('-')
            heading['id'] = heading_id
        
        # Add anchor link
        anchor = soup.new_tag('a')
        anchor['class'] = 'anchor'
        anchor['href'] = f"#{heading['id']}"
        anchor.string = '#'
        heading.append(anchor)
    
    # Make images zoomable and fix paths
    for img in soup.find_all('img'):
        if not img['src'].startswith(('http://', 'https://', 'data:')):
            # Convert image paths to relative paths
            img_src = img['src']
            if img_src.startswith('../'):
                img_src = img_src.replace('../', '')
            img['src'] = img_src
        
        img['class'] = img.get('class', []) + ['zoomable']
        
        # Add alt text if missing
        if not img.get('alt'):
            filename = os.path.basename(img['src'])
            img['alt'] = f"Image: {filename}"
    
    return str(soup)

def organize_nav_by_sections(nav_items):
    """Organize navigation items into collapsible sections"""
    sections = {}
    
    # Group items by section
    for item in nav_items:
        section = item.get('section', 'main')
        if section not in sections:
            sections[section] = {
                'title': ' '.join(word.capitalize() for word in section.replace('-', ' ').split()),
                'items': [],
                'expanded': section == 'main'  # Only expand the main section by default
            }
        
        sections[section]['items'].append(item)
    
    # Sort sections
    sorted_sections = []
    # Ensure 'main' comes first
    if 'main' in sections:
        sorted_sections.append(sections.pop('main'))
    
    # Add the rest of the sections in alphabetical order
    for key in sorted(sections.keys()):
        sorted_sections.append(sections[key])
    
    return sorted_sections

def copy_images(metadata, args):
    """Copy and optimize images to output directory"""
    # Create images directory if not exists
    os.makedirs(os.path.join(args.output, "images"), exist_ok=True)
    
    # Keep track of unique images to avoid duplicates
    processed_images = set()
    total_images = 0
    
    for url, data in metadata.items():
        for original_src, filename in data.get('images', {}).items():
            if filename in processed_images:
                continue
                
            processed_images.add(filename)
            total_images += 1
            
            src_path = os.path.join(args.images_dir, filename)
            dest_path = os.path.join(args.output, "images", filename)
            
            if not os.path.exists(src_path):
                logger.warning(f"Image file not found: {src_path}")
                continue
                
            try:
                if args.optimize_images:
                    # Copy with image optimization
                    with Image.open(src_path) as img:
                        # Only resize if the image is very large
                        max_size = (1200, 1200)
                        if img.width > max_size[0] or img.height > max_size[1]:
                            img.thumbnail(max_size, Image.LANCZOS)
                        
                        # Save with appropriate format and compression
                        if filename.lower().endswith(('.jpg', '.jpeg')):
                            img.save(dest_path, "JPEG", quality=85, optimize=True)
                        elif filename.lower().endswith('.png'):
                            img.save(dest_path, "PNG", optimize=True)
                        else:
                            # For other formats, just copy the file
                            shutil.copy2(src_path, dest_path)
                else:
                    # Just copy the file without optimization
                    shutil.copy2(src_path, dest_path)
                    
            except Exception as e:
                logger.error(f"Error processing image {filename}: {e}")
                # Fallback to direct copy
                try:
                    shutil.copy2(src_path, dest_path)
                except Exception as copy_error:
                    logger.error(f"Failed to copy image {filename}: {copy_error}")
    
    logger.info(f"Copied {total_images} unique images to output directory")

def download_fonts(output_dir):
    """Download required fonts for the documentation"""
    fonts_dir = os.path.join(output_dir, "fonts")
    os.makedirs(fonts_dir, exist_ok=True)
    
    # Font URLs - using public CDN links for these common fonts
    font_urls = {
        "Inter-Regular.woff2": "https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyfAZ9hiA.woff2",
        "Inter-Medium.woff2": "https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuI6fAZ9hiA.woff2",
        "Inter-SemiBold.woff2": "https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuGKYAZ9hiA.woff2",
        "Inter-Bold.woff2": "https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuFuYAZ9hiA.woff2",
        "FiraCode-Regular.woff2": "https://fonts.gstatic.com/s/firacode/v21/uU9eCBsR6Z2vfE9aq3bL0fxyUs4tcw4W_D1sJVD7MOzlojwUKaJO.woff2"
    }
    
    for font_name, url in font_urls.items():
        font_path = os.path.join(fonts_dir, font_name)
        
        # Skip if font already exists
        if os.path.exists(font_path):
            continue
            
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                with open(font_path, 'wb') as f:
                    f.write(response.content)
                logger.info(f"Downloaded font: {font_name}")
            else:
                logger.warning(f"Failed to download font {font_name}, status code: {response.status_code}")
        except Exception as e:
            logger.error(f"Error downloading font {font_name}: {e}")

def create_index(metadata, nav_sections, template_env, args, logo_base64):
    """Create index.html with links to all pages"""
    content = "<h1>Anthropic API Documentation</h1>"
    content += "<p>Welcome to the Anthropic API documentation. Use the navigation menu on the left to browse the documentation or explore the sections below.</p>"
    
    # Create card-based index
    content += '<div class="card-container">'
    
    # Group pages by categories based on URL structure
    categories = {}
    for url, data in metadata.items():
        parts = url.split('/')
        if len(parts) > 4:
            category = parts[4]  # Adjust based on URL structure
        else:
            category = "Getting Started"
            
        if category not in categories:
            categories[category] = []
            
        categories[category].append({
            'title': data['title'],
            'url': data['html_file'],
            'description': data.get('description', '')
        })
    
    # Create cards for each category
    for category, pages in sorted(categories.items()):
        # Format category name
        category_title = ' '.join(word.capitalize() for word in category.replace('-', ' ').split())
        
        content += f'<div class="category-section">'
        content += f'<h2>{category_title}</h2>'
        content += '<div class="card-container">'
        
        for page in sorted(pages, key=lambda x: x['title']):
            content += f'''
            <div class="card">
                <h3><a href="{page['url']}">{page['title']}</a></h3>
                <p>{page.get('description', '')}</p>
            </div>
            '''
            
        content += '</div></div>'
    
    content += '</div>'
    
    # Get current date for footer
    generation_date = datetime.now().strftime("%B %d, %Y")
    
    # Render the template
    template = template_env.get_template('base.html')
    html = template.render(
        title="Home",
        content=content,
        nav_sections=nav_sections,
        css_file=CSS_FILE,
        js_file=JS_FILE,
        logo_base64=logo_base64,
        generation_date=generation_date
    )
    
    # Save the index.html file
    with open(os.path.join(args.output, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    
    logger.info("Created index.html")

def create_toc(metadata, nav_sections, template_env, args, logo_base64):
    """Create a table of contents page"""
    content = "<h1>Table of Contents</h1>"
    content += "<p>A comprehensive list of all documentation pages.</p>"
    
    # Group by sections
    sections = {}
    for url, data in metadata.items():
        parts = url.split('/')
        if len(parts) > 4:
            section = parts[4]
        else:
            section = "Main"
            
        if section not in sections:
            sections[section] = []
            
        sections[section].append({
            'title': data['title'],
            'url': data['html_file'],
            'level': url.count('/') - 3  # Determine nesting level
        })
    
    # Create TOC with sections
    for section_name, pages in sorted(sections.items()):
        # Format section name
        section_title = ' '.join(word.capitalize() for word in section_name.replace('-', ' ').split())
        
        content += f'<h2>{section_title}</h2>'
        content += '<ul>'
        
        # Sort pages by title
        for page in sorted(pages, key=lambda x: x['title']):
            margin_left = (page['level'] - 1) * 20 if page['level'] > 1 else 0
            content += f'<li style="margin-left: {margin_left}px;"><a href="{page["url"]}">{page["title"]}</a></li>'
            
        content += '</ul>'
    
    # Get current date for footer
    generation_date = datetime.now().strftime("%B %d, %Y")
    
    # Render the template
    template = template_env.get_template('base.html')
    html = template.render(
        title="Table of Contents",
        content=content,
        nav_sections=nav_sections,
        css_file=CSS_FILE,
        js_file=JS_FILE,
        logo_base64=logo_base64,
        generation_date=generation_date
    )
    
    # Save the TOC file
    with open(os.path.join(args.output, 'toc.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    
    logger.info("Created table of contents page")

def process_markdown_to_html(md_content, page_name):
    """Convert Markdown content to HTML"""
    html = markdown.markdown(
        md_content,
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            'markdown.extensions.tables'
        ]
    )
    return html

def convert_pages(metadata, args):
    """Convert HTML pages to standalone HTML with navigation"""
    start_time = time.time()
    
    # Set up Jinja2 environment
    template_dir = os.path.join(os.getcwd(), 'temp_templates')
    os.makedirs(template_dir, exist_ok=True)
    
    # Save template to file
    with open(os.path.join(template_dir, 'base.html'), 'w', encoding='utf-8') as f:
        f.write(create_template())
    
    # Create Jinja2 environment
    env = Environment(loader=FileSystemLoader(template_dir))
    
    # Build navigation
    nav_items = build_navigation(metadata)
    nav_sections = organize_nav_by_sections(nav_items)
    
    # Create Anthropic logo for the header
    logo_base64 = create_anthropic_logo_base64()
    
    # Generate date for footer
    generation_date = datetime.now().strftime("%B %d, %Y")
    
    # Create index page
    create_index(metadata, nav_sections, env, args, logo_base64)
    
    # Create TOC page
    create_toc(metadata, nav_sections, env, args, logo_base64)
    
    # Process each page with a progress bar
    total_pages = len(metadata)
    logger.info(f"Converting {total_pages} pages...")
    
    with tqdm(total=total_pages, desc="Converting pages") as pbar:
        # Use ThreadPoolExecutor for parallel processing
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = []
            
            for url, data in metadata.items():
                html_file = data['html_file']
                md_file = data['md_file']
                title = data['title']
                description = data.get('description', '')
                
                # Determine which source to use
                if args.md_source:
                    source_path = os.path.join(args.md_dir, md_file)
                    source_type = "markdown"
                else:
                    source_path = os.path.join(args.html_dir, html_file)
                    source_type = "html"
                
                # Submit the task to the executor
                future = executor.submit(
                    process_page, 
                    source_path, 
                    source_type,
                    html_file,
                    title,
                    description,
                    env,
                    nav_sections,
                    logo_base64,
                    generation_date,
                    args
                )
                futures.append(future)
            
            # Process results as they complete
            for future in concurrent.futures.as_completed(futures):
                try:
                    result = future.result()
                    if result:
                        pbar.update(1)
                except Exception as exc:
                    logger.error(f"Page processing failed: {exc}")
                    pbar.update(1)
    
    # Clean up template directory
    shutil.rmtree(template_dir)
    
    duration = time.time() - start_time
    logger.info(f"Converted {total_pages} pages in {duration:.2f} seconds")

def process_page(source_path, source_type, html_file, title, description, template_env, nav_sections, logo_base64, generation_date, args):
    """Process a single documentation page"""
    try:
        # Read the source file
        if not os.path.exists(source_path):
            logger.warning(f"Source file not found: {source_path}")
            return False
            
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert content based on source type
        if source_type == "markdown":
            # Convert Markdown to HTML
            html_content = process_markdown_to_html(content, html_file)
        else:
            # Process HTML content
            html_content = content
        
        # Process the HTML content
        processed_content = process_html_content(html_content, html_file, args)
        
        # Render the template
        template = template_env.get_template('base.html')
        output_html = template.render(
            title=title,
            description=description,
            content=processed_content,
            nav_sections=nav_sections,
            css_file=CSS_FILE,
            js_file=JS_FILE,
            logo_base64=logo_base64,
            generation_date=generation_date
        )
        
        # Save the output HTML file
        with open(os.path.join(args.output, html_file), 'w', encoding='utf-8') as f:
            f.write(output_html)
        
        return True
    except Exception as e:
        logger.error(f"Error processing page {html_file}: {e}")
        return False

def main():
    # Parse command line arguments
    args = parse_arguments()
    
    # Print welcome message
    logger.info("Converting documentation to standalone HTML...")
    
    # Load metadata
    metadata = load_metadata(args.metadata)
    if not metadata:
        logger.error("Error: Metadata file not found or empty.")
        sys.exit(1)
    
    # Create output directory structure
    create_output_dir(args.output)
    
    # Download fonts
    download_fonts(args.output)
    
    # Create CSS and JS files
    css_content = create_css(args.theme)
    with open(os.path.join(args.output, "css", CSS_FILE), 'w', encoding='utf-8') as f:
        f.write(css_content)
        
    js_content = create_js()
    with open(os.path.join(args.output, "js", JS_FILE), 'w', encoding='utf-8') as f:
        f.write(js_content)
    
    # Copy and optimize images
    copy_images(metadata, args)
    
    # Convert HTML pages
    convert_pages(metadata, args)
    
    logger.info("\nConversion completed successfully!")
    logger.info(f"Standalone HTML documentation is available in the '{args.output}' directory.")
    logger.info(f"Open '{args.output}/index.html' in your browser to view the documentation.")

if __name__ == "__main__":
    main() 