---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 428ea50db98b5f2a5c3200e1053f41c77bfab9adb6b1dc85f924bf958eb02cbc
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - featureengineeringclient-vs-featurestoreclient
    - FVF
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: FeatureEngineeringClient vs FeatureStoreClient
description: "Two distinct clients: FeatureEngineeringClient for Unity Catalog feature tables and FeatureStoreClient for the legacy Workspace Feature Store."
tags:
  - databricks
  - feature-engineering
  - api-differences
timestamp: "2026-06-19T18:48:06.856Z"
---

# FeatureEngineeringClient vs FeatureStoreClient

**FeatureEngineeringClient** and **FeatureStoreClient** are two Python client classes for managing feature tables on Databricks. `FeatureEngineeringClient` is the current, recommended client for working with feature tables in [Unity Catalog](/concepts/unity-catalog.md), while `FeatureStoreClient` is the legacy client for the deprecated [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). ^[feature-engineering-python-api-databricks-on-aws.md]

## Key Differences

| Aspect | FeatureEngineeringClient | FeatureStoreClient |
|--------|--------------------------|-------------------|
| **Package** | `databricks-feature-engineering` | `databricks-feature-store` |
| **Target catalog** | Unity Catalog | Workspace Feature Store (legacy) |
| **Status** | Current, actively developed | Deprecated as of v0.17.0 |
| **Minimum version** | v0.2.0+ | v0.17.0 and below |
| **API import** | `from databricks.feature_engineering import FeatureEngineeringClient` | `from databricks.feature_store import FeatureStoreClient` |

^[feature-engineering-python-api-databricks-on-aws.md]

As of version 0.17.0 of `databricks-feature-store` and version 0.2.0 of `databricks-feature-engineering`, all modules from `FeatureStoreClient` are now available in `FeatureEngineeringClient`. The `databricks-feature-store` package is no longer maintained. ^[feature-engineering-python-api-databricks-on-aws.md]

`FeatureEngineeringClient` below version 0.2.0 only works with feature tables in Unity Catalog. From version 0.2.0 and later, it contains modules for working with feature tables in both Unity Catalog and Workspace Feature Store. ^[feature-engineering-python-api-databricks-on-aws.md]

## When to Use Which Client

- **Use `FeatureEngineeringClient`** for all new projects and when working with feature tables in Unity Catalog. It is the recommended client for the current implementation.
- **Use `FeatureStoreClient` only** if you are still running on the deprecated `databricks-feature-store` package and have not yet migrated. The package will receive no future updates.

Both clients can be used for unit testing in local environments and for integration testing on Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported Scenarios

On Databricks (including Databricks Runtime and Databricks Runtime for Machine Learning), both clients support:

- Create, read, and write feature tables
- Train and score models on feature data
- Publish feature tables to online stores for real-time serving

From a local environment or external to Databricks, both clients support:

- Develop code with local IDE support
- Unit test using mock frameworks
- Write integration tests to be run on Databricks

^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

Both client libraries can only be run on Databricks environments (Databricks Runtime or Databricks Runtime for Machine Learning). They do not support calling Feature Engineering or Feature Store APIs from a local environment or from any environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Migration from FeatureStoreClient to FeatureEngineeringClient

To migrate from the deprecated `FeatureStoreClient` to `FeatureEngineeringClient`:

1. Install the new package: `pip install databricks-feature-engineering` instead of `pip install databricks-feature-store`
2. No code changes are required. Import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work after installing `databricks-feature-engineering` because the new package re-exports the legacy modules
3. To work with feature tables in Unity Catalog, use `FeatureEngineeringClient` explicitly
4. To use Workspace Feature Store, continue using `FeatureStoreClient` (available through the legacy module)

^[feature-engineering-python-api-databricks-on-aws.md]

## Compatibility

For a reference of which client version corresponds to which Databricks Runtime version, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). Note that `databricks-feature-engineering <= 0.7.0` is not compatible with `mlflow >= 2.18.0`. To use `databricks-feature-engineering` with MLflow 2.18.0 and above, upgrade to version 0.8.0 or higher. ^[feature-engineering-python-api-databricks-on-aws.md]

## Unit Testing Example

Both clients can be installed locally for unit testing. For example, to validate that a method correctly calls `FeatureEngineeringClient.write_table`:

```python
from unittest.mock import MagicMock, patch
from my_feature_update_module import update_customer_features
from databricks.feature_engineering import FeatureEngineeringClient

@patch.object(FeatureEngineeringClient, "write_table")
@patch("my_feature_update_module.compute_customer_features")
def test_something(compute_customer_features, mock_write_table):
    customer_features_df = MagicMock()
    compute_customer_features.return_value = customer_features_df
    update_customer_features()
    mock_write_table.assert_called_once_with(
        name='ml.recommender_system.customer_features',
        df=customer_features_df,
        mode='merge'
    )
```

^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The data governance solution for managing feature tables with `FeatureEngineeringClient`
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The legacy feature store that uses `FeatureStoreClient`
- [Feature Engineering](/concepts/featureengineeringclient-api.md) — The practice of creating and managing features for machine learning
- [Online Stores](/concepts/online-feature-store.md) — Real-time serving stores for feature tables
- MLflow Models — Models that can be trained and scored using feature data

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
