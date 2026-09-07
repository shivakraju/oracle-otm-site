---
title: "REST API"
date: 2026-09-07T00:00:00+00:00
draft: false
weight: 50
url: "/posts/otm-rest-api/"
tags:
  - "OTM"
  - "REST API"
  - "Integration"
keywords:
  - "Oracle OTM REST API"
  - "OTM REST API GET POST PATCH DELETE"
  - "OTM logisticsRestApi"
  - "Oracle Transportation Management REST API"
  - "OTM integration user REST ACL"
  - "OTM saved query REST API"
  - "OTM REST API location"
  - "OTM REST API shipment"
  - "OTM REST API refnum delete"
  - "OTM custom-actions queries REST"
description: "Practical guide to OTM's REST API covering GET, POST, PATCH, and DELETE methods using Location as the example entity, plus running OTM Saved Queries over REST."
---

OTM exposes a REST API that lets external systems read and write OTM data without using XML transmissions. All four standard HTTP methods are supported — GET, POST, PATCH, and DELETE — and the same API can run OTM Saved Queries, which lets you pass parameters into complex SQL-backed searches.

**Setup — Create an Integration User**

Before making any API call, create a dedicated user in OTM and attach a role that includes the REST ACLs for the objects you need.

<div class="step-box">Business Process Automation > User Management > User</div>

<div class="field-box"><strong>Username:</strong> {DOMAIN}.INTEGRATION</div>

Attach a user role that has REST API ACLs enabled for the required entities (Locations, Shipments, Order Releases, etc.). OTM ships a default role called **INTEGRATION** that already has these ACLs configured — you can assign that role directly or create a custom role with only the ACLs your use case needs.

The username is free text and does not have to be "INTEGRATION" — use any name that makes the account's purpose clear in your environment.

<div class="note-box"><strong>Note:</strong> Use <code>resources-int</code> in the URL path (not <code>resources</code>) to bypass SSO and authenticate with Basic Auth directly.</div>

**Base URL Pattern**

Every OTM REST API call follows this structure:

```
https://{your-otm-host}/logisticsRestApi/resources-int/v2/{entity}
```

Replace `{your-otm-host}` with your OTM instance hostname. Replace `{entity}` with the object collection name — for example `locations`, `shipments`, `orderBases`.

In Postman or any REST client set the authorization to **Basic Auth** and use the integration user credentials. OTM SaaS versions also support **OAuth 2.0** — authentication is handled through the Oracle IDCS (Identity Cloud Service) layer. For Basic Auth, use the `resources-int` path as noted above. For OAuth 2.0, use the standard `resources` path and pass the bearer token obtained from IDCS.

---

**GET — Read a Record**

The examples below use **Location** as the entity, but the same URL patterns and parameters work for any OTM resource — Shipments, Order Bases, Order Releases, and others. See the [Common Entity URLs](#common-entity-urls) section at the bottom of this page for a quick reference list.

Fetch a specific location by its GID:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/{DOMAIN}.{LOCATION_XID}
```

OTM returns the full location JSON including address, timestamps, and links to child collections (refnums, contacts, documents, etc.).

**Limit returned fields**

Use the `fields` parameter to retrieve only the columns you need:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/{DOMAIN}.{LOCATION_XID}?fields=locationXid,countryCode3Gid,isTemplate
```

**Filter a collection with a query**

Use the `q` parameter to filter results. The syntax is `fieldName eq "value"`:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/?q=countryCode3Gid eq "CHN"
```

Combine `q` and `fields` to filter and shape the response in one call:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/?q=countryCode3Gid eq "CHN"&fields=locationXid,countryCode3Gid
```

Use `in` for multi-value filters on child collections:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/orderBases/{DOMAIN}.{ORDER_BASE_XID}/lines?q=destLocationGid eq "{DOMAIN}.{LOCATION_XID}" and packagedItemGid in ["{DOMAIN}.ITEM1", "{DOMAIN}.ITEM2"]&fields=orderBaseGid,obLineGid,destLocationGid,packagedItemGid
```

<div class="note-box"><strong>Note:</strong> Refer to Oracle's "Manage Collections" documentation for the full query syntax and supported operators.</div>

---

**POST — Create a Record**

Create a new location:

```
POST https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations
```

Set the request body to raw JSON:

```json
{
  "locationXid": "TEST_LOCATION_001",
  "locationName": "Test Location",
  "countryCode3Gid": "USA",
  "timeZoneGid": "America/Denver",
  "domainName": "{DOMAIN}",
  "isActive": true,
  "isTemporary": false,
  "isTemplate": false,
  "isLtlSplitable": true
}
```

OTM returns `201 Created` with the new location's full JSON.

**Add refnums to a record**

POST to the child `refnums` collection using the GID of the parent record in the URL:

```
POST https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/{DOMAIN}.TEST_LOCATION_001/refnums
```

```json
{
  "items": [
    {
      "locationRefnumQualGid": "{DOMAIN}.{REFNUM_QUALIFIER_1}",
      "locationRefnumValue": "VALUE1",
      "domainName": "{DOMAIN}"
    },
    {
      "locationRefnumQualGid": "{DOMAIN}.{REFNUM_QUALIFIER_2}",
      "locationRefnumValue": "VALUE2",
      "domainName": "{DOMAIN}"
    }
  ]
}
```

<div class="note-box"><strong>Note:</strong> By default the POST does not create an OTM Transmission record. To force transmission creation, add the appropriate synchronous request header — refer to Oracle documentation for the header name and value.</div>

---

**PATCH — Update a Record**

Update specific fields on an existing record. Include only the fields you want to change — other fields are left as-is:

```
PATCH https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/{DOMAIN}.{LOCATION_XID}
```

```json
{
  "locationName": "Updated Location Name"
}
```

OTM returns `204 No Content` on success.

---

**DELETE — Delete a Record**

Delete a location:

```
DELETE https://{your-otm-host}/logisticsRestApi/resources-int/v2/locations/{DOMAIN}.{LOCATION_XID}
```

No request body required.

**Delete a specific refnum**

Deleting a refnum is a three-step process.

**Step 1 — Find the refnum** using a GET with a query filter:

```
GET https://{your-otm-host}/logisticsRestApi/resources-int/v2/shipments/{DOMAIN}.{SHIPMENT_XID}/refnums?q=shipmentRefnumQualGid eq "{DOMAIN}.{REFNUM_QUALIFIER}"
```

**Step 2 — Check the response.** If `shipmentRefnumValue` is present in the JSON, the refnum exists. If the field is absent, no refnum exists and no delete is needed.

**Step 3 — Delete** using `RefnumQualifier x RefnumValue` as the composite key in the URL:

```
DELETE https://{your-otm-host}/logisticsRestApi/resources-int/v2/shipments/{DOMAIN}.{SHIPMENT_XID}/refnums/{DOMAIN}.{REFNUM_QUALIFIER}x{REFNUM_VALUE}
```

OTM returns `200 OK` on success.

<div class="note-box"><strong>Note:</strong> The <code>x</code> between qualifier and value in the URL is a literal character — it is OTM's separator for composite refnum keys.</div>

---

**Saved Query via REST**

OTM Saved Queries can be executed over REST. This is useful when you need SQL-level filtering that the standard `q` parameter cannot express — for example, joining across multiple tables or applying complex business logic.

<div class="note-box"><strong>Requirement:</strong> The Saved Query SQL must return the primary key GID of the object being queried. The REST API uses this to fetch the matching records.</div>

```
POST https://{your-otm-host}/logisticsRestApi/resources-int/v2/custom-actions/queries/{entity}?showParentPks=true&showPks=true&totalResults=true&offset=0&limit=50
```

Replace `{entity}` with the OTM object collection name — for example `shipments`, `orderBases`, `trackingEvents`.

**Payload:**

```json
{
  "copiedFrom": "{DOMAIN}.{SAVED_QUERY_NAME}",
  "parameterValues": {
    "0": "PARAM_VALUE_1",
    "1": "PARAM_VALUE_2"
  }
}
```

<div class="field-box"><strong>copiedFrom:</strong> GID of the Saved Query defined in OTM</div>
<div class="field-box"><strong>parameterValues:</strong> Matches the <code>?</code> placeholder positions in the query SQL (0-indexed)</div>

**Example — find shipments by tracking number**

OTM Saved Query SQL:

```sql
SELECT shipment_gid
FROM shipment_refnum
WHERE shipment_refnum_qual_gid = '{DOMAIN}.TRACKING_NUMBER'
AND shipment_refnum_value = ?
```

REST call:

```
POST https://{your-otm-host}/logisticsRestApi/resources-int/v2/custom-actions/queries/shipments?showParentPks=true&showPks=true&totalResults=true&fields=shipmentXid
```

```json
{
  "copiedFrom": "{DOMAIN}.{YOUR_SAVED_QUERY}",
  "parameterValues": {
    "0": "TRACKING_NUMBER_VALUE"
  }
}
```

<div class="note-box"><strong>Important:</strong> The column alias in your SQL must exactly match the entity's primary key field name, and the value returned must be the full GID of that entity. For shipments the alias must be <code>SHIPMENT_GID</code> and the value must include the domain prefix (e.g. <code>DOMAIN.SHIPMENT123</code>). For tracking events the alias must be <code>I_TRANSACTION_NO</code>. A wrong alias or a value without the domain prefix returns empty results with no error.</div>

---

**Common Entity URLs**

- **Locations** — `.../v2/locations`
- **Shipments** — `.../v2/shipments`
- **Order Bases** — `.../v2/orderBases`
- **Order Releases** — `.../v2/orderReleases`
- **Tracking Events** — `.../v2/trackingEvents`
- **Location refnums** — `.../v2/locations/{DOMAIN}.{XID}/refnums`
- **Shipment refnums** — `.../v2/shipments/{DOMAIN}.{XID}/refnums`
