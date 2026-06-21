---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 789a213c65b14ec73901859fc377a53fad61b69e94f0d79ed6487b20e22d9b1c
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-serving-default-values
    - FSDV
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Feature Serving Default Values
description: A mechanism to supply fallback values for feature lookups when keys are not found in the online store, requiring renamed feature names when using rename_outputs.
tags:
  - feature-store
  - resilience
  - api
timestamp: "2026-06-19T18:48:24.298Z"
---

# Feature Serving Default Values

**Feature Serving Default Values** allow you to specify fallback values for [feature lookups](/concepts/featurelookup.md) in a [FeatureSpec](/concepts/featurespec.md) when a lookup key is missing from the online feature store or when the feature value is null. Default values ensure that Feature Serving endpoints can still return complete responses even when some data is unavailable.

## Overview

When you define a [FeatureSpec](/concepts/featurespec.md) using the `databricks-feature-engineering` package, you can provide default values for features in a [FeatureLookup](/concepts/featurelookup.md). If a lookup key does not match any row in the underlying feature table, or if the feature column contains a null value, the system substitutes the default value instead of returning an error or an empty result. ^[feature-serving-endpoints-databricks-on-aws.md]

Default values are optional. Without them, a missing lookup key or null feature value causes the serving endpoint to fail for that request record. ^[feature-serving-endpoints-databricks-on-aws.md]

## Specifying Default Values

Use the `default_values` parameter of the `FeatureLookup` class. The parameter accepts a dictionary where the keys are feature column names and the values are the fallback values. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureLookup

feature_lookups = [
    FeatureLookup(
        table_name="ml.recommender_system.customer_features",
        feature_names=[
            "membership_tier",
            "age",
            "page_views_count_30days",
        ],
        lookup_key="customer_id",
        default_values={
          "age": 18,
          "membership_tier": "bronze"
        },
    ),
]
```

^[feature-serving-endpoints-databricks-on-aws.md]

In this example, if a `customer_id` is not found, the endpoint returns `age` as 18 and `membership_tier` as "bronze" instead of failing.

## Default Values with Renamed Outputs

If you rename feature columns using the `rename_outputs` parameter, the `default_values` dictionary must use the renamed output names, not the original column names. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
FeatureLookup(
  table_name = 'main.default.table',
  feature_names = ['materialized_feature_value'],
  lookup_key = 'id',
  rename_outputs={"materialized_feature_value": "feature_value"},
  default_values={
    "feature_value": 0
  }
)
```

^[feature-serving-endpoints-databricks-on-aws.md]

Here, the default value is specified using the renamed key `"feature_value"`, not the original column name `"materialized_feature_value"`.

## Behavior

When a request contains a lookup key that does not exist in the feature table:
- Features with a defined default value return the default.
- Features without a default value cause the request to fail.

Default values apply only to features in `FeatureLookup` objects, not to features computed by [FeatureFunction](/concepts/featurefunction.md) objects. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions served by an endpoint.
- [FeatureLookup](/concepts/featurelookup.md) — A component that retrieves feature values from an online feature table by key.
- [FeatureFunction](/concepts/featurefunction.md) — A component that computes feature values using a UDF.
- [Online Feature Store](/concepts/online-feature-store.md) — The store from which feature lookups read data.
- [Feature Serving Endpoints](/concepts/feature-serving-endpoint.md) — The serving infrastructure that uses the FeatureSpec to respond to queries.

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
