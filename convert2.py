#!/usr/bin/env python3
"""Convert Astro pages to MkDocs markdown files."""
import re, os, sys

ASTRO_SRC = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-research/src/pages"
DOCS_DST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def extract_astro_slot(content):
    """Extract content between <BaseLayout ...> and </BaseLayout>."""
    # Remove frontmatter (--- ... ---)
    parts = content.split('---')
    if len(parts) >= 3:
        body = '---'.join(parts[2:])
    else:
        body = content
    
    # Find BaseLayout opening and closing
    start = body.find('<BaseLayout')
    if start == -1:
        return body.strip()
    
    start = body.find('>', start) + 1
    end = body.find('</BaseLayout>')
    if end == -1:
        # Try </BaseLayout without closing >
        end = body.find('</BaseLayout')
    
    if end > start:
        slot = body[start:end].strip()
        return slot
    return body.strip()

def extract_title(content):
    m = re.search(r"const title\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def extract_description(content):
    m = re.search(r"const description\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def get_nav_title(body):
    """Get first h1 text."""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body)
    if m: return m.group(1).strip()
    return None

def convert_file(astro_path):
    rel_path = os.path.relpath(astro_path, ASTRO_SRC)
    base = rel_path[:-6] if rel_path.endswith('.astro') else rel_path
    
    # Skip index pages (handled separately for nav)
    md_rel_path = base + '.md'
    md_path = os.path.join(DOCS_DST, md_rel_path)
    
    with open(astro_path) as f:
        content = f.read()
    
    title = extract_title(content)
    desc = extract_description(content)
    slot = extract_astro_slot(content)
    
    if not slot:
        print(f"  WARNING: No slot content for {rel_path}")
        return None
    
    # Build frontmatter
    fm = "---\n"
    if title:
        fm += f"title: {title}\n"
    if desc:
        desc_escaped = desc.replace('"', '\\"')
        fm += f"description: \"{desc_escaped}\"\n"
    fm += "---\n\n"
    
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write(fm)
        f.write(slot + '\n')
    
    nav_title = title or get_nav_title(slot) or base.split('/')[-1]
    return {
        'path': md_rel_path,
        'title': nav_title
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
    pages = main()
    # Print nav structure
    sections = {}
    for p in pages:
        section = p['path'].split('/')[0]
        if section not in sections:
            sections[section] = []
        sections[section].append(p)
    for s, ps in sorted(sections.items()):
        print(f"\n  {s}/ ({len(ps)} pages)")
