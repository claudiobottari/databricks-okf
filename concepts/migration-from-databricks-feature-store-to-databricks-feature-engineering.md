---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4fbf90245b684609add00a862f5fa4136b8817b2164b0368620e8f17dd53cf9
  pageDirectory: concepts
  sources:
    - feature-engineering-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - migration-from-databricks-feature-store-to-databricks-feature-engineering
    - MFDTD
  citations:
    - file: feature-engineering-python-api-databricks-on-aws.md
title: Migration from databricks-feature-store to databricks-feature-engineering
description: The process and compatibility notes for migrating from the deprecated databricks-feature-store package to the new databricks-feature-engineering package, with backward compatibility for import statements.
tags:
  - databricks
  - migration
  - feature-engineering
  - upgrade
timestamp: "2026-06-19T10:29:18.291Z"
---

```yaml
---
title: Migration from databricks-feature-store to databricks-feature-engineering
summary: Process for migrating code from the legacy Feature Store package to the newer Feature Engineering package with minimal code changes
sources:
  - feature-engineering-python-api-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:18:23.601Z"
updatedAt: "2026-06-18T12:18:23.601Z"
tags:
  - databricks
  - migration
  - feature-engineering
  - feature-store
aliases:
  - migration-from-databricks-feature-store-to-databricks-feature-engineering
  - MFDTD
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Migration from `databricks-feature-store` to `databricks-feature-engineering`

The `databricks-feature-engineering` Python package is the replacement for the deprecated `databricks-feature-store` package. Version 0.17.0 of `databricks-feature-store` is the final release; all modules from that package have been moved into `databricks-feature-engineering` version 0.2.0 and later. ^[feature-engineering-python-api-databricks-on-aws.md]

## Migrating your Code

1. **Install the new package** – Replace `pip install databricks-feature-store` with `pip install databricks-feature-engineering`. The new package is available on [PyPI](https://pypi.org/project/databricks-feature-engineering) and is pre-installed in Databricks Runtime 13.3 LTS ML and above. ^[feature-engineering-python-api-databricks-on-aws.md]

2. **Keep existing imports** – No code changes are required. Import statements such as `from databricks.feature_store import FeatureStoreClient` continue to work unchanged after installing `databricks-feature-engineering`. ^[feature-engineering-python-api-databricks-on-aws.md]

3. **Choose the right client for your use case** – To work with [[Feature Engineering in Unity Catalog]] (feature tables stored in Unity Catalog), use `FeatureEngineeringClient`. To continue using [[Workspace Feature Store UI|Workspace Feature Store]] (the legacy workspace-level feature store), you must use `FeatureStoreClient`. Both clients are available in the same package. ^[feature-engineering-python-api-databricks-on-aws.md]

## Compatibility Considerations

| Component | Required Version | Notes |
|-----------|------------------|-------|
| `databricks-feature-engineering` | ≥ 0.2.0 | Contains all modules previously in `databricks-feature-store`. |
| `databricks-feature-engineering` | ≥ 0.8.0 | Required when using `mlflow` ≥ 2.18.0. Versions ≤ 0.7.0 are incompatible with MLflow 2.18.0+. ^[feature-engineering-python-api-databricks-on-aws.md] |
| Databricks Runtime ML | 13.3 LTS ML or above | Pre-installs `databricks-feature-engineering`. |

For a full compatibility matrix mapping Databricks Runtime ML versions to package versions, see the [Feature Engineering compatibility matrix](https://docs.databricks.com/aws/en/release-notes/runtime/#feature-engineering-compatibility-matrix). ^[feature-engineering-python-api-databricks-on-aws.md]

## Limitations

The `databricks-feature-engineering` client can only be run on Databricks (including Databricks Runtime and Databricks Runtime for Machine Learning). It does not support calling Feature Engineering or Feature Store APIs from a local or external environment. However, you can install the package locally to support unit testing with mock frameworks. ^[feature-engineering-python-api-databricks-on-aws.md]

## API Reference

See the [Feature Engineering Python API reference](https://api-docs.databricks.com/python/feature-engineering/latest/index.html) for full documentation of `FeatureEngineeringClient` and related classes. ^[feature-engineering-python-api-databricks-on-aws.md]

## Related Concepts

- [[Feature Engineering in Unity Catalog]]
- [[Workspace Feature Store UI|Workspace Feature Store]]
- Feature Store Client
- [[FeatureEngineeringClient API|FeatureEngineeringClient]]
- [[Databricks Runtime Compatibility|Databricks Runtime ML Compatibility Matrix]]

## Sources

- feature-engineering-python-api-databricks-on-aws.md
```

# Citations

1. [feature-engineering-python-api-databricks-on-aws.md](/references/feature-engineering-python-api-databricks-on-aws-78d13678.md)
