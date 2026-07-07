#!/usr/bin/env python3
"""Replace old oracle-otm.com links with new local paths in Basic OTM Configurations posts."""
import os, re

POSTS_DIR = "content/posts"

url_map = {
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-01-domain.html":
        "/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-02-itinerary.html":
        "/posts/basic-otm-configurations-02-itinerary/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-03-service.html":
        "/posts/basic-otm-configurations-03-service-provider-and-rates/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-04-business.html":
        "/posts/basic-otm-configurations-04-business-numbers-planning-parameter/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-05-bulk-plan.html":
        "/posts/basic-otm-configurations-05-bulk-plan/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-06-tender.html":
        "/posts/basic-otm-configurations-06-tender-process/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-07-invoicing.html":
        "/posts/basic-otm-configurations-07-invoicing/",
    "https://www.oracle-otm.com/2020/08/basic-otm-configurations-08-voucher.html":
        "/posts/basic-otm-configurations-08-voucher-allocation/",
}

updated = 0
for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.startswith("basic-otm-configurations") or not fname.endswith(".md"):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    new_content = content
    for old_url, new_url in url_map.items():
        new_content = new_content.replace(old_url, new_url)
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        updated += 1
        print(f"Fixed: {fname}")

print(f"\nDone! Updated {updated} files.")
