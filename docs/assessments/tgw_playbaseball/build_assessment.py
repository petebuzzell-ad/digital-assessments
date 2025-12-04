#!/usr/bin/env python3
"""
Build script to combine markdown assessment files into a single HTML document
with password protection and search, plus a PDF version.
"""

import os
import sys
import json
import hashlib
import argparse
import base64
from pathlib import Path
import markdown
from markdown.extensions import tables, fenced_code, codehilite

# Get the directory where this script is located
SCRIPT_DIR = Path(__file__).parent
ASSESSMENT_DIR = SCRIPT_DIR
IMAGES_DIR = ASSESSMENT_DIR / "images"
OUTPUT_DIR = ASSESSMENT_DIR

def get_password_hash(password):
    """Generate SHA-256 hash of password."""
    return hashlib.sha256(password.encode()).hexdigest()

def embed_image_as_base64(image_path):
    """Embed image as base64 data URI."""
    if not image_path.exists():
        return None
    
    ext = image_path.suffix.lower()
    mime_types = {
        '.png': 'image/png',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.gif': 'image/gif',
        '.svg': 'image/svg+xml',
        '.webp': 'image/webp'
    }
    
    mime_type = mime_types.get(ext, 'image/png')
    
    with open(image_path, 'rb') as f:
        image_data = base64.b64encode(f.read()).decode('utf-8')
    
    return f"data:{mime_type};base64,{image_data}"

def process_markdown_images(html_content, base_dir):
    """Convert markdown image references to base64 embedded images."""
    import re
    
    # Pattern to match markdown images: ![alt](path)
    pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
    
    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Handle relative paths
        if not image_path.startswith(('http://', 'https://', 'data:')):
            full_path = base_dir / image_path
            if full_path.exists():
                base64_data = embed_image_as_base64(full_path)
                if base64_data:
                    return f'<img src="{base64_data}" alt="{alt_text}" />'
        
        # Return original if we can't process it
        return match.group(0)
    
    return re.sub(pattern, replace_image, html_content)

def read_markdown_files():
    """Read all markdown files (00-11) in order."""
    files = []
    for i in range(12):
        filename = f"{i:02d}_*.md"
        matching_files = list(ASSESSMENT_DIR.glob(filename))
        if matching_files:
            files.append(matching_files[0])
    
    if not files:
        raise FileNotFoundError("No markdown files found (00-11)")
    
    content_parts = []
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            content_parts.append({
                'filename': filepath.name,
                'content': content
            })
    
    return content_parts

def extract_headings(content):
    """Extract headings from markdown to build table of contents."""
    import re
    headings = []
    lines = content.split('\n')
    
    for line in lines:
        # Match markdown headings: # Heading, ## Heading, etc.
        match = re.match(r'^(#{1,6})\s+(.+)$', line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            # Create anchor from heading text
            anchor = re.sub(r'[^\w\s-]', '', text.lower())
            anchor = re.sub(r'[-\s]+', '-', anchor)
            headings.append({
                'level': level,
                'text': text,
                'anchor': anchor
            })
    
    return headings

def convert_markdown_to_html(markdown_content):
    """Convert markdown to HTML with extensions."""
    md = markdown.Markdown(extensions=[
        'tables',
        'fenced_code',
        'codehilite',
        'nl2br',
        'sane_lists'
    ])
    html = md.convert(markdown_content)
    return html

def build_html_content(markdown_files, password_hash):
    """Build the complete HTML document."""
    # Combine all markdown content
    combined_markdown = []
    all_headings = []
    
    for file_data in markdown_files:
        # Extract headings for TOC
        headings = extract_headings(file_data['content'])
        all_headings.extend(headings)
        
        # Convert to HTML
        html_content = convert_markdown_to_html(file_data['content'])
        
        # Process images
        html_content = process_markdown_images(html_content, ASSESSMENT_DIR)
        
        # Add section wrapper
        section_id = file_data['filename'].replace('.md', '').replace('_', '-')
        combined_markdown.append(f'<section id="{section_id}" class="assessment-section">')
        combined_markdown.append(html_content)
        combined_markdown.append('</section>')
    
    content_html = '\n'.join(combined_markdown)
    
    # Read template
    template_path = SCRIPT_DIR / 'templates' / 'assessment_template.html'
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")
    
    with open(template_path, 'r', encoding='utf-8') as f:
        template = f.read()
    
    # Replace placeholders
    html = template.replace('{{CONTENT}}', content_html)
    html = html.replace('{{PASSWORD_HASH}}', password_hash)
    
    return html

def generate_pdf(html_content, output_path):
    """Generate PDF from HTML using weasyprint."""
    try:
        from weasyprint import HTML, CSS
        from weasyprint.text.fonts import FontConfiguration
        
        font_config = FontConfiguration()
        html_doc = HTML(string=html_content, base_url=str(ASSESSMENT_DIR))
        
        # Add print-specific CSS
        css = CSS(string='''
            @page {
                size: letter;
                margin: 1in;
            }
            .password-modal, .search-bar, .toc-sidebar {
                display: none !important;
            }
            body {
                padding: 0;
            }
        ''')
        
        html_doc.write_pdf(output_path, stylesheets=[css], font_config=font_config)
        print(f"✓ PDF: {output_path}")
    except ImportError:
        print("⚠ weasyprint not available")
    except Exception as e:
        print(f"⚠ PDF failed: {e}")

def main():
    parser = argparse.ArgumentParser(description='Build assessment HTML and PDF')
    parser.add_argument('--password', type=str, help='Password for HTML document')
    parser.add_argument('--config', type=str, help='Path to config.json file')
    parser.add_argument('--no-pdf', action='store_true', help='Skip PDF generation')
    
    args = parser.parse_args()
    
    # Get password
    password = None
    if args.password:
        password = args.password
    elif args.config:
        config_path = Path(args.config)
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = json.load(f)
                password = config.get('password')
    
    if not password:
        config_path = ASSESSMENT_DIR / 'config.json'
        if config_path.exists():
            with open(config_path, 'r') as f:
                config = json.load(f)
                password = config.get('password')
    
    if not password:
        print("⚠ No password provided. Using default 'assessment'")
        password = "assessment"
    
    # Generate password hash
    password_hash = get_password_hash(password)
    
    markdown_files = read_markdown_files()
    html_content = build_html_content(markdown_files, password_hash)
    
    html_output = OUTPUT_DIR / 'assessment.html'
    with open(html_output, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✓ HTML: {html_output}")
    
    if not args.no_pdf:
        pdf_output = OUTPUT_DIR / 'assessment.pdf'
        generate_pdf(html_content, pdf_output)

if __name__ == '__main__':
    main()

