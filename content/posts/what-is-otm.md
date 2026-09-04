---
title: "What is OTM ?"
date: 2016-04-14T21:35:00+00:00
draft: false
weight: 10
tags:
  - "G-log"
  - "Introduction"
  - "Basics"
  - "OTM"
  - "Learn"
  - "Oracle"
aliases:
  - "/2016/04/introduction-to-oracle.html"
keywords:
  - "Oracle Transportation Management OTM overview"
  - "what is Oracle OTM"
  - "OTM software introduction"
  - "Oracle OTM G-log history"
  - "OTM freight management system"
  - "Oracle OTM SaaS vs on-premise"
  - "OTM GlogXML integration overview"
  - "Oracle OTM bulk plan overview"
  - "OTM tender process overview"
  - "Oracle OTM order management introduction"
  - "OTM carrier freight consolidation"
  - "Oracle Transportation Management consultant guide"
description: "An introduction to Oracle Transportation Management (OTM), covering its origins as G-Log, core capabilities like order management, bulk planning, tendering, and invoicing, and how it integrates with ERP systems via GlogXML."
---

OTM stands for **Oracle Transportation Management**. It is a software product designed to automate various logistics business processes — receiving orders from source ERP systems for freight consolidation, optimizing routes and shipping costs, sending tender requests to carriers, receiving shipment tracking events, processing invoices, allocating freight costs to orders, and more.

**Some of the Core Capabilities of OTM:**

<div class="field-box"><strong>Order Management:</strong> Receive Purchase Orders (Order Base) from source ERP or legacy systems and create Order Releases (Bookings) for full or partial quantities, either manually or through automated release rules.</div>

<div class="field-box"><strong>Bulk Planning:</strong> Consolidate Order Releases (Bookings) with common source and destination locations, or build multi-stop shipments. The Bulk Plan algorithm identifies the optimal route (Itinerary), selects the least-cost carrier based on pre-configured rates, optimizes loading of items into equipment, and calculates in-transit times.</div>

<div class="field-box"><strong>Third-Party Rate and Distance Engines:</strong> OTM can dynamically fetch LTL rates from third-party engines such as <strong>SMC³ RateWare XL</strong>, and calculate distances between locations using mileage engines such as <strong>PC*MILER</strong> or <strong>MileMaker</strong>.</div>

<div class="field-box"><strong>Tendering:</strong> Send Tender Offer requests to the carriers identified during planning. If a carrier cannot accept XML tender files directly, middleware tools such as MuleSoft, Oracle BPEL, or similar integration platforms can be used to translate OTM outbound XML to carrier-readable formats such as EDI.</div>

<div class="field-box"><strong>Tender Response:</strong> Receive and process carrier tender responses and update the shipment accordingly.</div>

<div class="field-box"><strong>Shipment Tracking:</strong> Receive shipment tracking updates from carriers and update shipment status in OTM.</div>

<div class="field-box"><strong>Invoicing:</strong> Receive and process invoices from carriers, match invoice costs against planned costs for approval, create vouchers for approved invoices, and allocate freight costs back to customer orders.</div>

**Ease of Implementation:**

OTM is designed to be configured and customized by consultants for client-specific business needs with minimal technical expertise.

<div class="field-box"><strong>Functional consultants</strong> need basic logistics domain knowledge to configure the product based on the business requirements and Oracle documentation.</div>

<div class="field-box"><strong>IT/Technical consultants</strong> need basic Oracle SQL and XML knowledge for customizations and integrations.</div>

Latest OTM SaaS versions allow clients to focus purely on core business configurations, while Oracle manages the infrastructure, upgrades, and maintenance of all standard out-of-the-box features.

**History:**

OTM was originally developed by a company called **Global Logistics Technologies, Inc.** (also known as G-Log). Oracle acquired G-Log in 2005 and rebranded the product as OTM — Oracle Transportation Management.

**Integration:**

OTM has built-in integrations with Oracle E-Business Suite applications such as Oracle Shipping (WSH). It can also integrate with any external system by exchanging XML files based on **GlogXML.xsd** — Oracle's product-defined XML schema. Newer versions of OTM additionally support REST API-based integrations.

<div class="note-box"><strong>Note:</strong> OTM is not a module within Oracle E-Business Suite. It is a standalone product that requires its own installation — web, application, and database tiers for on-premise deployments. See the next topic <a href="/posts/otm-architecture-this-is-applicable-for-on-premise-installations/">OTM Architecture</a> for details.</div>
