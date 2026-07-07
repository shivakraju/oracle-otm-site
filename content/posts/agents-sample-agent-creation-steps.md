---
title: "Agents - Sample Agent Creation Steps"
date: 2016-08-05T19:33:00+00:00
draft: false
weight: 260
tags:
  - "Agent"
  - "Agent Actions"
  - "Error Handler"
aliases:
  - "/2016/08/agents-sample-agent-creation-steps.html"
---

Agents in OTM are workflow processes that listen to specific events happening in the system and trigger actions. These are similar to database triggers that trigger code based on DML events occurring in the database layer.  
  
**Let us try to understand more with below example:**  
  
**Requirement:** Send a notification to specific user when shipment is created from bulk plan with total volume less than 100 cubic feet.  
  
For this, you need to follow below steps(high level):  
  
1\. Identify the business object on which Agent is to be created. In our example ‘Shipment’ is the business object.  
  
2\. Identify the event in OTM for which you want to define an action.  
In our example, ‘Shipment - Created’ is the event.  
  
3\. Identity the conditions (if any) that should be met for performing the Agent Actions.  
**In our example, following are the conditions:**  
Shipment should be a bulk plan shipment  
Shipment should have volume less than 100 cubic feet  
  
4\. Define actions to be performed.  
In our example, sending notification is the action.  
  
5\. Error Handling: Define error handling actions.  
  
**Steps in OTM application:**  
  
Create a Saved Condition 'IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100' as follows:  
  
**Navigation:** Business Process Automation -> Power Data -> Event Management -> Saved Queries -> New  
  

In the Saved Query Manager screen you enter following details:

  * User Query Name: Give some name to your query. Use underscore character to separate words in the name as a convention. In our example, we can give name as ‘IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100’.
  * Object Type ID: Give the name of entity (or business object) on which you want to base your query. In our example ‘SHIPMENT’ is the entity.
  * Give the domain name. In our example we are creating the query in ‘XXX’ domain.
  * Click on ‘View/Define Query’ button.

![](/images/agents-sample-agent-creation-s-img1-317e6ba7ab.png)  
  
  

In the Saved Query Definition screen you enter following details:

  * Column: You can select the columns of the entity on which you want to define conditions. In our example, we define conditions on Total Gross Volume and Bulk Plan ID columns of shipment. 
  * After selecting the column you can define the condition. In our example we can define conditions to check that Bulk Plan Gid is not null and Total Gross Volume is less than 100. Save the conditions.
  * Click on ‘Finished’ button to complete the definition.

  
![](/images/agents-sample-agent-creation-s-img2-e16aa04f97.png)  
  
Saved query must be associated with a Saved condition, so that it can referred from an agent.  
**Navigation:** Business Process Automation -> Power Data -> Event Management -> Saved Conditions -> New  
  
  

In the Saved Condition Manager screen you enter following details:

  * Saved Condition ID: As a convention, we give the same name as the query name that we have created in previou step. In our example, it is ‘IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100’
  * Object Type ID: Give the name of entity or business object on which you want to base your condition. In our example ‘SHIPMENT’ is the entity.
  * Give the domain name. In our example we are creating the query in ‘XXX’ domain.
  * Saved Query ID: Give the saved query name you want to associate to this condition. In our example it is ‘IS_BULK_SHIPMENT_HAS_VOL_LESS_THAN_100’. This is created in previous step.
  * Click on ‘Save’ button against this saved query record. 
  * Click on ‘Finished’ button to complete the definition.

![](/images/agents-sample-agent-creation-s-img3-803fa6d4be.png)  
  
**Now we can go ahead and create a new agent:**  
**Navigation:** Business Process Automation -> Agents and Milestones -> New  

In the Agent Header screen you enter following details:

  * Agent ID: Give a name to the agent as shown.
  * Agent Type : Give the name of entity or business object on which you want to base your agent. In our example ‘SHIPMENT’ is the entity.
  * Give the domain name. In our example we are creating the query in ‘XXX’ domain
  * Active Check box: Check this button to make this agent active once it is ready for use 
  * Agent Event: This is the triggering action for the agent. There are several standard events provided by OTM. In our example we select the standard event of ‘SHIPMENT – CREATED’.
  * Restrictions: Click on ‘I’ symbol and you will see restrictions such as ‘Integration’, ‘User’ , ‘Internal’ etc. These will control by whom this agent can be triggered. If we select ‘User’, it means that only actions done by user within the OTM system will trigger the event.
  * Saved condition : Give the saved condition defined earlier in order to restrict the shipments having volume less than 100 cubic feet.
  * Click on ‘View/Enter Actions’ button to defined actions.

![](/images/agents-sample-agent-creation-s-img4-35620c6c02.png)  
  

In the Agent Actions screen you enter following details:

Click on ‘Add Action’ button that appears after opening this screen. Select ‘Notify Contact’ as the action. Note that list appears for ‘Action’ column will contain many seeded actions provided by OTM.

  

![](/images/agents-sample-agent-creation-s-img5-258e6777c8.png)

In the Notify Contact action,

  * Select Contact for which notification has to be sent. In our example we have selection ‘ADMIN’ as the user.
  * Select ‘MESSAGE CENTER’ as communication method. Note that you can select other communication method such as ‘Email’ depending on the requirement.
  * Subject: Write the message you want to send to the contact upon the action. Refer slide to see the subject defined for our example scenario.
  * Save
  * You can click on ‘Error Handler’ button and define actions. An example for an error handling action can be to send a notification to system administrator. This action will be invoked every time agent has failed to process the actions defined in the Agent.
  * Click on ‘Finished’ button to complete the definition.

![](/images/agents-sample-agent-creation-s-img6-3b5e1ecabb.png)

  

**Review/Verify Results:**

  

Select an order release and bulk plan a shipment that can have volume < 100 cu ft.

After such shipment is created, click on the ‘Refresh Messages’ against the Message Center at the top of your screen. Note that you must have logged in as ‘ADMIN’ user for that domain in order to see the message.

![](/images/agents-sample-agent-creation-s-img7-bfd56183da.png)