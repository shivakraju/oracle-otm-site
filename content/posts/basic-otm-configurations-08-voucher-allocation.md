---
title: "08 - Voucher Allocation"
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
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

Voucher Allocations

After invoice is approved, OTM creates a voucher record for this invoice.

  

> ![](/images/basic-otm-configurations-08-vo-img1-0151e64dfd.png)

  

At this stage, ALLOCATION_VOUCHER status on the voucher is – NOT ALLOCATED

  

> ![](/images/basic-otm-configurations-08-vo-img2-09dfa2084c.png)

  

To allocate total voucher costs to correspoding orders based on weight or volume we need to define voucher allocation rule.

Financials > Allocation Rule Management > Allocation Rules:

Define allocation rule with line level weight 100%

> ![](/images/basic-otm-configurations-08-vo-img3-11037065f9.png)

Attach this allocation rule to the service provider.

  

> ![](/images/basic-otm-configurations-08-vo-img4-5c05c98d75.png)

Now go to voucher actions > Financials > Manage Vouchers > Allocate Voucher

Status on the voucher now changes to ALLOCATED.

> ![](/images/basic-otm-configurations-08-vo-img5-e384f3eea3.png)

After the voucher is allocated, then we can see the Order Release in View mode to see those details:

> ![](/images/basic-otm-configurations-08-vo-img6-dd1dde4b1d.png)

This information or freight cost allocated to PO level or Order Release Line level is critical because incase where you have multiple POs from different vendors on the same shipment and you want to allocate or identify vendor level shipping costs, use this allocation feature.