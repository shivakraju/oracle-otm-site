---
title: "07 - Invoicing"
date: 2020-08-22T04:57:00+00:00
draft: false
weight: 220
tags:
  - "Invoice"
  - "OTM"
  - "Oracle"
aliases:
  - "/2020/08/basic-otm-configurations-07-invoicing.html"
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

Invoicing

Once Shipment execution is completed, carrier sends invoice and OTM can:

• Match invoice to shipment based on MATCH rule

• Approve Invoice based on Invoice APPROVAL rule

• Allocate shipment costs to related order releases/POs based on weight or volume

> Invoice Matching:
> 
> Carrier who executed the shipping function will send an freigh charge invoice for settlement.
> 
> In OTM, we can validate this invoice cost against the OTM planned shipment cost by first matching invoice to a shipment.
> 
> This can be done by matching rule.

> Financials > Payment Rule Management > Match Rule: 

  

> ![](/images/basic-otm-configurations-07-in-img1-845c364684.png)

  

> A match rule will try to identify a shipment for an invoice by matching:
> 
> · Service Provider
> 
> · Refnums as shown above. Here we are creating invoice with SID (Shipment ID) as refnum and matching this to shipment refnum SID. In a real time business scenario these numbers can be BOL Number, Container Number references, etc.
> 
> To trigger this matching process go to:

> Invoice Actions > Auto Match Invoices

> ![](/images/basic-otm-configurations-07-in-img2-0a073a1406.png)

  

> Invoice once matched to a shipment will be recorded in below table:
> 
> SELECT * FROM INVOICE_SHIPMENT WHERE INVOICE_GID = 'TCRP.20180518-0001'

  

> Invoice Routes/Ports tab will show Match/approval notes, matched shipment details

> ![](/images/basic-otm-configurations-07-in-img3-08f8031794.png)

> Invoice Approvals
> 
> For a particular user to approve an invoice, note that OTM checks what is the invoice approval rule attached to the user definition.
> 
> So, create below invoice approval rule:
> 
> Financials > Payment Rule Management > Invoice Approval Rules:

> ![](/images/basic-otm-configurations-07-in-img4-d4bbab97fb.png)

> This rule says approve all invoices from $1 to $1000.
> 
> Attach this rule to Approval Rule profile:

> ![](/images/basic-otm-configurations-07-in-img5-66238a617c.png)

> Attach this profile to the user record:

> > ![](/images/basic-otm-configurations-07-in-img6-0234c62a46.png)

**Now we can approve invoice using below action:**

  

> ![](/images/basic-otm-configurations-07-in-img7-d217d23638.png)