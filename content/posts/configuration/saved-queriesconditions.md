---
title: "Saved Queries/Conditions"
date: 2016-07-20T21:30:00+00:00
draft: false
weight: 5
tags:
  - "User in Finder"
  - "OTM"
  - "Saved Condition"
  - "Saved Query"
aliases:
  - "/2016/07/saved-queriesconditions.html"
keywords:
  - "Oracle OTM saved query configuration"
  - "OTM saved condition setup"
  - "Oracle OTM order release finder saved query"
  - "OTM saved query in agent condition"
  - "Oracle OTM business monitor saved query"
  - "OTM recurring process saved condition"
  - "Oracle Transportation Management query builder"
  - "OTM saved query SQL condition"
  - "Oracle OTM custom search criteria"
  - "OTM finder screen save query"
description: "Shows how to create and save queries in Oracle OTM using the Order Release Finder and custom SQL conditions, which can then be reused in agents, business monitors, and recurring processes."
url: "/posts/saved-queriesconditions/"
---

Saved Queries in OTM help to query specific records in a screen or add conditions to custom logic while creating an Agent or similar configuration. They can be reused across multiple OTM features including recurring processes and business monitors.

<div class="note-box"><strong>Start here — this is foundational:</strong> Saved Queries and Conditions are arguably the most important configuration concept in OTM for both UI customisation and automation. Almost every advanced OTM feature — Agents, Business Monitors, Recurring Processes, Action Checks, and custom Workbenches — requires a Saved Query or Condition to define <em>which records</em> the logic should act on. Without a solid grasp of how to build and reuse queries, you cannot effectively configure any of these features.<br><br>Beyond automation, Saved Queries power the everyday user experience: they let you build pre-filtered finder screens that surface only the records relevant to a specific role or workflow — for example, a shipment coordinator who should only see shipments in their region, or an approver who only sees invoices within their approval threshold. A well-designed set of Saved Queries is often the difference between an OTM implementation that users actually adopt and one they work around.<br><br>Invest time here before moving to Agents, Business Monitors, or any other automation topic. Every hour spent mastering Saved Queries will save you many hours of troubleshooting downstream.</div>

**Method 1: Simple Query from the UI using Order Release Finder Screen**

<div class="step-box">Order Management > Order Release > Order Release</div>

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

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Query</div>

![](/images/saved-queriesconditions-img6-8dd623a834.png)

Enter the Query name that was provided earlier and click 'Search'. Select the Query and 'Edit' to see the definition as below:

![](/images/saved-queriesconditions-img7-0cf28abb2d.png)

Note that 'Use in Finder' is checked for this query as this is created from the Finder Screen.

![](/images/saved-queriesconditions-img8-9113c5fa7e.png)

You will review the criteria you have added while defining the query.

You can also create query directly from this screen and add necessary criteria. For example, if you want to add another criteria/condition that 'Indicator = Red', you can select 'Indicator' under Column drop down list. This will populate the possible list of value once you tab out of column. You can select 'Red' as value and 'Save'.

![](/images/saved-queriesconditions-img9-37ea3c479b.png)

This is an easy feature for functional consultants who are not familiar with SQL to write simple queries.

**Method 2: Complex SQL Query**

If you need to write complex SQL queries using joins with multiple object types (like Order Release to Shipment) or SQL built-in functions like SUM, use the method below.

**Example:** Check if an Order Release is split into multiple shipments while planning. This type of query/condition cannot be written from the Finder Screen criteria.

```sql
select orl.order_release_gid
from order_release orl,
view_shipment_order_release vsor
where orl.order_release_gid = vsor.order_release_gid
and orl.order_release_gid = $gid
group by orl.order_release_gid
having count(*) > 1
```

Note that `$gid` is a variable (primary key to identify order release) that is passed to the query during execution time from the application. For example, if you use this query in an 'ORDER RELEASE' agent, then Order Release GID will be passed during agent run-time.

These types of queries are normally used in Agents, Recurring Processes, Business Monitors, etc.

**We define these queries in the system as below:**

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Queries</div>

![](/images/saved-queriesconditions-img10-4451a43d6a.png)

<div class="field-box"><strong>Query Name:</strong> Enter a unique query name</div>
<div class="field-box"><strong>Object Type:</strong> ORDER RELEASE</div>
<div class="field-box"><strong>Domain Name:</strong> Enter domain name</div>

Click 'View/Define Query'. Copy the query without any ending semicolon (`;`) in the 'Check one SQL' and 'Find All SQL' fields as shown above, then click 'Finished'.

![](/images/saved-queriesconditions-img11-ebad4cc20e.png)

If you need to use the same query in an agent, associate it to a saved condition. Saved conditions are mostly used to write IF condition logic in Agents.

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Condition > New</div>

![](/images/saved-queriesconditions-img12-61e25779cc.png)

Specify details as shown above to link the Saved Query with a Saved Condition. Saved Conditions will be true if all the Saved Queries in the list return records.

![](/images/saved-queriesconditions-img13-7fa6ba4dda.png)

<div class="note-box"><strong>Note:</strong> While writing saved queries using SQL, ensure the entire query is written in a single line with no line breaks. Line breaks will cause issues when you try to export the query to CSV and load it in another environment.</div>
