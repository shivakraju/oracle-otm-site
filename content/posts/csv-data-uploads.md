---
title: "CSV Data Uploads"
date: 2026-03-04T21:48:00+00:00
draft: false
weight: 80
aliases:
  - "/2026/03/csv-data-uploads.html"
keywords:
  - "Oracle OTM CSV data upload"
  - "OTM CSV export import locations"
  - "Oracle OTM bulk data load CSV"
  - "OTM CSV upload order release shipment"
  - "Oracle OTM Data Export CSV Export"
  - "OTM mass data upload technique"
  - "Oracle Transportation Management CSV loading"
  - "OTM location CSV upload steps"
  - "Oracle OTM GLOGOWNER table CSV"
  - "OTM data migration CSV method"
description: "Step-by-step guide to loading data into Oracle OTM using CSV uploads, demonstrated with the Location object, covering the CSV Export screen, WHERE clause setup, and the resulting import file format."
---

OTM supports loading data using CSV (comma-separated values) files. This is a practical method for bulk data uploads during initial implementation or data migrations — especially when the source data is available in spreadsheet form.

The approach works by first exporting a sample record from OTM in CSV format, which gives you the exact column structure OTM expects. You then populate that template with your data and upload it back. The steps below use a Location record as an example — the same process applies to any OTM business object such as Order Release, Shipment, Service Provider, Invoice, and more.

**Step by Step — Load a Location via CSV:**

<div class="step-box">
<strong>Step 1 — Create a sample Location in OTM manually</strong>

Log in to OTM and create one sample Location record with all the fields you plan to load via CSV. This sample record will be used in the next step to generate the correct CSV template.

<p>Navigate to:</p>

Shipment Management > Location Manager > New

Fill in the required fields — Location GID, Name, Address — and save the record.
</div>

> ![OTM Location Manager showing a sample location record](/images/csv-otm-location-record.png)

<div class="step-box">
<strong>Step 2 — Find the backend table name and WHERE clause</strong>

OTM stores Location data in the `LOCATION` table. To export just your sample record, you need a WHERE clause that identifies it. The Location GID's Xid maps to `LOCATION_XID`:
</div>

```sql
SELECT * FROM location WHERE location_xid = 'YOUR-LOCATION-XID'
```

Note down the `LOCATION_XID` value — you will enter this as the WHERE clause in the next step.

<div class="step-box">
<strong>Step 3 — Export the sample record as CSV from OTM</strong>

Navigate to:

Business Process Automation > Data Export > CSV Export
</div>

> ![OTM CSV Export screen](/images/csv-data-uploads-img1-80b819bdb1.png)

<div class="step-box">
<strong>Step 4 — Select table and run the export</strong>

On the CSV Export screen, set **Table Name** to `LOCATION` and paste the WHERE clause from Step 2 into the WHERE clause field. Click **Run**.
</div>

> ![CSV Export — selecting LOCATION table with WHERE clause](/images/csv-export-table-select.png)

<div class="step-box">
<strong>Step 5 — Save the output as a CSV file</strong>

OTM displays the exported data as grey text. Select all of that text and save it as a `.txt` file. Then open the `.txt` file in Microsoft Excel — when prompted, choose **comma** as the delimiter. Save the result as a `.csv` file.

To verify the file is correctly formatted, open it in a text editor (Notepad or TextPad) — you should see values separated by commas, with the column headers in the first line and the NLS date format in line 2.
</div>

> ![OTM CSV export output showing comma-separated data](/images/CSVUploadResult.png)

<div class="step-box">
<strong>Step 6 — Populate the CSV template with your data</strong>

Add your actual records to the CSV file, following the same column structure as the exported sample row. Each row represents one Location (or whichever object you are loading). Do not change the column order or the header rows.
</div>

<div class="step-box">
<strong>Step 7 — Upload the CSV file to OTM</strong>

Navigate to:

Business Process Automation > Integration > Integration Manager > Upload XML/CSV Transmission

Browse for your `.csv` file and click **Upload**.
</div>

> ![OTM Integration Manager upload screen](/images/csv-data-uploads-img2-7f6b9b4bab.png)

<div class="step-box">
<strong>Step 8 — Verify the result</strong>

After the upload, OTM displays a results screen showing **Process Count** and **Error Count**. A non-zero Error Count means some records failed — click the error details to review.
</div>

> ![OTM CSV upload result showing Process Count and Error Count](/images/csv-upload-result2.png)

> ![OTM CSV upload confirmation screen](/images/csv-data-uploads-img3-f36c44c247.png)

<div class="note-box"><strong>Important:</strong> Date columns in your CSV file must follow the NLS Date Format specified in line 2 of the exported CSV. If the date format does not match, OTM will reject those rows with a format error.</div>

**What's Next:**

Now that you have seen the main methods for loading data into OTM — XML uploads, HTTP POST from PL/SQL, and CSV uploads — the next topic covers OTM Outbound Integrations: how OTM sends data out to external systems such as carrier platforms, ERP applications, and middleware.

Next Topic: [Outbound Integrations](/posts/otm-outbound-integrations/)
