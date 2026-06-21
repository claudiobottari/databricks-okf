---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6d73fdae372aa883eae9a4d2d97704ca199b2974cc3a55131f2ef02a4008de2
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-engineering-compatibility-matrix
    - DFECM
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Databricks Feature Engineering Compatibility Matrix
description: A reference mapping package versions (databricks-feature-engineering and databricks-feature-store) to Databricks Runtime ML versions.
tags:
  - databricks
  - compatibility
  - versioning
timestamp: "2026-06-19T18:47:36.299Z"
---

# Databricks Feature Engineering Compatibility Matrix

The **Databricks Feature Engineering Compatibility Matrix** maps the appropriate Python client package and version to use based on where your feature tables are located and which [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) version you are running. It helps determine whether to use `databricks-feature-engineering` or the legacy `databricks-feature-store` package. ^[feature-engineering-python-api-databricks-on-aws.md]

## Overview

The compatibility matrix defines the relationship between Databricks Runtime ML versions and the built-in Feature Engineering client package versions. It also clarifies which client to use depending on whether your feature tables reside in [Unity Catalog](/concepts/unity-catalog.md) or the older [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). ^[feature-engineering-python-api-databricks-on-aws.md]

## Package Selection by Location

- **Unity Catalog feature tables**: Use the `databricks-feature-engineering` package with `FeatureEngineeringClient`. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Workspace Feature Store tables**: Use the `databricks-feature-store` package with `FeatureStoreClient`. ^[feature-engineering-python-api-databricks-on-aws.md]

As of `databricks-feature-engineering` version 0.2.0 and later, the package contains modules for working with feature tables in both Unity Catalog and Workspace Feature Store. Versions below 0.2.0 only work with Unity Catalog feature tables. ^[feature-engineering-python-api-databricks-on-aws.md]

## Deprecation and Migration

As of version 0.17.0, `databricks-feature-store` has been deprecated. All existing modules from this package are now available in `databricks-feature-engineering` version 0.2.0 and later. Import statements such as `from databricks.feature_store import FeatureStoreClient` will continue to work after installing `databricks-feature-engineering`; no code changes are required. ^[feature-engineering-python-api-databricks-on-aws.md]

## Runtime Pre-Installation

`databricks-feature-engineering` is pre-installed in Databricks Runtime 13.3 LTS ML and above. To identify the specific package version built into your Databricks Runtime ML version, consult the [Feature Engineering Compatibility Matrix](/concepts/feature-engineering-compatibility-matrix.md) in the Databricks release notes. ^[feature-engineering-python-api-databricks-on-aws.md]

## Important Compatibility Notes

| Constraint | Requirement |
|---|---|
| `databricks-feature-engineering <= 0.7.0` with `mlflow >= 2.18.0` | Upgrade to `databricks-feature-engineering` version 0.8.0 or above |
| `databricks-feature-engineering < 0.2.0` | Only works with Unity Catalog feature tables, not Workspace Feature Store |

^[feature-engineering-python-api-databricks-on-aws.md]

## Installing the Packages

To install the appropriate package in a Databricks notebook or local environment:

- **Feature Engineering (Unity Catalog)**: `pip install databricks-feature-engineering` ^[feature-engineering-python-api-databricks-on-aws.md]
- **Workspace Feature Store (deprecated legacy)**: `pip install databricks-feature-store` ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-client.md) – The full API reference for `databricks-feature-engineering`
- Workspace Feature Store Python API – Deprecated API reference for `databricks-feature-store`
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) for managing feature tables in the modern architecture
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime version that determines which client is pre-installed
- Feature Store and Feature Engineering release notes – Version-specific compatibility details

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
