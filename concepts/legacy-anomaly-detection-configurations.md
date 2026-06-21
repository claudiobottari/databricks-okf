---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 741c7d254e10a0307c9d34d10f017078a1ef7f2e18da69f9a4b0e28c9d3590ea
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.88
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - legacy-anomaly-detection-configurations
    - LADC
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Legacy Anomaly Detection Configurations
description: Earlier version features including a data quality dashboard at /Shared/Databricks Quality Monitoring/ and customizable job parameters for freshness/completeness evaluation thresholds.
tags:
  - data-quality
  - legacy
  - configuration
timestamp: "2026-06-19T22:06:22.151Z"
---

# Legacy Anomaly Detection Configurations

**Legacy Anomaly Detection Configurations** refers to the deprecated job-level settings that were available in earlier versions of Databricks anomaly detection for data quality monitoring. These configurations allowed users to customize the behavior of the anomaly detection job, including its schedule, logging table name, and evaluation parameters for freshness and completeness checks. The current version of anomaly detection does not include these features. ^[anomaly-detection-databricks-on-aws.md]

## Overview

Starting from July 21, 2025, configuration of the job parameters is not supported for new customers. Users who need to configure the job settings must contact Databricks. The legacy configurations have been replaced by the Data Quality Monitoring Results UI, which provides a more streamlined experience. ^[anomaly-detection-databricks-on-aws.md]

## Data Quality Dashboard (Legacy)

The first data quality monitor run created a dashboard to summarize results and trends derived from the logging table. The dashboard was automatically populated with insights for the scanned schema. A single dashboard was created per workspace at this path: `/Shared/Databricks Quality Monitoring/Data Quality Monitoring`. ^[anomaly-detection-databricks-on-aws.md]

### Quality Overview Tab

The **Quality Overview** tab showed a summary of the latest quality status of tables in the schema based on the most recent evaluation. To populate the dashboard, users had to enter the logging table for the schema they wanted to analyze. ^[anomaly-detection-databricks-on-aws.md]

The top section of the dashboard displayed an overview of the scan results. Below the summary was a table listing quality incidents by impact, with any identified root causes displayed in the `root_cause_analysis` column. Below the quality incident table was a table of identified static tables that had not been updated in a long time. ^[anomaly-detection-databricks-on-aws.md]

## Editing Job Parameters (Legacy)

To edit the parameters that controlled the anomaly detection job — such as how often the job ran or the name of the logged results table — users had to edit the job parameters on the **Tasks** tab of the job page. ^[anomaly-detection-databricks-on-aws.md]

### Schedule and Notifications

To customize the schedule for the job or set up notifications, users used the **Schedules & Triggers** settings on the jobs page. ^[anomaly-detection-databricks-on-aws.md]

### Name of Logging Table

To change the name of the logging table or save the table in a different schema, users edited the job task parameter `logging_table_name` and specified the desired name. To save the logging table in a different schema, users specified the full 3-level name. ^[anomaly-detection-databricks-on-aws.md]

## Customizing Freshness and Completeness Evaluations (Legacy)

All parameters in this section were optional. By default, anomaly detection determined thresholds based on an analysis of the table's history. These parameters were fields inside the task parameter `metric_configs`, which was formatted as a JSON string with the following default values: ^[anomaly-detection-databricks-on-aws.md]

```json
[
  {
    "disable_check": false,
    "tables_to_skip": null,
    "tables_to_scan": null,
    "table_threshold_overrides": null,
    "table_latency_threshold_overrides": null,
    "static_table_threshold_override": null,
    "event_timestamp_col_names": null,
    "metric_type": "FreshnessConfig"
  },
  {
    "disable_check": true,
    "tables_to_skip": null,
    "tables_to_scan": null,
    "table_threshold_overrides": null,
    "metric_type": "CompletenessConfig"
  }
]
```

The following parameters could be used for both `freshness` and `completeness` evaluations:

- `disable_check`
- `tables_to_skip`
- `tables_to_scan`
- `table_threshold_overrides`

The following parameters applied only to the `freshness` evaluation:

- `table_latency_threshold_overrides`
- `static_table_threshold_override`
- `event_timestamp_col_names`

The following parameter applied only to the `completeness` evaluation:

- (No additional parameters were listed beyond the shared ones)

^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The current version of data quality monitoring on Databricks
- Data Quality Monitoring Results UI — The replacement for the legacy dashboard
- [Freshness and Completeness](/concepts/freshness-and-completeness-quality-metrics.md) — The two quality dimensions monitored by anomaly detection
- [Unity Catalog](/concepts/unity-catalog.md) — Required for anomaly detection functionality

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
