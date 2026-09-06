---
title: "Business Numbers"
date: 2026-02-15T19:04:00+00:00
draft: false
weight: 40
tags:
  - "business numbers"
  - "BN rule"
  - "instructions"
  - "expressions"
aliases:
  - "/2026/02/business-numbers.html"
keywords:
  - "Oracle OTM business number rule"
  - "OTM business number sequence configuration"
  - "Oracle OTM custom ID generation rule"
  - "OTM business number expression format"
  - "Oracle OTM invoice shipment number rule"
  - "OTM BN rule instruction definition"
  - "Oracle Transportation Management numbering"
  - "OTM business number date format expression"
  - "Oracle OTM default XID sequence override"
  - "OTM business number rule edit steps"
description: "Explains Oracle OTM Business Number Rules and how to create custom ID sequences for business objects like shipments and invoices using expression syntax with date tokens and numeric range definitions."
url: "/posts/business-numbers/"
---

Business Number Rules control how OTM generates IDs for business objects such as Order Bases, Order Releases, Shipments, and Invoices. OTM provides default XID sequences for all objects, but you can create custom rules when business requirements call for a specific format or numbering range.

<div class="step-box">Business Process Automation > Power Data > Business Numbers > Business Number Rule</div>

Every rule definition consists of one or more instructions enclosed in braces `{ }`. Literal text, if any, appears outside the braces. For example, the default rule for the invoice ID is:

```
{dddddddd:id=1}-{nnnn:contexts=1:start=1}
```

**Common expression formats:**

```
{dddddddd:id=1}               — Date in YYYYDDMM format
{nnnn:start=1000:end=4999}    — 4-digit number starting at 1000, ending at 4999
```

**To edit an existing Business Number rule:**

1. Ensure the existing rule is not set as the Default.
2. Create a new BN rule and set it as the Default.
3. Specify the rule definition to control how the generated number is formed.
4. Ensure the **BN Type** on the new rule matches the BN Type of the original rule — otherwise the system will not generate the number.

**Backend Table:**

The `BN_SEQUENCE` table maintains two critical columns — `BN_CONTEXT` and `CURVALUE` — both derived from the BN rule.

**Example:**

The BN Rule for bulk plan ID is:

```
{dddddddd:id=1}-{nnnn:contexts=1:start=1}
```

If 10 bulk plans are run for a particular day, the generated IDs look like this:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEghbYi7452qWb6LCa5xIWc-0DoiC60_2Y3ZROnx43HPrG2ch_CCP628hbj6ccu3jqpnuORafc71jRhcVb6vh67R98rKUtU0uW4JVSU2va0MdZIA8L62ICkGiTy0vDRxLrLcNi3RHg1XcS8B3EY-X9Ehy0b-rdgaIYWGpqXd_2ebDo3FSc9Ryk7waFgan5E=w136-h200)](https://blogger.googleusercontent.com/img/a/AVvXsEghbYi7452qWb6LCa5xIWc-0DoiC60_2Y3ZROnx43HPrG2ch_CCP628hbj6ccu3jqpnuORafc71jRhcVb6vh67R98rKUtU0uW4JVSU2va0MdZIA8L62ICkGiTy0vDRxLrLcNi3RHg1XcS8B3EY-X9Ehy0b-rdgaIYWGpqXd_2ebDo3FSc9Ryk7waFgan5E)

`BN_SEQUENCE` maintains `CURVALUE` with the last or maximum sequence for that context. In the example below, the next bulk plan in that context takes `0010 + 1 = 0011` as the next ID:

```sql
SELECT *
FROM BN_SEQUENCE bs
WHERE BN_RULE_GID = 'DOMAIN_NAME.BULK_PLAN_XID.DEFAULT'
AND BN_CONTEXT = '20210126'
ORDER BY insert_date DESC;
```

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi_B194DIabpSHuhQf0r7O89E7fO8ylV-mMN_CeBIwKlO5lHuQ375NclJ-eLBKE6z0VSPUwxt2OO87mIhPvA_felpFQyx5hq1xlikpQBwjiThCcFWX9CcyvuuJOAfu3UWl4FnLcJI3WklrWDYWxgGMrqMo4lQHnZWlEv1BkoLT21eREWcbv6ZTU2-aqOwE=w640-h125)](https://blogger.googleusercontent.com/img/a/AVvXsEi_B194DIabpSHuhQf0r7O89E7fO8ylV-mMN_CeBIwKlO5lHuQ375NclJ-eLBKE6z0VSPUwxt2OO87mIhPvA_felpFQyx5hq1xlikpQBwjiThCcFWX9CcyvuuJOAfu3UWl4FnLcJI3WklrWDYWxgGMrqMo4lQHnZWlEv1BkoLT21eREWcbv6ZTU2-aqOwE)

**A common problem scenario:**

If the ORDER_MOVEMENT_XID.DEFAULT rule is defined as:

```
{r*:id=1:xml=ORDER_RELEASE}-{nnn:contexts=1:start=1}
```

A 3-digit sequence (`nnn`) allows a maximum of 999 values. Creation of the 1000th order movement will fail because the generated number would require 4 digits. Increase the digit count in the rule definition before this limit is reached.
