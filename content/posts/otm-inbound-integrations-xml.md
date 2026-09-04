---
title: "OTM Inbound Integrations (XML)"
date: 2016-04-15T18:20:00+00:00
draft: false
weight: 60
tags:
  - "Integration"
  - "upload"
  - "Schema"
  - "CSV"
  - "GlogXML"
  - "OTM"
  - "Inbound"
  - "example"
  - "Integrations"
  - "XML"
  - "Servlet"
  - "PLSQL"
  - "Learn"
  - "API"
  - "Oracle"
  - "Glog"
aliases:
  - "/2016/04/otm-inbound-integrations.html"
keywords:
  - "Oracle OTM inbound integration GlogXML"
  - "OTM XML upload WMServlet"
  - "Oracle OTM GlogXML schema inbound"
  - "OTM integration via Oracle SOA webMethods Mulesoft"
  - "Oracle OTM CSV upload integration"
  - "OTM DB.XML upload"
  - "Oracle OTM REST API integration"
  - "OTM PLSQL HTTP post integration"
  - "Oracle Transportation Management data loading methods"
  - "OTM manual XML upload process"
  - "GlogXML inbound data structure OTM"
description: "Covers the multiple methods for loading data into Oracle OTM, including GlogXML posts via middleware, manual XML uploads, CSV uploads, DB.XML uploads, REST-API calls, and PLSQL HTTP requests."
---

OTM supports several methods for receiving data from external systems. This topic covers XML-based integrations, which are the most common approach in OTM implementations.

**Integration Methods Overview:**

<div class="field-box"><strong>GlogXML via Middleware:</strong> XML files following the GlogXML schema, posted to OTM from middleware platforms such as Oracle SOA/BPEL, webMethods, or MuleSoft. This is the most common approach for production integrations.</div>

<div class="field-box"><strong>Manual XML Upload:</strong> OTM users manually upload a GlogXML-formatted XML file through the OTM Integration Manager screen. Useful for testing, one-time loads, or small data corrections.</div>

<div class="field-box"><strong>CSV Upload:</strong> Uploading data using comma-separated value files for supported OTM entities. See the <a href="/posts/csv-data-uploads/">CSV Data Uploads</a> topic for details.</div>

<div class="field-box"><strong>DB.XML Upload:</strong> A method for loading data directly using database-level XML files, typically used in implementations or data migrations.</div>

<div class="field-box"><strong>REST API:</strong> Newer versions of OTM support REST API-based integrations for querying and updating OTM data without using GlogXML format.</div>

<div class="field-box"><strong>HTTP Post from Code:</strong> Custom programs written in PL/SQL, Java, or other languages can post GlogXML directly to the OTM WMServlet endpoint. See the <a href="/posts/posting-data-to-otm-using-http-request/">Post Data via HTTP Request</a> topic for details.</div>

**GlogXML Schema:**

OTM's standard XML format is defined by the **GlogXML schema** (`GlogXML.xsd`). This schema describes the XML structure for every OTM entity — Location, Order Release, Shipment, Service Provider, Rate Offering, and more — along with field-level documentation. You can download the schema from inside OTM at:

Shipment Management > Business Process Automation > Integration > Integration Manager > Retrieve Schemas > GlogXML.xsd

Open the downloaded XSD file in any XML or text editor to look up the structure for the entity you want to load.

**Manual XML Upload — Step by Step:**

The following example shows how to manually upload a Location record to OTM using a GlogXML XML file. Location is used here as an example — the same approach applies to any other OTM business object such as Order Base, Order Release, Shipment, Service Provider, Rate Offering, Invoice, and more. The only difference is the GLogXMLElement you choose inside the transmission body.

<div class="step-box">
<strong>Step 1 — Build your XML file</strong>

Read `GlogXML.xsd` and identify the XML structure for the entity you want to load (e.g. `Location`). Map your source data values to the OTM XML fields. A sample Location XML file looks like this:
</div>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Transmission xmlns="http://xmlns.oracle.com/apps/otm/transmission/v6.4">
  <TransmissionHeader>
    <UserName>DBA.ADMIN</UserName>
    <Password>CHANGEME</Password>
    <IsProcessInSequence>Y</IsProcessInSequence>
  </TransmissionHeader>
  <TransmissionBody>
    <GLogXMLElement>
      <Location>
        <TransactionCode>IU</TransactionCode>
        <LocationGid>
          <Gid>
            <DomainName>ABC</DomainName>
            <Xid>TEST-LOCATION-001</Xid>
          </Gid>
        </LocationGid>
        <LocationName>Test Location, Houston, TX, USA</LocationName>
        <Address>
          <AddressLines>
            <SequenceNumber>1</SequenceNumber>
            <AddressLine>1039 East Plantation Drive</AddressLine>
          </AddressLines>
          <City>CLUTE</City>
          <ProvinceCode>TX</ProvinceCode>
          <PostalCode>77531</PostalCode>
          <CountryCode3Gid>
            <Gid><Xid>USA</Xid></Gid>
          </CountryCode3Gid>
        </Address>
        <LocationRefnum>
          <LocationRefnumQualifierGid>
            <Gid><Xid>ORIGIN</Xid></Gid>
          </LocationRefnumQualifierGid>
          <LocationRefnumValue>CUSTOMER</LocationRefnumValue>
        </LocationRefnum>
        <LocationRole>
          <LocationRoleGid>
            <Gid><Xid>CUSTOMER</Xid></Gid>
          </LocationRoleGid>
        </LocationRole>
      </Location>
    </GLogXMLElement>
  </TransmissionBody>
</Transmission>
```

<div class="note-box"><strong>Note:</strong> <code>TransactionCode</code> IU means Insert or Update — OTM will insert the record if it does not exist, or update it if the GID already exists. Use <code>D</code> to delete a record.</div>

<div class="step-box">
<strong>Step 2 — Upload the XML file in OTM</strong>

Navigate to:

Business Process Automation > Integration > Integration Manager > Upload XML/CSV Transmission

Browse for your XML file and click **Upload**.
</div>

<div class="step-box">
<strong>Step 3 — Check the upload log</strong>

After clicking Upload, OTM displays a log showing the transmission number and initial processing status. Note the **Transmission Number** — you will need it to verify the final processing status.
</div>

> ![OTM Integration Manager upload log showing transmission number](/images/otm-inbound-integrations-xml-img1-364ef35ae6.png)

<div class="step-box">
<strong>Step 4 — Verify in Transmission Manager</strong>

Navigate to:

Business Process Automation > Integration > Transmission Manager

Query for your transmission number. The status should show as **PROCESSED**. If there are errors, click the **Report** button to see the error details — common errors include missing foreign key references (e.g. a Domain or Location that does not yet exist in OTM).
</div>

> ![OTM Transmission Manager showing PROCESSED status](/images/otm-inbound-transmission-manager.png)

**Posting XML via Middleware:**

Middleware platforms (Oracle SOA/BPEL, webMethods, MuleSoft, etc.) post GlogXML directly to the OTM WMServlet endpoint using an HTTP POST request.

<div class="field-box"><strong>Method:</strong> POST</div>

<div class="field-box"><strong>URL:</strong> <code>https://&lt;OTM-Application-URL&gt;/GC3/glog.integration.servlet.WMServlet</code></div>

<div class="field-box"><strong>Body Type:</strong> Raw XML</div>

<div class="field-box"><strong>Authorization:</strong> Basic Auth — use the INTEGRATION domain username and password from your OTM Admin.</div>

<div class="note-box"><strong>Note:</strong> For SaaS OTM, the WMServlet URL and credentials are provided by Oracle. The path structure remains the same but the hostname will be Oracle-managed.</div>

**Sample Payload — Update Voucher Status:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Transmission xmlns="http://xmlns.oracle.com/apps/otm/transmission/v6.4">
  <TransmissionHeader>
    <AckSpec>
      <ComMethodGid>
        <Gid><Xid>HTTPPOST</Xid></Gid>
      </ComMethodGid>
      <AckOption>ERROR</AckOption>
    </AckSpec>
  </TransmissionHeader>
  <TransmissionBody>
    <GLogXMLElement>
      <GenericStatusUpdate>
        <GenericStatusObjectType>VOUCHER</GenericStatusObjectType>
        <Gid>
          <DomainName>YOURDOMAIN</DomainName>
          <Xid>20240823-00001310</Xid>
        </Gid>
        <TransactionCode>IU</TransactionCode>
        <Status>
          <StatusTypeGid>
            <Gid>
              <DomainName>YOURDOMAIN</DomainName>
              <Xid>PAYMENT STATUS</Xid>
            </Gid>
          </StatusTypeGid>
          <StatusValueGid>
            <Gid>
              <DomainName>YOURDOMAIN</DomainName>
              <Xid>PAYMENT_RECEIVED</Xid>
            </Gid>
          </StatusValueGid>
        </Status>
      </GenericStatusUpdate>
    </GLogXMLElement>
  </TransmissionBody>
</Transmission>
```

**Sample OTM Response (success — no errors):**

```xml
<otm:TransmissionAck xmlns:otm="http://xmlns.oracle.com/apps/otm/transmission/v6.4">
  <otm:EchoedTransmissionHeader>
    <otm:TransmissionHeader>
      <otm:ReferenceTransmissionNo>311245595</otm:ReferenceTransmissionNo>
      <otm:AckSpec>
        <otm:ComMethodGid>
          <otm:Gid><otm:Xid>HTTPPOST</otm:Xid></otm:Gid>
        </otm:ComMethodGid>
        <otm:AckOption>ERROR</otm:AckOption>
      </otm:AckSpec>
    </otm:TransmissionHeader>
  </otm:EchoedTransmissionHeader>
</otm:TransmissionAck>
```

When `AckOption` is set to `ERROR`, OTM only returns a response if there is an error — a response like the above (with no error element) confirms the transmission was accepted. Use the `ReferenceTransmissionNo` to query the Transmission Manager and confirm the record was processed successfully.

<div class="note-box"><strong>Note:</strong> If you need OTM to always return a response (not just on error), set <code>AckOption</code> to <code>ALWAYS</code> in the TransmissionHeader.</div>

**What's Next:**

If your source system is Oracle E-Business Suite or another Oracle database, you can post GlogXML directly from PL/SQL using the `UTL_HTTP` package — no middleware required. The next topic walks through a complete working example.

Next Topic: [Post Data to OTM via HTTP Request](/posts/posting-data-to-otm-using-http-request/)
