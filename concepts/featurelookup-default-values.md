---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5fea5961259e2e6ae29760b1efb9007f14e531a9efb298ceadf54dde8545d09d
  pageDirectory: concepts
  sources:
    - on-demand-feature-computation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurelookup-default-values
    - FDV
  citations:
    - file: on-demand-feature-computation-databricks-on-aws.md
title: FeatureLookup default values
description: Mechanism to specify default values for feature lookups when lookup keys are missing, with special handling when using rename_outputs.
tags:
  - feature-store
  - configuration
  - databricks
timestamp: "2026-06-19T19:49:38.901Z"
---

# FeatureLookup Default Values

**FeatureLookup default values** allow you to specify fallback values for features when a requested lookup key is not found in the feature table. This ensures that feature computation can proceed without errors when data is missing, and is particularly useful in combination with On-Demand Feature Computation.

## Overview

When using `FeatureLookup` in Databricks Feature Store, you can provide default values for features that may not be present for every lookup key. This is done through the `default_values` parameter when constructing a `FeatureLookup`. ^[on-demand-feature-computation-databricks-on-aws.md]

## Specification

The `default_values` parameter accepts a dictionary where keys are feature column names and values are the fallback values to use when the lookup key is not found. For example:

```python
from databricks.feature_engineering import FeatureLookup

FeatureLookup(
    table_name='main.default.table',
    feature_names=['materialized_feature_value'],
    lookup_key='id',
    default_values={
        "materialized_feature_value": 0
    }
)
```

^[on-demand-feature-computation-databricks-on-aws.md]

## Interaction with Renamed Outputs

If you rename feature columns using the `rename_outputs` parameter, the `default_values` dictionary must use the renamed feature names, not the original column names. Example:

```python
FeatureLookup(
    table_name='main.default.table',
    feature_names=['materialized_feature_value'],
    lookup_key='id',
    rename_outputs={"materialized_feature_value": "feature_value"},
    default_values={
        "feature_value": 0  # Uses renamed output name
    }
)
```

^[on-demand-feature-computation-databricks-on-aws.md]

## Context: Missing Feature Values

Default values are particularly relevant in the context of On-Demand Feature Computation, where a Python UDF may depend on the result of a `FeatureLookup`. The actual value returned when a lookup key is not found differs by environment:

- **Batch scoring** (`score_batch`): Returns `None`
- **Online serving**: Returns `float("nan")`

^[on-demand-feature-computation-databricks-on-aws.md]

A Python UDF can handle both cases using logic such as:

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

Using `default_values` in the `FeatureLookup` provides an alternative approach to handling missing keys, ensuring that the downstream UDF or model always receives a well-defined value.

## Related Concepts

- On-Demand Feature Computation — Features computed at inference time using Python UDFs
- [FeatureLookup](/concepts/featurelookup.md) — The lookup mechanism for retrieving pre-materialized features
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client API for creating training sets and logging models
- [Feature Store](/concepts/feature-store.md) — Central repository for feature tables and metadata

## Sources

- on-demand-feature-computation-databricks-on-aws.md

# Citations

1. [on-demand-feature-computation-databricks-on-aws.md](/references/on-demand-feature-computation-databricks-on-aws-0b31cd40.md)
