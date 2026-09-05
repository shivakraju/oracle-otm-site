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

![Overview diagram showing DC in Indianapolis distributing to three store locations](/images/basic-otm-configurations-01-do-img1-d2cb92713c.png)

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