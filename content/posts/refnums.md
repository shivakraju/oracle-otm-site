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
---

OTM gives flexibility to associate custom attributes(also called refnums) to every transaction object like Order Base, Order Release, Shipment, etc.  
  
Developers can use these refnums to store client specific custom values like source system information, custom dates, etc. Note that in newer versions of OTM, we also have attribute columns to save custom values. We discussed this in previous post 'Flexfields'.  
  
To create a refnum, you can navigate to specific business object menu. For example for shipment renfum, you can navigate to :  
Shipment Management > Power Data > Qaulifiers > Shipment Reference Number Qualifiers > Enter below values:  
  

  * Shipment Reference Number Qualifier: Give some name to the qualifier
  * Updates Allowed: This has three options. If you select 'One, Update' it means that your existing refnum value is updated with new value that is coming from inbound XML. If you select 'One, Do not Update' - it means your existing refnum value is not updated. If you select 'Many' - it means additional refnum with same qualifier is created when incoming XML comes with new value. 

**Note:** Qualifier ID and Value combination must be unique when you are having 'Many' option so that inbound XML transmission will not fail.  
  
Once Refnum is defined, you can use it to enter data just like any other attributes.  
Select refnum qualifier from dropdown, enter value and save it as shown.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigJtwF0DrDi2XECmHsjLPTn8yEOkLlz2TnbO2LMcZ-yXOKHA57-Qko_TCVdodHYlDAqgXEmzuwRniVwv6lCo8qti8SyFfI29daOTBKi_LwHDHMbIhYijTYiDWrVvjpWniwlivnEnbtjfE/s640/Capture0707_001.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigJtwF0DrDi2XECmHsjLPTn8yEOkLlz2TnbO2LMcZ-yXOKHA57-Qko_TCVdodHYlDAqgXEmzuwRniVwv6lCo8qti8SyFfI29daOTBKi_LwHDHMbIhYijTYiDWrVvjpWniwlivnEnbtjfE/s1600/Capture0707_001.JPG)

  
Also you can add this refnum values in the inbound XML. Refer to OTM schema GlogXML.xsd for details.