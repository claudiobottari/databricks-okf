---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1b0fb5ff7c6fc05c876e3f9cdb25e82741f605615c73473d31d4eeecccfa5cc7
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unit-testing-with-databricks-feature-engineering-clients
    - UTWDFEC
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Unit Testing with Databricks Feature Engineering Clients
description: Using mock frameworks (e.g., unittest.mock) to unit-test code that calls FeatureEngineeringClient or FeatureStoreClient APIs locally.
tags:
  - databricks
  - testing
  - unit-testing
timestamp: "2026-06-19T18:48:04.352Z"
---

```markdown
---
title: Unit testing with Databricks Feature Engineering clients
summary: Using mock frameworks to unit test code that calls FeatureEngineeringClient or FeatureStoreClient methods
sources:
  - feature-engineering-python-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:18:31.778Z"
updatedAt: "2026-06-18T12:18:31.778Z"
tags:
  - databricks
  - unit-testing
  - mock
  - python
aliases:
  - unit-testing-with-databricks-feature-engineering-clients
  - UTWDFEC
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Unit Testing with Databricks Feature Engineering Clients

The Databricks Feature Engineering Python client (`databricks-feature-engineering`) supports unit testing in local environments by allowing developers to mock client method calls. This enables validation of your code’s interactions with feature tables without requiring a running Databricks cluster. ^[feature-engineering-python-api-databricks-on-aws.md]

## Overview

The `databricks-feature-engineering` client library is designed to run on Databricks (including Databricks Runtime and Databricks Runtime for Machine Learning) and does not support calling Feature Engineering APIs from a local environment directly. However, you can install the package locally to aid in running unit tests by using Python’s standard mocking frameworks to simulate the client’s behavior. ^[feature-engineering-python-api-databricks-on-aws.md]

This approach works for both the newer `FeatureEngineeringClient` (for [[Unity Catalog]] feature tables) and the deprecated `FeatureStoreClient` (for [[Workspace Feature Store UI|Workspace Feature Store]]). ^[feature-engineering-python-api-databricks-on-aws.md]

## Installation for Testing

To use the client library in a local Python environment for unit testing:

```python
pip install databricks-feature-engineering
```

For projects still using the deprecated `databricks-feature-store` package:

```python
pip install databricks-feature-store
```

^[feature-engineering-python-api-databricks-on-aws.md]

## Mocking the Client

The recommended pattern is to use `unittest.mock.patch` to replace the client’s methods with MagicMock objects. This allows you to assert that your code calls the right methods with the expected arguments.

### Example: Testing `write_table` Calls

The following example validates that a function `update_customer_features` correctly calls `FeatureEngineeringClient.write_table`: ^[feature-engineering-python-api-databricks-on-aws.md]

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

### Key Elements of the Pattern

- **`@patch.object(FeatureEngineeringClient, "write_table")`** – Patches the `write_table` method on the client class, creating a mock that records all calls.
- **`@patch("my_feature_update_module.compute_customer_features")`** – Patches any dependencies your function uses to produce data.
- **`MagicMock()`** – Used to create a mock DataFrame that stands in for a real [[Spark DataFrame Evaluation Pattern|Spark DataFrame]] without needing a Spark session.
- **`assert_called_once_with()`** – Verifies that the client method was called exactly once with the specified arguments.

The same pattern applies to `FeatureStoreClient.write_table` for Workspace Feature Store usage. ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported Scenarios

Unit testing is one of several supported scenarios for the client library: ^[feature-engineering-python-api-databricks-on-aws.md]

| Scenario | Description |
|----------|-------------|
| Local environments | Develop code with local IDE support and unit test using mock frameworks |
| Databricks environments | Create, read, and write feature tables; train and score models; publish to online stores |
| Integration tests | Write integration tests to be run on Databricks (see [[DevOps for ML on Databricks|CI/CD for Databricks]]) |

## Limitations

The client library cannot call Feature Engineering or Feature Store APIs from a local environment. Unit testing must rely on mocking — you cannot perform actual read/write operations on feature tables outside of Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Best Practices

- **Mock at the client method level.** Patch `write_table`, `read_table`, or other methods your code calls, rather than mocking the entire client object. This keeps tests focused and maintainable.
- **Use MagicMock for DataFrames.** Avoid creating real Spark DataFrames in unit tests. Use `MagicMock()` to simulate DataFrame objects, as your code receiving a DataFrame should treat it as a black box.
- **Separate unit and integration tests.** Keep mocked unit tests in a separate directory or test file from your integration tests. Integration tests should run on Databricks and use the real client.
- **Verify call parameters.** Use assertions like `assert_called_once_with()` or `assert_any_call()` to confirm that your code passes the correct feature table name, DataFrame, write mode, and other parameters to the client.

## Related Concepts

- [[FeatureEngineeringClient API|FeatureEngineeringClient]] – The primary client for working with feature tables in Unity Catalog.
- [[Feature Store|FeatureStoreClient]] – The deprecated client for Workspace Feature Store (migrate to FeatureEngineeringClient).
- [[Databricks Feature Engineering Client|Databricks Feature Engineering]] – Overview of the feature management system.
- [[DevOps for ML on Databricks|CI/CD for Databricks]] – Running integration tests with real feature engineering clients on Databricks.
- MLflow with Feature Engineering – Using feature tables in MLflow training and serving workflows.

## Sources

- feature-engineering-python-api-databricks-on-aws.md
```

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
