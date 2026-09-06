---
title: "Business Monitors"
date: 2026-02-15T18:17:00+00:00
draft: false
weight: 50
tags:
  - "Business Monitor"
  - "Business"
  - "Monitor"
  - "business_monitor"
  - "auto refresh"
aliases:
  - "/2026/02/business-monitors.html"
keywords:
  - "Oracle OTM business monitor configuration"
  - "OTM business monitor setup steps"
  - "Oracle OTM monitor bulk plan failed orders"
  - "OTM business monitor refresh interval"
  - "Oracle OTM manage business monitors"
  - "OTM business monitor user role"
  - "Oracle Transportation Management monitor setup"
  - "OTM business monitor saved query screen set"
  - "Oracle OTM auto refresh monitor"
  - "OTM planner business monitor"
description: "Covers how to create and configure Business Monitors in Oracle OTM to give planners and other users real-time visibility into critical transactions like failed bulk plan orders, with configurable auto-refresh intervals."
url: "/posts/business-monitors/"
---

The Business Monitor is designed to give planners and operations teams real-time visibility into critical business transactions relevant to their role. For example, a planner can configure a monitor to display all orders that failed during bulk planning, using a saved query and screen set â€” then attach the monitor to their user profile or role so it updates automatically.

You can launch the Business Monitor by clicking the flag icon at the top of the OTM page.

[![](https://blogger.googleusercontent.com/img/a/AVvXsEit1IubQK1Y-7qezHq4Wwua5QetcJBiNT_cFTwIjLZwM986HPEebtytgyYotbrVTLkYFyzPjNqakFMoGLEOsHOfhG-29OaCVTj3-ZDYwH3g27OsJrNfd6lYlydeeobdc8P3kuMBNCcld-04vNQ8VPeOclCSjwsP1f_heAVq7AInRAXHRXplgvLhG-3QWKs=s16000)](https://blogger.googleusercontent.com/img/a/AVvXsEit1IubQK1Y-7qezHq4Wwua5QetcJBiNT_cFTwIjLZwM986HPEebtytgyYotbrVTLkYFyzPjNqakFMoGLEOsHOfhG-29OaCVTj3-ZDYwH3g27OsJrNfd6lYlydeeobdc8P3kuMBNCcld-04vNQ8VPeOclCSjwsP1f_heAVq7AInRAXHRXplgvLhG-3QWKs)

**Creating a Business Monitor:**

Assuming the required saved queries and screen sets are already created:

<div class="step-box">Configuration and Administration > Preferences > Manage Business Monitors > New</div>

Enter the following details:

- **Business Monitor ID:** A unique ID to identify this monitor.
- **Refresh Interval (in Minutes):** The frequency at which the monitor refreshes.
- **Domain Name:** Choose from the dropdown.

Then add one or more monitor rows:

- Enter the **Sequence**, **Query ID** (Order Base, Order Release, etc.), **Saved Query ID**, and **Screen Set ID** (the screen set in which results will be displayed).
- Click **Save** after each row.
- Click **Finish** to save the Business Monitor.

**Assigning a Business Monitor to a User or Role:**

After the Business Monitor is created, attach it to a User Preference, then assign that preference to a user or role.

<div class="step-box">Configuration and Administration > Preferences > User Preference</div>

1. Search for the User Preference you want to update.
2. Click **Edit**.
3. Select **Business Monitor** from the Name field and choose the Business Monitor ID from the Value dropdown.
4. Click **Finished**.

**Disable / Enable Business Monitor Auto Refresh:**

The auto-refresh interval runs all saved queries at each cycle and displays the counts. If a Business Monitor has many saved queries or returns large result sets, frequent auto-refresh adds significant load to the database.

To disable auto-refresh, set the following property:

```
glog.webserver.businessMonitor.autoRefresh=false
```

To re-enable:

```
glog.webserver.businessMonitor.autoRefresh=true
```

**Database Tables and SQL:**

<div class="field-box"><strong>BUSINESS_MONITOR:</strong> Stores the Business Monitor definitions created by users.</div>

<div class="field-box"><strong>BUSINESS_MONITOR_D:</strong> Stores the Saved Query and Screen Set details for each Business Monitor ID.</div>

To find the Business Monitor assigned to a specific user:

```sql
SELECT UPD.PREFERENCE_GID, UPD.USER_PREFERENCE_VALUE, GU.*
FROM USER_PREFERENCE_D UPD,
     USER_PREFERENCE_ACCESS UPA,
     USER_ACCESS UA,
     GL_USER GU
WHERE UPD.PREFERENCE_GID = 'BUSINESS_MONITOR'
AND UPA.USER_PREFERENCE_GID = UPD.USER_PREFERENCE_GID
AND UPA.USER_ACCESS_GID = UA.USER_ACCESS_GID
AND UA.ACCESS_TYPE = 'USER_PREFERENCE'
AND UA.USER_ROLE_GID = GU.DEFAULT_USER_ROLE_GID
```
