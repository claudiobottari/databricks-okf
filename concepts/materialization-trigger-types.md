---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f8c9d3fbb781788230e9fd38f8dd74d063887828e4ceb464e276853c5758cbdf
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - materialization-trigger-types
    - MTT
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
    - file: declarative-features-databricks-on-aws.md
title: Materialization Trigger Types
description: CronSchedule for periodic materialization of aggregation features and TableTrigger for incremental materialization of column-selection features
tags:
  - feature-engineering
  - serving
  - scheduling
timestamp: "2026-06-19T18:18:18.848Z"
---

# Materialization Trigger Types

**Materialization Trigger Types** control when a declarative feature materialization pipeline runs to compute and store feature values in offline or online stores. In the Databricks [Declarative Feature Engineering](/concepts/declarative-feature-engineering-api.md) API, the `trigger` parameter of `materialize_features()` determines whether the pipeline executes on a fixed schedule or is triggered by changes to the source data. ^[materialize-declarative-features-databricks-on-aws.md, declarative-features-databricks-on-aws.md]

## CronSchedule

`CronSchedule` configures the pipeline to run at a fixed, recurring interval specified by a Quartz cron expression. It is **required** for features that use an `AggregationFunction` (time‑windowed aggregations). ^[materialize-declarative-features-databricks-on-aws.md]

The schedule includes:
- `quartz_cron_expression` – a standard Quartz cron string (example: `"0 0 * * * ?"` for hourly runs).
- `timezone_id` – the time zone in which the cron expression is evaluated.
- `pipeline_schedule_state` – can be set to `MaterializedFeaturePipelineScheduleState.ACTIVE` to start the pipeline immediately. ^[materialize-declarative-features-databricks-on-aws.md]

CronSchedule is the only trigger type accepted when materializing aggregation features. It ensures that time‑windowed features are recomputed on a regular cadence. ^[materialize-declarative-features-databricks-on-aws.md]

## TableTrigger

`TableTrigger` runs the materialization pipeline **whenever the upstream source Delta table receives a new commit**. It is **required** for `ColumnSelection` features that are backed by a `DeltaTableSource`. ^[materialize-declarative-features-databricks-on-aws.md]

Because `ColumnSelection` features simply pick the latest value of a column per entity key, they do not need aggregation windows or scheduled recomputation. The event‑driven model ensures that the online store reflects the most current data as soon as the source table is updated. ^[materialize-declarative-features-databricks-on-aws.md]

## Choosing a Trigger Type

The following table summarises which trigger is appropriate:

| Feature type                    | Required trigger   | Notes |
|---------------------------------|--------------------|-------|
| `AggregationFunction` (time‑windowed aggregations) | `CronSchedule` | Scheduled recomputation needed for sliding/tumbling windows. |
| `ColumnSelection` (latest value per entity)       | `TableTrigger`    | Event‑driven; runs on source table changes. |

You **cannot mix** `ColumnSelection` and aggregation features in a single `materialize_features()` call because they require different trigger types. Separate calls must be issued for each group. ^[materialize-declarative-features-databricks-on-aws.md]

`RequestSource` features cannot be materialized at all; they represent data provided at inference time and have no source table to trigger from. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- [Declarative Features](/concepts/declarative-feature-engineering-api.md) – Defining and managing features in Unity Catalog.
- [Feature Materialization](/concepts/feature-materialization.md) – The process of precomputing feature data.
- [OfflineStoreConfig](/concepts/offlinestoreconfig.md) / [OnlineStoreConfig](/concepts/onlinestoreconfig.md) – Destination configurations for materialized features.
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) – Feature functions that use time windows.
- [ColumnSelection](/concepts/automl-column-selection.md) – Feature functions that select the latest value per entity.
- MaterializedFeature – The result of a materialization call.
- CronSchedule – Schedule trigger definition.
- TableTrigger – Change‑data‑capture trigger definition.

## Sources

- declarative-features-databricks-on-aws.md
- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
2. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
