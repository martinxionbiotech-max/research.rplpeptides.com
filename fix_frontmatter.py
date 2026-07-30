#!/usr/bin/env python3
"""Add missing title and description frontmatter to all MkDocs files."""
import re, os

DOCS = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def extract_h1(body):
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body)
    if m: return m.group(1).strip()
    return None

def extract_first_p(body):
    m = re.search(r'<p>(.*?)</p>', body)
    if m: return m.group(1).strip()
    return None

def fix_file(fpath):
    rel = os.path.relpath(fpath, DOCS)
    with open(fpath) as f:
        content = f.read()
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = parts[1]
    body = '---' + parts[2] if len(parts) == 3 else ''
    changed = False
    
    # Fix missing title
    if 'title:' not in fm and 'title: ' not in fm:
        h1 = extract_h1(body)
        if h1:
            fm = 'title: ' + h1 + '\n' + fm
            changed = True
    
    # Fix missing description
    if 'description:' not in fm and 'description: ' not in fm:
        p = extract_first_p(body)
        if p:
            # Take first 80 chars
            desc = p[:120].replace('"', '\\"')
            fm = fm.strip() + '\ndescription: "' + desc + '"\n'
            changed = True
    
    if changed:
        content = '---\n' + fm.strip() + '\n---\n' + parts[2]
        with open(fpath, 'w') as f:
            f.write(content)
        return True
    return False

count = 0
for root, dirs, files in os.walk(DOCS):
    for f in files:
        if not f.endswith('.md'): continue
        if fix_file(os.path.join(root, f)):
            count += 1

print(f"Fixed {count} files")
