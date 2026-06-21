---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8189ec0110e9f0db18de2f970be52c6561f244ad9616accc26d5edc29b59eb0f
  pageDirectory: concepts
  sources:
    - declarative-features-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - materializedfeaturepipelineschedule
    - MaterializedFeaturePipelineScheduleState
    - Materialization schedules
  citations:
    - file: declarative-features-databricks-on-aws.md
title: MaterializedFeaturePipelineSchedule
description: Configuration for scheduling feature materialization pipelines using CronSchedule (for aggregation features) or TableTrigger (for column selection features), with ACTIVE/PAUSED state management.
tags:
  - feature-engineering
  - scheduling
  - pipelines
timestamp: "2026-06-18T15:13:01.127Z"
---

Here is the wiki page for "MaterializedFeaturePipelineSchedule", based solely on the provided source material.

---

## MaterializedFeaturePipelineSchedule

**MaterializedFeaturePipelineSchedule** is a configuration entity used by the Databricks [Feature Engineering Client](/concepts/featureengineeringclient-api.md) to control the state of a scheduled feature materialization pipeline. It is set as part of the `trigger` parameter when calling `materialize_features`, and determines whether the materialization schedule is active or paused. ^[declarative-features-databricks-on-aws.md]

### Overview

When materializing features to an offline or online store, you can specify a schedule trigger (CronSchedule or TableTrigger). For `CronSchedule`, you must provide a `pipeline_schedule_state` of type `MaterializedFeaturePipelineScheduleState`. This state tells the system whether to start the pipeline immediately or keep it in a non‑active state. ^[declarative-features-databricks-on-aws.md]

The entity is imported from `databricks.feature_engineering.entities`. ^[declarative-features-databricks-on-aws.md]

### Usage

In a `materialize_features` call, the `CronSchedule` trigger object accepts a `pipeline_schedule_state` parameter. The example in the source material creates a CronSchedule with the state set to `ACTIVE`: ^[declarative-features-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    CronSchedule,
    MaterializedFeaturePipelineScheduleState,
    ...
)

fe.materialize_features(
    features=[avg_feature, sum_feature],
    offline_config=...,
    online_config=...,
    trigger=CronSchedule(
        quartz_cron_expression="0 0 * * * ?",
        timezone_id="UTC",
        pipeline_schedule_state=MaterializedFeaturePipelineScheduleState.ACTIVE,
    ),
)
```

The source material only shows `ACTIVE` as a state value. Other possible states (e.g., `PAUSED`) are not documented in the provided excerpt. ^[declarative-features-databricks-on-aws.md]

### States

The `MaterializedFeaturePipelineScheduleState` enum defines the operational state of the materialization pipeline:

| State    | Description |
|----------|-------------|
| `ACTIVE` | The materialization pipeline runs according to the cron schedule. |

The source material does not enumerate all possible values; only `ACTIVE` appears in the example. ^[declarative-features-databricks-on-aws.md]

### Related Concepts

- CronSchedule – The trigger type that uses this state.
- TableTrigger – An alternative trigger that does not require a schedule state.
- materialize_features() API|materialize_features – The API that accepts the `CronSchedule` with a pipeline state.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) – The client used to manage feature materialization.
- [Feature Materialization](/concepts/feature-materialization.md) – The overall process of materializing features for offline/online stores.

### Sources

- declarative-features-databricks-on-aws.md

# Citations

1. [declarative-features-databricks-on-aws.md](/references/declarative-features-databricks-on-aws-681d2599.md)
