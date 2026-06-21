---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac72cd61bd3130a97e6f54280ef854c7e910891d749cfeae6f7d4e201ac59eeb
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-legacy-feature-store-databricks-feature-store
    - DLFS(
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Databricks Legacy Feature Store (databricks-feature-store)
description: The deprecated legacy Python client package (databricks-feature-store) for workspace-level feature store operations, superseded by databricks-feature-engineering as of version 0.17.0.
tags:
  - databricks
  - feature-store
  - deprecated
  - legacy
timestamp: "2026-06-19T10:29:00.193Z"
---

# Databricks Legacy Feature Store (databricks-feature-store)

The **Databricks Legacy Feature Store** refers to the original feature store client package `databricks-feature-store`, which has been deprecated as of version 0.17.0. All modules from this package have been migrated to the newer `databricks-feature-engineering` package. ^[feature-engineering-python-api-databricks-on-aws.md]

## Deprecation Status

The `databricks-feature-store` package was deprecated starting with version 0.17.0. Existing code that imports from this package continues to work after installing `databricks-feature-engineering` because all modules have been preserved under the same import paths. Import statements such as `from databricks.feature_store import FeatureStoreClient` remain valid after migration. ^[feature-engineering-python-api-databricks-on-aws.md]

## Installation

The legacy package is available on [PyPI](https://pypi.org/project/databricks-feature-store) and was pre-installed in Databricks Runtime for Machine Learning. To install in Databricks Runtime: ^[feature-engineering-python-api-databricks-on-aws.md]

```python
%pip install databricks-feature-store
```

To install in a local Python environment:

```python
pip install databricks-feature-store
```

## Migrating to `databricks-feature-engineering`

To migrate from the legacy package, install `databricks-feature-engineering` instead of `databricks-feature-store`. All modules from `databricks-feature-store` have been moved to `databricks-feature-engineering` version 0.2.0 and later, so no code changes are required. ^[feature-engineering-python-api-databricks-on-aws.md]

When working with feature tables in Unity Catalog, use `FeatureEngineeringClient`. To continue using the Workspace Feature Store, use `FeatureStoreClient`. ^[feature-engineering-python-api-databricks-on-aws.md]

## API Reference

For the `databricks-feature-store` v0.17.0 API reference, see the [Feature Engineering Python API reference](/concepts/featureengineeringclient-python-api.md) for the latest Workspace Feature Store API. For v0.16.3 and below, see the compatibility matrix to determine the correct documentation version. ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported Scenarios

On Databricks Runtime and Databricks Runtime for Machine Learning, the legacy package supports: ^[feature-engineering-python-api-databricks-on-aws.md]

- Creating, reading, and writing feature tables
- Training and scoring models on feature data
- Publishing feature tables to online stores for real-time serving

From local or external environments, the package supports:
- Code development with local IDE support
- Unit testing using mock frameworks
- Writing integration tests to be run on Databricks

## Limitations

The client library can only be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. It does not support calling Feature Store APIs from a local environment or from an environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Engineering Client (databricks-feature-engineering)](/concepts/databricks-feature-engineering-client.md) — The modern replacement package
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The feature store implementation that the legacy package interacts with
- [Feature Store in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The newer feature store architecture
- [Feature Engineering Compatibility Matrix](/concepts/feature-engineering-compatibility-matrix.md) — Runtime version compatibility information

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
