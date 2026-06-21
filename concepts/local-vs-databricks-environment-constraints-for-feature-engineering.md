---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: df85113a5e8412419f6db6fb4d0101d12d46e242d8381c5303d652fc06309f45
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - local-vs-databricks-environment-constraints-for-feature-engineering
    - LVDECFFE
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Local vs Databricks Environment Constraints for Feature Engineering
description: The limitation that the client library can only run on Databricks (Runtime or ML Runtime) for actual API calls, but can be installed locally for code development, IDE support, and unit testing.
tags:
  - databricks
  - environment
  - limitations
  - development
timestamp: "2026-06-19T10:29:33.772Z"
---

# Local vs Databricks Environment Constraints for Feature Engineering

The **Local vs Databricks Environment Constraints for Feature Engineering** refer to the specific limitations and allowed operations when using the Databricks Feature Engineering Python client (`databricks-feature-engineering`) in a local development environment compared to a Databricks Runtime environment. Understanding these constraints is critical for designing development, testing, and deployment workflows for feature tables and online stores.

## Overview

The `databricks-feature-engineering` package provides APIs for creating, reading, writing, training, scoring, and publishing feature tables to online stores. However, the client library’s ability to execute these operations depends on where it is running. The library is designed to work fully only on Databricks infrastructure (Databricks Runtime or Databricks Runtime for Machine Learning); it cannot make direct API calls to Feature Engineering in Unity Catalog or the Workspace Feature Store from a local environment. ^[feature-engineering-python-api-databricks-on-aws.md]

## Key Constraints

### Local Environment Limitations

- **No direct API calls to Databricks**: The client library does **not** support calling Feature Engineering in Unity Catalog APIs or Feature Store APIs from a local environment or any non-Databricks environment. Operations like `write_table`, `read_table`, or publishing to an online store will fail if run locally. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Installation is possible locally**: Users can install the `databricks-feature-engineering` package locally (e.g., via `pip install databricks-feature-engineering`) for code development with IDE support and for running unit tests. However, these tests must simulate Databricks operations using mocking frameworks rather than performing real API calls. ^[feature-engineering-python-api-databricks-on-aws.md]

### Databricks Environment Requirements

- **Full API support requires Databricks Runtime**: All Feature Engineering client operations (create, read, write, train, score, publish) are fully supported only when the client runs inside a Databricks Runtime or Databricks Runtime for Machine Learning environment. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Pre-installed in certain runtimes**: The `databricks-feature-engineering` package is pre-installed in Databricks Runtime 13.3 LTS ML and above. For earlier runtimes, users must install the package manually using `%pip install databricks-feature-engineering` within a notebook or cluster. ^[feature-engineering-python-api-databricks-on-aws.md]

## Development and Testing Workflow

Despite the limitations, the client library supports a structured workflow that separates development and testing:

| Activity | Local Environment | Databricks Environment |
|----------|-------------------|------------------------|
| Code development with IDE | Supported | Supported |
| Unit testing | Supported (using mock frameworks like `unittest.mock`) | Supported |
| Integration testing | Not supported | Supported (run on Databricks) |
| API calls to feature tables | Not supported | Supported |

^[feature-engineering-python-api-databricks-on-aws.md]

### Example: Unit Testing Locally with Mocks

The following pattern validates that a function correctly calls `FeatureEngineeringClient.write_table` without needing a Databricks cluster:

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

Integration tests that exercise real feature table operations must be executed on a Databricks cluster, as described in the CI/CD developer tools and guidance. ^[feature-engineering-python-api-databricks-on-aws.md]

## Summary

In short, the Databricks Feature Engineering client is a **Databricks-only runtime library** for production operations. Local development is limited to writing code, unit testing, and preparing integration tests that will run on Databricks. This architectural constraint ensures that all interactions with feature tables occur within the secure and governed Databricks environment, while still enabling a rapid local development loop through mocking.

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) – The core client library and its functions.
- [Feature Tables](/concepts/feature-tables.md) – The storage objects for features (Unity Catalog or Workspace Feature Store).
- [Unity Catalog](/concepts/unity-catalog.md) – The governed catalog system for feature tables.
- [Online Stores](/concepts/online-feature-store.md) – Real-time serving endpoints for features.
- CI/CD on Databricks – Guidance for running integration tests on Databricks.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that pre-installs the client.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
