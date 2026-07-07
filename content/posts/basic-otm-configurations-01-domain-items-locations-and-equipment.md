---
title: "01 - Domain, Items, Locations, and Equipment"
date: 2020-08-22T05:25:00+00:00
draft: false
weight: 160
tags:
  - "Item"
  - "Equipment"
  - "domain"
  - "OTM"
  - "Oracle"
  - "Location"
aliases:
  - "/2020/08/basic-otm-configurations-01-domain.html"
  - "/2020/06/basic-otm-configurations.html"
---

**Note:** These posts are numbered to cover a typical end to end transaction flow that happens in OTM at a very high level. 

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

[02 - Itinerary](/posts/basic-otm-configurations-02-itinerary/)

[03 - Service Provider and Rates](/posts/basic-otm-configurations-03-service-provider-and-rates/)

[04 - Business Numbers, Planning Parameter](/posts/basic-otm-configurations-04-business-numbers-planning-parameter/)

[05 - Bulk Plan](/posts/basic-otm-configurations-05-bulk-plan/)

[06 - Tender process](/posts/basic-otm-configurations-06-tender-process/)

[07 - Invoicing](/posts/basic-otm-configurations-07-invoicing/)

[08 - Voucher Allocation](/posts/basic-otm-configurations-08-voucher-allocation/)

  

Below is a typical OTM end to end flow in it's most simple/vanilla usage. Readers can explore more on each of the below topics and use this as starting point to understand basic OTM configurations using OTM Help documentation.

  

**Business Scenario:**  

There is Toys Corporation (TCRP) with one DC/Warehouse and three stores in 3 different cities. DC distributes items – Item A, Item B and Item C to three locations (store locations). TCRP has contract with two carriers (SGTM, PNDP) to support their logistics needs and these carriers use their 20 foot, 40 foot or 50 foot equipments. As specified below each carrier supports specific itineraries/legs for TCRP.

TCRP wants to optimize their transport costs using "bulk planning" feature of OTM app and settle invoices for the transport services provied by these carriers.

Below is a draft overview of what we are trying to implement:

> > > ![](/images/basic-otm-configurations-01-do-img1-d2cb92713c.png)

> We can map above locations to real time locations as below:

>   * DC/Warehouse location in Indianapolis, IN, 46202
>   * Loc_A in Nashville, TN, 37203
>   * Loc_B in Charlotte, NC, 28078
>   * Loc_C in Atlanta, GA, 30303
> 

> > ![](/images/basic-otm-configurations-01-do-img2-729bca9542.png)

  

  

**Domain:**

Create a new domain TCRP to store the configurations and transaction data related to this business scenario. 

  

Config and Admin > Domain Management > Add Domain

  

> > ![](/images/basic-otm-configurations-01-do-img3-c3dc82dd27.png)

  

  

Login to this new domain with default ADMIN user and CHANGEME as password:

  

> > ![](/images/basic-otm-configurations-01-do-img4-2cf8fe190c.png)

**Once you login, you will see:** 

> > ![](/images/basic-otm-configurations-01-do-img5-3d014c7b9f.png)

**Items:**

Define three items ITEMA01, 02, 03

Order Management > Material Management > Item:

> ![](/images/basic-otm-configurations-01-do-img6-bd7cb8d0d2.png)

**Item Dimensions:**

Item Weight = 2 LB. 

> ![](/images/basic-otm-configurations-01-do-img7-a40bf90d33.png)

**Other item dimensions are updated as below:**

  

> ![](/images/basic-otm-configurations-01-do-img8-8bba784532.png)

**Locations:**

  

First, let's create for required locations as shown below:

Shipment Management > Location Manager

  

**Create Warehouse/DC location:** DC_TCRP with below details:

  

> ![](/images/basic-otm-configurations-01-do-img9-c911a8fa98.png)

  

  

> ![](/images/basic-otm-configurations-01-do-img10-6cb1a6d6fb.png)

  

> ![](/images/basic-otm-configurations-01-do-img11-0095e94000.png)

  

Create other 3 store locations with role as ship from/to:

> ![](/images/basic-otm-configurations-01-do-img12-1dd20378a4.png)

  

Equipment

Define equipment groups – 20_FT, 40_FT, 53_FT with below data:

Shipment Management > Equipment Management > Equipment Groups:

  

> ![](/images/basic-otm-configurations-01-do-img13-e748421598.png)

**Define Equipment Group Profiles with below data:**

Shipment Management > Equipment Management > Equipment Group Profile:

> ![](/images/basic-otm-configurations-01-do-img14-504d5e728e.png)

> ![](/images/basic-otm-configurations-01-do-img15-032b315090.png)