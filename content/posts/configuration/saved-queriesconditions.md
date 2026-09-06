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

**Type 1: User in Finder Query**

A User in Finder query is a search criteria set saved directly from a Finder screen (such as Order Release, Shipment, or Invoice). OTM stores the criteria you enter on a Finder screen and lets you replay it instantly from a dropdown — no SQL required. This is the right starting point for functional consultants who need to build pre-filtered views for end users without writing code.

<div class="step-box">Order Management > Order Release > Order Release</div>

Enter your search criteria on the Finder screen:

![Order Release Finder screen with search criteria entered](/images/saved-queriesconditions-img1-30bf48b186.png)

![Finder screen showing additional criteria fields populated](/images/saved-queriesconditions-img2-13b34ec6ee.png)

Click **Save** and give the query a name:

![Save Query dialog with query name field](/images/saved-queriesconditions-img3-5a733322dd.png)

The saved query now appears in the Saved Query dropdown on the Finder screen:

![Finder screen showing the saved query in the dropdown list](/images/saved-queriesconditions-img4-6c758e6dbc.png)

Click **Execute Query** to run it and see results:

![Finder screen showing results after executing the saved query](/images/saved-queriesconditions-img5-23908464dd.png)

The query is stored in the system and can be re-executed at any time. To inspect or edit the query definition:

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Query</div>

![Saved Query search screen](/images/saved-queriesconditions-img6-8dd623a834.png)

Search for the query by name, then select and edit it:

![Saved Query definition screen showing criteria](/images/saved-queriesconditions-img7-0cf28abb2d.png)

Notice that **Use in Finder** is checked — this flag is set automatically when a query is created from a Finder screen. It controls whether the query appears in the Finder screen dropdown.

![Saved Query showing Use in Finder checkbox checked](/images/saved-queriesconditions-img8-9113c5fa7e.png)

You can also add further criteria directly here — for example, adding **Indicator = Red** by selecting the Indicator column, choosing Red as the value, and saving:

![Saved Query editor with Indicator = Red criteria added](/images/saved-queriesconditions-img9-37ea3c479b.png)

**Type 2: Saved Query (SQL-Based)**

A Saved Query defined with custom SQL lets you express logic that the Finder screen criteria builder cannot — multi-table joins, aggregates, subqueries, and runtime variables. This is the primary query type used in automation: Agents, Business Monitors, Recurring Processes, and Action Checks all reference Saved Queries to identify which records to act on. The query receives the record's primary key (GID) as a runtime variable from OTM, so it always evaluates against the specific object being processed.

**Example:** Check whether an Order Release has been split across multiple shipments during planning — something that cannot be expressed as Finder screen criteria:

```sql
select orl.order_release_gid
from order_release orl,
view_shipment_order_release vsor
where orl.order_release_gid = vsor.order_release_gid
and orl.order_release_gid = $gid
group by orl.order_release_gid
having count(*) > 1
```

`$gid` is a runtime variable OTM substitutes with the GID of the object being evaluated — for an Order Release agent this will be the Order Release GID.

Define this in the system:

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Queries > New</div>

![Saved Query new screen with SQL fields](/images/saved-queriesconditions-img10-4451a43d6a.png)

<div class="field-box"><strong>Query Name:</strong> Enter a unique query name</div>
<div class="field-box"><strong>Object Type:</strong> ORDER RELEASE</div>
<div class="field-box"><strong>Domain Name:</strong> Enter your domain name</div>

Click **View/Define Query** and paste the SQL (without a trailing semicolon) into both the **Check one SQL** and **Find All SQL** fields, then click **Finished**:

![Saved Query SQL editor showing Check one SQL and Find All SQL fields](/images/saved-queriesconditions-img11-ebad4cc20e.png)

<div class="note-box"><strong>Note:</strong> Write the entire SQL on a single line with no line breaks. Line breaks cause export-to-CSV failures and will break the query when migrating between environments.</div>

**Type 3: Saved Condition**

A Saved Condition is a named grouping of one or more Saved Queries that evaluates to true or false. It is the construct OTM Agents use for IF/ELSE logic — the agent's condition step references a Saved Condition, and if all queries in that condition return at least one row, the condition is true and the agent proceeds to its action. Think of a Saved Query as a data filter and a Saved Condition as the boolean decision built on top of it.

<div class="step-box">Business Process Automation > Power Data > Event Management > Saved Condition > New</div>

![Saved Condition new screen showing query association fields](/images/saved-queriesconditions-img12-61e25779cc.png)

Link one or more Saved Queries to the condition. The condition evaluates to true when every associated query returns at least one record:

![Saved Condition screen showing the list of associated Saved Queries](/images/saved-queriesconditions-img13-7fa6ba4dda.png)
