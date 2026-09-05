---
title: "Business Process Automation Data Structure"
date: 2016-05-06T20:15:00+00:00
draft: false
weight: 140
tags:
  - "Agent"
  - "Reports"
  - "Integration"
  - "Contacts"
  - "External System"
aliases:
  - "/2016/05/business-process-automation-data.html"
keywords:
  - "Oracle OTM business process automation data structure"
  - "OTM contacts external system tables"
  - "Oracle OTM CONTACT table"
  - "OTM external system outbound XML"
  - "Oracle OTM agent workflow data model"
  - "OTM CONTACT_COM_METHOD table"
  - "Oracle OTM BPA module configuration"
  - "OTM integration contacts setup"
  - "Oracle Transportation Management automation tables"
  - "OTM notify contact agent action"
  - "Oracle OTM reports data structure"
description: "Describes the Oracle OTM Business Process Automation data structures, including Contacts, External Systems, Agent configurations, Reports, and Integration transmission tables."
---

The Business Process Automation (BPA) module handles the technical configuration layer of OTM — workflows, notifications, outbound integrations, reports, and transmission logging. The tables below are useful when troubleshooting agent behaviour, auditing integration traffic, or diagnosing report failures.

**Contacts:**

A Contact in OTM defines a communication endpoint — an email address, fax number, or integration URL — that OTM can reach when sending notifications or outbound data. Contacts can be associated with:

<div class="field-box"><strong>Users</strong> — to notify OTM users by email on business events.</div>

<div class="field-box"><strong>External Systems</strong> — to route outbound XML transmissions to middleware or third-party systems.</div>

<div class="field-box"><strong>Locations, Service Providers, Involved Parties</strong> — for carrier or partner notifications.</div>

<div class="field-box"><strong>Agent Notify Contact actions</strong> — triggered automatically by OTM Agents on business events.</div>

**Contact tables:**

<div class="field-box"><strong>CONTACT</strong> — Contact record with name and type.</div>

<div class="field-box"><strong>CONTACT_COM_METHOD</strong> — Communication method linked to the contact — stores the actual email address, URL, or fax number and the communication type (EMAIL, HTTP, FAX, etc.).</div>

**External System:**

An External System defines an outbound destination — typically a middleware platform (Oracle SOA, MuleSoft, webMethods) or any system that receives GlogXML transmissions from OTM. An Out XML Profile is associated to control which fields are included in the outbound XML.

<div class="field-box"><strong>EXTERNAL_SYSTEM</strong> — External System record with name, URL, credentials, and transport method.</div>

<div class="field-box"><strong>EXTERNAL_SYSTEM_OUT_XML</strong> — Links the External System to its Out XML Profile, controlling the shape of the outbound XML payload.</div>

**Agents:**

Agents are OTM's workflow engine — event-driven rules that trigger actions automatically when business events occur (e.g. ORDER CREATED, SHIPMENT TENDERED, STATUS UPDATED). Agents can use standard OTM events or custom events defined by developers. They are covered in detail in the [Agents](/posts/agents-frequently-used-actions/) topic.

**Agent tables:**

<div class="field-box"><strong>AGENT</strong> — Agent header with name, description, active flag, and triggering event.</div>

<div class="field-box"><strong>AGENT_ACTION</strong> — Actions to execute when the agent fires (e.g. Send Interface Transmission, Notify Contact, Raise Event).</div>

<div class="field-box"><strong>AGENT_ACTION_DETAILS</strong> — Parameters for each action — this is where the actual agent code and configuration lives.</div>

<div class="field-box"><strong>AGENT_EVENT</strong> — Events that trigger the agent.</div>

<div class="field-box"><strong>AGENT_EVENT_DETAILS</strong> — Conditions and filters on the triggering event.</div>

**Sample query — search for specific text within agent action parameters:**

```sql
SELECT aad.*
FROM   agent_action_details aad,
       agent ag
WHERE  UPPER(aad.action_parameters) LIKE UPPER('%TEXT TO SEARCH%')
AND    aad.agent_gid = ag.agent_gid
AND    ag.is_active = 'Y'
```

**Sample query — find all active agents that raise a specific custom event:**

```sql
SELECT a.agent_gid,
       a.description,
       aad.action_sequence
FROM   agent a,
       agent_action_details aad
WHERE  a.agent_gid = aad.agent_gid
AND    a.is_active = 'Y'
AND    aad.agent_action_gid IN ('RAISE EVENT', 'FOR EACH')
AND    aad.action_parameters LIKE '%custom event text%'
```

**Reports:**

OTM reports are built using SQL and BI Publisher. Report development is covered in detail in the [Report Development](/posts/report-development-sample-report/) topic.

<div class="note-box"><strong>Note:</strong> All report tables exist in the REPORTOWNER schema. They are also accessible from the GLOGOWNER schema under the same names because OTM creates public synonyms for them.</div>

**Report tables:**

<div class="field-box"><strong>REPORT</strong> — Report definition record with name, query, and output format.</div>

<div class="field-box"><strong>REPORT_PARAMETER</strong> — Input parameters defined for the report (e.g. shipment ID, date range).</div>

<div class="field-box"><strong>REPORT_SET</strong> — Groups related reports together. Used in Agent actions like PRINT DOCUMENT.</div>

<div class="field-box"><strong>REPORT_SET_DETAIL</strong> — Individual report entries within a Report Set.</div>

<div class="field-box"><strong>REPORT_LOG</strong> — Execution log for each report run — stores output file name, run status, and timestamp.</div>

<div class="field-box"><strong>REPORT_LOG_PARAMETER</strong> — Input parameter values used for a specific report run.</div>

**Sample query — find the Shipment ID from a report output file name:**

```sql
SELECT rlp.parameter_value
FROM   report_log_parameter rlp
WHERE  rlp.file_name      = '<output file name>'
AND    rlp.parameter_name = 'P_SHIPMENT_ID'
```

**Integration:**

Every inbound and outbound transmission in OTM is logged in the integration tables — including the raw XML, processing status, and any error details. These tables are the first place to look when troubleshooting a failed transmission.

<div class="field-box"><strong>I_TRANSMISSION</strong> — Transmission header. Stores status, direction (inbound/outbound), external system name, and timestamps.</div>

<div class="field-box"><strong>I_TRANSACTION</strong> — Transaction detail at the object level. Holds the raw XML payload and the GlogXML element name (e.g. TransOrder, OrderRelease, ShipmentStatus).</div>

<div class="field-box"><strong>I_LOG</strong> — Error log for failed transactions. Contains the error message text for each failed I_TRANSACTION row.</div>

**Sample query — fetch error details for a failed transmission:**

```sql
SELECT it.i_transmission_no,
       il.i_transaction_no,
       DBMS_LOB.SUBSTR(il.i_message_text, 200) AS error_message
FROM   i_transaction it,
       i_log il
WHERE  it.insert_date      > SYSDATE - 1
AND    it.i_transmission_no = <Enter Transmission No>
AND    it.element_name      = 'ShipmentStatus'
AND    it.transaction_code  = 'I'
AND    it.status            = 'ERROR'
AND    it.i_transaction_no  = il.i_transaction_no
```

**What's Next:**

The next topic covers Basic OTM Configurations — starting with Domain Items, Locations, and Equipment Groups — the foundational setup every OTM implementation requires before planning and tendering can begin.

Next Topic: [Basic OTM Configurations — Domain Items, Locations and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)
