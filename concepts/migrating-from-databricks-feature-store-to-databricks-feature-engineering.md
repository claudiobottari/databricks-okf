---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d5b8392eb01c0eb3798e15209ad88a49e8b9f5ffe0452fe29aa853272706694f
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migrating-from-databricks-feature-store-to-databricks-feature-engineering
    - MFDTD
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Migrating from databricks-feature-store to databricks-feature-engineering
description: The migration path from the deprecated legacy package to the new unified package, requiring only a pip install change without code modifications.
tags:
  - databricks
  - migration
  - feature-engineering
timestamp: "2026-06-19T18:47:31.700Z"
---

# Migrating from `databricks-feature-store` to `databricks-feature-engineering`

The `databricks-feature-store` Python package, which provides the [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) API, has been deprecated as of version 0.17.0. All its modules have been moved into the new `databricks-feature-engineering` package, starting from version 0.2.0. This page guides you through the migration process. ^[feature-engineering-python-api-databricks-on-aws.md]

## Key Changes

- **Package name**: `databricks-feature-store` → `databricks-feature-engineering`.
- **No code changes needed**: Existing import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work after installing the new package. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Client distinction**:
  - To work with feature tables in [Unity Catalog](/concepts/unity-catalog.md), use `FeatureEngineeringClient` (available only in `databricks-feature-engineering`).
  - To continue using the deprecated Workspace Feature Store, use `FeatureStoreClient` (kept as an alias in the new package). ^[feature-engineering-python-api-databricks-on-aws.md]

## Migration Steps

1. **Uninstall the old package** (optional, but recommended to avoid confusion):
   ```bash
   %pip uninstall databricks-feature-store -y
   ```

2. **Install the new package**:
   ```bash
   %pip install databricks-feature-engineering
   ```
   For local Python environments, use the same `pip install` command. ^[feature-engineering-python-api-databricks-on-aws.md]

3. **Update import statements** (not strictly required, but recommended for clarity): change `from databricks.feature_store import ...` to `from databricks.feature_engineering import ...` where you are ready to adopt the new API. The `FeatureStoreClient` class remains available under `databricks.feature_engineering` for backward compatibility. ^[feature-engineering-python-api-databricks-on-aws.md]

4. **If using Unity Catalog**, switch to `FeatureEngineeringClient`:
   ```python
   from databricks.feature_engineering import FeatureEngineeringClient
   fe = FeatureEngineeringClient()
   fe.write_table(...)
   ```

## Compatibility Notes

- `databricks-feature-engineering` is pre-installed in Databricks Runtime 13.3 LTS ML and above. For earlier runtimes, install it via `%pip`. ^[feature-engineering-python-api-databricks-on-aws.md]
- **Version compatibility with MLflow**: `databricks-feature-engineering <= 0.7.0` is **not** compatible with `mlflow >= 2.18.0`. If you use MLflow 2.18.0 or later, upgrade to `databricks-feature-engineering` version 0.8.0 or higher. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [Feature Engineering](/concepts/featureengineeringclient-api.md) – The new package for both Unity Catalog and Workspace Feature Store.
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) – The deprecated legacy feature store.
- [Unity Catalog](/concepts/unity-catalog.md) – The recommended catalog for organizing feature tables.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime that includes the feature engineering packages.
- [MLflow](/concepts/mlflow.md) – Model lifecycle management; requires compatible feature engineering version.
- Python API – General reference for Databricks Python clients.

## Sources

- feature-engineering-python-api-databricks-on-aws.md

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
