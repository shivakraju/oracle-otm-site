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
---

In this article we will discuss how we can configure OTM system to handle users from your service providers to login to OTM and perform actions like accepting tenders, etc.  
  
First step is you create a service provider (say ABCD) in the required domain (say DOMN).  
  
Now you can login as SERVPROV.ADMIN with default password of 'CHANGEME' or check with your system administrator if this password has been updated.  
  
You can view that OTM by default has created a user "SERVPROV.DOMN-ABCD" with default role of 'SERVPROV' and default password for this user as 'CHANGEME'.  
  
Also OTM will link this User ID to service provider 'ABCD' so that this user can only review tender, shipment data, etc associated to this particular carrier. OTM does this by creating "Manage Association" configuration.  
**Navigation:** Login as SERVPROV.ADMIN, User Manager > Manage Association > select the ID "SERVPROV.DOMN-ABCD" > Click 'Retrieve' > Select the ID again to see association definition. Note that association qualifier is "Service Provider" and you that User ID and Service Provider SCAC are linked/associated.  
  
If there are multiple users from the same carrier who need to access to OTM, you may define IDs in the format DOMN-ABCD-<EMP_NO> and mention their email ID or some unique identifier for each user as User name(as login ID) on the user definition record. Once this is done, go to "Manage Association" screen as mentioned above to link this User ID to carrier 'ABCD'.  
  
Also you can review these user associations from back end table in GLOGOWNER schema:  
  
SELECT * FROM USER_ASSOCIATION WHERE GL_USER_GID LIKE '%DOMN%ABCD%'