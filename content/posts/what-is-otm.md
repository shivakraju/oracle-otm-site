---
title: "What is OTM ?"
date: 2016-04-14T21:35:00+00:00
draft: false
weight: 10
tags:
  - "G-log"
  - "Introduction"
  - "Basics"
  - "OTM"
  - "Learn"
  - "Gottimukkala"
  - "Oracle"
  - "Shiva"
aliases:
  - "/2016/04/introduction-to-oracle.html"
---

OTM stands for Oracle Transportation Management and it is a software product designed to automate various logistics business processes like receiving orders from source ERP systems for freight consolidation, optimizing routes and shipping costs, sending tender requests to service providers(carriers), receiving shipment tracking revents from carriers, recieving and processing invoices from carriers, allocate freight costs to orders, and similar other functions which we will further discuss in future posts.

  
This product is designed such a way that it can be easily configured and customized by IT Consultants for various client specific business needs with minimal technical expertise. IT Technical consultants would need basic Oracle SQL and XML knowledge for customizing the product and Functional consultants would need basic logistics domain knowledge to configure(setup) the product based on the documentation and use cases provided by Oracle. Latest OTM SaaS versions make it easier for clients to just focus on core business configurations to fast track product implementation timelines while Oracle provides necessary infrastructure and application maintainance for all the standard (out of the box) OTM features.  
  
This product is originally developed by a company with name "Global Logistics Technologies, Inc" (also known as G-log). G-log was acquired by Oracle around 2005 and was renamed as OTM - Oracle Transportation Management.   
  
OTM has in-built integration with Oracle E-Business Suite of applications like Oracle Shipping(WSH). OTM can integrate with any external system by posting and receiving XML files based on GlogXML.xsd (product defined schema/data structure). Latest versions of OTM also support REST-API call based integrations. Note that OTM is not an application/module within the Oracle E-Business Suite of applications. OTM requires a separate installation - web, application and database tiers for on-premise configurations. Please see the next topic "OTM Architecuture" for these details.  
  
At a high level, few core capabilities of OTM are mentioned here:  

  * Receiving Purchase Orders(Order Base) from source ERP systems/legacy systems 
  * Processing Order Release s(bookings) from the Purchase Orders for partial quantity or complete quantity with manual or automated release instructions
  * Plan/consolidate Order Releases with common source and destination locations or into multi-stop shipments based on standard Bulk Plan algorithm that is configurable for client specific requirements. Bulk Plan involves identifying Itinerary(route), least cost Service Provider or Carrier (based on pre-uploaded rates), optimize loading of items into containers(equipments), calculating shipment in-transit times based on setups, etc. 
  * OTM can dynamically fetch LTL rates from third party applications like 'SMC Rateware' and also distances between zip codes using third party applications like 'MILEMAKER', 'PCMILER', etc
  * Send Tender Offer requests to Service Providers identified during planning. Note that if Carrier cannot accept XML tender files, we need to use Middleware tools like Web Methods, Mulesoft, Oracle BPEL etc to translate OTM outbound XML files to carrier readable formats like EDI files.
  * Receive T ender Offer response and update the shipment
  * Receive Shipment Tracking updates from Service Providers and update the shipment
  * Receive/process invoices from Service Providers, match the invoice costs with planned costs for invoice approvals, create vouchers for approved invoices, allocate the costs against customer orders, etc.