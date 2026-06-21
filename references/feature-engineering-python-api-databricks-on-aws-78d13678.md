---
title: Feature Engineering Python API | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/feature-store/python-api
ingestedAt: "2026-06-18T08:10:31.620Z"
---

The Databricks Feature Engineering Python client (`databricks-feature-engineering`) provides APIs for working with feature tables and online stores. This page links to the API reference and describes the client packages, including the deprecated legacy `databricks-feature-store`.

note

As of version 0.17.0, `databricks-feature-store` has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering` version 0.2.0 and later. For information about migrating to `databricks-feature-engineering`, see [Migrate to databricks-feature-engineering](#migrate-to-feature-engineering).

## Compatibility matrix[​](#compatibility-matrix "Direct link to Compatibility matrix")

The package and client you should use depend on where your feature tables are located and what Databricks Runtime ML version you are running, as shown in the following table.

To identify the package version that is built in to your Databricks Runtime ML version, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix).

note

*   `databricks-feature-engineering<=0.7.0` is not compatible with `mlflow>=2.18.0`. To use `databricks-feature-engineering` with MLflow 2.18.0 and above, upgrade to `databricks-feature-engineering` version 0.8.0 or above.

## Release notes[​](#release-notes "Direct link to Release notes")

See [Databricks Feature Store and legacy Workspace Feature Store release notes](https://docs.databricks.com/aws/en/release-notes/feature-store/databricks-feature-store).

## Feature Engineering Python API reference[​](#feature-engineering-python-api-reference "Direct link to feature-engineering-python-api-reference")

See the Feature Engineering [Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html).

## Workspace Feature Store Python API reference (deprecated)[​](#workspace-feature-store-python-api-reference-deprecated "Direct link to Workspace Feature Store Python API reference (deprecated)")

note

*   As of version 0.17.0, `databricks-feature-store` has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering` version 0.2.0 and later.

For `databricks-feature-store` v0.17.0, see Databricks `FeatureStoreClient` in [Feature Engineering Python API reference](#feature-engineering-api-reference) for the latest Workspace Feature Store API reference.

For v0.16.3 and below, use the links in the table to download or display the Feature Store Python API reference. To determine the pre-installed version for your Databricks Runtime ML version, see [the compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix).

## Python package[​](#python-package "Direct link to Python package")

This section describes how to install the Python packages to use Databricks Feature Engineering and Databricks Workspace Feature Store.

### Feature Engineering[​](#feature-engineering "Direct link to Feature Engineering")

note

*   As of version 0.2.0, `databricks-feature-engineering` contains modules for working with feature tables in both Unity Catalog and Workspace Feature Store. `databricks-feature-engineering` below version 0.2.0 only works with feature tables in Unity Catalog.

The Databricks Feature Engineering APIs are available through the Python client package `databricks-feature-engineering`. The client is available on [PyPI](https://pypi.org/project/databricks-feature-engineering) and is pre-installed in Databricks Runtime 13.3 LTS ML and above.

For a reference of which client version corresponds to which runtime version, see the [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix).

To install the client in Databricks Runtime:

Python

    %pip install databricks-feature-engineering

To install the client in a local Python environment:

Python

    pip install databricks-feature-engineering

### Workspace Feature Store (deprecated)[​](#workspace-feature-store-deprecated "Direct link to Workspace Feature Store (deprecated)")

note

*   As of version 0.17.0, `databricks-feature-store` has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering`, version 0.2.0 and later.
*   See [Migrate to databricks-feature-engineering](#migrate-to-feature-engineering) for more information.

The Databricks Feature Store APIs are available through the Python client package `databricks-feature-store`. The client is available on [PyPI](https://pypi.org/project/databricks-feature-store) and is pre-installed in Databricks Runtime for Machine Learning. For a reference of which runtime includes which client version, see the [compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix).

To install the client in Databricks Runtime:

Python

    %pip install databricks-feature-store

To install the client in a local Python environment:

Python

    pip install databricks-feature-store

## Migrate to `databricks-feature-engineering`[​](#migrate-to-databricks-feature-engineering "Direct link to migrate-to-databricks-feature-engineering")

To install the `databricks-feature-engineering` package, use `pip install databricks-feature-engineering` instead of `pip install databricks-feature-store`. All of the modules in `databricks-feature-store` have been moved to `databricks-feature-engineering`, so you do not have to change any code. Import statements such as `from databricks.feature_store import FeatureStoreClient` will continue to work after you install `databricks-feature-engineering`.

To work with feature tables in Unity Catalog, use `FeatureEngineeringClient`. To use Workspace Feature Store, you must use `FeatureStoreClient`.

## Supported scenarios[​](#supported-scenarios "Direct link to Supported scenarios")

On Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning, you can:

*   Create, read, and write feature tables.
*   Train and score models on feature data.
*   Publish feature tables to online stores for real-time serving.

From a local environment or an environment external to Databricks, you can:

*   Develop code with local IDE support.
*   Unit test using mock frameworks.
*   Write integration tests to be run on Databricks.

## Limitations[​](#limitations "Direct link to Limitations")

The client library can only be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. It does not support calling Feature Engineering in Unity Catalog or Feature Store APIs from a local environment, or from an environment other than Databricks.

## Use the clients for unit testing[​](#use-the-clients-for-unit-testing "Direct link to Use the clients for unit testing")

You can install the Feature Engineering in Unity Catalog client or the Feature Store client locally to aid in running unit tests.

For example, to validate that a method `update_customer_features` correctly calls `FeatureEngineeringClient.write_table` (or for Workspace Feature Store, `FeatureStoreClient.write_table`), you could write:

Python

    from unittest.mock import MagicMock, patchfrom my_feature_update_module import update_customer_featuresfrom databricks.feature_engineering import FeatureEngineeringClient@patch.object(FeatureEngineeringClient, "write_table")@patch("my_feature_update_module.compute_customer_features")def test_something(compute_customer_features, mock_write_table):  customer_features_df = MagicMock()  compute_customer_features.return_value = customer_features_df  update_customer_features()  # Function being tested  mock_write_table.assert_called_once_with(    name='ml.recommender_system.customer_features',    df=customer_features_df,    mode='merge'  )

## Use the clients for integration testing[​](#use-the-clients-for-integration-testing "Direct link to Use the clients for integration testing")

You can run integration tests with the Feature Engineering in Unity Catalog client or the Feature Store client on Databricks. For details, see [Developer Tools and Guidance: Use CI/CD](https://docs.databricks.com/aws/en/dev-tools/ci-cd/).
