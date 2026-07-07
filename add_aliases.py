#!/usr/bin/env python3
"""Add Hugo aliases (redirects from old Blogger URLs) to each post's front matter."""
import os, re

POSTS_DIR = "content/posts"

# Map: post filename → list of old Blogger URLs to redirect from
aliases = {
    "what-is-otm.md": [
        "/2016/04/introduction-to-oracle.html"
    ],
    "basic-logistics-terminology.md": [
        "/2016/05/otm-basic-terminology.html"
    ],
    "otm-architecture-this-is-applicable-for-on-premise-installations.md": [
        "/2016/04/otm-architecture.html"
    ],
    "otm-inbound-integrations-xml.md": [
        "/2016/04/otm-inbound-integrations.html"
    ],
    "otm-outbound-integrations.md": [
        "/2016/04/otm-outbound-integrations.html"
    ],
    "otm-domains-standard-schema-and-data-dictionary.md": [
        "/2016/05/otm-data-structure.html"
    ],
    "otm-order-management-data-structure.md": [
        "/2016/05/otm-order-management-data-structure.html"
    ],
    "otm-shipment-management-data-structure.md": [
        "/2016/05/otm-shipment-management-data-structure.html"
    ],
    "otm-contract-rate-management-data-structure.md": [
        "/2016/05/otm-contract-rate-management-data.html"
    ],
    "business-process-automation-data-structure.md": [
        "/2016/05/business-process-automation-data.html"
    ],
    "csv-data-uploads.md": [
        "/2026/03/csv-data-uploads.html"
    ],
    "posting-data-to-otm-using-http-request.md": [
        "/2026/03/posting-data-to-otm-using-http-request.html"
    ],
    "basic-otm-configurations-01-domain-items-locations-and-equipment.md": [
        "/2020/08/basic-otm-configurations-01-domain.html",
        "/2020/06/basic-otm-configurations.html"
    ],
    "basic-otm-configurations-02-itinerary.md": [
        "/2020/08/basic-otm-configurations-02-itinerary.html"
    ],
    "basic-otm-configurations-03-service-provider-and-rates.md": [
        "/2020/08/basic-otm-configurations-03-service.html"
    ],
    "basic-otm-configurations-04-business-numbers-planning-parameter.md": [
        "/2020/08/basic-otm-configurations-04-business.html"
    ],
    "basic-otm-configurations-05-bulk-plan.md": [
        "/2020/08/basic-otm-configurations-05-bulk-plan.html"
    ],
    "basic-otm-configurations-06-tender-process.md": [
        "/2020/08/basic-otm-configurations-06-tender.html"
    ],
    "basic-otm-configurations-07-invoicing.md": [
        "/2020/08/basic-otm-configurations-07-invoicing.html"
    ],
    "basic-otm-configurations-08-voucher-allocation.md": [
        "/2020/08/basic-otm-configurations-08-voucher.html"
    ],
    "saved-queriesconditions.md": [
        "/2016/07/saved-queriesconditions.html"
    ],
    "agents-sample-agent-creation-steps.md": [
        "/2016/08/agents-sample-agent-creation-steps.html"
    ],
    "agents-frequently-used-actions.md": [
        "/2016/08/agents-frequently-used-actions.html"
    ],
    "agents-agent-event-restrictions.md": [
        "/2016/08/agents-agent-event-restrictions.html"
    ],
    "report-development-sample-report.md": [
        "/2016/10/report-development-sample-report_21.html"
    ],
    "report-workspaces.md": [
        "/2017/06/report.html"
    ],
    "emailing-reports-to-users-on-a-business-event.md": [
        "/2016/11/emailing-reports-to-users.html"
    ],
    "user-roles-vpd-and-access-control-lists.md": [
        "/2016/12/user-roles-vpd-and-access-control-lists.html"
    ],
    "user-menu-and-manage-user-access.md": [
        "/2017/04/user-menu-and-manage-user-access.html"
    ],
    "manager-layouts-screen-sets-labels.md": [
        "/2017/04/manager-layouts-screen-sets-labels.html"
    ],
    "advanced-layouts.md": [
        "/2017/04/advanced-layouts.html"
    ],
    "flex-fields.md": [
        "/2017/04/flex-fields.html"
    ],
    "refnums.md": [
        "/2017/07/refnums.html"
    ],
    "status-types.md": [
        "/2017/07/status-types.html"
    ],
    "g-log-properties.md": [
        "/2017/08/g-log-properties.html"
    ],
    "otm-application-admin-notes.md": [
        "/2017/08/otm-application-admin-notes.html"
    ],
    "oracle-dba-notes.md": [
        "/2017/08/oracle-dba-notes.html"
    ],
    "service-provider-user-login-creation.md": [
        "/2018/01/service-provider-user-login-creation.html"
    ],
    "action-checks.md": [
        "/2018/09/action-checks.html"
    ],
    "custom-actions-smart-links.md": [
        "/2018/09/custom-actions.html"
    ],
    "agent-gates.md": [
        "/2026/02/agent-gates.html"
    ],
    "business-monitors.md": [
        "/2026/02/business-monitors.html"
    ],
    "business-numbers.md": [
        "/2026/02/business-numbers.html"
    ],
    "yard-management-and-appointment-scheduling.md": [
        "/2026/02/yard-management.html"
    ],
    "workbenches.md": [
        "/2026/05/workbenches.html"
    ],
}

updated = 0
for fname, alias_list in aliases.items():
    fpath = os.path.join(POSTS_DIR, fname)
    if not os.path.exists(fpath):
        print(f"SKIPPED (not found): {fname}")
        continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if aliases already added
    if 'aliases:' in content:
        print(f"Already has aliases: {fname}")
        continue

    # Build alias block
    alias_block = "aliases:\n"
    for a in alias_list:
        alias_block += f'  - "{a}"\n'

    # Insert before closing --- of front matter
    content = content.replace('---\n\n', f'{alias_block}---\n\n', 1)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    updated += 1
    print(f"Added aliases: {fname}")

print(f"\nDone! Updated {updated} files.")
