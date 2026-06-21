---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c127b864cd35d6cde64ee93788762b3f87d0f403fcfb31480a2b130293a2ea5
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-workspace-feature-store-deprecated
    - DWFS(
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Databricks Workspace Feature Store (Deprecated)
description: The legacy databricks-feature-store Python package, deprecated as of version 0.17.0, with all modules moved to databricks-feature-engineering.
tags:
  - databricks
  - feature-store
  - deprecated
timestamp: "2026-06-19T18:47:49.217Z"
---

---
title: Databricks Workspace Feature Store (Deprecated)
summary: The legacy feature store for Databricks, now deprecated in favor of the Databricks Feature Engineering client and Unity Catalog-based feature tables.
sources:
  - feature-engineering-python-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:10:31.620Z"
updatedAt: "2026-06-18T08:10:31.620Z"
tags:
  - databricks
  - feature-store
  - deprecated
  - mlops
aliases:
  - workspace-feature-store-deprecated
  - legacy-feature-store
confidence: 0.99
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Workspace Feature Store (Deprecated)

**Databricks Workspace Feature Store** is the legacy feature management system on Databricks that stores feature tables within a workspace. It has been deprecated as of `databricks-feature-store` version 0.17.0. All existing modules from `databricks-feature-store` are now available in the `databricks-feature-engineering` package starting from version 0.2.0. ^[feature-engineering-python-api-databricks-on-aws.md]

## Deprecation and Migration

The `databricks-feature-store` package is deprecated. Users are strongly encouraged to migrate to the `databricks-feature-engineering` package, which provides APIs for working with feature tables in both Workspace Feature Store and [Unity Catalog](/concepts/unity-catalog.md). ^[feature-engineering-python-api-databricks-on-aws.md]

To migrate, install `databricks-feature-engineering` instead of `databricks-feature-store`. Existing import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work after installing the new package, so no code changes are required for existing code. ^[feature-engineering-python-api-databricks-on-aws.md]

### Key Migration Facts

- The deprecated package version is 0.17.0 and above.
- The replacement package `databricks-feature-engineering` version 0.2.0 and later contains all modules from the legacy package.
- To work with feature tables in Unity Catalog, use `FeatureEngineeringClient`.
- To continue using Workspace Feature Store, you must use `FeatureStoreClient`.
- `databricks-feature-engineering` versions ≤0.7.0 are not compatible with `mlflow≥2.18.0`. Upgrade to version 0.8.0 or above to use with MLflow 2.18.0 and later.

^[feature-engineering-python-api-databricks-on-aws.md]

## API Reference

For the latest Workspace Feature Store API reference, see the [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) reference documentation for `FeatureStoreClient`. For versions 0.16.3 and below, download the appropriate reference for your Databricks Runtime ML version using the compatibility matrix. ^[feature-engineering-python-api-databricks-on-aws.md]

## Installation

The deprecated Workspace Feature Store Python client is available on PyPI and is pre-installed in Databricks Runtime for Machine Learning. To install in a Databricks notebook or local environment: ^[feature-engineering-python-api-databricks-on-aws.md]

```python
%pip install databricks-feature-store
```

## Supported Scenarios

On Databricks Runtime and Databricks Runtime for Machine Learning, you can:

- Create, read, and write feature tables.
- Train and score models on feature data.
- Publish feature tables to online stores for real-time serving.

^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

The Workspace Feature Store client library can only be run on Databricks Runtime or Databricks Runtime for Machine Learning. It does not support calling Feature Engineering or Feature Store APIs from a local environment or any non-Databricks environment. ^[feature-engineering-python-api-databricks-on-aws.md]

## Testing

### Unit Testing

Install the Feature Store client locally to aid in running unit tests. Use `unittest.mock` to patch `FeatureStoreClient.write_table` and validate method calls. ^[feature-engineering-python-api-databricks-on-aws.md]

```python
from unittest.mock import MagicMock, patch
from databricks.feature_store import FeatureStoreClient

@patch.object(FeatureStoreClient, "write_table")
def test_update_customer_features(mock_write_table):
    customer_features_df = MagicMock()
    mock_write_table.assert_called_once_with(
        name='ml.recommender_system.customer_features',
        df=customer_features_df,
        mode='merge'
    )
```

### Integration Testing

Run integration tests with the Feature Store client on Databricks. See the CI/CD documentation for details. ^[feature-engineering-python-api-databricks-on-aws.md]

## Release Notes

See the [Databricks Feature Store](/concepts/databricks-feature-store.md) release notes for version history and changes. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) — The replacement API package for feature management.
- [Unity Catalog](/concepts/unity-catalog.md) — The recommended catalog for storing feature tables in Unity Catalog mode.
- [Feature Store vs Feature Engineering](/concepts/feature-store-and-feature-engineering.md) — Comparison between the legacy and modern approaches.
- [Online Feature Stores](/concepts/online-feature-store.md) — Publishing features for real-time serving.
- MLflow Integration with Feature Store — How feature tables integrate with MLflow experiments.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
