---
title: "Outbound Integrations"
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
keywords:
  - "Oracle OTM outbound integration setup"
  - "OTM Out XML Profile configuration"
  - "Oracle OTM send interface transmission"
  - "OTM outbound GlogXML generation"
  - "Oracle OTM external system integration"
  - "OTM MIN mode XML profile"
  - "Oracle OTM agent outbound XML"
  - "OTM shipment outbound XML"
  - "Oracle Transportation Management outbound file setup"
  - "OTM integration middleware webMethods"
  - "Oracle OTM XPath Out XML Profile"
description: "Step-by-step guide to configuring Oracle OTM outbound integrations using Out XML Profiles and the Send Interface Transmission action, including how to control output data with MIN mode and XPath filters."
---

OTM can generate outbound XML data for any business object — Order Release, Shipment, Invoice, and more — and send it to an external system such as a carrier platform, ERP, or middleware. This can be triggered manually using the **Send Interface Transmission** action, or automatically from an OTM Agent (workflow). OTM Agents are covered in a later topic.

There are three things you need to set up before OTM can send outbound data:

<div class="field-box"><strong>Out XML Profile:</strong> Controls which fields are included in the outbound XML. Without this, OTM generates a complete XML for the object which can be very large (a Shipment XML can be several MB). The profile lets you trim it down to only what the receiving system needs.</div>

<div class="field-box"><strong>External System:</strong> Defines the destination — the URL or web service endpoint where OTM will POST the XML, along with authentication credentials and the Out XML Profile to use.</div>

<div class="field-box"><strong>Send Interface Transmission action:</strong> The action that triggers OTM to generate the XML and send it to the External System. Can be run manually from any object's Actions menu, or fired by an OTM Agent on a business event.</div>

**Step by Step — Configure OTM Outbound Integration:**

<div class="step-box">
<strong>Step 1 — Create an Out XML Profile</strong>

Navigate to:

Business Process Automation > Power Data > Integration > Out XML Profiles

Create a new profile and set **Default Mode** to `MIN`. Then add XPath expressions for each field you want to include in the outbound XML. Using MIN mode means OTM only outputs the fields you explicitly list — everything else is excluded. This keeps the XML compact and relevant to the receiving system.
</div>

> ![OTM Out XML Profile screen showing MIN mode and XPath configuration](/images/otm-outbound-xml-profile.jpg)

<div class="step-box">
<strong>Step 2 — Create an External System</strong>

Navigate to:

Business Process Automation > Communication Management > External Systems

Create a new External System record and fill in the following fields:
</div>

<div class="field-box"><strong>External System ID:</strong> A unique identifier for the destination system (e.g. EBS, CARRIER-PORTAL, MIDDLEWARE).</div>

<div class="field-box"><strong>User Name / Password:</strong> Credentials sent to the external application for authentication. These are included in the outbound request.</div>

<div class="field-box"><strong>URL / Web Service:</strong> The HTTPS endpoint or web service URL where OTM will POST the generated XML.</div>

<div class="field-box"><strong>Out XML Profile ID:</strong> Link the profile created in Step 1. OTM uses this to determine which fields to include in the XML before sending.</div>

> ![OTM External System definition screen](/images/otm-outbound-external-system1.png)

> ![OTM External System showing URL and Out XML Profile fields](/images/otm-outbound-external-system2.png)

<div class="step-box">
<strong>Step 3 — Send a transmission manually</strong>

To test the setup or trigger a one-off outbound send, open the object you want to send (e.g. a Shipment) and navigate to:

Shipment > Actions > Utilities > Send Interface Transmission

Select the External System defined in Step 2 and choose the appropriate notification type — **HTTP** for a direct URL post, or **Service** for a web service call. Click **Send**.
</div>

> ![OTM Send Interface Transmission dialog showing External System selection](/images/otm-outbound-send-transmission.png)

<div class="step-box">
<strong>Step 4 — Verify the generated XML</strong>

Navigate to:

Business Process Automation > Integration > Transmission Manager > Transactions Tab

Enter the Object GID in the **Object** field and search. OTM displays the Transmission Result. Click **Raw XML** to view the actual XML that was generated and sent to the external system.
</div>

<div class="note-box"><strong>Note:</strong> In a production implementation, the Send Interface Transmission step is typically automated using an OTM Agent that fires on a business event — for example, sending a shipment XML to a carrier whenever a shipment status changes to TENDERED. Manual triggering (Step 3) is mainly used for testing and troubleshooting.</div>

**Configuring a Web Service for the External System:**

If your external system exposes a SOAP web service endpoint (common with middleware platforms such as Oracle SOA/BPEL), you need to register that web service in OTM and link it to the External System. This is an alternative to the simple HTTP POST URL approach — use it when the receiving system requires a WSDL-based service call.

<div class="step-box">
<strong>Step A — Create a new Web Service in OTM</strong>

Navigate to:

Business Process Automation > Communication Management > Web Services

Click **New**.
</div>

> ![OTM Web Services screen — new Web Service form with WSDL Document field](/images/otm-webservice-new-form.png)

On the new Web Service form, click **+** next to the WSDL Document field to upload the WSDL file. You will be prompted to enter a Document Type and Content Management System.

> ![OTM Document Type and Content Management System selection](/images/otm-webservice-document-type.png)

Click **Document Detail**. Enter a Document ID (e.g. `YOUR_WEBSERVICE_WSDL`) and click **Upload** to upload the WSDL file provided by your middleware team. Click **Finished**.

<div class="step-box">
<strong>Step B — Review Service Details auto-populated from the WSDL</strong>

Back on the Web Service form, click **Service Details**. OTM reads the uploaded WSDL file and automatically populates the Service Name, Namespace, Port Name, SOAP Encoding, and Operations.
</div>

> ![OTM Web Service — WSDL linked, Service Details button highlighted](/images/otm-webservice-wsdl-linked.png)

Enter a **Service ID** and click **Finished**. The Service ID is how you will reference this web service from the External System.

<div class="step-box">
<strong>Step C — Create the External System and link the Web Service</strong>

Navigate to:

Business Process Automation > Communication Management > External Systems

Click **New**. Enter an External System ID and click **Finished**.
</div>

> ![OTM External System form showing ID, credentials, and configuration options](/images/otm-external-system-form.png)

Open the External System again. Navigate to the **Web Service** section and enter the Web Service ID you created in Step B. Click **Finished**.

> ![OTM External System — Web Service tab showing Out XML Profiles section](/images/otm-external-system-webservice-tab.png)

<div class="step-box">
<strong>Step D — Select Service Operation and Service Endpoint</strong>

Open the External System once more and set the **Service Operation** and **Service Endpoint** dropdowns — these are populated from the WSDL. Click **Finished**.
</div>

> ![OTM External System — Service Operation and Service Endpoint fields highlighted](/images/otm-external-system-service-operation.png)

<div class="step-box">
<strong>Step E — Test by sending a transmission</strong>

Open a test Shipment (or any object) and go to:

Actions > Utilities > Send Interface Transmission
</div>

> ![OTM Shipment Actions menu showing Send Interface Transmission option](/images/otm-send-interface-transmission-menu.png)

Enter the External System ID and set **Notify Type** to **SERVICE**. Click **Send**.

> ![OTM Send Interface Transmission dialog — External System and SERVICE notify type highlighted](/images/otm-send-interface-transmission-dialog.png)

In the Transmission Manager, you should see the outbound transmission with status **PROCESSED**.

> ![OTM Transmission Manager showing PROCESSED and ERROR status rows](/images/otm-transmission-manager-processed.png)

**What's Next:**

The next topic covers OTM Domains, Standard Schema and Data Dictionary — foundational reference material that explains how OTM organises data across domains and where to find field-level documentation.

Next Topic: [OTM Domains, Standard Schema and Data Dictionary](/posts/otm-domains-standard-schema-and-data-dictionary/)
