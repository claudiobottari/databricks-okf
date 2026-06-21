---
title: View data quality monitoring expenses | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/expense
ingestedAt: "2026-06-18T08:04:18.983Z"
---

To check data quality monitoring expenses, query the system table `system.billing.usage`. For more information on querying billing records, see [Billable usage system table reference](https://docs.databricks.com/aws/en/admin/system-tables/billing).

## Anomaly detection expenses[​](#anomaly-detection-expenses "Direct link to Anomaly detection expenses")

To view only anomaly detection expenses, use the filter `usage_metadata.schema_id is NOT NULL`. The `billing_origin_product` is `DATA_QUALITY_MONITORING`.

Anomaly detection is enabled at the schema level, so checking for a non-null `schema_id` identifies costs related to anomaly detection.

SQL

    SELECT usage_date, sum(usage_quantity) as dbusFROM system.billing.usageWHERE  usage_date >= DATE_SUB(current_date(), 30) AND  billing_origin_product = "DATA_QUALITY_MONITORING" AND  usage_metadata.schema_id is NOT NULLGROUP BY usage_dateORDER BY usage_date DESC

To view only costs attributed to a specific schema:

SQL

    SELECT usage_date, sum(usage_quantity) as dbusFROM system.billing.usageWHERE  usage_date >= DATE_SUB(current_date(), 30) AND  billing_origin_product = "DATA_QUALITY_MONITORING" AND  usage_metadata.schema_id = "<schema_id>"GROUP BY usage_dateORDER BY usage_date DESC

## Data profiling expenses[​](#data-profiling-expenses "Direct link to Data profiling expenses")

To check expenses, use a query or the billing portal.

### View usage from the system table `system.billing.usage`[​](#view-usage-from-the-system-table-systembillingusage "Direct link to view-usage-from-the-system-table-systembillingusage")

To view only data profiling expenses, use the filter `usage_metadata.table_id is NOT NULL`. Data profiling is enabled at the table level, so checking for a non-null `table_id` identifies costs related to data profiling.

For results created starting in February 2026, the `billing_origin_product` is `DATA_QUALITY_MONITORING`.

SQL

    SELECT usage_date, sum(usage_quantity) as dbusFROM system.billing.usageWHERE  usage_date >= DATE_SUB(current_date(), 30) AND  billing_origin_product = "DATA_QUALITY_MONITORING" AND  usage_metadata.table_id is NOT NULLGROUP BY usage_dateORDER BY usage_date DESC

To view only costs attributed to a specific table:

SQL

    SELECT usage_date, sum(usage_quantity) as dbusFROM system.billing.usageWHERE  usage_date >= DATE_SUB(current_date(), 30) AND  billing_origin_product = "DATA_QUALITY_MONITORING" AND  usage_metadata.table_id = "<table_id>"GROUP BY usage_dateORDER BY usage_date DESC

To query results created before February 2026:

SQL

    SELECT usage_date, sum(usage_quantity) as dbusFROM system.billing.usageWHERE  usage_date >= DATE_SUB(current_date(), 30) AND  sku_name like "%JOBS_SERVERLESS%" AND  custom_tags["LakehouseMonitoring"] = "true"GROUP BY usage_dateORDER BY usage_date DESC

### View usage from the billing portal[​](#view-usage-from-the-billing-portal "Direct link to View usage from the billing portal")

You can also check data profiling expenses using the billing portal.

1.  Log in to the [Databricks account console](https://accounts.cloud.databricks.com/login).
2.  In the sidebar, click the **Usage** icon.
3.  On the Usage page, select **By tags**.
4.  In the first drop-down menu, select **LakehouseMonitoring** as the tag key.
5.  In the second drop-down menu, select **true** as the tag value. After you do this, **true** appears in the UI as shown in the diagram, and the second drop-down menu shows `LakehouseMonitoring(1)` to indicate that one tag key is selected.

![track monitoring expenses AWS](https://docs.databricks.com/aws/en/assets/images/track-expenses-aws-0274a6600e7c9b3d564575197d8709aa.png)
