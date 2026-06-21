---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a504827d1e93c1a99ee8c6299a011eb58b6a936a1157c863605917dfb5e75870
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-engineering-python-api
    - DFEPA
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Databricks Feature Engineering Python API
description: The Python client library (databricks-feature-engineering) for working with feature tables and online stores on Databricks
tags:
  - databricks
  - feature-engineering
  - python-api
timestamp: "2026-06-18T12:18:07.311Z"
---

# Databricks Feature Engineering Python API

The Databricks Feature Engineering Python client (`databricks-feature-engineering`) provides APIs for working with feature tables and online stores. As of version 0.17.0, the legacy `databricks-feature-store` package has been deprecated, and all its modules are available in `databricks-feature-engineering` version 0.2.0 and later. ^[feature-engineering-python-api-databricks-on-aws.md]

## Package Installation

The `databricks-feature-engineering` package is available on PyPI and pre‑installed in Databricks Runtime 13.3 LTS ML and above. To install it in a Databricks notebook or a local Python environment:

```python
%pip install databricks-feature-engineering  # Databricks Runtime
pip install databricks-feature-engineering   # Local environment
```

^[feature-engineering-python-api-databricks-on-aws.md]

> **Note:** `databricks-feature-engineering` version 0.2.0 and later contains modules for both Unity Catalog and Workspace Feature Store. Versions below 0.2.0 only work with feature tables in Unity Catalog. ^[feature-engineering-python-api-databricks-on-aws.md]

## Compatibility

The client version you use depends on your [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) version and where your feature tables reside. Consult the official Feature Engineering compatibility matrix for exact mappings. ^[feature-engineering-python-api-databricks-on-aws.md]

> **Important:** `databricks-feature-engineering<=0.7.0` is not compatible with `mlflow>=2.18.0`. Upgrade to version 0.8.0 or above to use with MLflow 2.18.0+. ^[feature-engineering-python-api-databricks-on-aws.md]

## Migration from `databricks-feature-store`

To migrate, replace `pip install databricks-feature-store` with `pip install databricks-feature-engineering`. No code changes are required—imports such as `from databricks.feature_store import FeatureStoreClient` continue to work. ^[feature-engineering-python-api-databricks-on-aws.md]

For Unity Catalog feature tables, use `FeatureEngineeringClient`. For the Workspace Feature Store (deprecated), use `FeatureStoreClient`. ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported Scenarios

Within a Databricks environment (Databricks Runtime or Databricks Runtime for Machine Learning), you can: ^[feature-engineering-python-api-databricks-on-aws.md]
- Create, read, and write feature tables.
- Train and score models on feature data.
- Publish feature tables to online stores for real‑time serving.

From a local or external environment, you can:
- Develop code with local IDE support.
- Unit test using mock frameworks.
- Write integration tests to run on Databricks.

## Limitations

The client library can only be executed **on Databricks**. It does not support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local or non‑Databricks environment. ^[feature-engineering-python-api-databricks-on-aws.md]

## Testing

### Unit Testing

Install the package locally to unit‑test code that uses the Feature Engineering or Feature Store client. Use mocking frameworks to verify correct API calls, for example validating that a function calls `FeatureEngineeringClient.write_table` with the expected parameters. ^[feature-engineering-python-api-databricks-on-aws.md]

### Integration Testing

Run integration tests on Databricks using the client. See [CI/CD for Databricks](/concepts/devops-for-ml-on-databricks.md) for guidance. ^[feature-engineering-python-api-databricks-on-aws.md]

## API Reference

The full Python API reference for the Feature Engineering client is available online:
- [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html)

For the deprecated Workspace Feature Store (v0.17.0), the same reference applies. For v0.16.3 and below, see the compatibility matrix for links to the archived documentation. ^[feature-engineering-python-api-databricks-on-aws.md]

## Release Notes

Release notes are published under [Databricks Feature Store and legacy Workspace Feature Store release notes](https://docs.databricks.com/aws/en/release-notes/feature-store/databricks-feature-store). ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md) – Conceptual overview of feature management on Databricks.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer where Unity Catalog feature tables reside.
- Online Store for Feature Serving – Real‑time serving of feature values.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Runtime that includes the Feature Engineering client.
- [MLflow](/concepts/mlflow.md) – Experiment tracking and model management; compatibility considerations apply.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
