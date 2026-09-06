---
title: "Report Workspaces"
date: 2017-06-28T21:03:00+00:00
draft: false
weight: 330
tags:
  - "glog.webserver.report.ReportWorkspaceServlet"
  - "Report Workspace"
aliases:
  - "/2017/06/report.html"
keywords:
  - "Oracle OTM report workspace configuration"
  - "OTM restrict reports by user role"
  - "Oracle OTM ReportWorkspaceServlet setup"
  - "OTM report workspace menu link"
  - "Oracle OTM manage user access report workspace"
  - "OTM user role report access control"
  - "Oracle Transportation Management report restriction"
  - "OTM report workspace role assignment"
  - "Oracle OTM report ID restrict visibility"
  - "OTM custom menu report workspace"
description: "Explains how to configure Report Workspaces in Oracle OTM to restrict report access by user or role, including adding the workspace to the menu using the ReportWorkspaceServlet URL."
---

If you want to restrict users to running or viewing only specific reports, you can use the Report Workspace feature in OTM. The steps below restrict a list of reports to a particular user or user role.

**Step 1 — Configure the Report Workspace**

<div class="step-box">Configuration and Administration > User Configuration > Manage User Access</div>

- <div class="field-box"><strong>User Access Type:</strong> Report Workspace</div>
- Select the Role or User ID to update.
- Click 'Edit User Access'.

**Step 2 — Add Reports to the Workspace**

Add the list of Report IDs and select an Icon ID for each report. Click 'Finish' once all reports have been added.

**Step 3 — Add the Workspace to the Menu**

Add a new menu element with the following entries:

- <div class="field-box"><strong>Text:</strong> Reports Workspace (or any appropriate name)</div>
- <div class="field-box"><strong>Type:</strong> External URL</div>
- <div class="field-box"><strong>URL:</strong> glog.webserver.report.ReportWorkspaceServlet</div>

When the user logs in and clicks the 'Reports Workspace' menu element, they will see only the reports added to the workspace.
