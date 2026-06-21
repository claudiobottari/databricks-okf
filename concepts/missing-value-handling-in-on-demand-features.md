---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f4c977100f4bb45bf068800de06b78d88e391b658f8e8ed66be48ef164d2bd7
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - missing-value-handling-in-on-demand-features
    - MVHIOF
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: Missing value handling in on-demand features
description: "Difference in how missing feature lookup values are returned depending on the environment: None for batch scoring vs float('nan') for online serving."
tags:
  - edge-cases
  - error-handling
  - feature-store
timestamp: "2026-06-19T19:49:37.738Z"
---

# Missing Value Handling in On-Demand Features

**Missing value handling in on-demand features** refers to the behavior and best practices for managing undefined or absent feature values during inference when using on-demand feature computation with Python user-defined functions (UDFs) on Databricks.

## Environment-Dependent Return Value

When a Python UDF depends on the result of a `FeatureLookup`, the value returned by the lookup if the requested key is not found depends on the inference environment:

- **Batch scoring (using `score_batch`)**: The missing lookup returns `None`.
- **Online serving (using [Model Serving](/concepts/model-serving.md))**: The missing lookup returns `float("nan")`.

^[on-demand-feature-computation-databricks-on-aws.md]

### Recommended Guard Code

Because the return type differs between environments, a robust UDF should handle both `None` and `NaN`. The following example from the documentation shows a UDF that squares an integer and returns `0` when the input is missing:

```sql
CREATE OR REPLACE FUNCTION square(x INT)
RETURNS INT
LANGUAGE PYTHON
AS $$
import numpy as np
if x is None or np.isnan(x):
  return 0
return x * x
$$
```

^[on-demand-feature-computation-databricks-on-aws.md]

## Default Values via FeatureLookup

An alternative way to handle missing values is to specify default values directly in the `FeatureLookup` definition using the `default_values` parameter. If the requested lookup key is not found in the feature table, the system uses the provided default value for that feature column.

```python
FeatureLookup(
  table_name = 'main.default.table',
  feature_names = ['materialized_feature_value'],
  lookup_key = 'id',
  default_values={
    "materialized_feature_value": 0
  }
)
```

### Renaming and Defaults

If the `rename_outputs` parameter is used to rename a feature column, the `default_values` dictionary must use the renamed column names instead of the original feature names.

^[on-demand-feature-computation-databricks-on-aws.md]

## Related Concepts

- On-demand feature computation – How Python UDFs are used for real-time feature calculation.
- [FeatureLookup](/concepts/featurelookup.md) – The mechanism to retrieve pre-materialized feature values.
- [Model Serving](/concepts/model-serving.md) – Online inference environment where missing values return `float("nan")`.
- [Unity Catalog UDFs](/concepts/unity-catalog.md) – Registration and management of Python UDFs used in on-demand features.
- Batch scoring with score_batch – Batch inference environment where missing values return `None`.

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
