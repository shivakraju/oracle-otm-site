---
title: "Yard Management and Appointment Scheduling"
date: 2026-02-14T12:11:00+00:00
draft: false
weight: 450
tags:
  - "Yard"
  - "Dock"
  - "OTM"
  - "appointment"
  - "resource"
  - "rows"
  - "slots"
  - "scheduling"
aliases:
  - "/2026/02/yard-management.html"
---

**Yard Management:** 

A warehouse usually has - Parking Yard and Dock Doors. Yard will have Rows and Each Row has some defined number of slots. Container will first be placed in the Yard slot. Users at warehouse will pull the container from Yard Slot to Door for unloading. Usually, responsibility of the carrier is to bring the container from port to yard. To move a container from Port to Yard – we can have a custom container ranking algorithm based on certain parameters (like PO priority, delivery dates, etc.) to give ranking to containers. Users at warehouse can use this rank to identify what containers they need to pull to the door at the earliest.

Once the shipment/container is in the yard slot, next step is to assign shipment to a door where loading/unloading happens. This step is called scheduling an appointment. Door will have time slots (30 min slot etc.) for loading or unloading activity that can be configured on the location resource.

Depending on the requirement, the Drayage carrier should be notified once the appointment is made in the system for a specific container. This is usually done by sending a tender offer EDI 204 file with expected delivery time and other details like Yard/Door No. Fpr example, EDI 204 can be triggered based on status update events from Ocean carrier like ‘Available for Delivery’ etc.

Below are the OTM location resource level configurations to define the yard:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjrxQUGWafBrevr1zt44kolMnCJIz5zrpVtOf5O-d08HPnPnKkEdnwuaZJkEgC270PCfyQtlNkxt8MaKVH9ZqdDmHq6O-nCC7U1GuomYJnF_ozYn82pXYEDhWsJQvKUNXgBKMqoz3vsysALGnNc8h6XL7HkgMpaQuecpG_QoD0XHpRHlKvHDQ-uFFp-sXI=w640-h233)](https://blogger.googleusercontent.com/img/a/AVvXsEjrxQUGWafBrevr1zt44kolMnCJIz5zrpVtOf5O-d08HPnPnKkEdnwuaZJkEgC270PCfyQtlNkxt8MaKVH9ZqdDmHq6O-nCC7U1GuomYJnF_ozYn82pXYEDhWsJQvKUNXgBKMqoz3vsysALGnNc8h6XL7HkgMpaQuecpG_QoD0XHpRHlKvHDQ-uFFp-sXI)

  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEjldfMqvjGGYyzOmlJx1OODq_4CeZtzIM7QoLV7Esiu_UJbZqI_7a-HRxEBzapATZZVkYmlk3BYUKPx7cMl6rqtGLWcdhWLDxMxMZMAkQaTFw0YKAG2y6lO0knoVGVkpNakNFRAXVyttyuJVD8Pa2A8gxsQzG8bBMXIOj3RgMRnhxOcga8fvUa4rp6EhhI=w640-h388)](https://blogger.googleusercontent.com/img/a/AVvXsEjldfMqvjGGYyzOmlJx1OODq_4CeZtzIM7QoLV7Esiu_UJbZqI_7a-HRxEBzapATZZVkYmlk3BYUKPx7cMl6rqtGLWcdhWLDxMxMZMAkQaTFw0YKAG2y6lO0knoVGVkpNakNFRAXVyttyuJVD8Pa2A8gxsQzG8bBMXIOj3RgMRnhxOcga8fvUa4rp6EhhI)

Once location resource level yard is defined, you can use custom logic to select shipments that are eligible to be displayed in the yard using business rules. For example, shipments/containers that are unloaded at destination port can be made visible in the yard. In this example, yard can be virtual yard just to give warehouse users visibility on what containers they can expect in coming days.Also, high priority shipments can be assigned to first rows and slots so that warehouse users can pull shipments for appointment scheduling from left to right and bottom down approach on the yard manager screen.

Using all this custom logic, insert entries in Yard table as shown below:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhGhWMLXI951n5-qWrBMaYCyyDmB3GAekIuu9IGIJsDsLAdcEMGioKXaClGM66fLcNg9YbmuF1kFZCmzJEOJGu1kMC1Uv_uSvr-_nC3vL_uQ42WMvfpepOKytk_Hw5xx6QiAMCzvLhYj44_NxjkTWY6EnIGldyp51Y6gFkXukvGGZhODLSGsUOoyu-iXfs=w640-h206)](https://blogger.googleusercontent.com/img/a/AVvXsEhGhWMLXI951n5-qWrBMaYCyyDmB3GAekIuu9IGIJsDsLAdcEMGioKXaClGM66fLcNg9YbmuF1kFZCmzJEOJGu1kMC1Uv_uSvr-_nC3vL_uQ42WMvfpepOKytk_Hw5xx6QiAMCzvLhYj44_NxjkTWY6EnIGldyp51Y6gFkXukvGGZhODLSGsUOoyu-iXfs)

  
Once shipments are inserted into yard table, we can see them in UI with below navigation:

Operational Planning > Appointment Management > Dock and Yard Managers > Query location > Actions > Manage Yard

[![](https://blogger.googleusercontent.com/img/a/AVvXsEikxyWncKgWr3x8m6T9R0u49s6wVB9zIv6x1uryw37gfk62pbgsQZ3nqwyJgNdzz2LkgnK7_RLzPtgggZWr-5aAmVrJu63M5Kfnm4N02azQzFaBbixSAPeZsvHgBLremuF6oJRO6GAkkw_oBW9IhLLtHrhmv9LQ3dvaJ8cWRYwjZsZrdPPqLKyLlArlSgk=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEikxyWncKgWr3x8m6T9R0u49s6wVB9zIv6x1uryw37gfk62pbgsQZ3nqwyJgNdzz2LkgnK7_RLzPtgggZWr-5aAmVrJu63M5Kfnm4N02azQzFaBbixSAPeZsvHgBLremuF6oJRO6GAkkw_oBW9IhLLtHrhmv9LQ3dvaJ8cWRYwjZsZrdPPqLKyLlArlSgk)

  

In the above screen, display text on shipments can be configured using glog property:

glog.otm.yard.displayText.shipmentRefnumQual

**Appointment Scheduling:** 

Once shipment is in the yard, next step for warehouse managers is to pull the shipment to available dock door for unloading. For this user can select shipment in the yard and right click to see below options:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiQvVB_Q0--A6pO52uJlQO5dW-apfIq_C8GWJxQ90miFtkSUJHXiKgEto1im9Nu1qU4ueTsxv_GyNqJ8-l2VlXgLgDlAd1f3STpf3VtfxlPwm8ox9AByuYeHYp4b9OVIPNXncc4V2imbcs1lAASejK0AYuQatJQLPeDQQTB0452HTKNB04dUuqyzLyPQOs=w400-h164)](https://blogger.googleusercontent.com/img/a/AVvXsEiQvVB_Q0--A6pO52uJlQO5dW-apfIq_C8GWJxQ90miFtkSUJHXiKgEto1im9Nu1qU4ueTsxv_GyNqJ8-l2VlXgLgDlAd1f3STpf3VtfxlPwm8ox9AByuYeHYp4b9OVIPNXncc4V2imbcs1lAASejK0AYuQatJQLPeDQQTB0452HTKNB04dUuqyzLyPQOs)

  

  

Click action 'Yard - Schedule Appointment - Show Options' and this will show appointment options for all the available resources. Select the resource and time slot and click submit to create an appoinment.  

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgDZ4BqhBRybFT9kqXvLjOeY6yOsfYO_c45nrIn0VSVik9dAwsbnr-QqEs94ZvY4awlUUphXdVV5UO1x6nH3aeDUh_yjLNKtbg2m8ZcUm2pIMtPitgOAxH9C-ch1j5sHmoOEgoe_Tnkco4SsT8-cudEpxeVd1BvlKXCTbWAl6woObL7Khby3GESpmftakI=w640-h214)](https://blogger.googleusercontent.com/img/a/AVvXsEgDZ4BqhBRybFT9kqXvLjOeY6yOsfYO_c45nrIn0VSVik9dAwsbnr-QqEs94ZvY4awlUUphXdVV5UO1x6nH3aeDUh_yjLNKtbg2m8ZcUm2pIMtPitgOAxH9C-ch1j5sHmoOEgoe_Tnkco4SsT8-cudEpxeVd1BvlKXCTbWAl6woObL7Khby3GESpmftakI)

  
Now go to actions > manage appointments screen:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEiUvr1lkg6fokhZBEBFdPA1lQAZYnOxtSKvBAHZ6kPjFLPr6QgopV2cXkOCEqoG3kLzGKr4cksXnBRe4eEZXEUzp2Ke_C2C4S5-G5LkQY0cTzhsQg4ZTXeiXD7rrq6Nr6_vnc-Xlu3E-Vyes56LpIrg2_hDX3cCq1TUbWWGd7gLr5oN9OzZJ8UzC8TQiAo=w640-h181)](https://blogger.googleusercontent.com/img/a/AVvXsEiUvr1lkg6fokhZBEBFdPA1lQAZYnOxtSKvBAHZ6kPjFLPr6QgopV2cXkOCEqoG3kLzGKr4cksXnBRe4eEZXEUzp2Ke_C2C4S5-G5LkQY0cTzhsQg4ZTXeiXD7rrq6Nr6_vnc-Xlu3E-Vyes56LpIrg2_hDX3cCq1TUbWWGd7gLr5oN9OzZJ8UzC8TQiAo)

  
You can see the shipment added to time slot against the selected resource(dock door). Time interval slot duration can be configured from location resource screen:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEg5BGJIjMx7OA7wFrF7hd7x8Z16dbn_MkSkc48A-ZdZK6Ld47i_cQN-yI2IRHcCENlMGYXc9eQhrNJ1qphahAFL4efCKWutf_1b_HDEWxk4PIMhEfoUZkVcoEMTkwJZC50UoiUGD2ftV1uoRUUZUkv9UWWtWlMn4dZaVZzxNS9g34eYzYwDTR9OmXKTdSw=w640-h234)](https://blogger.googleusercontent.com/img/a/AVvXsEg5BGJIjMx7OA7wFrF7hd7x8Z16dbn_MkSkc48A-ZdZK6Ld47i_cQN-yI2IRHcCENlMGYXc9eQhrNJ1qphahAFL4efCKWutf_1b_HDEWxk4PIMhEfoUZkVcoEMTkwJZC50UoiUGD2ftV1uoRUUZUkv9UWWtWlMn4dZaVZzxNS9g34eYzYwDTR9OmXKTdSw)

  
Display value on the appointment slot can be configued via glog property:

glog.appointment.displayString.shipment=objectRefnum:<shipment qulaifier GID>

**Appointment Rule Sets:**

To automate appointment scheduling using business rules you can follow below steps:

  * Identify business criteria or rules to match shipments to specific dock doors. For example all TL shipments should be assigned to Dock Door A and all LTL shipments should be assigned to Dock Door B for appointments.
  * Go to location > Resource > Resource Type screen and against each location Resource attach an appointment rule set with criteria. In above example, Mode Profile ID can be added as TL for Dock Door A and LTL for Dock Door B.
  * On Resource Type enable 'Auto Schedule' and 'Constraint Appointment'
  * Note that if standard fields provided by OTM on Appointment Rule Set are not covering required fields, you can use shipment reference number and flex fields. These refnum and flex fields can be populated via shipment creation workflow or any business event that occurs before appointment scheduling.
  * Once Resources are configured with appointment rule sets, to automatically schedule appointments from shipment workflow use below standard action:

[![](https://blogger.googleusercontent.com/img/a/AVvXsEj_2LF23cUf2AgEDTKC7PWsISp_BYtcC_gN1iSrk4MqFKdhTrzbqvcEJHwUfBo4xo8kOX918p7EYDsqT2if1Ug500oFWmC9XK4H5jFr-MyyrdoN9iuqOYYt4HfUE4S4NThpPu9JywYsNqv6iKLnLN44Mr_ssIBqj8lwenmF4s9qz_4aM4WP8aKKGSIU8W0=w640-h278)](https://blogger.googleusercontent.com/img/a/AVvXsEj_2LF23cUf2AgEDTKC7PWsISp_BYtcC_gN1iSrk4MqFKdhTrzbqvcEJHwUfBo4xo8kOX918p7EYDsqT2if1Ug500oFWmC9XK4H5jFr-MyyrdoN9iuqOYYt4HfUE4S4NThpPu9JywYsNqv6iKLnLN44Mr_ssIBqj8lwenmF4s9qz_4aM4WP8aKKGSIU8W0)

  

>   
>