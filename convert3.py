#!/usr/bin/env python3
"""Ultimate converter: extract slot, handle all wrapper divs, for ALL pages including index."""
import re, os

ASTRO_SRC = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-research/src/pages"
DOCS_DST = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def extract_title(content):
    """Extract title from Astro: const title='...' or <BaseLayout title="...">"""
    # Pattern 1: const title = '...'
    m = re.search(r"const\s+title\s*=\s*'([^']+)'", content)
    if m:
        return m.group(1)
    # Pattern 2: <BaseLayout ... title="..."
    m = re.search(r'<BaseLayout[^>]*title=["\']([^"\']+)["\']', content, re.DOTALL)
    if m:
        return m.group(1)
    return None

def extract_description(content):
    m = re.search(r"const\s+description\s*=\s*'([^']+)'", content)
    if m:
        return m.group(1)
    return None

def clean_slot(slot):
    """Strip outermost wrapper divs leaving inner visible content."""
    # Check for <div class="container article-body">...</div> or <div class="container ...">...</div>
    # or <div class="container page-header">...</div> or <div class="container section">...</div>
    wrapper_patterns = [
        r'<div\s+class="[^"]*container[^"]*article-body[^"]*"[^>]*>',
        r'<div\s+class="container\s+page-header"[^>]*>',
        r'<div\s+class="container\s+section"[^>]*>',
        r'<div\s+class="container"[^>]*>',
    ]
    
    for pat in wrapper_patterns:
        m = re.match(pat + r'\s*(.*?)\s*</div>\s*$', slot, re.DOTALL)
        if m:
            inner = m.group(1).strip()
            inner = clean_slot(inner)  # recursive
            return inner
    
    return slot

def convert(astro_path):
    rel = os.path.relpath(astro_path, ASTRO_SRC)
    base = rel[:-6] if rel.endswith('.astro') else rel
    md_base = base + '.md'
    md_path = os.path.join(DOCS_DST, md_base)
    
    with open(astro_path) as f:
        content = f.read()
    
    title = extract_title(content)
    desc = extract_description(content)
    
    # Get content after frontmatter
    parts = content.split('---')
    if len(parts) >= 3:
        body = '---'.join(parts[2:])
    else:
        body = content
    
    # Extract slot from BaseLayout
    s = body.find('<BaseLayout')
    if s >= 0:
        s = body.find('>', s) + 1
    else:
        s = 0
    e = body.find('</BaseLayout>')
    if e < 0:
        e = body.find('</BaseLayout')
    if e < 0:
        e = len(body)
    
    slot = body[s:e].strip() if s < e else body.strip()
    clean = clean_slot(slot)
    
    if not clean:
        print(f"  WARNING: empty content for {base}")
        return None
    
    # Build frontmatter
    fm_lines = ["---"]
    if title:
        fm_lines.append(f"title: {title}")
    if desc:
        desc_esc = desc.replace('"', '\\"')
        fm_lines.append(f'description: "{desc_esc}"')
    fm_lines.append("---")
    fm_lines.append("")
    
    os.makedirs(os.path.dirname(md_path), exist_ok=True)
    with open(md_path, 'w') as f:
        f.write('\n'.join(fm_lines))
        f.write('\n')
        f.write(clean)
        f.write('\n')
    
    return {'path': md_base, 'title': title or base.split('/')[-1]}

def main():
    count = 0
    for root, dirs, files in os.walk(ASTRO_SRC):
        for fn in sorted(files):
            if not fn.endswith('.astro'):
                continue
            convert(os.path.join(root, fn))
            count += 1
    print(f"Converted {count} pages")
    
    # Verify div balance
    from html.parser import HTMLParser
    class C(HTMLParser):
        def __init__(self):
            super().__init__()
            self.div = 0
        def handle_starttag(self, tag, attrs):
            if tag == 'div': self.div += 1
        def handle_endtag(self, tag):
            if tag == 'div': self.div -= 1
    
    bad = 0
    for root, dirs, files in os.walk(DOCS_DST):
        for fn in files:
            if not fn.endswith('.md'): continue
            path = os.path.join(root, fn)
            with open(path) as fh:
                c = fh.read()
            pts = c.split('---')
            b = '---'.join(pts[2:]) if len(pts) >= 3 else c
            counter = C()
            counter.feed(b)
            if counter.div != 0:
                print(f"  DIV IMBALANCE {counter.div}: {path}")
                bad += 1
    
    if bad == 0:
        print("All div tags balanced!")
    else:
        print(f"{bad} files with div imbalance")

if __name__ == '__main__':
    main()
