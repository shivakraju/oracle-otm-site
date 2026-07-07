---
title: "Posting Data to OTM using HTTP request"
date: 2026-03-04T21:37:00+00:00
draft: false
weight: 90
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
---

Any external system like EBS, SAP can frame this XML structure programatically and 'POST' this xml to OTM Integration servlet: glog.integration.servlet.WMServlet

Below is an PLSQL program posting Location element to OTM:

```sql
DECLARE

-- This is OTM Application URL Where string after GC3 is replaced as shown below
v_chr_url VARCHAR2(1000) := 'http://OTM-SERVER:7777/GC3/glog.integration.servlet.WMServlet';

-- This is OTM USER from which transmission needs to be created
v_otm_user VARCHAR2(100) := 'DBA.ADMIN';

-- This is password for the OTM USER
v_otm_pwd VARCHAR2(100) := 'CHANGEME';

-- You can programtically form the xml string and pass it to this variable
v_data_in VARCHAR2 (10000);
v_http_req UTL_HTTP.req;
v_http_resp UTL_HTTP.resp;
v_chr_resp_val VARCHAR2 (3000);

BEGIN
-- This is a sample transmission that creates location (Shipment Management -> Location Manager) in OTM
-- Note that in the Transmission Body, GLOGXMLElement chosen here is Location.
-- By choosing appropriate element, you can load required data.
-- In this script file, you see XML structure to send location information.
-- You can get this structure by referring the GLOGXML.xsd
-- Navigation to fetch this from OTM:
--   1. Login in to OTM using DBA.ADMIN user
--   2. Business Process Automation -> Integration -> Integration Manager -> GlogXML.xsd

v_data_in := '<Transmission>
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
          <DomainName>WHD</DomainName>
          <Xid>TEST SH HAJOCA CORPORATION-45769</Xid>
        </Gid>
      </LocationGid>
      <LocationName>TEST SH HAJOCA COR,CLUTE,TX,USA</LocationName>
      <Address>
        <AddressLines>
          <SequenceNumber>1</SequenceNumber>
          <AddressLine>449 TEST PLANTATION</AddressLine>
        </AddressLines>
        <City>CLUTE</City>
        <ProvinceCode>TX</ProvinceCode>
        <PostalCode>32830</PostalCode>
        <CountryCode3Gid>
          <Gid>
            <Xid>USA</Xid>
          </Gid>
        </CountryCode3Gid>
      </Address>
      <LocationRefnum>
        <LocationRefnumQualifierGid>
          <Gid><Xid>ORIGIN</Xid></Gid>
        </LocationRefnumQualifierGid>
        <LocationRefnumValue>CUSTOMER</LocationRefnumValue>
      </LocationRefnum>
      <LocationRefnum>
        <LocationRefnumQualifierGid>
          <Gid><Xid>CUSID</Xid></Gid>
        </LocationRefnumQualifierGid>
        <LocationRefnumValue>1130</LocationRefnumValue>
        <LocationRole>
          <LocationRoleGid>
            <Gid><Xid>CUSTOMER</Xid></Gid>
          </LocationRoleGid>
        </LocationRole>
        <Corporation>
          <CorporationName>TEST CORPORATION</CorporationName>
        </Corporation>
      </LocationRefnum>
    </Location>
  </GLogXMLElement>
</TransmissionBody>
</Transmission>';

UTL_HTTP.set_transfer_timeout (1000);
UTL_HTTP.set_detailed_excp_support (ENABLE => TRUE);

-- Invoking the Web Service.
v_http_req := UTL_HTTP.begin_request (v_chr_url, 'POST');

-- Set the HTTP request headers
UTL_HTTP.set_header (v_http_req, 'content-type', 'text/html');
UTL_HTTP.set_header (v_http_req, 'content-length', LENGTH (v_data_in));

-- Write the data to the body of the HTTP request
UTL_HTTP.write_text (v_http_req, v_data_in);

-- Retrieving response of Transmission ID for OTM
v_http_resp := UTL_HTTP.get_response (v_http_req);
UTL_HTTP.read_text (v_http_resp, v_chr_resp_val, 3000);
UTL_HTTP.end_response (v_http_resp);

END;
/
```

**Note:** If you have multiple integrations to be built from an external system to OTM to load data coming in different formats like EDI, text files, etc. you should typically go for a middleware tool like Oracle SOA(BPEL), Webmethods etc. to translate these files from various formats to the XML format defined by the GlogXML schema.
