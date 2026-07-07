---
title: "Business Monitors"
date: 2026-02-15T18:17:00+00:00
draft: false
weight: 290
tags:
  - "Business Monitor"
  - "Business"
  - "Monitor"
  - "business_monitor"
  - "auto refresh"
aliases:
  - "/2026/02/business-monitors.html"
---

The Business Monitor as the name suggests is designed to monitor critical business functions associated to the role or specific user. For example, if a planner wants to review bulk plan failed orders, define a query identify such orders and a screen to display these orders and add them to business monitor. Business monitor can then be attached to user or role evel.

You can launch it by clicking on flag icon at top of the page:

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEit1IubQK1Y-7qezHq4Wwua5QetcJBiNT_cFTwIjLZwM986HPEebtytgyYotbrVTLkYFyzPjNqakFMoGLEOsHOfhG-29OaCVTj3-ZDYwH3g27OsJrNfd6lYlydeeobdc8P3kuMBNCcld-04vNQ8VPeOclCSjwsP1f_heAVq7AInRAXHRXplgvLhG-3QWKs=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEit1IubQK1Y-7qezHq4Wwua5QetcJBiNT_cFTwIjLZwM986HPEebtytgyYotbrVTLkYFyzPjNqakFMoGLEOsHOfhG-29OaCVTj3-ZDYwH3g27OsJrNfd6lYlydeeobdc8P3kuMBNCcld-04vNQ8VPeOclCSjwsP1f_heAVq7AInRAXHRXplgvLhG-3QWKs)

  

**Creating a Business Monitor:**  
  
Assuming that required saved queries and screensets are already created, lets see how to create a Business Monitor:

  1. Navigate to Configuration and Administration -> Preferences -> Manager Business Monitors
  2. Click on 'New' Button
  3. Enter the follow details 
     * Business Monitor ID* : Unique ID to identify a business monitor
     * Refresh Interval (in Minutes): Enter the frequency of BM Refresh
     * Domain Name: Choose it from drop down button
  4. Enter the Sequence, Query ID (OrderBase/OrderRelease/etc), Saved Query ID, Screen Set ID (Data will be opened in this screen set). Click on save button
  5. Repeat step 4 to enter all Saved queries & relevant screensets.
  6. Click on Finish to save the Business Monitor setup data. 

**Assigning Business Monitor to a user or user role:**  
  
After BM is created, it can be linked to a user preference, than that preference can be assigned to a user or a role. 

  1. Navigate to Configuration and Administration -> Preferences -> User Preference
  2. Search for the User Preference you want to attach the Business Monitor
  3. Click on the Edit
  4. Select 'Business Monitor' from the name and choose the Business Monitor ID under the 'Value' drop down list. 
  5. Click on Finished.

**Disable/Enable Business Monitor Auto Refresh:**  
  
When creating a Business Monitor, we can specify the refresh interval. If your BM has too many saved queries which results in lot of data, Auto Refresh could be a disadvantage for the application. For every refresh interval, it has to run all the saved queries, get their counts and display it. This will be a lot of load on the database.   
Disabling Business Monitor Auto Refresh is a very common activity done to improve the database performance.   
  
To disable, change the below setting to  
glog.webserver.businessMonitor.autoRefresh=false  
  

To Enable  
glog.webserver.businessMonitor.autoRefresh=true  

  

**Database tables and SQL:**

**Table BUSINESS_MONITOR:** Stores the Business Monitors defined by users

**Table BUSINESS_MONITOR_D:** Stores the Saved Query, Screenset details of a particular Business Monitor ID

How to find BM for a user ? 

SELECT UPD.PREFERENCE_GID,UPD.USER_PREFERENCE_VALUE,GU.*

FROM USER_PREFERENCE_D UPD,

USER_PREFERENCE_ACCESS UPA,

USER_ACCESS UA,

GL_USER GU

WHERE UPD.PREFERENCE_GID = 'BUSINESS_MONITOR'

AND UPA.USER_PREFERENCE_GID = UPD.USER_PREFERENCE_GID

AND UPA.USER_ACCESS_GID = UA.USER_ACCESS_GID

AND UA.ACCESS_TYPE = 'USER_PREFERENCE'

AND UA.USER_ROLE_GID = GU.DEFAULT_USER_ROLE_GID