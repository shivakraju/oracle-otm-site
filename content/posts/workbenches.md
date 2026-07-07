---
title: "Workbenches"
date: 2026-05-14T18:55:04+00:00
draft: false
weight: 370
aliases:
  - "/2026/05/workbenches.html"
---

Workbenches provided easy way for users to view data across multiple object types on the same screen and also load data using some default criteria (query) as soon as workbench is launched.

  

There are several ways to configure the workbench and several features provided by Oracle but let's take a simple example of how to create a 3 level hierarchy display to show order releases related to a PO and shipment related to order releases.

  

A workbench will have one or more layouts and each layout can be assoicated to content from standard object types like Order Base, Order Release, etc.

  

**For our scenario, we need to create three layouts:**

  * Purchase Orders layout with content from Order Base table
  * Order Releases/Bookings layout with content from Order Release table. This content should be detail (child level) for Purchase Order content.
  * Shipment layout with contect from Buy Shipments table. This content should be detail (child) level content associated to order release selected.

**Note:** As pre-requisite you need to have screensets defined for each of above layouts ready before you proceed further. Screenset configuration is covered in a different post.

  

**To create a new workbench layout:**

  

**Navigate to:**

Configuration and Administration > User Configuration > Workbench Designer New

On the left hand side, select 'Create Layout' action. Enter below details:

  * Component Type: Table
  * Object Type: Order Base
  * Tab Name: Purchase Orders
  * Screen Set: OB_ORDER_BASE
  * Check 'Default first row selection'

Click OK and You will now see Layout added.

  

Click 'Done Editing' action on the right side panel.

  

To see PO data using this new Layout, click 'Add' button and query required Order Base(PO) as shown:

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgL_6EbMuHv0zO1qyMWkoqbKFN5EwMI4Y5KhSNkyudNH6CTjdonIXKvWEyHfr_Xqiertm1YDoCmr7jClf1WmWvOc-xk8bsv-lFncMfyJgL0WQSPz7FiJcGD10N9MV8cvZ0YY5M3ThK3GINbj-XGPvU_KbtSe5Y4xE9lNl6mCaLhXmkxBJjN3V191wzumzk=w400-h231)](https://blogger.googleusercontent.com/img/a/AVvXsEgL_6EbMuHv0zO1qyMWkoqbKFN5EwMI4Y5KhSNkyudNH6CTjdonIXKvWEyHfr_Xqiertm1YDoCmr7jClf1WmWvOc-xk8bsv-lFncMfyJgL0WQSPz7FiJcGD10N9MV8cvZ0YY5M3ThK3GINbj-XGPvU_KbtSe5Y4xE9lNl6mCaLhXmkxBJjN3V191wzumzk)

  
  

Now let's add a new layout to show order releases associated to PO.

For this, let's write an SQL that takes PO number as input and fetches Order Release GID:

**Saved Query:** TEMP_ORDER_REL

select order_release_gid from order_release where order_base_gid = '?'

On the right panel click 'Edit Layout', and on the top right corner of this layout, click button 'Split Horizontally'.

This will create a new empty layout on the right side of existing 'Purchase Orders' layout.

On this new blank layout, go to right top corner and click 'Add content' button and enter below details:

  * Component Type: Table
  * Object Type: Order Release
  * Tab Name: Bookings
  * Screen Set: ORDER_RELEASE
  * Detail Table: Check this option
  * Associated Tables: Purchase Order Saved Search: TEMP_ORDER_REL
    * Note: Using this 'Associated Table' option - link is being establshed from Parent PO level data to child order release level data record.

Click OK

  

Click 'Done Editing' from right side panel.

  

Now to test this select a PO that has order releases, and add query this PO using first layout. This should automatically display related order releases in second layout.

  

Now to see shipments associated to Bookings repeat the same steps as above but note that query associated should always point to primary key of the object type and to the associated base table. If you have complex SQL to fetch data, use IN clause on final SQL as shown in below example.

  

Create below Saved Query to pull Shipment GID for a particular Order Release:

  

**Saved Query ID:** TEMP_SHIPMENT with below SQL:

> > select shipment_gid 
>
>> from shipment
>
>> where shipment_gid in 
>
>> (select ssej.shipment_gid
>
>> from S_SHIP_UNIT_LINE ssulej, 
>
>> S_SHIP_UNIT ssuej, 
>
>> S_EQUIPMENT_S_SHIP_UNIT_JOIN sessuj, 
>
>> ORDER_RELEASE orej, 
>
>> SHIPMENT_S_EQUIPMENT_JOIN ssej,
>
>> shipment shp
>
>> where ssulej.order_release_gid=orej.order_release_gid 
>
>> and ssuej.s_ship_unit_gid=ssulej.s_ship_unit_gid 
>
>> and sessuj.s_ship_unit_gid=ssuej.s_ship_unit_gid
>
>> and orej.order_release_gid='?'
>
>> and ssej.s_equipment_gid=sessuj.s_equipment_gid)

Now edit 'Bookings' Layout and from top right corner click 'Split Vertically'

This will add blank layout on bottom of the 'Bookings' Layout. 

On this blank layout. go to top right corner and click 'Add Content' and enter below details:

  * Component Type: Table
  * Object Type: Buy Shipment
  * Tab Name: Shipments
  * Screen Set: BUY_SHIPMENT
  * Detail Table: Check this option
  * Associated Tables: 
    * Purchase Order Saved Search: Leave this as blank
    * Bookings Saved Search: TEMP_SHIPMENT
      * Note: Using this 'Associated Table' option - link is being establshed from Parent Order Release level data to child shipment level data record for this scenario

Click OK

  

Click 'Done Editing' from right side panel.

  

Now to test this select a PO that has order releases, and add query this PO using first layout. This should automatically display related order releases in second layout. Now select an order release that has shipments, you should see the shipment records on the third layout.