---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 520a53f53554af98e9c2e6fc1acc2bb2dca0a642f45cd8916634fba07523e641
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-engineering-python-client
    - DFEPC
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Databricks Feature Engineering Python Client
description: The databricks-feature-engineering Python package that provides APIs for working with feature tables and online stores in Unity Catalog and Workspace Feature Store.
tags:
  - databricks
  - feature-engineering
  - python-api
timestamp: "2026-06-19T18:47:36.633Z"
---

---
title: Databricks Feature Engineering Python Client
summary: The Python client library (`databricks-feature-engineering`) providing APIs for creating, reading, writing feature tables, training/scoring models, and publishing to online stores on Databricks.
sources:
  - feature-engineering-python-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:30:16.403Z"
updatedAt: "2026-06-19T10:30:16.403Z"
tags:
  - databricks
  - feature-engineering
  - python-client
  - machine-learning
aliases:
  - databricks-feature-engineering-python-client
  - DFEPC
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Databricks Feature Engineering Python Client

The **Databricks Feature Engineering Python Client** (`databricks-feature-engineering`) is the primary Python package for working with feature tables and online stores on Databricks. It provides APIs for creating, reading, writing, and managing feature tables, as well as training and scoring models on feature data, and publishing feature tables to online stores for real-time serving. ^[feature-engineering-python-api-databricks-on-aws.md]

## Package Overview

The `databricks-feature-engineering` package is available on [PyPI](https://pypi.org/project/databricks-feature-engineering) and is pre-installed in Databricks Runtime 13.3 LTS ML and above. As of version 0.2.0, the package contains modules for working with feature tables in both [Unity Catalog](/concepts/unity-catalog.md) and the deprecated Workspace Feature Store. Versions below 0.2.0 only work with feature tables in Unity Catalog. ^[feature-engineering-python-api-databricks-on-aws.md]

### Installation

To install the client in Databricks Runtime:

```python
%pip install databricks-feature-engineering
```

To install the client in a local Python environment:

```python
pip install databricks-feature-engineering
```

^[feature-engineering-python-api-databricks-on-aws.md]

## Deprecation of `databricks-feature-store`

As of version 0.17.0, the legacy `databricks-feature-store` package has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering` version 0.2.0 and later. When you install `databricks-feature-engineering`, import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work without any code changes. ^[feature-engineering-python-api-databricks-on-aws.md]

### Client Selection

The package and client you should use depend on where your feature tables are located:

- **`FeatureEngineeringClient`**: Use this client to work with feature tables in [Unity Catalog](/concepts/unity-catalog.md).
- **`FeatureStoreClient`**: Use this client to work with the deprecated Workspace Feature Store.

^[feature-engineering-python-api-databricks-on-aws.md]

## Compatibility

### MLflow Compatibility

`databricks-feature-engineering` version 0.7.0 and below is not compatible with `mlflow>=2.18.0`. To use the package with MLflow 2.18.0 and above, upgrade to `databricks-feature-engineering` version 0.8.0 or above. ^[feature-engineering-python-api-databricks-on-aws.md]

### Runtime Compatibility

For a reference of which client version corresponds to which Databricks Runtime ML version, see the Databricks documentation on the [Feature Engineering Compatibility Matrix](/concepts/feature-engineering-compatibility-matrix.md). ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported Scenarios

### On Databricks

On Databricks (including Databricks Runtime and [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)), you can:

- Create, read, and write feature tables.
- Train and score models on feature data.
- Publish feature tables to online stores for real-time serving.

^[feature-engineering-python-api-databricks-on-aws.md]

### From Local or External Environments

From a local environment or an environment external to Databricks, you can:

- Develop code with local IDE support.
- Unit test using mock frameworks.
- Write integration tests to be run on Databricks.

^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

The client library can only be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. It does not support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local environment or from an environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Unit Testing

The client can be installed locally to aid in running unit tests. For example, to validate that a method correctly calls `FeatureEngineeringClient.write_table`, you can use mocking:

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

^[feature-engineering-python-api-databricks-on-aws.md]

## Integration Testing

You can run integration tests with the Feature Engineering in Unity Catalog client or the Feature Store client on Databricks. For details, see Developer Tools and Guidance: Use CI/CD. ^[feature-engineering-python-api-databricks-on-aws.md]

## API Reference

For the complete Feature Engineering Python API reference, see the [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html). ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for managing feature tables
- [Feature Store](/concepts/feature-store.md) – The legacy workspace-level feature store (deprecated)
- [Online Stores](/concepts/online-feature-store.md) – For real-time model serving
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-built runtime with feature engineering support
- [Feature Engineering Compatibility Matrix](/concepts/feature-engineering-compatibility-matrix.md) – Client-to-runtime version mapping
- Developer Tools and Guidance: Use CI/CD – For integration testing workflows

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
