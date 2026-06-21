---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 258a4a5650c32eaa398bd9c61355fdba9710ac90469576a40d641e4c4b5d27b7
  pageDirectory: concepts
  sources:
    - get-started-with-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-quality-monitoring
    - DQM
    - DATA_QUALITY_MONITORING
    - Data quality monitoring expenses
    - data quality monitor
    - Data Quality Validation
    - Data quality
  citations:
    - file: get-started-with-unity-catalog-databricks-on-aws.md
title: Data Quality Monitoring
description: Anomaly detection across all tables in a schema and data profiling at the table level, automatically monitoring freshness and completeness using historical data patterns.
tags:
  - data-governance
  - monitoring
  - data-quality
timestamp: "2026-06-19T19:01:37.498Z"
---

---

title: Data Quality Monitoring
summary: A Unity Catalog feature that provides anomaly detection across all tables in a schema and data profiling at the table level to track freshness, completeness, and statistical changes.
sources:
  - get-started-with-unity-catalog-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:45:38.144Z"
updatedAt: "2026-06-19T14:44:27.033Z"
tags:
  - data-governance
  - data-quality
  - monitoring
aliases:
  - data-quality-monitoring
  - DQM
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
---

## Data Quality Monitoring

**Data Quality Monitoring** is a feature of [Unity Catalog](/concepts/unity-catalog.md) that helps maintain data integrity by automatically detecting anomalies and profiling data distributions. It operates across all tables in a schema, reducing the need for manual quality checks. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Anomaly Detection

Anomaly detection automatically monitors the **freshness** and **completeness** of tables using historical data patterns. It surfaces potential data quality issues without requiring manual configuration. Freshness tracks how recently a table has been updated, while completeness checks whether the expected number of rows has been written in the last 24 hours. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Data Profiling

Data profiling captures statistical distributions of data over time. This enables you to track data integrity and set alerts for unexpected changes. Profiling operates at the table level and provides historical snapshots of metrics such as null fractions, value distributions, and percentiles. ^[get-started-with-unity-catalog-databricks-on-aws.md]

### Integration with Unity Catalog

Data quality monitoring is one of several governance tools within Unity Catalog. It complements [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md), [Data Classification](/concepts/data-classification.md), and [Data Lineage](/concepts/data-lineage.md) to provide a comprehensive governance framework. The monitoring system does not modify source tables or add overhead to jobs that populate them. ^[get-started-with-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Data Classification](/concepts/data-classification.md)
- [ABAC](/concepts/abac-attribute-based-access-control.md)
- [Unity AI Gateway](/concepts/unity-ai-gateway.md)
- [Data Lineage](/concepts/data-lineage.md)

## Sources

- get-started-with-unity-catalog-databricks-on-aws.md

# Citations

1. [get-started-with-unity-catalog-databricks-on-aws.md](/references/get-started-with-unity-catalog-databricks-on-aws-3c48b4d4.md)
