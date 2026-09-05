---
title: "Shipment Management Data Structure"
date: 2016-05-03T20:01:00+00:00
draft: false
weight: 120
tags:
  - "Itinerary"
  - "Shipment Stop"
  - "Shipment"
  - "Shipment Ship Unit"
  - "Equipment"
aliases:
  - "/2016/05/otm-shipment-management-data-structure.html"
keywords:
  - "Oracle OTM shipment management tables"
  - "OTM shipment ship unit data structure"
  - "Oracle OTM shipment stop tables"
  - "OTM shipment equipment assignment"
  - "Oracle OTM shipment ship unit line"
  - "OTM secondary shipment primary shipment"
  - "Oracle OTM ASN inbound shipment"
  - "OTM CIN qualifier ship unit line"
  - "Oracle Transportation Management shipment schema"
  - "OTM bulk plan shipment split equipment"
  - "Oracle OTM itinerary shipment data model"
description: "Describes the Oracle OTM shipment management data structure, including how shipments relate to equipment, ship units, and order release lines, and how bulk plan splits quantities across containers."
---

A shipment in OTM consists of one or more **Equipment** records (containers or trailers), **Shipment Ship Units** loaded into each equipment, and **Shipment Ship Unit Lines** that link back to the original Order Release lines. Understanding this structure is essential for troubleshooting planning results, writing integration queries, and working with carrier tracking events.

**Shipment Structure:**

When OTM plans an Order Release to a shipment, it creates Shipment Ship Units and assigns them to equipment. If a Bulk Plan splits an order across two containers — say 60 units in one and 40 in another — that split is recorded at the Shipment Ship Unit Line level. This line is the critical link between the shipment and the originating order: it ties back to a specific item, Order Release Line, Order Release, and Order Base.

<div class="note-box"><strong>Secondary shipments:</strong> When secondary shipments are created from a primary shipment, the Shipment Ship Unit Lines are shared — they are not duplicated for each secondary shipment.</div>

<div class="note-box"><strong>ASN integration:</strong> When OTM receives an ASN (Advance Ship Notice) directly via integration, populate the <code>CIN</code> qualifier on the Ship Unit Line reference number and use the standard shipment action to link the ship unit back to the Order Base or PO.</div>

![OTM shipment structure showing order release ship units splitting across two equipment containers](/images/otm-shipment-management-data-s-img1-4bcedcc132.png)

**Shipment tables:**

<div class="field-box"><strong>SHIPMENT</strong> — Shipment header. Stores dates, locations, status, carrier, and overall shipment attributes.</div>

<div class="field-box"><strong>S_EQUIPMENT</strong> — Shipment equipment (container/trailer). For vessel shipments, a single shipment can have multiple equipment records — one per container on the vessel.</div>

<div class="field-box"><strong>SHIPMENT_S_EQUIPMENT_JOIN</strong> — Join table linking a shipment to its equipment records.</div>

**Shipment Ship Unit tables:**

<div class="field-box"><strong>S_SHIP_UNIT</strong> — Shipment Ship Unit. Represents a pallet or carton assigned to equipment on the shipment.</div>

<div class="field-box"><strong>S_SHIP_UNIT_REFNUM</strong> — Reference numbers on the Shipment Ship Unit.</div>

<div class="field-box"><strong>S_SHIP_UNIT_REMARK</strong> — Remarks on the Shipment Ship Unit.</div>

<div class="field-box"><strong>S_SHIP_UNIT_LINE</strong> — Shipment Ship Unit Line. Links the shipment ship unit back to a specific Order Release Line, Order Release, and Order Base. Captures the split quantity if a single order line was split across containers during planning.</div>

<div class="field-box"><strong>S_SHIP_UNIT_LINE_REFNUM</strong> — Reference numbers at Ship Unit Line level.</div>

<div class="field-box"><strong>S_SHIP_UNIT_LINE_REMARK</strong> — Remarks at Ship Unit Line level.</div>

<div class="field-box"><strong>S_EQUIPMENT_S_SHIP_UNIT_JOIN</strong> — Links Shipment Ship Units to the specific equipment they are loaded into.</div>

<div class="field-box"><strong>S_SHIP_UNIT_PIECE</strong> — Used when load configuration is enabled. Stores X/Y/Z coordinates for each item placed inside the container — (0,0,0) is the front left corner, Z runs along the container length. Also records orientation (lengthwise, widthwise, etc.).</div>

**Shipment Stop tables:**

<div class="field-box"><strong>SHIPMENT_STOP</strong> — Stop-level details including arrival and departure dates, stop sequence, and location.</div>

<div class="field-box"><strong>SHIPMENT_STOP_D</strong> — Stop-level ship unit assignments — which ship units are picked up or dropped off at each stop.</div>

**Equipment:**

Equipment represents the physical container used to move freight — a 53 FT trailer, a 40 FT ocean container, etc. The same container can move across multiple legs and transport modes (intermodal). For example, a sealed container may travel from a supplier in China to a Chinese port by truck, then cross to a US port by vessel, then move to a warehouse by truck. Note that trucks have two parts: the Power Unit (engine) and the Trailer (that holds the container).

<div class="field-box"><strong>EQUIPMENT_GROUP</strong> — Defines equipment types (e.g. <code>53_FTL</code>) along with their dimensions and capacity.</div>

<div class="field-box"><strong>EQUIPMENT_GROUP_PROFILE</strong> — A logical grouping of Equipment Groups used in itinerary and rate configurations.</div>

**Itinerary:**

An Itinerary defines the scope of shipment planning — which origin/destination regions are covered, what equipment types are valid for each region pair, what transport modes apply, and how many legs exist between source and destination.

For example, an import itinerary from China suppliers to a US warehouse might have three legs:

<div class="field-box"><strong>Leg 1:</strong> Supplier region to China port — LORRY equipment, TL transport mode.</div>

<div class="field-box"><strong>Leg 2:</strong> China port to US port — VESSEL transport mode.</div>

<div class="field-box"><strong>Leg 3:</strong> US port to US warehouse — US_GROUND equipment (53 FT, 40 FT), TL transport mode.</div>

Identifying the itinerary is the first step OTM Bulk Plan performs. Rate Offerings and Rate Records must also be defined for each leg's source/destination region, transport mode, and equipment combination.

**Itinerary tables:**

<div class="field-box"><strong>ITINERARY</strong> — Itinerary header with name and lane (source/destination region) details.</div>

<div class="field-box"><strong>ITINERARY_DETAIL</strong> — Leg names and sequence within an itinerary.</div>

<div class="field-box"><strong>LEG</strong> — Leg-level details: transport mode, equipment group profile, and applicable locations.</div>

**Shipment Tracking Events:**

Once goods are picked up and the shipment is in transit, the carrier can send tracking events to OTM specifying the event location and status code. These are stored in:

<div class="field-box"><strong>IE_SHIPMENTSTATUS</strong> — Inbound event record with event date and status code.</div>

<div class="field-box"><strong>SS_STATUS_HISTORY</strong> — Links the event to the shipment stop and location.</div>

<div class="field-box"><strong>BS_STATUS_CODE</strong> — Reference table for status code descriptions.</div>

**Sample query — tracking events for a shipment:**

```sql
SELECT ies.i_transaction_no,
       shp.shipment_gid,
       ssh.event_location_gid,
       ssh.shipment_stop_num,
       TO_CHAR(ies.eventdate, 'MM/DD/YYYY HH24:MI:SS') AS event_date,
       ies.status_code_gid,
       bsc.description
FROM   shipment shp,
       ss_status_history ssh,
       ie_shipmentstatus ies,
       bs_status_code bsc
WHERE  shp.shipment_gid = 'DOMAIN.554680'
AND    shp.shipment_gid = ssh.shipment_gid
AND    ies.i_transaction_no = ssh.i_transaction_no
AND    ies.status_code_gid = bsc.bs_status_code_gid
ORDER BY ies.eventdate
```

**Shipment Tender:**

<div class="field-box"><strong>TENDER_COLLABORATION</strong> — Key tender table. Stores source/destination locations, expected response time, pickup time, delivery time, and other tender attributes.</div>

<div class="field-box"><strong>TENDER_COLLAB_SERVPROV</strong> — Links the tender to the carrier, including acceptance code and carrier response.</div>

<div class="field-box"><strong>TENDER_COLLABORATION_STATUS</strong> — Current shipment status associated with the tender.</div>

<div class="note-box"><strong>Note:</strong> <code>i_transaction_no</code> is the unique reference for each tender. Carrier responses must be sent against the latest OUTSTANDING tender record.</div>

**Sample queries:**

```sql
-- Order Release and its ship units
SELECT * FROM order_release WHERE order_release_gid = 'DOMAIN.TST3PL1029001-001';
SELECT * FROM order_release_line WHERE order_release_gid = 'DOMAIN.TST3PL1029001-001';
SELECT * FROM ship_unit WHERE order_release_gid = 'DOMAIN.TST3PL1029001-001';
SELECT * FROM ship_unit_line
WHERE  order_release_line_gid IN (
         SELECT order_release_line_gid FROM order_release_line
         WHERE  order_release_gid = 'DOMAIN.TST3PL1029001-001');

-- Shipment and its equipment, ship units, and stops
SELECT * FROM shipment WHERE shipment_gid = 'DOMAIN.267199';
SELECT * FROM shipment_s_equipment_join WHERE shipment_gid = 'DOMAIN.267199';
SELECT * FROM s_equipment_s_ship_unit_join
WHERE  s_equipment_gid IN (
         SELECT s_equipment_gid FROM shipment_s_equipment_join
         WHERE  shipment_gid = 'DOMAIN.267199');
SELECT * FROM shipment_stop_d WHERE shipment_gid = 'DOMAIN.267199';
SELECT * FROM s_ship_unit
WHERE  s_ship_unit_gid IN (
         SELECT s_ship_unit_gid FROM shipment_stop_d
         WHERE  shipment_gid = 'DOMAIN.267199');
SELECT * FROM s_ship_unit_line
WHERE  s_ship_unit_gid IN (
         SELECT s_ship_unit_gid FROM shipment_stop_d
         WHERE  shipment_gid = 'DOMAIN.267199');
```

**What's Next:**

The next topic covers the Contract and Rate Management Data Structure — how OTM stores carrier contracts, rate records, and the tables used to look up freight costs during planning.

Next Topic: [Contract & Rate Management Data Structure](/posts/otm-contract-rate-management-data-structure/)
