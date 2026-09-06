---
title: "Agents - Agent Event Restrictions"
date: 2016-08-15T16:53:00+00:00
draft: false
weight: 270
tags:
  - "Before Persist"
  - "Event Source"
  - "Agent Event Restrictions"
aliases:
  - "/2016/08/agents-agent-event-restrictions.html"
keywords:
  - "Oracle OTM agent event restrictions"
  - "OTM agent source INTEGRATION INTERNAL USER"
  - "Oracle OTM before persist agent validation"
  - "OTM agent event source restriction"
  - "Oracle OTM agent inbound XML validation"
  - "OTM before persist pre-commit validation"
  - "Oracle OTM agent trigger control"
  - "OTM agent GlogXML event source"
  - "Oracle Transportation Management agent event filter"
  - "OTM agent event restriction configuration"
description: "Explains Oracle OTM Agent Event Restrictions, covering the INTEGRATION, INTERNAL, and USER source options and the Before Persist setting for pre-commit validation of inbound XML transactions."
---

Agent Event Restrictions give you control over which types of transactions trigger an agent, and optionally allow you to validate inbound XML transactions before they are committed to the database.

Access this by clicking the **"i" icon** on the agent header screen:

![](/images/agents-agent-event-restriction-img1-3b832dd4b4.png)

The Event Restrictions panel appears:

![](/images/agents-agent-event-restriction-img2-1b611276a7.png)

**Source Options:**

<div class="field-box"><strong>INTEGRATION:</strong> Triggers the agent only when the business object (e.g., Order Release) is created by an inbound GlogXML transmission from an external system. Use this when you want agent logic to run only for XML-uploaded transactions.</div>

<div class="field-box"><strong>INTERNAL:</strong> Triggers the agent only when the business object is created by a standard OTM internal action, such as "RELEASE ORDER BASE". Use this when the agent should respond to system-generated events, not user or integration activity.</div>

<div class="field-box"><strong>USER:</strong> Triggers the agent only when the business object is manually entered by a user within the OTM application.</div>

**Before Persist:**

The **Before Persist** option allows validation of an inbound XML transaction before it is committed to the database.

**Example:** Validate that a required reference number exists in an inbound PO XML before creating the Order Base record. Suppose the integration layer sends OTM XML and you want to create the PO only if the reference number `SOURCE_SYSTEM` is present.

Create the following agent:

![](/images/agents-agent-event-restriction-img3-01d56efc28.png)

In the Restrictions section, check the **Before Persist** box:

![](/images/agents-agent-event-restriction-img4-70e039283f.png)

<div class="note-box"><strong>Note:</strong> Once Before Persist is selected, the list of actions available in the Agent Actions section changes. They will differ from the standard ORDER BASE – CREATED action set.</div>

![](/images/agents-agent-event-restriction-img5-6e13519067.png)

Set the following expression to check for the reference number in the XML:

```
#OB_REFNUM/OB_REFNUM_QUAL_GID<>DOMAIN.SOURCE_SYSTEM
```

If the `SOURCE_SYSTEM` reference number does not exist in the XML, the standard **DON'T PERSIST** action is triggered — meaning the PO is not created in OTM.

Upload a PO XML without the `SOURCE_SYSTEM` reference number. The transmission will show as PROCESSED, but no Order Base record will be created:

![](/images/agents-agent-event-restriction-img6-1279d97034.png)

If you repeat the upload with the reference number present, the Order Base record is created successfully. This feature is useful for enforcing data quality rules on transactions arriving from external systems.
