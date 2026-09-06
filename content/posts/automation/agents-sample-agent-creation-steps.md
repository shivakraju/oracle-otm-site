---
title: "Agents - Sample Agent Creation Steps"
date: 2016-08-05T19:33:00+00:00
draft: false
weight: 10
tags:
  - "Agent"
  - "Agent Actions"
  - "Error Handler"
aliases:
  - "/2016/08/agents-sample-agent-creation-steps.html"
keywords:
  - "Oracle OTM agent creation steps"
  - "OTM agent workflow configuration"
  - "Oracle OTM shipment agent setup"
  - "OTM agent event action configuration"
  - "Oracle OTM agent notify contact"
  - "OTM agent condition shipment volume"
  - "Oracle Transportation Management workflow agent"
  - "OTM agent error handler setup"
  - "Oracle OTM agent trigger shipment created"
  - "OTM business process automation agent"
description: "Step-by-step guide to creating an Oracle OTM agent, covering how to select the business object, choose the trigger event, define conditions, configure actions, and set up error handling."
url: "/posts/agents-sample-agent-creation-steps/"
---

Agents in OTM are workflow processes that listen to specific events happening in the system and trigger actions. They are similar to database triggers that execute code when DML events occur at the database layer.

**Example Requirement:** Send a notification to a specific user when a shipment is created from bulk plan with a total volume less than 100 cubic feet.

**High-level steps:**

1. Identify the business object — in this example, **Shipment**.
2. Identify the OTM event — in this example, **Shipment - Created**.
3. Identify the conditions that must be met — the shipment must be a bulk plan shipment and have volume less than 100 cubic feet.
4. Define the action — send a notification.
5. Define error handling actions.

---

**Step 1: Create a Saved Query**

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Queries > New</div>

In the Saved Query Manager screen, enter the following details:

- **User Query Name:** Use underscores to separate words. For this example: `IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100`
- **Object Type ID:** `SHIPMENT`
- **Domain Name:** Enter your domain, e.g., `XXX`
- Click **View/Define Query**

![](/images/agents-sample-agent-creation-s-img1-317e6ba7ab.png)

In the Saved Query Definition screen:

- Select the **Total Gross Volume** and **Bulk Plan ID** columns.
- Define conditions: Bulk Plan GID is not null AND Total Gross Volume is less than 100.
- Click **Finished**.

![](/images/agents-sample-agent-creation-s-img2-e16aa04f97.png)

---

**Step 2: Create a Saved Condition**

A saved query must be associated with a saved condition before it can be referenced from an agent.

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Conditions > New</div>

In the Saved Condition Manager screen:

- **Saved Condition ID:** `IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100` (use the same name as the query)
- **Object Type ID:** `SHIPMENT`
- **Domain Name:** `XXX`
- **Saved Query ID:** `IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100`
- Click **Save** against the saved query record, then click **Finished**.

![](/images/agents-sample-agent-creation-s-img3-803fa6d4be.png)

---

**Step 3: Create the Agent**

<div class="step-box">Business Process Automation > Agents and Milestones > New</div>

In the Agent Header screen:

- **Agent ID:** Give the agent a descriptive name.
- **Agent Type:** `SHIPMENT`
- **Domain Name:** `XXX`
- **Active:** Check this box when the agent is ready for use.
- **Agent Event:** `SHIPMENT – CREATED`
- **Restrictions:** Click the **I** icon to see restriction options (Integration, User, Internal). Select **User** to trigger only on actions performed manually within OTM.
- **Saved Condition:** `IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100`
- Click **View/Enter Actions**.

![](/images/agents-sample-agent-creation-s-img4-35620c6c02.png)

---

**Step 4: Define Agent Actions**

Click **Add Action** and select **Notify Contact**.

![](/images/agents-sample-agent-creation-s-img5-258e6777c8.png)

In the Notify Contact action:

- **Contact:** Select the user to notify — in this example, `ADMIN`.
- **Communication Method:** `MESSAGE CENTER` (or select Email depending on requirements).
- **Subject:** Write the notification message text.
- Click **Save**.
- Optionally click **Error Handler** to define actions that run if the agent fails — for example, sending an alert to the system administrator.
- Click **Finished**.

![](/images/agents-sample-agent-creation-s-img6-3b5e1ecabb.png)

---

**Review / Verify Results:**

Select an order release and bulk plan a shipment with volume less than 100 cubic feet. After the shipment is created, click **Refresh Messages** in the Message Center at the top of the screen.

<div class="note-box"><strong>Note:</strong> You must be logged in as the ADMIN user for the domain to see the message in Message Center.</div>

![](/images/agents-sample-agent-creation-s-img7-bfd56183da.png)
