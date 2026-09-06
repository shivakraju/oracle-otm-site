---
title: "Oracle DBA notes"
date: 2017-08-13T15:25:00+00:00
draft: false
weight: 20
tags:
  - "alter profile"
  - "Init.ora"
  - "ALTER USER"
  - "INVALID objects"
  - "EM Console"
  - "STARTUP"
  - "DBA_DDL_LOCKS"
  - "Oracle DB"
  - "lsnrctl"
  - "COMPILE_SCHEMA"
  - "SHUTDOWN IMMEDIATE"
  - "tnsnames.ora"
aliases:
  - "/2017/08/oracle-dba-notes.html"
keywords:
  - "Oracle OTM DBA notes database maintenance"
  - "OTM Oracle database startup shutdown"
  - "Oracle lsnrctl start listener OTM"
  - "OTM tnsnames.ora configuration"
  - "Oracle OTM invalid objects compile schema"
  - "OTM alter profile password"
  - "Oracle OTM DBA_DDL_LOCKS"
  - "OTM Oracle database 11g maintenance"
  - "Oracle OTM GLOGOWNER schema DBA"
  - "OTM database SHUTDOWN IMMEDIATE STARTUP"
description: "DBA quick-reference notes for Oracle OTM on-premise installations, covering database startup and shutdown, listener management, tnsnames.ora, invalid object recompilation, and common database maintenance tasks."
url: "/posts/oracle-dba-notes/"
---

<div class="note-box"><strong>Note:</strong> This post applies to OTM version 6.x and below.</div>

The following quick-reference notes cover common Oracle DBA tasks for maintaining an OTM on-premise database. These activities are typically performed by a DBA rather than an application administrator.

**Start the database after an OS reboot:**

Log in to the OS as a super user and start the Oracle Listener process. The Listener receives client connection requests and routes traffic to the database server.

```bash
lsnrctl start
```

Connect to the database as sysdba and issue the STARTUP command:

```bash
sqlplus / as sysdba
```

[![Oracle sqlplus startup screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKkSEb4MmGUYyd8CXo_CXDphurYNx9kcjoP6A4DlCUpB6-J_l_Y3B1ZdBO6E9YVw5VzuyTJkNRSoyyF0SClytmZFoRZwsIqsfKE1xWUa7ekS4Yr9PplTjp3DKQxjC_Qqx5e0TMoUWMlv4/s400/IMG1.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKkSEb4MmGUYyd8CXo_CXDphurYNx9kcjoP6A4DlCUpB6-J_l_Y3B1ZdBO6E9YVw5VzuyTJkNRSoyyF0SClytmZFoRZwsIqsfKE1xWUa7ekS4Yr9PplTjp3DKQxjC_Qqx5e0TMoUWMlv4/s1600/IMG1.JPG)

```sql
STARTUP;
```

[![Oracle database startup output screenshot](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEiyKRKzYCoCpJFnccsZBY8XjP3m2KjL-8BY7FyDlNkUmzZLLqFrWFC22bMY6049MzDqB2vhlmno6c-YEEy0gGHHmI1tJJ3Ydba2wQcGiFx8FTWQffUeKC2gUlP2qzh7h5BM3u7TggibQ/s320/IMG2.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEiyKRKzYCoCpJFnccsZBY8XjP3m2KjL-8BY7FyDlNkUmzZLLqFrWFC22bMY6049MzDqB2vhlmno6c-YEEy0gGHHmI1tJJ3Ydba2wQcGiFx8FTWQffUeKC2gUlP2qzh7h5BM3u7TggibQ/s1600/IMG2.JPG)

To stop the database:

```sql
SHUTDOWN IMMEDIATE;
```

**Reset password for a DB schema or user:**

```sql
ALTER USER GLOGOWNER IDENTIFIED BY GLOGOWNER;
```

**Unlock a DB account:**

```sql
ALTER USER GLOGDBA ACCOUNT UNLOCK;
```

**Recompile OTM DB invalid objects:**

Log in to the server where OTM is installed, switch to the script8 directory, and connect as glogowner:

```bash
cd $OTM_HOME/glog/oracle/script8
ls recom*
sqlplus glogowner/glogowner@OTMDB
```

```sql
@recompile_invalid_objects.sql
```

To verify all objects are fixed:

```sql
SELECT object_name, owner, object_type, status
FROM   all_objects
WHERE  owner  = 'GLOGOWNER'
AND    status = 'INVALID';
```

This should return no rows.

<div class="note-box"><strong>Note:</strong> Ask your system administrator for the &lt;OTM Home&gt; path â€” this is the base directory on the server where OTM is installed. Get the glogowner schema password from your DBA.</div>

**Init.ora file:**

Oracle DB configuration parameters are maintained in the `init.ora` file located at:

```
$ORACLE_HOME/dbs
```

For OTM, set `open_cursors` to greater than 3000 in this file. The default value of 300 is insufficient for OTM workloads.

**Kill locked DB sessions:**

The `DBA_DDL_LOCKS` table shows sessions holding DDL locks by schema name. Use it together with `V$SESSION` to identify SID and serial number:

```sql
SELECT vs.sid, vs.serial#
FROM   dba_ddl_locks ddl,
       v$session vs
WHERE  ddl.owner      = 'GLOGOWNER'
AND    vs.sid         = ddl.session_id;
```

To identify your own current session (e.g. from TOAD or SQL Developer) before killing anything:

```sql
SELECT sys_context('USERENV', 'SID') FROM dual;
```

To kill a session (as sysdba on the OS):

```sql
ALTER SYSTEM KILL SESSION 'sid,serial#';
```

**Compile all objects in a schema:**

```sql
EXEC DBMS_UTILITY.compile_schema(schema => 'GLOGOWNER');
```

**Get all active DB sessions and their SQL:**

```sql
SELECT s.username, s.sid, s.osuser, t.sql_id, sql_text
FROM   v$sqltext_with_newlines t,
       v$session s
WHERE  t.address    = s.sql_address
AND    t.hash_value = s.sql_hash_value
AND    s.status     = 'ACTIVE'
AND    s.username  <> 'SYSTEM'
ORDER BY s.sid, t.piece
/
```

**Access Oracle Enterprise Manager (EM) Console:**

Log in to the server as OS super user. Start or stop the DB Console:

```bash
cd $ORACLE_HOME/bin
./emctl start dbconsole
./emctl stop dbconsole
```

Find the hostname and EM port:

```bash
sqlplus / as sysdba
```

```sql
SELECT host_name FROM v$instance;
```

The EM port is in `$ORACLE_HOME/install/readme.txt`. Access the console at:

```
https://otm-server:1158/em
```

The first time you access it, the browser may throw a certificate exception â€” add the exception to continue.

**EM user account issues:**

Log in to EM using the SYSMAN user ID. Ensure SYSMAN and DBSNMP are not locked and have no password expiry:

```sql
SELECT username, account_status, lock_date, expiry_date, profile
FROM   dba_users
WHERE  username IN ('SYSMAN', 'DBSNMP');

ALTER USER SYSMAN  ACCOUNT UNLOCK;
ALTER USER DBSNMP  ACCOUNT UNLOCK;
ALTER PROFILE DEFAULT            LIMIT password_life_time UNLIMITED;
ALTER PROFILE MONITORING_PROFILE LIMIT password_life_time UNLIMITED;
```

To reset the SYSMAN password:

```bash
$emctl setpasswd dbconsole
```

Enter the SYSMAN password when prompted, then restart the console:

```bash
cd $ORACLE_HOME/bin
./emctl stop dbconsole
./emctl start dbconsole
```

**TNS Names file path:**

Log in to the server where the Oracle DB is installed:

```bash
cd $ORACLE_HOME/network/admin
vi tnsnames.ora
```

This file contains the DB connection details including hostname and port. To test connectivity by SID:

```bash
tnsping OTMDB
```

**Remove password expiry for default DB users:**

Connect as sysdba and check the current profile for a user:

```sql
SELECT p.profile AS "Profile",
       p.limit   AS "Limit"
FROM   dba_profiles p,
       dba_users u
WHERE  u.username          = 'SYSMAN'
AND    u.profile           = p.profile
AND    p.resource_name     = 'PASSWORD_LIFE_TIME';
```

If DEFAULT is the profile returned, remove the expiry:

```sql
ALTER PROFILE DEFAULT            LIMIT password_life_time UNLIMITED;
ALTER PROFILE MONITORING_PROFILE LIMIT password_life_time UNLIMITED;
```
