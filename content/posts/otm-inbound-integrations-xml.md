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
---

There are several ways of bringing in data into OTM system. Below are some of the methods:

  * via XML that follows Glog XML schema posted from a middleware applications like Oracle SOA, webMethods, Mulesoft, etc
  * Manaul XML uploads by OTM users
  * CSV Uploads
  * DB.XML Uploads
  * REST-API Calls
  * HTTP Post Requests from programming languages like PLSQL, etc

**XML Inbound Integrations:**

  

Most common way of receiving OTM Inbound data is via XML files from middleware applications. OTM can read XML files which are in the format specified by GlogXML Schema(OTM Standard XML Schema). You can download this schema from :  
  
Business Process Automation > Integration > Integration Manager > Retrieve Schemas > GlogXML.xsd  
  
This file will describe the data structure for each OTM element like 'Location', 'Order Release', 'Shipment', etc along with some documentation.  
  
Say, if we want to upload a new location to OTM, you follow below steps:  
  
1\. Read the GlogXML.xsd and identify the XML structure for element "Location". Once you map your input data values to OTM XML elements, you will end up coming with XML file similar to one below:  

  * <Transmission>  
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
<Xid>TEST SH OTM CORPORATION-45769</Xid>  
</Gid>  
</LocationGid>  
<LocationName>TEST SH OTM COR,CLUTE,TX,USA</LocationName>  
<Address>  
<AddressLines>  
<SequenceNumber>1</SequenceNumber>  
<AddressLine>1039 EAST PLANTATION</AddressLine>  
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
<Gid>  
<Xid>ORIGIN</Xid>  
</Gid>  
</LocationRefnumQualifierGid>  
<LocationRefnumValue>CUSTOMER</LocationRefnumValue>  
</LocationRefnum>  
<LocationRefnum>  
<LocationRefnumQualifierGid>  
<Gid>  
<Xid>CUSID</Xid>  
</Gid>  
</LocationRefnumQualifierGid>  
<LocationRefnumValue>1130</LocationRefnumValue>  
</LocationRefnum>  
<LocationRefnum>  
<LocationRefnumQualifierGid>  
<Gid>  
<Xid>CUSNM</Xid>  
</Gid>  
</LocationRefnumQualifierGid>  
<LocationRefnumValue>MOORE SUPPLY CO</LocationRefnumValue>  
</LocationRefnum>  
<LocationRole>  
<LocationRoleGid>  
<Gid>  
<Xid>CUSTOMER</Xid>  
</Gid>  
</LocationRoleGid>  
</LocationRole>  
<Corporation>  
<CorporationName>OTM CORPORATION</CorporationName>  
</Corporation>  
</Location>  
</GLogXMLElement>  
</TransmissionBody>  
</Transmission>

2. Save this file with extension '.xml'  

3. Once you have XML ready, you can upload to OTM as below: Goto Business Process Automation -> Integration -> Integration Manager -> Upload XML/CSV Transmission and Browse XML File. 

4. Click Upload.

  
  

**5. You will see following log:**

  

![](/images/otm-inbound-integrations-xml-img1-364ef35ae6.png)

  

6. Note the transmission number from the log

7. Navigate to Business Process Automation -> Integration -> Transmission Manager

8. Query for transmission and you should see transmission status as ‘PROCESSED’. 

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8yx-abkjdZ-Dk5gx-oYVUSbER84jrRRqwdd5lYEM4YKwWV3xKTSeiv6DJt0Rz3iVKmfob3T68LFVX6_QfHGjVamEjedqI1O8y78akuyDqVzutH8Rq68QAhS5Kcs9GhgylAUbACAT1SdU/s1600/Transmission.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8yx-abkjdZ-Dk5gx-oYVUSbER84jrRRqwdd5lYEM4YKwWV3xKTSeiv6DJt0Rz3iVKmfob3T68LFVX6_QfHGjVamEjedqI1O8y78akuyDqVzutH8Rq68QAhS5Kcs9GhgylAUbACAT1SdU/s1600/Transmission.png)

  

In case of errors Report button displays error reasons like foreign key reference missing etc.

  

Posting XML from Other middleware applications like Oracle SOA/BPEL, webMethods, Mulesoft, etc

Middleware applications can post XML using below details:

  

**Method:** POST

**OTM Servlet:** https://<OTM Application URL>/GC3/glog.integration.servlet.WMServlet

**Body Type:** Raw

**File format:** XML

**Authorization:** Basic Auth (Get domain INTEGRATION username and password credentials from OTM Admin)

  

**Sample Payload to update VOUCHER status:**

  

<Transmission xmlns="http://xmlns.oracle.com/apps/otm/transmission/v6.4">

<TransmissionHeader>

<AckSpec>

<ComMethodGid>

<Gid>

<Xid>HTTPPOST</Xid>

</Gid>

</ComMethodGid>

<AckOption>ERROR</AckOption>

</AckSpec>

</TransmissionHeader>

<TransmissionBody>

<GLogXMLElement>

<GenericStatusUpdate>

<GenericStatusObjectType>VOUCHER</GenericStatusObjectType>

<Gid>

<DomainName>DPSCM</DomainName>

<Xid>20240823-00001310</Xid>

</Gid>

<TransactionCode>IU</TransactionCode>

<Status>

<StatusTypeGid>

<Gid>

<DomainName>DPSCM</DomainName>

<Xid>PAYMENT STATUS</Xid>

</Gid>

</StatusTypeGid>

<StatusValueGid>

<Gid>

<DomainName>DPSCM</DomainName>

<Xid>PAYMENT_RECEIVED</Xid>

</Gid>

</StatusValueGid>

</Status>

</GenericStatusUpdate>

</GLogXMLElement>

</TransmissionBody>

</Transmission>

  

**Sample Response from OTM for above request:**

  

<otm:TransmissionAck xmlns:otm="http://xmlns.oracle.com/apps/otm/transmission/v6.4" xmlns:gtm="http://xmlns.oracle.com/apps/gtm/transmission/v6.4">

<otm:EchoedTransmissionHeader>

<otm:TransmissionHeader>

<otm:ReferenceTransmissionNo>311245595</otm:ReferenceTransmissionNo>

<otm:AckSpec>

<otm:ComMethodGid>

<otm:Gid>

<otm:Xid>HTTPPOST</otm:Xid>

</otm:Gid>

</otm:ComMethodGid>

<otm:AckOption>ERROR</otm:AckOption>

</otm:AckSpec>

</otm:TransmissionHeader>

</otm:EchoedTransmissionHeader>

</otm:TransmissionAck>

  

Using Reference Transmission Number, you can query OTM transmission screen to see if the message is posted to OTM without any errors.

  

**Other methods:**

  

Review below topics for loading data into OTM using other methods:

  

https://www.oracle-otm.com/2026/03/csv-data-uploads.html

  

https://www.oracle-otm.com/2026/03/posting-data-to-otm-using-http-request.html

  
**Note:** Please post corrections(if any) to 'learnotm@outlook.com'