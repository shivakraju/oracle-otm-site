---
title: "Product Architecture"
date: 2016-04-15T14:54:00+00:00
draft: false
weight: 35
tags:
  - "Architecture"
  - "OTM"
  - "3 tier"
  - "Oracle"
  - "WebLogic"
aliases:
  - "/2016/04/otm-architecture.html"
keywords:
  - "Oracle OTM product architecture"
  - "OTM three tier architecture"
  - "Oracle OTM web tier app tier database tier"
  - "OTM Oracle HTTP Server OHS"
  - "OTM WebLogic application server"
  - "OTM mod_wl_ohs connector"
  - "Oracle OTM UI component business component"
  - "OTM GLOGOWNER REPORTOWNER schema"
  - "Oracle Transportation Management architecture overview"
  - "OTM on-premise SaaS architecture"
  - "OTM JDBC database connection"
  - "Oracle OTM GC3 application tier"
description: "An overview of Oracle OTM's three-tier product architecture â€” covering the Web Tier (Oracle HTTP Server), Application Tier (Oracle WebLogic with UI and Business components), and Database Tier (Oracle Database with GLOGOWNER and REPORTOWNER schemas)."
---

OTM follows a standard **three-tier architecture** â€” a widely used design in enterprise software where the application is split into three distinct layers: Web Tier, Application Tier, and Database Tier. Each tier has a specific responsibility, and together they allow OTM to scale, be maintained, and support many users simultaneously.

Depending on the deployment model â€” on-premise or SaaS â€” the underlying infrastructure differs, but the three-tier concept remains the same. In on-premise deployments, your organization manages each tier on its own servers. In SaaS (cloud) deployments, Oracle manages the infrastructure and these tiers are hosted and maintained by Oracle.

**The Three Tiers:**

<div class="tier-web">
<strong>Web Tier (Presentation Layer):</strong> Runs on Oracle HTTP Server (OHS). It receives browser requests from end users. Static content such as OTM help pages, labels, and JavaScript files are served directly from this tier. Dynamic requests (such as running Bulk Plan or searching for shipments) are forwarded to the Application Tier via the <strong>mod_wl_ohs</strong> connector.
</div>

<div class="tier-app">
<strong>Application Tier (Business Logic Layer):</strong> Runs on Oracle WebLogic Application Server. It has two logical components â€” the <strong>UI Component</strong>, which is a servlet container that renders dynamic HTML pages back to the user, and the <strong>Business Component</strong>, which contains all OTM business logic including the Bulk Plan algorithm, OTM Agents (workflows), rating, tender processing, and invoice handling. The tiers communicate using JNDI and RMI calls internally, and JDBC to connect to the database.
</div>

<div class="tier-db">
<strong>Database Tier (Data Layer):</strong> Oracle Database stores all OTM data and is accessed from the Application Tier via JDBC. It has two primary schemas â€” <strong>GLOGOWNER</strong>, which is the main OTM schema containing orders, shipments, and configuration data, and <strong>REPORTOWNER</strong>, which holds reporting and reference data such as rates, locations, and carriers.
</div>

**OTM Product Architecture â€” Three-Tier Overview:**

![OTM Product Architecture Diagram](/images/otm-product-architecture.svg)

**How Data Flows:**

When a user opens OTM in a browser, they are connecting to the **Web Tier**. Every action the user takes â€” such as searching for a shipment or running Bulk Plan â€” sends a request from the browser to the Web Tier. If the request is for static content (like a help page), the Web Tier (OHS) responds directly. If the request requires business processing, OHS proxies it to the **Application Tier** via the mod_wl_ohs connector. The UI Component receives the request and passes it to the Business Component for processing. The Business Component executes the required logic (sometimes reading or writing to the Database Tier via JDBC) and returns the result back through the UI Component and Web Tier to the user's browser.

**Server Setup:**

Each of the three tiers can be deployed on separate servers or combined on a single server, depending on the environment:

<div class="tier-env">
<strong>Production environments</strong> typically use separate servers for each tier to ensure performance, scalability, and reliability.
</div>

<div class="tier-env">
<strong>Lower environments</strong> (Development, Test, UAT) often run all three tiers on a single server to reduce infrastructure costs.
</div>

<div class="tier-env">
<strong>SaaS deployments</strong> â€” Oracle manages all server infrastructure. You access OTM through a URL provided by Oracle and do not need to manage or install any tiers.
</div>

**External Systems:**

The Application Tier can be configured to communicate with external systems that extend OTM's capabilities:

- **Mileage Engines** (e.g. PC\*MILER, MileMaker) â€” for calculating distances between locations
- **LTL Rate Engines** (e.g. SMCÂ³ RateWare XL) â€” for dynamically fetching carrier rates
- **ERP Systems** (e.g. Oracle E-Business Suite, SAP) â€” for exchanging orders and cost data
- **Middleware / Integration Platforms** (e.g. MuleSoft, Oracle BPEL) â€” for translating OTM XML to carrier EDI formats and vice versa
- **SMTP Mail Server** â€” for sending email notifications from OTM Agents

<div class="note-box">
<strong>Note:</strong> For on-premise deployments, the specific software versions for the database, application server, and web server depend on the OTM version being installed. Always refer to the Oracle certification matrix for your OTM version to confirm compatible software versions.
</div>

**What's Next:**

Before diving into OTM configuration topics, it helps to be familiar with common logistics terms you will encounter throughout the product â€” such as Bill of Lading, LTL, TL, 3PL, Incoterms, and more. These terms are used throughout OTM screens, documentation, and day-to-day consulting work.

Next Topic: [Basic Logistics Terminology](/posts/basic-logistics-terminology/)
