---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6a6e2fd4c5a143717c1bbedcd2966f986219453cf147b7bd0629dbe5309e7408
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
    - troubleshooting-and-limitations-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-feature-engineering-package-installation
    - DFEPI
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
    - file: troubleshooting-and-limitations-databricks-on-aws.md
title: Databricks Feature Engineering package installation
description: Instructions for installing databricks-feature-engineering via pip in Databricks Runtime or local environments
tags:
  - databricks
  - installation
  - python-package
timestamp: "2026-06-18T12:18:24.851Z"
---

# Databricks Feature Engineering Package Installation

The **Databricks Feature Engineering package** (`databricks-feature-engineering`) is the Python client library for working with feature tables and online stores in Databricks. It provides APIs for creating, reading, and writing feature tables, training and scoring models on feature data, and publishing feature tables to online stores for real-time serving. ^[feature-engineering-python-api-databricks-on-aws.md]

## Package Overview

As of version 0.2.0, `databricks-feature-engineering` contains modules for working with feature tables in both [Unity Catalog](/concepts/unity-catalog.md) and the legacy Workspace Feature Store. Versions below 0.2.0 only work with feature tables in Unity Catalog. ^[feature-engineering-python-api-databricks-on-aws.md]

The package is available on [PyPI](https://pypi.org/project/databricks-feature-engineering) and is pre-installed in Databricks Runtime 13.3 LTS ML and above. For a compatibility matrix showing which client version corresponds to which runtime version, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]

## Installation

### On Databricks Runtime

To install the client in a Databricks notebook or cluster, use `%pip`:

```python
%pip install databricks-feature-engineering
```

^[feature-engineering-python-api-databricks-on-aws.md]

### In a Local Python Environment

To install the client for local development or unit testing:

```bash
pip install databricks-feature-engineering
```

^[feature-engineering-python-api-databricks-on-aws.md]

### On Lakeflow Spark Declarative Pipelines

When using Lakeflow Spark Declarative Pipelines as feature tables, Databricks Runtime ML clusters are not supported. Instead, use a standard access mode compute resource and manually install the client using `pip install databricks-feature-engineering`. You must also install any other required ML libraries. ^[troubleshooting-and-limitations-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering
```

## Version Compatibility

### MLflow Compatibility

`databricks-feature-engineering` version 0.7.0 and below is not compatible with `mlflow` version 2.18.0 and above. To use `databricks-feature-engineering` with MLflow 2.18.0 and above, upgrade to version 0.8.0 or above. ^[feature-engineering-python-api-databricks-on-aws.md]

### Runtime Compatibility

For a detailed compatibility matrix showing which package version is built into each Databricks Runtime ML version, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]

## Migration from Legacy Package

As of version 0.17.0, the legacy `databricks-feature-store` package has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering` version 0.2.0 and later. ^[feature-engineering-python-api-databricks-on-aws.md]

To migrate, install `databricks-feature-engineering` instead of `databricks-feature-store`:

```bash
pip install databricks-feature-engineering
```

All import statements such as `from databricks.feature_store import FeatureStoreClient` will continue to work after installing `databricks-feature-engineering`. No code changes are required. ^[feature-engineering-python-api-databricks-on-aws.md]

## Client Selection

After installation, choose the appropriate client based on your feature table location: ^[feature-engineering-python-api-databricks-on-aws.md]

| Feature Table Location | Client to Use |
|------------------------|---------------|
| Unity Catalog | `FeatureEngineeringClient` |
| Workspace Feature Store (legacy) | `FeatureStoreClient` |

## Troubleshooting

### ModuleNotFoundError

If you encounter `ModuleNotFoundError: No module named 'databricks.feature_engineering'`, the package is not installed on your Databricks Runtime. Install it with: ^[troubleshooting-and-limitations-databricks-on-aws.md]

```python
%pip install databricks-feature-engineering
```

For the legacy package, if you see `ModuleNotFoundError: No module named 'databricks.feature_store'`, install with: ^[troubleshooting-and-limitations-databricks-on-aws.md]

```python
%pip install databricks-feature-store
```

> **Note:** For Databricks Runtime 14.3 and above, install `databricks-feature-engineering` instead of the legacy `databricks-feature-store`. ^[troubleshooting-and-limitations-databricks-on-aws.md]

## Supported Scenarios

### On Databricks

On Databricks Runtime and Databricks Runtime for Machine Learning, you can: ^[feature-engineering-python-api-databricks-on-aws.md]

- Create, read, and write feature tables
- Train and score models on feature data
- Publish feature tables to online stores for real-time serving

### From Local or External Environments

From a local environment or an environment external to Databricks, you can: ^[feature-engineering-python-api-databricks-on-aws.md]

- Develop code with local IDE support
- Unit test using mock frameworks
- Write integration tests to be run on Databricks

### Limitations

The client library can only be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. It does not support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local environment or from an environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Unit Testing

You can install the Feature Engineering client locally to aid in running unit tests. For example, to validate that a method correctly calls `FeatureEngineeringClient.write_table`: ^[feature-engineering-python-api-databricks-on-aws.md]

```python
from unittest.mock import MagicMock, patch
from my_feature_update_module import update_customer_features
from databricks.feature_engineering import FeatureEngineeringClient

@patch.object(FeatureEngineeringClient, "write_table")
@patch("my_feature_update_module.compute_customer_features")
def test_something(compute_customer_features, mock_write_table):
    customer_features_df = MagicMock()
    compute_customer_features.return_value = customer_features_df
    update_customer_features()  # Function being tested
    mock_write_table.assert_called_once_with(
        name='ml.recommender_system.customer_features',
        df=customer_features_df,
        mode='merge'
    )
```

## Related Concepts

- [Feature Engineering Python API Reference](/concepts/featureengineeringclient-python-api.md) — The full API documentation
- Feature Store Compatibility Matrix — Runtime and package version mappings
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer for feature tables
- [Online Feature Store](/concepts/online-feature-store.md) — Publishing feature tables for real-time serving
- [Automatic Feature Lookup](/concepts/automatic-feature-lookup-for-model-serving.md) — Using feature tables with model serving

## Sources

- feature-engineering-python-api-databricks-on-aws.md
- troubleshooting-and-limitations-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
2. [troubleshooting-and-limitations-databricks-on-aws.md](/references/troubleshooting-and-limitations-databricks-on-aws-eb936059.md)
