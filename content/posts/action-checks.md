---
title: "Action Checks"
date: 2018-09-20T18:06:00+00:00
draft: false
weight: 430
tags:
  - "Audit Action ID"
  - "Cause"
  - "Post Action Check"
  - "Allow Condition"
  - "Action Checks"
aliases:
  - "/2018/09/action-checks.html"
---

If you have custom manager layout and want to perform some validations before data is saved to the DB, you can use this feature.  
  
**Example scenario:** Develop a custom manager layout for entering PO details where user can either select pre-existing location as destination location or can enter complete address details like address line1, zip code etc using custom attributes.  
  
In this custom screen, if we want to make sure that user either enters Destination Location XID or Enter new Destination location details with address details for the destination address.  
  
For this scenario, we need to make a custom validation checking that if Destination Location XID is entered or not, if this is not entered then check the custom attribute fields used to create location address lines etc. If both the details are missing, only then show a error message to user.  
  
**For this requirement we do following:**  
  
Go to Manage User Access > Enter ‘Action Checks’ as User Access Type > Enter the User Role for which these validations are to be performed > Click ‘Edit User Access’  
  
  

**In the screen we need to select:**

  

**Audit Action ID:** This drop down covers all standard user actions. For our scenario select ‘ADD ORDER BASE’ as the audit action.

  

**Allow Condition:** As the name suggests this is the SQL condition that should pass in-order for error NOT TO DISPLAY:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-xiRTAfX9K5eoEMT5_JI3M65hGxUejeprsISuSzddUeaOY0nr0pxZZrTQi2pPz_t38NaBdUy9X7PwWcsstZf2AeMSk2hDAtSRS8r_SXNViGB0viU1cEkyTTuNdkfNSoIntXKH1Ye-ubI/s400/Capture1.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-xiRTAfX9K5eoEMT5_JI3M65hGxUejeprsISuSzddUeaOY0nr0pxZZrTQi2pPz_t38NaBdUy9X7PwWcsstZf2AeMSk2hDAtSRS8r_SXNViGB0viU1cEkyTTuNdkfNSoIntXKH1Ye-ubI/s1600/Capture1.JPG)

  

  

In above query we are saying that for error not to display, source_location_gid <> ‘DEFAULT’ OR OB. Attribute2(Address line1) is not null.

  

**Cause:** This is a label with reason text that you want to provide to user as error reason. Note Type of label=ERROR.

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm3t3iuSrt4d5KmeWLef_hBl7P77g8Dw-lysomJjyWqfidt9v2jAMEZLm4UUXqjSg05qiWUTTYQbtaKNlZYLi6145Oa0BS4aRSTQVRvFx_6FeHPKaS2eyajRMrufSpGBotoGKqqr6QCvA/s400/Capture2.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm3t3iuSrt4d5KmeWLef_hBl7P77g8Dw-lysomJjyWqfidt9v2jAMEZLm4UUXqjSg05qiWUTTYQbtaKNlZYLi6145Oa0BS4aRSTQVRvFx_6FeHPKaS2eyajRMrufSpGBotoGKqqr6QCvA/s1600/Capture2.JPG)

  

  
  
  

**Post Action Check:** This if checked performs validation after the execution of action and before data is saved to the database. Note that for Delete Record validations, this should be unchecked. Also you can add same Audit Action validation one with Post Action Check and other with Pre Action Check based on your requirements.

  

**Testing:**

If user tries to save a PO without entering both the details mentioned above, user will receive error:

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Z1CdJkNhyphenhyphenkAcdqzbEO62T46ZsWdzLGzQPIbczAvsc63NxEAFNCqAOg-l-60nzeGXEUJqN1df6d2q9bRfGj-57Sy8qZUKNtaOKgqjyHtJCvTs7cL1xZgPPjjavwT21q5Nfa7J06KNfGc/s400/Capture3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Z1CdJkNhyphenhyphenkAcdqzbEO62T46ZsWdzLGzQPIbczAvsc63NxEAFNCqAOg-l-60nzeGXEUJqN1df6d2q9bRfGj-57Sy8qZUKNtaOKgqjyHtJCvTs7cL1xZgPPjjavwT21q5Nfa7J06KNfGc/s1600/Capture3.JPG)