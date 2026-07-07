---
title: "User Roles - VPD and Access Control Lists"
date: 2016-12-01T21:30:00+00:00
draft: false
weight: 380
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
---

OTM application users will be grouped/classified based on their daily functions they perform in their organization. Each such group of users will be assigned a "Role" in OTM.   
  
So a "Role" controls:  
1\. Data visibility (using VPD setups)   
2\. User Interface or screen access (using ACLs)   
  
For example ADMIN role might have complete data visibility and access to all OTM data and UI functions whereas PLANNER role might have access to only particular domain and particular Order Type PO transactions. PLANNER also might need access to only few OTM functions like Order review, Bulk Plan, Tendering, etc.   
  
So, before defining the roles for a particular domain, we need to identify below information:  

  * Complete list of users who need access to the application for the domain.
  * Functions each user in that domain performs using the application.
  * Find if users require access to roles other than the Default role that is granted to them at user definition level.

**Define a new role:** Configuration and Administration > User Management > User Role

**Below are some important value to enter:**

**User Role ID:** Give Unique ID for the role

**Level:** Give this value same as Role ID.  
**Note:**This can be used to group a set of Roles. If you want to assign a single menu to set of roles, you can give this Level as same value for all such roles. We can discuss further about Level in another topic 'Manager User Access'.

**Data Source Profile ID:** DEFAULT  
  

**VPD Profile:** This can be defined from Configuration and Administration > VPD Profile. Below are important values while defining VPD Profile:

  * Check the options 'Use External Predicate Rule' and 'User Domain Role'(to restrict user from accessing data in other domains than where user record is created)
  * External Predicate Rule option allows us to define conditions at table level to restrict data access for that user. For example, if you want users to view only location data that they created, we can define:

  1. Table Name=LOCATION
  2. Predicate=location.insert_user = SYS_CONTEXT('gl_user_ctx','gl_user_gid')
  3. External Predicate Access = Read

It is always better to keep the VPD logic as simple as possible by populating required filtering data elements on the base objects(attribute columns etc) and define rules on these values. For example if you want to ensure user has access to specific type of POs, use custom logic in agents, etc to populate attribute value on those POs and later define Predicate as:  
Table Name=OB_ORDER_BASE, Predicate=attribute1='Type Value', External Predicate Access=All.  
  
**Tables related to VPD profile:**  
select * from vpd_profile where vpd_profile_gid = 'DOMAIN.VPD_PROFILE_ID'  
select * from external_predicate where vpd_profile_gid = 'DOMAIN.VPD_PROFILE_ID'  
  
**Grantee User Role:** Add all role names in this list that require access to current role being defined. For example if you have role like LOGISTICS_SUPERUSER and if those users want to switch to current role being defined, you should add 'LOGISTICS_SUPERUSER' role in this list. It is better to add Domain ADMIN role to all the new roles you define for that domain. Adding this access should be done from DBA.ADMIN login if current user has restricted privilege at current domain level.  
  
**Access Control List:** This is used to restrict certain screens(certain UI based functionality) like bulk plans, tender actions, etc. OTM has 'Access Control Entry Points' for each UI functionality. We can use them to control specific sub functions but OTM has defined(grouped) most of the commonly used Entry Points(sub functions) and created some default Access Control Lists which we can readily use. Example: 'Bulk Plan - View'  
  
As per Oracle documentation, every custom ACL we define with 'Granted' option checked should include ‘COMMON’ ACL provided by Oracle. This COMMON list covers standard OTM functionality like User Logins, etc.  
  
  

**Example:** We can define a custom ACL for a role with access only to create Order Release by querying a PO as follows:

Access Control = ORDER_ONLY_ACCESS(give any name)

**Child Access Control List with list of values:** Allocation - View, COMMON, Customer-Actions, Customer-Update, Customer-View, Logic Config-View, Material-View, Order-Actions, Order Update, Order-View, Parameter Set-View, Remark Qualifier - Update, Remark Qualifier-View, Shipment-View.

Note that in above list some of the values like 'Parameter Set - View' need to be defined due to some bugs in the current version.

  

**Restricting Certain ACL/Entry Points:**

**Example:** To restrict users from seeing Bulk Plan related data, we can use below as child ACLs and Create a custom ACL.

Bulk Plan – View

Bulk Plan – Update

Bulk Plan – Actions

  

To use as restricted list in the role definition, we should uncheck “Granted” check box while saving this ACL in the "Access Control List" section of the Role definition.

  

If you cannot control some access with ACLs provided by Oracle, you might need to go to Entry Point Level and define your ACLs. 

For example, to prevent users from access to User Preferences, Recurring Process, Business Monitor templates, etc. we created Entry Point Level access control lists and restricted them.   
  
**Assigning Role to User:** Once you have the role defined, you can assign it to a user.  
Configuration and Administration > User Management > User Manager > New   
**Enter below important values:**  
**User ID:** Unique ID like Employee ID etc for that user  
**User Name:** Unique Name or ID assigned to the user in Organization IT system(HR system)  
**Password/Retype password:** Provide password for the user.  
**User Role ID:** Provide role that you defined. This will be default role for that user when they login. It appears on the top right corner of the application after the login(next to User ID).  
  
**OTM Tables:**  
To see what is default role asscoiated to user and vice versa:  
\--------------------------------------------------------------  
select * from gl_user where gl_user_gid = 'DOMAIN.USER_ID_VALUE'  
select * from gl_user where default_user_role_gid = 'DOMAIN.ROLE_ID'  
  
**To see role defintion(VPD etc):**  
\--------------------------------  
select * from user_role where user_role_gid = 'DOMAIN.ROLE_ID'  
  
**To see what are ACLs associated to give user role:**  
\----------------------------------------------------  
SELECT * FROM USER_ROLE_ACR_ROLE WHERE USER_ROLE_GID = 'DOMAIN.ROLE_ID'  
  
**To see what ACLs available with in a ACL:**  
\-----------------------------------------  
SELECT * FROM ACR_ROLE_ROLE WHERE ACR_ROLE_GID = 'DOMAIN.ACCESS_CONTROL_LIST_ID'  
  
To see what entry points are available within an ACL:  
\-------------------------------------------------------  
SELECT * FROM ACR_ROLE_ENTRY_POINT WHERE ACR_ROLE_GID = 'ACCESS CONTROL LIST ID OR SUB LIST ID'   
  
**Steps to disable SQL Servlet Access for some users:**  
At the role level, associate ACL that restricts below two elements:  
SQL - Update  
SQL - View  
  
**We can test by re-login and using below servlet:**  
https://hostname/GC3/glog.webserver.sql.SqlServlet