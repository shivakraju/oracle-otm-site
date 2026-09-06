---
title: "Action Checks"
date: 2018-09-20T18:06:00+00:00
draft: false
weight: 60
tags:
  - "Audit Action ID"
  - "Cause"
  - "Post Action Check"
  - "Allow Condition"
  - "Action Checks"
aliases:
  - "/2018/09/action-checks.html"
keywords:
  - "Oracle OTM action checks configuration"
  - "OTM post action check validation"
  - "Oracle OTM allow condition action check"
  - "OTM audit action ID action checks"
  - "Oracle OTM manager layout validation"
  - "OTM action check cause message"
  - "Oracle OTM custom validation before save"
  - "OTM action checks user role setup"
  - "Oracle Transportation Management UI validation"
  - "OTM ADD ORDER BASE action check"
description: "Explains Oracle OTM Action Checks, a configuration feature for adding custom pre-save validations on manager layouts, illustrated with an example that validates destination location data before a purchase order is created."
url: "/posts/action-checks/"
---

Action Checks allow you to add custom validations on manager layouts before data is saved to the database. This is useful when a screen has conditional mandatory fields — for example, requiring either a pre-existing location XID or a full set of address fields, but not both.

**Example Scenario:**

A custom manager layout allows users to enter PO details. The destination can be set by selecting an existing Location XID, or by entering a new address (address line 1, zip code, etc.) using custom attributes. The validation must ensure that at least one of these two options is populated before the record is saved.

**Configuration Steps:**

<div class="step-box">Manage User Access > Enter 'Action Checks' as User Access Type > Enter the User Role > Click 'Edit User Access'</div>

**In the screen, configure the following fields:**

<div class="field-box"><strong>Audit Action ID:</strong> Covers all standard user actions. For this scenario, select <strong>ADD ORDER BASE</strong> as the audit action.</div>

<div class="field-box"><strong>Allow Condition:</strong> The SQL condition that must pass in order for the error NOT to display. In the example below, the condition allows the save to proceed if <code>source_location_gid &lt;&gt; 'DEFAULT'</code> OR the custom attribute <code>OB.Attribute2</code> (Address Line 1) is not null — meaning at least one destination detail is present.</div>

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-xiRTAfX9K5eoEMT5_JI3M65hGxUejeprsISuSzddUeaOY0nr0pxZZrTQi2pPz_t38NaBdUy9X7PwWcsstZf2AeMSk2hDAtSRS8r_SXNViGB0viU1cEkyTTuNdkfNSoIntXKH1Ye-ubI/s400/Capture1.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-xiRTAfX9K5eoEMT5_JI3M65hGxUejeprsISuSzddUeaOY0nr0pxZZrTQi2pPz_t38NaBdUy9X7PwWcsstZf2AeMSk2hDAtSRS8r_SXNViGB0viU1cEkyTTuNdkfNSoIntXKH1Ye-ubI/s1600/Capture1.JPG)

<div class="field-box"><strong>Cause:</strong> A label that provides the error reason text shown to the user when the validation fails. Set the label Type to <strong>ERROR</strong>.</div>

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm3t3iuSrt4d5KmeWLef_hBl7P77g8Dw-lysomJjyWqfidt9v2jAMEZLm4UUXqjSg05qiWUTTYQbtaKNlZYLi6145Oa0BS4aRSTQVRvFx_6FeHPKaS2eyajRMrufSpGBotoGKqqr6QCvA/s400/Capture2.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhm3t3iuSrt4d5KmeWLef_hBl7P77g8Dw-lysomJjyWqfidt9v2jAMEZLm4UUXqjSg05qiWUTTYQbtaKNlZYLi6145Oa0BS4aRSTQVRvFx_6FeHPKaS2eyajRMrufSpGBotoGKqqr6QCvA/s1600/Capture2.JPG)

<div class="field-box"><strong>Post Action Check:</strong> When checked, validation runs after the action executes but before data is committed to the database. For Delete Record validations, this should be <strong>unchecked</strong>. You can also add the same Audit Action twice — once with Post Action Check enabled and once without — to cover both pre- and post-action scenarios.</div>

**Testing:**

If the user tries to save a PO without entering either destination detail, the following error is displayed:

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Z1CdJkNhyphenhyphenkAcdqzbEO62T46ZsWdzLGzQPIbczAvsc63NxEAFNCqAOg-l-60nzeGXEUJqN1df6d2q9bRfGj-57Sy8qZUKNtaOKgqjyHtJCvTs7cL1xZgPPjjavwT21q5Nfa7J06KNfGc/s400/Capture3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_Z1CdJkNhyphenhyphenkAcdqzbEO62T46ZsWdzLGzQPIbczAvsc63NxEAFNCqAOg-l-60nzeGXEUJqN1df6d2q9bRfGj-57Sy8qZUKNtaOKgqjyHtJCvTs7cL1xZgPPjjavwT21q5Nfa7J06KNfGc/s1600/Capture3.JPG)
