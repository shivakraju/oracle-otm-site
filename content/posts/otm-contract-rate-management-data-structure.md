---
title: "OTM Contract & Rate Management Data Structure"
date: 2016-05-06T17:29:00+00:00
draft: false
weight: 130
tags:
  - "RATE_OFFERING"
  - "Rate Record"
  - "Rate Service"
  - "Service Provider"
  - "RATE_SERVICE"
  - "RATE_GEO"
  - "Rate Distance"
  - "Rate Offering"
aliases:
  - "/2016/05/otm-contract-rate-management-data.html"
---

Service Provider  
  
Service Provider/Carrier is the party who provides transportation services. Service Providers typically own the trucks, equipment(containers), trailers, other resources like drivers, etc. They receive tender offer request from customers specifying the freight details(source location, destination location, weight and volume, shipment date ranges - start time, end time, etc). Once shipment is delivered, they issue invoice to the customer for freight cost settlements.  
  
**Tables:**  
SCAC - every Service Provider in OTM should be associated with a SCAC code - usually a four letter code standard code associated with that Carrier  
SERVPROV - Service Provider details like Service Provider name, SCAC code, transport modes, cost allocation rules, invoice approval rules, etc. A LOCATION record is also created for every SERVPROV record.   
  
If you are manufacturing company or any business not having your own infrastructure to move freight from one location to another, you will negotiate a contract with these carriers on the:  

  * Transport Mode(mode of transport like TL,LTL,PARCEL) 
  * Rate service(like 2 day shipping, 3 day shipping etc)
  * Lanes to be covered(source/dest region combinations to be served)
  * Rates and discounts on these lanes depending on your volume and so on

You create a Rate Offering, Rate service, Rate Record in the OTM with above details.  
  
Rate Service  

Rate Service defines how much time it takes for shipment to reach from source to destination location. For TL and LTL rate service type is usually defined as SIMULATION with assumption that average truck speed would be - say 50 Mile per hour, etc. For PARCELS, rate service type may be defined with type as DAYDURATION specifying number to days for your lanes. For example FedX 1 DAY service, FedX 2 DAY service, etc. All these configurations would depend on your business needs.  
  
**Tables:**  
RATE_SERVICE_TYPE  
RATE_SERVICE_PROFILE   
RATE_SERVICE  
RATE_SERVICE_SPEED  
**SERVICE_TIME:** This is to see service times associated to a particular Rate Service ID.   
  
Rate Distance   
  
This is used to configure how you calculate distance between source/dest location on your shipment.  
You can either use standard LOOKUP/ESTIMATE or you can use external(third party) distance engine like MILEMAKER or PCMILER to calculate distance between two zip codes, cities, etc  
  
**Tables:**  
RATE_DISTANCE  
DISTANCE_EXTERNAL_ENGINE  
DISTANCE_EXTERNAL_ENGINE_PARMS   
  
Rate Offering  
  
Rate Offering is the contract defined with carrier confirming below details :  
Service Provider  
Service times(Rate Service)  
Transport Mode(TL, VESSEL, etc)  
Base Rate Service and Distance Service engines(for LTL)  
StopOff Charges, Accessorial costs(like fuel surchage, etc)   
Currency  
Contract Expiration Date, etc  
  
**Tables:**  
RATE_OFFERING_TYPE   
RATE_OFFERING  
RATE_OFFERING_STOPS  
RATE_OFFERING_REMARK  
RATE_OFFERING_ACCESSORIAL  
RATE_OFFERING_INV_PARTY  
  
Rate Record  
  
Rate record holds the cost details associated with the services provided by the carrier. Depending on the business requirements costs can be defined at container level, lane based, weight/volume, etc  
  
**Tables:**  
RATE_GEO  
RATE_GEO_COST  
RATE_GEO_COST_UNIT_BREAK  
RATE_GEO_COST_WEIGHT_BREAK  
RATE_GEO_COST_GROUP  
RATE_GEO_ACCESSORIAL  
RATE_GEO_REFNUM  
RATE_GEO_REMARK