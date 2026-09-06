---
title: "User Menu and Manage User Access"
date: 2017-04-05T20:10:00+00:00
draft: false
weight: 20
tags:
  - "User Menu"
  - "Edit User Access"
  - "Manage user access"
  - "custom menu"
aliases:
  - "/2017/04/user-menu-and-manage-user-access.html"
keywords:
  - "Oracle OTM user menu configuration"
  - "OTM custom menu creation steps"
  - "Oracle OTM manage user access setup"
  - "OTM user role menu restriction"
  - "Oracle OTM user manager configuration"
  - "OTM menu element screen set link"
  - "Oracle Transportation Management user access control"
  - "OTM user login role assignment"
  - "Oracle OTM domain admin menu setup"
  - "OTM restrict user to specific screens"
description: "Explains how to create custom menus in Oracle OTM and restrict user access to specific screens by assigning the menu to a user or role through the User Manager and Manage User Access screens."
url: "/posts/user-menu-and-manage-user-access/"
---

Once a user logs in to the application, they will have access to OTM functions based on the role associated to their user record. You can further restrict the menu at role level or user level by creating a custom menu and associating it to the user or role.

Note that while creating a user, the following values are mandatory:

<div class="step-box">Configuration and Administration > User Management > User Manager</div>

- <div class="field-box"><strong>User ID:</strong> Unique identifier for the user</div>
- <div class="field-box"><strong>User Name:</strong> Can be used to avoid entering the domain name at login</div>
- <div class="field-box"><strong>Password:</strong> Initial password for the user</div>
- <div class="field-box"><strong>User Role ID:</strong> Default role for that user after initial login</div>

You can restrict the menu so that a user sees only specific screens — for example, only the Purchase Order (Order Base) screen. First create a custom menu with that single screen set link, then associate the menu to the user or role.

**Menu Creation:**

1. Login as Domain ADMIN.
2. Navigate to:
   <div class="step-box">Configuration and Administration > User Configuration > Menu Manager > New</div>
3. Enter Menu ID.
4. Select the text that reads 'Top' and click the Add (+) button next to it.
5. You will have options to create a Link or Group. Select 'Link' and click Create.
6. <div class="field-box"><strong>Text:</strong> Purchase Order</div>
7. Select option 'Screen set'.
8. <div class="field-box"><strong>Screen Set:</strong> OB_ORDER_BASE</div>
9. Click 'Save'.

This creates the custom menu. The next step is to link it to your role or user.

**Manage User Access:**

1. Login as Domain ADMIN.
2. Navigate to:
   <div class="step-box">Configuration and Administration > User Configuration > Manage User Access</div>
3. <div class="field-box"><strong>User Access Type:</strong> User Menu</div>
4. Select the User ID or Role ID to which you want to assign the menu.
5. Click 'Edit User Access'.
6. Select 'Exclude all user menus except the following' and select your custom user menu defined earlier.

If you log in with the User ID or with a User ID associated to the updated role, you will see the new custom menu.

**OTM Tables**

Query to find users associated to a role or vice-versa:

```sql
SELECT *
FROM GL_USER
WHERE DEFAULT_USER_ROLE_GID LIKE '%ROLE%'
AND GL_USER_GID LIKE '%USER%'
```

Query to find the menu name associated to a role:

```sql
SELECT USER_ACCESS_GID
FROM USER_ACCESS
WHERE ACCESS_TYPE = 'USER_MENU'
AND DOMAIN_NAME = '<enter domain name>'
AND USER_ROLE_GID = '<enter role GID>'
```

```sql
SELECT USER_MENU_LAYOUT_GID
FROM USER_MENU_ACCESS
WHERE USER_ACCESS_GID = '<Output from above Query>';
```
