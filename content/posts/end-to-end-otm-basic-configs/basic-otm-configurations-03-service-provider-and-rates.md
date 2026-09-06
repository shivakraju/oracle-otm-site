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

Define the remaining Rate Records for all other lanes in the same way:

![Rate Records list showing all lanes for SGTM](/images/basic-otm-configurations-03-se-img3-bae23963e6.png)

![Rate Records list showing lanes for PNDP](/images/basic-otm-configurations-03-se-img4-1e8cf7b957.png)

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-02-itinerary/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Itinerary</div>
  </a>  <a href="/posts/basic-otm-configurations-04-business-numbers-planning-parameter/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Business Numbers, Planning Parameter</div>
  </a></div>
