---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c07e9db8ce57b90dd59e8530ade3a9a0a8574a852cb7ed697a4314aff59d70d9
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - time-series-feature-table-point-in-time-lookup
    - TSFT(L
    - Time Series Feature Tables (Point-in-Time Lookups)
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Time Series Feature Table (Point-in-time Lookup)
description: Feature tables that include a timestamp column to ensure training datasets use only feature values known up to the time of each target observation, preventing lookahead bias.
tags:
  - machine-learning
  - time-series
  - feature-engineering
timestamp: "2026-06-19T09:51:32.702Z"
---

---

title: Time Series Feature Table (Point-in-time Lookup)
summary: A feature table that includes a timestamp column enabling point-in-time lookups during training and inference, ensuring each row reflects the latest known feature values as of a given time.
sources:
  - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T12:00:00.000Z"
updatedAt: "2026-06-19T12:00:00.000Z"
tags:
  - feature-store
  - time-series
  - point-in-time
  - feature-engineering
aliases:
  - time-series-feature-table-point-in-time-lookup
  - TSFTPITL
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Time Series Feature Table (Point-in-time Lookup)

A **time series feature table** is a [Feature Table](/concepts/feature-table.md) that includes one or more timestamp columns, enabling point-in-time lookups when joining features to training or inference data. This ensures that each row in the resulting training dataset or batch inference output represents the latest known feature values *as of* the timestamp of that row, preventing data leakage from future observations. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## When to Use Time Series Feature Tables

Time series feature tables are recommended whenever feature values change over time, such as with:

- Time series data (e.g., sensor readings, stock prices)
- Event-based data (e.g., user clicks, transaction logs)
- Time-aggregated data (e.g., daily, weekly, or monthly rolling statistics)

If features are static or do not depend on time, a standard feature table without timestamp keys is sufficient. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## How Point-in-time Lookups Work

When you create a time series feature table, you designate specific time-related columns as *time series columns* (in Feature Engineering in Unity Catalog) or *timestamp keys* (in the legacy Workspace Feature Store). These columns form part of the table’s primary key structure.

During training or batch inference, the system performs an **as-of timestamp join** using the `timestamp_lookup_key` you specify. Instead of matching rows exactly on the timestamp, it retrieves the most recent feature value for each entity up to the timestamp of the target row. This point-in-time logic ensures that the model never sees feature values that were not yet known at the time of the prediction. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

### What Happens Without Timestamp Keys

If you only designate a time series column as a primary key column without using the dedicated `timeseries_columns` (or `timestamp_keys`) argument, Feature Store applies **exact timestamp matching** instead of point-in-time logic. In that case, rows are joined only when the timestamps match exactly, which may lead to missing or incorrect feature‑time alignments. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Creating a Time Series Feature Table

The exact syntax depends on whether you use [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) or the [Workspace Feature Store (legacy)](/concepts/databricks-workspace-feature-store-legacy.md). In both cases:

- Specify the time series columns in the primary key definition.
- Use the appropriate argument:
  - `timeseries_columns` (Unity Catalog)
  - `timestamp_keys` (Workspace Feature Store)

These arguments enable Feature Store’s point-in-time join logic when you later call `create_training_set` or `score_batch`. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Usage in Training and Inference

Time series feature tables integrate seamlessly with the rest of the Feature Store workflow:

- **Training**: When you create a [training set](/concepts/training-set-feature-store.md) using `create_training_set`, point-in-time lookups are automatically applied if the feature tables are marked as time series.
- **Batch inference**: When you call `score_batch`, the same point‑in‑time logic ensures that the feature values used for scoring are consistent with the timestamp of each inference request.
- **Real‑time serving**: For [Online Feature Store](/concepts/online-feature-store.md) publishing, time series features are published together with the associated timestamp metadata. The model serving endpoint uses entity IDs to look up pre‑computed features from the online store.

## Benefits

- **Prevents data leakage**: Future feature values cannot be accidentally included in training or inference.
- **Accurate modeling**: Time‑dependent signals are aligned with the correct context.
- **Reusability**: The same feature table can serve both training and production inference with consistent time‑aware joins.

## Related Concepts

- [Feature Table](/concepts/feature-table.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [Training Set](/concepts/training-set-feature-store.md)
- [FeatureSpec](/concepts/featurespec.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- [As‑of Join](/concepts/as-of-join.md)

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
