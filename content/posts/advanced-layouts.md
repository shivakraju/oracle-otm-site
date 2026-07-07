---
title: "Advanced Layouts"
date: 2017-04-06T21:09:00+00:00
draft: false
weight: 360
tags:
  - "Advanced Layout"
  - "Panel splitter"
aliases:
  - "/2017/04/advanced-layouts.html"
---

There can be requirements like show shipments based on some complex query criteria(which cannot be written using simple default query criteria provided in screen sets) and also show related order releases for selected shipment in same screen, etc.  

  

In such requirements we can use advanced layout which gives option to split the screen into panels and each panel can be associated to different business objects(like Order Release, Shipment, etc). We can have parent, child relationship between panel data(like shipment to order release). We can also associate saved query(SQL) to display results while launching the screen using these advanced layouts.

  

Below are the steps to create a simple advanced layout:

  1. Login as Domain ADMIN
  2. Configuration and Administration > User Configuration > Advanced Layout > New
  3. Give ID(name) to the layout
  4. Right click on the 'Layout' text to see options - 'Add Panel Splitter' and 'Add Table'
  5. Click 'Add Table' if you want to add a simple table
  6. After table is added, if you select the table(Under Layout), you can see table properties on the right side.
  7. In these properties - select screen set ID(how to display data), population method(like Saved Query, etc which tells what data to be displayed)
  8. Finish. Attach this layout to your menu as link.
  9. Once you click this link, saved query is executed and data is shown in the advanced layout.