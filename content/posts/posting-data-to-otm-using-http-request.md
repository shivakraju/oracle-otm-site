---
title: "Post Data to OTM via HTTP Request"
date: 2026-03-04T21:37:00+00:00
draft: false
weight: 65
tags:
  - "UTL_HTTP"
  - "PLSQL"
  - "BEGIN_REQUEST"
  - "SET_HEADER"
  - "WRITE_TEXT"
  - "READ_TEXT"
  - "END_RESPONSE"
  - "UTL_HTTP.req"
  - "UTL_HTTP.resp"
aliases:
  - "/2026/03/posting-data-to-otm-using-http-request.html"
keywords:
  - "Oracle OTM HTTP POST integration PLSQL"
  - "OTM WMServlet HTTP request"
  - "Oracle OTM UTL_HTTP post XML"
  - "OTM PLSQL inbound integration"
  - "Oracle OTM GC3 WMServlet endpoint"
  - "OTM UTL_HTTP.req UTL_HTTP.resp"
  - "Oracle OTM post location via HTTP"
  - "OTM EBS SAP integration HTTP post"
  - "Oracle Transportation Management REST HTTP integration"
  - "OTM programmatic XML post from Oracle DB"
description: "Shows how to post GlogXML data to Oracle OTM using a PL/SQL UTL_HTTP program targeting the WMServlet endpoint, with a complete working code example for loading a Location record."
---

If your source system is an Oracle database — such as Oracle E-Business Suite (EBS) — you can post GlogXML data directly to OTM using PL/SQL without requiring a middleware layer. This is done using Oracle's built-in `UTL_HTTP` package, which allows a PL/SQL program to make HTTP requests to external URLs.

This approach is useful for simple, direct integrations where installing or configuring a middleware platform is not practical. For more complex scenarios involving multiple source systems or non-XML formats such as EDI or flat files, a dedicated middleware tool such as Oracle SOA/BPEL, webMethods, or MuleSoft is a better fit — see the [Inbound Integrations (XML)](/posts/otm-inbound-integrations-xml/) topic for an overview of all available methods.

**Prerequisites:**

<div class="field-box"><strong>UTL_HTTP access:</strong> The Oracle database user running this code must have the <code>EXECUTE</code> privilege on <code>UTL_HTTP</code>. In Oracle 12c and later, an Oracle Wallet must also be configured if you are connecting to OTM over HTTPS.</div>

<div class="field-box"><strong>OTM WMServlet URL:</strong> You need the OTM application server URL. The WMServlet endpoint follows this pattern: <code>http://&lt;OTM-SERVER&gt;:&lt;PORT&gt;/GC3/glog.integration.servlet.WMServlet</code></div>

<div class="field-box"><strong>OTM credentials:</strong> A valid OTM username and password. For production use, create a dedicated integration user with appropriate domain access — do not use DBA.ADMIN.</div>

**How it works:**

The PL/SQL program builds a GlogXML-formatted XML string, then uses `UTL_HTTP` to POST it to the OTM WMServlet endpoint. OTM receives the request, processes the XML, and returns a response containing the transmission number. You can then query the Transmission Manager in OTM using that number to verify whether the data was processed successfully.

**Complete PL/SQL Example — Load a Location record:**

```sql
DECLARE

  -- OTM WMServlet endpoint URL
  v_chr_url      VARCHAR2(1000) := 'http://OTM-SERVER:7777/GC3/glog.integration.servlet.WMServlet';

  -- XML payload variable — build this string programmatically from your source data
  v_data_in      VARCHAR2(32767);

  -- UTL_HTTP request and response handles
  v_http_req     UTL_HTTP.req;
  v_http_resp    UTL_HTTP.resp;
  v_chr_resp_val VARCHAR2(3000);

BEGIN

  -- Build the GlogXML transmission payload
  -- GLogXMLElement here is 'Location' — replace with the appropriate OTM element
  -- for the data you want to load (e.g. OrderRelease, Shipment, ServiceProvider, etc.)
  -- Refer to GlogXML.xsd in OTM for the full element structure:
  --   Business Process Automation > Integration > Integration Manager > Retrieve Schemas
  v_data_in :=
    '<Transmission xmlns="http://xmlns.oracle.com/apps/otm/transmission/v6.4">
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
                 <DomainName>YOURDOMAIN</DomainName>
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
     </Transmission>';

  -- Configure UTL_HTTP timeouts and exception handling
  UTL_HTTP.set_transfer_timeout(1000);
  UTL_HTTP.set_detailed_excp_support(ENABLE => TRUE);

  -- Open the HTTP POST request to OTM WMServlet
  v_http_req := UTL_HTTP.begin_request(v_chr_url, 'POST');

  -- Set HTTP headers — content-type must be text/xml for OTM to parse the body correctly
  UTL_HTTP.set_header(v_http_req, 'content-type',   'text/xml');
  UTL_HTTP.set_header(v_http_req, 'content-length',  LENGTH(v_data_in));

  -- Write the XML payload to the request body
  UTL_HTTP.write_text(v_http_req, v_data_in);

  -- Read OTM's response — it will contain the Reference Transmission Number
  v_http_resp    := UTL_HTTP.get_response(v_http_req);
  UTL_HTTP.read_text(v_http_resp, v_chr_resp_val, 3000);
  UTL_HTTP.end_response(v_http_resp);

  -- Print the response to verify the transmission number
  DBMS_OUTPUT.put_line('OTM Response: ' || v_chr_resp_val);

END;
/
```

**Key Points in the Code:**

<div class="field-box"><strong>v_data_in:</strong> This is where you build the XML payload. In a real integration, you would construct this string dynamically from your source tables — for example, querying customer or location data from EBS and mapping it to the OTM XML structure.</div>

<div class="field-box"><strong>content-type: text/xml:</strong> This header is required for OTM to correctly parse the XML body. Using <code>text/html</code> can cause the WMServlet to reject or mishandle the payload.</div>

<div class="field-box"><strong>GLogXMLElement:</strong> Change this element to match the OTM object you want to load — <code>OrderRelease</code>, <code>Shipment</code>, <code>ServiceProvider</code>, <code>RateOffering</code>, and so on. Refer to <code>GlogXML.xsd</code> for the correct structure of each element.</div>

<div class="field-box"><strong>OTM Response:</strong> OTM returns a transmission acknowledgement XML containing a <code>ReferenceTransmissionNo</code>. Use this number to query the Transmission Manager and confirm that the record was processed without errors.</div>

<div class="field-box"><strong>TransactionCode IU:</strong> Stands for Insert or Update. OTM inserts the record if the GID does not exist, or updates it if it does. Use <code>D</code> to delete a record.</div>

**Verifying the Result in OTM:**

After running the PL/SQL block, note the transmission number from the response output. Then navigate to:

Business Process Automation > Integration > Transmission Manager

Query for the transmission number. The status should show as **PROCESSED**. If there are errors, click the **Report** button for details.

<div class="note-box"><strong>Note:</strong> If you are building multiple integrations from an external system — especially when the source data arrives in non-XML formats such as EDI, fixed-width flat files, or proprietary formats — a middleware platform such as Oracle SOA/BPEL, webMethods, or MuleSoft is the recommended approach. These tools provide transformation, routing, error handling, and monitoring capabilities that are difficult to replicate in custom PL/SQL code.</div>

**What's Next:**

The next topic covers OTM Outbound Integrations — how OTM sends data to external systems such as carrier platforms, ERP applications, and middleware.

Next Topic: [Outbound Integrations](/posts/otm-outbound-integrations/)
