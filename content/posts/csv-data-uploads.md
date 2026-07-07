---
title: "CSV Data Uploads"
date: 2026-03-04T21:48:00+00:00
draft: false
weight: 80
aliases:
  - "/2026/03/csv-data-uploads.html"
---

We can load data to OTM is using CSV files. You can follow below steps to load location into OTM using CSV upload. Note that same steps are applicable to any OTM object like order release,shipment, invoice, etc.

1\. Create a sample location manually in OTM with requirement information.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi59aQDCW9K0M4nW9jR1R4VjcCsmIkowgc9bnC7DztULfJ24FFFoDl3yf-YEpSVwsP0hxDR2ACfu8grfQ8pS93uHg4z2ngQ4vABzMh15Q9_kYgsrG7MDtfeFu1de_yyCFuPR2zVac5Ce2M/s1600/OTM_Location.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi59aQDCW9K0M4nW9jR1R4VjcCsmIkowgc9bnC7DztULfJ24FFFoDl3yf-YEpSVwsP0hxDR2ACfu8grfQ8pS93uHg4z2ngQ4vABzMh15Q9_kYgsrG7MDtfeFu1de_yyCFuPR2zVac5Ce2M/s1600/OTM_Location.png)

2\. Query for this location from back end table as follows:  
  

select * from location where location_xid = 'TEST SH CORPORATION-45769'

  
3\. Note down the WHERE clause from the query.  
4\. Goto Business Process Automation > Data Export > CSV Export  
  
![](/images/csv-data-uploads-img1-80b819bdb1.png)  
  
  

  

5.

![](https://blogger.googleusercontent.com/img/a/AVvXsEg5_oszH_mTbaed3D2S08SF-d7CTgbLoGE-z3yuXNvFMXEZJXW6Z83BrTq_p8jlZJVy1Lbt9fvIYvvIHvDFBok7oRmX_SZyQw5KzgdNRGRFGqgFtR5LvY9I3xAG9QxwbciJkegHjEuCphri_zPIolVqamdUwZbzWsqemGHp4ocmVo883qLwmKvPttxRIFE)  
Select Table Name as 'LOCATION' and copy the WHERE clause that you have noted down in earlier step.  
6\. Click 'Run' and you will have following output:  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiMEL8SIaYV2g2_IasZKirtNzb5EIfKGfIoWRrV-7Rn8BNxPs4zVQO1hwYKImg0QML0DzzsrYFzEi-yO7JvcnEZqnXK0aMNyhyKUxg2C1_rx_mYufjmmDyozMkliLfq3gdZeG9-NfYyBk/s1600/CSVUploadResult.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgiMEL8SIaYV2g2_IasZKirtNzb5EIfKGfIoWRrV-7Rn8BNxPs4zVQO1hwYKImg0QML0DzzsrYFzEi-yO7JvcnEZqnXK0aMNyhyKUxg2C1_rx_mYufjmmDyozMkliLfq3gdZeG9-NfYyBk/s1600/CSVUploadResult.png)

7\. Select the grey text which is location data and save it in .txt file.   
Open this .txt file using Microsoft xls application and select comma as delimiter. Save this file as .csv file. To verify the .csv has data is correct format open the file using textpad and you should see data with comma separated values. 8\. Now upload the file using Business Process Automation -> Integration -> Integration Manager -> Upload XML/CSV Transmission:  
  
  
![](/images/csv-data-uploads-img2-7f6b9b4bab.png)   
![](/images/csv-data-uploads-img3-f36c44c247.png)   
  
**Important Note:**  
Ensure that date columns will follow the NLS Date Format mentioned in line 2 of the csv file.The results screen is something like this. Note that Process Count and Error Count values are populated in the result.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDKW3LF0KTVpdM9h8uOFRsvkgjiRLGAlkdOn4HcOnAManxyXtV1PyZyoaxW6DCt0_YzkPSlIuFIOWKWOdhj7B_BLB36iLg24DOpK0Xxmgbd0dliCejlboo4xSNyOG_IVgFQozdCxarruA/s1600/UplaodResult2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiDKW3LF0KTVpdM9h8uOFRsvkgjiRLGAlkdOn4HcOnAManxyXtV1PyZyoaxW6DCt0_YzkPSlIuFIOWKWOdhj7B_BLB36iLg24DOpK0Xxmgbd0dliCejlboo4xSNyOG_IVgFQozdCxarruA/s1600/UplaodResult2.png)