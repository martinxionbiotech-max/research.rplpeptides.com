#!/usr/bin/env python3
"""Clean converter: strip all <div> wrappers not part of visible content."""
import re, os

ASTRO_SRC = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-research/src/pages"
DOCS_DST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def clean_slot(slot):
    """Remove <div class="container article-body">...</div> wrapper if present."""
    # The slot content may have this wrapping div at the outermost level
    # Pattern: <div class="container article-body">\n    (content)\n  </div>
    m = re.match(r'<div\s+class="[^"]*container[^"]*article-body[^"]*"[^>]*>\s*(.*?)\s*</div>\s*$', slot, re.DOTALL)
    if m:
        return m.group(1).strip()
    
    # Also check for container-only or other wrapper divs
    m = re.match(r'<div\s+class="container[^"]*"[^>]*>\s*(.*?)\s*</div>\s*$', slot, re.DOTALL)
    if m:
        return m.group(1).strip()
    
    return slot

def extract_title(content):
    m = re.search(r"const title\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def extract_description(content):
    m = re.search(r"const description\s*=\s*'([^']+)'", content)
    if m: return m.group(1)
    return None

def convert(astro_path):
    rel = os.path.relpath(astro_path, ASTRO_SRC)
    base = rel[:-6] if rel.endswith('.astro') else rel
    
    if base.endswith('index'):
        return None  # skip index pages
    
    md_base = base + '.md'
    md_path = os.path.join(DOCS_DST, md_base)
    
    with open(astro_path) as f:
        content = f.read()
    
    title = extract_title(content)
    desc = extract_description(content)
    
    # Get slot content
    parts = content.split('---')
    body = '---'.join(parts[2:]) if len(parts) >= 3 else content
    
    # Extract slot between <BaseLayout ...> and </BaseLayout>
    s = body.find('<BaseLayout')
    s = body.find('>', s) + 1
    e = body.find('</BaseLayout>')
    if e == -1:
        e = body.find('</BaseLayout')
    if s < e:
        slot = body[s:e].strip()
    else:
        slot = body.strip()
    
    # Clean wrapper divs
    clean = clean_slot(slot)
    
    # Build frontmatter
    fm = "---\n"
    if title:
        fm += f"title: {title}\n"
    if desc:
        fm += f"description: \"{desc.replace('\"', '\\\\\"')}\"\n"
    fm += "---\n\n"
    
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write(fm)
        f.write(clean + '\n')
    
    return {'path': md_base, 'title': title or base.split('/')[-1]}

def main():
    import sys
    count = 0
    for root, dirs, files in os.walk(ASTRO_SRC):
        for fn in sorted(files):
            if not fn.endswith('.astro'): continue
            info = convert(os.path.join(root, fn))
            if info:
                count += 1
                print(f"  {info['path']} — {info['title'][:60]}")
    print(f"\nConverted {count} pages")

if __name__ == '__main__':
    main()
