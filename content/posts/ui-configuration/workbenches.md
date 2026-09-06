---
title: "Workbenches"
date: 2026-05-14T18:55:04+00:00
draft: false
weight: 40
aliases:
  - "/2026/05/workbenches.html"
keywords:
  - "Oracle OTM workbench configuration"
  - "OTM workbench layout setup"
  - "Oracle OTM multi-object workbench"
  - "OTM workbench order base order release shipment"
  - "Oracle OTM workbench hierarchy display"
  - "OTM workbench screenset layout"
  - "Oracle Transportation Management workbench"
  - "OTM workbench parent child content"
  - "Oracle OTM workbench default query"
  - "OTM workbench buy shipments order release"
description: "Explains how to create Oracle OTM Workbenches that display multiple related business objects in a hierarchical view — for example, Purchase Orders linked to Order Releases and Shipments — on a single screen."
url: "/posts/workbenches/"
---

Workbenches provide an easy way for users to view data across multiple object types on the same screen and load data using a default query as soon as the workbench is launched.

There are several ways to configure a workbench, but below is a simple example of how to create a three-level hierarchy showing Order Releases related to a PO and Shipments related to those Order Releases.

A workbench has one or more layouts and each layout can be associated to content from standard object types like Order Base, Order Release, etc.

**For this scenario, three layouts are needed:**

- Purchase Orders layout with content from the Order Base table
- Order Releases/Bookings layout with content from the Order Release table — this is a detail (child) level for the Purchase Order content
- Shipment layout with content from the Buy Shipments table — this is detail (child) level content associated to the selected order release

<div class="note-box"><strong>Note:</strong> As a prerequisite, you need screensets defined for each of the above layouts before proceeding. Screenset configuration is covered in a separate post.</div>

**To create a new workbench layout:**

<div class="step-box">Configuration and Administration > User Configuration > Workbench Designer > New</div>

On the left-hand side, select 'Create Layout' action and enter the following details:

- <div class="field-box"><strong>Component Type:</strong> Table</div>
- <div class="field-box"><strong>Object Type:</strong> Order Base</div>
- <div class="field-box"><strong>Tab Name:</strong> Purchase Orders</div>
- <div class="field-box"><strong>Screen Set:</strong> OB_ORDER_BASE</div>
- Check 'Default first row selection'

Click OK. You will now see the Layout added. Click 'Done Editing' on the right side panel.

To see PO data using this new Layout, click the 'Add' button and query the required Order Base (PO):

[![OTM workbench Purchase Orders layout](https://blogger.googleusercontent.com/img/a/AVvXsEgL_6EbMuHv0zO1qyMWkoqbKFN5EwMI4Y5KhSNkyudNH6CTjdonIXKvWEyHfr_Xqiertm1YDoCmr7jClf1WmWvOc-xk8bsv-lFncMfyJgL0WQSPz7FiJcGD10N9MV8cvZ0YY5M3ThK3GINbj-XGPvU_KbtSe5Y4xE9lNl6mCaLhXmkxBJjN3V191wzumzk=w400-h231)](https://blogger.googleusercontent.com/img/a/AVvXsEgL_6EbMuHv0zO1qyMWkoqbKFN5EwMI4Y5KhSNkyudNH6CTjdonIXKvWEyHfr_Xqiertm1YDoCmr7jClf1WmWvOc-xk8bsv-lFncMfyJgL0WQSPz7FiJcGD10N9MV8cvZ0YY5M3ThK3GINbj-XGPvU_KbtSe5Y4xE9lNl6mCaLhXmkxBJjN3V191wzumzk)

Now add a new layout to show Order Releases associated to the PO. First, create a saved query that takes the PO number as input and returns the Order Release GID:

<div class="field-box"><strong>Saved Query ID:</strong> TEMP_ORDER_REL</div>

```sql
select order_release_gid from order_release where order_base_gid = '?'
```

On the right panel click 'Edit Layout', and in the top right corner of the layout click 'Split Horizontally'. This creates a new empty layout to the right of the existing 'Purchase Orders' layout.

On the new blank layout, go to the top right corner and click 'Add content' and enter:

- <div class="field-box"><strong>Component Type:</strong> Table</div>
- <div class="field-box"><strong>Object Type:</strong> Order Release</div>
- <div class="field-box"><strong>Tab Name:</strong> Bookings</div>
- <div class="field-box"><strong>Screen Set:</strong> ORDER_RELEASE</div>
- Check 'Detail Table'
- <div class="field-box"><strong>Associated Tables — Purchase Order Saved Search:</strong> TEMP_ORDER_REL</div>

<div class="note-box"><strong>Note:</strong> The 'Associated Table' option establishes the link from the parent PO level data to child order release level data records.</div>

Click OK, then click 'Done Editing' from the right side panel.

To test, select a PO that has order releases and query it using the first layout. The related order releases should automatically appear in the second layout.

To show Shipments associated to Bookings, repeat the same steps but note that the query associated to a layout should always point to the primary key of the object type. If you have complex SQL to fetch data, use an IN clause as shown below.

Create the following Saved Query to pull Shipment GID for a particular Order Release:

<div class="field-box"><strong>Saved Query ID:</strong> TEMP_SHIPMENT</div>

```sql
select shipment_gid
from shipment
where shipment_gid in
(select ssej.shipment_gid
from S_SHIP_UNIT_LINE ssulej,
S_SHIP_UNIT ssuej,
S_EQUIPMENT_S_SHIP_UNIT_JOIN sessuj,
ORDER_RELEASE orej,
SHIPMENT_S_EQUIPMENT_JOIN ssej,
shipment shp
where ssulej.order_release_gid=orej.order_release_gid
and ssuej.s_ship_unit_gid=ssulej.s_ship_unit_gid
and sessuj.s_ship_unit_gid=ssuej.s_ship_unit_gid
and orej.order_release_gid='?'
and ssej.s_equipment_gid=sessuj.s_equipment_gid)
```

Now edit the 'Bookings' layout and from the top right corner click 'Split Vertically'. This adds a blank layout at the bottom of the 'Bookings' layout.

On the blank layout, go to the top right corner and click 'Add Content' and enter:

- <div class="field-box"><strong>Component Type:</strong> Table</div>
- <div class="field-box"><strong>Object Type:</strong> Buy Shipment</div>
- <div class="field-box"><strong>Tab Name:</strong> Shipments</div>
- <div class="field-box"><strong>Screen Set:</strong> BUY_SHIPMENT</div>
- Check 'Detail Table'
- <div class="field-box"><strong>Associated Tables — Purchase Order Saved Search:</strong> Leave blank</div>
- <div class="field-box"><strong>Associated Tables — Bookings Saved Search:</strong> TEMP_SHIPMENT</div>

<div class="note-box"><strong>Note:</strong> The 'Associated Table' option here establishes the link from the parent Order Release level data to child shipment level data records.</div>

Click OK, then click 'Done Editing' from the right side panel.

To test, select a PO that has order releases and query it using the first layout. Related order releases should appear in the second layout. Selecting an order release that has shipments should display the shipment records in the third layout.

