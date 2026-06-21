---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 12491000c7b879864be667974590dc342e21125b533ffd5622797dfcd60bd31a
  pageDirectory: concepts
  sources:
    - declarative-features-api-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - requestsource
  citations:
    - file: declarative-features-api-reference-databricks-on-aws.md
title: RequestSource
description: A data source that defines a schema for inference-time request payload data, used with ColumnSelection for pass-through features without pre-materialized tables
tags:
  - data-source
  - model-serving
  - feature-engineering
  - databricks
timestamp: "2026-06-18T11:45:07.392Z"
---

# RequestSource

**RequestSource** is a data source definition in the Databricks Declarative Feature Engineering API that specifies a schema for data provided at inference time — values sent as part of a model serving request payload — rather than data looked up from a pre-materialized table. During training, these values are extracted from the labeled DataFrame passed to `create_training_set`; during model serving, the calling application must include them in the HTTP request.^[declarative-features-api-reference-databricks-on-aws.md]

RequestSource is used exclusively with [ColumnSelection](/concepts/automl-column-selection.md) to pass through a value directly. It does not support [aggregation functions](/concepts/aggregationfunction-and-columnselection.md) or [Time Windows](/concepts/time-windows.md).^[declarative-features-api-reference-databricks-on-aws.md]

## Schema Definition

Define the schema as a list of `FieldDefinition` objects, each specifying a column name and a `ScalarDataType`:

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

## Supported Data Types

`RequestSource` supports the scalar types defined in `ScalarDataType`: `INTEGER`, `FLOAT`, `BOOLEAN`, `STRING`, `DOUBLE`, `LONG`, `TIMESTAMP`, `DATE`, `SHORT`. Complex types like arrays, maps, and structs are not supported.^[declarative-features-api-reference-databricks-on-aws.md]

## Usage

### Creating a RequestSource Feature

A `RequestSource` is paired with a `ColumnSelection` to define a pass-through feature — a value provided at inference time that is not computed from a historical table:

```python
from databricks.feature_engineering.entities import (
    ColumnSelection, Feature, RequestSource,
)

session_feature = Feature(
    source=request_source,
    function=ColumnSelection("session_duration"),
    name="session_duration",
)
```

^[declarative-features-api-reference-databricks-on-aws.md]

### Model Signature

When a model is logged using `log_model` with a training set that includes `RequestSource` features, the `RequestSource` columns are added to the MLflow model signature as required inputs. This means the serving endpoint's API schema documents which fields callers must provide at inference time.^[declarative-features-api-reference-databricks-on-aws.md]

## How Request Data is Hydrated

- **During training**: The values for `RequestSource` fields are extracted from the labeled DataFrame passed to `create_training_set`. The DataFrame must contain columns matching the `RequestSource` schema.^[declarative-features-api-reference-databricks-on-aws.md]
- **During model serving**: The caller must include the `RequestSource` fields in the HTTP request payload to the serving endpoint. The endpoint rejects requests that omit required fields.^[declarative-features-api-reference-databricks-on-aws.md]

## Comparison with DeltaTableSource

| Aspect | RequestSource | [DeltaTableSource](/concepts/deltatablesource.md) |
|--------|--------------|---------------------|
| Data origin | Provided in request payload at inference time | Looked up from a Delta table |
| Aggregation support | No | Yes (with entity and timeseries columns) |
| Time windows | Not supported | Supported (rolling, tumbling, sliding) |
| Use case | Real-time signals, session attributes, contextual data | Historical aggregates, computed features |

^[declarative-features-api-reference-databricks-on-aws.md]

## Sources

- declarative-features-api-reference-databricks-on-aws.md

# Citations

1. [declarative-features-api-reference-databricks-on-aws.md](/references/declarative-features-api-reference-databricks-on-aws-48fad3de.md)
