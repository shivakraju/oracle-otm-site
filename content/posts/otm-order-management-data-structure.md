---
title: "Order Management Data Structure"
date: 2016-05-03T17:42:00+00:00
draft: false
weight: 110
tags:
  - "Packaging Unit"
  - "Item"
  - "Ship Unit Spec"
  - "Order Movement"
  - "Order Release"
  - "Purchase Order"
  - "OTM"
  - "Packaged Item"
  - "Learn"
  - "Order Base"
  - "Oracle"
aliases:
  - "/2016/05/otm-order-management-data-structure.html"
keywords:
  - "Oracle OTM order management tables"
  - "OTM OB_ORDER_BASE table structure"
  - "Oracle OTM purchase order data model"
  - "OTM order release data structure"
  - "Oracle OTM order base order release tables"
  - "OTM packaged item ship unit spec"
  - "Oracle OTM order movement tables"
  - "OTM OB_LINE table explained"
  - "Oracle Transportation Management order schema"
  - "OTM packaging unit data structure"
  - "Oracle OTM GLOGOWNER order tables"
description: "Details the Oracle OTM order management database structure, covering OB_ORDER_BASE, OB_LINE, Order Release, Packaging Unit, and Ship Unit Spec tables used to model purchase orders and bookings."
---

OTM models order management across three levels: the **Purchase Order** (what was ordered), the **Order Release** (a confirmed booking for movement), and **Order Movements** (the planned legs of that movement). Understanding this hierarchy and the underlying tables is essential for integration work and troubleshooting.

**Purchase Order (Order Base):**

A Purchase Order represents the commercial transaction — what items are being moved, from where, to where, and under what terms. POs are typically created in an ERP system (e.g. Oracle E-Business Suite) and sent to OTM via inbound integration. Note that POs often lack exact weight and volume details, which are required for shipment planning — those are defined on the Order Release.

**PO Header tables:**

<div class="field-box"><strong>OB_ORDER_BASE</strong> — PO header. Stores source/destination locations, INCO terms, and overall PO attributes.</div>

<div class="field-box"><strong>OB_REFNUM</strong> — PO header reference numbers (e.g. buyer PO number, vendor reference).</div>

<div class="field-box"><strong>OB_REMARK</strong> — Free-text remarks at PO header level.</div>

<div class="field-box"><strong>OB_ORDER_BASE_STATUS</strong> — Status values attached to the PO header.</div>

<div class="field-box"><strong>OB_INVOLVED_PARTY</strong> — Parties involved in the PO (e.g. buyer, seller, freight payer).</div>

**PO Line tables:**

<div class="field-box"><strong>OB_LINE</strong> — PO line. One row per item on the PO, with item number, quantity, and unit of measure.</div>

<div class="field-box"><strong>OB_LINE_REFNUM</strong> — Reference numbers at PO line level.</div>

<div class="field-box"><strong>OB_LINE_REMARK</strong> — Remarks at PO line level.</div>

<div class="field-box"><strong>OB_LINE_STATUS</strong> — Status values at PO line level.</div>

**Order Release:**

An Order Release (booking) is a confirmed request for transportation — it specifies the exact weight, volume, and ship units required for planning. Unlike a PO, an Order Release has enough detail for OTM to plan and tender a shipment. Business constraints such as carrier preference or itinerary can be set directly on the Order Release.

**Order Release tables:**

<div class="field-box"><strong>ORDER_RELEASE</strong> — Order Release header.</div>

<div class="field-box"><strong>ORDER_RELEASE_REFNUM</strong> — Reference numbers at header level.</div>

<div class="field-box"><strong>ORDER_RELEASE_REMARK</strong> — Remarks at header level.</div>

<div class="field-box"><strong>ORDER_RELEASE_STATUS</strong> — Status values at header level.</div>

<div class="field-box"><strong>ORDER_RELEASE_INV_PARTY</strong> — Involved party records on the order release.</div>

<div class="field-box"><strong>ORDER_RELEASE_LINE</strong> — Order Release line with item details and quantity.</div>

<div class="field-box"><strong>ORDER_RELEASE_LINE_REFNUM</strong> — Reference numbers at line level.</div>

<div class="field-box"><strong>ORDER_RELEASE_LINE_REMARK</strong> — Remarks at line level.</div>

**Ship Unit tables:**

<div class="field-box"><strong>SHIP_UNIT</strong> — A physical handling unit (e.g. pallet) derived from the Order Release line. This is what OTM plans to a shipment — weight and volume on the Ship Unit drive planning.</div>

<div class="field-box"><strong>SHIP_UNIT_LINE</strong> — Items within the Ship Unit. Most implementations have a one-to-one mapping between Order Release Line and Ship Unit, but multi-item pallets (rainbow pallets) can have multiple Ship Unit Lines under one Ship Unit.</div>

<div class="field-box"><strong>SHIP_UNIT_LINE_REFNUM</strong> — Reference numbers at Ship Unit Line level.</div>

<div class="field-box"><strong>SHIP_UNIT_LINE_REMARK</strong> — Remarks at Ship Unit Line level.</div>

<div class="note-box"><strong>Note:</strong> Order Ship Units and Shipment Ship Units are separate entities. Order Ship Units are created from Order Release Lines based on the Order Type configuration on the Order Release. Shipment Ship Units are created when OTM assigns the order to a shipment during planning.</div>

**Order Movements:**

Order Movements are created from Order Releases and represent the individual legs of transportation. One shipment is created per Order Movement. They honour any constraints set on the Order Release (carrier, itinerary, date windows).

Order Movements are created either via the **Create Order Movements** action on the Order Release, or automatically by an OTM Agent. A HUB itinerary generates two Order Movements — one from origin to hub, one from hub to destination — allowing planners to consolidate and plan each leg independently.

![OTM Order Movement screen](/images/otm-order-management-data-stru-img1-1c11f626db.png)

**Order Movement tables:**

<div class="field-box"><strong>ORDER_MOVEMENT</strong> — One row per planned leg.</div>

<div class="field-box"><strong>ORDER_MOVEMENT_STATUS</strong> — Status values on the Order Movement.</div>

<div class="field-box"><strong>ORDER_MOVEMENT_REFNUM</strong> — Reference numbers on the Order Movement.</div>

<div class="field-box"><strong>ORDER_MOVEMENT_REMARK</strong> — Remarks on the Order Movement.</div>

<div class="field-box"><strong>ORDER_MOVEMENT_INV_PARTY</strong> — Involved parties on the Order Movement.</div>

**Items, Packaged Items, and Ship Unit Specs:**

<div class="field-box"><strong>ITEM</strong> — Represents an individual product SKU (e.g. a pencil box). Items are the base unit of inventory in OTM.</div>

<div class="field-box"><strong>SHIP_UNIT_SPEC</strong> — Also known as a Packaging Unit or Transportation Handling Unit (THU). Defines the physical dimensions (L x W x H) of a container such as a pallet or carton. This is linked to Ship Units on the order and drives planning calculations.</div>

<div class="field-box"><strong>PACKAGED_ITEM</strong> — Links an Item to a Ship Unit Spec. This is the entity referenced on the Order Base, Order Release, and other transactions. It carries Item ID, Packaging Unit, package dimensions, and Ti/High values (Ti = cartons per layer, High = number of layers on a pallet).</div>

<div class="note-box"><strong>Packaging hierarchy:</strong> Items > Packaged Items > Ship Unit Spec > Equipment/Container > Shipment. In most implementations, Item ID and Packaged Item ID are the same, and the Ship Unit Spec is a CARTON whose dimensions match the Ship Unit dimensions. Ship Units are loaded into Equipment for planning.</div>

**What's Next:**

The next topic covers the Shipment Management Data Structure — how OTM organises shipments, stops, ship units, and status events in the database.

Next Topic: [Shipment Management Data Structure](/posts/otm-shipment-management-data-structure/)
