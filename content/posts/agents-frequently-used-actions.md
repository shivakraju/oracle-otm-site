---
title: "Agents - Frequently Used Actions"
date: 2016-08-05T20:29:00+00:00
draft: false
weight: 250
tags:
  - "CALL"
  - "DATA TYPE ASSOCIATIONS"
  - "DIRECT SQL UPDATE"
  - "RAISE EVENT"
aliases:
  - "/2016/08/agents-frequently-used-actions.html"
---

DIRECT SQL UPDATE  

  

This is very useful action in writing a DML statement or to call an PLSQL procedure.

While using the Action, there are specific formats for DML statements or calling Procedures:

  

**Insert Statement format:**

  

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

**Update Statement format:**

  

UPDATE SHIP_UNIT SU  
SET su.transport_handling_unit_gid = 'EXPORT'  
WHERE EXISTS  
(SELECT 1  
FROM ORDER_RELEASE_LINE ORL, ship_unit_line sul  
WHERE ORL.ORDER_RELEASE_GID = $GID  
AND SUL.SHIP_UNIT_GID = SU.SHIP_UNIT_GID  
AND sul.order_release_line_gid = orl.order_release_line_gid)

  

  

**Stored Procedure Calls:**

  

CALL xxotm_agent_pkg.update_ebs_fsu($gid)

  

For Oracle Stored Procedure to be accessible by OTM agent, we need to create a PUBLIC synonym for the procedure that you define in GLOGOWNER schema.

  
CREATE OR REPLACE PUBLIC SYNONYM xxotm_agent_pkg FOR glogowner.xxotm_agent_pkg;   
  
**Note:** Synonym is not required if you are making a call to the stored procedure along with the schema name. Example : CALL glogowner.xxotm_agent_pkg.update_ebs_fsu($gid)

  

**Direct SQL Update Tips:**

  

  * While using statement type as stored procedure, ensure refresh cache is not 'DML Returing' which is default value.
  * SQL Description - always write small description for the DSU action so that agent is readable.

  

ASSIGN VARIABLE

  

This is used in agents to declare a variable and associate a SQL statement to the variable.

For example, following agent reads status of order release and sets the indicator color appropriately:

  

![](/images/agents-frequently-used-actions-img1-1be557884e.png)

  

![](/images/agents-frequently-used-actions-img2-ae374fffe2.png)

**Query SQL:**

SELECT NVL(STATUS_VALUE_XID,'X')  
FROM ORDER_RELEASE_STATUS ORS, STATUS_VALUE SV, STATUS_TYPE ST  
WHERE SV.STATUS_VALUE_GID = ORS.STATUS_VALUE_GID  
AND ST.STATUS_TYPE_GID = ORS.STATUS_TYPE_GID  
AND ST.STATUS_TYPE_XID = 'PLANNING'  
AND ORS.ORDER_RELEASE_GID = $gid

  

**Note:** SQL associated with assign variable should always have NVL handling. If SQL doesn’t return a value, agent will fail at that point.

  

Variables used in Parent Agent can be accessed from child agent

  
**Agent Variables:**  
Refer Topic ‘Agent Variables’ in OTM Help for variables like $gid.  
**Examples:**   
$gid variable refers to current object ID on which agent is triggered like Order Release GID for Order Release agent, Shipment GID for shipment agent, etc.$event_gid variable: Say, if we have an agent already created in OTM that triggers on ORDER - CREATED and ORDER - MODIFIED events, and if we want to add some action specific to ORDER – CREATED event , use $EVENT_GID which is standard variable provided by OTM.  
  
  

RAISE EVENT ACTION

This is used to trigger one agent from another agent.

  

**Example:** If we have 5 agents based on ORDER - CREATED event for different business process flows and if we need to perform activities common to all the processes, in this scenario we follow these steps:

Business Process Automation > Power Data > Event Management > Agent Events  
**Define a custom agent event:**  
  
![](/images/agents-frequently-used-actions-img3-ea95a9fb7c.png)   
  
  

Define an agent based on this custom event as shown:

  
![](/images/agents-frequently-used-actions-img4-dd0af676bc.png)   
  
  

You can call this agent now from another agent using RAISE EVENT as shown below:

  
![](/images/agents-frequently-used-actions-img5-a862c3a8db.png)   
  
  

DATA TYPE ASSOCIATIONS   
**Example:** Set Order Release Status to Executed, when corresponding Shipment is in Accepted status.

This requires updating order release status when shipment agent is running. In such cases use Data Type Associations as follows:  
  
![](/images/agents-frequently-used-actions-img6-a48947db2e.png)   
Above screen shot shows SHIPMENT AGENT action that updates status on all corresponding order releases.  
  

When using a Data Type Association to run an agent action against related objects, “Create New Process” checkbox appears. If selected, the related action runs in a separate workflow process. The initial agent does not wait for the related object actions to complete. This provides you a way to avoid potential deadlock when raising custom events.  
  
FOR EACH  

This is used from any agent to repeat a custom event on related objects.   
**Example:** From a shipment agent, you want to identify specific order release based on some saved query and perform some custom action on each of these order releases. In this case define a saved query and condition to identify those order releases, define a custom agent(listening to custom event) with the set of actions that you want to perform on these order releases. Call this event for those order releases using FOR-EACH.  
**Note:** For performing standard events on related objects, note that you can use DATA TYPE ASSOCIATION.  
  
IF, ESLE, ESLEIF, END IF  
These are condition actions provided by OTM to control the agent action flow as required.IF and ELSEIF should be associated with saved conditions and this action would return either true or false based on either saved condition returns rows or not.

Complex Expression

In the IF conditions, you can use complex expressions if you have multiple individual conditions to be combined with a logical AND or OR operators.   
  
SCHEDULE EVENT 

  

**Usage:** Alternate to WAIT logic

  

**Example:** Say we need to ensure that a particular action in an agent is triggered only after a record exists in particular table and if we are not aware of the time when this record would be available in the DB. In this case, using WAIT will not work as we might not be aware of exactly how much time to WAIT. So create an IF condition checking if record that we are looking is existing or not. If record is not existing call the same agent again after 2 mins using this action.To call the same agent, create a custom event and trigger the custom event in the above IF block. Add the custom event to existing agent. In the IF block use STOP so that no further processing happens in the agent.If the IF condition fails – meaning record not exists – we can write further processing logic after the IF block.  

  
BUILD SHIPMENT   
This is used in ORDER RELEASE agent to plan the order and create a shipment. In this action you need to specify the perspective('B' for Buy, etc) and parameter set value.  
  
RELEASE ORDER BASE  
This is used in ORDER BASE agent to release the instructions associated with that Order Base(PO) to create Order Release transactions.  
  
LINK SHIPMENT TO ORDER BASE  
From Shipment Agent, we can use this action to link related Order Bases to Shipment. As a pre-req we need to ensure:   

  * Corresponding Order Bases(PO) are released - Order Releases exist
  * Shipment Ship Unit Line qualifier 'CIN' value should match to Order Base(PO Number)

  
SEND INTEGRATION  
This is used from any agent to send object XML to an external system.   
  
SET STATUS  
This is used in any agent to set internal status values for current object.   
  
STOP  
This is used to stop the workflow at that point based on some condition. Please note that no further agent actions will be executed once a STOP action is encountered.  
  
NOTIFY CONTACT  
This is used in any agent to send notification to already defined contact in the system(like E-mail, etc)  
  
AUTO MATCH INVOICE  
On Invoice Agent, this will trigger the match rule defined for the carrier sending this invoice.  
  
INVOICE - AUTO APPROVE, REJECT INVOICE  
These actions on invoice agent are used to approve/reject that particular invoice transaction.  
  
DIVERT SHIPMENT  
This action on a shipment is used to change destination location on the shipment and re-rate the shipment.  
  
SET INDICATOR  
This action on any agent is used to set indicator status to Red, Green, White or Yellow. Usually R is used to indicate transaction failure, Green for success, White for New status and Yellow for Warning status.