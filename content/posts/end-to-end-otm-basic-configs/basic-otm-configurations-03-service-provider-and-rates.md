---
title: "Service Provider and Rates"
date: 2020-08-22T04:43:00+00:00
draft: false
weight: 180
tags:
  - "RATE_OFFERING"
  - "Rate Record"
  - "Rate Service"
  - "Rates"
  - "RATE_SERVICE"
  - "Service Provider"
  - "RATE_GEO"
  - "Rate Offering"
aliases:
  - "/posts/basic-otm-configurations-03-service-provider-and-rates/"
  - "/2020/08/basic-otm-configurations-03-service.html"
keywords:
  - "Oracle OTM service provider setup"
  - "OTM carrier rate configuration"
  - "Oracle OTM rate offering rate service setup"
  - "OTM SCAC code service provider"
  - "Oracle OTM rate record configuration"
  - "OTM RATE_GEO lane rate setup"
  - "Oracle OTM carrier contract rate entry"
  - "OTM service provider SCAC country code"
  - "Oracle Transportation Management rate setup steps"
  - "OTM basic configuration carrier rates"
description: "Covers how to define service providers with SCAC codes and configure rate offerings, rate services, and rate records in Oracle OTM as part of the basic end-to-end configuration series."
---

OTM models carrier contracting in two layers: a **Rate Offering** (the contract — who, what transport mode, what service level) and **Rate Records** (the lanes — source, destination, and cost). Bulk Plan uses Rate Offerings and Rate Records to select a carrier and calculate freight cost for each shipment leg.

**Service Provider:**

A Service Provider (carrier) must exist in OTM before a Rate Offering can be created. Each carrier requires a SCAC code — the four-letter industry identifier that uniquely distinguishes them.

<div class="step-box">Contract and Rate Management > Service Provider Manager</div>

Define two service providers for the TCRP scenario:

<div class="field-box"><strong>SGTM</strong> — SCAC: SGTM, Country Code: USA</div>

<div class="field-box"><strong>PNDP</strong> — SCAC: PNDP, Country Code: USA</div>

![Service Provider list showing SGTM and PNDP](/images/basic-otm-configurations-03-se-img1-d84a74c0db.png)

**Rate Offering:**

A Rate Offering defines the high-level contract between your organisation and a carrier — the transport mode, rate service (transit time method), and distance engine. Create one Rate Offering per carrier.

<div class="step-box">Contract and Rate Management > Contract Management > Rate Offering</div>

Create the Rate Offering for carrier SGTM with the following details:

<div class="field-box"><strong>Offering ID:</strong> SGTM_TL</div>

<div class="field-box"><strong>Offering Type:</strong> TL</div>

<div class="field-box"><strong>Service Provider:</strong> SGTM</div>

<div class="field-box"><strong>Rate Service ID:</strong> TL-SIM</div>

<div class="field-box"><strong>Version:</strong> EXP2020 (New)</div>

<div class="field-box"><strong>Rate Distance ID:</strong> LOOKUP ELSE ESTIMATE</div>

<div class="note-box"><strong>Note:</strong> TL-SIM and LOOKUP ELSE ESTIMATE are default Rate Service and Rate Distance configurations provided by Oracle. For production implementations it is possible to configure external engines such as PC*MILER for mileage and RATEWARE XL for LTL rate calculations.</div>

**Rate Records:**

Rate Records define the cost for each lane (source city to destination city) within the Rate Offering. Each lane the carrier serves needs a separate Rate Record.

<div class="step-box">Open Rate Offering > Actions > Create Rate Record</div>

Create the first Rate Record for the DC to LOC-B lane (Indianapolis to Charlotte):

<div class="field-box"><strong>Rate Record ID:</strong> SGTM_TL_DC_STOREB</div>

<div class="field-box"><strong>Source Geo Hierarchy:</strong> CITY</div>

<div class="field-box"><strong>Source City / Province / Country:</strong> INDIANAPOLIS / IN / USA</div>

<div class="field-box"><strong>Destination Geo Hierarchy:</strong> CITY</div>

<div class="field-box"><strong>Destination City / Province / Country:</strong> CHARLOTTE / NC / USA</div>

<div class="field-box"><strong>Rate Cost:</strong> 100 USD PER BUY SHIPMENT</div>

![Rate Record screen for SGTM_TL_DC_STOREB showing lane and cost details](/images/basic-otm-configurations-03-se-img2-b7d3679583.png)

Define the remaining Rate Records for all other lanes in the same way. Below is the complete set of Rate Records for this scenario:

<div style="background:#f0f4f8;border:1px solid #d1dce8;border-radius:8px;padding:16px 20px;margin:16px 0;">
<svg viewBox="0 0 700 330" xmlns="http://www.w3.org/2000/svg" style="width:100%;max-width:660px;display:block;margin:0 auto 16px;">
  <defs>
    <marker id="arr3" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto">
      <path d="M0,0 L0,6 L8,3 z" fill="#4a8bb5"/>
    </marker>
  </defs>
  <line x1="268" y1="90" x2="165" y2="248" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr3)"/>
  <line x1="320" y1="97" x2="320" y2="252" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr3)"/>
  <line x1="372" y1="82" x2="530" y2="152" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr3)"/>
  <line x1="215" y1="272" x2="288" y2="272" stroke="#4a8bb5" stroke-width="1.6" marker-end="url(#arr3)"/>
  <text x="200" y="152" fill="#64748b" font-size="10" text-anchor="end" font-family="Consolas,monospace">SGTM  20-FT  $30</text>
  <text x="200" y="164" fill="#64748b" font-size="10" text-anchor="end" font-family="Consolas,monospace">SGTM  40-FT  $50</text>
  <text x="200" y="176" fill="#64748b" font-size="10" text-anchor="end" font-family="Consolas,monospace">PNDP  20-FT  $20</text>
  <text x="200" y="188" fill="#64748b" font-size="10" text-anchor="end" font-family="Consolas,monospace">PNDP  40-FT  $40</text>
  <text x="356" y="172" fill="#64748b" font-size="10" font-family="Consolas,monospace">SGTM</text>
  <text x="356" y="184" fill="#64748b" font-size="10" font-family="Consolas,monospace">53-FT  $75</text>
  <text x="480" y="118" fill="#64748b" font-size="10" text-anchor="start" font-family="Consolas,monospace">SGTM  40-FT  $50</text>
  <text x="252" y="312" fill="#64748b" font-size="10" text-anchor="middle" font-family="Consolas,monospace">SGTM  20-FT  $20</text>
  <rect x="282" y="52" width="76" height="36" rx="6" fill="#1c3557"/>
  <text x="320" y="75" fill="#fff" font-size="13" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">DC</text>
  <rect x="115" y="254" width="96" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="163" y="277" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">STORE_A</text>
  <rect x="282" y="254" width="76" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="320" y="277" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">STORE_C</text>
  <rect x="500" y="152" width="96" height="36" rx="6" fill="#fff" stroke="#1c3557" stroke-width="1.8"/>
  <text x="548" y="175" fill="#1c3557" font-size="12" font-weight="bold" text-anchor="middle" font-family="Consolas,monospace">STORE_B</text>
</svg>
<table style="width:100%;border-collapse:collapse;font-size:13px;">
  <thead><tr style="background:#e8f0f8;">
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Rate Record</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Source</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Destination</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Equipment</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Carrier</th>
    <th style="padding:8px 12px;text-align:left;font-size:10px;letter-spacing:.07em;text-transform:uppercase;color:#64748b;border-bottom:1px solid #d1dce8;">Rate (USD)</th>
  </tr></thead>
  <tbody>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-family:Consolas,monospace;font-size:12px;font-weight:600;color:#1c3557;">SGTM_TL_DC_STOREB</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_B</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">40-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$50</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-family:Consolas,monospace;font-size:12px;font-weight:600;color:#1c3557;">SGTM_TL_DC_STOREC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_C</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">53-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$75</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-family:Consolas,monospace;font-size:12px;font-weight:600;color:#1c3557;" rowspan="2">SGTM_TL_DC_STOREA</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">20-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$30</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">40-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">SGTM</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$50</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-family:Consolas,monospace;font-size:12px;font-weight:600;color:#1c3557;" rowspan="2">PNDP_TL_DC_STOREA</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">20-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">PNDP</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$20</td></tr>
    <tr><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">DC</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">STORE_A</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">40-FT</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;">PNDP</td><td style="padding:8px 12px;border-bottom:1px solid #e2e8f0;font-weight:600;color:#16a34a;">$40</td></tr>
    <tr><td style="padding:8px 12px;font-family:Consolas,monospace;font-size:12px;font-weight:600;color:#1c3557;">SGTM_TL_STOREA_STOREC</td><td style="padding:8px 12px;">STORE_A</td><td style="padding:8px 12px;">STORE_C</td><td style="padding:8px 12px;">20-FT</td><td style="padding:8px 12px;">SGTM</td><td style="padding:8px 12px;font-weight:600;color:#16a34a;">$20</td></tr>
  </tbody>
</table>
</div>

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-02-itinerary/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Itinerary</div>
  </a>  <a href="/posts/basic-otm-configurations-04-business-numbers-planning-parameter/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Business Numbers, Planning Parameter</div>
  </a></div>
