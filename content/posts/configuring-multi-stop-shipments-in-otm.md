---
title: "Configuring Multi-Stop Shipments in OTM"
date: 2026-09-03T00:00:00+00:00
draft: false
weight: 215
tags:
  - "Multi-Stop"
  - "Bulk Plan"
  - "Logic Configuration"
  - "Rate Offering"
  - "Distance Lookup"
  - "OTM"
---

In OTM, a **multi-stop shipment** is a single shipment that picks up or delivers freight at more than one location. For example, a truck may pick up goods from one warehouse and deliver them to multiple customer locations in sequence — all on the same shipment.

OTM's Bulk Plan algorithm can automatically consolidate multiple orders into a single multi-stop shipment to optimize transportation costs. To enable this, the following areas need to be configured.

**Logic Configuration (MULTISTOP):**

This is the main configuration that enables multi-stop behavior in the Bulk Plan algorithm.

Shipment Management > Power Data > General > Logic Configuration

Create a new Logic Configuration record with the below header fields:

> **Logic Configuration ID:** Enter a unique ID for this configuration (e.g. CUSTOM_MULTISTOP or any name that suits your business).
>
> **Logic Configuration Type:** Select **MULTISTOP** from the dropdown. This is the key field that tells OTM this is a multi-stop logic configuration.
>
> **Domain Name:** Select the domain applicable to your business.

Once the header is saved, update the below parameters in the GENERAL section:

> **MULTISTOP ALLOWED:** Set to TRUE to enable multi-stop shipments in Bulk Plan.
>
> **MULTISTOP CHECK TIME FEASIBILITY:** Controls whether OTM checks if stops are time-feasible before consolidating orders into a multi-stop shipment.
>
> **MULTISTOP MAX DISTANCE BETWEEN DELIVERIES:** Maximum road distance allowed between two consecutive delivery stops. Configure based on your business area coverage.
>
> **MULTISTOP MAX DISTANCE BETWEEN PICKUPS:** Maximum road distance allowed between two consecutive pickup stops. Configure based on your business area coverage.
>
> **MULTISTOP MAX RADIUS FOR DELIVERIES:** Maximum radius from a central point within which delivery stops can be consolidated. Configure based on your business area coverage.
>
> **MULTISTOP MAX RADIUS FOR PICKUPS:** Maximum radius from a central point within which pickup stops can be consolidated. Configure based on your business area coverage.
>
> **MULTISTOP RATE DISTANCE ID:** Distance calculation method used for multi-stop rating. Set this to the mileage engine configured in your OTM environment.
>
> **MAXIMUM DELIVERY STOPS ALLOWED:** Maximum number of delivery stops allowed on a single shipment. Configure based on your operational requirements.
>
> **MAXIMUM PICKUP STOPS ALLOWED:** Maximum number of pickup stops allowed on a single shipment. Configure based on your operational requirements.
>
> **MAXIMUM STOPS ALLOWED:** Total maximum stops (pickup + delivery) allowed on a single shipment.

**Bulk Plan Parameter Set Configuration:**

After updating the Logic Configuration, the MULTISTOP Config ID must be linked to the Bulk Plan Parameter Set so that the algorithm picks up the correct multi-stop settings during planning.

Shipment Management > Power Data > General > Parameter Sets

Open the Parameter Set used by your Bulk Plan and locate the **MULTISTOP** section. Update the below parameter:

> **MULTISTOP CONFIG ID:** Set this to the Logic Configuration ID updated in the previous step. This links the Bulk Plan to the multi-stop settings you configured.

The other parameters visible in this section can be left at their default values unless your business scenario requires specific adjustments:

> **CONSIDER CARRIER CAPACITIES DURING MULTISTOP:** Controls whether carrier capacity limits are checked when building multi-stop shipments. Default is FALSE.
>
> **FLEXIBLE ROUTE PROFILE ID:** Optional. Used to reference a flexible route profile if your business uses flexible routing.
>
> **MULTISTOP XDOCK INBOUND AFTER OUTBOUND COMPLETE:** Controls cross-dock sequencing for multi-stop. Default is FALSE.
>
> **USE MULTIPASS MULTISTOP:** Enables multiple passes of the multi-stop algorithm for better optimization. Default is FALSE.
>
> **USE PRIORITY IN COST SAVINGS:** Controls whether order priority is considered in cost savings calculations. Default is FALSE.
>
> **VOLUME PADDING FACTOR BETWEEN STOPS:** Additional volume buffer added between stops. Leave at default unless required.
>
> **WEIGHT PADDING FACTOR BETWEEN STOPS:** Additional weight buffer added between stops. Leave at default unless required.

**Note:** Some parameters may appear blank on an existing MULTISTOP Logic Configuration. If the multi-stop Bulk Plan algorithm is failing during testing, check that all parameters above have explicit values. Blank values can cause the algorithm to fail without a clear error.

**Itinerary Level Configuration:**

The Itinerary in OTM defines the route lanes and stop sequences used by the Bulk Plan algorithm when building shipments. For multi-stop shipments to work, configure the below two settings on the Itinerary.

Shipment Management > Power Data > Itinerary

> **Multi-Stop Itinerary (Header Level):** On the Itinerary header, check the **Multi-Stop Itinerary** checkbox. This tells OTM that this itinerary is eligible for multi-stop shipment building during Bulk Plan.
>
> **Auto Consolidation Type (Itinerary Leg Level):** On each itinerary leg, set the **Auto Consolidation Type** field to **MULTISTOP INTO ONE EQUIP**. This instructs OTM to consolidate multiple order releases into one equipment (single shipment) at the leg level during Bulk Plan execution.

**Rate Offering Level Configuration:**

The Rate Offering controls how OTM rates a shipment. For multi-stop shipments, stop count limits must be configured on the Rate Offering so OTM knows how many stops are permitted under a given rate.

Shipment Management > Rate Management > Rate Offering

On the Rate Offering, update the below stop count limits:

> **Minimum Stop Count:** Minimum number of stops for this rate to apply.
>
> **Maximum Stop Count:** Maximum number of stops allowed under this rate. Set this to cover the maximum number of stops your multi-stop shipments will have.

**Distance Lookup Configuration:**

Shipment Management > Power Data > Geography > Distance

For direct shipments, OTM only needs distance from the source location to the destination location. However, for multi-stop shipments, OTM also needs distances **between each stop** to correctly calculate the total route distance and shipment costs.

> Maintain distance records between all stop locations that may appear together on a multi-stop shipment — not just from origin to final destination.
>
> If you use an external mileage engine (such as PC*MILER, MileMaker, or RatewareXL), verify that it is configured to return distances between intermediate stops and not just the direct origin-to-destination distance.
>
> For LTL rates using an external rating engine, note that these engines typically only return direct origin-to-destination distances. For LTL multi-stop shipments, you may need to manually maintain inter-stop distance records in OTM.

**Note:** Missing distance records between stops is one of the most common reasons Bulk Plan fails to build multi-stop shipments. If Bulk Plan is not consolidating orders into multi-stop shipments as expected, verify that all inter-stop distances are populated.

**Testing:**

Once the above configurations are in place, run a Bulk Plan with order releases that have nearby delivery or pickup locations. Verify that Bulk Plan consolidates them into a single multi-stop shipment rather than separate direct shipments.
