---
title: Review anomaly detection logged results | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/results
ingestedAt: "2026-06-18T08:04:11.563Z"
---

By default, data quality monitoring scan results are stored in the `system.data_quality_monitoring.table_results` table. Only account admins can access this table, and they must grant access to others as needed. Data quality monitoring uses [default storage](https://docs.databricks.com/aws/en/storage/default-storage) to store the anomaly detection results. You are not billed for the storage.

important

The results table `system.data_quality_monitoring.table_results` contains all results across the entire metastore and includes sample values from tables in each catalog. You should share this table only with users who are authorized to view metastore-wide data quality monitoring results.

## Anomaly detection result table schema[​](#anomaly-detection-result-table-schema "Direct link to Anomaly detection result table schema")

Each row in the results table corresponds to a single table in the schema that was scanned.

The table has the following schema:

### `commit_freshness` array structure[​](#-commit_freshness-array-structure "Direct link to -commit_freshness-array-structure")

The `commit_freshness` struct contains the following:

### `total_row_count` and `daily_row_count` array structure[​](#-total_row_count-and-daily_row_count-array-structure "Direct link to -total_row_count-and-daily_row_count-array-structure")

The `total_row_count` and `daily_row_count` structs contain the following:

### `upstream_jobs` array structure[​](#-upstream_jobs-array-structure "Direct link to -upstream_jobs-array-structure")

The structure of the array shown in the `upstream_jobs` column is shown in the following table:

### Downstream impact information[​](#-downstream-impact-information "Direct link to -downstream-impact-information")

In the logged results table, the column `downstream_impact` is a `struct` with the following fields:
