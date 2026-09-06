---
title: "Agents - Frequently Used Actions"
date: 2016-08-05T20:29:00+00:00
draft: false
weight: 30
tags:
  - "CALL"
  - "DATA TYPE ASSOCIATIONS"
  - "DIRECT SQL UPDATE"
  - "RAISE EVENT"
aliases:
  - "/2016/08/agents-frequently-used-actions.html"
keywords:
  - "Oracle OTM agent actions list"
  - "OTM agent direct SQL update action"
  - "Oracle OTM RAISE EVENT agent action"
  - "OTM agent CALL action PLSQL"
  - "Oracle OTM DATA TYPE ASSOCIATIONS agent"
  - "OTM agent insert statement format"
  - "Oracle OTM agent SQL DML action"
  - "OTM agent assign variable action"
  - "Oracle Transportation Management agent action types"
  - "OTM agent PLSQL procedure call"
description: "Reference guide to frequently used Oracle OTM agent actions including Direct SQL Update, Raise Event, Call (PLSQL), and Data Type Associations, with syntax examples for DML statements and procedure calls."
url: "/posts/agents-frequently-used-actions/"
---

This page covers the most commonly used Oracle OTM agent actions, with syntax examples and usage notes for each.

**DIRECT SQL UPDATE**

This action is used to execute a DML statement or call a PL/SQL procedure from within an agent.

**Insert Statement format:**

```sql
INSERT INTO order_release_refnum (order_release_gid,
ORDER_RELEASE_REFNUM_QUAL_GID,
ORDER_RELEASE_REFNUM_VALUE,
DOMAIN_NAME)
SELECT orr.order_release_gid,
'SO_NUM',
orlr.orl_refnum_value,
orlr.domain_name
FROM order_release orr,
order_release_line orl,
order_release_line_refnum orlr
WHERE orr.order_release_gid = orl.order_release_gid
AND orl.order_release_line_gid = orlr.order_release_line_gid
AND orlr.ORDER_RELEASE_REFNUM_QUAL_GID = 'SO_NUM'
AND ROWNUM = 1
AND NOT EXISTS
(SELECT 1
FROM order_release_refnum oref
WHERE oref.order_release_gid =
orr.order_release_gid
AND oref.order_release_refnum_qual_gid =
'SO_NUM')
AND orr.order_release_gid = $gid
```

**Update Statement format:**

```sql
UPDATE SHIP_UNIT SU
SET su.transport_handling_unit_gid = 'EXPORT'
WHERE EXISTS
(SELECT 1
FROM ORDER_RELEASE_LINE ORL, ship_unit_line sul
WHERE ORL.ORDER_RELEASE_GID = $GID
AND SUL.SHIP_UNIT_GID = SU.SHIP_UNIT_GID
AND sul.order_release_line_gid = orl.order_release_line_gid)
```

**Stored Procedure Calls:**

```sql
CALL xxotm_agent_pkg.update_ebs_fsu($gid)
```

For an Oracle stored procedure to be accessible by an OTM agent, create a PUBLIC synonym for the procedure defined in the GLOGOWNER schema:

```sql
CREATE OR REPLACE PUBLIC SYNONYM xxotm_agent_pkg FOR glogowner.xxotm_agent_pkg;
```

<div class="note-box"><strong>Note:</strong> A synonym is not required if you call the stored procedure with the schema name explicitly, for example: <code>CALL glogowner.xxotm_agent_pkg.update_ebs_fsu($gid)</code></div>

**Direct SQL Update Tips:**

- When using statement type as stored procedure, ensure the Refresh Cache setting is not set to **DML Returning** (which is the default value).
- Always write a short description in the SQL Description field so the agent remains readable.

---

**ASSIGN VARIABLE**

This action declares a variable and associates a SQL query to populate it. For example, the following agent reads the planning status of an order release and sets the indicator color accordingly:

![](/images/agents-frequently-used-actions-img1-1be557884e.png)

![](/images/agents-frequently-used-actions-img2-ae374fffe2.png)

**Query SQL:**

```sql
SELECT NVL(STATUS_VALUE_XID,'X')
FROM ORDER_RELEASE_STATUS ORS, STATUS_VALUE SV, STATUS_TYPE ST
WHERE SV.STATUS_VALUE_GID = ORS.STATUS_VALUE_GID
AND ST.STATUS_TYPE_GID = ORS.STATUS_TYPE_GID
AND ST.STATUS_TYPE_XID = 'PLANNING'
AND ORS.ORDER_RELEASE_GID = $gid
```

<div class="note-box"><strong>Note:</strong> The SQL associated with Assign Variable must always include NVL handling. If the SQL returns no value, the agent will fail at that point.</div>

Variables declared in a parent agent can be accessed from a child agent.

**Agent Variables:**

Refer to the topic "Agent Variables" in OTM Help for built-in variables such as `$gid`.

- `$gid` refers to the current object ID on which the agent is triggered — for example, Order Release GID for an Order Release agent, or Shipment GID for a Shipment agent.
- `$event_gid` — if an agent listens to both ORDER - CREATED and ORDER - MODIFIED events and you need an action specific to ORDER - CREATED only, use `$EVENT_GID` to distinguish between the two.

---

**RAISE EVENT ACTION**

This action triggers one agent from within another agent.

**Example:** If you have 5 agents triggered by ORDER - CREATED for different business process flows, and several common actions need to run for all 5, define a shared custom agent event and call it from each agent using RAISE EVENT.

<div class="step-box">Business Process Automation > Power Data > Event Management > Agent Events</div>

Define a custom agent event:

![](/images/agents-frequently-used-actions-img3-ea95a9fb7c.png)

Define an agent based on this custom event:

![](/images/agents-frequently-used-actions-img4-dd0af676bc.png)

Call this agent from another agent using RAISE EVENT:

![](/images/agents-frequently-used-actions-img5-a862c3a8db.png)

---

**DATA TYPE ASSOCIATIONS**

**Example:** Set Order Release Status to Executed when the corresponding Shipment reaches Accepted status. This requires updating the order release from within a shipment agent. Use Data Type Associations for cross-object updates.

![](/images/agents-frequently-used-actions-img6-a48947db2e.png)

The screenshot above shows a Shipment agent action that updates the status on all corresponding order releases.

<div class="note-box"><strong>Note:</strong> When using a Data Type Association to run an agent action against related objects, a <strong>Create New Process</strong> checkbox appears. If selected, the related action runs in a separate workflow process and the initial agent does not wait for completion. Use this to avoid potential deadlocks when raising custom events.</div>

---

**FOR EACH**

This action repeats a custom event on a set of related objects from within any agent.

**Example:** From a shipment agent, identify specific order releases via a saved query and perform a custom action on each. Define a saved query to identify the target order releases, define a custom agent listening to a custom event with the desired actions, then call that event for each result using FOR EACH.

<div class="note-box"><strong>Note:</strong> For performing standard events on related objects, use DATA TYPE ASSOCIATION instead of FOR EACH.</div>

---

**IF, ELSE, ELSEIF, END IF**

These are conditional flow-control actions provided by OTM. IF and ELSEIF must be associated with saved conditions. The action evaluates to true or false based on whether the saved condition returns rows.

**Complex Expression:** In IF conditions, you can combine multiple individual conditions using logical AND or OR operators.

---

**SCHEDULE EVENT**

**Usage:** An alternative to WAIT logic when the wait duration is unknown.

**Example:** If an agent action should only run after a specific record exists in a table, but you do not know when that record will be available, a WAIT with a fixed duration will not work. Instead:

1. Create an IF condition that checks whether the required record exists.
2. If the record does not exist, use SCHEDULE EVENT to call the same agent again after 2 minutes (via a custom event).
3. Add a STOP action inside the IF block so no further processing occurs in the current run.
4. If the IF condition fails (record not found), the further processing logic after the IF block handles it.

---

**BUILD SHIPMENT**

Used in an ORDER RELEASE agent to plan the order and create a shipment. You must specify the perspective (e.g., `B` for Buy) and the parameter set value.

---

**RELEASE ORDER BASE**

Used in an ORDER BASE agent to release the instructions associated with that Order Base (PO) and create Order Release transactions.

---

**LINK SHIPMENT TO ORDER BASE**

From a Shipment agent, links related Order Bases to the shipment. Prerequisites:

- Corresponding Order Bases (POs) must already be released — Order Releases must exist.
- The Shipment Ship Unit Line qualifier **CIN** value must match the Order Base (PO Number).

---

**SEND INTEGRATION**

Used from any agent to send the object XML to an external system.

---

**SET STATUS**

Used in any agent to set internal status values for the current object.

---

**STOP**

Stops the agent workflow at that point, based on a condition. No further agent actions are executed after STOP is encountered.

---

**NOTIFY CONTACT**

Used in any agent to send a notification to a defined contact in the system (such as an email or message center notification).

---

**AUTO MATCH INVOICE**

On an Invoice agent, triggers the match rule defined for the carrier sending the invoice.

---

**INVOICE - AUTO APPROVE / REJECT INVOICE**

These Invoice agent actions are used to approve or reject a particular invoice transaction.

---

**DIVERT SHIPMENT**

Used on a Shipment agent to change the destination location on the shipment and re-rate it.

---

**SET INDICATOR**

Used in any agent to set an indicator status to Red, Green, White, or Yellow. Typically: Red for failure, Green for success, White for new/unprocessed, Yellow for warning.
