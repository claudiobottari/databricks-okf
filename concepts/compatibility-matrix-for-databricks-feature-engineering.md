---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8a88a4055fa43cadc86bf52a5f03039813a8b01355dcec491f8708dcb4a8fec
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - compatibility-matrix-for-databricks-feature-engineering
    - CMFDFE
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Compatibility matrix for Databricks Feature Engineering
description: A table mapping Databricks Runtime ML versions to the appropriate databricks-feature-engineering or databricks-feature-store package versions
tags:
  - databricks
  - compatibility
  - runtime
timestamp: "2026-06-18T12:18:16.322Z"
---

# Compatibility Matrix for Databricks Feature Engineering

## Overview

The compatibility matrix for Databricks Feature Engineering helps you determine which Python client package and version to use based on where your feature tables are located (Unity Catalog or Workspace Feature Store) and which Databricks Runtime ML version you are running. ^[feature-engineering-python-api-databricks-on-aws.md]

The key packages are:

- **`databricks-feature-engineering`** – The primary client for working with feature tables in both Unity Catalog (≥0.2.0) and the legacy Workspace Feature Store (≥0.2.0). ^[feature-engineering-python-api-databricks-on-aws.md]
- **`databricks-feature-store`** – The deprecated legacy client (≤0.17.0). Its modules have been moved into `databricks-feature-engineering` version 0.2.0 and later. ^[feature-engineering-python-api-databricks-on-aws.md]

## Package and Runtime Compatibility

Databricks Runtime ML versions include a pre-installed version of the client. To find the exact version that ships with your runtime, consult the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]

In general:

- `databricks-feature-engineering` is pre-installed in Databricks Runtime 13.3 LTS ML and above. ^[feature-engineering-python-api-databricks-on-aws.md]
- The `databricks-feature-store` package is pre-installed in earlier Databricks Runtime for Machine Learning versions, but usage is deprecated. ^[feature-engineering-python-api-databricks-on-aws.md]

## MLflow Compatibility

`databricks-feature-engineering` version ≤0.7.0 is **not compatible** with `mlflow` version ≥2.18.0. If you are using MLflow 2.18.0 or later, you must upgrade to `databricks-feature-engineering` version 0.8.0 or above. ^[feature-engineering-python-api-databricks-on-aws.md]

## Identifying Your Version

You can determine the installed package version by running:

```python
import databricks.feature_engineering
print(databricks.feature_engineering.__version__)
```

For the legacy package:

```python
import databricks.feature_store
print(databricks.feature_store.__version__)
```

For a reference of which client version corresponds to each Databricks Runtime ML release, see the official [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Databricks Feature Engineering](/concepts/databricks-feature-engineering-client.md) – The service for managing feature tables
- [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md) – Legacy feature store
- [Unity Catalog](/concepts/unity-catalog.md) – Catalog that can host feature tables
- [MLflow](/concepts/mlflow.md) – Lifecycle management for ML models
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Optimized runtime for machine learning workloads

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
