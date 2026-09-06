---
title: "User Roles - VPD and Access Control Lists"
date: 2016-12-01T21:30:00+00:00
draft: false
weight: 10
tags:
  - "Grantee User Role"
  - "User"
  - "USER_ROLE_ACR"
  - "SQL Servlet"
  - "ACR_ROLE_ENTRY_POINT"
  - "VPD_PROFILE"
  - "User Role"
  - "EXTERNAL_PREDICATE"
  - "VPD Profile"
  - "ACR_ROLE_ROLE"
  - "Default Role"
  - "COMMON"
  - "USER_ROLE"
  - "Access Control List"
  - "Password"
aliases:
  - "/2016/12/user-roles-vpd-and-access-control-lists.html"
keywords:
  - "Oracle OTM user roles VPD access control"
  - "OTM VPD profile data visibility"
  - "Oracle OTM ACL access control list setup"
  - "OTM USER_ROLE table configuration"
  - "Oracle OTM role based data access"
  - "OTM VPD_PROFILE external predicate"
  - "Oracle OTM ACR_ROLE_ENTRY_POINT"
  - "OTM user role grantee configuration"
  - "Oracle Transportation Management user security setup"
  - "OTM domain level user access control"
description: "Explains Oracle OTM role-based security, covering how VPD profiles control data visibility and Access Control Lists (ACLs) govern UI screen access for each user role."
url: "/posts/user-roles-vpd-and-access-control-lists/"
---

<div class="note-box"><strong>Why three mechanisms — User Role, VPD, and Access Control List?</strong>

In any enterprise application, controlling "who can see what and do what" requires more than a single switch. OTM handles this through three layered mechanisms that work together under a single <strong>User Role</strong> definition:

<strong>User Role</strong> is the container that binds everything together. Every OTM user is assigned a default role that determines their identity within the system — which domain they belong to, what data they can see, and which screens and functions they can access. Think of it as the user's job profile inside OTM.

<strong>VPD (Virtual Private Database)</strong> controls <em>data-level</em> visibility. It operates at the database row level, silently filtering query results so that a user only ever sees records they are permitted to access — for example, a planner restricted to their own region's shipments, or an approver who can only see invoices within their approval threshold. VPD rules are invisible to the user: the application does not show them a filtered view, it simply never returns the rows they are not allowed to see.

<strong>Access Control List (ACL)</strong> controls <em>function-level</em> access. Even if a user can see a record, ACLs determine which actions they can take — whether they can initiate a Bulk Plan, approve a tender, run a recurring process, or access the SQL servlet. ACLs work at the UI entry-point level, granting or restricting individual buttons, menus, and screens.

Together: the Role defines <em>who</em> the user is, VPD defines <em>what data</em> they can see, and ACL defines <em>what they can do</em>. All three are configured under the User Role and must be planned together during an OTM implementation — a gap in any one of them can expose data or functionality that should be restricted.</div>

OTM application users are grouped and classified based on the daily functions they perform in their organization. Each such group of users is assigned a "Role" in OTM.

A "Role" controls:

1. Data visibility (using VPD setups)
2. User interface or screen access (using ACLs)

For example, the ADMIN role might have complete data visibility and access to all OTM data and UI functions, whereas the PLANNER role might have access only to a particular domain and particular Order Type PO transactions. The PLANNER may also need access to only a few OTM functions like Order review, Bulk Plan, and Tendering.

Before defining roles for a domain, identify the following:

- Complete list of users who need access to the application for the domain.
- Functions each user in that domain performs using the application.
- Whether users require access to roles other than the Default role granted to them at user definition level.

**Define a new role:**

<div class="step-box">Configuration and Administration > User Management > User Role</div>

**Important values to enter:**

<div class="field-box"><strong>User Role ID:</strong> Give a unique ID for the role</div>

<div class="field-box"><strong>Level:</strong> Give this value the same as the Role ID. This can be used to group a set of roles — for example, if you want to assign a single menu to a set of roles, give this Level the same value for all such roles.</div>

<div class="field-box"><strong>Data Source Profile ID:</strong> DEFAULT</div>

**VPD Profile:**

<div class="step-box">Configuration and Administration > VPD Profile</div>

Important values while defining a VPD Profile:

- Check the options 'Use External Predicate Rule' and 'User Domain Role' (to restrict users from accessing data in other domains than where their user record is created).
- The External Predicate Rule option allows you to define conditions at table level to restrict data access. For example, to allow users to view only location data they created:
  - <div class="field-box"><strong>Table Name:</strong> LOCATION</div>
  - <div class="field-box"><strong>Predicate:</strong> location.insert_user = SYS_CONTEXT('gl_user_ctx','gl_user_gid')</div>
  - <div class="field-box"><strong>External Predicate Access:</strong> Read</div>

It is always better to keep VPD logic as simple as possible by populating required filtering data elements on the base objects (attribute columns, etc.) and defining rules on those values. For example, to ensure a user has access to specific types of POs, use custom logic in agents to populate an attribute value on those POs and then define the predicate as:

<div class="field-box"><strong>Table Name:</strong> OB_ORDER_BASE</div>
<div class="field-box"><strong>Predicate:</strong> attribute1='Type Value'</div>
<div class="field-box"><strong>External Predicate Access:</strong> All</div>

**Tables related to VPD profile:**

```sql
select * from vpd_profile where vpd_profile_gid = 'DOMAIN.VPD_PROFILE_ID'
select * from external_predicate where vpd_profile_gid = 'DOMAIN.VPD_PROFILE_ID'
```

**Grantee User Role:** Add all role names in this list that require access to the current role being defined. For example, if you have a role like LOGISTICS_SUPERUSER and those users need to switch to the current role, add 'LOGISTICS_SUPERUSER' in this list. It is better to add the Domain ADMIN role to all new roles you define for that domain. Adding this access should be done from a DBA.ADMIN login if the current user has restricted privileges at the current domain level.

**Access Control List:** This is used to restrict certain screens (certain UI-based functionality) like bulk plans and tender actions. OTM has 'Access Control Entry Points' for each UI function, and has also grouped most commonly used entry points into default Access Control Lists that can be readily used — for example, 'Bulk Plan - View'.

As per Oracle documentation, every custom ACL defined with the 'Granted' option checked should include the 'COMMON' ACL provided by Oracle. This COMMON list covers standard OTM functionality like user logins.

**Example — ACL for order-only access:**

<div class="field-box"><strong>Access Control:</strong> ORDER_ONLY_ACCESS (or any name)</div>

Child Access Control List values: Allocation - View, COMMON, Customer-Actions, Customer-Update, Customer-View, Logic Config-View, Material-View, Order-Actions, Order Update, Order-View, Parameter Set-View, Remark Qualifier - Update, Remark Qualifier-View, Shipment-View.

<div class="note-box"><strong>Note:</strong> Some values like 'Parameter Set - View' may need to be included due to bugs in certain versions.</div>

**Restricting Certain ACL/Entry Points:**

To restrict users from seeing Bulk Plan related data, create a custom ACL using these child ACLs:

- Bulk Plan — View
- Bulk Plan — Update
- Bulk Plan — Actions

To use this as a restricted list in the role definition, uncheck the "Granted" checkbox when saving this ACL in the "Access Control List" section of the Role definition.

If you cannot control certain access with ACLs provided by Oracle, you may need to go to the Entry Point level and define your own ACLs. For example, to prevent users from accessing User Preferences, Recurring Process, or Business Monitor templates, Entry Point level access control lists can be created and restricted.

**Assigning a Role to a User:**

<div class="step-box">Configuration and Administration > User Management > User Manager > New</div>

<div class="field-box"><strong>User ID:</strong> Unique ID such as an employee number</div>
<div class="field-box"><strong>User Name:</strong> Unique name or ID from the organization's IT/HR system</div>
<div class="field-box"><strong>Password / Retype password:</strong> Provide the initial password</div>
<div class="field-box"><strong>User Role ID:</strong> The role defined above — this will be the default role for that user at login, appearing in the top right corner of the application</div>

**OTM Tables:**

Query to see the default role associated to a user and vice versa:

```sql
select * from gl_user where gl_user_gid = 'DOMAIN.USER_ID_VALUE'
select * from gl_user where default_user_role_gid = 'DOMAIN.ROLE_ID'
```

Query to see role definition (VPD, etc.):

```sql
select * from user_role where user_role_gid = 'DOMAIN.ROLE_ID'
```

Query to see ACLs associated to a user role:

```sql
SELECT * FROM USER_ROLE_ACR_ROLE WHERE USER_ROLE_GID = 'DOMAIN.ROLE_ID'
```

Query to see ACLs available within an ACL:

```sql
SELECT * FROM ACR_ROLE_ROLE WHERE ACR_ROLE_GID = 'DOMAIN.ACCESS_CONTROL_LIST_ID'
```

Query to see entry points available within an ACL:

```sql
SELECT * FROM ACR_ROLE_ENTRY_POINT WHERE ACR_ROLE_GID = 'ACCESS CONTROL LIST ID OR SUB LIST ID'
```

**Steps to disable SQL Servlet access for some users:**

At the role level, associate an ACL that restricts these two elements:

- SQL - Update
- SQL - View

You can test by re-logging in and accessing the servlet at:

```
https://hostname/GC3/glog.webserver.sql.SqlServlet
```
