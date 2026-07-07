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
---

OTM comes with a variety of screens for each business object like Shipment, Order Release, etc and some of them can be copied and customized to ensure that they show only data elements required for that particular user/role.  
  
For example, a user might want to query a shipment by some attribute(custom) element, want the results screen to show only few elements like Shipment ID, Carrier Name etc, want view only screen(layout) to display the information to avoid accidental data updates, etc. All these requirements can be configured from the OTM UI using Manager Layouts and Screen sets.  
  
Manager Layout is used to control the Layout of data elements, names(labels) for each data element, and source of the data elements.  
  
Screen set is used to control - Query/Finder elements, Results Screen elements, Actions, Smart links etc. Note that at screen set level we associate New/Edit/View mode manger layouts in the 'General' tab.  
  
**Creating custom layouts:**  

  1. Login as domain ADMIN
  2. Configuration and Administration > User configuration > Manager Layout
  3. Query the standard layout that you want to customize
  4. Select the Layout and click 'Copy Manager Layout' button
  5. Enter the ID,Name for the new layout and change the title(label) if required. 
  6. Click 'Detail' button.
  7. You will notice sections and data elements within a section. 
  8. If you select a section, you see options to move this section up/down, edit, delete or add a new element to the section.
  9. If you select a data element, you see options to edit/delete or replace this element with another one. 
  10. You can complete the modification to the layout using these options. If you are losing control over the position of elements, it is better to create your own custom section and start adding required elements.

**Creating custom screen sets:**  

  1. Login as domain ADMIN
  2. Configuration and Administration > User configuration > Screen Set Manager 
  3. Query the standard screen set that you want to copy and customize
  4. Select the screen set and click 'Copy Screen Set'
  5. Enter the ID for new screen set, change the label name if required.
  6. In the search tab you can Add/Remove fields that you want to use for the search criteria.
  7. In the default criteria tab you can add filter conditions to restrict the data being searched to a order type, business unit etc.
  8. In the results tab you can control what columns you want to display in the results screen that comes after your search function. Note that you can also add Refnum and Reference numbers to this results screen. Sequence number is used to control the order in which you want to display the columns.
  9. Actions and Smartlinks tab shows the actions/smart links that we can add/delete. We can discuss more regarding these two in another topic.
  10. General tab helps you to control/select the layout for the data display. Say if you want only a view-only data display - you create a view only manager layout, uncheck 'New', 'Edit','Delete' options in this General tab, and against 'View' option select your view only manager layout.
  11. Finish. This will create as custom screen set that you can use in your menu.

**Creating custom labels(names for fields):**  

  1. Login as DBA.ADMIN. You need this login for below navigation.
  2. Configuration and Administration > User configuration > Label Manager > New 
  3. In the screen you can enter the Label ID and required Text.