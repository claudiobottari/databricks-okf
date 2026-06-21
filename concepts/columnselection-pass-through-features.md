---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8dcf5379caf47f40ffc596f47e048a7acdd2f221b8d504aa472ecf09f3a51d2b
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - columnselection-pass-through-features
    - C(F
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: ColumnSelection (Pass-through Features)
description: A non-aggregating function that selects a single column from a data source, returning the latest value per entity via point-in-time join or passing through inference-time request data.
tags:
  - feature-engineering
  - pass-through
  - column-selection
timestamp: "2026-06-19T14:56:53.967Z"
---

# ColumnSelection (Pass-through Features)

**ColumnSelection** is a feature engineering function in Databricks' Declarative Feature Engineering API that selects a single column from a data source without applying any aggregation. It is used to create pass-through features that return the raw column value directly, either from a Delta table or from inference-time request data. ^[declarative-features-api-reference-databricks-on-aws.md]

## Overview

Unlike [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md), which computes windowed aggregations like sums or averages over time, `ColumnSelection` passes through the column value as-is. The return type is inferred from the source schema. `ColumnSelection` is wrapped directly in the `function` parameter of a Feature object, not inside an `AggregationFunction`. ^[declarative-features-api-reference-databricks-on-aws.md]

## Usage with Data Sources

`ColumnSelection` can be used with any supported data source:

- **[DeltaTableSource](/concepts/deltatablesource.md)**: Returns the latest value per entity key via a point-in-time join. No lookback window aggregation is applied.
- **[RequestSource](/concepts/requestsource.md)**: Passes through the value provided at inference time in the request payload, or extracted from the labeled DataFrame at training time.

^[declarative-features-api-reference-databricks-on-aws.md]

### Example: ColumnSelection from a Delta Table

```python
from databricks.feature_engineering.entities import (
    ColumnSelection, DeltaTableSource, Feature,
)

delta_source = DeltaTableSource(
    catalog_name="main", schema_name="feature_store", table_name="transactions",
)

latest_amount = Feature(
    source=delta_source,
    function=ColumnSelection("amount"),
    entity=["user_id"],
    timeseries_column="transaction_time",
    name="latest_transaction_amount",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### Example: ColumnSelection from a RequestSource

```python
from databricks.feature_engineering.entities import (
    ColumnSelection, Feature, FieldDefinition,
    RequestSource, ScalarDataType,
)

request_source = RequestSource(
    schema=[
        FieldDefinition(name="session_duration", data_type=ScalarDataType.DOUBLE),
    ]
)

session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

## Materialization Triggers

`ColumnSelection` features backed by a `DeltaTableSource` use a TableTrigger for materialization. The pipeline runs whenever the upstream Delta table receives a new commit. This differs from aggregation features, which use CronSchedule triggers. ^[declarative-features-api-reference-databricks-on-aws.md]

### Important Constraint

You cannot mix `ColumnSelection` and aggregation features in a single `materialize_features` call because they require different trigger types. Separate calls must be issued for each type. ^[declarative-features-api-reference-databricks-on-aws.md]

## Related Concepts

- [Declarative Feature Engineering API](/concepts/declarative-feature-engineering-api.md) — The overarching API framework for defining features
- [AggregationFunction](/concepts/aggregationfunction-and-columnselection.md) — The counterpart to ColumnSelection for windowed aggregations
- Feature — The core entity that wraps a data source and function together
- [DeltaTableSource](/concepts/deltatablesource.md) — Data source for Delta table-backed features
- [RequestSource](/concepts/requestsource.md) — Data source for inference-time request features
- materialize_features() API|Materialized Features — How features are materialized for low-latency serving

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
