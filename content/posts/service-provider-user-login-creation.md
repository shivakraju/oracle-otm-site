---
title: "Service Provider User Login creation"
date: 2018-01-08T22:53:00+00:00
draft: false
weight: 400
tags:
  - "service provider login"
  - "Carrier login"
  - "SERPROV"
  - "Manage Association"
aliases:
  - "/2018/01/service-provider-user-login-creation.html"
keywords:
  - "Oracle OTM service provider user login"
  - "OTM carrier user login creation"
  - "Oracle OTM SERVPROV user setup"
  - "OTM manage association service provider user"
  - "Oracle OTM carrier tender login"
  - "OTM SERVPROV.ADMIN default password"
  - "Oracle OTM user association configuration"
  - "OTM carrier user access tender"
  - "Oracle Transportation Management carrier login setup"
  - "OTM USER_ASSOCIATION table GLOGOWNER"
description: "Explains how to create and configure carrier (service provider) user logins in Oracle OTM, including the Manage Association setup that links a user ID to a specific service provider so they can only access their own tender and shipment data."
---

In OTM, service providers such as carriers can be given their own login credentials to accept tenders and view shipment data. This article explains how to configure service provider user logins and the Manage Association setup that restricts each user to their specific carrier's data.

First, create a service provider (for example, ABCD) in the required domain (for example, DOMN).

You can then log in as SERVPROV.ADMIN with the default password of 'CHANGEME', or check with your system administrator if this password has been updated.

OTM automatically creates a user **SERVPROV.DOMN-ABCD** with the default role of 'SERVPROV' and default password 'CHANGEME'. OTM also links this User ID to service provider 'ABCD' so that this user can only review tender and shipment data associated to that carrier. OTM does this by creating a **Manage Association** configuration.

**Reviewing the Manage Association:**

<div class="step-box">Login as SERVPROV.ADMIN > User Manager > Manage Association</div>

Select the ID **SERVPROV.DOMN-ABCD** and click 'Retrieve'. Select the ID again to see the association definition. Note that the association qualifier is "Service Provider" and that the User ID and Service Provider SCAC are linked.

If multiple users from the same carrier need access to OTM, define IDs in the format `DOMN-ABCD-<EMP_NO>` and enter their email ID or a unique identifier as the User Name (login ID) on the user definition record. Once this is done, go to the Manage Association screen as described above to link each User ID to carrier 'ABCD'.

You can also review user associations from the back-end table in the GLOGOWNER schema:

```sql
SELECT * FROM USER_ASSOCIATION WHERE GL_USER_GID LIKE '%DOMN%ABCD%'
```
