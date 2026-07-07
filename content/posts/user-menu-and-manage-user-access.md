---
title: "User Menu and Manage User Access"
date: 2017-04-05T20:10:00+00:00
draft: false
weight: 390
tags:
  - "User Menu"
  - "Edit User Access"
  - "Manage user access"
  - "custom menu"
aliases:
  - "/2017/04/user-menu-and-manage-user-access.html"
---

Once a user logins to application, they we will have access to OTM functions based on the role associated to their user record.  
  
Note that while creating an user ( Configuration and Administration > User Management > User Manager) below are the mandatory values:  
  

  * User ID
  * User Name(can be used so that we can avoid domain name at log-in)
  * Password
  * User Role ID(Default role for that user after initial log-in)

We discussed how we can restrict data and functions using VPD and Access Control List in previous topic "User Roles"

  

We can also restrict the menu at role level or user level with below steps. Say you want user to have menu with only Purchase order(order base) screen, you first create a custom menu with this single screen set(menu link) and then associate this menu to the user or role.

  

**Menu Creation:**

  1. Login as Domain ADMIN.
  2. Navigate to Configuration and Administration > User Configuration > Menu Manager > New
  3. Enter Menu ID.
  4. Select text that reads 'Top' and click Add(+) button next to it.
  5. You will have options to create Link/Group. Select 'Link'. Hit Create button.
  6. Type Text 'Purchase Order'.
  7. Select option 'Screen set'.
  8. Enter Screen Set 'OB_ORDER_BASE'. Click 'Save'.

This will create a menu and next step is to link this custom menu to your role/user. For this you can follow steps:

  

**Manage User Access:**

  1. Login as Domain ADMIN.
  2. Configuration and Administration > User Configuration > Manage User Access
  3. Select User Access Type=User Menu
  4. Select User ID or Role ID to which you want to update the menu
  5. Click 'Edit User Access'
  6. Select 'Exclude all user menus except the following' and select your custom user menu defined earlier.

If you login now with User ID or User ID associated to updated role, you can see the new custom menu.

  
Below are OTM tables where related entries are made:  
  
Query to find Users associated to role or vice-versa:  
  
SELECT *  
FROM GL_USER   
WHERE DEFAULT_USER_ROLE_GID LIKE '%ROLE%'  
AND GL_USER_GID LIKE '%USER%'  
  
**Queries to find menu name associated to a role:**  
  
SELECT USER_ACCESS_GID  
FROM USER_ACCESS   
WHERE ACCESS_TYPE = 'USER_MENU'   
AND DOMAIN_NAME = '<enter domain name>'   
AND USER_ROLE_GID = '<enter role GID>'  
  
  
SELECT USER_MENU_LAYOUT_GID  
FROM USER_MENU_ACCESS   
WHERE USER_ACCESS_GID = '<Output from above Query>';