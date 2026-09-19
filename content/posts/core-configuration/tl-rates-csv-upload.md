---
title: "TL Rates — CSV Upload"
date: 2026-09-19T00:00:00+00:00
draft: false
weight: 60
url: "/posts/tl-rates-csv-upload/"
tags:
  - "OTM"
  - "TL Rates"
  - "CSV Upload"
  - "Rate Offering"
keywords:
  - "Oracle OTM TL rate CSV upload"
  - "OTM truckload rate upload CSV"
  - "Oracle OTM rate offering CSV"
  - "OTM X_LANE CSV upload"
  - "OTM RATE_GEO CSV upload"
  - "Oracle OTM RATE_GEO_COST CSV"
  - "OTM TL rate configuration CSV"
  - "Oracle Transportation Management rate upload"
  - "OTM distance lookup CSV"
  - "OTM rate geo cost group CSV"
description: "Step-by-step guide to uploading Truckload rates in Oracle OTM using six CSV files — X_LANE, RATE_OFFERING, DISTANCE_LOOKUP, RATE_GEO, RATE_GEO_COST_GROUP, and RATE_GEO_COST — with copy-paste templates for each file."
---

OTM allows Truckload (TL) rate contracts to be loaded using CSV files instead of manual UI entry. This is the most efficient approach when setting up rates for multiple lanes or carriers.

Six CSV files must be uploaded in a specific order — each file builds on data created by the previous one:

- **File 1 — X_LANE:** Define the lane (origin and destination geography)
- **File 2 — RATE_OFFERING:** Define the rate offering header (carrier, mode, weight limits)
- **File 3 — DISTANCE_LOOKUP:** Assign a distance to the lane
- **File 4 — RATE_GEO:** Link the rate offering to the lane
- **File 5 — RATE_GEO_COST_GROUP:** Create a cost group container
- **File 6 — RATE_GEO_COST:** Define the actual rate amount

**How to upload:**

<div class="step-box">Business Process Automation > Integration > Integration Manager > Upload an XML/CSV Transmission</div>

Select the file type from the dropdown, choose your CSV file, and click Upload. Repeat for each file in the order listed above.

<div class="note-box"><strong>Note:</strong> Every CSV file must follow this structure: the first row is the object name, the second row is the column header, and data starts from the third row. OTM will reject files that do not follow this format.</div>

---

**File 1 — X_LANE**

Defines the lane — the origin and destination geography. OTM matches Order Releases to lanes by comparing their source and destination against these city, state, and country values.

**Key fields:**

<div class="field-box"><strong>X_LANE_GID:</strong> Full GID of the lane — format: <code>YOUR_DOMAIN.YOUR_LANE_XID</code></div>

<div class="field-box"><strong>X_LANE_XID:</strong> Unique ID for this lane within the domain. Use a naming convention that clearly identifies the lane, e.g. <code>CHICAGO_IL-DALLAS_TX</code></div>

<div class="field-box"><strong>SOURCE_CITY / SOURCE_PROVINCE_CODE / SOURCE_COUNTRY_CODE3_GID:</strong> Origin city, state or province code, and 3-character country code</div>

<div class="field-box"><strong>SOURCE_GEO_HIERARCHY_GID:</strong> Granularity of the origin geography — use <code>CITY</code> for point-to-point TL rates</div>

<div class="field-box"><strong>DEST_CITY / DEST_PROVINCE_CODE / DEST_COUNTRY_CODE3_GID:</strong> Destination city, state or province, and country code</div>

<div class="field-box"><strong>DEST_GEO_HIERARCHY_GID:</strong> Granularity of the destination geography — use <code>CITY</code> for point-to-point TL rates</div>

<div class="field-box"><strong>DOMAIN_NAME:</strong> Your OTM domain</div>

**CSV Template — copy, save as `.csv`, and replace values for your lane:**

```csv
X_LANE
X_LANE_GID,X_LANE_XID,SOURCE_CITY,SOURCE_PROVINCE_CODE,SOURCE_COUNTRY_CODE3_GID,SOURCE_GEO_HIERARCHY_GID,DEST_CITY,DEST_PROVINCE_CODE,DEST_COUNTRY_CODE3_GID,DEST_GEO_HIERARCHY_GID,DOMAIN_NAME
YOUR_DOMAIN.CHICAGO_IL-DALLAS_TX,CHICAGO_IL-DALLAS_TX,CHICAGO,IL,USA,CITY,DALLAS,TX,USA,CITY,YOUR_DOMAIN
```

---

**File 2 — RATE_OFFERING**

Defines the rate offering header — the carrier, transport mode, rate service, and shipment weight constraints. This is the top-level container for the rate.

**Key fields:**

<div class="field-box"><strong>RATE_OFFERING_GID / RATE_OFFERING_XID:</strong> GID and unique ID for this offering. The XID becomes the name visible in OTM.</div>

<div class="field-box"><strong>RATE_OFFERING_TYPE_GID:</strong> Use <code>TL</code> for Truckload</div>

<div class="field-box"><strong>SERVPROV_GID:</strong> GID of the carrier (Service Provider) in OTM — must already exist in your domain</div>

<div class="field-box"><strong>CURRENCY_GID:</strong> Currency for the rate, e.g. <code>USD</code></div>

<div class="field-box"><strong>TRANSPORT_MODE_GID:</strong> Transport mode GID defined in OTM, e.g. <code>YOUR_DOMAIN.TL</code></div>

<div class="field-box"><strong>RATE_SERVICE_GID:</strong> Rate service GID defined in OTM, e.g. <code>YOUR_DOMAIN.SOLO</code> for solo driver or <code>YOUR_DOMAIN.TEAM</code> for team driver — must exist in your domain</div>

<div class="field-box"><strong>RATE_VERSION_GID:</strong> Rate version — use <code>YOUR_DOMAIN.DEFAULT</code> if no custom version has been created</div>

<div class="field-box"><strong>MIN_WEIGHT_CONSTRAINT / MAX_WEIGHT_CONSTRAINT:</strong> Minimum and maximum shipment weight this rate applies to. Each requires a <code>_UOM_CODE</code> column (e.g. <code>LB</code>) and a <code>_BASE</code> column (same numeric value, used internally by OTM for unit conversion).</div>

<div class="field-box"><strong>RATE_DISTANCE_GID:</strong> Distance provider GID used to calculate mileage — e.g. <code>YOUR_DOMAIN.MILEMAKER</code> or <code>YOUR_DOMAIN.PC_MILER</code>. Must match what you use in DISTANCE_LOOKUP.</div>

<div class="field-box"><strong>IS_ACTIVE:</strong> <code>Y</code> to activate the rate offering</div>

<div class="field-box"><strong>TOTAL_STOPS_CONSTRAINT / PICKUP_STOPS_CONSTRAINT / DELIVERY_STOPS_CONSTRAINT:</strong> Maximum stops allowed on a shipment. For a simple point-to-point TL rate: <code>2</code> total, <code>1</code> pickup, <code>1</code> delivery.</div>

<div class="field-box"><strong>STOPS_INCLUDED_IN_RATE:</strong> Number of stops included in the base rate before extra-stop charges apply</div>

**CSV Template:**

```csv
RATE_OFFERING
RATE_OFFERING_GID,RATE_OFFERING_XID,RATE_OFFERING_TYPE_GID,SERVPROV_GID,CURRENCY_GID,TRANSPORT_MODE_GID,RATE_SERVICE_GID,RATE_VERSION_GID,MIN_WEIGHT_CONSTRAINT,MIN_WEIGHT_CONSTRAINT_UOM_CODE,MIN_WEIGHT_CONSTRAINT_BASE,MAX_WEIGHT_CONSTRAINT,MAX_WEIGHT_CONSTRAINT_UOM_CODE,MAX_WEIGHT_CONSTRAINT_BASE,RATE_DISTANCE_GID,IS_ACTIVE,TOTAL_STOPS_CONSTRAINT,PICKUP_STOPS_CONSTRAINT,DELIVERY_STOPS_CONSTRAINT,STOPS_INCLUDED_IN_RATE,DOMAIN_NAME
YOUR_DOMAIN.TL_RATE_001,TL_RATE_001,TL,YOUR_DOMAIN.YOUR_CARRIER,USD,YOUR_DOMAIN.TL,YOUR_DOMAIN.SOLO,YOUR_DOMAIN.DEFAULT,20000,LB,20000,40000,LB,40000,YOUR_DOMAIN.MILEMAKER,Y,2,1,1,2,YOUR_DOMAIN
```

---

**File 3 — DISTANCE_LOOKUP**

Assigns a pre-defined distance to the lane. OTM uses this stored value when calculating freight cost rather than computing distance dynamically at runtime.

**Key fields:**

<div class="field-box"><strong>X_LANE_GID:</strong> GID of the lane created in File 1</div>

<div class="field-box"><strong>RATE_DISTANCE_GID:</strong> Distance provider GID — must match the value used in RATE_OFFERING</div>

<div class="field-box"><strong>DISTANCE_VALUE:</strong> Distance between origin and destination</div>

<div class="field-box"><strong>DISTANCE_VALUE_UOM_CODE:</strong> Unit of measure — <code>MI</code> for miles, <code>KM</code> for kilometres</div>

<div class="field-box"><strong>DISTANCE_VALUE_BASE:</strong> Same numeric value as DISTANCE_VALUE (used internally by OTM for unit conversion)</div>

**CSV Template:**

```csv
DISTANCE_LOOKUP
X_LANE_GID,RATE_DISTANCE_GID,DISTANCE_VALUE,DISTANCE_VALUE_UOM_CODE,DISTANCE_VALUE_BASE,DOMAIN_NAME
YOUR_DOMAIN.CHICAGO_IL-DALLAS_TX,YOUR_DOMAIN.MILEMAKER,920,MI,920,YOUR_DOMAIN
```

---

**File 4 — RATE_GEO**

Links a Rate Offering to a Lane. One Rate Offering can cover multiple lanes — each lane gets its own RATE_GEO record.

**Key fields:**

<div class="field-box"><strong>RATE_GEO_GID / RATE_GEO_XID:</strong> GID and unique ID for this record. Recommended convention: <code>{RATE_OFFERING_XID}_{X_LANE_XID}</code></div>

<div class="field-box"><strong>RATE_OFFERING_GID:</strong> GID of the Rate Offering created in File 2</div>

<div class="field-box"><strong>X_LANE_GID:</strong> GID of the Lane created in File 1</div>

<div class="field-box"><strong>IS_ACTIVE:</strong> <code>Y</code> to activate this lane within the rate offering</div>

**CSV Template:**

```csv
RATE_GEO
RATE_GEO_GID,RATE_GEO_XID,RATE_OFFERING_GID,X_LANE_GID,IS_ACTIVE,DOMAIN_NAME
YOUR_DOMAIN.TL_RATE_001_CHICAGO_IL-DALLAS_TX,TL_RATE_001_CHICAGO_IL-DALLAS_TX,YOUR_DOMAIN.TL_RATE_001,YOUR_DOMAIN.CHICAGO_IL-DALLAS_TX,Y,YOUR_DOMAIN
```

---

**File 5 — RATE_GEO_COST_GROUP**

Creates a cost group under the Rate Geo. The cost group is a container for one or more rate cost lines — for example, a base line-haul rate and a fuel surcharge would each be a separate sequence under the same cost group.

**Key fields:**

<div class="field-box"><strong>RATE_GEO_COST_GROUP_GID / RATE_GEO_COST_GROUP_XID:</strong> GID and unique ID. Typically the same value as RATE_GEO_GID.</div>

<div class="field-box"><strong>RATE_GEO_GID:</strong> GID of the Rate Geo created in File 4</div>

<div class="field-box"><strong>RATE_GEO_COST_GROUP_SEQ:</strong> Sequence number — use <code>1</code> for a single cost group</div>

**CSV Template:**

```csv
RATE_GEO_COST_GROUP
RATE_GEO_COST_GROUP_GID,RATE_GEO_COST_GROUP_XID,RATE_GEO_GID,RATE_GEO_COST_GROUP_SEQ,DOMAIN_NAME
YOUR_DOMAIN.TL_RATE_001_CHICAGO_IL-DALLAS_TX,TL_RATE_001_CHICAGO_IL-DALLAS_TX,YOUR_DOMAIN.TL_RATE_001_CHICAGO_IL-DALLAS_TX,1,YOUR_DOMAIN
```

---

**File 6 — RATE_GEO_COST**

Defines the actual freight cost — the rate amount, currency, unit of measure, and effective dates.

<div class="note-box"><strong>Important:</strong> Row 3 of this file must contain the date format declaration exactly as shown in the template below. This tells OTM's database how to parse the date columns. Do not remove or modify this line.</div>

**Key fields:**

<div class="field-box"><strong>RATE_GEO_COST_GROUP_GID:</strong> GID of the Cost Group created in File 5</div>

<div class="field-box"><strong>RATE_GEO_COST_SEQ:</strong> Sequence number — use <code>1</code> for a single rate line. Add additional rows with incrementing sequences to add multiple cost components (e.g. base rate on sequence 1, fuel surcharge on sequence 2).</div>

<div class="field-box"><strong>CHARGE_AMOUNT:</strong> The rate amount</div>

<div class="field-box"><strong>CHARGE_CURRENCY_GID:</strong> Currency code, e.g. <code>USD</code></div>

<div class="field-box"><strong>CHARGE_AMOUNT_BASE:</strong> Same numeric value as CHARGE_AMOUNT</div>

<div class="field-box"><strong>CHARGE_UNIT_UOM_CODE:</strong> Unit of measure for the charge — <code>MI</code> for a per-mile rate, <code>FLAT</code> for a flat rate</div>

<div class="field-box"><strong>CHARGE_UNIT_COUNT:</strong> Number of units per calculation — typically <code>1</code></div>

<div class="field-box"><strong>CHARGE_MULTIPLIER:</strong> What OTM multiplies CHARGE_AMOUNT by — use <code>SHIPMENT.DISTANCE</code> for a per-mile rate, leave blank for a flat rate</div>

<div class="field-box"><strong>EFFECTIVE_DATE:</strong> Date this rate becomes active — format <code>YYYYMMDDHH24MISS</code>, e.g. <code>20260101000000</code> for 1 Jan 2026</div>

<div class="field-box"><strong>EXPIRATION_DATE:</strong> Date this rate expires — leave blank for no expiry</div>

**CSV Template:**

```csv
RATE_GEO_COST
RATE_GEO_COST_GROUP_GID,RATE_GEO_COST_SEQ,CHARGE_AMOUNT,CHARGE_CURRENCY_GID,CHARGE_AMOUNT_BASE,CHARGE_UNIT_UOM_CODE,CHARGE_UNIT_COUNT,CHARGE_MULTIPLIER,EFFECTIVE_DATE,EXPIRATION_DATE,DOMAIN_NAME
EXEC SQL ALTER SESSION SET NLS_DATE_FORMAT = 'YYYYMMDDHH24MISS'
YOUR_DOMAIN.TL_RATE_001_CHICAGO_IL-DALLAS_TX,1,1.99,USD,1.99,MI,1,SHIPMENT.DISTANCE,20260101000000,,YOUR_DOMAIN
```
