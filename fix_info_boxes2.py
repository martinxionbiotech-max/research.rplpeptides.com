#!/usr/bin/env python3
"""Re-run conversion + fix indent: `!!! info` must start at column 0."""
import re, glob

def convert_html_to_markdown_text(html):
    html = re.sub(r'<strong>(.*?)</strong>', r'**\1**', html, flags=re.DOTALL)
    html = re.sub(r'<a\s+href="([^"]*)"[^>]*>([^<]*)</a>', r'[\2](\1)', html, flags=re.DOTALL)
    html = re.sub(r'<em>(.*?)</em>', r'*\1*', html, flags=re.DOTALL)
    html = re.sub(r'<[^>]+>', '', html)
    html = re.sub(r'\s*\n\s*', '\n', html)
    return html.strip()

def convert_info_box(content):
    """Replace HTML info-box with MkDocs admonition (!!! at column 0)."""
    pattern = r'<div class="info-box info">\s*(.*?)\s*</div>'
    def replacer(m):
        raw = m.group(1).strip()
        lines = [l.strip() for l in raw.split('\n') if l.strip()]
        text = convert_html_to_markdown_text('\n'.join(lines))
        indented = '\n    '.join(text.split('\n'))
        return f'!!! info ""\n    {indented}'
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

root = '/home/ubuntu/.openclaw/workspace/projects/rpl-peptides-docs/docs'
files = sorted(glob.glob(f'{root}/**/*.md', recursive=True))

for fpath in files:
    with open(fpath) as fh:
        content = fh.read()
    new_content = convert_info_box(content)
    if new_content != content:
        with open(fpath, 'w') as fh:
            fh.write(new_content)
        rel = fpath[len(root)+1:]
        print(f'✅ {rel}')

print('Done')
