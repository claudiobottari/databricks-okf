---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41329094471c1e47057fa54edc0ad31c8cf0a81654f2d2971615c549fda6fb97
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-values-for-feature-lookups
    - DVFFL
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: Default values for feature lookups
description: A mechanism in FeatureLookup that supplies fallback values when a feature column has no value, with the restriction that renamed outputs must use the new name in default_values.
tags:
  - feature-store
  - error-handling
timestamp: "2026-06-18T12:18:51.539Z"
---

# Default values for feature lookups

**Default values for feature lookups** allow you to specify fallback values for feature columns in a `FeatureLookup` when the lookup key does not match any row in the source table, or when the feature value is `NULL`. By providing defaults, you ensure that your [FeatureSpec](/concepts/featurespec.md) always returns complete data for downstream inference or serving, even when the online feature store does not contain an entry for every key. ^[feature-serving-endpoints-databricks-on-aws.md]

## Specifying default values

To set default values, use the `default_values` parameter of the [FeatureLookup](/concepts/featurelookup.md) class when creating a `FeatureSpec`. The parameter accepts a dictionary where each key is a feature name (as defined in `feature_names`) and each value is the default to use when the lookup fails. ^[feature-serving-endpoints-databricks-on-aws.md]

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

In this example, if `customer_id` is not found in the `customer_features` table, the feature vector will substitute `18` for `age` and `"bronze"` for `membership_tier`. The `page_views_count_30days` column is omitted from the dictionary and will receive no default; if it is missing from the lookup result, it will be `NULL` or cause an error depending on the serving endpoint’s schema validation. ^[feature-serving-endpoints-databricks-on-aws.md]

## Defaults with renamed outputs

If you use the `rename_outputs` parameter to change the name of a feature column in the output, the `default_values` dictionary must use the **renamed** feature names, not the original column names. ^[feature-serving-endpoints-databricks-on-aws.md]

```python
FeatureLookup(
    table_name='main.default.table',
    feature_names=['materialized_feature_value'],
    lookup_key='id',
    rename_outputs={"materialized_feature_value": "feature_value"},
    default_values={
        "feature_value": 0
    }
)
```

Here, the original column `materialized_feature_value` is renamed to `feature_value` in the output. The default value `0` is specified under the renamed key `"feature_value"`. ^[feature-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [FeatureLookup](/concepts/featurelookup.md) – The class used to define a lookup from a feature table.
- [FeatureSpec](/concepts/featurespec.md) – A user-defined set of features and functions stored in Unity Catalog.
- [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) – Endpoints that serve the features defined in a `FeatureSpec`.
- [Online Feature Store](/concepts/online-feature-store.md) – The store from which feature lookups retrieve data.

## Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
