---
title: "Domain, Items, Locations, and Equipment"
date: 2020-08-22T05:25:00+00:00
draft: false
weight: 160
tags:
  - "Item"
  - "Equipment"
  - "domain"
  - "OTM"
  - "Oracle"
  - "Location"
aliases:
  - "/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/"
  - "/2020/08/basic-otm-configurations-01-domain.html"
  - "/2020/06/basic-otm-configurations.html"
keywords:
  - "Oracle OTM basic configuration domain setup"
  - "OTM domain item location equipment configuration"
  - "Oracle OTM location setup steps"
  - "OTM item master configuration"
  - "Oracle OTM equipment type setup"
  - "OTM end-to-end transaction configuration guide"
  - "Oracle Transportation Management initial setup"
  - "OTM domain creation configuration"
  - "Oracle OTM consultant configuration walkthrough"
  - "OTM basic setup domain items locations"
description: "First in a series of end-to-end OTM configuration posts, covering how to set up a domain, define items, create locations, and configure equipment types as the foundation for a working OTM transaction flow."
---

This is the first in a series of eight posts that walk through a complete OTM end-to-end transaction flow — from initial setup through planning, tendering, invoicing, and cost allocation. Each post builds on the previous one. Use this series as a starting point and refer to OTM Help documentation to explore each topic in depth.

**Business Scenario:**

Toys Corporation (TCRP) has one DC/Warehouse and three store locations in different cities. The DC distributes three items (Item A, Item B, Item C) to those stores. TCRP has contracts with two carriers (SGTM, PNDP) who use 20 ft, 40 ft, and 53 ft equipment. TCRP wants to use OTM Bulk Plan to optimise transport costs and settle carrier invoices.

<div style="background:#f0f4f8;border:1px solid #d1dce8;border-radius:8px;padding:16px 20px;margin:16px 0;font-family:'Consolas','Courier New',monospace;">
<div style="display:flex;gap:20px;flex-wrap:wrap;margin-bottom:16px;">
  <div style="background:#fff;border:1px solid #d1dce8;border-radius:6px;padding:10px 16px;">
    <div style="font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#64748b;margin-bottom:6px;">Carriers</div>
    <div style="display:flex;gap:8px;"><span style="background:#e8f0f8;border:1px solid #b8d0e8;border-radius:4px;padding:2px 10px;font-size:12px;font-weight:600;color:#1c3557;">SGTM</span><span style="background:#e8f0f8;border:1px solid #b8d0e8;border-radius:4px;padding:2px 10px;font-size:12px;font-weight:600;color:#1c3557;">PNDP</span></div>
  </div>
  <div style="background:#fff;border:1px solid #d1dce8;border-radius:6px;padding:10px 16px;">
    <div style="font-size:10px;letter-spacing:.1em;text-transform:uppercase;color:#64748b;margin-bottom:6px;">Equipment Types</div>
    <div style="display:flex;gap:8px;"><span style="background:#e8f0f8;border:1px solid #b8d0e8;border-radius:4px;padding:2px 10px;font-size:12px;font-weight:600;color:#1c3557;">20-FT</span><span style="background:#e8f0f8;border:1px solid #b8d0e8;border-radius:4px;padding:2px 10px;font-size:12px;font-weight:600;color:#1c3557;">40-FT</span><span style="background:#e8f0f8;border:1px solid #b8d0e8;border-radius:4px;padding:2px 10px;font-size:12px;font-weight:600;color:#1c3557;">53-FT</span></div>
  </div>
</div>
<svg viewBox="0 0 640 340" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:600px;display:block;margin:0 auto;">
  <defs>
    <marker id="arr2" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#4a8bb5"/>
    </marker>
  </defs>
  <line x1="268" y1="90" x2="168" y2="248" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr2)"/>
  <line x1="320" y1="97" x2="320" y2="248" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr2)"/>
  <line x1="372" y1="84" x2="490" y2="198" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr2)"/>
  <line x1="214" y1="272" x2="282" y2="272" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr2)"/>
  <text x="196" y="162" fill="#64748b" font-size="11" text-anchor="middle" font-family="Consolas,monospace">50 miles</text>
  <text x="196" y="174" fill="#1c64a0" font-size="10" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">Eqp: 20/40-FT</text>
  <text x="344" y="178" fill="#64748b" font-size="11" font-family="Consolas,monospace">75 miles</text>
  <text x="344" y="190" fill="#1c64a0" font-size="10" font-weight="bold" font-family="Consolas,monospace">Eqp: 53-FT</text>
  <text x="448" y="143" fill="#64748b" font-size="11" text-anchor="start" font-family="Consolas,monospace">100 miles</text>
  <text x="448" y="155" fill="#1c64a0" font-size="10" font-weight="bold" text-anchor="start" font-family="Consolas,monospace">Eqp: 40-FT</text>
  <text x="248" y="296" fill="#64748b" font-size="11" text-anchor="middle" font-family="Consolas,monospace">50 miles</text>
  <text x="248" y="308" fill="#1c64a0" font-size="10" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">Eqp: 20/40-FT</text>
  <rect x="282" y="52" width="76" height="36" rx="6" fill="#1c3557"/>
  <text x="320" y="75" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">DC</text>
  <rect x="120" y="254" width="88" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="164" y="277" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">LOC-A</text>
  <rect x="282" y="254" width="76" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="320" y="277" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">LOC-C</text>
  <rect x="460" y="200" width="88" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="504" y="223" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">LOC-B</text>
</svg>
<table style="width:100%;border-collapse:collapse;margin-top:16px;font-size:13px;">
  <thead><tr style="background:#e8f0f8;">
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Itinerary</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Route</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Carriers</th>
  </tr></thead>
  <tbody>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#1c3557;">ITIN-A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#1c64a0;">DC → LOC-B</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM, PNDP</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#1c3557;">ITIN-B</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#1c64a0;">DC → LOC-C</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#1c3557;">ITIN-C</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;color:#1c64a0;">DC → LOC-A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM, PNDP</td></tr>
    <tr><td style="padding:8px 12px;font-weight:600;color:#1c3557;">ITIN-D</td><td style="padding:8px 12px;color:#1c64a0;">DC → LOC-A → LOC-B</td><td style="padding:8px 12px;">SGTM, PNDP</td></tr>
  </tbody>
</table>
</div>

The locations map to real addresses:

<div class="field-box"><strong>DC_TCRP</strong> — DC/Warehouse in Indianapolis, IN 46202</div>

<div class="field-box"><strong>LOC_A</strong> — Store in Nashville, TN 37203</div>

<div class="field-box"><strong>LOC_B</strong> — Store in Charlotte, NC 28078</div>

<div class="field-box"><strong>LOC_C</strong> — Store in Atlanta, GA 30303</div>

![Map showing Indianapolis DC and the three store locations](/images/basic-otm-configurations-01-do-img2-729bca9542.png)

**Domain:**

Create a new domain TCRP to hold all configurations and transaction data for this business scenario.

<div class="step-box">Configuration and Administration > Domain Management > Add Domain</div>

![Add Domain screen with TCRP domain details](/images/basic-otm-configurations-01-do-img3-c3dc82dd27.png)

Log in to the new domain with the default credentials:

<div class="field-box"><strong>User:</strong> ADMIN</div>

<div class="field-box"><strong>Password:</strong> CHANGEME</div>

![Login screen for TCRP domain](/images/basic-otm-configurations-01-do-img4-2cf8fe190c.png)

![OTM home screen after logging into TCRP domain](/images/basic-otm-configurations-01-do-img5-3d014c7b9f.png)

**Items:**

Define three items — ITEMA01, ITEMA02, ITEMA03.

<div class="step-box">Order Management > Material Management > Item</div>

![Item creation screen showing ITEMA01](/images/basic-otm-configurations-01-do-img6-bd7cb8d0d2.png)

Set item weight and dimensions:

<div class="field-box"><strong>Weight:</strong> 2 LB</div>

![Item dimensions tab showing weight of 2 LB](/images/basic-otm-configurations-01-do-img7-a40bf90d33.png)

![Item dimensions showing length, width, height values](/images/basic-otm-configurations-01-do-img8-8bba784532.png)

**Locations:**

Create the four locations used in this scenario.

<div class="step-box">Shipment Management > Location Manager</div>

Create the DC/Warehouse location first with role Ship From:

<div class="field-box"><strong>Location GID:</strong> TCRP.DC_TCRP</div>

![DC_TCRP location header details](/images/basic-otm-configurations-01-do-img9-c911a8fa98.png)

![DC_TCRP location address tab](/images/basic-otm-configurations-01-do-img10-6cb1a6d6fb.png)

![DC_TCRP location role configuration](/images/basic-otm-configurations-01-do-img11-0095e94000.png)

Create the three store locations with role Ship To:

![Store locations LOC_A, LOC_B, LOC_C list view](/images/basic-otm-configurations-01-do-img12-1dd20378a4.png)

**Equipment:**

Define equipment groups for the three container sizes used by the carriers.

<div class="step-box">Shipment Management > Equipment Management > Equipment Groups</div>

Create groups 20_FT, 40_FT, and 53_FT with their dimensions and capacity:

![Equipment groups list showing 20_FT, 40_FT, 53_FT](/images/basic-otm-configurations-01-do-img13-e748421598.png)

Define an Equipment Group Profile that groups these equipment types for assignment to itinerary legs:

<div class="step-box">Shipment Management > Equipment Management > Equipment Group Profile</div>

![Equipment Group Profile header](/images/basic-otm-configurations-01-do-img14-504d5e728e.png)

![Equipment Group Profile details showing 20_FT, 40_FT, 53_FT assigned](/images/basic-otm-configurations-01-do-img15-032b315090.png)

**Basic OTM Configurations:**

[Itinerary →](/posts/basic-otm-configurations-02-itinerary/)