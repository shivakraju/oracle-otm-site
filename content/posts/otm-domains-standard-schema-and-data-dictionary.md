---
title: "OTM Domains, Standard Schema and Data Dictionary"
date: 2016-05-02T16:34:00+00:00
draft: false
weight: 100
tags:
  - "DATA_DICT"
  - "XID"
  - "GID"
  - "domain"
  - "Schema"
  - "OTM"
  - "REPORTOWNER"
  - "GLOGOWNER"
aliases:
  - "/2016/05/otm-data-structure.html"
---

**Domains:**   
  
OTM Data is organized into domains. Each domain is like grouping of data / business transactions based on the different business units with in the same organization.  
  
If there is a corporation with logistics requirements across various business units like "Merchandise Shipping", "Food and Beverages", etc - you typically create one domain for each of these business units so that users and their roles can be tied to each business unit. User/role tied to a particular domain can only access data for their specific domain/business unit. Also advantage with domains is that customization specific to a business unit can be better controlled/maintained. For example, OTM Agents(workflows) with custom code can be developed specific to each domain so they they trigger only for transactions within that domain.  
  
Domains can be created in hierarchical manner - like one parent domain at corporation level and child domains at business unit level under the same parent domain. With this structure you can maintain customization/features common to both the child domains at parent domain level. For example, you may define Item Numbers at parent domain level these items can be used on both the child domain transactions.  
  
Each table in OTM will have DOMAIN_NAME as column to distinguish both setup/transactional data between domains. Also each table will have GID/XID columns for each business object. For example a PO will have ORDER_BASE_GID and ORDER_BASE_XID:  

  * ORDER_BASE_GID to represent a unique system generated/user entered identifier(primary key in most cases) that takes format "Domain Name"."PO Number" (For example, DMN.12345 would be ORDER_BASE_GID value where DMN is the domain name and 12345 is the PO Number) 
  * ORDER_BASE_XID to represent actual PO number that can be recognized by business users like free text value. Most of the cases business users might use same value for both these GID/XID columns.

**Standard OTM Schema:**  
  
**GLOGOWNER Schema:** This schema is used to maintain all the transnational data like PO Data, Order Release data, Shipment data, etc.  
  
**REPORT OWNER Schema:** This schema is used to store report definitions, oracle stored procedures that will be used by BI Publisher Query templates, etc. For objects created in this schema we should create a public synonym to make the object accessible to OTM application.  
  
OTM Data Dictionary  
  
Once you know the table name for a business object you can get more details from OTM Data Dictionary. In the OTM URL place "html/data_dict" next to "GC3" to access data dictionary  
  
**Example:** www.otm-oracle.com/GC3/html/data_dict/  
  
**Note:** There is '*' against the columns to represent primary key combination and next to each column is Foreign Key information within the brackets.  
  
Below example says - SHIP_UNIT_LINE table has SHIP_UNIT_GID, SHIP_UNIT_LINE_NO as primary key combination and SHIP_UNIT_LINE.SHIP_UNIT_GID references SHIP_UNIT.SHIP_UNIT_GID.  
![](/images/otm-domains-standard-schema-an-img1-16093e055e.png)  
  
  
**Note:** Please post corrections(if any) to 'learnotm@outlook.com'