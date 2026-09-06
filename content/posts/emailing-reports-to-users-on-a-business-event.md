---
title: "Emailing Reports to Users on a Business Event"
date: 2016-11-29T20:57:00+00:00
draft: false
weight: 320
tags:
  - "PRINT DOCUMENT"
  - "REPORT_LOG_PARAMETER"
  - "Email OTM Report"
  - "REPORT - READY"
aliases:
  - "/2016/11/emailing-reports-to-users.html"
keywords:
  - "Oracle OTM email report on business event"
  - "OTM PRINT DOCUMENT agent action"
  - "Oracle OTM REPORT-READY event agent"
  - "OTM shipment tender accepted email report"
  - "Oracle OTM report set email attachment"
  - "OTM agent email report PDF"
  - "Oracle OTM REPORT_LOG_PARAMETER"
  - "OTM notify contact email report"
  - "Oracle Transportation Management automated report email"
  - "OTM agent send report on tender acceptance"
description: "Shows how to configure Oracle OTM to automatically email a report as a PDF attachment when a shipment tender is accepted, using the PRINT DOCUMENT agent action and the REPORT-READY event."
---

OTM can automatically generate a report and email it as an attachment when a business event occurs. The example below shows how to send a custom report to the user who created a purchase order when a shipment tender is accepted.

**Step 1 — Create a Report Set:**

<div class="step-box">Business Process Automation > Reporting > Report Manager > Report Set Manager</div>

Create a Report Set and include your report. You may add multiple reports to the Report Set as required.

**Step 2 — Create a SHIPMENT agent with a PRINT DOCUMENT action:**

Create a SHIPMENT agent that listens to the **SHIPMENT - STATUS CHANGED** event with the restriction **SECURE RESOURCES_ACCEPTED**. Add the following standard action to the agent:

<div class="field-box"><strong>PRINT DOCUMENT:</strong> Specify the name of the Report Set from Step 1 and the output format (e.g. PDF). When a tender is accepted, this action generates the report and OTM raises a standard <strong>REPORT-READY</strong> event for the generated report.</div>

**Step 3 — Create a REPORT agent that listens to the REPORT-READY event:**

Create a REPORT agent that listens to the **REPORT-READY** event with an event restriction that filters on the Report Set name from Step 1. Add the following two actions to this agent:

**Action 1 — ASSIGN VARIABLE to fetch the PO creator:**

Use the ASSIGN VARIABLE action with the following SQL to fetch the user who created the purchase order:

```sql
SELECT MAX(ob.insert_user)
FROM   report_log_parameter rlp,
       view_shipment_order_release vsor,
       order_release orl,
       ob_order_base ob
WHERE  file_name = $gid
AND    parameter_name = 'P_SHIPMENT_ID'
AND    parameter_value = vsor.shipment_gid
AND    vsor.order_release_gid = orl.order_release_gid
AND    orl.order_base_gid = ob.order_base_gid
```

<div class="note-box"><strong>Note:</strong> The REPORT_LOG_PARAMETER table stores the input parameter values used for each report run. This query fetches the Shipment ID parameter value and joins to the related PO to identify the creator. A separate report definition for email purposes may be required — report definitions with multiple parameters beyond Shipment ID may not work reliably in this context.</div>

**Action 2 — NOTIFY CONTACT:**

Use the NOTIFY CONTACT action with the following settings:

<div class="field-box"><strong>Contact:</strong> Set to the variable returned by Action 1. Create Contact records under Business Process Automation > Communication Management > Contacts with Contact ID matching the User ID for each user who should receive emails. Ensure the <strong>Notification On</strong> flag is checked on each Contact record.</div>

<div class="field-box"><strong>Communication Method:</strong> EMAIL</div>

<div class="field-box"><strong>Subject:</strong> Use a dynamic subject with variables, for example: Report - ShpRef#: $SHP_REF; SID=$GID</div>

<div class="field-box"><strong>Stylesheet Profile:</strong> Create a Stylesheet Profile under Business Process Automation > Power Data > Event Management > Stylesheet Profiles with the following settings:
<ul>
<li>Template Name: workflow/DefaultReportEventHtml.xsl (Standard)</li>
<li>Format: text/html</li>
<li>Subject Property Key: {2} — this ensures the email subject uses the value defined in the NOTIFY CONTACT action</li>
<li>Message Direction: OUTBOUND</li>
<li>Type: XSL</li>
<li>Attachments: EMBED</li>
</ul>
</div>
