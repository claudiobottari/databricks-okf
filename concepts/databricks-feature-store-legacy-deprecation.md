---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94bcf687bd9ef3f5322950ac2d7b30dd27c5aa81d136ad00d41f52af24ed8b77
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-feature-store-legacy-deprecation
    - D(D
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: databricks-feature-store (legacy) deprecation
description: The legacy databricks-feature-store package is deprecated as of version 0.17.0 in favor of databricks-feature-engineering
tags:
  - databricks
  - deprecation
  - feature-store
  - migration
timestamp: "2026-06-18T12:18:11.271Z"
---

---
title: databricks-feature-store (legacy) deprecation
summary: The `databricks-feature-store` Python package, used for the legacy Workspace Feature Store, is deprecated as of version 0.17.0. All functionality has been moved to the `databricks-feature-engineering` package.
sources:
  - feature-engineering-python-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - databricks
  - feature-store
  - deprecation
  - migration
  - python
aliases:
  - legacy-workspace-feature-store-deprecation
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# databricks-feature-store (legacy) deprecation

The `databricks-feature-store` Python package provided the client API for the legacy **Workspace Feature Store** (also known as the feature store before Unity Catalog integration). As of version 0.17.0, this package is officially deprecated. All its modules have been moved into the new [`databricks-feature-engineering`](databricks-feature-engineering) package, starting from version 0.2.0. Users are encouraged to migrate to `databricks-feature-engineering` to continue receiving updates and to support feature tables in [Unity Catalog](/concepts/unity-catalog.md). ^[feature-engineering-python-api-databricks-on-aws.md]

## Deprecation details

The deprecation means that no new features or bug fixes will be released for `databricks-feature-store` beyond version 0.17.0. The package remains available on PyPI and continues to be pre-installed in [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) for compatibility with existing workflows, but all future development effort has shifted to `databricks-feature-engineering`. ^[feature-engineering-python-api-databricks-on-aws.md]

## Migration path

To migrate, replace the installed package from `databricks-feature-store` to `databricks-feature-engineering`. No code changes are required because all module names, classes, and import paths are preserved. For example, the import `from databricks.feature_store import FeatureStoreClient` continues to work after installing `databricks-feature-engineering`. ^[feature-engineering-python-api-databricks-on-aws.md]

The key differences are:
- **[FeatureEngineeringClient](/concepts/featureengineeringclient-api.md)** — the new client for working with feature tables in Unity Catalog.
- **[FeatureStoreClient](/concepts/feature-store.md)** — the existing client for the legacy Workspace Feature Store. It is still available in the `databricks-feature-engineering` package for backward compatibility.

If you currently use `FeatureStoreClient` for the Workspace Feature Store, you can continue to do so after migration. If you want to take advantage of Unity Catalog features, switch to `FeatureEngineeringClient`. ^[feature-engineering-python-api-databricks-on-aws.md]

## Compatibility and version notes

The following compatibility considerations apply when using `databricks-feature-engineering`:

- `databricks-feature-engineering` version 0.7.0 and earlier is not compatible with `mlflow` 2.18.0 and above. To use the package with MLflow 2.18.0+, upgrade to `databricks-feature-engineering` version 0.8.0 or later. ^[feature-engineering-python-api-databricks-on-aws.md]
- The package is pre-installed in Databricks Runtime 13.3 LTS ML and later. The legacy `databricks-feature-store` is pre-installed in older Databricks Runtime for Machine Learning versions. For a detailed compatibility matrix between runtime versions and client versions, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]
- `databricks-feature-engineering` versions below 0.2.0 only work with feature tables in Unity Catalog, not with the Workspace Feature Store. Version 0.2.0 and later support both. ^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

The client library (both legacy and new) can only be run on Databricks, including Databricks Runtime and Databricks Runtime for Machine Learning. It does not support calling Feature Engineering or Feature Store APIs from a local environment or from any environment other than Databricks. However, you can install the library locally for unit testing with mock frameworks. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related concepts

- [databricks-feature-engineering](/concepts/databricks-feature-engineering-client.md) — The successor package that provides all legacy Feature Store functionality
- [FeatureEngineeringClient](/concepts/featureengineeringclient-api.md) — New client for Unity Catalog feature tables
- [FeatureStoreClient](/concepts/feature-store.md) — Legacy client for Workspace Feature Store (still supported in new package)
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — The deprecated feature store that `databricks-feature-store` originally served
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) — The modern feature store solution
- MLflow integration with Feature Store — How feature tables are used in ML workflows

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
