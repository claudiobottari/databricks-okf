---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bfb0b79bfc2573bd35ce01529b1872208c68714df2f6f3cec47eb170bd344b77
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - health-indicators-catalog-explorer
    - HI(E
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Health Indicators (Catalog Explorer)
description: Visual status badges displayed on schema and table overview pages that summarize table health (healthy/unhealthy/error) for data consumers without requiring navigation to the monitoring UI.
tags:
  - data-quality
  - ui
  - catalog
timestamp: "2026-06-19T22:06:11.164Z"
---

```yaml
---
title: Health Indicators (Catalog Explorer)
summary: Visual status badges (Healthy/Unhealthy/Error) shown per table in Databricks Catalog Explorer after anomaly detection is enabled on a schema, providing at-a-glance data quality summaries.
sources:
  - anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:45:40.687Z"
updatedAt: "2026-06-18T10:45:40.687Z"
tags:
  - ui
  - data-quality
  - catalog-explorer
aliases:
  - health-indicators-catalog-explorer
  - HI(E
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Health Indicators (Catalog Explorer)

**Health indicators** are visual summaries of table health displayed in Catalog Explorer after [[anomaly detection]] is enabled on a schema. They provide a quick, at-a-glance assessment of data quality for data consumers and business users without requiring them to navigate to the full [[Data Quality Monitoring UI|data quality monitoring results UI]].^[anomaly-detection-databricks-on-aws.md]

## How they appear

Once you enable anomaly detection on a schema in Unity Catalog, health indicator icons appear next to each table in the schema overview and table detail pages within Catalog Explorer. A table’s health is determined by its **freshness** (how recently it was updated) and **completeness** (whether the expected number of rows was written in the last 24 hours).^[anomaly-detection-databricks-on-aws.md]

Smart scanning automatically schedules scans for each table; the initial health indicator may be delayed by up to two weeks for tables that are skipped during the first scan. The indicator appears on the next scheduled rescan.^[anomaly-detection-databricks-on-aws.md]

## Permissions required

To view health indicator statuses, a user must have either `SELECT` or `BROWSE` privilege on the table.^[anomaly-detection-databricks-on-aws.md]

## Health statuses

The following health statuses are defined:

| Status | Description |
|--------|-------------|
| **Healthy** | The table’s freshness and completeness are within expected ranges. |
| **Unhealthy** (Stale) | A commit is unusually late based on the historical pattern of updates to the table. |
| **Unhealthy** (Incomplete) | The number of rows committed in the last 24 hours is below the lower bound of the predicted range. Additionally, a table can be marked incomplete if a column’s null percentage exceeds its predicted upper bound. |
| **Error** | The anomaly detection scan encountered a system error or the table is unsupported (e.g., views or foreign tables are not supported). |

For the authoritative and complete list, refer to the [[anomaly detection]] documentation.^[anomaly-detection-databricks-on-aws.md]

## Interaction with data quality monitoring

Health indicators are part of the broader [[anomaly detection]] feature. Incident details, historical trends, and root‑cause analysis are available from the **Quality** tab on a table page in Catalog Explorer, or from the **View results** link on the schema’s **Details** tab.^[anomaly-detection-databricks-on-aws.md]

## Related concepts

- [[Anomaly Detection]] — The underlying mechanism that analyzes freshness and completeness.
- [[Catalog Explorer]] — The workspace UI where health indicators are displayed.
- [[Unity Catalog]] — The governance layer that secures table access and manages metadata.
- [[Data Quality Monitoring UI|Data quality monitoring results UI]] — The detailed view for investigating incidents.
- [[Unity Catalog Permissions Model|Unity Catalog Permissions]] — `SELECT` and `BROWSE` required to view indicators.

## Sources

- anomaly-detection-databricks-on-aws.md
```

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
