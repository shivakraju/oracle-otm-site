---
title: "Rate Distance"
date: 2026-09-20T00:00:00+00:00
draft: false
weight: 62
url: "/posts/rate-distance/"
tags:
  - "OTM"
  - "Rate Distance"
  - "PCMiler"
  - "Distance Lookup"
keywords:
  - "Oracle OTM Rate Distance configuration"
  - "OTM distance lookup configuration"
  - "Oracle OTM PCMiler integration"
  - "OTM external distance engine"
  - "Oracle OTM LOOKUP ONLY rate distance"
  - "OTM PCMiler web service configuration"
  - "Oracle Transportation Management distance calculation"
  - "OTM lane distance miles configuration"
  - "Oracle OTM ALK PCMiler setup"
  - "OTM rate distance geo hierarchy"
description: "How OTM calculates distances between locations — using either manually pre-configured Distance Lookups or an external engine like PCMiler. Covers setup for both approaches including geo hierarchy, parameters, and the PCMiler API key property."
---

Rate Distance in OTM is the calculated distance between a shipment's origin and destination. OTM needs this distance to cost TL shipments on per-mile rate contracts. There are two ways to provide this distance:

- **Distance Lookup** — your team pre-loads a table of distances lane by lane. OTM looks up the matching lane and reads the stored mileage. No external system is needed.
- **External Distance Engine** — OTM calls a third-party routing engine (such as PCMiler from ALK Technologies) at plan time to fetch the live calculated distance. This requires a license and API access to the external system.

The Rate Distance record is linked to the **Rate Offering** (carrier contract) — whichever approach you configure, you reference it in that field so OTM knows which distance method to use when costing shipments under that contract.

---

**Rate Distance Using Distance Lookups**

With the lookup approach, your business team manually creates records for each lane they want to cover, assigning a fixed mileage to each origin-destination pair. OTM uses Oracle's built-in **LOOKUP ONLY** Rate Distance ID — no external system or configuration is needed beyond loading the data.

**Step 1 — Create the Rate Distance record**

<div class="step-box">Rates > Contract Rate Management > Rate Distance > New</div>

<div class="field-box"><strong>Rate Distance ID / XID:</strong> A unique identifier for this rate distance record, e.g. <code>YOUR_DOMAIN.LOOKUP_ONLY</code>. Oracle provides a built-in record — use <code>PUBLIC.LOOKUP ONLY</code> if you do not need a custom one.</div>

<div class="field-box"><strong>Distance Type:</strong> Set to <code>LOOKUP</code>. This tells OTM to use the pre-loaded distance table rather than calling an external engine.</div>

<div class="field-box"><strong>Domain Name:</strong> Your OTM domain</div>

Save the record.

**Step 2 — Create Distance Lookup records (Lane Definitions)**

Each Distance Lookup record defines the mileage for one lane. Open the rate distance record you just created and navigate to the **Distance Lookup** section, or go to:

<div class="step-box">Rates > Contract Rate Management > Distance Lookup > New</div>

<div class="field-box"><strong>Rate Distance GID:</strong> The rate distance record you created in Step 1</div>

<div class="field-box"><strong>Source Geo Hierarchy / Destination Geo Hierarchy:</strong> The geographic level used to identify the origin and destination. OTM supports multiple options — choose based on how you want to define your lanes.</div>

Common geo hierarchy options:

- **CITY** — city + state + country (e.g. Dallas, TX, USA)
- **USZIP5** — 5-digit US zip code
- **USZIP3** — 3-digit zip prefix (covers a broader area)
- **LOCATION** — a specific OTM Location record
- **STATE/PROVINCE** — state-level matching

<div class="field-box"><strong>Source / Destination values:</strong> Enter the matching values for the selected geo hierarchy (e.g. city name + state, or zip code)</div>

<div class="field-box"><strong>Distance / UOM:</strong> The fixed mileage for this lane, e.g. <code>920</code> with UOM <code>MI</code></div>

Add one record per lane. OTM matches an incoming shipment's origin and destination against these records at plan time and reads the stored mileage.

**Step 3 — Link to Rate Offering**

In your Rate Offering (carrier contract) record, set the **Rate Distance GID** field to the Rate Distance ID you created above. OTM will then use the lookup table when costing shipments under that contract.

<div class="note-box"><strong>Note:</strong> If you use Oracle's built-in <code>PUBLIC.LOOKUP ONLY</code> rate distance, you can reference it directly in the Rate Offering without creating a custom Rate Distance record. Custom records are useful when you need different distance tables for different contracts.</div>

---

**Rate Distance Using External Distance Engine (PCMiler)**

PCMiler (from ALK Technologies) is a widely used routing engine that calculates distances based on road networks, route type, and address or postal code inputs. OTM integrates with PCMiler via a web service call at plan time.

This setup requires a PCMiler license and an API Authorization Key from ALK.

**Step 1 — Create the External Distance Engine record**

<div class="step-box">Rates > Contract Rate Management > External Distance Engine > New</div>

<div class="field-box"><strong>External Distance Engine ID / Description:</strong> A unique ID for this engine record, e.g. <code>YOUR_DOMAIN.PCMILER_WS</code>. Description can be something like <code>DISTANCE BASED ON POSTAL CODES USING PCMILER/PRACTICAL - WS</code></div>

<div class="field-box"><strong>External Engine Type:</strong> Select <code>ALK</code></div>

<div class="field-box"><strong>Connection Type:</strong> Select <code>Java Class</code></div>

<div class="field-box"><strong>Java Class:</strong> Enter exactly: <code>glog.business.rate.ratedistance.external.PCMilerEngineWS</code></div>

<div class="field-box"><strong>Cache Control Type:</strong> Set to <code>Cache by XLane Don't Lookup - Don't Save</code>. This prevents OTM from attempting to save results to a lookup table, which avoids errors when the distance cache tables are not in use.</div>

<div class="field-box"><strong>Domain Name:</strong> Your OTM domain</div>

**Parameters** — the following rows are a sample configuration commonly used with PCMiler. OTM provides several additional parameters and the right combination depends on your business requirements and how your locations are set up.

| Parameter | Value | Country Code |
|-----------|-------|--------------|
| BACKUP_WITH_LAT_LON | N | * |
| DEST_ADDRESS_TYPE | POSTAL_CODE | * |
| ROUTE_TYPE | P | * |
| SAME_SOURCE_DEST_DIST | 5 MI | * |
| SOURCE_ADDRESS_TYPE | POSTAL_CODE | * |

<div class="field-box"><strong>BACKUP_WITH_LAT_LON:</strong> <code>N</code> — do not fall back to lat/lon coordinates if the postal code lookup fails</div>

<div class="field-box"><strong>DEST_ADDRESS_TYPE / SOURCE_ADDRESS_TYPE:</strong> <code>POSTAL_CODE</code> — OTM passes the shipment's origin and destination postal codes to PCMiler for routing</div>

<div class="field-box"><strong>ROUTE_TYPE:</strong> <code>P</code> — Practical route (fastest practical driving path). Other options include <code>S</code> (Shortest) and <code>T</code> (Toll-discouraged).</div>

<div class="field-box"><strong>SAME_SOURCE_DEST_DIST:</strong> <code>5 MI</code> — the distance OTM assigns when origin and destination postal codes are identical, avoiding a zero-distance result</div>

**Geo Hierarchy** — add the following rows to tell OTM which address level to use when passing location data to PCMiler:

| Geo Hierarchy ID | Country Code |
|-----------------|--------------|
| POSTAL_CODE | * |
| USZIP5 | USA |

Save the record.

**Step 2 — Set up the PCMiler API Authorization Key**

PCMiler requires an API key for authentication. In OTM, this is stored as a system property rather than directly on the External Distance Engine record.

<div class="step-box">Configuration > System Administration > Property Sets</div>

Locate or create the property:

<div class="field-box"><strong>Property Name:</strong> <code>glog.ExternalDistanceEnginePCMilerWS.AuthorizationKey</code></div>

<div class="field-box"><strong>Value:</strong> The API Authorization Key provided by ALK Technologies when you purchased the PCMiler license</div>

OTM passes this key with every web service call to PCMiler. Keep this value secure — anyone with access to this property set can use the API license.

**Step 3 — Create the Rate Distance record linking to the External Engine**

<div class="step-box">Rates > Contract Rate Management > Rate Distance > New</div>

<div class="field-box"><strong>Rate Distance ID:</strong> A unique ID, e.g. <code>YOUR_DOMAIN.PCMILER</code></div>

<div class="field-box"><strong>Distance Type:</strong> Set to <code>EXTERNAL</code></div>

<div class="field-box"><strong>External Distance Engine GID:</strong> The External Distance Engine record you created in Step 1</div>

<div class="field-box"><strong>Domain Name:</strong> Your OTM domain</div>

**Step 4 — Link to Rate Offering**

In your Rate Offering (carrier contract) record, set the **Rate Distance GID** field to the Rate Distance ID you created in Step 3. OTM will now call PCMiler at plan time to calculate the distance for each shipment costed under that contract.

<div class="note-box"><strong>Note:</strong> PCMiler calculates distance based on postal codes by default with the configuration above. If your shipments frequently involve locations with no postal code (e.g. rural addresses or private sidings), consider enabling <code>BACKUP_WITH_LAT_LON = Y</code> and ensuring your OTM Location records have latitude/longitude coordinates populated.</div>
