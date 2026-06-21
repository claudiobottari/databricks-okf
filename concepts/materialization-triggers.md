---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14f5070693543e4c853d1a5e3d6109465e82f203fefe1988e78ab8f81d759f9b
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materialization-triggers
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Materialization Triggers
description: CronSchedule (for aggregation features, scheduled via Quartz cron) and TableTrigger (for ColumnSelection features, triggered on upstream Delta table commits) control when materialization pipelines run.
tags:
  - feature-engineering
  - materialization
  - scheduling
timestamp: "2026-06-19T18:17:43.808Z"
---

# Materialization Triggers

**Materialization triggers** control when a materialization pipeline runs for [Declarative Feature Engineering|declarative features](/concepts/declarative-feature-engineering-apis.md). The appropriate trigger type depends on the feature type being materialized—aggregation features and column selection features require different trigger mechanisms and cannot be mixed in a single call. ^[declarative-features-api-reference-databricks-on-aws.md]

## CronSchedule

Use `CronSchedule` for aggregation features defined with `AggregationFunction`. The pipeline runs on a fixed schedule defined by a Quartz cron expression. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import CronSchedule
from databricks.sdk.service.ml import MaterializedFeaturePipelineScheduleState

trigger = CronSchedule(
    quartz_cron_expression="0 0 * * * ?",  # Hourly
    timezone_id="UTC",
    pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

The `pipeline_schedule_state` parameter can be set to `ACTIVE` to enable the schedule or `PAUSED` to suspend it without deleting the pipeline definition. ^[declarative-features-api-reference-databricks-on-aws.md]

## TableTrigger

Use `TableTrigger` for `ColumnSelection` features backed by a `DeltaTableSource`. The pipeline runs automatically whenever the upstream Delta table receives a new commit. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import TableTrigger

trigger = TableTrigger()
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Choosing a trigger

The trigger type is determined by the feature type being materialized. The two trigger types cannot be mixed in a single `materialize_features` call. ^[declarative-features-api-reference-databricks-on-aws.md]

| Feature Type | Required Trigger | Notes |
|-------------|-----------------|-------|
| Aggregation features (`AggregationFunction`) | `CronSchedule` | Runs on a fixed schedule (e.g., hourly, daily) |
| Column selection features (`ColumnSelection`) backed by `DeltaTableSource` | `TableTrigger` | Runs on source table commits only |
| `RequestSource` features | N/A | Cannot be materialized |

If you need to materialize both aggregation features and column selection features, you must issue separate `materialize_features` calls with the appropriate trigger for each group. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) — The framework that uses materialization triggers
- [Feature Materialization](/concepts/feature-materialization.md) — The process of precomputing feature values
- [DeltaTableSource](/concepts/deltatablesource.md) — The data source type used with TableTrigger
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — The function type used with CronSchedule triggers
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — The client used to issue `materialize_features` calls

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
