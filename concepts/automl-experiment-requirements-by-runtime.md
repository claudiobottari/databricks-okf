---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ec2c715bdb57659b3a808d815ab7a1c06b86839399ea4c6c6f00343425457efc
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-requirements-by-runtime
    - AERBR
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML Experiment Requirements by Runtime
description: Classification and regression AutoML experiments with feature store integration require Databricks Runtime 11.3 LTS ML+, while forecasting experiments require 12.2 LTS ML+.
tags:
  - machine-learning
  - automl
  - databricks
  - requirements
timestamp: "2026-06-19T17:38:28.550Z"
---

# AutoML Experiment Requirements by Runtime

**AutoML Experiment Requirements by Runtime** defines the minimum [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) version needed to run AutoML experiments with Feature Store integration, depending on the experiment type.

## Requirements

The required runtime version depends on the type of AutoML experiment being conducted:

- **Classification and regression experiments** require Databricks Runtime 11.3 LTS ML and above.
- **Forecasting experiments** require Databricks Runtime 12.2 LTS ML and above.

^[automl-feature-store-integration-databricks-on-aws.md]

## Implications

These requirements apply when augmenting the original input dataset with features from feature tables in [Unity Catalog](/concepts/unity-catalog.md) or the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md). If you attempt to run a forecasting experiment with feature store integration on Databricks Runtime 11.3 LTS ML, the experiment will not succeed because the required runtime is 12.2 LTS ML or higher. ^[automl-feature-store-integration-databricks-on-aws.md]

## Feature Table Selection

Separately from runtime requirements, when configuring an AutoML experiment with feature tables:
- You must select corresponding lookup keys (columns in the training dataset) for each feature table primary key.
- For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), you must select a corresponding timestamp lookup key. ^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- AutoML – Overview of automated machine learning on Databricks
- [Feature Store](/concepts/feature-store.md) – Centralized feature management
- [Unity Catalog](/concepts/unity-catalog.md) – Unified governance for data and AI assets
- Classification and Regression Experiments – AutoML experiment types affected by runtime requirements
- [Forecasting Experiments](/concepts/automl-forecasting-experiment-stages.md) – AutoML experiment type with higher runtime requirement
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – Pre-configured ML environments

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
