#!/usr/bin/env python3
"""Convert HTML tags to Markdown in MkDocs files, preserving complex HTML structures."""
import re, os

DOCS = "/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs"

# Tags that should remain as HTML (complex structures)
PRESERVE_BLOCKS = [
    'table', 'div.quick-facts', 'div.card-grid', 'div.faq-section', 'div.faq-list',
    'ol.references', 'div.info-box', 'div.card', 'div.hero', 'div.list-grid', 'div.list-item',
    'div.executive-summary', 'div.quick-fact', 'div.facts-table',
    'span.tag',
]

def is_preserved_block(tag, class_attr):
    """Check if this block should be preserved as HTML."""
    for p in PRESERVE_BLOCKS:
        if '.' in p:
            t, cls = p.split('.')
            if tag == t and cls in class_attr:
                return True
        elif tag == p:
            return True
    return False

def convert_line(line):
    """Convert HTML tags to Markdown within a single line of text."""
    # Must not be inside a preserved block
    
    # <strong>text</strong> -> **text**
    line = re.sub(r'<strong>(.*?)</strong>', r'**\1**', line)
    
    # <em>text</em> -> *text*
    line = re.sub(r'<em>(.*?)</em>', r'*\1*', line)
    
    # <code>text</code> -> `text`
    line = re.sub(r'<code>(.*?)</code>', r'`\1`', line)
    
    # <a href="url">text</a> -> [text](url)
    line = re.sub(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', line)
    
    # <br> or <br/>
    line = re.sub(r'<br\s*/?>', '\n', line)
    
    # <sub>text</sub> -> ~text~ (not standard MD, but keep for readability)
    # <sup>text</sup> -> ^text^
    line = re.sub(r'<sub>(.*?)</sub>', r'~\1~', line)
    line = re.sub(r'<sup>(.*?)</sup>', r'^\1^', line)
    
    return line

def convert_file(fpath):
    """Convert an .md file from HTML tags to Markdown where possible."""
    with open(fpath) as f:
        content = f.read()
    
    # Split frontmatter and body
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    fm = parts[1]
    body = parts[2]
    original = body
    lines = body.split('\n')
    
    result = []
    i = 0
    skip_until = -1
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip already processed lines
        if i < skip_until:
            i += 1
            continue
        
        # Detect preserved blocks
        preserved_end = -1
        
        # <table> blocks
        if stripped.startswith('<table'):
            # Find the closing </table>
            for j in range(i, len(lines)):
                if '</table>' in lines[j]:
                    preserved_end = j
                    break
            if preserved_end > 0:
                result.append(line)  # keep as-is
                for k in range(i+1, preserved_end + 1):
                    result.append(lines[k])
                i = preserved_end + 1
                continue
        
        # <div class="card-grid"> etc preserved blocks
        if stripped.startswith('<div') and ('card-grid' in stripped or 'faq-section' in stripped or 
            'faq-list' in stripped or 'quick-facts' in stripped or 'info-box' in stripped or 
            'list-grid' in stripped or 'executive-summary' in stripped or 'facts-table' in stripped or
            'hero' in stripped or 'quick-fact' in stripped or 'card"' in stripped or 'card ' in stripped):
            # Find matching closing </div>
            depth = 1
            for j in range(i+1, len(lines)):
                if '<div' in lines[j] and '/div>' not in lines[j].strip()[:5]:
                    depth += 1
                if '</div>' in lines[j]:
                    depth -= 1
                    if depth == 0:
                        preserved_end = j
                        break
            if preserved_end > 0:
                for k in range(i, preserved_end + 1):
                    result.append(lines[k])
                i = preserved_end + 1
                continue
        
        # <ol class="references"> blocks
        if stripped.startswith('<ol') and 'references' in stripped:
            for j in range(i, len(lines)):
                if '</ol>' in lines[j]:
                    preserved_end = j
                    break
            if preserved_end > 0:
                for k in range(i, preserved_end + 1):
                    result.append(lines[k])
                i = preserved_end + 1
                continue
        
        # Convert h2, h3, h4 to Markdown
        h2_match = re.match(r'<h2>(.*?)</h2>', stripped)
        if h2_match:
            text = h2_match.group(1)
            result.append('## ' + text)
            i += 1
            continue
        
        h3_match = re.match(r'<h3>(.*?)</h3>', stripped)
        if h3_match:
            text = h3_match.group(1)
            result.append('### ' + text)
            i += 1
            continue
        
        h4_match = re.match(r'<h4>(.*?)</h4>', stripped)
        if h4_match:
            text = h4_match.group(1)
            result.append('#### ' + text)
            i += 1
            continue
        
        # Convert h1 to h1 Markdown (but we already have title in fm)
        h1_match = re.match(r'<h1[^>]*>(.*?)</h1>', stripped)
        if h1_match:
            text = h1_match.group(1)
            result.append('# ' + text)
            i += 1
            continue
        
        # Convert paragraphs - but they may span multiple lines
        if stripped.startswith('<p>') and '</p>' in stripped:
            # Single line paragraph
            inner = stripped[3:-4]  # remove <p> and </p>
            inner = convert_line(inner)
            result.append(inner)
            i += 1
            continue
        
        if stripped.startswith('<p>') and '</p>' not in stripped:
            # Multi-line paragraph - collect all lines
            para_lines = [stripped[3:]]  # remove <p>
            for j in range(i+1, len(lines)):
                s = lines[j].strip()
                if '</p>' in s:
                    para_lines.append(s[:-4])  # remove </p>
                    # Reconstruct as single paragraph
                    para_text = ' '.join(para_lines)
                    para_text = convert_line(para_text)
                    result.append(para_text)
                    i = j + 1
                    break
                else:
                    para_lines.append(s)
            else:
                # No close found, keep as-is
                result.append(line)
                i += 1
            continue
        
        # Convert <ul> lists
        if stripped == '<ul>' or stripped.startswith('<ul'):
            result.append(line)
            i += 1
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith('<li>') and '</li>' in s:
                    inner = s[4:-5]  # remove <li> and </li>
                    inner = convert_line(inner)
                    result.append('- ' + inner)
                    i += 1
                elif '</ul>' in s:
                    result.append(s)
                    i += 1
                    break
                else:
                    result.append(lines[i])
                    i += 1
            continue
        
        # Convert <ol> lists
        if stripped == '<ol>' or stripped.startswith('<ol'):
            result.append(line)
            i += 1
            item_num = 1
            while i < len(lines):
                s = lines[i].strip()
                if s.startswith('<li>') and '</li>' in s:
                    inner = s[4:-5]
                    inner = convert_line(inner)
                    result.append(f'  {item_num}. {inner}')
                    item_num += 1
                    i += 1
                elif '</ol>' in s:
                    result.append(s)
                    i += 1
                    break
                else:
                    result.append(lines[i])
                    i += 1
            continue
        
        # Handle standalone </div> closing tags (from previously preserved blocks)
        if stripped == '</div>' and i < len(lines) - 1:
            result.append(line)
            i += 1
            continue
        
        # Handle <!-- comments -->
        if stripped.startswith('<!--'):
            result.append(line)
            i += 1
            continue
        
        # Detect headings already in Markdown format -> skip
        if re.match(r'^#{1,6}\s', stripped):
            result.append(line)
            i += 1
            continue
        
        # Detect horizontal rules
        if stripped == '<hr>' or stripped == '<hr/>':
            result.append('---')
            i += 1
            continue
        
        # Anything else - keep as-is but convert inline tags
        if stripped:
            converted = convert_line(line)
            result.append(converted)
        else:
            result.append(line)
        
        i += 1
    
    new_body = '\n'.join(result)
    if new_body != original:
        new_content = '---\n' + fm.strip() + '\n---\n' + new_body
        with open(fpath, 'w') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    count = 0
    for root, dirs, files in os.walk(DOCS):
        for f in files:
            if not f.endswith('.md'): continue
            fpath = os.path.join(root, f)
            if convert_file(fpath):
                count += 1
                rel = os.path.relpath(fpath, DOCS)
                print(f'Converted: {rel}')
    
    print(f'\n{count} files converted from HTML to Markdown')

if __name__ == '__main__':
    main()
