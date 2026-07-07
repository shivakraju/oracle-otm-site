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
---

There can be requirements where we want to send report as attachment to a user. We can configure that with below steps in OTM.  
  
In this example, suppose that we want to generate a custom report after shipment tender is accepted and send this report to contact on the PO or user who created the PO.  
  
**Step 1:** Create a Report Set and include your report.  
Business Process Automation > Reporting > Report Manager > Report Set Manager  
You may add multiple report to the report set as required.  
  
**Step 2:** Create a SHIPMENT agent that listens to 'SHIPMENT - STATUS CHANGED' event with restriction as SECURE RESOURCES_ACCEPTED. In this agent use standard action:  
**PRINT DOCUMENT:** In this action specify the name of the Report Set(from Step 1) and output format(say PDF).  
  
**Step 3:** Now in the application, when a tender is accepted on the shipment, PRINT DOCUMENT action generates the report. OTM application will raise an event REPORT-READY(standard OTM event) for the REPORT generated. So you can create a 'REPORT' agent that listens to this event with event restriction having report set name(from step 1). In this agent, you can have following actions:  
  
**Action 1:**  
ASSIGN VARIABLE with below SQL to fetch the user who created the PO:  
select max (ob.insert_user)  
from report_log_parameter rlp,  
view_shipment_order_release vsor,  
order_release orl,  
ob_order_base ob  
where file_name = $gid  
and parameter_name = 'P_SHIPMENT_ID'  
and parameter_value = vsor.shipment_gid  
and vsor.order_release_gid = orl.order_release_gid  
and orl.order_base_gid = ob.order_base_gid  
  
Note that REPORT_LOG_PARAMETER table has log of input parameter values and in this example we are fetching Shipment ID input parameter run time value and going to related PO details using that Shipment ID.  
  
You may need to create a new report definition for e-mail purposes because report definition with multiple other parameters apart from Shipment ID did not work for me. More analysis not done on this issue at this point.  
  
**Action 2:** Use NOTIFY CONTACT action with:  

  1. Contact value as variable(from Action 1 above) 
  2. Communication Method = EMAIL. You can create Contact(Business Process Automation> Communication Management > Contacts) with Contact ID same as User ID for all the users who have PO Create access and wish to receive emails. On the contact record ensure flag 'Notification On' is checked.
  3. Subject with $GID or other required variable for dynamic display like: "Report - ShpRef#: $SHP_REF; SID=$GID"
  **4. Stylesheet profile with below settings:** Business Process Automation > Power Data > Event Management > Stylesheet Profiles:

  * Template Name = workflow/DefaultReportEventHtml.xsl(Standard)
  * Format = text/html
  * Subject Property Key = {2}. This will ensure that subject for e-mail will be as per the definition mentioned in the NOTIFY CONTACT.
  * Message direction =OUTBOUND
  * Type=XSL
  * Attachments=EMBED