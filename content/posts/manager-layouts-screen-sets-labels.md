---
title: "Manager Layouts, Screen Sets, Labels"
date: 2017-04-06T21:05:00+00:00
draft: false
weight: 340
tags:
  - "Manager Layouts"
  - "Labels"
  - "Screen sets"
aliases:
  - "/2017/04/manager-layouts-screen-sets-labels.html"
keywords:
  - "Oracle OTM manager layout configuration"
  - "OTM screen set custom layout"
  - "Oracle OTM custom screen set creation"
  - "OTM manager layout data elements sections"
  - "Oracle OTM label manager configuration"
  - "OTM screen set finder results actions"
  - "Oracle Transportation Management UI customization"
  - "OTM copy manager layout steps"
  - "Oracle OTM view edit query layout"
  - "OTM screen customization user role"
description: "Covers how to create and customize Manager Layouts and Screen Sets in Oracle OTM to control which data elements appear in query, results, and edit screens for specific users or roles."
---

OTM ships with a variety of screens for each business object — Shipment, Order Release, and others — and most of these screens can be copied and customized to show only the data elements relevant to a particular user or role. For example, a user may need to query a shipment by a custom attribute, see only selected columns in the results, and open a view-only layout to prevent accidental edits. All of this can be configured from the OTM UI using Manager Layouts and Screen Sets.

A **Manager Layout** controls the arrangement of data elements on a screen — which fields appear, what labels they carry, and where the data comes from.

A **Screen Set** controls the broader screen behaviour — the query/finder fields, the results columns, available Actions and Smart Links, and which Manager Layouts are used for New, Edit, and View modes.

**Creating custom layouts:**

<div class="step-box">Configuration and Administration > User Configuration > Manager Layout</div>

1. Log in as domain ADMIN.
2. Query the standard layout you want to customize.
3. Select the layout and click **Copy Manager Layout**.
4. Enter the ID and Name for the new layout and change the title (label) if required.
5. Click **Detail**.
6. You will see sections and data elements within each section.
7. Selecting a section shows options to move it up or down, edit it, delete it, or add a new element to it.
8. Selecting a data element shows options to edit, delete, or replace it with another element.
9. Complete your modifications using these options. If managing element positions becomes difficult, create a new custom section and add the required elements there directly.

**Creating custom screen sets:**

<div class="step-box">Configuration and Administration > User Configuration > Screen Set Manager</div>

1. Log in as domain ADMIN.
2. Query the standard screen set you want to copy and customize.
3. Select the screen set and click **Copy Screen Set**.
4. Enter the ID for the new screen set and change the label name if required.
5. In the **Search** tab, add or remove fields used as search criteria.
6. In the **Default Criteria** tab, add filter conditions to restrict the data being searched — for example, by order type or business unit.
7. In the **Results** tab, control which columns appear in the results screen after a search. Reference numbers and Refnum fields can also be added here. The Sequence Number controls the column display order.
8. The **Actions** and **Smart Links** tabs show the actions and smart links that can be added or removed. These are covered in the Custom Actions topic.
9. In the **General** tab, select the Manager Layout for each mode — New, Edit, View, and Delete. To create a view-only layout, create a view-only Manager Layout, uncheck New, Edit, and Delete in this tab, and assign your view-only layout against the View option.
10. Click **Finish** to create the custom screen set. It can then be assigned to a menu item for your users.

**Creating custom labels (field names):**

<div class="step-box">Configuration and Administration > User Configuration > Label Manager > New</div>

Log in as DBA.ADMIN (required for this navigation). Enter the Label ID and the display text for the label.
