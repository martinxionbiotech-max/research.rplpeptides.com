#!/usr/bin/env python3
"""Convert <div class="info-box info"> to MkDocs !!! info admonitions."""
import re, glob

def convert_html_to_markdown_text(html):
    """Convert simple HTML inline tags to Markdown within admonition text."""
    # <strong>text</strong> → **text**
    html = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html, flags=re.DOTALL)
    # <a href="url">text</a> → [text](url)
    html = re.sub(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', html, flags=re.DOTALL)
    # <em>text</em> → *text*
    html = re.sub(r'<em>(.*?)</em>', r'*\1*', html, flags=re.DOTALL)
    # Remove any remaining HTML tags
    html = re.sub(r'<[^>]+>', '', html)
    # Clean up whitespace
    html = re.sub(r'\s*\n\s*', '\n', html)
    html = html.strip()
    return html

def convert_info_box(content):
    """Replace all <div class="info-box info"> blocks with MkDocs admonitions."""
    pattern = r'<div class="info-box info">\s*(.*?)\s*</div>'
    
    def replacer(m):
        raw = m.group(1).strip()
        # Split into lines, strip leading whitespace from each line
        lines = raw.split('\n')
        cleaned_lines = []
        for line in lines:
            stripped = line.strip()
            if stripped:
                cleaned_lines.append(stripped)
        text = '\n'.join(cleaned_lines)
        # Convert HTML to Markdown
        md_text = convert_html_to_markdown_text(text)
        # Ensure it's indented for admonition
        indented = '\n'.join('    ' + ln for ln in md_text.split('\n'))
        return f'!!! info ""\n{indented}'
    
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

root = '/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs'
files = sorted(glob.glob(f'{root}/**/*.md', recursive=True))

count_files = 0
count_boxes = 0

for fpath in files:
    with open(fpath) as fh:
        content = fh.read()
    
    new_content = convert_info_box(content)
    if new_content != content:
        with open(fpath, 'w') as fh:
            fh.write(new_content)
        boxes = content.count('<div class="info-box info">')
        count_files += 1
        count_boxes += boxes
        rel = fpath[len(root)+1:]
        print(f'✅ {rel} ({boxes} boxes)')

print(f'\nTotal: {count_files} files, {count_boxes} info-boxes converted')
