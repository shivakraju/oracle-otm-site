#!/usr/bin/env python3
"""Bold terms before colons at the start of lines across all posts."""
import os, re

POSTS_DIR = "content/posts"

def process_file(fpath):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split off front matter
    if content.startswith('---'):
        parts = content.split('---', 2)
        front = '---' + parts[1] + '---'
        body = parts[2]
    else:
        front = ''
        body = content

    lines = body.split('\n')
    new_lines = []
    in_code_block = False

    for line in lines:
        # Track code blocks — don't modify inside them
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue

        if in_code_block:
            new_lines.append(line)
            continue

        # Skip headings, blank lines, already bold lines, HTML, list markers
        stripped = line.lstrip()
        if (not stripped
                or stripped.startswith('#')
                or stripped.startswith('**')
                or stripped.startswith('<')
                or stripped.startswith('!')
                or stripped.startswith('http')
                or stripped.startswith('|')):
            new_lines.append(line)
            continue

        # Match: word(s) before a colon at start of the (stripped) line
        # Allow letters, digits, spaces, /, (, ), ., _, -, &
        # Must NOT be a URL pattern (no ://)
        def bold_term(m):
            term = m.group(1).rstrip()
            rest = m.group(2)
            # Skip if it looks like a URL scheme e.g. "http" before "://"
            if rest.startswith('//'):
                return m.group(0)
            # Skip if term is very long (likely a sentence, not a label)
            if len(term) > 50:
                return m.group(0)
            return f'**{term}:**{rest}'

        new_line = re.sub(
            r'^([A-Za-z0-9][A-Za-z0-9 /().,_\-&]*?):(.*)',
            bold_term,
            stripped
        )

        # Preserve original leading whitespace
        leading = line[:len(line) - len(stripped)]
        new_lines.append(leading + new_line)

    new_body = '\n'.join(new_lines)
    new_content = front + new_body

    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False

updated = 0
for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    if process_file(fpath):
        updated += 1
        print(f"Updated: {fname}")

print(f"\nDone! Updated {updated} files.")
