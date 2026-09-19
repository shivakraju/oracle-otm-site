---
title: "LTL Rates — CSV Upload"
date: 2026-09-19T00:00:00+00:00
draft: false
weight: 61
url: "/posts/ltl-rates-csv-upload/"
tags:
  - "OTM"
  - "LTL Rates"
  - "CSV Upload"
  - "Rate Offering"
keywords:
  - "Oracle OTM LTL rate CSV upload"
  - "OTM less than truckload rate upload CSV"
  - "Oracle OTM LTL rate offering CSV"
  - "OTM RATE_BASE_DEF CSV upload"
  - "OTM LTL base tariff rate offering"
  - "Oracle OTM LTL discount rate CSV"
  - "OTM RATE_GEO minimum cost LTL"
  - "Oracle Transportation Management LTL rate upload"
  - "OTM LTL class based rate CSV"
  - "Oracle OTM NMFC LTL rate configuration"
description: "Step-by-step guide to uploading Less-than-Truckload (LTL) rates in Oracle OTM using six CSV files — including the LTL-specific RATE_BASE_DEF file that links a carrier's rate offering to a base tariff for class-based discount pricing."
---

LTL (Less-than-Truckload) rate pricing works differently from TL. Rather than a flat per-mile charge, LTL rates are **class-based** — the freight cost depends on the shipment's weight, the distance, and the NMFC freight class of the goods being shipped. Heavier, denser freight falls into lower classes and attracts lower rates; lighter, bulkier freight is assigned higher classes.

In OTM, LTL pricing uses two layers:

- **Base Tariff** — a rate offering already loaded in OTM that contains the published class-based rate table (rate per hundredweight by freight class and distance). This tariff is typically loaded once and shared across all carriers that use the same tariff basis.
- **Carrier Rate Offering** — the actual contract with a specific carrier, which defines a **discount percentage** off the base tariff. OTM looks up the class rate from the base tariff, then applies the discount to calculate the final cost.

LTL lanes are also typically defined at a broader geography than TL. Where TL uses city-to-city lanes, LTL carriers often publish rates by **origin city to destination state** — reflecting how their regional networks are structured.

Six CSV files must be uploaded in the order listed below:

- **File 1 — RATE_OFFERING:** Define the rate offering header (carrier, mode, weight range)
- **File 2 — RATE_BASE_DEF:** Link the rate offering to a base tariff *(LTL only — not used in TL)*
- **File 3 — X_LANE:** Define the lane (origin city → destination state)
- **File 4 — RATE_GEO:** Link the rate offering to the lane and set the minimum charge
- **File 5 — RATE_GEO_COST_GROUP:** Create a cost group container
- **File 6 — RATE_GEO_COST:** Define the discount percentage off the base tariff

**How to upload:**

<div class="step-box">Business Process Automation > Integration > Integration Manager > Upload an XML/CSV Transmission</div>

Select the file type from the dropdown, choose your CSV file, and click Upload. Repeat for each file in the order listed above.

<div class="note-box"><strong>Note:</strong> Every CSV file must have the object name as the first row, column headers as the second row, and data starting from the third row. OTM will reject files that do not follow this structure.</div>

---

**File 1 — RATE_OFFERING**

Same structure as a TL rate offering but with LTL-specific values. The weight range reflects the typical LTL shipment band — below the minimum is parcel, above the maximum is TL.

<div class="field-box"><strong>RATE_OFFERING_GID / RATE_OFFERING_XID:</strong> GID and unique ID for this offering</div>

<div class="field-box"><strong>RATE_OFFERING_TYPE_GID:</strong> Use <code>LTL - MASTER</code> (not <code>TL</code>). The "MASTER" indicates this offering will reference a base tariff via RATE_BASE_DEF.</div>

<div class="field-box"><strong>SERVPROV_GID:</strong> GID of the carrier (Service Provider) in OTM — must already exist in your domain</div>

<div class="field-box"><strong>CURRENCY_GID:</strong> Currency for the rate, e.g. <code>USD</code></div>

<div class="field-box"><strong>TRANSPORT_MODE_GID:</strong> Use <code>LTL</code> — this is a system-level value in OTM and is not prefixed with the domain name</div>

<div class="field-box"><strong>RATE_SERVICE_GID:</strong> Rate service GID defined in OTM for this carrier contract — must exist in your domain. Rate Service configuration will be covered in a separate topic.</div>

<div class="field-box"><strong>RATE_VERSION_GID:</strong> Rate version — use <code>YOUR_DOMAIN.DEFAULT</code> if no custom version has been created</div>

<div class="field-box"><strong>MIN_WEIGHT_CONSTRAINT / MAX_WEIGHT_CONSTRAINT:</strong> Typical LTL range is 151 LB minimum (below this is parcel) up to 19,999 LB maximum (above this is TL). Each requires a <code>_UOM_CODE</code> column (e.g. <code>LB</code>) and a <code>_BASE</code> column (same numeric value).</div>

<div class="field-box"><strong>RATE_DISTANCE_GID:</strong> Distance provider GID — e.g. <code>YOUR_DOMAIN.MILEMAKER</code> or <code>YOUR_DOMAIN.PC_MILER</code></div>

<div class="field-box"><strong>IS_ACTIVE:</strong> <code>Y</code> to activate</div>

<div class="field-box"><strong>TOTAL_STOPS_CONSTRAINT / PICKUP_STOPS_CONSTRAINT / DELIVERY_STOPS_CONSTRAINT:</strong> For a standard LTL shipment: <code>2</code> total, <code>1</code> pickup, <code>1</code> delivery</div>

<div class="field-box"><strong>STOPS_INCLUDED_IN_RATE:</strong> Number of stops included in the base rate</div>

**CSV Template:**

```csv
RATE_OFFERING
RATE_OFFERING_GID,RATE_OFFERING_XID,RATE_OFFERING_TYPE_GID,SERVPROV_GID,CURRENCY_GID,TRANSPORT_MODE_GID,RATE_SERVICE_GID,RATE_VERSION_GID,MIN_WEIGHT_CONSTRAINT,MIN_WEIGHT_CONSTRAINT_UOM_CODE,MIN_WEIGHT_CONSTRAINT_BASE,MAX_WEIGHT_CONSTRAINT,MAX_WEIGHT_CONSTRAINT_UOM_CODE,MAX_WEIGHT_CONSTRAINT_BASE,RATE_DISTANCE_GID,IS_ACTIVE,TOTAL_STOPS_CONSTRAINT,PICKUP_STOPS_CONSTRAINT,DELIVERY_STOPS_CONSTRAINT,STOPS_INCLUDED_IN_RATE,DOMAIN_NAME
YOUR_DOMAIN.LTL_RATE_001,LTL_RATE_001,LTL - MASTER,YOUR_DOMAIN.YOUR_CARRIER,USD,LTL,YOUR_DOMAIN.YOUR_RATE_SERVICE,YOUR_DOMAIN.DEFAULT,151,LB,151,19999,LB,19999,YOUR_DOMAIN.MILEMAKER,Y,2,1,1,2,YOUR_DOMAIN
```

---

**File 2 — RATE_BASE_DEF** *(LTL only)*

Links the carrier's rate offering to a base tariff. This is what makes the offering an `LTL - MASTER` — OTM uses the base tariff's class rate table as the starting point, and then applies the discount defined in RATE_GEO_COST to calculate the actual cost.

<div class="field-box"><strong>RATE_MASTER_RO_GID:</strong> GID of the Rate Offering created in File 1</div>

<div class="field-box"><strong>BASE_TARIFF_RO_GID:</strong> GID of the base tariff rate offering already loaded in OTM — e.g. <code>YOUR_DOMAIN.LTL-BASE-US</code>. This tariff must exist in OTM before uploading this file.</div>

<div class="field-box"><strong>DOMAIN_NAME:</strong> Your OTM domain</div>

**CSV Template:**

```csv
RATE_BASE_DEF
RATE_MASTER_RO_GID,BASE_TARIFF_RO_GID,DOMAIN_NAME
YOUR_DOMAIN.LTL_RATE_001,YOUR_DOMAIN.LTL-BASE-US,YOUR_DOMAIN
```

<div class="note-box"><strong>Note:</strong> The base tariff is typically loaded once per environment and shared across all carriers that use the same tariff basis. If your organisation uses multiple tariff bases (e.g. one for domestic, one for regional carriers), confirm which tariff applies to this carrier before uploading.</div>

---

**File 3 — X_LANE**

Defines the lane. LTL lanes use a **city-level origin** and a **state/province-level destination** — reflecting how LTL carriers structure their regional pricing rather than pricing point-to-point like TL.

<div class="field-box"><strong>X_LANE_GID / X_LANE_XID:</strong> GID and unique ID for the lane. Recommended convention: <code>{ORIGIN_CITY}_{ORIGIN_STATE}-{DEST_STATE}</code>, e.g. <code>DALLAS_TX-GA</code></div>

<div class="field-box"><strong>SOURCE_CITY / SOURCE_PROVINCE_CODE / SOURCE_COUNTRY_CODE3_GID:</strong> Origin city, state, and 3-character country code</div>

<div class="field-box"><strong>SOURCE_GEO_HIERARCHY_GID:</strong> Use <code>CITY</code> for the origin</div>

<div class="field-box"><strong>DEST_PROVINCE_CODE:</strong> Destination state or province code (e.g. <code>GA</code> for Georgia). No destination city is required for state-level lanes.</div>

<div class="field-box"><strong>DEST_GEO_HIERARCHY_GID:</strong> Use <code>STATE/PROVINCE</code> — this means the rate applies to all destinations within that state</div>

**CSV Template:**

```csv
X_LANE
X_LANE_GID,X_LANE_XID,SOURCE_CITY,SOURCE_PROVINCE_CODE,SOURCE_COUNTRY_CODE3_GID,SOURCE_GEO_HIERARCHY_GID,DEST_PROVINCE_CODE,DEST_GEO_HIERARCHY_GID,DOMAIN_NAME
YOUR_DOMAIN.DALLAS_TX-GA,DALLAS_TX-GA,DALLAS,TX,USA,CITY,GA,STATE/PROVINCE,YOUR_DOMAIN
```

---

**File 4 — RATE_GEO**

Links the Rate Offering to the Lane and sets the **minimum charge** for this lane. The minimum charge is the floor cost OTM applies if the calculated freight cost (base tariff rate × discount) falls below this amount — a standard feature of LTL contracts.

<div class="field-box"><strong>RATE_GEO_GID / RATE_GEO_XID:</strong> GID and unique ID. Recommended convention: <code>{RATE_OFFERING_XID}_{X_LANE_XID}</code></div>

<div class="field-box"><strong>RATE_OFFERING_GID:</strong> GID of the Rate Offering created in File 1</div>

<div class="field-box"><strong>X_LANE_GID:</strong> GID of the Lane created in File 3</div>

<div class="field-box"><strong>MIN_COST:</strong> Minimum charge for any shipment on this lane, e.g. <code>178</code></div>

<div class="field-box"><strong>MIN_COST_GID:</strong> Currency for the minimum cost, e.g. <code>USD</code></div>

<div class="field-box"><strong>MIN_COST_BASE:</strong> Same numeric value as MIN_COST</div>

<div class="field-box"><strong>IS_ACTIVE:</strong> <code>Y</code> to activate this lane within the rate offering</div>

**CSV Template:**

```csv
RATE_GEO
RATE_GEO_GID,RATE_GEO_XID,RATE_OFFERING_GID,X_LANE_GID,MIN_COST,MIN_COST_GID,MIN_COST_BASE,IS_ACTIVE,DOMAIN_NAME
YOUR_DOMAIN.LTL_RATE_001_DALLAS_TX-GA,LTL_RATE_001_DALLAS_TX-GA,YOUR_DOMAIN.LTL_RATE_001,YOUR_DOMAIN.DALLAS_TX-GA,178,USD,178,Y,YOUR_DOMAIN
```

---

**File 5 — RATE_GEO_COST_GROUP**

Creates a cost group under the Rate Geo — same purpose as in TL. Acts as a container for the discount cost line.

**CSV Template:**

```csv
RATE_GEO_COST_GROUP
RATE_GEO_COST_GROUP_GID,RATE_GEO_COST_GROUP_XID,RATE_GEO_GID,RATE_GEO_COST_GROUP_SEQ,DOMAIN_NAME
YOUR_DOMAIN.LTL_RATE_001_DALLAS_TX-GA,LTL_RATE_001_DALLAS_TX-GA,YOUR_DOMAIN.LTL_RATE_001_DALLAS_TX-GA,1,YOUR_DOMAIN
```

---

**File 6 — RATE_GEO_COST**

Defines the **discount percentage** off the base tariff for this lane. Unlike TL (which stores a rate per mile), LTL stores a discount factor — OTM looks up the applicable class rate from the base tariff, then applies this discount to arrive at the final freight cost.

<div class="note-box"><strong>Important:</strong> Row 3 of this file must contain the date format declaration exactly as shown. Do not remove or modify this line.</div>

<div class="field-box"><strong>RATE_GEO_COST_GROUP_GID:</strong> GID of the Cost Group created in File 5</div>

<div class="field-box"><strong>RATE_GEO_COST_SEQ:</strong> Sequence number — use <code>1</code> for a single discount line</div>

<div class="field-box"><strong>CHARGE_MULTIPLIER_SCALAR:</strong> The discount percentage — e.g. <code>17.2</code> means a 17.2% discount off the base tariff rate</div>

<div class="field-box"><strong>CHARGE_ACTION:</strong> Use <code>D</code> for Discount</div>

<div class="field-box"><strong>COST_TYPE:</strong> Use <code>D</code> for Discount type</div>

<div class="field-box"><strong>EFFECTIVE_DATE:</strong> Date this rate becomes active — format <code>YYYYMMDDHH24MISS</code>, e.g. <code>20260101000000</code> for 1 Jan 2026</div>

<div class="field-box"><strong>EXPIRATION_DATE:</strong> Date this rate expires — leave blank for no expiry</div>

**CSV Template:**

```csv
RATE_GEO_COST
RATE_GEO_COST_GROUP_GID,RATE_GEO_COST_SEQ,CHARGE_MULTIPLIER_SCALAR,CHARGE_ACTION,COST_TYPE,EFFECTIVE_DATE,EXPIRATION_DATE,DOMAIN_NAME
EXEC SQL ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDDHH24MISS'
YOUR_DOMAIN.LTL_RATE_001_DALLAS_TX-GA,1,17.2,D,D,20260101000000,,YOUR_DOMAIN
```
