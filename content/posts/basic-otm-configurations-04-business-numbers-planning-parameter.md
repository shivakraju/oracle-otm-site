---
title: "04 - Business Numbers, Planning Parameter"
date: 2020-08-22T04:47:00+00:00
draft: false
weight: 190
tags:
  - "Business Number"
  - "Planning Parameter"
  - "OTM"
  - "Oracle"
aliases:
  - "/2020/08/basic-otm-configurations-04-business.html"
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

**Business Numbers:**

OTM has default numbering for all business data objects like the one shown below for shipment - 01001.

  

> ![](/images/basic-otm-configurations-04-bu-img1-18e64bcaca.png)

  

To change this to a specific number requested by business, we can do below:

Business Process Automation > Power Data > Business Numbers > Business Number Rule > Search for %SHIPMENT%

You will notice that there is default rule (TCRP domain level) for generating XID. Let us edit this rule for this domain:

  

> ![](/images/basic-otm-configurations-04-bu-img2-0ce1184927.png)

  

Let’s change this to use below rule. Rule is combination of static and dynamic expressions. Let us use three expressions:

'SHIP' which is static

{dddddddd:id=1} for date is YYYYMMDD format

One Hyphen which is static

{nnnnn:start=01000} for a five digit number starting with 01000 value

> ![](/images/basic-otm-configurations-04-bu-img3-73428c0a62.png)

Now if you plan a shipment, it will generate ID as below:

  

> ![](/images/basic-otm-configurations-04-bu-img4-ffe4ea06c0.png)

  

**Planning Parameter:**

  

Shipment Management > Power Data > General > Parameter Sets > New > Enter ‘TCRP_PLAN’ as new ID and save the record.

  

> ![](/images/basic-otm-configurations-04-bu-img5-a647769878.png)

  

Note that all above configuration parameters can be changed based on business requirements and they control how OTM Bulk Plan algorithm works. For now let us proceed with default values.

Now let us set this parameter as default planning parameter for domain TCRP.

Configuration and Administration > Domain Management > Domain Settings > Search > Select TCRP record and Edit > Change Parameter Set ID=TCRP_PLAN > Finished.

Now while submitting bulk plan, this new parameter comes up as default parameter.