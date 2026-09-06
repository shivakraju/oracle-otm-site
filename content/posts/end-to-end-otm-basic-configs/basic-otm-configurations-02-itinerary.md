---
title: "Itinerary"
date: 2020-08-22T04:32:00+00:00
draft: false
weight: 170
tags:
  - "Multi-leg"
  - "Itinerary"
  - "Leg"
aliases:
  - "/posts/basic-otm-configurations-02-itinerary/"
  - "/2020/08/basic-otm-configurations-02-itinerary.html"
keywords:
  - "Oracle OTM itinerary configuration"
  - "OTM multi-leg itinerary setup"
  - "Oracle OTM route itinerary definition"
  - "OTM leg source destination configuration"
  - "Oracle Transportation Management itinerary setup"
  - "OTM itinerary bulk plan configuration"
  - "Oracle OTM lane itinerary definition"
  - "OTM itinerary leg sequence"
  - "Oracle OTM basic configuration itinerary"
  - "OTM route configuration steps"
description: "Explains how to define itineraries in Oracle OTM as part of the basic configuration series, including setting up source-to-destination legs used during bulk plan route optimization."
---

An Itinerary defines the route OTM Bulk Plan uses to move freight — the origin region, destination region, transport mode, and equipment types for each leg. Bulk Plan matches order release origins and destinations against itinerary lanes to determine which route to use. Without a matching itinerary, planning will fail.

For the TCRP scenario we defined four itineraries — three single-leg and one multi-leg. Refer to the [business scenario](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/) for the full network diagram.

**Itinerary summary:**

![Table showing ITIN-A through ITIN-D with source, destination, carriers, and equipment](/images/basic-otm-configurations-02-it-img1-f4ab54eb77.png)

<div class="note-box"><strong>S</strong> = Source Location &nbsp;&nbsp; <strong>D</strong> = Destination Location</div>

**Create itineraries:**

<div class="step-box">Shipment Management > Itinerary Management > Itinerary</div>

![Itinerary list screen showing ITIN-A, ITIN-B, ITIN-C, ITIN-D](/images/basic-otm-configurations-02-it-img2-247e7d669f.png)

**Single-leg itineraries (ITIN-A, ITIN-B, ITIN-C):**

ITIN-A, ITIN-B, and ITIN-C are each single-leg itineraries — one direct lane from source to destination. The header defines the lane (source and destination location groups) and the leg defines the transport mode and equipment types.

![ITIN-A header showing source and destination lane](/images/basic-otm-configurations-02-it-img3-a577b1ef97.png)

![ITIN-A leg details showing transport mode and equipment group profile](/images/basic-otm-configurations-02-it-img4-0847727dcb.png)

![ITIN-B configuration screen](/images/basic-otm-configurations-02-it-img5-51c047e157.png)

![ITIN-C configuration screen](/images/basic-otm-configurations-02-it-img6-d142177af0.png)

**Multi-leg itinerary (ITIN-D):**

ITIN-D is a multi-leg itinerary — DC to LOC-A (Leg 1), then LOC-A to LOC-B (Leg 2). The itinerary header shows only the overall source and final destination; the intermediate stop (LOC-A) is defined at the leg level.

<div class="note-box"><strong>Note:</strong> The lane definition on the itinerary header shows the source location and final destination only. Intermediate stops are configured within each leg.</div>

![ITIN-D header showing DC as source and LOC-B as final destination](/images/basic-otm-configurations-02-it-img7-d892b20abc.png)

![ITIN-D lane definition screen](/images/basic-otm-configurations-02-it-img8-8c9ab76fab.png)

**Leg 1 — DC to LOC-A:**

![ITIN-D Leg 1 header showing sequence and name](/images/basic-otm-configurations-02-it-img9-67a3ab1305.png)

![ITIN-D Leg 1 details showing source DC, destination LOC-A, transport mode, and equipment](/images/basic-otm-configurations-02-it-img10-e716e063ec.png)

**Leg 2 — LOC-A to LOC-B:**

![ITIN-D Leg 2 header](/images/basic-otm-configurations-02-it-img11-fbaf4986c2.png)

![ITIN-D Leg 2 details showing source LOC-A, destination LOC-B, transport mode, and equipment](/images/basic-otm-configurations-02-it-img12-770a4132df.png)

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Domain, Items, Locations, and Equipment</div>
  </a>  <a href="/posts/basic-otm-configurations-03-service-provider-and-rates/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Service Provider and Rates</div>
  </a></div>