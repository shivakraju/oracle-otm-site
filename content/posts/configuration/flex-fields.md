---
title: "Flex fields"
date: 2017-04-06T22:10:00+00:00
draft: false
weight: 20
tags:
  - "PickList"
  - "FlexDropList"
  - "Flex fields"
aliases:
  - "/2017/04/flex-fields.html"
keywords:
  - "Oracle OTM flex field configuration"
  - "OTM FlexDropList PickList flex field"
  - "Oracle OTM custom attribute columns"
  - "OTM flex field definition manager layout"
  - "Oracle OTM order release custom field"
  - "OTM flex field query list of values"
  - "Oracle Transportation Management attribute fields"
  - "OTM flex field CONTACT table query"
  - "Oracle OTM custom data fields setup"
  - "OTM flex field char number date currency"
description: "Explains Oracle OTM Flex Fields, how to define FlexDropList and PickList field types on attribute columns, and how to add them to Manager Layouts so users can enter custom data from the UI."
url: "/posts/flex-fields/"
---

OTM provides attribute columns (Char, Number, Date, and Currency) on most major transaction tables such as ORDER_RELEASE and SHIPMENT to store custom data alongside standard fields. Flex Fields are definitions applied to these attribute columns that control how the field behaves in the UI â€” including whether it shows a free-text entry, a query-driven dropdown, or a standard lookup list. Once defined, a Flex Field can be added to a Manager Layout so that users can enter data directly from the screen.

**Example â€” add a Contact ID field to the Order Release layout:**

The Contact ID is not a standard column on the Order Release table. Using a FlexDropList Flex Field, you can expose it as a dropdown populated from the CONTACT table.

**Step 1 â€” Create the Flex Field definition:**

<div class="step-box">Configuration and Administration > User Configuration > Flex Field Definition > New</div>

Log in as domain ADMIN and create a new Flex Field Definition. Set the following:

<div class="field-box"><strong>Field Type:</strong> FlexDropList â€” presents the user with a dropdown list populated by the query you specify below.</div>

<div class="field-box"><strong>Query:</strong> Enter a SQL query that returns the list of values. For example, to pull Contact IDs from the CONTACT table, query the CONTACT_XID column from CONTACT.</div>

![OTM Flex Field Definition screen showing FlexDropList field type and CONTACT table query](/images/flex-fields-img1-091b9556e1.png)

**Step 2 â€” Add the Flex Field to a Manager Layout:**

After saving the Flex Field Definition, add the field to your Manager Layout for Order Release. When users open the Order Release screen, the field will display as a dropdown populated with values from the CONTACT table.

![OTM Order Release screen showing the Contact ID flex field dropdown](/images/flex-fields-img2-e203f479b6.png)

**PickList Flex Fields:**

A PickList Flex Field associates the attribute column with a standard OTM reference table rather than a custom query. For example, to expose a country code selector on a layout, set Field Type to PickList and select SERVPROV as the Query Table ID.

![OTM Flex Field Definition screen showing PickList field type with SERVPROV query table](/images/flex-fields-img3-12700a279f.png)
