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
keywords:
  - "Oracle OTM agent gates configuration"
  - "OTM agent gate status function"
  - "Oracle OTM agent gate saved condition"
  - "OTM WKFLW_TENDER agent gate"
  - "Oracle OTM custom workflow validation"
  - "OTM agent gate condition additive"
  - "Oracle OTM shipment tender gate"
  - "OTM functor class agent gate"
  - "Oracle Transportation Management workflow gate"
  - "OTM domain level agent gate control"
description: "Covers Oracle OTM Agent Gates, which allow consultants to add saved-query conditions to standard OTM events and workflows — such as blocking the tender workflow for specific transport modes — at the domain level."
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