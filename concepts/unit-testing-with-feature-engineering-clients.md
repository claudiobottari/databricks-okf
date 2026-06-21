---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 38d3a71c40b524c208f7ccdc6c74ca27824c74f0bb8bb2ff4e2b180ce0dd2e10
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unit-testing-with-feature-engineering-clients
    - UTWFEC
    - Unit Testing with Feature Engineering
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Unit Testing with Feature Engineering Clients
description: The ability to install databricks-feature-engineering or databricks-feature-store locally to unit test code using mock frameworks like unittest.mock for validating feature table operations.
tags:
  - databricks
  - testing
  - unit-testing
  - mock
timestamp: "2026-06-19T10:29:36.728Z"
---

# Unit Testing with Feature Engineering Clients

**Unit Testing with Feature Engineering Clients** refers to the practice of writing automated unit tests for code that uses the Databricks Feature Engineering Python API (`databricks-feature-engineering`) or the legacy Workspace Feature Store API (`databricks-feature-store`). Because the client libraries cannot actually call Databricks APIs from a local environment, unit tests rely on mocking the client objects to verify that the correct methods are called with expected arguments. ^[feature-engineering-python-api-databricks-on-aws.md]

## Overview

The `databricks-feature-engineering` package is designed to run on Databricks (including Databricks Runtime and Databricks Runtime for Machine Learning). It does not support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local environment or from any environment other than Databricks. However, you can install the package locally to aid in running unit tests that validate the logic of your code without making actual API calls. ^[feature-engineering-python-api-databricks-on-aws.md]

## Installing the Package Locally

To install the client in a local Python environment for testing:

```bash
pip install databricks-feature-engineering
```

For the legacy Workspace Feature Store package (deprecated):

```bash
pip install databricks-feature-store
```

^[feature-engineering-python-api-databricks-on-aws.md]

## Unit Testing by Mocking the Client

The recommended approach is to use Python’s standard mocking framework (e.g., `unittest.mock`) to replace the client’s methods with `MagicMock` objects. This allows you to assert that your code calls the appropriate client methods (such as `write_table`) with the correct parameters, without needing a real backend connection. ^[feature-engineering-python-api-databricks-on-aws.md]

### Example: Testing a Function That Calls `write_table`

The following example validates that a function `update_customer_features` correctly invokes `FeatureEngineeringClient.write_table` with the expected table name, DataFrame, and write mode. The same pattern applies to `FeatureStoreClient` for the legacy Workspace Feature Store. ^[feature-engineering-python-api-databricks-on-aws.md]

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

In this test:

- `@patch.object(FeatureEngineeringClient, "write_table")` replaces the `write_table` method with a `MagicMock`.
- `@patch("my_feature_update_module.compute_customer_features")` mocks any data computation function.
- The assertion verifies that `write_table` was called once with the expected arguments.

^[feature-engineering-python-api-databricks-on-aws.md]

## Integration Testing

For integration tests that actually interact with Databricks, you must run the tests on a Databricks cluster (e.g., as part of a CI/CD pipeline). The same `FeatureEngineeringClient` or `FeatureStoreClient` can then make real API calls. For more details, see Integration Testing on Databricks and Developer Tools and Guidance: Use CI/CD. ^[feature-engineering-python-api-databricks-on-aws.md]

## Best Practices

- **Mock at the API boundary** – Mock the client methods (e.g., `write_table`, `read_table`, `create_table`) rather than lower-level HTTP calls. This keeps tests focused on business logic.
- **Use `MagicMock` for returned DataFrames** – When your tested function uses the result of a client call (e.g., a DataFrame), return a `MagicMock` with the expected interface.
- **Separate unit and integration tests** – Keep local unit tests fast and mock-dependent; run integration tests only on Databricks.

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) – Overview and installation guide.
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – The main client for feature tables in Unity Catalog.
- [FeatureStoreClient](/concepts/feature-store.md) – The legacy client for Workspace Feature Store.
- Integration Testing on Databricks – Running tests that interact with Databricks resources.
- Mocking in Python – General unit testing patterns with `unittest.mock`.
- Unit Testing – Broader testing methodology.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
