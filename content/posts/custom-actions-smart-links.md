---
title: "Custom Actions & Smart Links"
date: 2018-09-21T20:38:00+00:00
draft: false
weight: 440
tags:
  - "Actions"
  - "Label"
  - "Action Definition ID"
  - "Smart Links"
aliases:
  - "/2018/09/custom-actions.html"
---

Actions  
This feature can be used to allow users to perform some actions like triggering an agent for a list of transactions.  
  
**Example scenario:** Trigger an INVOICE agent when user selects a custom action 'Reprocess Invoice' from the UI on the user selected list of invoices.  
  
**Below are the setups required:**  
  
Login as DBA.ADMIN to create a label.  
Configuration and Administration > User Configuration > Label Manager  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwCKT_MrUWjkeGliAlrZiFK1kihtsAQnfBg6OX8x0RiL-HYJ4Zj5Ds5O3DZAkIqkD4V4I9VOzX486od3K7OZwthbuH5_ntGALQwJKTaRpzcTksTtQNfK0uLwFc2JshMpGFOviEP8M6DoU/s400/Capture5.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwCKT_MrUWjkeGliAlrZiFK1kihtsAQnfBg6OX8x0RiL-HYJ4Zj5Ds5O3DZAkIqkD4V4I9VOzX486od3K7OZwthbuH5_ntGALQwJKTaRpzcTksTtQNfK0uLwFc2JshMpGFOviEP8M6DoU/s1600/Capture5.JPG)

  
Login to transactions domain as ADMIN now and create a custom action to call the agent.  
Configuration and Administration > User Configuration > Actions Manager  
**Enter below details:**  
Action = Give some name to the action  
Label=Give name of label created in earlier step  
Action Definition ID=RUN_AGENT_INVOICE  
Agent ID=Select the name of the agent that should trigger.  
  
**Note:** Here agent is being called by name rather than the event. So make sure if you are creating new version of the agent, you need to come back and update this custom action with new agent name.  
  
Now, as a final step - add this action to your screen set.  
Configuration and Administration > User Configuration > Screen set Manager > Query the screen set for which you need to add custom action > Go to 'Actions' tab > Select 'Top' on hierarchy list and click '+' button > Select 'Add Actions' > In the 'Actions' drop down you should see label you associated to the new action - select it > Save.  
  
**Test:**  
Open your custom manager layout and select few invoices > click 'Actions' button > Select the action label.  
  
This should trigger the agent on the invoices selected.  
  
Smart Links  
•Steps for creating Smart links are similar to creating Action.  
  
•In the screen set, there is tab ‘Smart Links’ next to ‘Actions’. You need to add the custom action here, so that it appears as smart link.  
  
•Difference between Smart links and actions:  
  
Actions can work on group of transactions. Say for example, you can select 10 order releases and bulk them together. Here Bulk Plan is defined as an action.  
Smart link will work on specific selected transaction. For example, you can select specific order release and say ‘Related Buy Shipment’. This will fetch list of shipments associated with that specific Order Release.