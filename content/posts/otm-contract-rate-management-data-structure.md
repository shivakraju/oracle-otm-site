---
title: "Contract & Rate Management Data Structure"
date: 2016-05-06T17:29:00+00:00
draft: false
weight: 130
tags:
  - "RATE_OFFERING"
  - "Rate Record"
  - "Rate Service"
  - "Service Provider"
  - "RATE_SERVICE"
  - "RATE_GEO"
  - "Rate Distance"
  - "Rate Offering"
aliases:
  - "/2016/05/otm-contract-rate-management-data.html"
keywords:
  - "Oracle OTM rate management data structure"
  - "OTM RATE_OFFERING table"
  - "Oracle OTM rate service rate record setup"
  - "OTM SERVPROV table structure"
  - "Oracle OTM carrier contract rate setup"
  - "OTM RATE_GEO lane configuration"
  - "Oracle OTM service provider SCAC code"
  - "OTM rate distance table"
  - "Oracle Transportation Management carrier rate tables"
  - "OTM contract rate offering configuration"
  - "Oracle OTM LTL TL parcel rate setup"
description: "Covers the Oracle OTM contract and rate management data model, including the SERVPROV, RATE_OFFERING, RATE_SERVICE, RATE_GEO, and Rate Record tables used to store carrier contracts and freight rates."
---

OTM models carrier contracting across five layers: **Service Provider** (who moves the freight), **Rate Service** (transit time commitments), **Rate Distance** (how mileage is calculated), **Rate Offering** (the contract), and **Rate Records** (the actual cost lanes). Understanding this structure is essential for rate setup, planning troubleshooting, and freight cost analysis.

**Service Provider:**

A Service Provider (carrier) is the party that physically moves freight. They own or manage trucks, containers, trailers, and drivers. They receive tender requests from OTM specifying origin, destination, weight, volume, and shipment dates — and issue invoices once delivery is complete.

When contracting with a carrier, you typically negotiate:

<div class="field-box"><strong>Transport Mode:</strong> How the freight moves — TL (truckload), LTL (less-than-truckload), PARCEL, VESSEL, RAIL, etc.</div>

<div class="field-box"><strong>Rate Service:</strong> The service level — 2-day, 3-day, standard ground, express, etc.</div>

<div class="field-box"><strong>Lanes:</strong> The origin/destination region combinations the carrier will serve.</div>

<div class="field-box"><strong>Rates and discounts:</strong> Cost per unit of weight, volume, or container, with any volume-based discounts.</div>

**Service Provider tables:**

<div class="field-box"><strong>SCAC</strong> — Standard Carrier Alpha Code. Every Service Provider in OTM must be associated with a SCAC — a standard four-letter industry code that uniquely identifies the carrier.</div>

<div class="field-box"><strong>SERVPROV</strong> — Service Provider record. Stores the carrier name, SCAC code, supported transport modes, cost allocation rules, and invoice approval rules. A LOCATION record is automatically created for every SERVPROV.</div>

**Rate Service:**

Rate Service defines the transit time commitment from origin to destination. The configuration approach varies by transport mode:

<div class="field-box"><strong>TL / LTL:</strong> Rate Service type is typically set to SIMULATION — OTM estimates transit time based on an assumed average truck speed (e.g. 50 mph).</div>

<div class="field-box"><strong>PARCEL:</strong> Rate Service type is set to DAYDURATION — transit days are specified explicitly per lane. For example, FedEx 1-Day, FedEx 2-Day, UPS Ground 5-Day.</div>

**Rate Service tables:**

<div class="field-box"><strong>RATE_SERVICE_TYPE</strong> — Lookup table for service type classifications.</div>

<div class="field-box"><strong>RATE_SERVICE_PROFILE</strong> — Profile grouping rate services for assignment to rate offerings.</div>

<div class="field-box"><strong>RATE_SERVICE</strong> — Rate Service header record with service name and type.</div>

<div class="field-box"><strong>RATE_SERVICE_SPEED</strong> — Speed and transit time parameters for SIMULATION-type services.</div>

<div class="field-box"><strong>SERVICE_TIME</strong> — Service times associated with a specific Rate Service ID — useful for verifying how transit days are being calculated.</div>

**Rate Distance:**

Rate Distance controls how OTM calculates mileage between origin and destination locations. This feeds into distance-based rate calculations and transit time estimates.

<div class="field-box"><strong>RATE_DISTANCE</strong> — Rate Distance configuration record. Can be set to LOOKUP (use pre-loaded distance table), ESTIMATE (calculated from lat/long), or EXTERNAL (call a third-party engine).</div>

<div class="field-box"><strong>DISTANCE_EXTERNAL_ENGINE</strong> — Configuration for an external distance engine such as PC*MILER or MileMaker.</div>

<div class="field-box"><strong>DISTANCE_EXTERNAL_ENGINE_PARMS</strong> — Connection parameters for the external distance engine.</div>

**Rate Offering:**

A Rate Offering is the carrier contract in OTM. It ties together the carrier, the transport mode, the service levels, and the applicable cost structure. Key attributes on a Rate Offering include:

<div class="field-box"><strong>Service Provider:</strong> The carrier this contract applies to.</div>

<div class="field-box"><strong>Rate Service:</strong> Transit time service levels covered by this contract.</div>

<div class="field-box"><strong>Transport Mode:</strong> TL, LTL, VESSEL, PARCEL, etc.</div>

<div class="field-box"><strong>Base Rate and Distance engines:</strong> Used for LTL rating to determine base cost and mileage.</div>

<div class="field-box"><strong>Stop-off charges and accessorials:</strong> Additional charges such as fuel surcharge, liftgate, residential delivery, etc.</div>

<div class="field-box"><strong>Currency and contract expiration date.</strong></div>

**Rate Offering tables:**

<div class="field-box"><strong>RATE_OFFERING_TYPE</strong> — Lookup table for offering type classifications.</div>

<div class="field-box"><strong>RATE_OFFERING</strong> — Rate Offering header record.</div>

<div class="field-box"><strong>RATE_OFFERING_STOPS</strong> — Stop-off charge configuration within the offering.</div>

<div class="field-box"><strong>RATE_OFFERING_REMARK</strong> — Remarks on the Rate Offering.</div>

<div class="field-box"><strong>RATE_OFFERING_ACCESSORIAL</strong> — Accessorial charges (fuel surcharge, liftgate, etc.) linked to the offering.</div>

<div class="field-box"><strong>RATE_OFFERING_INV_PARTY</strong> — Involved parties on the Rate Offering (e.g. shipper, carrier).</div>

**Rate Record:**

Rate Records hold the actual freight cost details within a Rate Offering. Costs can be structured in many ways depending on the business — flat per container, lane-based, weight breaks, volume breaks, or a combination.

**Rate Record tables:**

<div class="field-box"><strong>RATE_GEO</strong> — Rate Record header. Defines the lane (origin/destination regions) and the rate structure type.</div>

<div class="field-box"><strong>RATE_GEO_COST</strong> — Cost line within the Rate Record — the actual rate amount and unit (per mile, per cwt, per container, etc.).</div>

<div class="field-box"><strong>RATE_GEO_COST_UNIT_BREAK</strong> — Unit-based cost breaks (e.g. different rates above/below a quantity threshold).</div>

<div class="field-box"><strong>RATE_GEO_COST_WEIGHT_BREAK</strong> — Weight-based cost breaks — rates that change at defined weight thresholds.</div>

<div class="field-box"><strong>RATE_GEO_COST_GROUP</strong> — Groups related cost lines within a Rate Record.</div>

<div class="field-box"><strong>RATE_GEO_ACCESSORIAL</strong> — Accessorial charges applied at the Rate Record (lane) level.</div>

<div class="field-box"><strong>RATE_GEO_REFNUM</strong> — Reference numbers on the Rate Record.</div>

<div class="field-box"><strong>RATE_GEO_REMARK</strong> — Remarks on the Rate Record.</div>

**What's Next:**

The next topic covers the Business Process Automation Data Structure — the tables behind OTM Agents, workflow events, and automation configurations.

Next Topic: [Business Process Automation Data Structure](/posts/business-process-automation-data-structure/)
