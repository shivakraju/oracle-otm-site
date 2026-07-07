---
title: "03 - Service Provider and Rates"
date: 2020-08-22T04:43:00+00:00
draft: false
weight: 180
tags:
  - "RATE_OFFERING"
  - "Rate Record"
  - "Rate Service"
  - "Rates"
  - "RATE_SERVICE"
  - "Service Provider"
  - "RATE_GEO"
  - "Rate Offering"
aliases:
  - "/2020/08/basic-otm-configurations-03-service.html"
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

**Service Provider (Carrier):**

Define two service providers with their SCAC codes and country code as USA as shown below:

Contract and Rate Management > Service Provider Manager:

> ![](/images/basic-otm-configurations-03-se-img1-d84a74c0db.png)

  

**Rates:**

  

Create new Rate Offering that details high level contract details between your organization and service providers like type of offering(TL,LTL, PARCEL, etc.), Rate Service, Rate Distance, etc.

  

Contract and Rate Management > Contract Management > Rate Offering > Enter below data:

  

> Offering ID=SGTM_TL
> 
> Offering Type=TL
> 
> Service Provider=SGTM
> 
> Rate Service ID=TL-SIM
> 
> Version=EXP2020 (New)
> 
> Rate Distance ID=LOOKUP ELSE ESTIMATE

  

Note that here we are using default Rate Service and Rate Distance provided by Oracle. However it is possible to configure external engines for time and distance calculations like PCMILER, RATEWARE XL.

  

Next create new Rate Records  which define cost details for each lane served by the service provider as per the contract agreed.

  

Open Rate Offering > Actions > Create Rate Record > Enter below data:

> Rate Record ID= SGTM_TL_DC_STOREB
> 
> Source Geo Hierarchy=CITY
> 
> Destination Geo Hierarchy=CITY
> 
> SG city= INDIANAPOLIS
> 
> SG Province Code= IN
> 
> SG Country Code ID= USA
> 
> DG City= CHARLOTTE
> 
> DG Province Code=NC
> 
> DG Country Code ID=USA
> 
> Rate Cost > Charge 100 USD PER Buy Shipment

  

> ![](/images/basic-otm-configurations-03-se-img2-b7d3679583.png)

> Define other rate records as shown below: 

> ![](/images/basic-otm-configurations-03-se-img3-bae23963e6.png)

> ![](/images/basic-otm-configurations-03-se-img4-1e8cf7b957.png)