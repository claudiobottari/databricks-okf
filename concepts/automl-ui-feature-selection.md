---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c6714732d3d3a61ffa4e6f9bac4313dc7d1e5c2b14cdb421704ce8d11d635ffc
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-ui-feature-selection
    - AUFS
    - automl-ui-feature-table-selection
    - AUFTS
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML UI Feature Selection
description: The graphical workflow in the Databricks AutoML UI for selecting, configuring, and joining multiple feature tables to an experiment's training dataset.
tags:
  - user-interface
  - automl
  - feature-store
timestamp: "2026-06-18T10:51:03.706Z"
---

# AutoML UI Feature Selection

**AutoML UI Feature Selection** refers to the process of augmenting the original input dataset with features from existing feature tables when configuring an AutoML experiment through the Databricks UI. This allows AutoML experiments to leverage pre-computed features stored in [Unity Catalog](/concepts/unity-catalog.md) feature tables or the legacy [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) without requiring manual data joins.^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

Feature table integration with the AutoML UI is supported under the following runtime conditions:^[automl-feature-store-integration-databricks-on-aws.md]

- Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.

## Selecting a Feature Table Using the AutoML UI

After configuring your AutoML experiment parameters (such as target column, prediction type, and training data), you can join additional feature tables by following these steps:^[automl-feature-store-integration-databricks-on-aws.md]

1. **Click Join features (optional)** — This button appears on the AutoML experiment configuration page after you have set the basic experiment parameters.

2. **Select a feature table** — On the **Join additional features** page, choose a feature table from the **Feature Table** field. Feature tables can reside in [Unity Catalog](/concepts/unity-catalog.md) or the legacy Workspace Feature Store.

3. **Configure lookup keys** — For each **Feature table primary key**, select the corresponding lookup key from your training dataset. The lookup key should be a column that exists in the training dataset you provided for your AutoML experiment. This establishes how the feature table rows map to your training data rows.

4. **Configure timestamp lookup keys (for time series)** — For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), select the corresponding timestamp lookup key. The timestamp lookup key should also be a column in the training dataset you provided for your AutoML experiment. This enables temporal joins for time-based features.

5. **Add more feature tables (optional)** — To incorporate additional feature tables, click **Add another feature table** and repeat the above steps for each table you want to join.

## How Feature Selection Works

When you join feature tables through the AutoML UI, the AutoML experiment automatically performs the following:^[automl-feature-store-integration-databricks-on-aws.md]

- The training dataset is augmented with all columns from the selected feature tables, matched by the configured lookup keys.
- The joined features are included in the AutoML modeling process alongside the original input data columns.
- The feature store integration ensures that features are consistently available for both training and inference.

## Feature Store API Alternative

In addition to the UI, you can achieve the same feature table integration programmatically by setting the `feature_store_lookups` parameter in your AutoML run specification when using the [AutoML API](/concepts/automl-python-api.md). The API approach follows the same lookup key mapping pattern and is functionally equivalent to the UI-based selection.^[automl-feature-store-integration-databricks-on-aws.md]

## Related Concepts

- AutoML — The automated machine learning platform on Databricks
- [Feature Store](/concepts/feature-store.md) — Centralized repository for feature storage and sharing
- [Unity Catalog Feature Tables](/concepts/unity-catalog-feature-tables.md) — Feature tables managed under Unity Catalog governance
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) — Legacy feature store for workspace-level features
- [Time Series Feature Tables](/concepts/time-series-feature-tables.md) — Feature tables designed for temporal data
- [AutoML API](/concepts/automl-python-api.md) — Programmatic interface for configuring and running AutoML experiments

## Sources

- automl-feature-store-integration-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
