---
title: "Saved Queries/Conditions"
date: 2016-07-20T21:30:00+00:00
draft: false
weight: 240
tags:
  - "User in Finder"
  - "OTM"
  - "Saved Condition"
  - "Saved Query"
aliases:
  - "/2016/07/saved-queriesconditions.html"
---

Saved Queries in OTM help to query specific records in a screen or add some conditions to your custom logic while creating an Agent, etc. They can be used in multiple other OTM features like recurring processes, business monitors etc.  
  
Below steps show how to create a simple Saved Query.  
  
If we need to find orders that have failed planning in OTM in this month, we can create a query as below:  
  
**Method1:** Simple Query from the UI using Order Release Finder Screen  
  
Order Management > Order Release> Order Release  
  
**Enter Search Criteria:**  
  
![](/images/saved-queriesconditions-img1-30bf48b186.png)  
  
![](/images/saved-queriesconditions-img2-13b34ec6ee.png)  
  
Click Save button and give a name to your query.  
  
![](/images/saved-queriesconditions-img3-5a733322dd.png)  
  
You will see this query appearing in the Saved Query drop down list as shown below:  
  
![](/images/saved-queriesconditions-img4-6c758e6dbc.png)  
  
Click 'Execute Query' button to see the results of the query.  
  
![](/images/saved-queriesconditions-img5-23908464dd.png)  
  
Please note that this query is saved in the application and can be executed any time.  
  
**You can review this query definition as below:**  
  
Business Process Automation > Power Data > Event Management > Saved Query  
  
![](/images/saved-queriesconditions-img6-8dd623a834.png)   
Enter the Query same that was provided earlier and 'Search'.  
  
Select the Query and 'Edit' to see the definition as below:  
  
  
  
  
![](/images/saved-queriesconditions-img7-0cf28abb2d.png)  
  
  
  
Note that 'Use in Finder' is checked for this query as this is created from the Finder Screen.   
  
![](/images/saved-queriesconditions-img8-9113c5fa7e.png)   
  
You will review the criteria you have added while defining the query.  
  
You can also create query directly from this screen and add necessary criteria.  
  
For example, if you want to add another criteria/condition that 'Indicator = Red', you can select 'Indicator' under Column drop down list. This will populate the possible list of value once you tab out of column. You can select 'Red' as value and 'Save'.   
  
![](/images/saved-queriesconditions-img9-37ea3c479b.png)  
  
This is a easy feature for functional consultants who are not familiar with SQL to write simple queries.  
  
**Method2:** If you need to write complex SQL queries using Joins with multiple other object types(like Order Release to Shipment) or use SQL built-in functions like SUM etc, then you need to use below method.  
  
**Example:** Check if an Order Release is split into multiple shipments while planning. This type of query/condition cannot be written from 'Finder Screen' criteria.   
  
**We need to write a SQL for this as below:**  
  
select orl.order_release_gid  
from order_release orl,  
view_shipment_order_release vsor  
where orl.order_release_gid = vsor.order_release_gid  
and orl.order_release_gid = $gid  
group by orl.order_release_gid  
having count(*) > 1   
  
Note that $gid is variable(primary key to identify order release) that is passed to query during execution time from the application. For example, if you use this query in 'ORDER RELEASE' agent, then Order Release GID will be passed during agent run-time.  
  
These type of queries are normally used in Agents, Recurring Processes, Business Monitors, etc.  
  
**We define these queries in the system as below:**  
  
Business Process Automation > Power Data > Event Management > Saved Queries  
  
![](/images/saved-queriesconditions-img10-4451a43d6a.png)  
  
Enter Query name, Object Type as 'ORDER RELEASE',Domain Name and click 'View/Define Query'  
  
![](/images/saved-queriesconditions-img11-ebad4cc20e.png)  
  
Copy the query without any ending semi colon(;) in the 'Check one SQL' and 'Find All SQL' fields as shown above, click 'Finished' button.  
  
If we need to use same query in an agent, we need to associate it to saved condition. Saved conditions are mostly used write IF condition logic in the Agents.  
  
Business Process Automation > Power Data > Event Management > Saved Condition > New:  
[](https://draft.blogger.com/blogger.g?blogID=581121661120046731)[](https://draft.blogger.com/blogger.g?blogID=581121661120046731)[](https://draft.blogger.com/blogger.g?blogID=581121661120046731)![](/images/saved-queriesconditions-img12-61e25779cc.png)   
  
Specify details as shown above to link Saved Query with Saved Condition.  
  
Saved Conditions will be true if all the Saved Queries mentioned in the list will return records.  
![](/images/saved-queriesconditions-img13-7fa6ba4dda.png)   
  
**Important Note:** While writing saved queries using SQL, ensure entire query is written in single line(no line breaks). Line breaks will cause issues when you try to export this to csv and try to load in another environment.