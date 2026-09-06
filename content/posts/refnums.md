---
title: "Refnums"
date: 2017-07-07T18:37:00+00:00
draft: false
weight: 410
tags:
  - "Qualifier"
  - "Updates Allowed"
  - "Refnum"
aliases:
  - "/2017/07/refnums.html"
keywords:
  - "Oracle OTM refnum configuration"
  - "OTM reference number qualifier setup"
  - "Oracle OTM shipment refnum qualifier"
  - "OTM refnum updates allowed options"
  - "Oracle OTM order release reference number"
  - "OTM custom attribute refnum qualifier"
  - "Oracle Transportation Management refnum setup"
  - "OTM refnum GlogXML inbound XML"
  - "Oracle OTM order base refnum"
  - "OTM refnum one update many options"
description: "Explains Oracle OTM Reference Numbers (Refnums), how to define qualifier IDs for storing custom values on shipments, orders, and other objects, and how to control update behavior and populate values via inbound XML."
---

OTM provides the flexibility to associate custom attributes — also called refnums — to every transaction object such as Order Base, Order Release, and Shipment. Developers can use these refnums to store client-specific values like source system information, custom dates, and other custom fields. Note that newer versions of OTM also have attribute (flex field) columns for the same purpose, which are covered in a separate post.

To create a refnum, navigate to the specific business object menu. For a Shipment refnum:

<div class="step-box">Shipment Management > Power Data > Qualifiers > Shipment Reference Number Qualifiers > New</div>

Enter the following values:

- <div class="field-box"><strong>Shipment Reference Number Qualifier:</strong> Give a name to the qualifier</div>
- <div class="field-box"><strong>Updates Allowed:</strong> Controls how inbound XML updates the refnum value. 'One, Update' replaces the existing value with the incoming value. 'One, Do not Update' preserves the existing value. 'Many' creates an additional refnum with the same qualifier when new values arrive via inbound XML.</div>

<div class="note-box"><strong>Note:</strong> When using the 'Many' option, the Qualifier ID and Value combination must be unique so that inbound XML transmissions do not fail.</div>

Once the refnum qualifier is defined, you can use it to enter data just like any other attribute — select the qualifier from the dropdown, enter a value, and save:

[![OTM refnum entry on shipment screen](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigJtwF0DrDi2XECmHsjLPTn8yEOkLlz2TnbO2LMcZ-yXOKHA57-Qko_TCVdodHYlDAqgXEmzuwRniVwv6lCo8qti8SyFfI29daOTBKi_LwHDHMbIhYijTYiDWrVvjpWniwlivnEnbtjfE/s640/Capture0707_001.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigJtwF0DrDi2XECmHsjLPTn8yEOkLlz2TnbO2LMcZ-yXOKHA57-Qko_TCVdodHYlDAqgXEmzuwRniVwv6lCo8qti8SyFfI29daOTBKi_LwHDHMbIhYijTYiDWrVvjpWniwlivnEnbtjfE/s1600/Capture0707_001.JPG)

You can also add refnum values in inbound XML. Refer to the OTM schema GlogXML.xsd for details.
