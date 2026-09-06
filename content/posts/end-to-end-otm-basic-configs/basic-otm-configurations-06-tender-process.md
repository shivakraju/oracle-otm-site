---
title: "Tender Process"
date: 2020-08-22T04:55:00+00:00
draft: false
weight: 210
tags:
  - "OTM"
  - "Oracle"
  - "Tender"
aliases:
  - "/posts/basic-otm-configurations-06-tender-process/"
  - "/2020/08/basic-otm-configurations-06-tender.html"
keywords:
  - "Oracle OTM tender process configuration"
  - "OTM secure resources tender shipment"
  - "Oracle OTM tender carrier notification"
  - "OTM shipment tender accepted status"
  - "Oracle OTM tender offer to carrier"
  - "OTM SECURE_RESOURCES_NOT_STARTED status"
  - "Oracle Transportation Management tender workflow"
  - "OTM tender process steps"
  - "Oracle OTM shipment management tender"
  - "OTM carrier tender EDI XML"
description: "Demonstrates the Oracle OTM tender process, showing how to notify a carrier about a shipment using the Secure Resources action, and how shipment statuses change through the tender lifecycle."
---

After Bulk Plan creates Shipments, the next step is to notify the carrier — this is called Tendering. The carrier receives the shipment details (pickup time, locations, equipment), then accepts or rejects the tender. If rejected, OTM automatically re-tenders to the next available carrier on the lane.

**Shipment status after Bulk Plan:**

When shipments are first created by Bulk Plan, their Secure Resources status is **SECURE_RESOURCES_NOT_STARTED**, meaning no tender has been sent yet.

![Shipment list showing SECURE_RESOURCES_NOT_STARTED status after Bulk Plan](/images/basic-otm-configurations-06-te-img1-70d35394c8.png)

**Send the tender:**

<div class="step-box">Shipment > Actions > Shipment Management > Tender > Secure Resources</div>

![Secure Resources action dialog for selected shipments](/images/basic-otm-configurations-06-te-img2-96cea8f493.png)

After this action the Secure Resources status changes to **TENDERED**. OTM sends a tender notification to the carrier — this can be an XML message to an external TMS/EDI system, or an email notification, depending on the configuration at the Service Provider level.

**Carrier accept / reject:**

The carrier responds to the tender in one of two ways:

- Via EDI integration (automated, in production)
- By logging into OTM with the **Service Provider** role and accepting or rejecting manually

For manual login, the default credentials follow this format:

<div class="field-box"><strong>User ID:</strong> SERVPROV.DOMAIN-SCAC (e.g. SERVPROV.TCRP-PNDP)</div>

<div class="field-box"><strong>Password:</strong> CHANGEME</div>

In this scenario, login as the PNDP carrier first and decline the tender:

![OTM login screen using Service Provider credentials for PNDP](/images/basic-otm-configurations-06-te-img3-34e7fdac05.png)

The carrier sees outstanding tenders in their queue:

![Tender list showing the outstanding tender for the PNDP carrier](/images/basic-otm-configurations-06-te-img4-5be841085c.png)

<div class="step-box">Select the record > Actions > Accept / Decline</div>

Decline this tender as the PNDP carrier. Then login as the SGTM carrier and accept the tender for the second leg.

**OTM re-tenders automatically:**

After PNDP rejects the first leg, go back to TCRP.ADMIN and review the shipments:

![Shipment list showing OTM has re-tendered the first leg to SGTM at $30](/images/basic-otm-configurations-06-te-img5-f89924dec9.png)

OTM automatically re-tendered the first leg to the next available carrier — SGTM — at the $30 rate defined in the Rate Records for that lane.

![Shipment detail showing SGTM assigned to first leg after PNDP rejection](/images/basic-otm-configurations-06-te-img6-bae23963e6.png)

Login as SERVPROV.TCRP-SGTM to see the new tender for the first leg:

![OTM tender queue for SGTM showing the re-tendered first leg shipment](/images/basic-otm-configurations-06-te-img7-06b4e21ec1.png)

Accept this tender. Both shipments now show Secure Resources status as **ACCEPTED**:

![Shipment list showing both shipments with tender status ACCEPTED](/images/basic-otm-configurations-06-te-img8-8c7043a964.png)

With both legs tendered and accepted, the shipments are confirmed with their carriers and ready for the next step: invoicing.

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-05-bulk-plan/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Bulk Plan</div>
  </a>  <a href="/posts/basic-otm-configurations-07-invoicing/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Invoicing</div>
  </a></div>
