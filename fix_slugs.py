#!/usr/bin/env python3
"""
1. Add clean slug (no date) to each post's front matter
2. Update all internal /posts/YYYY-MM-DD-slug/ links to /posts/slug/
   across all post files and the menu file
"""
import os, re

POSTS_DIR = "content/posts"
MENU_FILE = "content/menu/_index.md"

# Build mapping: old-url-slug -> new-slug
slug_map = {}  # "2020-06-21-basic-otm-configurations" -> "basic-otm-configurations"

for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    old_slug = fname.replace('.md', '')                        # 2020-06-21-basic-otm-configurations
    new_slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', old_slug)   # basic-otm-configurations
    slug_map[old_slug] = new_slug

# Step 1: Add/update slug in each post's front matter
for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    old_slug = fname.replace('.md', '')
    new_slug = slug_map[old_slug]

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove existing slug line if present
    content = re.sub(r'\nslug:.*', '', content)

    # Insert slug into front matter after 'draft: false'
    content = content.replace('draft: false\n', f'draft: false\nslug: "{new_slug}"\n', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Added slugs to {len(slug_map)} posts")

# Step 2: Build URL replacement map
# old: /posts/2020-06-21-basic-otm-configurations/
# new: /posts/basic-otm-configurations/
url_map = {}
for old_slug, new_slug in slug_map.items():
    url_map[f'/posts/{old_slug}/'] = f'/posts/{new_slug}/'

def replace_links(text):
    for old_url, new_url in url_map.items():
        text = text.replace(old_url, new_url)
    return text

# Step 3: Update internal links in all posts
updated_posts = 0
for fname in os.listdir(POSTS_DIR):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = replace_links(content)
    if new_content != content:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        updated_posts += 1

print(f"Updated internal links in {updated_posts} posts")

# Step 4: Update menu file
with open(MENU_FILE, 'r', encoding='utf-8') as f:
    menu = f.read()
new_menu = replace_links(menu)
with open(MENU_FILE, 'w', encoding='utf-8') as f:
    f.write(new_menu)
print("Updated sidebar menu links")

# Show sample mappings
print("\nSample URL changes:")
for old, new in list(url_map.items())[:5]:
    print(f"  {old} -> {new}")
