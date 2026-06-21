---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 81c4a0ff0396f7f6f4d3ad82ace810d5e9cb498bb46afccba42f4efd7cf7ed5e
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requestsource-and-inference-time-features
    - Inference-Time Features and RequestSource
    - RAIF
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: RequestSource and Inference-Time Features
description: A data source type for features provided at inference time via HTTP request payload (or extracted from labeled DataFrame during training); uses FieldDefinition with ScalarDataType and is combined with ColumnSelection only.
tags:
  - inference
  - request-payload
  - feature-engineering
  - model-serving
timestamp: "2026-06-18T15:12:24.224Z"
---

# RequestSource and Inference-Time Features

**RequestSource** is a data source type in Databricks [Feature Engineering](/concepts/featureengineeringclient-api.md) that defines the schema for features provided at inference time in the request payload, rather than looked up from a pre‑materialized table. These are known as *inference‑time features* — values that are computed or supplied by the caller at the moment of scoring and are not available in offline [DeltaTableSource](/concepts/deltatablesource.md) backings. ^[declarative-features-api-reference-databricks-on-aws.md]

## Purpose

In many real‑time ML applications, some features cannot be pre‑computed from historical data because they depend on the current request context — for example, `transaction_amount`, `session_duration`, or `current_user_agent`. `RequestSource` allows a feature pipeline to accept such values directly at inference time, while still benefiting from the same feature engineering API, point‑in‑time correctness, and model lineage tracking used for offline features. ^[declarative-features-api-reference-databricks-on-aws.md]

## Defining a RequestSource

A `RequestSource` is constructed with a list of `FieldDefinition` objects, each specifying a column name and a `ScalarDataType`:

```python
from databricks.feature_engineering.entities import (
    FieldDefinition, RequestSource, ScalarDataType,
)

request_source = RequestSource(
    schema=[
        FieldDefinition(name="transaction_amount", data_type=ScalarDataType.DOUBLE),
        FieldDefinition(name="vendor_id", data_type=ScalarDataType.STRING),
        FieldDefinition(name="transaction_id", data_type=ScalarDataType.STRING),
        FieldDefinition(name="transaction_time", data_type=ScalarDataType.DATE),
    ]
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### Supported data types

`RequestSource` supports only scalar types defined in `ScalarDataType`: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`. Complex types such as arrays, maps, and structs are not supported. ^[declarative-features-api-reference-databricks-on-aws.md]

## Usage with ColumnSelection

`RequestSource` is used exclusively with [ColumnSelection](/concepts/automl-column-selection.md) (pass‑through features). It does **not** support aggregation functions (`AggregationFunction`) or time windows. When a `Feature` is defined with a `RequestSource` source and a `ColumnSelection` function, the value is simply passed through without any aggregation. ^[declarative-features-api-reference-databricks-on-aws.md]

```python
from databricks.feature_engineering.entities import (
    Feature, ColumnSelection, RequestSource,
)

session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## How request data is hydrated

### At training time

When you call `create_training_set()` with a DataFrame that includes columns matching the `RequestSource` schema, those columns are extracted directly from the labeled DataFrame. No lookback or point‑in‑time join is performed because inference‑time features are assumed to be provided alongside the training labels. ^[declarative-features-api-reference-databricks-on-aws.md]

### At inference time

During model serving, the caller must include the `RequestSource` columns in the HTTP request payload. The feature values are passed through to the model exactly as provided — no offline lookup is attempted. ^[declarative-features-api-reference-databricks-on-aws.md]

## Impact on model signature

When a model is logged using `log_model` with a training set that includes `RequestSource` features, those columns are added to the MLflow model signature as **required inputs**. This means the serving endpoint’s API schema automatically reflects which fields callers must supply at inference time, preventing missing‑feature errors at prediction time. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related concepts

- [DeltaTableSource](/concepts/deltatablesource.md) — Offline data source for pre‑computed features
- [ColumnSelection](/concepts/automl-column-selection.md) — Pass‑through feature function used with RequestSource
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — Overall framework for feature management
- FieldDefinition — Schema definition element
- ScalarDataType — Supported scalar types
- [create_training_set()](/concepts/point-in-time-training-sets.md) — Training API that extracts RequestSource columns
- log_model() — Model logging that bakes RequestSource schema into the model signature

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
