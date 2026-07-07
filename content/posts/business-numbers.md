---
title: "Business Numbers"
date: 2026-02-15T19:04:00+00:00
draft: false
weight: 300
tags:
  - "business numbers"
  - "BN rule"
  - "instructions"
  - "expressions"
aliases:
  - "/2026/02/business-numbers.html"
---

**Navigation:** Business Process Automation > Power Data > Business Numbers > Business Number Rule

OTM provides default XID sequences for all the business objects likes order bases, order releases, shipments, invoices, etc. However if we need to change the default sequences based on business specific requirements, we can create custom business number rules.

Every rule definition consists of one or more instructions, which are set in braces, { }. Literal text, if any, appears outside the braces. For example, this is the default rule definition for the invoice ID:

{ dddddddd:id=1}-{nnnn:contexts=1:start=1}

**Common expression formats:**

{dddddddd:id=1} for dates in YYYYDDMM format

{nnnn:start=1000:end=4999} for a 4 digit number starting with 1000 and ending with 4999

To edit the existing BN rule.

1. Make sure that it is not set as the Default rule.

2. Create a new BN rule and set that as the Default.

3. Specify the rule defintion. The rule definition determines how the generated number is formed.

4. Make sure that the BN Type on your new rule matches the BN type that you found earlier, otherwise the system will not generate the number.

**Backend table:**

BN_SEQUENCE table maitains two critical columns - BN_CONTEXT and CURVALUE. Both the values are derived from BN rule.

**Example:** 

**BN Rule for bulk plan ID is:** {dddddddd:id=1}-{nnnn:contexts=1:start=1}

If 10 bulk plans are run for a particular day, they look like below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEghbYi7452qWb6LCa5xIWc-0DoiC60_2Y3ZROnx43HPrG2ch_CCP628hbj6ccu3jqpnuORafc71jRhcVb6vh67R98rKUtU0uW4JVSU2va0MdZIA8L62ICkGiTy0vDRxLrLcNi3RHg1XcS8B3EY-X9Ehy0b-rdgaIYWGpqXd_2ebDo3FSc9Ryk7waFgan5E=w136-h200)](https://blogger.googleusercontent.com/img/a/AVvXsEghbYi7452qWb6LCa5xIWc-0DoiC60_2Y3ZROnx43HPrG2ch_CCP628hbj6ccu3jqpnuORafc71jRhcVb6vh67R98rKUtU0uW4JVSU2va0MdZIA8L62ICkGiTy0vDRxLrLcNi3RHg1XcS8B3EY-X9Ehy0b-rdgaIYWGpqXd_2ebDo3FSc9Ryk7waFgan5E)

BN_SEQUENCE maintains CURVALUE with last or max sequence for that context as shown below so that bulk plan takes 0010+1 = 0011 as next ID in below example:

  
SELECT *  
FROM BN_SEQUENCE bs  
WHERE BN_RULE_GID ='DOMAIN_NAME.BULK_PLAN_XID.DEFAULT'  
AND BN_CONTEXT= '20210126'  
ORDER BY insert_date DESC;

[![](https://blogger.googleusercontent.com/img/a/AVvXsEi_B194DIabpSHuhQf0r7O89E7fO8ylV-mMN_CeBIwKlO5lHuQ375NclJ-eLBKE6z0VSPUwxt2OO87mIhPvA_felpFQyx5hq1xlikpQBwjiThCcFWX9CcyvuuJOAfu3UWl4FnLcJI3WklrWDYWxgGMrqMo4lQHnZWlEv1BkoLT21eREWcbv6ZTU2-aqOwE=w640-h125)](https://blogger.googleusercontent.com/img/a/AVvXsEi_B194DIabpSHuhQf0r7O89E7fO8ylV-mMN_CeBIwKlO5lHuQ375NclJ-eLBKE6z0VSPUwxt2OO87mIhPvA_felpFQyx5hq1xlikpQBwjiThCcFWX9CcyvuuJOAfu3UWl4FnLcJI3WklrWDYWxgGMrqMo4lQHnZWlEv1BkoLT21eREWcbv6ZTU2-aqOwE)

  

**A problem scenario:** If you are generating ORDER_MOVEMENT_XID.DEFAULT as below:

{r*:id=1:xml=ORDER_RELEASE}-{nnn:contexts=1:start=1}

If there are 999 order movements created, creation of next order movement will fail as it will be four-digit number.