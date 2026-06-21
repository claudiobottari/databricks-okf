---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7ef939222f113196a3207d49ddbf76f004f0a7bca7b54adbf96ebe098856afda
  pageDirectory: concepts
  sources:
    - feature-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featurespec-default-values
    - FDV
    - Column Default Values
  citations:
    - file: feature-serving-endpoints-databricks-on-aws.md
title: FeatureSpec Default Values
description: The ability to specify fallback default values for feature lookups within a FeatureSpec, which are used when a lookup key is not found in the feature table.
tags:
  - feature-engineering
  - data-quality
  - databricks
timestamp: "2026-06-19T10:30:19.527Z"
---

Here is the wiki page for "FeatureSpec Default Values".

---

## FeatureSpec Default Values

**FeatureSpec Default Values** allow you to specify fallback values for features defined in a `FeatureLookup` within a [FeatureSpec](/concepts/featurespec.md). When a lookup request provides an input key that does not have a corresponding row in the source table, or if the requested feature column is `NULL` for a given key, the default value is returned instead. This prevents missing data from causing errors or `NULL` values in the feature vector served to downstream models or applications. ^[feature-serving-endpoints-databricks-on-aws.md]

### How to Specify Default Values

Default values are set per-`FeatureLookup` using the `default_values` parameter. The parameter accepts a dictionary where each key is a feature name and each value is the fallback to use when that feature is missing. ^[feature-serving-endpoints-databricks-on-aws.md]

The following example creates a `FeatureLookup` with default values for the `age` and `membership_tier` features:

```python
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

### Interaction with Output Renaming

If the `FeatureLookup` renames output columns using the `rename_outputs` parameter, the keys in the `default_values` dictionary must use the **renamed** feature names, not the source column names. ^[feature-serving-endpoints-databricks-on-aws.md]

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

### How Default Values Are Applied

Default values are resolved at query time when a [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) processes an incoming request. The endpoint looks up the requested features from the source table; for any requested feature key where no row is found or where the column value is `NULL`, the configured default value is returned as part of the feature vector. ^[feature-serving-endpoints-databricks-on-aws.md]

### Limitations

The source material does not describe any specific limitations on default values.

### Related Concepts

- [FeatureSpec](/concepts/featurespec.md) — The user-defined set of features and functions that an endpoint serves.
- [FeatureLookup](/concepts/featurelookup.md) — A component of a `FeatureSpec` that retrieves features from a table by key.
- [Feature Serving endpoints](/concepts/feature-serving-endpoint.md) — The serving infrastructure that hosts `FeatureSpec`s online.
- [Online Feature Store](/concepts/online-feature-store.md) — The store where feature tables are published for low-latency serving.

### Sources

- feature-serving-endpoints-databricks-on-aws.md

# Citations

1. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
