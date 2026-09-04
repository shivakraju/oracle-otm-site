---
title: "Basic Logistics Terminology"
date: 2016-04-14T23:00:00+00:00
draft: false
weight: 40
tags:
  - "THU"
  - "LTL"
  - "Stopoff charge"
  - "Inbound Shipping"
  - "Bill of Lading"
  - "INCOTERM"
  - "Pallet"
  - "Diversion"
  - "3PL"
  - "Consignee"
  - "Container"
  - "Dock"
  - "Yard"
  - "TL"
  - "Demurrage"
  - "Supplier"
  - "Carrier"
  - "Carton"
  - "Outbound Shipping"
  - "FTL"
aliases:
  - "/2016/05/otm-basic-terminology.html"
keywords:
  - "logistics terminology for OTM consultants"
  - "carrier SCAC code logistics"
  - "LTL TL FTL freight terms"
  - "Bill of Lading definition logistics"
  - "INCOTERM explanation freight"
  - "3PL third party logistics definition"
  - "consignee shipper logistics terms"
  - "demurrage detention freight charges"
  - "freight consolidation terminology"
  - "OTM basic logistics glossary"
  - "Oracle OTM domain knowledge prerequisites"
  - "stopoff charge logistics definition"
description: "A quick-reference glossary of basic logistics terms — carrier, SCAC code, LTL, TL, Bill of Lading, INCOTERM, demurrage, and more — written for OTM developers and consultants without a freight background."
---

If you are new to logistics or coming from a purely technical background, here are the key terms you will encounter in OTM and day-to-day freight operations.

**Parties Involved in Freight:**

<div class="field-box"><strong>Carrier:</strong> A transportation service company that moves freight from one location to another. Carriers typically own or operate trucks, cargo planes, vessels, or rail cars. Each carrier is identified by a four-letter <strong>SCAC code</strong> (Standard Carrier Alpha Code) used on all shipping documents.</div>

<div class="field-box"><strong>Supplier / Seller:</strong> The party that receives a Purchase Order from your company (the Buyer), manufactures or sources the goods, and ships them to your warehouse.</div>

<div class="field-box"><strong>Consignee:</strong> The party receiving the freight at the destination.</div>

<div class="field-box"><strong>3PL (Third Party Logistics):</strong> A company to which the Buyer outsources transportation management. The Buyer sends a Purchase Order to the Supplier and a copy to the 3PL. The 3PL coordinates with the Supplier to collect goods, consolidates freight where possible, negotiates rates with carriers, and arranges shipment to the Buyer. After delivery, the 3PL invoices the Buyer for freight costs and pays the carriers.</div>

<div class="field-box"><strong>Freight Forwarder:</strong> A specialist that focuses on moving goods internationally — arranging transportation, handling customs clearance, and managing documentation. Unlike a 3PL, a freight forwarder typically does not handle warehousing or order fulfillment.</div>

**Shipment Types & Transport Modes:**

<div class="field-box"><strong>Inbound Shipping:</strong> Movement of goods from suppliers into company-maintained warehouses.</div>

<div class="field-box"><strong>Outbound Shipping:</strong> Movement of goods from company-maintained warehouses to customers or other warehouse locations.</div>

<div class="field-box"><strong>TL / FTL (Truck Load / Full Truck Load):</strong> The carrier dedicates an entire truck to a single customer's freight moving from one point to another. Charges are typically based on distance and equipment size.</div>

<div class="field-box"><strong>LTL (Less than Truck Load):</strong> The carrier allocates only part of a truck's space or weight capacity to each customer. Multiple customers share the truck. Charges are based on weight and volume.</div>

<div class="field-box"><strong>Parcel:</strong> A transport mode used for individual packages weighing less than 150 lb. Each package is tracked individually using a tracking number issued by the carrier. Examples: UPS and FedEx packages.</div>

<div class="field-box"><strong>Drayage:</strong> Short-distance freight movement — for example, moving a container from a port to a nearby truck pickup location. Drayage charges are typically paid in local currency.</div>

**Packaging & Equipment:**

<div class="field-box"><strong>SKU (Stock Keeping Unit):</strong> An individual item or product unit placed inside cartons for shipping.</div>

<div class="field-box"><strong>Carton:</strong> A cardboard box used to package individual items for shipping.</div>

<div class="field-box"><strong>Pallet / THU (Transportation Handling Unit):</strong> A flat wooden platform used to stack and move cartons within a warehouse. Pallets are also loaded directly into trucks. In OTM, these are referred to as THUs.</div>

<div class="field-box"><strong>Shipping Container:</strong> A large, reusable steel box that holds cartons and pallets during transport. Intermodal containers follow standard dimensions defined by ISO 6346, meaning the same sealed container can travel across multiple transport modes — ocean vessel, truck, and rail — without being opened.</div>

<div class="field-box"><strong>Reefer:</strong> A refrigerated container used for perishable goods such as food, beverages, and pharmaceuticals. Reefer equipment is classified by temperature range.</div>

**Ocean Freight Terms:**

<div class="field-box"><strong>FCL (Full Container Load):</strong> A single customer's freight fills an entire shipping container.</div>

<div class="field-box"><strong>LCL (Less than Container Load):</strong> Multiple customers share space in a single shipping container.</div>

<div class="field-box"><strong>TEU / FEU:</strong> Twenty-foot Equivalent Unit and Forty-foot Equivalent Unit — standard measures of container capacity. For example, a 3PL might request an ocean carrier to reserve 2,000 TEU of space on a vessel voyage.</div>

<div class="field-box"><strong>CY (Container Yard):</strong> A storage area at a port or warehouse where containers are staged before loading or after unloading.</div>

<div class="field-box"><strong>CFS (Container Freight Station):</strong> A facility where LCL cargo is consolidated into containers (at origin) or broken down (at destination).</div>

<div class="field-box"><strong>CY/CY:</strong> Container Yard to Container Yard move — used for FCL shipments where a single shipper's container moves intact from origin to destination.</div>

<div class="field-box"><strong>CFS/CFS:</strong> Container Freight Station to Container Freight Station — used for LCL shipments where freight is consolidated at origin and deconsolidated at destination.</div>

<div class="field-box"><strong>CY/CFS:</strong> FCL at origin, broken down at destination. Used for shipments going to multiple consignees (also referred to as FCL/LCL).</div>

<div class="field-box"><strong>CFS/CY:</strong> Multiple sellers consolidated at origin, single consignee at destination (also referred to as LCL/FCL).</div>

**Documents:**

<div class="field-box"><strong>Bill of Lading (BOL):</strong> A document issued by the carrier to the party handing over the goods for transport. It serves as a receipt confirming the carrier has accepted the freight and specifies the destination. The carrier is then responsible for delivering the goods to that location.</div>

<div class="field-box"><strong>INCOTERMS:</strong> Internationally recognized trade terms agreed between buyer and seller that define at which point in the journey the buyer takes on responsibility and risk for the goods. For example, <strong>FOB (Free on Board)</strong> means the buyer assumes responsibility once the seller has loaded the goods onto the vessel or truck arranged by the buyer.</div>

<div class="field-box"><strong>NMFC (National Motor Freight Classification):</strong> Classification codes assigned to freight items to standardize and estimate accurate freight costs across the trucking industry.</div>

<div class="field-box"><strong>FCR (Forwarder's Cargo Receipt):</strong> A document issued by a freight forwarder to the shipper upon receipt of cargo — also referred to as Forwarder's Certificate of Receipt.</div>

<div class="field-box"><strong>Pro Number:</strong> A progressive tracking number assigned by the carrier to TL and LTL shipments, similar to a UPS or FedEx tracking number.</div>

**Freight Charges:**

<div class="field-box"><strong>Fuel Surcharge:</strong> A variable fee added to shipment costs to offset fluctuating fuel prices. Typically calculated as a percentage of the base freight charge and updated periodically.</div>

<div class="field-box"><strong>Demurrage / Detention:</strong> Penalty charges levied by the carrier on the consignee for holding transportation equipment (containers, trailers) beyond the agreed free-time period at a carrier or port facility.</div>

<div class="field-box"><strong>Stopoff Charges:</strong> Charges levied by the carrier when the shipper requests the truck to stop and load or unload at locations between the origin and final destination — i.e., on a multi-stop shipment.</div>

**Warehouse & Yard Operations:**

<div class="field-box"><strong>Yard:</strong> A designated parking area at a warehouse or distribution center, organized into rows and slots, where trailers and containers are staged before being moved to a dock door for loading or unloading.</div>

<div class="field-box"><strong>Loading Dock:</strong> A door in the warehouse building that aligns with the rear of a truck so goods can be loaded or unloaded directly between the truck and the warehouse staging area.</div>

<div class="field-box"><strong>Diversion:</strong> Changing the destination of a shipment while it is already in transit. The shipper or 3PL notifies the carrier of the new destination before the freight reaches the original delivery point.</div>

<div class="note-box"><strong>Note:</strong> In OTM, you will encounter most of these terms in screen field names, rate configurations, shipment records, and integration documents. Familiarity with these terms will make it significantly easier to understand OTM's data model and configuration options.</div>

**What's Next:**

Now that you are familiar with core logistics terminology, the next topic covers how external systems send data into OTM using XML — the primary integration method for feeding orders, locations, and reference data into OTM from ERP and other source systems.

Next Topic: [Inbound Integrations (XML)](/posts/otm-inbound-integrations-xml/)
