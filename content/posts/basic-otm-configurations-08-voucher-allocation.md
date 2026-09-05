---
title: "Voucher Allocation"
date: 2020-08-22T04:59:00+00:00
draft: false
weight: 230
tags:
  - "Allocation"
  - "OTM"
  - "Oracle"
  - "Voucher"
aliases:
  - "/2020/08/basic-otm-configurations-08-voucher.html"
keywords:
  - "Oracle OTM voucher allocation configuration"
  - "OTM voucher allocation invoice approved"
  - "Oracle OTM freight cost allocation voucher"
  - "OTM ALLOCATION_VOUCHER status"
  - "Oracle OTM voucher not allocated status"
  - "OTM cost allocation order release"
  - "Oracle Transportation Management voucher setup"
  - "OTM freight voucher allocation steps"
  - "Oracle OTM invoice voucher record"
  - "OTM allocate freight cost to PO"
description: "Covers the Oracle OTM voucher allocation process that runs after invoice approval, distributing freight costs to order releases and updating the ALLOCATION_VOUCHER status."
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

Voucher Allocations

After invoice is approved, OTM creates a voucher record for this invoice.

  

![](/images/basic-otm-configurations-08-vo-img1-0151e64dfd.png)

  

At this stage, ALLOCATION_VOUCHER status on the voucher is â€“ NOT ALLOCATED

  

![](/images/basic-otm-configurations-08-vo-img2-09dfa2084c.png)

  

To allocate total voucher costs to correspoding orders based on weight or volume we need to define voucher allocation rule.

Financials > Allocation Rule Management > Allocation Rules:

Define allocation rule with line level weight 100%

![](/images/basic-otm-configurations-08-vo-img3-11037065f9.png)

Attach this allocation rule to the service provider.

  

![](/images/basic-otm-configurations-08-vo-img4-5c05c98d75.png)

Now go to voucher actions > Financials > Manage Vouchers > Allocate Voucher

Status on the voucher now changes to ALLOCATED.

![](/images/basic-otm-configurations-08-vo-img5-e384f3eea3.png)

After the voucher is allocated, then we can see the Order Release in View mode to see those details:

![](/images/basic-otm-configurations-08-vo-img6-dd1dde4b1d.png)

This information or freight cost allocated to PO level or Order Release Line level is critical because incase where you have multiple POs from different vendors on the same shipment and you want to allocate or identify vendor level shipping costs, use this allocation feature.

**Basic OTM Configurations:**

[← Invoicing](/posts/basic-otm-configurations-07-invoicing/)