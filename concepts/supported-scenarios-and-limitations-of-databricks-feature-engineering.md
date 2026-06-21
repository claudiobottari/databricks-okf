---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 581f3acbc63786354c73b03a17897b671a74eb37ee78e51a83e67c7d3f132e4d
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - supported-scenarios-and-limitations-of-databricks-feature-engineering
    - limitations of Databricks Feature Engineering and Supported scenarios
    - SSALODFE
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Supported scenarios and limitations of Databricks Feature Engineering
description: Scenarios where the Feature Engineering client can be used (Databricks Runtime) and where it cannot (local/external environments)
tags:
  - databricks
  - limitations
  - supported-environments
timestamp: "2026-06-18T12:18:29.564Z"
---

# Supported scenarios and limitations of Databricks Feature Engineering

**Databricks Feature Engineering** provides a Python client (`databricks-feature-engineering`) for creating, managing, and serving feature tables. The client supports a range of development and production scenarios on Databricks and in local or external environments, but has specific limitations regarding where the client itself can execute API calls. ^[feature-engineering-python-api-databricks-on-aws.md]

## Supported scenarios

### On Databricks (Databricks Runtime and Databricks Runtime for Machine Learning)

When running on Databricks, you can use the Feature Engineering client to:

- Create, read, and write feature tables.
- Train and score models using feature data.
- Publish feature tables to online stores for real-time serving.

All of these operations are supported on Databricks Runtime and Databricks Runtime for Machine Learning. ^[feature-engineering-python-api-databricks-on-aws.md]

### From a local or external environment

Outside Databricks, the client is **not** intended for API calls to Feature Engineering, but you can use the installed package for development and testing:

- Develop code with local IDE support.
- Unit test using mock frameworks (e.g., `unittest.mock`).
- Write integration tests to be run later on Databricks.

These scenarios allow you to validate your application logic without requiring a live Databricks connection. ^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

The client library can only be run on Databricks (including Databricks Runtime and Databricks Runtime for Machine Learning). It does **not** support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local environment or from any environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

This means that while you can install the package locally for unit testing or code development, you cannot perform actual read/write operations on feature tables, publish to online stores, or train models with feature data from outside a Databricks cluster.

## Unit testing with mock frameworks

You can install the Feature Engineering client locally to aid in unit testing. The client classes (e.g., `FeatureEngineeringClient` or `FeatureStoreClient`) can be patched with `unittest.mock` to verify that your application code calls the correct methods with expected arguments. ^[feature-engineering-python-api-databricks-on-aws.md]

The following example demonstrates how to mock `FeatureEngineeringClient.write_table`:

```python
from unittest.mock import MagicMock, patch
from my_feature_update_module import update_customer_features
from databricks.feature_engineering import FeatureEngineeringClient

@patch.object(FeatureEngineeringClient, "write_table")
@patch("my_feature_update_module.compute_customer_features")
def test_something(compute_customer_features, mock_write_table):
    customer_features_df = MagicMock()
    compute_customer_features.return_value = customer_features_df
    update_customer_features()
    mock_write_table.assert_called_once_with(
        name='ml.recommender_system.customer_features',
        df=customer_features_df,
        mode='merge'
    )
```

^[feature-engineering-python-api-databricks-on-aws.md]

## Integration testing

Integration tests that involve actual Feature Engineering operations must be run on Databricks. You can write the test logic locally and then execute it on a Databricks cluster as part of a CI/CD pipeline. See Developer Tools and Guidance: Use CI/CD. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related concepts

- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — The primary client for Unity Catalog feature tables.
- [FeatureStoreClient](/concepts/feature-store.md) — The deprecated client for Workspace Feature Store.
- [Migration to databricks-feature-engineering](/concepts/upgradeclient-databricks-feature-engineering.md) — Transition guide from the deprecated package.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — The pre-configured environment that bundles the Feature Engineering client.
- [Online stores for real-time serving](/concepts/third-party-online-stores-for-feature-serving.md) — Publishing feature tables to low-latency serving stores.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
