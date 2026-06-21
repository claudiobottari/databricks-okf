---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7b5fa7281d5c1dbd24d11acb35e56d23bfae30d7bf1e1c6e43cd13432c55e94
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feature-engineering-compatibility-matrix
    - FECM
    - Compatibility Matrix
    - databricks-feature-engineering-compatibility-matrix
    - DFECM
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Feature Engineering Compatibility Matrix
description: A reference mapping Databricks Runtime ML versions to the corresponding pre-installed versions of databricks-feature-engineering and databricks-feature-store packages.
tags:
  - databricks
  - compatibility
  - runtime
  - versioning
timestamp: "2026-06-19T10:29:13.995Z"
---

# Feature Engineering Compatibility Matrix

The **Feature Engineering Compatibility Matrix** is a reference table that maps Databricks Runtime ML versions to the corresponding pre-installed versions of the `databricks-feature-engineering` and `databricks-feature-store` Python packages. This matrix helps users determine which client package and version to use for their environment when working with [Feature Engineering (Unity Catalog)](/concepts/feature-engineering-in-unity-catalog.md) or the [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). ^[feature-engineering-python-api-databricks-on-aws.md]

## Purpose

The correct package and client depend on two factors: where the feature tables are located (Unity Catalog or Workspace Feature Store) and which Databricks Runtime ML version is being run. The compatibility matrix provides a quick lookup to identify the built-in package version for a given runtime version, ensuring that feature engineering APIs are used with the appropriate dependencies. ^[feature-engineering-python-api-databricks-on-aws.md]

## How to Use the Matrix

1. Identify the Databricks Runtime ML version you are using (e.g., 14.3 LTS ML, 15.0 ML).
2. Locate that version in the compatibility matrix table, published in the Databricks release notes under the "Feature Engineering compatibility matrix" section.
3. Read the corresponding package versions for:
   - `databricks-feature-engineering` (for Unity Catalog feature tables)
   - `databricks-feature-store` (deprecated, for Workspace Feature Store)
4. Use that information to ensure your code imports and installed packages are aligned.

The matrix also serves as a guide for manual installs: when running `%pip install databricks-feature-engineering` in a notebook or cluster, the matrix confirms which version is natively bundled with the runtime, helping to avoid version conflicts. ^[feature-engineering-python-api-databricks-on-aws.md]

## Important Notes

- As of version 0.17.0, `databricks-feature-store` is deprecated, and all its modules are available in `databricks-feature-engineering` version 0.2.0 and later. ^[feature-engineering-python-api-databricks-on-aws.md]
- `databricks-feature-engineering` version 0.2.0 and above works with both Unity Catalog and Workspace Feature Store; versions below 0.2.0 work only with Unity Catalog. ^[feature-engineering-python-api-databricks-on-aws.md]
- `databricks-feature-engineering <= 0.7.0` is not compatible with `mlflow >= 2.18.0`. When using MLflow 2.18.0 or above, upgrade to `databricks-feature-engineering` version 0.8.0 or higher. ^[feature-engineering-python-api-databricks-on-aws.md]

## Location of the Matrix

The actual matrix table is hosted in the Databricks documentation under the release notes runtime section:  
[Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix).

## Related Concepts

- [Feature Engineering Python API](/concepts/featureengineeringclient-python-api.md) – The client packages and their usage.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – The runtime that bundles these packages.
- [Feature Engineering (Unity Catalog)](/concepts/feature-engineering-in-unity-catalog.md) – Working with feature tables in Unity Catalog.
- [Workspace Feature Store (Deprecated)](/concepts/workspace-feature-store-deprecated.md) – Legacy feature store approach.
- Migrate to databricks-feature-engineering – Guidance for moving from the deprecated package.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
