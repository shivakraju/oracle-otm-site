---
title: "Agent Gates"
date: 2026-02-15T17:29:00+00:00
draft: false
weight: 40
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
description: "Covers Oracle OTM Agent Gates, which allow consultants to add saved-query conditions to standard OTM events and workflows â€” such as blocking the tender workflow for specific transport modes â€” at the domain level."
url: "/posts/agent-gates/"
---

Agent Gates allow you to add custom saved-query conditions to standard OTM events and workflows. They operate at the domain level and can either extend or completely replace standard OTM validations. If the gate condition fails, the standard workflow is stopped.

<div class="step-box">Business Process Automation > Power Data > Event Management > Agent Gates</div>

For example, to stop the tender workflow for specific transport modes, configure an Agent Gate with the following values:

- **Object Type:** SHIPMENT
- **Status Function:** WKFLW_TENDER
- **Functor Class:** `glog.server.workflow.shipment.ShipmentStatus$Tender`
- **Saved Condition ID:** Write a SQL condition with your custom business rules
- **Saved Condition Additive:** Check this box
