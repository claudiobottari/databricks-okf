---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db443cde9734c58e204d8ebaf5d1ed4ad3632d770227b584f746e9be9ea22182
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - runtime-requirements-for-feature-store-automl
    - RRFFSA
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: Runtime Requirements for Feature Store AutoML
description: Classification and regression experiments with feature store require Databricks Runtime 11.3 LTS ML+, forecasting requires 12.2 LTS ML+.
tags:
  - automl
  - requirements
  - databricks-runtime
timestamp: "2026-06-19T09:06:45.959Z"
---

# Runtime Requirements for Feature Store AutoML

**Runtime Requirements for Feature Store AutoML** specifies the minimum Databricks Runtime versions needed to use AutoML with feature tables from [Unity Catalog](/concepts/unity-catalog.md) or the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md).

## Requirements

The required runtime version depends on the type of AutoML experiment being run:

- **Classification and regression experiments** require Databricks Runtime 11.3 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]
- **Forecasting experiments** require Databricks Runtime 12.2 LTS ML and above. ^[automl-feature-store-integration-databricks-on-aws.md]

These requirements apply regardless of whether the feature tables are stored in Unity Catalog or in the legacy Workspace Feature Store.

## Background

AutoML can augment the original input dataset with features from [Feature Tables](/concepts/feature-table.md) in Unity Catalog or in the legacy Workspace Feature Store. ^[automl-feature-store-integration-databricks-on-aws.md] The runtime version constraints ensure that the necessary ML feature store integration libraries and capabilities are available.

## Related Concepts

- [AutoML Feature Store Integration](/concepts/automl-feature-store-integration.md) — How to select and join feature tables in AutoML experiments.
- [Feature Store](/concepts/feature-store.md) — The feature management system for machine learning.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) — Pre-built runtime with ML libraries.
- [Classification and Regression AutoML](/concepts/xgboost-classification-and-regression-on-databricks.md) — AutoML experiment types for supervised learning.
- Forecasting AutoML — AutoML experiment type for time series forecasting.

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
