---
title: "Status Types"
date: 2017-07-07T20:10:00+00:00
draft: false
weight: 420
tags:
  - "external status"
  - "Status type"
  - "internal status"
aliases:
  - "/2017/07/status-types.html"
---

In OTM, transactions objects like Order Release, Shipment, etc have 'Status' button on the header screen that will have values to give information about current status of that object in the transaction life cycle.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyZIuy1FIKevdXODmirYkeJjss-0wovLYjzR_D9RF4vtHOQPEk6Up7mHHhNOI6ht5-ZlMpJQrB5haqynxRvGIFCNvQDj8z0fH8wbM0-9a9GY1dyHmju3AjsMoZ9VLwe1Up135RFsVkoEs/s640/Capture0707_002.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgyZIuy1FIKevdXODmirYkeJjss-0wovLYjzR_D9RF4vtHOQPEk6Up7mHHhNOI6ht5-ZlMpJQrB5haqynxRvGIFCNvQDj8z0fH8wbM0-9a9GY1dyHmju3AjsMoZ9VLwe1Up135RFsVkoEs/s1600/Capture0707_002.JPG)

  
  
For example, if you want to track the tender status of a shipment, you can review shipment status 'SECURE RESOURCES' and it's values at each stage in the tender life cycle to track the progress. When shipment is originally created, it might have status like 'SECURE RESOURCES_NOT STARTED'. Once we tender it to carrier, this status changes to 'SECURE RESOURCES_TENDERED'. Once carrier accepts tender, status changes to 'SECURE RESOURCES_ACCEPTED' and so on. So these status values give good information to the user on what are next actions to be taken on that transaction.  
  
**Status values are of two types:** Internal statuses and External Statuses.  
  
Internal statuses like 'SECURE RESOURCES' on the Shipment are standard OTM application statuses. OTM product code maintains these statuses. Ideally we should avoid doing any custom SQL DML statements on such internal status type values to avoid conflicts with OTM standard code flow.  
  
However, if consultants want to add new status types, they can create external statuses based on their client specific requirements. To create external status, follow below steps:  
  

  * Configuration and Administration Data > Power Data > General > Status Types > New
  * Enter Status Type ID(Some qualifier/name and the same appears when you click 'Status' button)
  * Enter Object Type(E.g. 'Shipment' if you are creating external status on the 'Shipment' etc)
  * Enter Status Values(Naming convention you follow is Status Type ID value followed by underscore and status value). Add all possible values here and mark one of the values as 'Initial Value'. This will be default value when the transaction is created. You can update these values with SQL DML through Agents etc based on standard or custom events.