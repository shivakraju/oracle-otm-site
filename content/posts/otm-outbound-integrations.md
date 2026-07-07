---
title: "OTM Outbound Integrations"
date: 2016-04-15T20:21:00+00:00
draft: false
weight: 70
tags:
  - "Outbound"
  - "Integration"
  - "Integrations"
  - "MIN"
  - "system"
  - "External"
  - "OTM"
  - "Learn"
  - "Oracle"
  - "Out XML profile"
aliases:
  - "/2016/04/otm-outbound-integrations.html"
---

OTM system can generate outbound XML data for any business object like 'Order Release', 'Shipment' etc either manually(using Send Interface Transmission action) or programmatically using same action from OTM Agent(workflow). We will discuss about OTM Agents in further posts.  
  
For generating outbound XMLs from OTM you may follow below steps:  
  
1\. Define an Out XML profile.   
  
Business Process Automation > Power Data > Integration > Out XML Profiles.  
  
Standard OTM XML for any object might have lot of data that might not be necessary or relevant to send it to the external systems. Also the file size for a complete XML would be in MB( for example Shipment XML might be 2 MB). In order to avoid generation of huge files and to control what data we generate in outbound XML we need to define an Out XML profile.  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfUVrk_ZRaGIZq_Q-0kl4oUFOTQWdXcKVfzRYupdbAo5p1t7d-r-qfjtWtyRFU2ysUCkfL78_rKrOlhzu2oW4coMFx84dGXPavRzZM5qQ4pGXsCfIqfLu_rrzJ_rGsVH7SUd6sXiICEsU/s640/Capture4.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfUVrk_ZRaGIZq_Q-0kl4oUFOTQWdXcKVfzRYupdbAo5p1t7d-r-qfjtWtyRFU2ysUCkfL78_rKrOlhzu2oW4coMFx84dGXPavRzZM5qQ4pGXsCfIqfLu_rrzJ_rGsVH7SUd6sXiICEsU/s1600/Capture4.JPG)

  
Select 'MIN' as Default Mode and specify the Xpath as shown above. This will ensure XML is limited to data that is within those Xpaths.   
  
2\. Define an External system and link the XML profile.   
Once you have the Out XML profile ready, you can go ahead and define External System:  
Business Process Automation > Communication Management > External Systems  

  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSNEUz8aFgysK7jzRgbQ9kVZDIF5spGgw958Ym1zejF-EMM59l0aRZ-PyE6zv6QWkOyW7KL2pi3_iK1sx11VbRhlIIVnUkHPUbznyOpXTb1n3uaLryZCL-WhOLTJM4j_s3ccB86o2y1Lo/s640/ExternalSystem1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiSNEUz8aFgysK7jzRgbQ9kVZDIF5spGgw958Ym1zejF-EMM59l0aRZ-PyE6zv6QWkOyW7KL2pi3_iK1sx11VbRhlIIVnUkHPUbznyOpXTb1n3uaLryZCL-WhOLTJM4j_s3ccB86o2y1Lo/s1600/ExternalSystem1.png)

[  
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_bQSmSwUZC_Ge7TUQxwPqxfmVN1aYa4czJJsVyqt2qR-Obuv42SpA5g0_Sna0OUuNZ-sW89xQfCWyMDe1a14jauoze9Nmb-V09Z1FlYdxBS_c0OoFfL7NHAEw9xMQUMVs5W9NSWZqqEM/s1600/ExternalSystem3.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN85RFhuc16z346LyC57QLrbTUwf6zPRhi2NLGRbZCcxroTn9WBa3M-eD7LOpz_wfhzXiHtr_pmWNxnlKxpR8iYNZsGNj4jgP_gs810CCdnf04WpfL8UH-_E3PwkH-HthfALBbl2RPqFY/s640/ExternalSystem2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgN85RFhuc16z346LyC57QLrbTUwf6zPRhi2NLGRbZCcxroTn9WBa3M-eD7LOpz_wfhzXiHtr_pmWNxnlKxpR8iYNZsGNj4jgP_gs810CCdnf04WpfL8UH-_E3PwkH-HthfALBbl2RPqFY/s1600/ExternalSystem2.png)

[  
](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_bQSmSwUZC_Ge7TUQxwPqxfmVN1aYa4czJJsVyqt2qR-Obuv42SpA5g0_Sna0OUuNZ-sW89xQfCWyMDe1a14jauoze9Nmb-V09Z1FlYdxBS_c0OoFfL7NHAEw9xMQUMVs5W9NSWZqqEM/s1600/ExternalSystem3.png)

Note that external system definition will have these critical details:  

  * External system ID 
  * User Name/Password that can be sent to external application for authentication
  * HTTPS URL or Webservice to which this XML should be sent
  * Out XML Profile ID that was created in first step

3\. We can invoke this external system for any object with below steps:  
  
In this example, we can invoke external system to generate a shipment XML as below:  
  
Shipment > Actions > Utilities > Send Interface Transmission   
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCA5yBFQFZ2CKO1RViuUkpMgtmTfnYTjNQmCDIbW3JBoXyD0TVojagQIGOZEfxlK0WJ07BFstaVvuupKMVzqV5_FVciNWZR868jkJ69VrOQjWRfjeUfsMrG8eqrd9qRyhZQvc1Mg9xi3w/s320/ExternalSystem3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhCA5yBFQFZ2CKO1RViuUkpMgtmTfnYTjNQmCDIbW3JBoXyD0TVojagQIGOZEfxlK0WJ07BFstaVvuupKMVzqV5_FVciNWZR868jkJ69VrOQjWRfjeUfsMrG8eqrd9qRyhZQvc1Mg9xi3w/s1600/ExternalSystem3.png)

  
Select the external system that was defined earlier and select notification type(HTTP/Service based on your external system definition).  
  
4\. You can verify the XML generated as below:  
Business Process Automation > Integration > Transmission Manager > Transactions Tab > Enter Object GID for 'Object' (Same AS) and Search.  
  
You will see Transmission Result page and 'Raw XML' option will show the generated XML.   
  
**Note:** Please post corrections(if any) to 'learnotm@outlook.com'