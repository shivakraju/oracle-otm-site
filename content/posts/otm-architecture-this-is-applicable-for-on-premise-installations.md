---
title: "OTM Architecture"
date: 2016-04-15T14:54:00+00:00
draft: false
weight: 50
tags:
  - "Installation"
  - "Architecture"
  - "OTM"
  - "Learn"
  - "Management"
  - "Oracle"
  - "Trasportation"
  - "Glog"
  - "3 tier"
aliases:
  - "/2016/04/otm-architecture.html"
---

OTM application has a typical three tier architecture. It has web tier, app tier and oracle database as third tier. These three components can be installed on separate servers (Linux/Windows) or they may be installed on the same server. Usually for lower environment like DEV or TEST they are installed on same server.  

  
At a high level, this OTM product can be installed with below software:  
  
1\. Install Oracle Enterprise Linux - Operating System on the base servers. Note that OTM can be installed either on Linux server or Windows Server.  
  
2\. Install Oracle Database 11g Enterprise Edition - Database Software from Oracle.   
  
3\. Install Oracle Weblogic Server 11g(software on which OTM App tier runs)  
This is where OTM App Tier(part of OTM software) is installed. OTM App tier has the business logic like standard OTM algorithms, OTM Agents(workflows), etc   
  
4\. Install Oracle HTTP Server(software on which OTM Web tier runs). This is where OTM Web Tier(part of OTM software) is installed. OTM Web Tier has static content like OTM Help pages, labels, etc  
  
5\. Install OTM software. OTM Installation steps would basically have below configurations:  

  * Base Path on the servers(app and web) where you want to install OTM. 
  * Configuring OTM Web tier with Web Server IP address and Port(Note that you can have multiple application/programs running on the same server and by knowing IP address request can hit the server and by knowing the port it will hit specific program/application running on the server)
  * Configuring OTM App tier with App Server IP address and Port.
  * Configuring OTM Database with DB Server IP address and Port. 
  * After OTM is installed successfully, on the OTM database run standard scripts provided by OTM to configure OTM Tablespaces, OTM Database Schema(like GLOGOWNER, REPORTOWNER, etc) 

See below diagram that shows software names that are installed on each server. In this example, assume that we are using three different servers - one for OTM web tier software components, one for OTM app tier software components and one for Oracle Database software.  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWtbxKM5vgfxIAYWbwnrRQ_0U76Dexpb1Utvy4lfUaC7FM87CcGRjTnB6vVf4aCWyxi1lCrRNmLhmzHeoFdJ6UQMOycLkiZ6PUK2Xlg18la_sireahVRfjwEtXKX6_XqwI7u7HJ1ueVmE/s640/OTMArcihtecture.png) ](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWtbxKM5vgfxIAYWbwnrRQ_0U76Dexpb1Utvy4lfUaC7FM87CcGRjTnB6vVf4aCWyxi1lCrRNmLhmzHeoFdJ6UQMOycLkiZ6PUK2Xlg18la_sireahVRfjwEtXKX6_XqwI7u7HJ1ueVmE/s1600/OTMArcihtecture.png)

  

A typical data flow between these servers can be understood as below:  
End User of the OTM application will start a browser like IE, Firefox on their local desktop(PC) which is referred to a "Client" machine. User will launch the OTM application(installed on server machine as explained above) using URL having host name and port number for the OTM Web tier. User will login and start performing actions in the OTM application.Each action will have an REQUEST("Client" to "Server") and RESPONSE("Server" to "Client"). There can be several users working simultaneously on the application. Google topics related to "Client Server Architecture" for more details.  
  
If you look at above diagram, user will send an HTTP request(in the form of actions) to OTM Web tier. If the request is for a static content (like some OTM help page topics,etc.) web tier will directly send this information back to the user. But, if the request requires some complex business logic processing (like bulk planning of orders into shipments), web tier will send the request to app tier that has all the software components like Bulk Plan alogoriths, etc and App tier will process the request(sometimes by fetching required data from Database tier) and send information back to web server. Web server will present this information to end user.  
  
OTM Web tier is just a information presentation layer. Web tier primarily takes care of User Interface functions. App tier takes care of all business logic/application logic functions.    
  
Also, you see that external applications(utilities) like SMC Rateware, PC Miler, SMTP server etc can be installed separately on a different server(Windows, etc) and OTM App tier can be configured to communicate with these applications. We will talk more about these external applications used by OTM and related configurations in future posts.  
  
**Note:** Please post corrections to 'learnotm@outlook.com'