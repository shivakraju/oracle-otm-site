#!/usr/bin/env python3
"""Add weight to post front matter to control sidebar order in Hugo Book."""
import os, re

POSTS_DIR = "content/posts"

# Define exact sidebar order (top to bottom)
ORDER = [
    "what-is-otm",
    "introduction-to-otm",
    "introduction-to-basic-teminology",
    "basic-logistics-terminology",
    "otm-architecture",
    "otm-inbound-integrations-xml",
    "otm-outbound-integrations",
    "csv-data-uploads",
    "posting-data-to-otm-using-http-request",
    "otm-domains-standard-schema-and-data-dictionary",
    "otm-order-management-data-structure",
    "otm-shipment-management-data-structure",
    "otm-contract-rate-management-data-structure",
    "business-process-automation-data-structure",
    "basic-otm-configurations",
    "basic-otm-configurations-01",
    "basic-otm-configurations-02",
    "basic-otm-configurations-03",
    "basic-otm-configurations-04",
    "basic-otm-configurations-05",
    "basic-otm-configurations-06",
    "basic-otm-configurations-07",
    "basic-otm-configurations-08",
    "saved-queriesconditions",
    "agents-frequently-used-actions",
    "agents-sample-agent-creation-steps",
    "agents-agent-event-restrictions",
    "agent-gates",
    "business-monitors",
    "business-numbers",
    "report-development-sample-report",
    "emailing-reports-to-users-on-a-business-event",
    "report-workspaces",
    "manager-layouts-screen-sets-labels",
    "flex-fields",
    "advanced-layouts",
    "workbenches",
    "user-roles-vpd-and-access-control-lists",
    "user-menu-and-manage-user-access",
    "service-provider-user-login-creation",
    "refnums",
    "status-types",
    "action-checks",
    "custom-actions-smart-links",
    "yard-management-and-appointment-scheduling",
    "otm-application-admin-notes",
    "oracle-dba-notes",
    "g-log-properties",
    "support-tips",
]

def get_weight(filename):
    # Strip date prefix and .md
    slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', filename).replace('.md', '')
    for i, pattern in enumerate(ORDER):
        if slug.startswith(pattern) or pattern in slug:
            return (i + 1) * 10
    return 9999  # unknown posts go to end

files = sorted(os.listdir(POSTS_DIR))
for fname in files:
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(POSTS_DIR, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    weight = get_weight(fname)

    # Remove existing weight line if present
    content = re.sub(r'\nweight: \d+', '', content)

    # Insert weight into front matter
    content = content.replace('draft: false\n', f'draft: false\nweight: {weight}\n', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"weight={weight:4d}  {fname}")

print("\nDone!")
