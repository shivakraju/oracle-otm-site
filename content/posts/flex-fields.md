---
title: "Flex fields"
date: 2017-04-06T22:10:00+00:00
draft: false
weight: 350
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
---

OTM provides attribute fields(Char, Number, Date and currency) on each table to store custom data. Note that we can also use refnum/remarks to store this custom data but those entries are made in separate tables. So new versions of OTM introduced these attribute columns on almost all major transaction data tables like ORDER_RELEASE, SHIPMENT etc.  
  
We can define flex fields on these attribute columns and add these fields to required manager layouts so that users can enter data directly into these fields from UI.  
  
If you are creating a manager layout on Order Release, and want to have Contact ID(not a standard column on Order Release) as a field to Order Release screen(layout) you can do following:  

  1. Login as domain ADMIN
  2. Goto Configuration and Administration > User Configuration > Flex Field Definition > New
  **3. Enter details as below:**![](/images/flex-fields-img1-091b9556e1.png) Field Type=FlexDropList and Query to pull contact IDs from CONTACT table as shown above. 
  4. Now when you add this field on the manager layout, it will display this list of values as shown: ![](/images/flex-fields-img2-e203f479b6.png)

You can also have Picklist to associate flex field to standard fields like country code as shown below:  
  
![](/images/flex-fields-img3-12700a279f.png)  
  
Note Field Type=PickList and Query Table ID=SERVPROV as shown above.