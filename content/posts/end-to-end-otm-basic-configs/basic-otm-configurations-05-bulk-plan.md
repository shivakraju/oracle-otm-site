---
title: "Bulk Plan"
date: 2020-08-22T04:52:00+00:00
draft: false
weight: 200
tags:
  - "OTM"
  - "Bulk Plan"
  - "Oracle"
aliases:
  - "/posts/basic-otm-configurations-05-bulk-plan/"
  - "/2020/08/basic-otm-configurations-05-bulk-plan.html"
keywords:
  - "Oracle OTM bulk plan configuration steps"
  - "OTM bulk plan run order release"
  - "Oracle OTM purchase order bulk plan"
  - "OTM bulk plan shipment creation"
  - "Oracle OTM order base bulk plan"
  - "OTM ONE_TO_ONE order configuration"
  - "Oracle Transportation Management bulk plan walkthrough"
  - "OTM bulk plan planning parameter setup"
  - "Oracle OTM freight consolidation bulk plan"
  - "OTM DC source location bulk plan"
description: "Walks through creating a purchase order and running Bulk Plan in Oracle OTM to generate shipments, as part of the basic end-to-end configuration series."
---

Bulk Plan is OTM's automated planning engine. It reads Order Releases, matches them against the Itineraries and Rate Records configured in earlier posts, and creates optimised Shipments with carrier assignments and freight cost.

**Create an Order Base:**

An Order Base (Purchase Order) represents a buying commitment for a quantity of goods. Order Releases drawn from it represent shipments of specific quantities.

<div class="step-box">Order Management > Purchase Order > Order Base > New</div>

Enter the following details for the TCRP scenario:

<div class="field-box"><strong>Order Base ID:</strong> PO2018051001</div>

<div class="field-box"><strong>Order Configuration:</strong> ONE_TO_ONE</div>

<div class="field-box"><strong>Item ID:</strong> ITEMA01</div>

<div class="field-box"><strong>Source Location ID:</strong> DC_TCRP</div>

<div class="field-box"><strong>Destination Location ID:</strong> STORE_B</div>

<div class="field-box"><strong>Total Package Count:</strong> 100</div>

<div class="note-box"><strong>Note:</strong> Order Configuration <strong>ONE_TO_ONE</strong> means each Order Release will generate exactly one Shipment. This is the simplest configuration and appropriate for this scenario.</div>

**Create two Order Releases:**

Order Releases represent specific quantities being released for shipment against the Order Base. Create two releases for different quantities.

<div class="step-box">Order Base > Actions > Order Management > Change Order > Release Lines > New Release Instruction</div>

Create the first release:

<div class="field-box"><strong>Unit Amount:</strong> 20 (quantity being released for shipping)</div>

Repeat the same path to create a second release:

<div class="field-box"><strong>Unit Amount:</strong> 10 (quantity being released for shipping)</div>

**Run Bulk Plan:**

Query for the two Order Releases you just created:

![Order Release query results showing two order releases ready for planning](/images/basic-otm-configurations-05-bu-img1-3c464757b9.png)

Select both Order Releases and run Bulk Plan:

<div class="step-box">Select Order Releases > Actions > Operational Planning > Create Buy Shipment > Bulk Plan – Buy</div>

OTM evaluates the available Itineraries and Rate Records and creates a single consolidated Shipment covering both Order Releases, assigning the least-cost carrier for the lane.

**Shipment Routing Options:**

To understand how OTM selects a route, use Shipment Routing Options before running Bulk Plan. This is useful when verifying your Rate and Itinerary configuration.

The rates configured for this scenario are:

![Rate records showing carrier, equipment, and cost for each lane](/images/basic-otm-configurations-05-bu-img2-1e8cf7b957.png)

Create a new Order Release with Source = DC and Destination = STORE_C, then request routing options:

<div class="step-box">Order Release > Actions > Operational Planning > Show Routing Options</div>

OTM evaluates all matching Itineraries and presents two routing options — one direct (ITIN-B: DC → STORE_C) and one multi-leg (ITIN-D: DC → STORE_A → STORE_C):

![Two routing options shown — ITIN-B direct and ITIN-D multi-leg](/images/basic-otm-configurations-05-bu-img3-bad36e64d2.png)

Select both Itineraries and click **Show Options** to see the cost breakdown for each:

![Cost and carrier details for both itinerary options](/images/basic-otm-configurations-05-bu-img4-485c789a85.png)

The results confirm our configuration is correct:

- **ITIN-B** (DC → STORE_C direct): SGTM, 53-FT, $75
- **ITIN-D** (DC → STORE_A → STORE_C, two legs): Leg 1 PNDP $20 + Leg 2 SGTM $20 = **$40 total**

When you run Bulk Plan on this Order Release, OTM selects ITIN-D as the least-cost option and creates two Shipments:

- Shipment 1: PNDP, DC → STORE_A, $20
- Shipment 2: SGTM, STORE_A → STORE_C, $20

![Shipment list showing two planned shipments with carriers and costs](/images/basic-otm-configurations-05-bu-img5-5117392ac6.png)

OTM has identified the carrier for each leg. The next step is to notify (tender) those carriers with the pickup dates, times, and location details.

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-04-business-numbers-planning-parameter/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Business Numbers, Planning Parameter</div>
  </a>  <a href="/posts/basic-otm-configurations-06-tender-process/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Tender Process</div>
  </a></div>
