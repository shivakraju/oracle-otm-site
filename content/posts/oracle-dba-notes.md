---
title: "Oracle DBA notes"
date: 2017-08-13T15:25:00+00:00
draft: false
weight: 470
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
---

**Note:** This post is applicable for OTM ver 6.x and below.

  

To maintain Oracle OTM Database, below quick notes are useful. Note that usually DBA takes care of below activities.  
  
**Start the Database after OS reboot:**  
  
Login to OS as super user and start the Oracle Listener process. This process receives request from the client and manages traffic to the database server. You can do this with below command:  
  
$lsnrctl start;  
  
This will start the listener for Oracle DB.  
  
**To restart Oracle DB issue below command:**  
$sqlplus / as sysdba;  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKkSEb4MmGUYyd8CXo_CXDphurYNx9kcjoP6A4DlCUpB6-J_l_Y3B1ZdBO6E9YVw5VzuyTJkNRSoyyF0SClytmZFoRZwsIqsfKE1xWUa7ekS4Yr9PplTjp3DKQxjC_Qqx5e0TMoUWMlv4/s400/IMG1.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgKkSEb4MmGUYyd8CXo_CXDphurYNx9kcjoP6A4DlCUpB6-J_l_Y3B1ZdBO6E9YVw5VzuyTJkNRSoyyF0SClytmZFoRZwsIqsfKE1xWUa7ekS4Yr9PplTjp3DKQxjC_Qqx5e0TMoUWMlv4/s1600/IMG1.JPG)

  
  
  
  
  
  
  
Now start the DB with below command at SQL prompt.  
  
SQL > STARTUP;  
  

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEiyKRKzYCoCpJFnccsZBY8XjP3m2KjL-8BY7FyDlNkUmzZLLqFrWFC22bMY6049MzDqB2vhlmno6c-YEEy0gGHHmI1tJJ3Ydba2wQcGiFx8FTWQffUeKC2gUlP2qzh7h5BM3u7TggibQ/s320/IMG2.JPG)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgEiyKRKzYCoCpJFnccsZBY8XjP3m2KjL-8BY7FyDlNkUmzZLLqFrWFC22bMY6049MzDqB2vhlmno6c-YEEy0gGHHmI1tJJ3Ydba2wQcGiFx8FTWQffUeKC2gUlP2qzh7h5BM3u7TggibQ/s1600/IMG2.JPG)

  
  
  
  
  
  
  
  
  
  
**Note that to stop DB, command is:**  
SQL > SHUTDOWN IMMEDIATE;  
  
**Reset password for DB schema/user(example):**  
$sqlplus / as sysdba;  
SQL > ALTER USER GLOGOWNER IDENTIFIED BY GLOGOWNER;  
  
**Unlock DB account(example):**  
SQL > ALTER USER GLOGDBA ACCOUNT UNLOCK;  
  
**Recompile OTM DB invalid objects:**  
  
Login to server where OTM application is installed and switch to :  
< OTM Home >/glog/oracle/script8 directory  
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
**Note:** You can ask your system administrator path details for <OTM Home>. This is base folder on the server where your OTM application is installed. You can get glogowner schema password details from your DBA.  
  
Init.ora file  
  
Oracle DB configurations are maintained in this file.  
$ORACLE_HOME/dbs  
File is in the dbs folder under Oracle Home directory as show above.  
In this file you can set DB parameters like open_cursors etc.  
For OTM DB, set the open_cursors parameter in this file to >3000\. Default is 300.  
  
**Kill locked DB sessions:**  
  
Table DBA_DDL_LOCKS has locked sessions by schema name.  
Table v$session has session details with SID and serial number.  
  
SELECT VS.SID, VS.SERIAL#  
FROM DBA_DDL_LOCKS DDL,  
V$SESSION VS  
WHERE DDL.OWNER = 'GLOGOWNER'  
AND VS.SID = DDL.SESSION_ID;  
  
If above query is from TOAD/SQL Developer, ensure you don't cancel that session :)  
Your current Toad session/SQL Developer session can be identified with query:  
  
select sys_context('USERENV','SID') from dual;  
  
**Now to kill the session:**  
  
Login to server as OS super user and run below commands:  
$sqlplus / as sysdba;  
SQL > alter system kill session 'sid,serial#';  
  
**To compile all objects in a schema:**  
  
EXEC DBMS_UTILITY.compile_schema(schema => 'GLOGOWNER');  
  
**To get all Active DB sessions and their CPU time:**  
  
select S.USERNAME, s.sid, s.osuser, t.sql_id, sql_text from v$sqltext_with_newlines t,V$SESSION s where t.address =s.sql_address  
and t.hash_value = s.sql_hash_value  
and s.status = 'ACTIVE'  
and s.username <> 'SYSTEM'  
order by s.sid,t.piece  
/  
  
**To access Oracle Enterprise Manager(EM) console:**  
Login to server as OS super user and follow below steps:  
  
**Start DB Console as follows:**  
[oracle@OTM-SERVER bin]$ cd $ORACLE_HOME/bin  
[oracle@OTM-SERVER bin]$ ./emctl start dbconsole  
  
**Stop DB Console as follows:**  
[oracle@OTM-SERVER bin]$ ./emctl stop dbconsole  
  
To access the console you need the Host Name and Port Number.  
**You can identify Host Name as follows:**  
[oracle@OTM-SERVER bin]$ sqlplus / as sysdba;  
SQL> select host_name from v$instance;  
HOST_NAME  
\-------------  
OTM-SERVER  
  
To find the port for em console, you can go to $ORACLE_HOME/install/readme.txt  
**This file shows the port number(for example:** 1158).  
  
**In browser now use URL:**  
<https://otm-server:1158/em>  
Firt time browser may throw exception and add this exception to the list so that you can access the console.  
  
**User Name/Password issues while accessing this EM:**  
  
You need to login using SYSMAN user ID.  
Please note that SYSMAN and DBSNMP user account must not be locked and password expiry must be removed.  
  
**You can review information using:**  
  
select USERNAME,ACCOUNT_STATUS,LOCK_DATE,EXPIRY_DATE,PROFILE   
from dba_users where username in ('SYSMAN', 'DBSNMP');  
alter user SYSMAN account unlock;  
alter user DBSNMP account unlock;  
alter profile DEFAULT limit password_life_time unlimited;  
alter profile MONITORING_PROFILE limit password_life_time unlimited;  
  
**You may re-set SYSMAN password using:**  
$emctl setpasswd dbconsole;  
Enter sysman password when prompted.  
  
**Restart dbconsole using:**  
cd $ORACLE_HOME/bin  
./emctl stop dbconsole  
./emctl start dbconsole  
  
**TNS NAMES file path:**  
  
Login to server as OS super user where Oracle DB is installed and then follow below steps:  
  
[oracle@OTM-SERVER admin]$ cd $ORACLE_HOME/network/admin  
[oracle@OTM-SERVER admin]$ vi tnsnames.ora  
  
This will show the DB connection details like host name and port number.  
  
**If you know the SID, you can use command:**  
[oracle@OTM-SERVER bin]$ tnsping OTMDB;  
  
**Removing password expiry of default DB users:**  
  
**Connect to DBA as OS rootuser and run command:**  
  
$ sqlplus / as sysdba;  
  
If we want to remove password expiry time period for SYSMAN user, run below SQL:  
  
select  
p.profile as "Profile",  
p.limit as "Limit"  
from  
dba_profiles p,  
dba_users u  
where  
u.USERNAME='SYSMAN'  
and u.profile=p.profile  
and p.resource_name='PASSWORD_LIFE_TIME';  
  
Now run below statement if DEFAULT is the profile name from above query:  
  
SQL>alter profile DEFAULT limit password_life_time unlimited;  
SQL>alter profile MONITORING_PROFILE limit password_life_time unlimited;