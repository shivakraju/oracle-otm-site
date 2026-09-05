---
title: "Domains, Standard Schema and Data Dictionary"
date: 2016-05-02T16:34:00+00:00
draft: false
weight: 75
tags:
  - "DATA_DICT"
  - "XID"
  - "GID"
  - "domain"
  - "Schema"
  - "OTM"
  - "REPORTOWNER"
  - "GLOGOWNER"
aliases:
  - "/2016/05/otm-data-structure.html"
keywords:
  - "Oracle OTM domain structure explained"
  - "OTM GLOGOWNER schema tables"
  - "Oracle OTM GID XID columns"
  - "OTM REPORTOWNER schema"
  - "Oracle OTM data dictionary"
  - "OTM domain hierarchy parent child"
  - "Oracle OTM database schema overview"
  - "OTM domain name column tables"
  - "Oracle Transportation Management data structure"
  - "OTM ORDER_BASE_GID explained"
  - "Oracle OTM standard schema GLOGOWNER REPORTOWNER"
description: "Explains Oracle OTM's domain-based data organisation, the GLOGOWNER and REPORTOWNER schemas, and how GID/XID columns uniquely identify business objects like purchase orders and shipments across domains."
---

OTM organises all of its data using a **domain** model. Understanding domains, the database schema, and how business objects are identified is foundational for anyone working with OTM data — whether you are building integrations, writing reports, or troubleshooting transactions.

**Domains:**

<div class="field-box"><strong>What is a domain?</strong> A domain is a logical grouping of OTM data for a business unit. A corporation with multiple shipping divisions — say, Merchandise and Food & Beverage — would typically have one domain per division. Users and roles are tied to a domain, so a user in one domain cannot see or modify data in another.</div>

<div class="field-box"><strong>Domain hierarchy:</strong> Domains can be nested — a parent domain at the corporate level with child domains under each business unit. Configuration defined at the parent level (e.g. Item Numbers, Agents, Rate Offerings) is shared across all child domains, while each child domain can also maintain its own configuration.</div>

<div class="field-box"><strong>DOMAIN_NAME column:</strong> Every table in OTM includes a <code>DOMAIN_NAME</code> column that ties each row to its domain. This is how OTM isolates data between business units within a single database instance.</div>

**GID and XID — How OTM Identifies Business Objects:**

Every OTM business object has two identifier columns:

<div class="field-box"><strong>GID (Global ID):</strong> The system-level unique identifier, formatted as <code>DOMAIN_NAME.XID</code>. For example, a purchase order in domain <code>ABC</code> with PO number <code>12345</code> has <code>ORDER_BASE_GID = ABC.12345</code>. GID is the primary key used in foreign key relationships across tables.</div>

<div class="field-box"><strong>XID (External ID):</strong> The business-facing identifier — just the <code>12345</code> part, without the domain prefix. This is what business users recognise. In most implementations, the XID matches the source system's reference number.</div>

**Standard OTM Database Schemas:**

<div class="field-box"><strong>GLOGOWNER:</strong> The main transactional schema. All OTM business data lives here — Purchase Orders (<code>ORDER_BASE</code>), Order Releases (<code>ORDER_RELEASE</code>), Shipments (<code>SHIPMENT</code>), Locations (<code>LOCATION</code>), Rates, Invoices, and more.</div>

<div class="field-box"><strong>REPORTOWNER:</strong> Stores report definitions, BI Publisher query templates, and Oracle stored procedures used for reporting. Objects created in this schema need a public synonym so the OTM application can access them.</div>

**OTM Data Dictionary:**

The Data Dictionary is built into OTM and documents every table and column in the GLOGOWNER schema — including primary keys, foreign keys, and field descriptions. To access it, add `html/data_dict` to your OTM URL after `GC3`:

`https://<your-otm-host>/GC3/html/data_dict/`

![OTM Data Dictionary showing SHIP_UNIT_LINE table with primary key and foreign key annotations](/images/otm-domains-standard-schema-an-img1-16093e055e.png)

<div class="note-box"><strong>Note:</strong> Columns marked with <code>*</code> are part of the primary key. The value in brackets next to a column shows the foreign key reference — for example, <code>SHIP_UNIT_LINE.SHIP_UNIT_GID</code> references <code>SHIP_UNIT.SHIP_UNIT_GID</code>.</div>

**What's Next:**

The next topic covers Basic OTM Configurations — the foundational setup steps every OTM implementation requires, starting with Domain Items, Locations, and Equipment Groups.

Next Topic: [Basic OTM Configurations — Domain Items, Locations and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)