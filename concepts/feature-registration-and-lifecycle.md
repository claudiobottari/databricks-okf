---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b43f5215c42653d251fdce151819d2bf881cb85b705547c2c2b6243e5e0cca41
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-registration-and-lifecycle
    - Lifecycle and Feature Registration
    - FRAL
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: Feature Registration and Lifecycle
description: "Two workflows for persisting features to Unity Catalog: a two-step approach (construct Feature locally, then register_feature) and a single-step approach (create_feature that validates and registers immediately)."
tags:
  - unity-catalog
  - feature-registration
  - lifecycle
timestamp: "2026-06-19T14:57:08.007Z"
---

```markdown
## Feature Registration and Lifecycle

**Feature Registration and Lifecycle** refers to the set of operations and states that a declarative feature passes through, from local experimentation to persistent registration in [[Unity Catalog]], optional materialization, and eventual deletion. The declarative Feature Engineering API provides two registration workflows and explicit lifecycle management methods. ^[declarative-features-api-reference-databricks-on-aws.md]

### Registration Methods

Features can be registered in Unity Catalog using one of two approaches:

- **Two‑step workflow** – Construct a `Feature` object locally, experiment with it (including creating a training set), then persist it by calling `register_feature()`. This lets you iterate before committing the feature to the catalog. ^[declarative-features-api-reference-databricks-on-aws.md]
- **Single‑step workflow** – Call `create_feature()` to validate, construct, and register the feature in one operation. Use this when you don’t need local experimentation. ^[declarative-features-api-reference-databricks-on-aws.md]

Both methods accept the same parameter set: a `DataSource` (either `DeltaTableSource` or `RequestSource`), a function (`AggregationFunction` or `ColumnSelection`), entity columns (required for aggregations), a timeseries column (required for aggregations), an optional name, and an optional description. ^[declarative-features-api-reference-databricks-on-aws.md]

### Lifecycle Phases

#### Experimentation

Before registration, a locally constructed `Feature` can be used with `create_training_set()` to produce point‑in‑time correct training data and validate the feature definition. The source data can be previewed via `source.to_dataframe()` to refine filter conditions or transformations. ^[declarative-features-api-reference-databricks-on-aws.md]

#### Registration

Once a feature is registered, it becomes a first‑class object in Unity Catalog. The registered feature stores its definition, including the source, function, entity keys, and time window configuration. Registered features are then available for use in training sets and model lineage. ^[declarative-features-api-reference-databricks-on-aws.md]

#### Materialization

Materialization is an optional step that pre‑computes feature values into a Delta table for low‑latency serving. The materialization pipeline runs on a trigger that depends on the feature type:

- **`CronSchedule`** – Used for aggregation features. Runs on a fixed Quartz cron schedule. ^[declarative-features-api-reference-databricks-on-aws.md]
- **`TableTrigger`** – Used for `ColumnSelection` features backed by a `DeltaTableSource`. Runs automatically when the upstream Delta table receives a new commit. ^[declarative-features-api-reference-databricks-on-aws.md]

Aggregation and `ColumnSelection` features cannot be materialized in the same call because they require different trigger types. ^[declarative-features-api-reference-databricks-on-aws.md]

#### Deletion

To delete a feature, call `delete_feature()` with its fully qualified name (`<catalog>.<schema>.<feature_name>`). Before deleting, you must:
- Remove or update any models or feature specs that reference the feature.
- If the feature has been materialized, delete the materialized feature first. ^[declarative-features-api-reference-databricks-on-aws.md]

### Auto‑Generated Names

When `name` is omitted during construction, the system generates a name following the pattern `{column}_{function}_{window}`. For example, `price_avg_rolling_1h` or `transaction_count_rolling_30d_1d`. ^[declarative-features-api-reference-databricks-on-aws.md]

### Time Windows and Triggers

Time windows control the lookback period for aggregation features. Three window types are supported:

- **Rolling window** – Real‑time, continuously updated window ending at the evaluation time (optionally with a delay to account for ingestion latency). ^[declarative-features-api-reference-databricks-on-aws.md]
- **Tumbling window** – Fixed, non‑overlapping windows that partition time completely. ^[declarative-features-api-reference-databricks-on-aws.md]
- **Sliding window** – Overlapping windows that advance by a configurable slide interval. ^[declarative-features-api-reference-databricks-on-aws.md]

The choice of window type influences both training‑time point‑in‑time computation and materialization schedule.

### Sources

- declarative-features-api-reference-databricks-on-aws.md

### Related Concepts

- [[Unity Catalog]] – The [[metastore|Metastore]] where features are registered and governed.
- [[Feature Store]] – The overall system for managing and serving features.
- [[Training Set (Feature Store)|TrainingSet]] – A dataset created with point‑in‑time correct feature computation.
- [[Point-in-time correctness|Point‑in‑Time Correctness]] – Ensuring feature values reflect the state at the label timestamp.
- Online‑Offline Skew – A common pitfall that correct feature lifecycle management helps avoid.
- materialize_features() API|Materialized Features – Pre‑computed feature tables for low‑latency serving.
- [[DeltaTableSource]] – The data source definition for time‑series or batch features.
- [[RequestSource]] – The data source definition for features provided at inference time.
- [[AutoML Column Selection|ColumnSelection]] – Pass‑through feature type without aggregation.
- [[AggregationFunction and ColumnSelection|AggregationFunction]] – Feature type that applies a function over a time window.
```

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
