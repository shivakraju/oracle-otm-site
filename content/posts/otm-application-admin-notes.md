---
title: "Application ADMIN Notes"
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
keywords:
  - "Oracle OTM application admin notes"
  - "OTM installation path gc3.dir"
  - "Oracle OTM WebLogic server admin"
  - "OTM gc3env.sh configuration"
  - "Oracle OTM glogapp-wl glogweb-wl"
  - "OTM application restart WebLogic tomcat"
  - "Oracle OTM Oracle patches apply"
  - "OTM admin console log"
  - "Oracle Transportation Management admin maintenance"
  - "OTM server directory structure"
description: "Quick-reference notes for Oracle OTM application administrators covering installation paths, key directories, WebLogic management, patch application, and server restart procedures."
---

This post covers common tasks for OTM application administrators — finding the installation path, restarting the application, applying Oracle patches, and resetting admin passwords.

**OTM installation path:**

To find the OTM home directory, log in to the OTM application and access the PropertiesServlet:

<div class="step-box">http://otm-server:7777/GC3/glog.webserver.properties.PropertiesServlet</div>

Click **List** to display the current G-Log properties. Note the following property — this is the base OTM installation path:

<div class="field-box"><strong>gc3.dir:</strong> /home/oracle/otm</div>

This is referred to as `$OTM_HOME` throughout this post. The actual path differs per installation depending on where your system administrator placed the OTM software.

**Key directories:**

<div class="field-box"><strong>G-Log properties:</strong> $OTM_HOME/glog/config — default application properties including DB connection details and install paths.</div>

<div class="field-box"><strong>Script8 folder:</strong> $OTM_HOME/glog/oracle/script8 — standard Oracle-provided scripts for maintenance tasks such as changing ADMIN passwords and recompiling DB objects.</div>

<div class="field-box"><strong>Web install:</strong> $OTM_HOME/install/ohs — OTM web tier software.</div>

<div class="field-box"><strong>App install:</strong> $OTM_HOME/install/weblogic — OTM application tier software.</div>

<div class="field-box"><strong>App log files:</strong> $OTM_HOME/logs/weblogic</div>

<div class="field-box"><strong>Web log files:</strong> $OTM_HOME/logs/tomcat</div>

**Restart OTM application:**

First, initialize the OTM environment variables:

```bash
cd $OTM_HOME/install
./gc3env.sh
```

When stopping OTM, bring the web tier down first (to stop user traffic), then the app tier. When starting, reverse the order — app first, then web.

**Stop the web tier:**

```bash
cd $OTM_HOME/install/ohs
./glogweb-wl stop
```

**Stop the app tier:**

```bash
cd $OTM_HOME/install/weblogic
./glogapp-wl stop
```

**Start the app tier:**

```bash
cd $OTM_HOME/install/weblogic
./glogapp-wl start
```

**Confirm the app tier is up:**

```bash
cd $OTM_HOME/logs/weblogic
tail -f console.log.0
```

Wait for the following message in the log:

```
OTM Event: serverReady
```

[![OTM app tier console.log showing serverReady message](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguOV-0GWHdVRqSQ53FuYfCuB7Muxmu1LHIDhcZ0zCIs0nmt9x2rGZRVbLYX3ifRIQ494I18u0lZ7iswOWH7ROUxym0906REE-b9NN7ie3m5ELoF-SCfR_-aUFfPNQ2XkRlBH7Iy-rkSjI/s320/IMG3.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEguOV-0GWHdVRqSQ53FuYfCuB7Muxmu1LHIDhcZ0zCIs0nft9x2rGZRVbLYX3ifRIQ494I18u0lZ7iswOWH7ROUxym0906REE-b9NN7ie3m5ELoF-SCfR_-aUFfPNQ2XkRlBH7Iy-rkSjI/s1600/IMG3.JPG)

**Start the web tier:**

```bash
cd $OTM_HOME/install/ohs
./glogweb-wl start
```

**Confirm the web tier is up:**

```bash
cd $OTM_HOME/logs/tomcat
tail -f console.log.0
```

Look for a message like:

```
INFO: Server startup in xxxxxx ms
```

[![OTM web tier console.log showing server startup message](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrjEYTwGNCzGK0gQOoIjQDoniKWPuYfrViBhDQ-5KwcMNxaP5CiHko7uv6U57Vr58vMktcb_Ipwaq3zaOMx3RkuUS92Qgm3WLm5AOSlbRWzn6XwbLI7YqNWomHOhZRDoIJ8vuIWVAjEE/s320/IMG4.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEigrjEYTwGNCzGK0gQOoIjQDoniKWPuYfrViBhDQ-5KwcMNxaP5CiHko7uv6U57Vr58vMktcb_Ipwaq3zaOMx3RkuUS92Qgm3WLm5AOSlbRWzn6XwbLI7YqNWomHOhZRDoIJ8vuIWVAjEE/s1600/IMG4.JPG)

Once both tiers are up, users can log in to the application.

**Run Oracle SR scripts:**

Place the script (e.g. `otm_analyzer.sql`) in `$OTM_HOME/glog/oracle/script8`, then connect to the GLOGOWNER schema via SQL*Plus and run it:

```bash
sqlplus glogowner/glogowner@OTMDB
```

```sql
@otm_analyzer.sql
```

Output is typically generated in the same folder.

**Reset GLOGDBA password:**

OTM connects to the database using the GLOGDBA schema password. If you change this password, you must update the G-Log properties file with the new Base64-encoded value.

On the OTM app server, generate the Base64-encoded password:

```bash
java glog.util.appclass.Base64Encoding <new_password>
```

Copy the output text, prefix it with `{e`, and set it as the value of `otm.db.password` in the G-Log properties file:

<div class="field-box"><strong>otm.db.password:</strong> {e&lt;base64-encoded-value&gt;</div>

Restart both the app and web tiers after saving the file.

**Recompile OTM DB invalid objects:**

```bash
cd $OTM_HOME/glog/oracle/script8
sqlplus glogowner/glogowner@OTMDB
```

```sql
@recompile_invalid_objects.sql
```

Verify no invalid objects remain:

```sql
SELECT object_name, owner, object_type, status
FROM   all_objects
WHERE  owner  = 'GLOGOWNER'
AND    status = 'INVALID';
```

<div class="note-box"><strong>Note:</strong> Ask your system administrator for the &lt;OTM Home&gt; path. Get the glogowner schema password from your DBA.</div>

**Reset OTM application ADMIN passwords:**

OTM ships with default ADMIN accounts such as DBA.ADMIN that have full access to all OTM data and configuration. To reset their passwords:

```bash
cd $OTM_HOME/glog/oracle/script8
./update_password.sh
```

Change passwords for the following users (recommended default: CHANGEME, or a password of your choice):

- system
- guest
- DBA.ADMIN
- GUEST.ADMIN
- GLOG.ADMIN
- SERVPROV.ADMIN

**Apply Oracle patches:**

1. Download the patch from Oracle (`.jar` file extension) to your desktop.
2. Copy the file to `$OTM_HOME/temp` on both the app server and web server.
3. Bring down the OTM app and web tiers.
4. On each server, switch to `$OTM_HOME/temp` and run:

```bash
java -jar <filename.jar>
```

The installer will prompt for the OTM Home directory and, in some cases, DB connection details if the patch updates database entries.

5. If the patch install summary shows a message about running a DB script, also run:

```bash
cd $OTM_HOME/glog/oracle/script8
sqlplus /nolog @run_patch.sql
```

6. Start the OTM app tier, then the web tier, following the restart steps above.
7. After a successful patch install, an entry is written to:

```
$OTM_HOME/glog/config/glog.patches.properties
```
