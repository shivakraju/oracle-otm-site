---
title: "OTM Order Management Data Structure"
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
---

Purchase Order   
  
PO record will have the basic details like source location, destination location, INCO terms, Item number, Qty etc. Note that PO might not have exact weight/volume details that might be required for planning orders. Usually POs are created in the ERP systems well ahead of time and sent to OTM.   
  
**PO tables:**  
  
OB_ORDER_BASE - PO Header  
OB_REFNUM - PO Header Reference number details  
OB_REMARK - PO Header remarks  
OB_ORDER_BASE_STATUS - PO Header status values  
OB_INVOLVED_PARTY - PO involved party details  
OB_LINE - PO Line  
OB_LINE_REFNUM - PO Line reference numbers  
OB_LINE_REMARK - PO Line level remarks  
OB_LINE_STATUS - PO Line level status values  
  
**Order Release:**  
  
Order Release(booking) in most cases is like a confirmed order for movement of items/goods from Point A to Point B on a specific date(date range) and this should also have the exact weight/volume of each ship unit required for transportation planning. On the Order Release we can also have constraints defined by business like specific carrier request, itinerary request etc.   
  
ORDER_RELEASE - Order Header  
ORDER_RELEASE_REFNUM - Order Header Refnum  
ORDER_RELEASE_REMARK - Order Header Remarks  
ORDER_RELEASE_STATUS - Order Header Status  
ORDER_RELEASE_INV_PARTY - Order Involved Party records  
ORDER_RELEASE_LINE - Order Line with item details  
ORDER_RELEASE_LINE_REFNUM - Order Line reference numbers  
ORDER_RELEASE_LINE_REMARK - Order Line level remarks  
  
SHIP_UNIT - Order Ship Unit  
SHIP_UNIT_LINE - Order Ship Unit Line  
SHIP_UNIT_LINE_REFNUM - Ship Unit level reference numbers  
SHIP_UNIT_LINE_REMARK - Ship Unit level remarks  
  
Note that Order Ship Units are different from Shipment Ship Units. Order Ship Units are created from Order Release Line information based on 'Order Type' configuration on the Order Release. Most implementations have one to one mapping between order release line and order release ship unit. But in some cases like rainbow pallets etc. multiple items can go into single pallet(single ship unit). In this case we might see multiple ship unit lines under a single ship unit. Ship Unit is like a pallet that is actually planned to a shipment. Planning considers the weight and volume that exists against the order release ship units.  
  
  

Order Movements

  

Order Movements are created from order releases and they honor the constraints put on the Order Release. One shipment is created for each Order Movement.

They can be created using ORDER RELEASE action or from the UI using Order Release > Actions menu.

![](/images/otm-order-management-data-stru-img1-1c11f626db.png)

Order Movements can be used to plan the different legs of the Order say Source location to HUB, HUB to final destination etc on different days by the planner. Say on Day1, planner want to consolidate all the orders coming from supplier to HUB location and on Day2 planner want to plan/consolidate different shipments going from HUB to inbound warehouses or customers.

  

**Business use case:** In XXX company, when supplier books the order, order release is created. If Items on the order release is having ‘DAYS ON HAND’ refnum value less than 14 days, then Agent will update the Itinerary as DIRECT Itinerary instead of HUB Itinerary. Difference between Direct and HUB Itinieraray is that HUB itinerary will have two legs – source location to HUB(California HUB etc), California HUB to Destination location etc. Since this constraint is updated on the order release, once we call standard action ‘CREATE ORDER MOVEMENTS’ it will create two order movements in case of HUB Itinerary and users can plan these order movements. This will have better control of planning.

  

**Below are the Order Movement related tables:**

ORDER_MOVEMENT

ORDER_MOVEMENT_STATUS

ORDER_MOVEMENT_REFNUM

ORDER_MOVEMENT_REMARK

ORDER_MOVEMENT_INV_PARTY  
  
Items  
  
Item is like an individual unit that is sold by a manufacturer like a pencil box.  
  

**Table:**

ITEM

  

Ship Unit Spec(Packaging Unit)

  

Ship Unit Spec - also referred to as Pallet or Transportation Handling Unit(THU) or Carton is similar to a box with specific dimensions - LxWxH. This is linked to the Ship Unit on an order. This is the unit that will be physically shipped and whose dimensions are critical for Order Planning.

  

**Table:**

SHIP_UNIT_SPEC

  

**Packaged Item:**

  

Packaged item links your item to ship unit spec(pallet). Packaged Item is the entity mentioned on the Order Base(PO), Order Release, etc  
  
**This will have information like:**

  * Item ID
  * Packaging Unit( which is Ship Unit Spec defined above in most cases)
  * Package dimensions
  * Ti/High – This term is used in logistic business to indicate number of cartons per layer(Ti) and number of layer(High) used on the pallet.

**Table:** 

PACKAGED_ITEM  
  
**Notes:** Items > Packaged Items > Ship Unit Spec > Equipment/Container > Shipment would be packaging hierarchy. But most implementations will have Item ID same as Packaged Item ID and use Ship Unit spec like a CARTON(box) with Ship Unit dimensions same as Ship Unit Spec dimensions. Ship Units go in Equipment.

  
**Note:** Please post corrections(if any) to 'learnotm@outlook.com'