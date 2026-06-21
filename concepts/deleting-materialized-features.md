---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 106515fd9129301507a12aa5cec00aa45d1d4426223d43507989eafc6e0a8fc1
  pageDirectory: concepts
  sources:
    - materialize-declarative-features-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deleting-materialized-features
    - DMF
    - delete_materialized_feature() API
  citations:
    - file: materialize-declarative-features-databricks-on-aws.md
title: Deleting Materialized Features
description: Process for removing materialized features by passing the appropriate materialized feature object; aggregation features require deleting the offline version to propagate to both stores, while ColumnSelection features are deleted directly via online materialized feature.
tags:
  - feature-store
  - lifecycle
  - deletion
timestamp: "2026-06-19T19:31:22.699Z"
---

# Deleting Materialized Features

**Deleting Materialized Features** is the process of removing previously materialized [Declarative Features](/concepts/declarative-feature-engineering-api.md) from the [Feature Store](/concepts/feature-store.md) in Databricks. When you delete a materialized feature, the feature metadata is removed immediately, while associated infrastructure such as tables, pipelines, and jobs is cleaned up asynchronously by a background process. ^[materialize-declarative-features-databricks-on-aws.md]

## Prerequisites

Before deleting a materialized feature, you must remove or update any models or [Feature Specs](/concepts/featurespec.md) that reference the feature. Attempting to delete a feature that is still referenced by downstream resources can cause errors. ^[materialize-declarative-features-databricks-on-aws.md]

Materialized features can only be deleted in the workspace in which they were created. ^[materialize-declarative-features-databricks-on-aws.md]

## API Function

Use the `delete_materialized_feature()` method on the `FeatureEngineeringClient` to delete a materialized feature. The method accepts a `MaterializedFeature` object as its argument.

```python
FeatureEngineeringClient.delete_materialized_feature(
    materialized_feature: MaterializedFeature,  # Required: The materialized feature to delete
) -> None
```

^[materialize-declarative-features-databricks-on-aws.md]

Use `list_materialized_features()` to retrieve the `MaterializedFeature` objects to pass to the delete function. ^[materialize-declarative-features-databricks-on-aws.md]

## Behavior By Feature Type

### Aggregation Features

For aggregation features (created using `AggregationFunction`), pass the **offline** materialized feature to the delete function. When the offline materialized feature is deleted, both the offline and the paired online materialized features are deleted. The online materialized feature for an aggregation feature **cannot be deleted directly** — it is always deleted through its paired offline materialized feature. ^[materialize-declarative-features-databricks-on-aws.md]

### ColumnSelection Features

For `ColumnSelection` features, pass the **online** materialized feature directly. `ColumnSelection` features are materialized only to the online store (see [ColumnSelection Materialization](/concepts/columnselection-materialization.md)), so there is no paired offline feature to delete. ^[materialize-declarative-features-databricks-on-aws.md]

### [RequestSource Features](/concepts/requestsource-features.md)

`RequestSource` features cannot be materialized and therefore do not need to be deleted through this process. ^[materialize-declarative-features-databricks-on-aws.md]

## Example

The following example shows how to delete multiple materialized features of different types:

```python
from databricks.feature_engineering import FeatureEngineeringClient
from databricks.feature_engineering.entities import ColumnSelection

fe = FeatureEngineeringClient()

feature_names = [
    "main.feature_store.amount_sum_sliding_7d_1d",
    "main.feature_store.amount_sum_sliding_30d_1d",
    "main.feature_store.transaction_count_sliding_7d_1d",
    "main.feature_store.latest_transaction_amount",
    "main.feature_store.latest_user_tier",
]

for name in feature_names:
    feature = fe.get_feature(full_name=name)
    for mf in fe.list_materialized_features(feature_name=name):
        if isinstance(feature.function, ColumnSelection):
            # ColumnSelection features only have online materializations.
            # Delete the online materialized feature directly.
            fe.delete_materialized_feature(materialized_feature=mf)
        elif not mf.is_online:
            # Aggregation features have both offline and online materializations.
            # Delete the offline materialized feature to delete both.
            fe.delete_materialized_feature(materialized_feature=mf)
        # Online materialized aggregation features cannot be deleted directly.
        # They are deleted via their paired offline materialized features.
```

^[materialize-declarative-features-databricks-on-aws.md]

## Background Resource Cleanup

When you delete a materialized feature, Databricks removes the feature metadata immediately. However, because multiple materialized features can share the same tables and pipelines, the shared infrastructure is not removed until every materialized feature that references it has been deleted. ^[materialize-declarative-features-databricks-on-aws.md]

When the last materialized feature sharing a set of resources is deleted, a background process automatically deletes the following resources: ^[materialize-declarative-features-databricks-on-aws.md]

- The offline Delta tables containing the materialized feature data
- The online tables, if the features were materialized to an online store
- The materialization pipeline
- The orchestration job

This cleanup process uses a Databricks-managed system service principal to perform these actions on your behalf, including deleting tables, pipelines, and jobs in your workspace. No action is required from you — the cleanup is fully managed by the feature store. ^[materialize-declarative-features-databricks-on-aws.md]

### Important Notes

- There might be a short delay between deleting the last materialized feature in a group and the removal of the associated tables and other resources. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized aggregation features created before April 20, 2026, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted. To create an updated pipeline that supports per-feature delete, delete and re-materialize the feature. ^[materialize-declarative-features-databricks-on-aws.md]
- For materialized `ColumnSelection` features, the materialization pipeline continues producing new feature values until all materialized features in the pipeline have been deleted, which triggers resource cleanup. ^[materialize-declarative-features-databricks-on-aws.md]

## Limitations

- Materialized aggregation features: the online materialized feature cannot be deleted directly. Delete the paired offline materialized feature, and the change propagates to both. ^[materialize-declarative-features-databricks-on-aws.md]
- Materialized features can only be deleted in the workspace in which they were created. ^[materialize-declarative-features-databricks-on-aws.md]

## Related Concepts

- materialize_features() API|Materializing Features — The process of producing feature data from declarative feature definitions.
- [Declarative Feature API](/concepts/declarative-feature-engineering-api.md) — The API used to create features that can be materialized.
- [Feature Engineering Client](/concepts/featureengineeringclient-api.md) — The client object used to manage features and materialization.
- [Online Feature Store](/concepts/online-feature-store.md) — The store for features used in model serving.
- [Offline Feature Store](/concepts/offline-feature-store.md) — The store for features used in training and batch inference.

## Sources

- materialize-declarative-features-databricks-on-aws.md

# Citations

1. [materialize-declarative-features-databricks-on-aws.md](/references/materialize-declarative-features-databricks-on-aws-fe7c4a29.md)
