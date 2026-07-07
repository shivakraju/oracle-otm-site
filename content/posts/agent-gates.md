---
title: "Agent Gates"
date: 2026-02-15T17:29:00+00:00
draft: false
weight: 280
tags:
  - "Agent Gates"
  - "Status Function"
  - "Functor"
  - "Condition Additive"
aliases:
  - "/2026/02/agent-gates.html"
---

**Navigation:** Business Process Automation > Power Data > Event Management > Agent Gates

Agent Gates can be used to add custom conditions via saved query to control standard OTM events/worfklows. Agent Gates work at domain level.

Validation can be either used to extend standard validations or completely replace standard validations. If validation fails, standard workflow stops. 

For example, you can stop tender worklfow for specific transport modes using below configurations:

  * Object type: SHIPMENT
  * Status Function: WKFLW_TENDER
  * Functor Class: glog.server.workflow.shipment.ShipmentStatus$Tender
  * Saved Condition ID: Write SQL with your custom business rules
  * Check 'Saved Condition Additive'