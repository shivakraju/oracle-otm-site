---
title: "Status Types"
date: 2017-07-07T20:10:00+00:00
draft: false
weight: 30
tags:
  - "external status"
  - "Status type"
  - "internal status"
aliases:
  - "/2017/07/status-types.html"
keywords:
  - "Oracle OTM status types configuration"
  - "OTM external status internal status"
  - "Oracle OTM custom status type setup"
  - "OTM shipment SECURE_RESOURCES status"
  - "Oracle OTM status type initial value"
  - "OTM order release status values"
  - "Oracle Transportation Management status configuration"
  - "OTM external status object type"
  - "Oracle OTM transaction lifecycle status"
  - "OTM custom status type agent SQL"
description: "Explains Oracle OTM Status Types, the difference between internal statuses (managed by OTM code) and external statuses (custom), and how to define new external status types with initial values for shipments and orders."
url: "/posts/status-types/"
---

In OTM, transaction objects like Order Release and Shipment have a 'Status' button on the header screen that shows values describing the current state of that object in the transaction lifecycle.

[![OTM Status button on shipment header screen](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyZIuy1FIKevdXODmirYkeJjss-0wovLYjzR_D9RF4vtHOQPEk6Up7mHHhNOI6ht5-ZlMpJQrB5haqynxRvGIFCNvQDj8z0fH8wbM0-9a9GY1dyHmju3AjsMoZ9VLwe1Up135RFsVkoEs/s640/Capture0707_002.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyZIuy1FIKevdXODmirYkeJjss-0wovLYjzR_D9RF4vtHOQPEk6Up7mHHhNOI6ht5-ZlMpJQrB5haqynxRvGIFCNvQDj8z0fH8wbM0-9a9GY1dyHmju3AjsMoZ9VLwe1Up135RFsVkoEs/s1600/Capture0707_002.JPG)

For example, if you want to track the tender status of a shipment, you can review shipment status 'SECURE RESOURCES' and its values at each stage in the tender lifecycle. When a shipment is originally created, it might have a status like 'SECURE RESOURCES_NOT STARTED'. Once tendered to a carrier, this status changes to 'SECURE RESOURCES_TENDERED'. Once the carrier accepts the tender, the status changes to 'SECURE RESOURCES_ACCEPTED', and so on. These status values give users clear information about what actions are required next.

**Status values are of two types: Internal Statuses and External Statuses.**

Internal statuses like 'SECURE RESOURCES' on the Shipment are standard OTM application statuses maintained by OTM product code. Custom SQL DML statements on such internal status type values should be avoided to prevent conflicts with the standard OTM code flow.

If you want to add new status types, you can create external statuses based on client-specific requirements. To create an external status, follow the steps below:

<div class="step-box">Configuration and Administration Data > Power Data > General > Status Types > New</div>

- <div class="field-box"><strong>Status Type ID:</strong> Enter a qualifier or name — this appears when you click the 'Status' button</div>
- <div class="field-box"><strong>Object Type:</strong> Enter the object this status applies to, for example 'Shipment'</div>
- <div class="field-box"><strong>Status Values:</strong> Use the naming convention of Status Type ID followed by an underscore and the status value. Add all possible values and mark one as 'Initial Value' — this will be the default when the transaction is created. You can update these values via SQL DML through Agents based on standard or custom events.</div>
