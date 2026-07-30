#!/usr/bin/env python3
"""Fix all Astro-style absolute paths (/path/to/page/) to MkDocs relative paths across all markdown files."""
import re, os

DOCS = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

def build_path_map():
    """Map Astro-style absolute paths to MkDocs relative markdown paths."""
    mapping = {}
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'):
                continue
            fpath = os.path.join(root, f)
            rel = os.path.relpath(fpath, DOCS)
            # Astro path (without trailing /)
            if rel.endswith('index.md'):
                astro_path = '/' + rel[:-9]  # remove 'index.md'
                if astro_path == '':
                    astro_path = '/'
            else:
                astro_path = '/' + rel[:-3]  # remove '.md'
            # Register both with and without trailing slash
            mapping[astro_path] = rel
            mapping[astro_path + '/'] = rel
            # Also for subdir index pages
            parts = rel.split('/')
            if len(parts) > 1 and parts[-1] == 'index.md':
                dir_path = '/' + '/'.join(parts[:-1])
                mapping[dir_path + '/'] = rel
    return mapping

def resolve_href(base_rel, target_rel):
    """Convert absolute Astro path to relative path from base file."""
    if target_rel == 'index.md':
        return target_rel
    
    base_dir = os.path.dirname(base_rel) if '/' in base_rel else ''
    result = os.path.relpath(target_rel, base_dir)
    return result

def fix_file(fpath, path_map):
    with open(fpath) as f:
        content = f.read()
    
    rel = os.path.relpath(fpath, DOCS)
    modified = False
    
    # Fix href="/path/" and href="/path"
    for astro_path, target_rel in sorted(path_map.items(), key=lambda x: -len(x[0])):
        if not astro_path.startswith('/'):
            continue
        # Pattern: href="/some/path/" or href="/some/path"
        # We need to handle quotes properly
        patterns = [
            f'href="{astro_path}"',
        ]
        new_href = resolve_href(rel, target_rel)
        
        for pat in patterns:
            if pat in content:
                new_pat = f'href="{new_href}"'
                content = content.replace(pat, new_pat)
                modified = True
    
    # Also fix href with single quotes
    for astro_path, target_rel in sorted(path_map.items(), key=lambda x: -len(x[0])):
        if not astro_path.startswith('/'):
            continue
        pat = f"href='{astro_path}'"
        if pat in content:
            new_href = resolve_href(rel, target_rel)
            new_pat = f"href='{new_href}'"
            content = content.replace(pat, new_pat)
            modified = True
    
    if modified:
        with open(fpath, 'w') as f:
            f.write(content)
        return True
    return False

def main():
    path_map = build_path_map()
    print(f"Path map has {len(path_map)} entries")
    
    fixed = 0
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'):
                continue
            fpath = os.path.join(root, f)
            if fix_file(fpath, path_map):
                fixed += 1
    
    # Check for remaining Astro paths
    remaining = 0
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'):
                continue
            fpath = os.path.join(root, f)
            with open(fpath) as fh:
                content = fh.read()
            # Look for href="/ at remaining absolute paths that aren't external URLs
            for m in re.finditer(r'href="(/[^"]+)"', content):
                href = m.group(1)
                if '//' not in href and not href.startswith('#'):
                    remaining += 1
                    print(f"  REMAINING: {os.path.relpath(fpath, DOCS)} -> {href}")
    
    print(f"\nFixed {fixed} files")
    if remaining == 0:
        print("All absolute paths resolved!")
    else:
        print(f"{remaining} absolute paths remain")

if __name__ == '__main__':
    main()
