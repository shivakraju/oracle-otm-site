---
title: "Business Numbers, Planning Parameter"
date: 2020-08-22T04:47:00+00:00
draft: false
weight: 190
tags:
  - "Business Number"
  - "Planning Parameter"
  - "OTM"
  - "Oracle"
aliases:
  - "/posts/basic-otm-configurations-04-business-numbers-planning-parameter/"
  - "/2020/08/basic-otm-configurations-04-business.html"
  - "/posts/end-to-end-otm-basic-configs/basic-otm-configurations-04-business-numbers-planning-parameter/"
url: "/posts/end-to-end-otm-basic-configs/business-numbers-planning-parameter/"
keywords:
  - "Oracle OTM business number rule configuration"
  - "OTM shipment number sequence setup"
  - "Oracle OTM planning parameter configuration"
  - "OTM business number XID rule"
  - "Oracle OTM bulk plan planning parameter"
  - "OTM custom shipment ID configuration"
  - "Oracle Transportation Management numbering setup"
  - "OTM business number rule TCRP domain"
  - "Oracle OTM planning parameter setup steps"
  - "OTM default business number override"
description: "Explains how to configure custom Business Number rules and Planning Parameters in Oracle OTM to control how shipment and order IDs are generated during bulk planning."
---

**Business Numbers:**

OTM auto-generates IDs for business objects — shipments, order releases, invoices — using Business Number Rules. By default, shipments get a simple sequential number (e.g. 01001). A custom rule lets you embed the date, a prefix, or a domain-specific sequence into the generated ID, making it easier to identify records and align with your organisation's numbering conventions.

The default shipment number looks like this:

![Default OTM shipment number showing sequential ID format](/images/basic-otm-configurations-04-bu-img1-18e64bcaca.png)

To customise the shipment number format, edit the Business Number Rule for the TCRP domain:

<div class="step-box">Business Process Automation > Power Data > Business Numbers > Business Number Rule > Search for %SHIPMENT%</div>

You will see a default rule at the TCRP domain level for generating the XID. Edit this rule:

![Business Number Rule list showing the default SHIPMENT rule for TCRP domain](/images/basic-otm-configurations-04-bu-img2-0ce1184927.png)

Build a new rule using a combination of static and dynamic expressions:

<div class="field-box"><strong>'SHIP'</strong> — static prefix</div>

<div class="field-box"><strong>{dddddddd:id=1}</strong> — date in YYYYMMDD format (dynamic)</div>

<div class="field-box"><strong>'-'</strong> — static hyphen separator</div>

<div class="field-box"><strong>{nnnnn:start=01000}</strong> — five-digit sequence starting at 01000 (dynamic)</div>

![Business Number Rule editor showing the four expression components](/images/basic-otm-configurations-04-bu-img3-73428c0a62.png)

With this rule in place, planned shipments generate IDs in the format `SHIP20200822-01000`:

![Shipment list showing newly generated ID in the custom format](/images/basic-otm-configurations-04-bu-img4-ffe4ea06c0.png)

**Planning Parameter:**

A Planning Parameter Set controls the behaviour of OTM Bulk Plan — consolidation rules, time windows, cost optimisation settings, and more. Each domain should have its own parameter set so plan settings can be tuned independently.

Create a new parameter set for the TCRP domain:

<div class="step-box">Shipment Management > Power Data > General > Parameter Sets > New</div>

<div class="field-box"><strong>Parameter Set ID:</strong> TCRP_PLAN</div>

![Planning Parameter Set screen for TCRP_PLAN with default values](/images/basic-otm-configurations-04-bu-img5-a647769878.png)

<div class="note-box"><strong>Note:</strong> All parameters in the set control how the Bulk Plan algorithm works — consolidation windows, maximum stops, weight/volume thresholds, etc. For this scenario we proceed with default values. In production these are tuned to match business planning rules.</div>

Set TCRP_PLAN as the default planning parameter for the TCRP domain so it is pre-selected each time a Bulk Plan is submitted:

<div class="step-box">Configuration and Administration > Domain Management > Domain Settings > Search > Select TCRP > Edit > Set Parameter Set ID = TCRP_PLAN > Finished</div>

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-03-service-provider-and-rates/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Service Provider and Rates</div>
  </a>  <a href="/posts/basic-otm-configurations-05-bulk-plan/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Bulk Plan</div>
  </a></div>
