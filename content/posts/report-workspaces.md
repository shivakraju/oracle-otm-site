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
---

If you want to restrict users to run or view only specific reports, you can use Report Workspace feature in OTM.  
  
You can restrict a list of reports to a particular user or user role by following below steps:  
  
**Step1:** Configuration and Administration > User Configuration > Manage User Access > Select 'Report Workspace' as User Access Type > Select Role/User against which you want update this workspace > Edit User Access.  
  
**Step2:** Add the list of Report IDs and select an Icon ID for each report. Click 'Finish' button once you add all the reports.  
  
**Step3:** Now add this Report workspace to your menu. Add new menu element with below entries:  
Text=Reports Workspace(or any name that is appropriate)   
Type=External URL  
URL=glog.webserver.report.ReportWorkspaceServlet  
  
Now if the user logs-in and clicks this menu element 'Reports Workspace' they see only the reports that you added in the list.