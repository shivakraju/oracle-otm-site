#!/usr/bin/env python3
"""Rename post files to remove date prefix, update all internal links."""
import os, re, shutil

POSTS_DIR = "content/posts"
MENU_FILE = "content/menu/_index.md"

files = sorted(os.listdir(POSTS_DIR))
url_map = {}

# Step 1: Rename files and build URL map
for fname in files:
    if not fname.endswith('.md'):
        continue
    new_fname = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', fname)
    if new_fname != fname:
        src = os.path.join(POSTS_DIR, fname)
        dst = os.path.join(POSTS_DIR, new_fname)
        shutil.move(src, dst)
        old_slug = fname.replace('.md', '')
        new_slug = new_fname.replace('.md', '')
        url_map[f'/posts/{old_slug}/'] = f'/posts/{new_slug}/'
        print(f"Renamed: {fname} -> {new_fname}")

print(f"\nRenamed {len(url_map)} files")

# Step 2: Remove 'slug' front matter from all posts (no longer needed)
for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = re.sub(r'\nslug: "[^"]*"', '', content)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

# Step 3: Update internal links in all posts
updated = 0
for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = content
    for old_url, new_url in url_map.items():
        new_content = new_content.replace(old_url, new_url)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated += 1

print(f"Updated links in {updated} posts")

# Step 4: Update menu file
with open(MENU_FILE, 'r', encoding='utf-8') as f:
    menu = f.read()
for old_url, new_url in url_map.items():
    menu = menu.replace(old_url, new_url)
with open(MENU_FILE, 'w', encoding='utf-8') as f:
    f.write(menu)
print("Updated sidebar menu")
print("\nDone!")
