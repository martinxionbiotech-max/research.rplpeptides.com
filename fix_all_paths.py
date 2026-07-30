#!/usr/bin/env python3
"""Fix ALL Astro-style absolute paths (/xxx/) to MkDocs relative paths (xxx.md or ../xxx.md).
Also add missing frontmatter (title, description).
"""
import re, os

DOCS = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

# Build mapping from Astro path -> actual .md path (relative to docs/)
PAGE_MAP = {}
for root, dirs, files in os.walk(DOCS):
    for f in files:
        if not f.endswith('.md'):
            continue
        fpath = os.path.join(root, f)
        rel = os.path.relpath(fpath, DOCS)
        
        # Astro path without extension
        if rel.endswith('/index.md'):
            astro_path = '/' + rel[:-9]  # remove 'index.md'
        else:
            astro_path = '/' + rel[:-3]  # remove '.md'
        
        PAGE_MAP[astro_path] = rel
        PAGE_MAP[astro_path + '/'] = rel

print(f"Page map has {len(PAGE_MAP)} entries")

def resolve_href(from_rel, astro_href):
    """Convert Astro absolute path to MkDocs relative path."""
    target_rel = PAGE_MAP.get(astro_href)
    if not target_rel:
        # Try without trailing slash or with
        if astro_href.endswith('/'):
            target_rel = PAGE_MAP.get(astro_href[:-1])
        else:
            target_rel = PAGE_MAP.get(astro_href + '/')
    
    if not target_rel:
        return None
    
    from_dir = os.path.dirname(from_rel) if '/' in from_rel else ''
    result = os.path.relpath(target_rel, from_dir)
    return result

def add_missing_frontmatter(content, title_guess, is_index):
    """Add YAML frontmatter if missing."""
    if content.startswith('---'):
        # Has frontmatter
        parts = content.split('---', 2)
        if len(parts) < 3:
            # Incomplete frontmatter - redo
            body = content[content.find('---', 3)+3:].strip() if content[3:].find('---') > 0 else content
        else:
            fm = parts[1]
            body = parts[2]
            
            # Check if title missing
            if 'title:' not in fm and title_guess:
                # Insert title after first line of fm
                fm_lines = fm.strip().split('\n')
                fm = 'title: ' + title_guess + '\n' + '\n'.join(fm_lines)
            
            new_content = '---\n' + fm.strip() + '\n---\n\n' + body.strip() + '\n'
            return new_content
    else:
        # No frontmatter
        body = content.strip()
        if title_guess:
            fm = f"title: {title_guess}\n"
        else:
            fm = ''
        return '---\n' + fm + '---\n\n' + body + '\n'
    
    return content

def extract_h1_title(body):
    """Extract title from <h1> tag."""
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body)
    if m: return m.group(1).strip()
    return None

def fix_file(fpath):
    rel = os.path.relpath(fpath, DOCS)
    with open(fpath) as f:
        content = f.read()
    
    has_fm = content.startswith('---')
    
    # Separate frontmatter and body
    if has_fm:
        parts = content.split('---', 2)
        if len(parts) < 3:
            fm = ''
            body = content
        else:
            fm = parts[1]
            body = parts[2]
    else:
        fm = ''
        body = content
    
    # 1. Fix href="/path/" → href="relative.md"
    # Sort by length (longest first) to avoid partial replacements
    modified = False
    for astro_path, target_rel in sorted(PAGE_MAP.items(), key=lambda x: -len(x[0])):
        # href="/path/" or href="/path"
        resolved = resolve_href(rel, astro_path)
        if not resolved:
            continue
        
        double_q = f'href="{astro_path}"'
        if double_q in body:
            body = body.replace(double_q, f'href="{resolved}"')
            modified = True
    
    # Fix rpl-peptides-ecosystem.md - it has href="/research/" etc
    # These are index page links so resolve to research/index.md etc
    for astro_path in ['/research/', '/peptide-library/', '/methods/', '/literature/',
                        '/comparisons/', '/rpl-peptides-ecosystem/', '/authors/']:
        resolved = resolve_href(rel, astro_path)
        if not resolved:
            continue
        double_q = f'href="{astro_path}"'
        if double_q in body:
            body = body.replace(double_q, f'href="{resolved}"')
            modified = True
    
    is_index = rel.endswith('/index.md') or rel == 'index.md'
    
    # 2. Add missing title to frontmatter
    if fm and 'title:' not in fm:
        h1 = extract_h1_title(body)
        if h1:
            fm = 'title: ' + h1 + '\n' + fm.strip()
            modified = True
    
    # 3. Add missing description to frontmatter  
    if fm and 'description:' not in fm:
        # Take first <p> text
        m = re.search(r'<p>(.*?)</p>', body)
        if m:
            desc = m.group(1)[:120]
            desc_esc = desc.replace('"', '\\"')
            fm = fm.strip() + '\ndescription: "' + desc_esc + '"\n'
            modified = True
    
    if modified:
        new_content = '---\n' + fm.strip() + '\n---' + body
        with open(fpath, 'w') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    fixed = 0
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'):
                continue
            fpath = os.path.join(root, f)
            if fix_file(fpath):
                fixed += 1
    
    print(f"Fixed {fixed} files")
    
    # Verify remaining broken links
    existing = set(PAGE_MAP.keys())
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'): continue
            fpath = os.path.join(root, f)
            rel = os.path.relpath(fpath, DOCS)
            with open(fpath) as fh:
                c = fh.read()
            for m in re.finditer(r'href="(/[^"]+)"', c):
                href = m.group(1)
                if '//' in href: continue
                # Resolve relative to file
                from_dir = os.path.dirname(rel) if '/' in rel else ''
                resolved = os.path.normpath(os.path.join(from_dir, href))
                # See if it matches any known page
                candidates = [resolved]
                if not resolved.endswith('.md'):
                    candidates.append(resolved + '.md')
                    candidates.append(resolved + '/index.md')
                    # Try /index path
                    candidates.append(resolved[:-1] + '/index.md' if resolved.endswith('/') else resolved + '/index.md')
                
                found = False
                for c in candidates:
                    rel_c = os.path.relpath(c, '.') if os.path.isabs(c) else c
                    if rel_c in existing:
                        found = True
                        break
                
                if not found:
                    print(f"  STILL BROKEN: {rel}: href=\"{href}\" (resolved={resolved})")
    
    # Check remaining missing frontmatter
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'): continue
            fpath = os.path.join(root, f)
            rel = os.path.relpath(fpath, DOCS)
            with open(fpath) as fh:
                c = fh.read()
            if not c.startswith('---'):
                print(f"  NO FM: {rel}")
            else:
                parts = c.split('---', 2)
                if len(parts) >= 2:
                    fm = parts[1]
                    if 'title:' not in fm:
                        print(f"  NO TITLE: {rel}")
                    if 'description:' not in fm:
                        print(f"  NO DESC: {rel}")
    
    print("Verification done")

if __name__ == '__main__':
    main()
