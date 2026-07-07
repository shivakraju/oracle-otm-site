---
title: "05 - Bulk Plan"
date: 2020-08-22T04:52:00+00:00
draft: false
weight: 200
tags:
  - "OTM"
  - "Bulk Plan"
  - "Oracle"
aliases:
  - "/2020/08/basic-otm-configurations-05-bulk-plan.html"
---

**Note:** This post is continuation to topic: 01 and these configurations are specific to business scenario mentioned in that post. Link below to that post for quick reference:

  

[01 - Domain, Items, Locations, and Equipment](/posts/basic-otm-configurations-01-domain-items-locations-and-equipment/)

**Bulk Plan:**

**Create a new purchase order/order base record:**

Order Management > Purchase Order > Order Base > New >Enter below data:

  

> Order Base ID= PO2018051001
> 
> Order Configuration=ONE_TO_ONE
> 
> Item ID= ITEMA01
> 
> Source Location ID= DC_TCRP
> 
> Destination Location ID= STORE_B
> 
> Total Package Count=100

  

**Create two new order releases:**

  

> Order Base > Actions > Order Management > Change Order > Release Lines
> 
> Click button New Release Instruction
> 
> Unit Amount=20(Qty being released for shipping)
> 
>   
> 
> 
> Order Base > Actions > Order Management > Change Order > Release Lines
> 
> Click button New Release Instruction
> 
> Unit Amount=10(Qty being released for shipping)

**Now Query for Order Releases:**

> ![](/images/basic-otm-configurations-05-bu-img1-3c464757b9.png)

  

Select Order Releases > Actions > Operational Planning > Create Buy Shipment > Bulk Plan – Buy

This will create a shipment that includes above two order releases. To see how bulk plan is working try 'Shipment Routing Options' as described below.

**Shipment Routing Options:**

**Note tht we have below rates defined:**

> ![](/images/basic-otm-configurations-05-bu-img2-1e8cf7b957.png)

Now release PO with Source = DC and Destination = Store C and perform below action:

Order Release> Actions > Operational Planning > Show Routing Options

**OTM will show two possible itineraries as below:**

  

> ![](/images/basic-otm-configurations-05-bu-img3-bad36e64d2.png)

  

Select both Itineraries and click ‘Show Options’

You will see below details – all expected as per our configurations above.

  

> ![](/images/basic-otm-configurations-05-bu-img4-485c789a85.png)

  

Now if you do a bulk plan on this order release, it should select ITIN_D(least cost itinerary) and create two shipments:

• Shipment 1 with carrier PNDP going from DC to STORE_A with $20 as cost.

• Shipment 2 with carrier SGTM going from Store A to Store C with $20 as cost.

  

> ![](/images/basic-otm-configurations-05-bu-img5-5117392ac6.png)

  

Note that OTM has identified the carrier for each leg. Next step is to notify/send tender to those carriers with these pickup date/time and location details.