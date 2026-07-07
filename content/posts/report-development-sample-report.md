---
title: "Report Development - Sample Report"
date: 2016-10-22T01:58:00+00:00
draft: false
weight: 310
tags:
  - "BI Publisher"
  - "Query Template"
  - "Format Template"
  - "Report"
aliases:
  - "/2016/10/report-development-sample-report_21.html"
---

**Note:** This post is applicable for OTM ver 6.x - Query and Format template based reports.

  

In OTM, you can develop a report with basic knowledge of SQL, PLSQL and Oracle BI Publisher. Reports Developer need to install Oracle BI Publisher Desktop version from Oracle Technology network.  
  
Once BI Publisher is installed, Word document menu appears as below with 'Add-Ins' option:  
  
![](/images/report-development-sample-repo-img1-2fe34ce33e.png)  
  
Below are the report development steps for typical BI Publisher report in OTM.  
  

  * PLSQL Package in REPORTOWNER schema to dynamically frame WHERE clause condition strings based on report input parameters
  * Query template with SQL query and XML elements for each output column for the SQL query
  * Format template to display the XML elements from Query template in the required display format
  * Report definition in OTM application with input parameters names, their data types and link report template, format template with report definition.

  
We can review above steps by talking a simple report example. In this example we want to query the salary details for a particular employee by their employee number.  
  
Let us first create required data.  
Login to GLOGOWNER schema of OTM database and create employee, salary table with sample records:  
  

create table glogowner.emp(emp_no number,  
emp_name varchar2(100)  
);

  
create table glogowner.sal(emp_no number,  
salary number,  
month varchar2(100)  
);   
  
begin 

insert into emp values(1,'Ram');  
insert into emp values(2,'Aby');  
insert into emp values(3,'Venkat');  
  
insert into sal values(1,1000,'JAN');  
insert into sal values(1,1100,'FEB');  
insert into sal values(2,1200,'JAN');  
insert into sal values(2,1300,'FEB');  
insert into sal values(3,1400,'JAN');  
insert into sal values(3,1500,'FEB');  
commit;  
end;  
/  
  
**Next step is to write and test your SQL query:**  
  
![](/images/report-development-sample-repo-img2-14fd49e674.png)  
Note that in above query passing employee number to query will be done from your report and let us take that as input parameter for the report.  
  
OTM application need to accept employee number as input parameter from the user and convert into WHERE clause condition, pass to your query during run time and display the results. To form the WHERE clause based on your input parameter value we will need to define a PLSQL package in REPORTOWNER schema as shown below:  
  
Login to REPORTOWNER schema for OTM Database and execute below:  
  
Report Package Body  
Report Package Specification  
Report Synonym  
  
CREATE OR REPLACE PACKAGE REPORTOWNER.REPORT_EMP_PKG  
IS  
p_emp_no VARCHAR2 (200);  
p_emp_no_param VARCHAR2 (200);  
p_gl_user VARCHAR2 (128);  
FUNCTION afterpform  
RETURN BOOLEAN;  
FUNCTION value_entered (lex_name IN VARCHAR2)  
RETURN BOOLEAN;  
END;  
/  
  
CREATE OR REPLACE PACKAGE BODY REPORTOWNER.REPORT_EMP_PKG  
IS  
FUNCTION afterpform  
RETURN BOOLEAN  
IS  
v_string VARCHAR2 (32750);  
v_boolean BOOLEAN;  
BEGIN  
reports_library.set_vpd (p_gl_user);  
  
IF value_entered (p_emp_no)  
THEN  
**p_emp_no_param:**= ' E.EMP_NO '|| '' ||REPORTS_LIBRARY.GET_FILTER_CONDITION(p_emp_no)||'';  
ELSE  
**p_emp_no_param:**= ' AND 1=1';  
END IF;   
  
RETURN (TRUE);  
END afterpform;  
  
FUNCTION value_entered (lex_name IN VARCHAR2)  
RETURN BOOLEAN  
IS  
BEGIN  
IF lex_name > ' ' AND lex_name <> '1=1' AND lex_name IS NOT NULL  
THEN  
RETURN (TRUE);  
ELSE  
RETURN (FALSE);  
END IF;  
END value_entered;  
  
END;  
/  
  
CREATE OR REPLACE PUBLIC SYNONYM REPORT_EMP_PKG FOR reportowner.REPORT_EMP_PKG;  
  
Note that in the package specification we used REPORTS_LIBRARY.GET_FILTER_CONDITION.   
This is standard API provided by OTM where you can pass the report parameter(P_EMP_NO) as input and it would output the WHERE clause condition parameter string depending on whether user has selected options like 'Equal to', 'Less Than' etc:  
  
![](/images/report-development-sample-repo-img3-d5e0baa2a6.png)   
  
In above package, you should note that p_emp_no_param will be your WHERE clause parameter string that you frame using your PLSQL code and you pass this value to SQL in the Query Template which we are going to define next.  
  
Once you have reports package defined, next step is to make this package available to your query template. Take below code and copy this to a file with extension .xml. This will be your Query Template xml file.  
  
<?xml version="1.0" encoding = 'UTF-8'?>  
<dataTemplate name="REPORT_QUERY_TEMPLATE" defaultPackage="REPORT_EMP_PKG" version="1.0">  
<properties>  
<property name="xml_tag_case" value="upper"/>  
<property name="debug_mode" value="on"/>  
</properties>  
<parameters>  
<parameter name="P_GL_USER" dataType="character" defaultValue="DBA.ADMIN"/>   
<parameter name="P_EMP_NO" dataType="character" defaultValue="1=1"/>  
</parameters>  
<dataQuery>  
<sqlStatement name="QUERY_HDR">  
<![CDATA[SELECT E.EMP_NO,  
E.EMP_NAME,  
S.SALARY,  
S.MONTH  
FROM GLOGOWNER.EMP E,  
GLOGOWNER.SAL S  
WHERE &P_EMP_NO_PARAM  
AND E.EMP_NO=S.EMP_NO  
]]>  
</sqlStatement>   
</dataQuery>  
<dataTrigger name="afterParameterFormTrigger" source="REPORT_EMP_PKG.afterpform"/>  
<dataStructure>  
<element name="P_EMP_NO_PARAM" dataType="varchar2" value="REPORT_EMP_PKG.P_EMP_NO_PARAM"/>  
<group name ="HEADER" source="QUERY_HDR">  
<element name="EMP_NO" value="EMP_NO"/>  
<element name="EMP_NAME" value="EMP_NAME"/>  
<group name ="LINES" source="QUERY_HDR">  
<element name="SALARY" value="SALARY"/>  
<element name="MONTH" value="MONTH"/>  
</group>  
</group>  
</dataStructure>  
</dataTemplate>  
  
In this query template, below are important points you should note:  

  * Report package name mentioned in first line should match to your REPORTOWNER package defined in earlier step.
  * Parameters section should have P_EMP_NO, etc and these parameter names should match to input parameters used in REPORT package and also the Report definition(last step below)
  * SQL Statement section should have your query where you should use the P_EMP_NO_PARAM string in the WHERE clause. The value from this string comes from your report package logic during report run time. 
  * Data Structure section where you source the query columns as elements, give name to each element and also group them as Header, Line level data. Same elements will appear in the format template(BI Publisher template) where you can re-arrange the elements as per your report display requirements.

Once you have query template(.xml file), you can upload this to OTM as follows:  
Business Process Automation > Power Data > Document Generation > Query Template > New  
![](/images/report-development-sample-repo-img4-47f1765b02.png)  
Give a name to the query template and click upload button to browse for the .xml query template file defined in previous step.  
  
Once you have .xml file uploaded, click 'Generate Sample XML' button on the query template definition to generate a sample xml file.   
  
![](/images/report-development-sample-repo-img5-3c1549f418.png)  
  
You can enter, input parameter value to generate sample data. In this case, pull xml file with data for employee with number 2.  
  
Save the sample xml file. You can use this to load data into format template(.rtf file) as shown in next step.  
  
Once you have sample xml, you can create a new word document and may name it as "Report_Format_Template.rtf". Open this document and load .xml from previous step from Add-Ins menu:  
Data > Load XML Data   
![](/images/report-development-sample-repo-img6-1178c96521.png)  
  
**You will receive below message:**  
  
![](/images/report-development-sample-repo-img7-2b9893aaff.png)  
  
Once, sample data is loaded, you can arrange the columns in the format template either manually or using wizard. If you want to use wizard, you can follow steps:  
Add-Ins > Insert > Table Wizard:   
![](/images/report-development-sample-repo-img8-934a0a81ec.png)  
**In the wizard you can select:**  
**Report Format:** Table  
**Data set:** select one of the groups - Headers/Lines that you defined in the Query Template Data Structure:  
![](/images/report-development-sample-repo-img9-e976a73e8f.png)  
In this example, we will select Headers(Emp Name and Number) first and then repeat same steps to display line level elements (Month and Salary details).  
![](/images/report-development-sample-repo-img10-329c314c82.png)  
You can select Group By and Sort By elements(optional) in next screens of the wizard and click 'Finish'.  
If you repeat the steps for line level elements, you will see below format:  
![](/images/report-development-sample-repo-img11-00c5345ec6.png)  
  
If you double click on any element like EMP_NO you will see details as below:  
![](/images/report-development-sample-repo-img12-102b8ff715.png)  
Each group, starts with 'F' and denotes begin loop logic:  
![](/images/report-development-sample-repo-img13-2c71f747a2.png)  
'E' denotes loop end logic for that group of elements:  
![](/images/report-development-sample-repo-img14-1bbcf72893.png)  
You can use above specifications if you are manually arranging elements in the format template without using the wizard.  
  
Save the RTF file and upload this to OTM as shown below:  
  
Business Process Automation > Power Data > Document Generation > Format Template:  
![](/images/report-development-sample-repo-img15-ef0be887a1.png)  
Give a name to the template and upload the .rtf file.  
  
Last step is to define the report in OTM, to link the format template, query template and define the input parameters.  
Business Process Automation > Power Data > Document Generation > Reports > New  
![](/images/report-development-sample-repo-img16-f6c8265564.png)  
**In the report, you specify below:**  
  

  * Report ID, Report Display Name and Description
  * Specify Query and Format Template names defined in previous steps
  * Check 'Report Manager Display' option
  * Check 'Select via UI' option
  * Uncheck 'Use report parameters as Bind values'Create a new(n) report group and name it (example: Custom Reports)

  
![](/images/report-development-sample-repo-img17-6cf2402140.png)  
Define parameter name 'P_EMP_NO'(should match to name used in query template and report package)  
Select parameter data type - number, character, etc. We can also standard objects types like Buy Shipment, etc as input parameters:  
![](/images/report-development-sample-repo-img18-236a8672c1.png)  
If we need to define input parameter as 'mandatory' we can check the option(shown above)  
Click 'Finished' button to save the report.  
  
**We can run the report as shown below:**  
Business Process Automation > Reporting > Report Manager > Run   
![](/images/report-development-sample-repo-img19-baee5baaf9.png)  
  
**Enter input parameters:**  
  
![](/images/report-development-sample-repo-img20-c14defb526.png)  
  
Click submit to see the report output. Report engine will invoke report package, report package will form the WHERE clause parameter as per your package logic, these parameters with values are passed to your SQL query defined in query template, Query is executed and output is associated to XML elements defined in the data structure of Query template, this XML data is passed to format template and displayed as report output as per the format template definition.  
  
  
![](/images/report-development-sample-repo-img21-689808d84c.png)  
  
Once you have report defined, you can automate it to go to certain email ID based on events or configure a report workspace with set of reports and attach this workspace to a user role and so on. We will discuss these configuration in future topics.