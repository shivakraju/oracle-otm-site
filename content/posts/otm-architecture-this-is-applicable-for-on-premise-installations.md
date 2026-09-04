---
title: "OTM Product Architecture"
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
description: "An overview of Oracle OTM's three-tier product architecture — covering the Web Tier (Oracle HTTP Server), Application Tier (Oracle WebLogic with UI and Business components), and Database Tier (Oracle Database with GLOGOWNER and REPORTOWNER schemas)."
---

OTM follows a standard **three-tier architecture** — a widely used design in enterprise software where the application is split into three distinct layers: Web Tier, Application Tier, and Database Tier. Each tier has a specific responsibility, and together they allow OTM to scale, be maintained, and support many users simultaneously.

Depending on the deployment model — on-premise or SaaS — the underlying infrastructure differs, but the three-tier concept remains the same. In on-premise deployments, your organization manages each tier on its own servers. In SaaS (cloud) deployments, Oracle manages the infrastructure and these tiers are hosted and maintained by Oracle.

**The Three Tiers:**

> **Web Tier (Presentation Layer):** Runs on Oracle HTTP Server (OHS). It receives browser requests from end users. Static content such as OTM help pages, labels, and JavaScript files are served directly from this tier. Dynamic requests (such as running Bulk Plan or searching for shipments) are forwarded to the Application Tier via the **mod_wl_ohs** connector.
>
> **Application Tier (Business Logic Layer):** Runs on Oracle WebLogic Application Server. It has two logical components — the **UI Component**, which is a servlet container that renders dynamic HTML pages back to the user, and the **Business Component**, which contains all OTM business logic including the Bulk Plan algorithm, OTM Agents (workflows), rating, tender processing, and invoice handling. The tiers communicate using JNDI and RMI calls internally, and JDBC to connect to the database.
>
> **Database Tier (Data Layer):** Oracle Database stores all OTM data and is accessed from the Application Tier via JDBC. It has two primary schemas — **GLOGOWNER**, which is the main OTM schema containing orders, shipments, and configuration data, and **REPORTOWNER**, which holds reporting and reference data such as rates, locations, and carriers.

**OTM Product Architecture — Three-Tier Overview:**

> ![OTM Product Architecture Diagram](/images/otm-product-architecture.svg)

**How Data Flows:**

When a user opens OTM in a browser, they are connecting to the **Web Tier**. Every action the user takes — such as searching for a shipment or running Bulk Plan — sends a request from the browser to the Web Tier. If the request is for static content (like a help page), the Web Tier (OHS) responds directly. If the request requires business processing, OHS proxies it to the **Application Tier** via the mod_wl_ohs connector. The UI Component receives the request and passes it to the Business Component for processing. The Business Component executes the required logic (sometimes reading or writing to the Database Tier via JDBC) and returns the result back through the UI Component and Web Tier to the user's browser.

**Server Setup:**

Each of the three tiers can be deployed on separate servers or combined on a single server, depending on the environment:

> **Production environments** typically use separate servers for each tier to ensure performance, scalability, and reliability.
>
> **Lower environments** (Development, Test, UAT) often run all three tiers on a single server to reduce infrastructure costs.
>
> **SaaS deployments** — Oracle manages all server infrastructure. You access OTM through a URL provided by Oracle and do not need to manage or install any tiers.

**External Systems:**

The Application Tier can be configured to communicate with external systems that extend OTM's capabilities:

- **Mileage Engines** (e.g. PC\*MILER, MileMaker) — for calculating distances between locations
- **LTL Rate Engines** (e.g. SMC³ RateWare XL) — for dynamically fetching carrier rates
- **ERP Systems** (e.g. Oracle E-Business Suite, SAP) — for exchanging orders and cost data
- **Middleware / Integration Platforms** (e.g. MuleSoft, Oracle BPEL) — for translating OTM XML to carrier EDI formats and vice versa
- **SMTP Mail Server** — for sending email notifications from OTM Agents

**Note:** For on-premise deployments, the specific software versions for the database, application server, and web server depend on the OTM version being installed. Always refer to the Oracle certification matrix for your OTM version to confirm compatible software versions.
