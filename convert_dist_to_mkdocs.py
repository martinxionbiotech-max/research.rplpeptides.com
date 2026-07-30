#!/usr/bin/env python3
"""Convert built dist/ HTML to MkDocs markdown files."""
import re, os, sys
from html.parser import HTMLParser

ASTRO_DIST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-research/dist"
DOCS_DST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def extract_title_desc_from_meta(html):
    """Extract title and description from HTML meta tags."""
    title = ''
    desc = ''
    m = re.search(r'<title>(.*?)\s*\|?\s*RPL Peptides Research', html)
    if m:
        title = m.group(1).strip()
    m = re.search(r'<meta[^>]*name="description"[^>]*content="([^"]*)"', html)
    if m:
        desc = m.group(1)
    return title, desc

def extract_body(html):
    """Extract content from article-body div, preserving HTML structure."""
    m = re.search(r'<div class="container article-body">(.*?)</div>\s*</main>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    # fallback: main content
    m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    return ''

def convert_html_to_md(html_body):
    """Convert HTML body elements to Markdown where possible."""
    # Remove skip-link and breadcrumb nav if present
    lines = []
    for line in html_body.split('\n'):
        stripped = line.strip()
        # Skip breadcrumb nav
        if 'class="breadcrumb"' in stripped or 'aria-label="Breadcrumb"' in stripped:
            continue
        if '<nav ' in stripped and 'Breadcrumb' in stripped:
            # Skip breadcrumb nav block - we'll handle it via MkDocs
            continue
        lines.append(line)
    return '\n'.join(lines)

def convert_file(item_rel_path, html_file):
    """Extract content from one HTML file and save as .md."""
    # Determine output path
    if item_rel_path.endswith('/index.html'):
        item_rel_path = item_rel_path[:-10]  # remove /index
        if not item_rel_path:
            item_rel_path = 'index'
    
    md_rel_path = item_rel_path + '.md'
    md_path = os.path.join(DOCS_DST, md_rel_path)
    
    with open(html_file) as f:
        html = f.read()
    
    title, desc = extract_title_desc_from_meta(html)
    
    # Skip the root index (handled separately) and index pages (handled as category pages)
    if item_rel_path == '' or item_rel_path == '/':
        # Skip root index - we'll create a custom one
        pass
    
    body = extract_body(html)
    if not body:
        print(f"  WARNING: No body for {item_rel_path}")
        return None
    
    # Build frontmatter
    fm = "---\n"
    if title:
        fm += f"title: {title}\n"
    if desc:
        # Escape quotes
        desc_escaped = desc.replace('"', '\\"')
        fm += f"description: \"{desc_escaped}\"\n"
    fm += "---\n\n"
    
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write(fm)
        f.write(body + '\n')
    
    return {
        'path': md_rel_path,
        'title': title or item_rel_path.split('/')[-1]
    }

def main():
    pages = []
    count = 0
    
    for root, dirs, files in os.walk(ASTRO_DIST):
        for fname in sorted(files):
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            rel_path = os.path.relpath(fpath, ASTRO_DIST)
            
            info = convert_file(rel_path, fpath)
            if info:
                pages.append(info)
                count += 1
    
    print(f"Converted {count} pages")
    
    # Print summary for nav
    print("\n=== Pages by section ===")
    sections = {}
    for p in pages:
        section = p['path'].split('/')[0] if '/' in p['path'] else 'root'
        if section not in sections:
            sections[section] = []
        sections[section].append(p)
    
    for section, spages in sorted(sections.items()):
        print(f"\n  {section}/ ({len(spages)} pages):")
        for p in spages[:5]:
            print(f"    - {p['path']}: {p['title'][:60]}")

if __name__ == '__main__':
    main()
