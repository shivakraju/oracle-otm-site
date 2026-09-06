---
title: "Advanced Layouts"
date: 2017-04-06T21:09:00+00:00
draft: false
weight: 80
tags:
  - "Advanced Layout"
  - "Panel splitter"
aliases:
  - "/2017/04/advanced-layouts.html"
keywords:
  - "Oracle OTM advanced layout configuration"
  - "OTM panel splitter layout setup"
  - "Oracle OTM multi-object screen layout"
  - "OTM advanced layout saved query"
  - "Oracle OTM parent child panel layout"
  - "OTM advanced layout shipment order release"
  - "Oracle Transportation Management advanced screen"
  - "OTM advanced layout table panel"
  - "Oracle OTM complex query layout"
  - "OTM split panel screen configuration"
description: "Explains how to create Oracle OTM Advanced Layouts with panel splitters to display multiple related business objects on the same screen, linked by parent-child relationships and populated via saved queries."
url: "/posts/advanced-layouts/"
---

Advanced Layouts allow you to build screens that display multiple related business objects side by side. For example, you can show shipments matching a complex saved query in one panel, and the corresponding order releases for a selected shipment in an adjacent panel â€” all on the same screen.

This is useful when the default query criteria on standard screens is not flexible enough, or when planners need a combined view of parent and child records without navigating between separate screens.

**Steps to create a simple Advanced Layout:**

1. Log in as Domain ADMIN.

2. Navigate to:
<div class="step-box">Configuration and Administration > User Configuration > Advanced Layout > New</div>

3. Give the layout an ID (name).

4. Right-click on the **Layout** text to see options â€” **Add Panel Splitter** and **Add Table**.

5. Click **Add Table** to add a simple table panel.

6. Select the table under Layout. The table properties appear on the right side.

7. In the properties, set the **Screen Set ID** (how to display the data) and the **Population Method** (such as Saved Query â€” which controls what data is loaded when the layout is launched).

8. Click **Finish**. Attach this layout to your menu as a link.

9. When the menu link is clicked, the saved query executes and results are displayed in the advanced layout.
