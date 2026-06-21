---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 64f854309a72cf86bee9b65c3e08f498bd4cf70bfca3b53283ce597269b8246f
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.92
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-quality-details-ui
    - TQDU
    - Table Quality Details
    - Table details view
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Table Quality Details UI
description: A detailed view per table showing trend graphs of predicted vs observed values for each quality check, along with identified upstream root causes for failures.
tags:
  - data-quality
  - ui
  - debugging
timestamp: "2026-06-19T22:06:15.780Z"
---

## Table Quality Details UI

The **Table Quality Details UI** is a view within [Data Quality Monitoring](/concepts/data-quality-monitoring.md) on Databricks that provides a deeper analysis of anomaly detection results for a specific table. It enables users to explore trends and understand why anomalies were detected for particular tables in a schema. ^[anomaly-detection-databricks-on-aws.md]

### Accessing the UI

The Table Quality Details view can be reached through any of the following paths: ^[anomaly-detection-databricks-on-aws.md]

- From the **Results UI** (the new experience), by clicking the review link in the incidents list.
- From the **Monitoring Dashboard** (the legacy Lakeview dashboard), by clicking the table name in the Quality Overview tab.
- From the **UC Table viewer**, by visiting the **Quality** tab on the table page.

All options lead to the same Table Quality Details view for the selected table. ^[anomaly-detection-databricks-on-aws.md]

### UI Features

Given a table, the UI shows summaries from each quality check for the table, with graphs of predicted and observed values at each evaluation timestamp. The graphs plot results from the last **1 week** of data. ^[anomaly-detection-databricks-on-aws.md]

If the table failed the quality checks, the UI also displays any upstream jobs that were identified as the root cause. This root‑cause analysis is presented in a dedicated table within the view. ^[anomaly-detection-databricks-on-aws.md]

### Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying mechanism that monitors table freshness and completeness.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The broader framework that includes the results UI and dashboards.
- [Unity Catalog](/concepts/unity-catalog.md) – The catalog system under which the monitored tables reside.
- [Root cause analysis](/concepts/inference-tables-for-root-cause-analysis.md) – Automatic identification of upstream jobs responsible for quality failures.

### Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
