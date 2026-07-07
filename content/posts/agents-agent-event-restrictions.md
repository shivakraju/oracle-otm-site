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
---

In Agents, "Event Restrictions" give us more control on what type of transactions agent should be triggered and also perform some pre- transaction commit validations(if required) on inbound XML transactions.  
  
We can access this by clicking the "i" icon as show below:  
![](/images/agents-agent-event-restriction-img1-3b832dd4b4.png)  
  
**You will see below options:**   
  
![](/images/agents-agent-event-restriction-img2-1b611276a7.png)  
  
**Source:** You select this value based on below requirements(Order Release examples discussed)  
  
**INTEGRATION:** If you are receiving Order Release transaction from an external system via GlogXML element and if you want your Agent logic to trigger only for this type of transactions, you select 'INTEGRATION' as the source. Only Order Releases uploaded to OTM via XMLs will trigger this agent.  
  
**INTERNAL:** If you want to trigger your agent logic only when Order Release is created by standard OTM internal actions like "RELEASE ORDER BASE", you use this source as INTERNAL.  
  
**USER:** If you want to trigger your agent logic only when Order Release is manually keyed-in by user within OTM system, we use this source.  
  

**Before Persist:** We can use this option to perform some validations on the inbound XML, before committing the transaction to database.   
  
**Example Usage:** Validate some elements/data in the input PO xml before committing (creating) PO in the OTM DB/application.   
Suppose that, integration layer is generating OTM XML and you want to ensure you create PO only if following reference number ‘SOURCE_SYSTEM’ exists - you can do following:  
  
**Create below agent:** 

  
![](/images/agents-agent-event-restriction-img3-01d56efc28.png)  
  
In the Restrictions section, “Check” Before Persist box as shown below:  
![](/images/agents-agent-event-restriction-img4-70e039283f.png)  
  
  
Note that once you select ‘Before Persist’, list of actions that appear in the Agent-Actions will vary. They will not be same as standard set of ORDER BASE – CREATED actions.  
![](/images/agents-agent-event-restriction-img5-6e13519067.png)  
  
  
**Expression:** #OB_REFNUM/OB_REFNUM_QUAL_GID<>DOMAIN.SOURCE_SYSTEM  
  
By using this expression we are checking if source system refnum exists in the XML and if refnum is not existing, we are using standard action ‘DON'T PERSIST’ meaning don’t commit/CREATE the PO.  
  
Now upload PO XML, by ensuring we don’t have the refnum SOURCE_SYSTEM.  
You will see the transmission in PROCESSED state,but Order Base record is not created in the system.  
  
![](/images/agents-agent-event-restriction-img6-1279d97034.png)   

If you repeat this case by adding the refnum, Order Base record would be created.  
So this feature might be used to perform some custom validations on the data coming from other systems to OTM.