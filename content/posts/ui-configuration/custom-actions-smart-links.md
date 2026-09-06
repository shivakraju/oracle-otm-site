---
title: "Custom Actions & Smart Links"
date: 2018-09-21T20:38:00+00:00
draft: false
weight: 26
tags:
  - "Actions"
  - "Label"
  - "Action Definition ID"
  - "Smart Links"
aliases:
  - "/2018/09/custom-actions.html"
keywords:
  - "Oracle OTM custom actions configuration"
  - "OTM smart links setup"
  - "Oracle OTM action definition ID RUN_AGENT"
  - "OTM custom action label manager"
  - "Oracle OTM actions manager screen set"
  - "OTM trigger agent from UI action"
  - "Oracle Transportation Management custom action"
  - "OTM smart link configuration"
  - "Oracle OTM reprocess invoice custom action"
  - "OTM action manager DBA admin setup"
description: "Explains how to create Custom Actions and Smart Links in Oracle OTM, enabling users to trigger agents or navigate to related records directly from the UI, with a worked example for reprocessing invoices."
url: "/posts/custom-actions-smart-links/"
---

Custom Actions allow users to trigger an agent or perform an operation directly from the OTM UI against a selected list of transactions. Smart Links are similar but operate on a single selected record and navigate the user to related data. The example below shows how to configure a custom action that triggers an INVOICE agent when a user selects 'Reprocess Invoice' from the Actions menu on a list of invoices.

**Step 1 — Create a Label (login as DBA.ADMIN):**

<div class="step-box">Configuration and Administration > User Configuration > Label Manager</div>

Create a new Label record. The Label ID and text you enter here will appear in the Actions menu in the UI.

[![OTM Label Manager screen showing a new label record](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwCKT_MrUWjkeGliAlrZiFK1kihtsAQnfBg6OX8x0RiL-HYJ4Zj5Ds5O3DZAkIqkD4V4I9VOzX486od3K7OZwthbuH5_ntGALQwJKTaRpzcTksTtQNfK0uLwFc2JshMpGFOviEP8M6DoU/s400/Capture5.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhwCKT_MrUWjkeGliAlrZiFK1kihtsAQnfBg6OX8x0RiL-HYJ4Zj5Ds5O3DZAkIqkD4V4I9VOzX486od3K7OZwthbuH5_ntGALQwJKTaRpzcTksTtQNfK0uLwFc2JshMpGFOviEP8M6DoU/s1600/Capture5.JPG)

**Step 2 — Create a Custom Action (login as domain ADMIN):**

<div class="step-box">Configuration and Administration > User Configuration > Actions Manager</div>

Create a new Action record with the following fields:

<div class="field-box"><strong>Action:</strong> Give the action a unique name.</div>

<div class="field-box"><strong>Label:</strong> Select the label created in Step 1.</div>

<div class="field-box"><strong>Action Definition ID:</strong> Enter RUN_AGENT_INVOICE (or the appropriate action definition for your use case).</div>

<div class="field-box"><strong>Agent ID:</strong> Select the name of the agent that should trigger when this action is invoked.</div>

<div class="note-box"><strong>Note:</strong> The agent is called by name rather than by event. If you create a new version of the agent, you must come back to this custom action and update the Agent ID to point to the new agent name.</div>

**Step 3 — Add the Action to a Screen Set:**

<div class="step-box">Configuration and Administration > User Configuration > Screen Set Manager</div>

Query the screen set for which you need to add the custom action. Go to the **Actions** tab, select **Top** on the hierarchy list, click the **+** button, and select **Add Actions**. In the Actions dropdown, select the label you associated with the new action, then save.

**Testing:**

Open your custom manager layout, select a few invoices, click the **Actions** button, and select the action label. This triggers the agent on the selected invoices.

**Smart Links:**

Smart Links are configured using the same steps as Actions with one difference: in the Screen Set, add the custom action under the **Smart Links** tab instead of the **Actions** tab.

The key difference between Actions and Smart Links is scope:

- **Actions** operate on a group of selected transactions. For example, you can select 10 order releases and trigger a Bulk Plan across all of them.
- **Smart Links** operate on a single selected transaction. For example, selecting a specific order release and clicking 'Related Buy Shipment' fetches the shipments associated with that one order release.
