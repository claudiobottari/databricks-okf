---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 596729cf588adb2d69e9ef65fdf346f7abbf8239cd658c3e29767b41d2b2a4e1
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-compatibility-with-databricks-feature-engineering
    - MCWD
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
    - file: feature-engineering-python-api-databricks-on-aws.md
      start: 19
      end: 21
title: MLflow Compatibility with databricks-feature-engineering
description: A compatibility note that databricks-feature-engineering versions <=0.7.0 are incompatible with mlflow >=2.18.0, requiring an upgrade to databricks-feature-engineering 0.8.0 or above.
tags:
  - databricks
  - mlflow
  - compatibility
  - versioning
timestamp: "2026-06-19T10:29:42.446Z"
---

# MLflow Compatibility with databricks-feature-engineering

**MLflow Compatibility with databricks-feature-engineering** refers to the version requirements needed for the `databricks-feature-engineering` Python package to correctly interoperate with MLflow, especially for training and scoring models using feature tables. As the package evolves, specific version combinations are required to avoid runtime errors.

## Overview

`databricks-feature-engineering` is a Python client that provides APIs for working with feature tables in both Unity Catalog and the legacy Workspace Feature Store. It is commonly used alongside MLflow to log models, manage feature metadata, and serve inferences. The package is pre-installed in Databricks Runtime 13.3 LTS ML and above, and can be installed via `pip install databricks-feature-engineering`. ^[feature-engineering-python-api-databricks-on-aws.md]

## Version Compatibility

The most critical compatibility requirement is between `databricks-feature-engineering` and `mlflow`:

- **`databricks-feature-engineering` version ≤ 0.7.0** is **not compatible** with `mlflow` version ≥ 2.18.0.
- To use `databricks-feature-engineering` with MLflow 2.18.0 or later, you must **upgrade** to `databricks-feature-engineering` version **0.8.0** or above. ^[feature-engineering-python-api-databricks-on-aws.md:19-21]

This restriction is documented in a note on the Feature Engineering Python API page. Users who encounter errors when calling `mlflow` functions after upgrading MLflow should check and update the `databricks-feature-engineering` package.

## Migration Considerations

As of version 0.2.0, `databricks-feature-engineering` contains all modules previously found in the deprecated `databricks-feature-store` package (legacy Workspace Feature Store). Import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work after installing `databricks-feature-engineering`. However, to work with feature tables in Unity Catalog, use `FeatureEngineeringClient`. ^[feature-engineering-python-api-databricks-on-aws.md]

When migrating from `databricks-feature-store` to `databricks-feature-engineering`, ensure the installed version is at least 0.2.0 and also satisfies the MLflow compatibility requirement (≥ 0.8.0 for MLflow ≥ 2.18.0).

## Usage with MLflow

The `databricks-feature-engineering` client is designed to support the following MLflow-related workflows on Databricks:

- Training and scoring models on feature data.
- Publishing feature tables to online stores for real-time serving.
- Logging model artifacts with feature metadata (via MLflow’s integration with the Feature Engineering API).

For detailed API usage, see the [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html).

## Related Concepts

- [MLflow](/concepts/mlflow.md)
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- Feature Store Client
- [Online Store](/concepts/online-feature-store.md)

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
2. [feature-engineering-python-api-databricks-on-aws.md:19-21](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
