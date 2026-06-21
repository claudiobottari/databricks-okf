---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c33dee84823f9515419b8cc4287ea74e5e3869e39822e6094de315111c49e7d0
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materialized-feature-pipeline-scheduling
    - MFPS
  citations:
    - file: declarative-features-databricks-on-aws.md
title: Materialized Feature Pipeline Scheduling
description: Mechanisms for scheduling feature materialization jobs using CronSchedule (time-based, for aggregation features) and TableTrigger (event-driven, for column selection features), with support for both offline and online store configurations.
tags:
  - feature-engineering
  - pipeline
  - scheduling
  - databricks
timestamp: "2026-06-19T09:57:56.190Z"
---

# Materialized Feature Pipeline Scheduling

**Materialized Feature Pipeline Scheduling** controls the timing and frequency of materialization jobs for declarative features in the Feature Store. After features are defined and registered in Unity Catalog, they can be materialized to offline or online stores using triggers that define when and how often the materialization pipeline runs.

## Overview

Feature materialization is the process of computing and storing feature values for efficient reuse in model training and serving workflows. The scheduling mechanism determines when these computations occur, using either time-based or event-based triggers. ^[declarative-features-databricks-on-aws.md]

## Trigger Types

### Cron Schedule

The `CronSchedule` trigger uses a standard quartz cron expression to define recurring materialization runs. It supports both offline and online store configurations and includes a timezone setting. ^[declarative-features-databricks-on-aws.md]

```python
CronSchedule(
    quartz_cron_expression="0 0 * * * ?",  # Hourly
    timezone_id="UTC",
    pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
)
```

The `MaterializedFeaturePipelineScheduleState` enum controls whether the schedule is active or paused. ^[declarative-features-databricks-on-aws.md]

### Table Trigger

The `TableTrigger` is an event-based trigger used with [ColumnSelection](/concepts/automl-column-selection.md) features. It only supports online store configurations and triggers materialization when the underlying source table is updated. ^[declarative-features-databricks-on-aws.md]

```python
TableTrigger()
```

## Configuration Types

### Offline Store Config

The `[OfflineStoreConfig](/concepts/offlinestoreconfig.md)` specifies where materialized features are stored for batch training and inference. It requires a catalog name, schema name, and table name prefix. ^[declarative-features-databricks-on-aws.md]

### Online Store Config

The `[OnlineStoreConfig](/concepts/onlinestoreconfig.md)` specifies the destination for features used in real-time serving. It includes an online store name to identify the serving store. ^[declarative-features-databricks-on-aws.md]

## Best Practices

- **Materialize features from the same data source in a single `materialize_features` call** to minimize data scans. ^[declarative-features-databricks-on-aws.md]
- **Use the same granularity** (for example, all 1-hour or all 1-day slide durations) for features on the same data source to enable better grouping during materialization. ^[declarative-features-databricks-on-aws.md]
- **Aggregation features use CronSchedule** and support both offline and online configurations. ^[declarative-features-databricks-on-aws.md]
- **ColumnSelection features use TableTrigger** and only support online store configuration. ^[declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Features](/concepts/declarative-feature-engineering-api.md) – The API for defining and computing features from data sources.
- [Feature Materialization](/concepts/feature-materialization.md) – The process of computing and storing features for reuse.
- [Online Store](/concepts/online-feature-store.md) – Storage for real-time feature serving.
- [Offline Store](/concepts/offline-feature-store.md) – Storage for batch training and inference datasets.
- Aggregation Functions – Time-windowed computations like Sum, Avg, and Count.
- [Column Selection](/concepts/automl-column-selection.md) – Simple feature selection without aggregation.

## Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
