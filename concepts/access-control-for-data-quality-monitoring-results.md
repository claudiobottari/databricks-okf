---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f87ce21c2964488d8c8d05d2061950a27c9d981847be8bf66e9317809de2d1c
  pageDirectory: concepts
  sources:
    - review-anomaly-detection-logged-results-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-control-for-data-quality-monitoring-results
    - ACFDQMR
  citations:
    - file: review-anomaly-detection-logged-results-databricks-on-aws.md
title: Access Control for Data Quality Monitoring Results
description: Only account admins can access the system.data_quality_monitoring.table_results table and must explicitly grant access to other users.
tags:
  - databricks
  - data-quality
  - security
timestamp: "2026-06-19T20:15:19.025Z"
---

## Access Control for Data Quality Monitoring Results

**Access Control for Data Quality Monitoring Results** refers to the permissions and visibility restrictions placed on the table that stores anomaly detection scan outcomes in [Unity Catalog](/concepts/unity-catalog.md)'s data quality monitoring system. Access is tightly controlled because the results table contains sample values from tables across the entire [Metastore](/concepts/metastore.md), making it a sensitive resource. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Default Access

By default, anomaly detection scan results are stored in the system table `system.data_quality_monitoring.table_results`. Only **account admins** have access to this table. Account admins must explicitly grant access to other users or groups as needed. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Granting Access

Users who are not account admins cannot view the results unless an admin grants them the appropriate permissions. When granting access, administrators should follow the principle of least privilege and only share the table with users who are authorized to view metastore-wide data quality monitoring results. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Security Considerations

Because `system.data_quality_monitoring.table_results` contains results across the entire [Metastore](/concepts/metastore.md) and includes **sample values** from tables in each catalog, it should be shared only with users who are authorized to view that information. Sharing this table broadly could expose sensitive data from multiple catalogs. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Storage and Billing

The anomaly detection results use Default Storage (Databricks)|default storage in the account. Users are not billed for this storage. ^[review-anomaly-detection-logged-results-databricks-on-aws.md]

### Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Anomaly Detection](/concepts/anomaly-detection.md)
- System Tables
- [Account Admin Role](/concepts/account-admin-unity-catalog.md)

### Sources

- review-anomaly-detection-logged-results-databricks-on-aws.md

# Citations

1. [review-anomaly-detection-logged-results-databricks-on-aws.md](/references/review-anomaly-detection-logged-results-databricks-on-aws-533e3349.md)
