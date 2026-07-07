---
title: "G-Log Properties"
date: 2017-08-13T21:22:00+00:00
draft: false
weight: 480
tags:
  - "G-log properties"
  - "config"
aliases:
  - "/2017/08/g-log-properties.html"
---

**Note:** This post is applicable for OTM ver 6.x and below.

  

G-Log Properties on the OTM App and Web server have the configurations that control the interactions between OTM App, Web and Database tiers. They also have configurable properties for the application like number of results to display on search screens, etc.  
  
Always take backup of current file, before changing these properties because this file is critical and used by the application during re-boot. Any corruption to this file would result in issues with application behavior.   
  
**To view the current properties from application:**  
  
Login to OTM application and in the URL use servlet "glog.webserver.properties.PropertiesServlet" as shown below:  
  
http://otm-server:7777/GC3/glog.webserver.properties.PropertiesServlet  
  
Click 'List' button and you will see the current properties.  
  
**To modify the properties file:**  
  
On the app and web server switch to base folder($OTM_HOME) where OTM is installed and you find the file in below folder:  
  
$cd $OTM_HOME/glog/config  
  
Take backup of current file and update changes. You need to apply changes on both app and web server and restart the application for new changes to take effect.  
  
Sample file with important properties marked in RED:  

```properties
#####################################################################  
# G-Log Properties File for Both Web and App Server  
# This property file holds the configurable settings for the  
# G-Log Web and App Servers (running on the same box). These  
# settings will override any settings in glog.webserver.properties,  
# glog.appserver.properties, glog.common.properties, and  
# glog.base.properties. These properties are initially set  
# by the install scripts, but can be modified to work with  
# your specific server. All G-Log property changes should be  
# made to this file, rather than the webserver, appserver,  
# common, or base property files.  
#####################################################################  
# !!!!!!!!!!!!!!!!!!!!!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!  
#-------------------------------------------------------------------  
# Place all thread settings changes in the Custom Thread Properties  
# section at the end of this file.  
#-------------------------------------------------------------------  
# Place all other changes, new properties, and custom properties in  
# the Custom Properties section near the end of this file.  
#-------------------------------------------------------------------  
# These sections will be used by future installers during upgrades.  
# Properties that are outside this section will not be migrated.  
#####################################################################  
#--------------------------------------------------------------------  
# Base Install Settings  
#--------------------------------------------------------------------  
# GC3 version  
glog.software.version=Otmv634  
glog.software.patch.version=OTMv6.3.4  
glog.software.installtype=WebAppServer  
glog.software.instancetype=OTM  
# installation paths  
gc3.dir=/home/oracle/otm  
gc3.config.dir=$gc3.dir$/glog/config  
temp.dir=$gc3.dir$/temp  
# application server URL and port  
appserver=OTM-SERVER  
appserver.port=7001  
# application server type  
glog.app.server.name=weblogic  
appserver.protocol=t3://  
# web server URL and port  
webserver=OTM-SERVER  
webserver.port=7777  
# web URL prefix - should be blank unless web server is behind a reverse-proxy server  
glog.webserver.urlprefix=  
  
# web server URL (may differ from server name)  
glog.webserver.URL=http://OTM-SERVER:7777$glog.webserver.urlprefix$  
## this should only be uncommented if running In-Memory Logistics Command Center  
#glog.includes.lc2=true  
# db server URL and information  
dbserver=127.0.0.1  
glog.database.sid=otmdb  
glog.database.connectstring=otmdb  
glog.database.port=1521  
glog.database.schema=glogowner  
# LCC Controller only  
#lc2.otm.database.server=lccdb.company.com  
#lc2.otm.database.port=1521  
#lc2.otm.database.service=lccdb  
#lc2.otm.database.schema=lc2dba  
#lc2.otm.database.password={e  
#lc2.otm.database.commonPassword={e  
# the following should only be used as directed by OTM Support:  
#otm.db.url=   
!includeIfSet $otm.db.url$,glog.rac.properties  
  
# db users and passwords  
otm.db.user=glogdba  
otm.db.password={eR0xPR0RCQQ==  
glog.database.load.user=glogload  
glog.database.load.password={eR0xPR0xPQUQ=  
# oracle driver type should be "Oracle" for thin drivers or "weblogic" for oci drivers  
glog.database.default.poolDriver=Oracle  
# default password storage setting (Encrypt/Text) - Note, changing this option also requires db changes  
glog.crypto.password.mode=Encrypt  
# App-to-Web authentication  
glog.signedServlet.password={eQ0hBTkdFTUU=  
#--------------------------------------------------------------------  
# Log Settings  
#--------------------------------------------------------------------  
# turn logging on or off  
glog.log.on=false  
# path to log file(s)  
glog.log.dir=$gc3.dir$/logs  
glog.log.file.defaultLog.filepath=$gc3.dir$/logs/glog.default.log  
# maximum size of log files (bytes)  
glog.log.maxsize=10000000  
# maximum number of log backup files  
glog.log.backups=10  
#--------------------------------------------------------------------  
# Web Server Settings  
#--------------------------------------------------------------------  
document.root=$gc3.dir$/web/htdocs  
# maximum number of results returned by port/airport finder, optional  
glog.webserver.portresults.count=100  
# maximum number of results returned by giv, optional  
glog.webserver.givresults.count=100   
# webservices  
appserver.port.webservice.weblogic=$appserver.port$  
# OHS settings  
ohs.config.dir=/home/oracle/Middleware/Oracle_WT1/instances/instance1/config/OHS/ohs1  
ohs.diagnostics.dir=/home/oracle/Middleware/Oracle_WT1/instances/instance1/diagnostics/logs/OHS/ohs1  
## Replicated Operational Database (ROD) - optional  
#ods_feature=true  
#glog.ods.dbserver=otmodsdb.company.com  
#glog.database.ods.sid=otmodsdb  
#glog.ods.connectstring=otmodsdb  
#glog.ods.database.port=1521  
#glog.database.ods.schema=glogowner  
## Fusion Transportation Intelligence (FTI) - optional  
#aa_webserver=http://otmfti.company.com:7001  
#ALLOW_ADVANCED_ANALYTICS=true  
#glog.fti.dbserver=otmftidb.company.com  
#glog.fti.database.port=1521  
#glog.fti.database.schema=hdowner  
#glog.database.fti.sid=otmrod01  
#glog.database.fti.user=hdowner  
#glog.database.fti.password={e  
#glog.fti.connectstring=jdbc:oracle:thin:@$glog.fti.dbserver$:$glog.fti.database.port$  
#glog.security.userSession.enabled=true  
  
## Oracle Data Integrator (ODI); for use with FTI - optional  
#glog.odi.agent.server=otmodiagent.company.com  
#glog.odi.agent.port=20910  
#glog.odi.password={e  
#glog.odi.work.repository.code=FTI_WORK  
## Oracle MapViewer server  
#glog.mapServer=mapviewer.company.com  
#glog.map.service_name=elocation_mercator  
#glog.map.basemap=elocation_mercator.world_map  
## Oracle Spatial server  
#OracleSpatial.host=spatial.company.com  
#OracleSpatial.port=7777  
#OracleSpatial.US_Canada.routeServlet=/routeserver/servlet/RouteServerServlet   
#OracleSpatial.WesternEurope.routeServlet=/routeserver_eu/servlet/RouteServerServlet   
#OracleSpatial.geocodeServlet=/geocoder/gcserver  
## URLStreamHandler Class for Outbound HTTPS - uncomment for AIX or WebSphere  
#glog.integration.https.urlStreamHandlerClass=com.ibm.net.ssl.www.protocol.https.Handler  
## LCC Analytics  
#lc2.obiee.analytics.server.protocol=http  
#lc2.obiee.analytics.server.host=lccanalytics.company.com  
#lc2.obiee.analytics.server.port=9704  
#lc2.odi.agent.server=lccodi.company.com  
#lc2.odi.agent.port=20910  
#lc2.odi.password={e  
#lc2.odi.work.repository.code=LC2_WORK  
## LCC Pool Server SSO  
#glog.security.sso=true  
#glog.security.sso.appUidLocation=3  
#--------------------------------------------------------------------  
# App Server Settings  
#--------------------------------------------------------------------  
# scalability settings  
glog.scalability.on=false  
glog.log.ID.JMS.on=false  
glog.log.ID.Scalability.on=false  
glog.scalability.thisTarget=gc3-OTM-SERVER  
glog.scalability.thisMachine=DEFAULT  
glog.scalability.thisMachineURL=$appserver.protocol$$appserver$:$appserver.port$  
glog.scalability.defaultServer=DEFAULT  
glog.scalability.defaultMachineURL=$appserver.protocol$$appserver$:$appserver.port$  
glog.scalability.defaultMachine=DEFAULT  
  
# list of avaliable app servers to poll for network topology - used only by web server. one per line.  
!remove glog.scalability.topologyMachineURL  
glog.scalability.topologyMachineURL=$appserver.protocol$$appserver$:$appserver.port$  
#glog.scalability.topologyMachineURL=<additional app server>  
# list of available web servers  
!remove glog.scalability.web.topologyMachineURL  
glog.scalability.web.topologyMachineURL=http://$webserver$:$webserver.port$  
#glog.scalability.web.topologyMachineURL=<additional web server>  
# mail settings  
glog.mail.smtp.host=mail.company.com  
glog.workflow.notify.defaultSmtphost=mail.company.com  
glog.mail.images=$glog.webserver.URL$/images/mail  
# settings for fixed property change log  
glog.properties.log.file=$glog.log.dir$/properties.log  
# mail settings for property change notifications (these properties are   
# reserved and cannot be changed via the Property Set Manager  
glog.properties.log.email.host=mail.company.com  
glog.properties.log.email.from=OtmAdvisor@company.com  
# workflow settings  
glog.workflow.notify.advisor.name=G-Log Advisor  
glog.workflow.notify.advisor.email=OtmAdvisor@company.com  
glog.workflow.notify.advisor.fax=555-555-1212  
## FaxMaker Settings - optional  
#glog.workflow.notify.faxmaker.email=fax@company.com  
## RightFax Settings - optional  
#glog.fax.defaultHandler.routingMode=to  
#glog.fax.defaultHandler.routingPicture=/name={lastName},{firstName}/fax={rawPhone}/  
#glog.fax.email=fax@company.com  
## external integration settings  
#glog.integration.URLtoSendBills=http://<server_name>/servlets/<ClassNameOfServletThatReceivesFinancialRelatedXML>  
#glog.integration.URLtoSendVouchers=http://<server_name>/servlets/<ClassNameOfServletThatReceivesFinancialRelatedXML>  
## external SMC Rateware - optional  
#glog.RatingEngine.Rateware.URL=rateware.company.com  
#glog.RatingEngine.Rateware.Port=23700  
## external SMC RateWare Version 1.2.325 (or later) or SMC Carrier Connect  
#glog.RatingEngine.Rateware.NewAPI=true  
## external SMC RatewareXL - optional  
#glog.RatingEngine.RatewareXL.Username=  
#glog.RatingEngine.RatewareXL.Password=  
#glog.RatingEngine.RatewareXL.License=  
## external PCMiler/PCMiler Streets - optional  
#pcmiler.host=pcmiler.company.com  
#pcmiler.port=8145  
## external PCMiler Rail - optional  
#pcmiler.rail.host=pcmiler-rail.company.com  
#pcmiler.rail.port=2001  
## external Rand McNally - optional  
#intelliroute.host=127.0.0.1  
#intelliroute.port=1998  
#intelliroute.user=otm  
#intelliroute.password=changeme  
#intelliroute.location=company  
## external MileMaker - optional  
#milemaker.host=milemaker.company.com  
#milemaker.port=1031  
## external Kewill FlagShip - optional  
#glog.RatingEngine.Kewill.URL=kewill.company.com  
#glog.RatingEngine.Kewill.Port=1200  
#glog.RatingEngine.Kewill.RefnumQual=KEWILL_CUST_NUM   
#--------------------------------------------------------------------  
# Transmission Error properties -- can help in debugging inbound  
# transmission errors  
#--------------------------------------------------------------------  
# This property specifies if the response is a StackTrace or TransmissionAck  
#glog.integration.servlet.TransmissionStageError.elementName = StackTrace  
# This property indicates if the full Transmission is sent back  
#glog.integration.servlet.TransmissionStageError.includeTransmissionText = false  
# This controls how the elements are formatted [comment|CDATA|normal]  
#glog.integration.schema.element.StackTrace = comment  
#glog.integration.schema.element.TransmissionText = comment  
  
# The following properties specify if an email should be sent and to whom  
#glog.integration.servlet.TransmissionStageError.sendErrorEmail = false  
#glog.integration.servlet.TransmissionStageError.errorEmailTo =  
#glog.integration.servlet.TransmissionStageError.errorEmailFrom =  
#glog.integration.servlet.TransmissionStageError.errorEmailSubject = Transmission XML Stage Error  
#glog.integration.servlet.TransmissionStageError.errorEmailSmtpHost =  
#--------------------------------------------------------------------  
# Custom Properties - Beginning  
#--------------------------------------------------------------------  
# Place all changes, new properties, and custom properties here.  
# This section will be used during GC3 Upgrades  
#  
# Note that Property Sets WEB_CUSTOM, APP_CUSTOM and APP_WORKFLOW_THREADING  
# can be used to specify custom properties via the OTM Property Set Manager  
# screen. Only changes to reserved properties must be entered here.  
#--------------------------------------------------------------------  
# This property should be uncommented and repeated for every e-mail   
# requiring notification of property changes.  
#glog.properties.log.email.recipients=recipient1@domain.com  
#glog.properties.log.email.recipients=recipient2@domain.com  
#--------------------------------------------------------------------  
# Custom Properties - End  
#--------------------------------------------------------------------  
#--------------------------------------------------------------------  
# Default EBS Properties  
#--------------------------------------------------------------------  
#!include ebs.properties  
#--------------------------------------------------------------------  
# Default E1 Intergration Properties  
#--------------------------------------------------------------------  
#glog.integration.enableCaseChange=true  
#glog.integration.printXmlDeclaration=true  
#glog.workflow.topic.OrderLatestEstDeliveryDateSync.suppresslifetime=false   
#--------------------------------------------------------------------  
# Default Web Server Properties  
#------------------------------------------------------------------  
# This directive allows for the use of Property Set WEB_CUSTOM to manage   
# custom properties for the web-tier. This property set is stored in the   
# OTM database and is accessible through the Property Set manager within OTM.   
# Comment this out to disable this data-driven property set  
!propertySet WEB_CUSTOM,sibling   
!include glog.webserver.properties  
#--------------------------------------------------------------------  
# Default App Server Properties  
#--------------------------------------------------------------------  
# This directive allows for the use of Property Set APP_CUSTOM to manage   
# custom properties for the application tier. This property set is stored in the   
# OTM database and is accessible through the Property Set manager within OTM.   
# Comment this out to disable this data-driven property set.  
!propertySet APP_CUSTOM,sibling  
!include glog.appserver.properties  
#--------------------------------------------------------------------  
# Turn off Workflow persistence  
#--------------------------------------------------------------------  
glog.workflow.persistent.reboot=false  
!remove glog.workflow.persistent.classes  
#--------------------------------------------------------------------  
# Thread model (should only be set to 'on' for WebSphere installs)  
#--------------------------------------------------------------------  
glog.util.commonj.threadModel.appServer=off  
#--------------------------------------------------------------------  
# compensate for WebSphere issues  
#--------------------------------------------------------------------  
#glog.vpd.cacheMode.profileTagging=pool  
#--------------------------------------------------------------------  
# Custom Thread Properties - Beginning  
#--------------------------------------------------------------------  
# Place all thread changes and properties here.  
# This section will be used during GC3 Upgrades  
#--------------------------------------------------------------------  
# This directive allows for the use of Property Set APP_WORKFLOW_THREADING to manage   
# workflow groups and their thread counts. This property set is stored in the   
# OTM database and is accessible through the Property Set manager within OTM.   
# Comment this out to disable this data-driven property set.  
!propertySet APP_WORKFLOW_THREADING,sibling  
#--------------------------------------------------------------------  
# Custom Thread Properties - End  
#--------------------------------------------------------------------
```