---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e7e60a04b36e3bd1681e238243d236fdda39c9feb0389b44ab49341ecc75791d
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - legacy-workspace-feature-store
    - LWFS
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Legacy Workspace Feature Store
description: The older feature store system in Databricks, separate from Unity Catalog, still supported for AutoML integration.
tags:
  - feature-store
  - legacy
  - databricks
timestamp: "2026-06-19T14:06:58.907Z"
---

---

title: Legacy Workspace Feature Store
summary: The older workspace-level feature store that AutoML can still use as a source of feature tables alongside Unity Catalog feature tables.
sources:
  - automl-feature-store-integration-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:30:22.250Z"
updatedAt: "2026-06-18T14:30:22.250Z"
tags:
  - machine-learning
  - feature-store
  - legacy
aliases:
  - legacy-workspace-feature-store
  - LWFS
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# Legacy Workspace Feature Store

The **Legacy Workspace Feature Store** is a feature store for machine learning that stores features within a single Databricks workspace. It is an older version of the feature store, distinct from the newer [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md). Workspace-scoped feature tables can be used with AutoML to augment the original input dataset during experiment configuration. ^[automl-feature-store-integration-databricks-on-aws.md]

## Overview

The Legacy Workspace Feature Store allows you to store, discover, and share machine learning features. Unlike feature tables in Unity Catalog, which are managed at the catalog level and can be shared across workspaces, the Legacy Workspace Feature Store operates only within the workspace where the feature tables were created. Databricks recommends migrating existing feature tables to Unity Catalog for new projects. ^[automl-feature-store-integration-databricks-on-aws.md]

## Usage with AutoML

When configuring an AutoML experiment, you can optionally join features from the Legacy Workspace Feature Store to your training dataset. This integration is supported for classification and regression experiments starting from Databricks Runtime 11.3 LTS ML, and for forecasting experiments starting from Databricks Runtime 12.2 LTS ML. ^[automl-feature-store-integration-databricks-on-aws.md]

### Selecting Feature Tables in the UI

To use feature tables from the Legacy Workspace Feature Store in an AutoML experiment via the UI:

1. After configuring your AutoML experiment, click **Join features (optional)**. ^[automl-feature-store-integration-databricks-on-aws.md]
2. On the **Join additional features** page, select a feature table from the Legacy Workspace Feature Store in the **Feature Table** field. ^[automl-feature-store-integration-databricks-on-aws.md]
3. For each **Feature table primary key**, select the corresponding lookup key from your training dataset. ^[automl-feature-store-integration-databricks-on-aws.md]
4. For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), select the corresponding timestamp lookup key from your training dataset. ^[automl-feature-store-integration-databricks-on-aws.md]
5. To join additional feature tables, click **Add another feature table** and repeat the steps. ^[automl-feature-store-integration-databricks-on-aws.md]

### Using the API

With the AutoML API, set the `feature_store_lookups` parameter in your AutoML run specification. Each entry specifies the `table_name`, `lookup_key`, and optionally a `timestamp_lookup_key` for time series tables. ^[automl-feature-store-integration-databricks-on-aws.md]

```python
feature_store_lookups = [
    {
        "table_name": "example.trip_pickup_features",
        "lookup_key": ["pickup_zip", "rounded_pickup_datetime"],
    },
    {
        "table_name": "example.trip_dropoff_features",
        "lookup_key": ["dropoff_zip", "rounded_dropoff_datetime"],
    }
]
```
^[automl-feature-store-integration-databricks-on-aws.md]

## Migration and Deprecation

The Legacy Workspace Feature Store is being superseded by feature tables in Unity Catalog. Databricks recommends using feature tables in Unity Catalog for new projects and migrating existing feature tables from the Legacy Workspace Feature Store to Unity Catalog to take advantage of cross-workspace governance and discoverability. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- [Feature Tables in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — The current recommended feature store solution
- AutoML — Automated machine learning that can integrate with feature stores
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables with temporal data that require timestamp lookups
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and cataloging system for modern feature stores

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
