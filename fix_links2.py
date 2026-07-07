#!/usr/bin/env python3
"""Convert bare URL lines that follow a link-text line into proper markdown links."""
import os, re

POSTS_DIR = "content/posts"

# Map bare URL paths to their link text
url_to_text = {
    "/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/":
        "Basic OTM Configurations - 01 - Domain, Items, Locations, and Equipment",
    "/posts/basic-otm-configurations-02-itinerary/":
        "Basic OTM Configurations - 02 - Itinerary",
    "/posts/basic-otm-configurations-03-service-provider-and-rates/":
        "Basic OTM Configurations - 03 - Service Provider and Rates",
    "/posts/basic-otm-configurations-04-business-numbers-planning-parameter/":
        "Basic OTM Configurations - 04 - Business Numbers, Planning Parameter",
    "/posts/basic-otm-configurations-05-bulk-plan/":
        "Basic OTM Configurations - 05 - Bulk Plan",
    "/posts/basic-otm-configurations-06-tender-process/":
        "Basic OTM Configurations - 06 - Tender process",
    "/posts/basic-otm-configurations-07-invoicing/":
        "Basic OTM Configurations - 07 - Invoicing",
    "/posts/basic-otm-configurations-08-voucher-allocation/":
        "Basic OTM Configurations - 08 - Voucher Allocation",
}

updated = 0
for fname in sorted(os.listdir(POSTS_DIR)):
    if not fname.startswith("basic-otm-configurations") or not fname.endswith(".md"):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    changed = False
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        # Check if this line is a link text and next line is a bare URL
        if i + 1 < len(lines):
            next_stripped = lines[i+1].strip()
            if next_stripped in url_to_text and stripped == url_to_text[next_stripped]:
                # Merge into a proper markdown link
                new_lines.append(f"[{stripped}]({next_stripped})\n")
                i += 2  # skip both lines
                # skip the blank line after if present
                if i < len(lines) and lines[i].strip() == "":
                    i += 1
                changed = True
                continue
        new_lines.append(line)
        i += 1

    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        updated += 1
        print(f"Fixed: {fname}")

print(f"\nDone! Updated {updated} files.")
