---
title: "06 - Tender process"
date: 2020-08-22T04:55:00+00:00
draft: false
weight: 210
tags:
  - "OTM"
  - "Oracle"
  - "Tender"
aliases:
  - "/2020/08/basic-otm-configurations-06-tender.html"
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

Tender Process

When shipments are created, note that status on these shipments is SECURE RESOURCES_NOT STARTED.

  

> ![](/images/basic-otm-configurations-06-te-img1-70d35394c8.png)

  

At this point, we need to notify carrier about the shipment information like pickup time and location. This can be done using:

Shipment > Actions > Shipment Management > Tender > Secure Resources

  

> ![](/images/basic-otm-configurations-06-te-img2-96cea8f493.png)

Notice that Shipment SECURE_RESOURCE status changes to 'TENDERED' 

  

OTM sends out tender XML to external system or email notification to carrier based on configuration at the service provider level.

  

Carrier should respond to the tender either via EDI or manually login into OTM app with 'Service Provider' role and accept or reject the tender.

Tender Accept/Reject Process

Assume that carriers have access to OTM application in that case they can login as:

> SERVPROV.DOMAIN-SCAC format as default USER ID
> 
> CHANGEME as default password

  

In this scenario, we login as SGTM and PNDP carriers and accept/reject these tenders:

> ![](/images/basic-otm-configurations-06-te-img3-34e7fdac05.png)

You can see the outstanding tenders for the carrier:

  

> ![](/images/basic-otm-configurations-06-te-img4-5be841085c.png)

You can select this record and Actions > Accept/Decline. Let’s decline this PNDP carrier tender.

  

**Accept the tender for SGTM carrier:**

  

Now go back to TCRP.ADMIN and review the shipments.

> ![](/images/basic-otm-configurations-06-te-img5-f89924dec9.png)

First leg shipment PNDP carrier rejected, so OTM automatically tendered to next available carrier SGTM with $30 rate we defined.

  

> ![](/images/basic-otm-configurations-06-te-img6-bae23963e6.png)

Now we login as SERVPROV.TCRP-SGTM to see this new tender for first leg.

  

> ![](/images/basic-otm-configurations-06-te-img7-06b4e21ec1.png)

  

Accept this tender. Now we can see both the shipments are show tender as accepted.

> ![](/images/basic-otm-configurations-06-te-img8-8c7043a964.png)