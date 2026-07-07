---
title: "OTM Application ADMIN Notes"
date: 2017-08-13T19:33:00+00:00
draft: false
weight: 460
tags:
  - "console.log"
  - "Oracle Patches"
  - "install"
  - "tomcat"
  - "gc3env.sh"
  - "glogweb-wl"
  - "weblogic"
  - "ohs"
  - "glogapp-wl"
aliases:
  - "/2017/08/otm-application-admin-notes.html"
---

Below are useful notes for OTM ADMIN to maintain the application.

  
**OTM Installation paths:**  
  
To get the home path on the server where OTM (web or app tier) is installed, you can login to OTM application and in the URL use servlet "glog.webserver.properties.PropertiesServlet" as shown below:  
  
http://otm-server:7777/GC3/glog.webserver.properties.PropertiesServlet  
  
Click 'List' button and you will see default application properties also knows as glog properties. Note below property for path where OTM is installed:  
  
gc3.dir=/home/oracle/otm  
  
Let's refer to this as $OTM_HOME directory going forward. Note this path will be different for each installation depending on where your system administrator installed OTM application.  
  
**Below are important directories:**  
  
**Glog properties:** $OTM_HOME/glog/config  
This will show all default application properties like DB connection details, install paths, etc  
  
**OTM Script8 folder:** $OTM_HOME/glog/oracle/script8  
This folder will have standard scripts provided by Oracle to maintain the application like changing ADMIN user passwords, re-compile DB objects, etc  
  
**OTM Web Install:** $OTM_HOME/install/ohs  
This is folder where web tier of OTM software is installed.  
  
**OTM App Install:** $OTM_HOME/install/weblogic  
This is folder where app tier of OTM software is installed.  
  
**OTM APP Log files:** $OTM_HOME/logs/weblogic  
**OTM Web Log files:** $OTM_HOME/logs/tomcat  
  
**To Restart OTM Application:**  
  
**Set the OTM environment variables as follows:**  
  
Login to server where OTM app tier is installed and switch to below directory:  
$cd $OTM_HOME/install/  
ls gc3env.sh*  
./gc3env.sh  
  
This will set or initialize the OTM environment variables.  
  
To bring down the application - you should bring web tier first(to ensure there is no user activity) and then app tier. While bringing application up - you should bring app first and then web.  
  
**To bring down Web:**  
cd $OTM_HOME/install/ohs  
$ls  
$./glogweb-wl stop  
  
**To bring down App:**  
cd $OTM_HOME/install/weblogic  
$ls  
$./glogapp-wl stop  
  
**To bring up App:**  
cd $OTM_HOME/install/weblogic  
$ls  
$./glogapp-wl start  
  
**To confirm if app is successfully up:**  
cd $OTM_HOME/logs/weblogic  
$ls -ltr  
$tail -f console.log.0  
This will show log messages as app is coming up. Wait until below message appears:  
"OTM Event: serverReady"  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguOV-0GWHdVRqSQ53FuYfCuB7Muxmu1LHIDhcZ0zCIs0nmt9x2rGZRVbLYX3ifRIQ494I18u0lZ7iswOWH7ROUxym0906REE-b9NN7ie3m5ELoF-SCfR_-aUFfPNQ2XkRlBH7Iy-rkSjI/s320/IMG3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguOV-0GWHdVRqSQ53FuYfCuB7Muxmu1LHIDhcZ0zCIs0nmt9x2rGZRVbLYX3ifRIQ494I18u0lZ7iswOWH7ROUxym0906REE-b9NN7ie3m5ELoF-SCfR_-aUFfPNQ2XkRlBH7Iy-rkSjI/s1600/IMG3.JPG)

  
  
  
  
  
  
  
  
  
**To bring up Web:**  
$cd $OTM_HOME/install/ohs  
$ls  
$./glogweb-wl start  
  
**To confirm if web is successfully up:**  
cd $OTM_HOME/logs/tomcat  
$ls -ltr  
$tail -f console.log.0  
  
You should see message like "INFO: Server startup in xxxxxx ms"  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrjEYTwGNCzGK0gQOoIjQDoniKWPuYfrViBhDQ-5KwcMNxaP5CiHko7uv6U57Vr58vMktcb_Ipwaq3zaOMx3RkuUS92Qgm3WLm5AOSlbRWzn6XwbLI7YqNWomHOhZRDoIJ8vuIWVAjEE/s320/IMG4.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrjEYTwGNCzGK0gQOoIjQDoniKWPuYfrViBhDQ-5KwcMNxaP5CiHko7uv6U57Vr58vMktcb_Ipwaq3zaOMx3RkuUS92Qgm3WLm5AOSlbRWzn6XwbLI7YqNWomHOhZRDoIJ8vuIWVAjEE/s1600/IMG4.JPG)

  
  
  
  
  
  
  
  
Once App and Web are up, users will be login to the application.  
  
**Run OTM Scripts from Oracle SRs:**  
  
If you want to run any script provided by Oracle like otm_analyzer.sql, place this script first in $OTM_HOME/glog/oracle/script8.  
  
From SQL PLus login to GLOGOWNER schema.  
At prompt run, @otm_analyzer.sql  
  
This will run the script and output is usually generated in the same folder.  
  
**Reset GLOGDBA password:**  
  
OTM application will connect to OTM DB using GLOGDBA schema password.  
If you change this password, you need to follow below steps.  
  
Log into OTM App server and type below command to get Base64Econding equivalent for password.  
$java glog.util.appclass.Base64Encoding <text>  
  
Take the text that you get, prefix {e and add this to glog.property  
otm.db.password  
  
Restart app and web tier.  
  
**Note:** Glogproperties and Restarting App/Web related notes available in next posts.  
  
**Recompile OTM DB invalid objects:**  
  
Login to server where OTM application is installed and switch to :  
$< OTM Home >/glog/oracle/script8 directory  
$ls recom*  
You will see recompile scripts. Now connect to glogowner:  
$sqlplus [glogowner/glogowner@OTMDB](mailto:glogowner/glogowner@OTMDB);  
SQL> @recompile_invalid_objects.sql;  
  
**To review if all objects are fixed run:**  
SQL> select Object_name, Owner, object_type, status  
from all_objects  
where owner='GLOGOWNER'  
and status ='INVALID';  
  
This should not show any records.   
**Note:** You can ask your system administrator path details for <OTM Home>. This is base folder on the server where your OTM application is installed. You can get "glogowner" schema password details from your DBA.  
  
**Reset OTM application ADMIN passwords:**  
  
OTM application comes with some default ADMIN user accounts like DBA.ADMIN that have full access to all OTM data and application configurations. We can re-set passwords for these ADMIN accounts as below:  
  
cd $OTM_HOME/glog/oracle/script8 folder and run script ./update_password.sh.  
  
Change password for below users to default pwd CHANGEME(or some PWD of your choice):  
  
system  
guest  
DBA.ADMIN  
GUEST.ADMIN  
GLOG.ADMIN  
SERVPROV.ADMIN  
  
**Apply Oracle Patches:**  
  
1\. Download patch given by Oracle to your desktop.  
2\. This will have .jar file extension.  
3\. Copy this file to <OTM Home>/temp on both app server and web server.  
4\. Bring down OTM app and web.  
5\. Run following command after switching to <OTM Home>/temp on web and app.  
java -jar <filename.jar>;  
  
This will ask OTM Home directory and DB connection ID details(in some cases where patch need to update DB entries)  
  
\- After installing on the application server run the following(only for cases where it show this message in patch install summary)  
  
cd <otm_install_dir>/glog/oracle/script8  
sqlplus /nolog @run_patch.sql  
  
6.Start the OTM/GC3 web (Apache and Tomcat) and application (WebLogic/WebSphere/OC4J) servers as described in the Administration guide.  
7\. After patch is successfully applied note that an entry is made in the file:  
<OTM_HOME>/glog/config/glog.patches.properties