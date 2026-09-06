---
title: "Invoicing"
date: 2020-08-22T04:57:00+00:00
draft: false
weight: 220
tags:
  - "Invoice"
  - "OTM"
  - "Oracle"
aliases:
  - "/posts/basic-otm-configurations-07-invoicing/"
  - "/2020/08/basic-otm-configurations-07-invoicing.html"
  - "/posts/end-to-end-otm-basic-configs/basic-otm-configurations-07-invoicing/"
url: "/posts/end-to-end-otm-basic-configs/invoicing/"
keywords:
  - "Oracle OTM invoicing configuration"
  - "OTM carrier invoice match rule"
  - "Oracle OTM invoice approval rule"
  - "OTM invoice shipment cost matching"
  - "Oracle OTM freight invoice processing"
  - "OTM invoice allocation order release"
  - "Oracle Transportation Management invoice setup"
  - "OTM invoice match approve allocate"
  - "Oracle OTM freight cost settlement"
  - "OTM carrier invoice validation"
description: "Explains how Oracle OTM processes carrier invoices by matching them to shipments, applying approval rules, and allocating freight costs to order releases and purchase orders."
---

Once shipment execution is completed, the carrier sends a freight charge invoice for settlement. OTM can validate the invoice cost against the planned shipment cost, approve it, and then allocate that cost back to the originating Order Releases or Purchase Orders.

The three steps are: **Match → Approve → Allocate.**

**Invoice Matching:**

A Match Rule identifies which shipment corresponds to an incoming carrier invoice, by comparing reference numbers and the Service Provider. In this scenario the invoice carries the Shipment ID (SID) as a reference number, which is matched to the same reference on the shipment record.

<div class="step-box">Financials > Payment Rule Management > Match Rule</div>

![Match Rule configuration showing Service Provider and SID refnum matching](/images/basic-otm-configurations-07-in-img1-845c364684.png)

<div class="note-box"><strong>Note:</strong> In a real-world scenario the reference numbers can be BOL Number, Container Number, or any other carrier-specific reference. The Match Rule links the incoming invoice to the correct shipment regardless of which reference number your carrier uses.</div>

Once the Match Rule is defined, trigger the matching process on the invoice:

<div class="step-box">Invoice > Actions > Auto Match Invoices</div>

![Invoice list showing Auto Match Invoices action in the Actions menu](/images/basic-otm-configurations-07-in-img2-0a073a1406.png)

After matching, the link between invoice and shipment is recorded in the `INVOICE_SHIPMENT` table. You can verify this with:

```sql
SELECT * FROM INVOICE_SHIPMENT WHERE INVOICE_GID = 'TCRP.20180518-0001'
```

The Invoice Routes/Ports tab also shows matching and approval notes alongside the matched shipment details:

![Invoice Routes/Ports tab showing matched shipment details and match notes](/images/basic-otm-configurations-07-in-img3-08f8031794.png)

**Invoice Approval:**

OTM determines which approval rule to apply based on the rule attached to the approving user's profile. Create an Invoice Approval Rule that covers the expected invoice range:

<div class="step-box">Financials > Payment Rule Management > Invoice Approval Rules</div>

![Invoice Approval Rule screen showing approval range $1 to $1000](/images/basic-otm-configurations-07-in-img4-d4bbab97fb.png)

This rule approves all invoices between $1 and $1,000. Next, attach this rule to an Approval Rule Profile:

![Approval Rule Profile screen with the invoice approval rule attached](/images/basic-otm-configurations-07-in-img5-66238a617c.png)

Then attach the profile to the user record so OTM knows which rule to apply when that user approves invoices:

![User record screen showing the Approval Rule Profile field populated](/images/basic-otm-configurations-07-in-img6-0234c62a46.png)

With the rule and profile in place, approve the invoice from the invoice record:

<div class="step-box">Invoice > Actions > Approve</div>

![Invoice Actions menu showing the Approve option](/images/basic-otm-configurations-07-in-img7-d217d23638.png)

The invoice status changes to **Approved**, and the freight cost is now ready to be allocated back to the originating Order Releases and Purchase Orders in the next step.

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-06-tender-process/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Tender Process</div>
  </a>  <a href="/posts/basic-otm-configurations-08-voucher-allocation/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Voucher Allocation</div>
  </a></div>
