---
title: "OTM Shipment Management Data Structure"
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
---

Shipments

Shipment will have - Equipment(s), Shipment Ship Units within an Equipment, and Shipment Ship Unit lines within a Shipment Ship Unit.Note that at shipment level, ship units are always tied to equipment.  
  
So, if a order release ship unit has quantity ‘100’, it may split across two equipments with say 60 quantity going in one equipment and other 40 going into second equipment during a bulk plan. Shipment Ship Unit Line will show this split information and is critical entity which is tied to a specific item, order release line, order release and order base. If we un-assign the shipment from order release, we are just breaking this link at this level.  

  

**Note:** If secondary shipments are created from primary shipment, shipment ship unit lines are shared for all the shipments. They are not created for each secondary shipment.

  

If OTM is receiving ASN(Shipment) directly via Integration, we can populate CIN qualifier on the Ship Unit Line refnum and use standard shipment action to link ship unit to Order Base/PO.

  

![](/images/otm-shipment-management-data-s-img1-4bcedcc132.png)

  

In this example an order has two lines and there order configuration is one to one which means one line has one ship unit only.

  

This example will show link between ship units on the order and ship units on the shipment.

  

Here we can see that ship unit on the order for item 400000879017 got split into two containers and hence into two ship units on the shipment:

  

**Sample Queries:**  
  
select * from order_release where order_release_gid = 'DOMAIN.TST3PL1029001-001'  
  
select * from order_release_line where order_release_gid = 'DOMAIN.TST3PL1029001-001'  
  
select * from ship_unit where order_release_gid = 'DOMAIN.TST3PL1029001-001'  
  
select * from ship_unit_line where order_release_line_gid in (  
select order_release_line_gid from order_release_line where order_release_gid = 'DOMAIN.TST3PL1029001-001')   
  
select * from shipment where shipment_gid = 'DOMAIN.267199'  
  
select * from shipment_s_equipment_join where shipment_gid = 'DOMAIN.267199'  
  
select * from s_equipment_s_ship_unit_join where s_equipment_gid in   
(select s_equipment_gid from shipment_s_equipment_join where shipment_gid = 'DOMAIN.267199')  
  
select * from shipment_stop_d where shipment_gid = 'DOMAIN.267199'   
  
select * from s_ship_unit where s_ship_unit_gid in  
(select s_ship_unit_gid from shipment_stop_d where shipment_gid = 'DOMAIN.267199')  
  
select * from s_ship_unit_line where s_ship_unit_gid in  
(select s_ship_unit_gid from shipment_stop_d where shipment_gid = 'DOMAIN.267199')  
  

**Below is the list of shipment related tables/views:**  
  
**Shipment tables:**  
  
SHIPMENT - Shipment Header details   
S_EQUIPMENT - Shipment Container(Equipment) details. Note incase of VESSEL shipments you will have multiple containers/equipment within the same shipment.  
SHIPMENT_S_EQUIPMENT_JOIN - Shows link between Shipment and Equipments

  
**Shipment Ship Unit tables:**  
  
S_SHIP_UNIT - Shipment Ship Unit data  
S_SHIP_UNIT_REFNUM  
S_SHIP_UNIT_REMARK  
S_SHIP_UNIT_LINE - Shipment Shp Unit Line data  
S_SHIP_UNIT_LINE_REFNUM  
S_SHIP_UNIT_LINE_REMARK  
S_EQUIPMENT_S_SHIP_UNIT_JOIN - Shipment Ship Units within a container  
S_SHIP_UNIT_PIECE - When using load configuration feature, this table will show X,Y,Z location co-ordinates for the items placed in the container. (0,0,0) is starting point for front left corner of the container and Z co-ordinate runs on length direction of the container.This will also show the orientation details - if ship unit is placed lengthwise, width wise etc.   
  
**Shipment Stop tables:**  
  
SHIPMENT_STOP - Shipment Stop level details like Arrival, Departure dates etc  
SHIPMENT_STOP_D - Stop level shipment ship units and other details.  
  
**Equipments:**  
  
Equipments are nothing but physical containers like 53 FT, 40 FT containers in which cartons/pallets are shipped from one location to another location. These are usually shipped across various legs/transport modes(INTERMODAL). For example a container sealed in China might arrive from China supplier location to China port, same container might be loaded into a Ship(Vessel) and transported to US Port, same container is unloaded from Vessel and placed on a trailer(truck) and shipped to a warehouse in US. Please note that trucks will have two parts - Power Unit(Engine) and Trailer(that holds container).   
  
**Table:**  
EQUIPMENT_GROUP - This table can hold the equipment name like 53_FTL along with dimensions.  
EQUIPMENT_GROUP_PROFILE - This is logical grouping of equipment groups that can be used in various setups  
  
**Itinerary:**  
  
Itineraries define the scope for your shipment planning like what source and destinations regions are covered by your OTM panning configuration, what are the equipments that are feasible for that source/dest region combinations, what are the transport modes for that source/dest combinations, how many different legs exist between that source/dest regions, etc.  
For example, if you want to import items from suppliers in CHINA to your company warehouse in USA, you might define a mult-leg itinerary with following configurations:  
**Leg1:** Supplier Region to China Port Locations with LORRY(2T,5T,etc) as equipment group profile and TL as transport mode.  
**Leg2:** China Port locations to US Port Locations with VESSEL as transport mode.  
**Leg3:** US Port locations to US Warehouse Locations with US_GROUND(53FT, 40FT, etc) equipment group profile and TL as transport mode.  
  
Identifying the itinerary is the first step that OTM Bulk Plan will perform. Note that you also need to define Rate Offering(Contract with carrier), Rate Records, etc for the source/dest region combinations, transport modes, etc.  
  
**Itinerary tables:**  
ITINERARY - Itinerary header with name, lane(source/dest) details  
ITINERARY_DETAIL - Leg names and sequence within an Itinerary  
LEG - Leg level details like transport mode, equipment group profile, etc  
  
**Shipment Tracking Events:**  
  
Once the goods are picked by the carrier and if the shipment is "in-transit", carrier can send events to OTMspecifying the event location and event description(code). Below tables store the details:  
  
IE_SHIPMENTSTATUS  
SS_STATUS_HISTORY  
BS_STATUS_CODE  
  
**Sample Query to fetch event details for a shipment:**  
  
select ies.i_transaction_no,shp.shipment_gid,  
ssh.event_location_gid,  
ssh.shipment_stop_num,  
to_char(ies.eventdate,'MM/DD/YYYY HH24:MI:SS'),  
ies.status_code_gid,  
bsc.description  
from shipment shp,  
ss_status_history ssh,  
ie_shipmentstatus ies,  
bs_status_code bsc  
where shp.shipment_gid = 'DOMAIN.554680'  
and shp.shipment_gid = ssh.shipment_gid  
and ies.i_transaction_no = ssh.i_transaction_no  
and ies.status_code_gid = bsc.bs_status_code_gid  
ORDER BY IES.EVENTDATE  
  
**Shipment Tender:**  
  
**Shipment tender info is captured in below tables:**  
  
select * from tender_collaboration where SHIPMENT_GID = 'DOM.SHP_ID'  
  
This is key table with details like source location, destination location, expected response time, pickup time, delivery time, etc  
  
select * from tender_collab_servprov where i_transaction_no = <from above query>  
  
This table will link the tender information to carrier involved, tender acceptance code, etc  
  
select * from tender_collaboration_status where i_transaction_no = <from above query>  
  
This table shows the current shipment status associated to the tender.  
  
Note that i_transaction_no is the unique reference for each tender. Response should be sent against the latest OUTSTANDING tender(i_transaction_no).   
  
Standard OTM Views  
  
To find Order Releases associated to shipment or vice-versa:  
view_shipment_order_release  
  
To find Order Base(PO) associated to shipment or vice-versa:  
view_shipment_order_base