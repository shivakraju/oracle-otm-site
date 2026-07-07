---
title: "Business Process Automation Data Structure"
date: 2016-05-06T20:15:00+00:00
draft: false
weight: 140
tags:
  - "Agent"
  - "Reports"
  - "Integration"
  - "Contacts"
  - "External System"
aliases:
  - "/2016/05/business-process-automation-data.html"
---

As the name suggests, this module in OTM mainly deals with technical configurations that can be done in OTM for various client specific requirements.  
  
Contacts  
  
Contact in OTM should be defined for any communication that you want to initiate from system to end users(via email, etc) or external systems(via integration, etc). Following are entities in OTM that would be associated to contact:  
Users  
External Systems  
Locations  
Service Providers  
Involved Parties  
Agent Notify Contact Actions  
  
**Tables:**  
CONTACT  
CONTACT_COM_METHOD  
  
External System   
  
This is used to define any system(like middleware tool etc) to which you want to send outbound Glog XMLs. You will typically associate an XML profile to control what data you are sending to external system.  
  
**Tables:**  
EXTERNAL_SYSTEM  
EXTERNAL_SYSTEM_OUT_XML  
  
Agents  
  
These are workflows that trigger based on events happening with in the OTM system. Agents can be of two types - standard OTM agents that come out of box or developers can create custom agents for client specfic requirements. Agents can be triggered using standard OTM events like ORDER - CREATED, etc or custom events created by developers.We will learn in detail about Agents in a future topic.  
  
**Tables:**  
AGENT  
AGENT_ACTION  
AGENT_ACTION_DETAILS  
AGENT_EVENT  
AGENT_EVENT_DETAILS  
  
Sample Query to search for specific text within agent code:  
  
SELECT aad.*  
FROM agent_action_details aad,  
agent ag  
WHERE upper(aad.action_parameters) like upper('%TEXT TO SEARCH%')  
AND aad.agent_gid = ag.agent_gid  
AND ag.is_active = 'Y'    
  
Sample Query to find all parent agents that raise a given event:  
  
SELECT a.agent_gid,  
a.description,  
action_sequence  
FROM agent a,  
agent_action_details aad  
WHERE a.agent_gid = aad.agent_gid  
AND is_active = 'Y'  
AND aad.agent_action_gid IN ('RAISE EVENT', 'FOR EACH')  
AND action_parameters LIKE '%custom event text%'  
  
Reports  
  
Report in OTM can be developed with expertise in SQL and BI Publisher tool. We will discuss in detail in a future post on how to create a custom report in OTM.  
  
**Tables:**  
**Note:** All below tables exist in REPORTOWNER schema. They can be also be accessed from GLOGOWER schema with same name because OTM created PUBLIC synonyms with same names.   
  
REPORT  
REPORT_PARAMETER  
  
Report Set is used to group reports. This is used in REPORT agent actions like PRINT DOCUMENT action, etc  
  
REPORT_SET  
REPORT_SET_DETAIL  
  
Report log and parameters table hold information(like output file name, input parameter values, etc) about reports:  
  
REPORT_LOG  
REPORT_LOG_PARAMETER  
  
Sample SQL to fetch Shipment ID based on the Output file name:  
  
SELECT rlp.parameter_value  
FROM report_log_parameter rlp  
WHERE rlp.file_name = $GID  
AND rlp.parameter_name = 'P_SHIPMENT_ID'   
  
Integration    
  
OTM Inbound and Outbound Integration transmissions are recorded for every transaction with XML files, Error Details, etc.  
  
**Tables:**  
I_TRANSMISSION - Transmission header table with details like transmission status, external system name(for outbound), etc  
I_TRANSACTION - Transmission detail table at transaction(object) level that holds XML, XML Element Name( like TransOrder, OrderRelease, etc)  
I_LOG - This table shows the error details for transactions  
  
**Sample query to find transaction error details:**  
  
select it.i_transmission_no,il.i_transaction_no,dbms_lob.substr(il.i_message_text,200)  
from I_TRANSACTION it,  
i_log il  
where it.insert_date > sysdate-1   
and i_transmission_no = <Enter Transmission No>   
and element_name = 'ShipmentStatus'   
and transaction_code = 'I'  
and it.status = 'ERROR'  
and it.i_transaction_no = il.i_transaction_no