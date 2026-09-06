---
title: "Service Provider and Rates"
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
  - "/posts/basic-otm-configurations-03-service-provider-and-rates/"
  - "/2020/08/basic-otm-configurations-03-service.html"
keywords:
  - "Oracle OTM service provider setup"
  - "OTM carrier rate configuration"
  - "Oracle OTM rate offering rate service setup"
  - "OTM SCAC code service provider"
  - "Oracle OTM rate record configuration"
  - "OTM RATE_GEO lane rate setup"
  - "Oracle OTM carrier contract rate entry"
  - "OTM service provider SCAC country code"
  - "Oracle Transportation Management rate setup steps"
  - "OTM basic configuration carrier rates"
description: "Covers how to define service providers with SCAC codes and configure rate offerings, rate services, and rate records in Oracle OTM as part of the basic end-to-end configuration series."
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

**Service Provider (Carrier):**

Define two service providers with their SCAC codes and country code as USA as shown below:

Contract and Rate Management > Service Provider Manager:

![](/images/basic-otm-configurations-03-se-img1-d84a74c0db.png)

  

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

  

![](/images/basic-otm-configurations-03-se-img2-b7d3679583.png)

> Define other rate records as shown below: 

![](/images/basic-otm-configurations-03-se-img3-bae23963e6.png)

![](/images/basic-otm-configurations-03-se-img4-1e8cf7b957.png)

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-02-itinerary/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Itinerary</div>
  </a>  <a href="/posts/basic-otm-configurations-04-business-numbers-planning-parameter/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Business Numbers, Planning Parameter</div>
  </a></div>