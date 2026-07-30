#!/usr/bin/env python3
"""Convert Astro pages to MkDocs markdown files.
Extracts HTML body from .astro files and wraps in MkDocs YAML frontmatter.
"""
import re, os, sys

ASTRO_SRC = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-research/src/pages"
DOCS_DST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

CATEGORY_MAP = {
    'peptide-biology': 'Peptide Biology',
    'peptide-chemistry': 'Peptide Chemistry',
    'analytical-science': 'Analytical Science',
    'metabolic': 'Metabolic Research',
    'applications': 'Research Applications',
}

def extract_title(content):
    """Extract title from Astro const declaration."""
    m = re.search(r"const title\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def extract_description(content):
    """Extract description from Astro const declaration."""
    m = re.search(r"const description\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def extract_body(content):
    """Extract the HTML body inside article-body div."""
    # Remove frontmatter (--- ... ---)
    parts = content.split('---')
    if len(parts) >= 3:
        body = '---'.join(parts[2:])
    else:
        body = content
    
    # Find article-body opening
    m = re.search(r'<div[^>]*class="[^"]*container[^"]*article-body[^"]*"[^>]*>\s*(.*?)(?:\s*</div>\s*</main>|\s*</div>\s*$)', body, re.DOTALL)
    if m:
        return m.group(1).strip()
    
    # Fallback: find content between main tags
    m = re.search(r'<main[^>]*>(.*?)</main>', body, re.DOTALL)
    if m:
        return m.group(1).strip()
    
    return body.strip()

def extract_h1(body):
    """Extract H1 tag content."""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body)
    if m: return m.group(1).strip()
    return None

def convert_file(astro_path):
    """Convert one .astro file to .md file."""
    rel_path = os.path.relpath(astro_path, ASTRO_SRC)
    
    base = rel_path
    if base.endswith('.astro'):
        base = base[:-6]
    
    # Determine output path
    md_rel_path = base + '.md'
    md_path = os.path.join(DOCS_DST, md_rel_path)
    
    # Skip index pages
    if base.endswith('/index'):
        return None
    
    with open(astro_path, 'r') as f:
        content = f.read()
    
    title = extract_title(content)
    description = extract_description(content)
    body = extract_body(content)
    
    if not body and '/index' not in rel_path:
        print(f"  WARNING: No body extracted for {rel_path}", file=sys.stderr)
    
    # Determine page category for nav
    cat_name = None
    for slug, name in CATEGORY_MAP.items():
        if f'/{slug}/' in base:
            cat_name = name
            break
    
    # Build YAML frontmatter
    frontmatter = "---\n"
    if title:
        frontmatter += f"title: {title}\n"
    if description:
        frontmatter += f"description: \"{description}\"\n"
    frontmatter += "---\n\n"
    
    # Write the file
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write(frontmatter)
        if body:
            f.write(body + '\n')
    
    # Get title for nav
    nav_title = title or extract_h1(body) or base.split('/')[-1]
    return {
        'slug': base,
        'title': nav_title,
        'path': md_rel_path,
        'category': cat_name
    }

def main():
    pages = []
    count = 0
    
    for root, dirs, files in os.walk(ASTRO_SRC):
        for fname in sorted(files):
            if not fname.endswith('.astro'):
                continue
            fpath = os.path.join(root, fname)
            info = convert_file(fpath)
            if info:
                pages.append(info)
                count += 1
    
    print(f"Converted {count} pages")
    return pages

if __name__ == '__main__':
    main()
