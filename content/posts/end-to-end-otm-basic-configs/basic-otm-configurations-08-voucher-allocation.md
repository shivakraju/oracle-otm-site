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
  - "/posts/basic-otm-configurations-08-voucher-allocation/"
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

After an invoice is approved, OTM creates a Voucher record for it. Voucher Allocation distributes the total freight cost across the Order Releases on the shipment — proportionally by weight or volume — so each PO or Order Release line carries its share of the freight charge.

**Voucher record after invoice approval:**

OTM automatically creates the voucher once the invoice is approved:

![Voucher record created after invoice approval](/images/basic-otm-configurations-08-vo-img1-0151e64dfd.png)

At this point the `ALLOCATION_VOUCHER` status on the voucher is **NOT ALLOCATED**:

![Voucher showing ALLOCATION_VOUCHER status as NOT ALLOCATED](/images/basic-otm-configurations-08-vo-img2-09dfa2084c.png)

**Define an Allocation Rule:**

An Allocation Rule controls how the total voucher cost is split across Order Release lines. Define a rule that allocates 100% by line-level weight:

<div class="step-box">Financials > Allocation Rule Management > Allocation Rules</div>

![Allocation Rule screen showing line level weight at 100%](/images/basic-otm-configurations-08-vo-img3-11037065f9.png)

**Attach the rule to the Service Provider:**

Attach the Allocation Rule to the carrier's Service Provider record so OTM knows which rule to apply when processing vouchers for that carrier's invoices:

![Service Provider screen showing Allocation Rule attached](/images/basic-otm-configurations-08-vo-img4-5c05c98d75.png)

**Run Allocate Voucher:**

<div class="step-box">Financials > Manage Vouchers > Voucher Actions > Allocate Voucher</div>

The `ALLOCATION_VOUCHER` status changes to **ALLOCATED**:

![Voucher showing ALLOCATION_VOUCHER status as ALLOCATED](/images/basic-otm-configurations-08-vo-img5-e384f3eea3.png)

**Verify the allocated cost on the Order Release:**

Open the Order Release in View mode to see the freight cost allocated to it:

![Order Release showing allocated freight cost after voucher allocation](/images/basic-otm-configurations-08-vo-img6-dd1dde4b1d.png)

<div class="note-box"><strong>Note:</strong> Voucher Allocation is especially valuable when multiple Purchase Orders from different vendors are consolidated on the same shipment. It lets you identify and report each vendor's precise share of the freight cost — rather than manually apportioning a single lump-sum invoice.</div>

<div style="display:flex;gap:12px;margin-top:32px;border-top:2px solid #e2e8f0;padding-top:20px;flex-wrap:wrap;">
  <a href="/posts/basic-otm-configurations-07-invoicing/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">&#8592; Previous</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Invoicing</div>
  </a>  <a href="/posts/otm-inbound-integrations-xml/" style="flex:1;display:block;padding:14px 18px;border:1px solid #d1dce8;border-radius:8px;text-decoration:none;background:#f8fafc;text-align:right;">
    <div style="font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:#64748b;margin-bottom:5px;">Next &#8594;</div>
    <div style="font-size:15px;font-weight:600;color:#1c3557;">Inbound Integrations (XML)</div>
  </a></div>
