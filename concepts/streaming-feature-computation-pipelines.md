---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 23da0c65fa3b0b824e4b1e7c1b7aa3acdba3325acc02b60bedb43964f9f8a4d6
  pageDirectory: concepts
  sources:
    - feature-tables-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - streaming-feature-computation-pipelines
    - SFCP
  citations:
    - file: feature-tables-in-unity-catalog-databricks-on-aws.md
title: Streaming Feature Computation Pipelines
description: Feature tables can be updated incrementally using streaming DataFrames with `write_table` in merge mode, supporting real-time feature computation.
tags:
  - streaming
  - feature-store
  - pipelines
timestamp: "2026-06-19T18:48:56.980Z"
---

# Streaming Feature Computation Pipelines

**Streaming Feature Computation Pipelines** are a Databricks capability that enables continuous, real-time updates to [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) by processing streaming data sources. Instead of periodically recomputing features via batch jobs, these pipelines process incoming data incrementally, merging new feature values into the feature table as they arrive.

## Overview

A streaming feature computation pipeline consumes data from a streaming source — such as a Delta table updated by a Streaming Table or a Kafka topic — computes new feature values on the fly, and writes those values back to a feature table. The pipeline uses Spark Structured Streaming to process the data continuously. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Implementation

To create a streaming feature computation pipeline, pass a streaming `DataFrame` as an argument to the `write_table` method of the `FeatureEngineeringClient`. This method returns a `StreamingQuery` object that can be managed using standard Spark Structured Streaming APIs. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

```python
def compute_additional_customer_features(data):
  ''' Returns Streaming DataFrame
  '''
  pass

from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

customer_transactions = spark.readStream.table("prod.events.customer_transactions")
stream_df = compute_additional_customer_features(customer_transactions)

fe.write_table(
  df=stream_df,
  name='ml.recommender_system.customer_features',
  mode='merge'
)
```

When using `mode = "merge"`, the pipeline updates existing rows based on the primary key and inserts new rows for primary keys that do not yet exist in the feature table. This ensures that the feature table always reflects the latest state of the streaming data. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Use Cases

Streaming feature computation pipelines are particularly useful when:

- Features must reflect the most recent data available, such as user behavior signals or transaction-based features.
- The time lag between data ingestion and feature availability must be minimized for real-time or near-real-time [Model Serving](/concepts/model-serving.md).
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) need continuous updates to maintain point-in-time correctness for training and scoring.

## Relationship to Batch Updates

Streaming pipelines complement scheduled batch updates. While [Scheduled Jobs](/concepts/scheduled-jobs-with-ai-runtime.md) with `mode='merge'` periodically refresh feature tables on a fixed cadence (e.g., daily), streaming pipelines provide continuous updates between those batch runs. Both approaches can coexist on the same feature table. ^[feature-tables-in-unity-catalog-databricks-on-aws.md]

## Requirements

- The feature table must have a [Primary Key Constraint](/concepts/primary-key-constraint-for-feature-tables.md) defined. Streaming `write_table` operations require a primary key to determine which rows to update via the merge operation.
- The feature table must reside in [Unity Catalog](/concepts/unity-catalog.md).
- Feature Engineering in Unity Catalog requires Databricks Runtime 13.2 or above.

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The underlying storage for features managed by streaming pipelines.
- Streaming Table — A Delta Live Table that incrementally processes streaming data.
- [Structured Streaming](/concepts/structured-streaming-on-shared-tables.md) — The Apache Spark engine that powers continuous data processing.
- [Model Serving](/concepts/model-serving.md) — Downstream consumers that benefit from fresh feature values.
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with time-based primary keys that support point-in-time lookups.

## Sources

- feature-tables-in-unity-catalog-databricks-on-aws.md

# Citations

1. [feature-tables-in-unity-catalog-databricks-on-aws.md](/references/feature-tables-in-unity-catalog-databricks-on-aws-f1336f1e.md)
