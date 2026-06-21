---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1860b81774011d20f9d9c242528ebd2cb55fa52c480750d19a0d9fa080a92d41
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - limitations-of-databricks-feature-engineering-client
    - LODFEC
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Limitations of Databricks Feature Engineering Client
description: The client library can only run on Databricks (Databricks Runtime or Databricks Runtime ML) and does not support calling Feature Engineering APIs from external/local environments.
tags:
  - databricks
  - limitations
  - feature-engineering
timestamp: "2026-06-19T18:47:46.751Z"
---

# Limitations of Databricks Feature Engineering Client

The **Limitations of Databricks Feature Engineering Client** describe the environments in which the `databricks-feature-engineering` Python package can be used to call Feature Engineering or Feature Store APIs. Understanding these constraints is important when planning development, testing, and production deployment workflows.

## Overview

The `databricks-feature-engineering` client library (and its deprecated predecessor `databricks-feature-store`) is designed to run only inside a Databricks environment, specifically Databricks Runtime and [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md). It does not support making API calls from a local environment or any environment outside of Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Limitation Details

The core limitation is:

- The client library **cannot** call Feature Engineering in [Unity Catalog](/concepts/unity-catalog.md) or Feature Store APIs from a local environment, or from any environment other than Databricks. ^[feature-engineering-python-api-databricks-on-aws.md]
- The library must be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. ^[feature-engineering-python-api-databricks-on-aws.md]

## Impact on Development Workflows

Because API calls cannot be made locally, developers cannot directly create, read, write, train, or score feature tables from their local IDE or CI/CD pipeline. This restriction affects:

- Local prototyping of feature engineering logic
- Running integration tests that interact with feature tables outside Databricks
- Offline model training that requires fetching feature data from a Unity Catalog feature table

## Workarounds

Despite the API call restriction, the client is still useful for local development and testing:

- **Unit testing**: The client can be installed locally (via `pip install databricks-feature-engineering`) to enable mocking of `FeatureEngineeringClient` methods such as `write_table`. This allows validation of function logic without making real API calls. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Integration testing**: Integration tests that exercise the actual Feature Engineering APIs must be run on a Databricks cluster. The recommended practice is to write tests locally and then execute them on Databricks as part of a CI/CD pipeline. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) – Full API reference for the client library
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) – Primary client for Unity Catalog feature tables
- [FeatureStoreClient](/concepts/feature-store.md) – Deprecated client for workspace-level feature store
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-installed environment that includes the client
- [Feature Store](/concepts/feature-store.md) – Legacy feature store concept
- [Unity Catalog](/concepts/unity-catalog.md) – Catalog system for managing feature tables
- Unit Testing with Feature Engineering – Best practices for mocking the client

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
