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
keywords:
  - "Oracle OTM yard management configuration"
  - "OTM dock appointment scheduling"
  - "Oracle OTM location resource yard setup"
  - "OTM yard slot row configuration"
  - "Oracle OTM appointment scheduling dock door"
  - "OTM drayage carrier tender EDI 204"
  - "Oracle Transportation Management yard management"
  - "OTM container yard slot assignment"
  - "Oracle OTM warehouse dock scheduling"
  - "OTM yard manager screen configuration"
description: "Describes Oracle OTM Yard Management and Appointment Scheduling, including how to configure location resources for yard rows and dock slots, schedule container appointments, and trigger drayage carrier notifications via EDI 204."
---

Oracle OTM's Yard Management and Appointment Scheduling features help warehouse teams track containers in the yard and coordinate dock door assignments for loading and unloading.

**Yard Management:**

A warehouse typically has a Parking Yard and Dock Doors. The yard has Rows and each row has a defined number of slots. A container is first placed in a yard slot. Warehouse staff then pull the container from the yard slot to a dock door for unloading. The carrier is typically responsible for bringing the container from port to yard.

To move a container from port to yard, a custom container ranking algorithm can be used based on parameters such as PO priority and delivery dates. Warehouse staff use this rank to identify which containers to pull to the door first.

Once the shipment or container is in a yard slot, the next step is to assign it to a dock door — a process called scheduling an appointment. Each dock door has time slots (for example, 30-minute slots) for loading or unloading activity that can be configured on the location resource.

Depending on the requirement, the drayage carrier should be notified once the appointment is created in the system for a specific container. This is typically done by sending a tender offer EDI 204 file with expected delivery time and details like Yard/Door number. EDI 204 can be triggered based on status update events from the ocean carrier, such as 'Available for Delivery'.

Below are the OTM location resource level configurations to define the yard:

[![OTM location resource yard configuration](https://blogger.googleusercontent.com/img/a/AVvXsEjrxQUGWafBrevr1zt44kolMnCJIz5zrpVtOf5O-d08HPnPnKkEdnwuaZJkEgC270PCfyQtlNkxt8MaKVH9ZqdDmHq6O-nCC7U1GuomYJnF_ozYn82pXYEDhWsJQvKUNXgBKMqoz3vsysALGnNc8h6XL7HkgMpaQuecpG_QoD0XHpRHlKvHDQ-uFFp-sXI=w640-h233)](https://blogger.googleusercontent.com/img/a/AVvXsEjrxQUGWafBrevr1zt44kolMnCJIz5zrpVtOf5O-d08HPnPnKkEdnwuaZJkEgC270PCfyQtlNkxt8MaKVH9ZqdDmHq6O-nCC7U1GuomYJnF_ozYn82pXYEDhWsJQvKUNXgBKMqoz3vsysALGnNc8h6XL7HkgMpaQuecpG_QoD0XHpRHlKvHDQ-uFFp-sXI)

[![OTM yard rows and slots configuration](https://blogger.googleusercontent.com/img/a/AVvXsEjldfMqvjGGYyzOmlJx1OODq_4CeZtzIM7QoLV7Esiu_UJbZqI_7a-HRxEBzapATZZVkYmlk3BYUKPx7cMl6rqtGLWcdhWLDxMxMZMAkQaTFw0YKAG2y6lO0knoVGVkpNakNFRAXVyttyuJVD8Pa2A8gxsQzG8bBMXIOj3RgMRnhxOcga8fvUa4rp6EhhI=w640-h388)](https://blogger.googleusercontent.com/img/a/AVvXsEjldfMqvjGGYyzOmlJx1OODq_4CeZtzIM7QoLV7Esiu_UJbZqI_7a-HRxEBzapATZZVkYmlk3BYUKPx7cMl6rqtGLWcdhWLDxMxMZMAkQaTFw0YKAG2y6lO0knoVGVkpNakNFRAXVyttyuJVD8Pa2A8gxsQzG8bBMXIOj3RgMRnhxOcga8fvUa4rp6EhhI)

Once the location resource yard is defined, custom logic can be used to select shipments eligible to be displayed in the yard using business rules. For example, shipments or containers unloaded at the destination port can be made visible in the yard. In this case, the yard can be a virtual yard to give warehouse users visibility on containers they can expect in coming days. High-priority shipments can be assigned to the first rows and slots so that warehouse users can pull shipments for appointment scheduling in a left-to-right, top-to-bottom approach on the Yard Manager screen.

Using this custom logic, insert entries in the Yard table as shown below:

[![OTM yard table insert example](https://blogger.googleusercontent.com/img/a/AVvXsEhGhWMLXI951n5-qWrBMaYCyyDmB3GAekIuu9IGIJsDsLAdcEMGioKXaClGM66fLcNg9YbmuF1kFZCmzJEOJGu1kMC1Uv_uSvr-_nC3vL_uQ42WMvfpepOKytk_Hw5xx6QiAMCzvLhYj44_NxjkTWY6EnIGldyp51Y6gFkXukvGGZhODLSGsUOoyu-iXfs=w640-h206)](https://blogger.googleusercontent.com/img/a/AVvXsEhGhWMLXI951n5-qWrBMaYCyyDmB3GAekIuu9IGIJsDsLAdcEMGioKXaClGM66fLcNg9YbmuF1kFZCmzJEOJGu1kMC1Uv_uSvr-_nC3vL_uQ42WMvfpepOKytk_Hw5xx6QiAMCzvLhYj44_NxjkTWY6EnIGldyp51Y6gFkXukvGGZhODLSGsUOoyu-iXfs)

Once shipments are inserted into the yard table, they can be seen in the UI:

<div class="step-box">Operational Planning > Appointment Management > Dock and Yard Managers > Query location > Actions > Manage Yard</div>

[![OTM Yard Manager screen](https://blogger.googleusercontent.com/img/a/AVvXsEikxyWncKgWr3x8m6T9R0u49s6wVB9zIv6x1uryw37gfk62pbgsQZ3nqwyJgNdzz2LkgnK7_RLzPtgggZWr-5aAmVrJu63M5Kfnm4N02azQzFaBbixSAPeZsvHgBLremuF6oJRO6GAkkw_oBW9IhLLtHrhmv9LQ3dvaJ8cWRYwjZsZrdPPqLKyLlArlSgk=w640-h298)](https://blogger.googleusercontent.com/img/a/AVvXsEikxyWncKgWr3x8m6T9R0u49s6wVB9zIv6x1uryw37gfk62pbgsQZ3nqwyJgNdzz2LkgnK7_RLzPtgggZWr-5aAmVrJu63M5Kfnm4N02azQzFaBbixSAPeZsvHgBLremuF6oJRO6GAkkw_oBW9IhLLtHrhmv9LQ3dvaJ8cWRYwjZsZrdPPqLKyLlArlSgk)

The display text on shipments in the Yard Manager screen can be configured using the glog property:

```
glog.otm.yard.displayText.shipmentRefnumQual
```

**Appointment Scheduling:**

Once a shipment is in the yard, the next step for warehouse managers is to pull it to an available dock door for unloading. The user can right-click on a shipment in the yard to see the available options:

[![OTM yard right-click options](https://blogger.googleusercontent.com/img/a/AVvXsEiQvVB_Q0--A6pO52uJlQO5dW-apfIq_C8GWJxQ90miFtkSUJHXiKgEto1im9Nu1qU4ueTsxv_GyNqJ8-l2VlXgLgDlAd1f3STpf3VtfxlPwm8ox9AByuYeHYp4b9OVIPNXncc4V2imbcs1lAASejK0AYuQatJQLPeDQQTB0452HTKNB04dUuqyzLyPQOs=w400-h164)](https://blogger.googleusercontent.com/img/a/AVvXsEiQvVB_Q0--A6pO52uJlQO5dW-apfIq_C8GWJxQ90miFtkSUJHXiKgEto1im9Nu1qU4ueTsxv_GyNqJ8-l2VlXgLgDlAd1f3STpf3VtfxlPwm8ox9AByuYeHYp4b9OVIPNXncc4V2imbcs1lAASejK0AYuQatJQLPeDQQTB0452HTKNB04dUuqyzLyPQOs)

Click action 'Yard - Schedule Appointment - Show Options'. This shows appointment options for all available resources. Select the resource and time slot, then click Submit to create an appointment.

[![OTM appointment scheduling options screen](https://blogger.googleusercontent.com/img/a/AVvXsEgDZ4BqhBRybFT9kqXvLjOeY6yOsfYO_c45nrIn0VSVik9dAwsbnr-QqEs94ZvY4awlUUphXdVV5UO1x6nH3aeDUh_yjLNKtbg2m8ZcUm2pIMtPitgOAxH9C-ch1j5sHmoOEgoe_Tnkco4SsT8-cudEpxeVd1BvlKXCTbWAl6woObL7Khby3GESpmftakI=w640-h214)](https://blogger.googleusercontent.com/img/a/AVvXsEgDZ4BqhBRybFT9kqXvLjOeY6yOsfYO_c45nrIn0VSVik9dAwsbnr-QqEs94ZvY4awlUUphXdVV5UO1x6nH3aeDUh_yjLNKtbg2m8ZcUm2pIMtPitgOAxH9C-ch1j5sHmoOEgoe_Tnkco4SsT8-cudEpxeVd1BvlKXCTbWAl6woObL7Khby3GESpmftakI)

Now go to Actions > Manage Appointments screen:

[![OTM Manage Appointments screen](https://blogger.googleusercontent.com/img/a/AVvXsEiUvr1lkg6fokhZBEBFdPA1lQAZYnOxtSKvBAHZ6kPjFLPr6QgopV2cXkOCEqoG3kLzGKr4cksXnBRe4eEZXEUzp2Ke_C2C4S5-G5LkQY0cTzhsQg4ZTXeiXD7rrq6Nr6_vnc-Xlu3E-Vyes56LpIrg2_hDX3cCq1TUbWWGd7gLr5oN9OzZJ8UzC8TQiAo=w640-h181)](https://blogger.googleusercontent.com/img/a/AVvXsEiUvr1lkg6fokhZBEBFdPA1lQAZYnOxtSKvBAHZ6kPjFLPr6QgopV2cXkOCEqoG3kLzGKr4cksXnBRe4eEZXEUzp2Ke_C2C4S5-G5LkQY0cTzhsQg4ZTXeiXD7rrq6Nr6_vnc-Xlu3E-Vyes56LpIrg2_hDX3cCq1TUbWWGd7gLr5oN9OzZJ8UzC8TQiAo)

You can see the shipment added to the time slot against the selected resource (dock door). The time interval slot duration can be configured from the location resource screen:

[![OTM location resource time slot configuration](https://blogger.googleusercontent.com/img/a/AVvXsEg5BGJIjMx7OA7wFrF7hd7x8Z16dbn_MkSkc48A-ZdZK6Ld47i_cQN-yI2IRHcCENlMGYXc9eQhrNJ1qphahAFL4efCKWutf_1b_HDEWxk4PIMhEfoUZkVcoEMTkwJZC50UoiUGD2ftV1uoRUUZUkv9UWWtWlMn4dZaVZzxNS9g34eYzYwDTR9OmXKTdSw=w640-h234)](https://blogger.googleusercontent.com/img/a/AVvXsEg5BGJIjMx7OA7wFrF7hd7x8Z16dbn_MkSkc48A-ZdZK6Ld47i_cQN-yI2IRHcCENlMGYXc9eQhrNJ1qphahAFL4efCKWutf_1b_HDEWxk4PIMhEfoUZkVcoEMTkwJZC50UoiUGD2ftV1uoRUUZUkv9UWWtWlMn4dZaVZzxNS9g34eYzYwDTR9OmXKTdSw)

The display value on the appointment slot can be configured via glog property:

```
glog.appointment.displayString.shipment=objectRefnum:<shipment qualifier GID>
```

**Appointment Rule Sets:**

To automate appointment scheduling using business rules, follow these steps:

- Identify business criteria to match shipments to specific dock doors. For example, all TL shipments should be assigned to Dock Door A and all LTL shipments to Dock Door B.
- Go to Location > Resource > Resource Type screen and attach an appointment rule set with criteria against each location resource. In the above example, Mode Profile ID can be set to TL for Dock Door A and LTL for Dock Door B.
- On Resource Type, enable 'Auto Schedule' and 'Constraint Appointment'.
- <div class="note-box"><strong>Note:</strong> If standard fields on the Appointment Rule Set do not cover required fields, you can use shipment reference numbers and flex fields. These refnum and flex fields can be populated via the shipment creation workflow or any business event occurring before appointment scheduling.</div>
- Once resources are configured with appointment rule sets, use the following standard action to automatically schedule appointments from the shipment workflow:

[![OTM standard action for automatic appointment scheduling](https://blogger.googleusercontent.com/img/a/AVvXsEj_2LF23cUf2AgEDTKC7PWsISp_BYtcC_gN1iSrk4MqFKdhTrzbqvcEJHwUfBo4xo8kOX918p7EYDsqT2if1Ug500oFWmC9XK4H5jFr-MyyrdoN9iuqOYYt4HfUE4S4NThpPu9JywYsNqv6iKLnLN44Mr_ssIBqj8lwenmF4s9qz_4aM4WP8aKKGSIU8W0=w640-h278)](https://blogger.googleusercontent.com/img/a/AVvXsEj_2LF23cUf2AgEDTKC7PWsISp_BYtcC_gN1iSrk4MqFKdhTrzbqvcEJHwUfBo4xo8kOX918p7EYDsqT2if1Ug500oFWmC9XK4H5jFr-MyyrdoN9iuqOYYt4HfUE4S4NThpPu9JywYsNqv6iKLnLN44Mr_ssIBqj8lwenmF4s9qz_4aM4WP8aKKGSIU8W0)
