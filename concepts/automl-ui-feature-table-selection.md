---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 082847727d80db58745216f62a034ff9799d06143f522b474732124cd2b30857
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-ui-feature-table-selection
    - AUFTS
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
title: AutoML UI Feature Table Selection
description: The workflow in the Databricks AutoML UI for selecting and joining feature tables to an experiment through the 'Join features' option
tags:
  - automl
  - ui
  - feature-store
  - databricks
timestamp: "2026-06-19T22:12:00.538Z"
---

```markdown
---
title: AutoML UI Feature Table Selection
summary: Step-by-step workflow in the AutoML UI for joining feature tables to training datasets via the "Join features (optional)" button.
sources:
  - automl-feature-store-integration-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:30:26.687Z"
updatedAt: "2026-06-19T14:06:37.382Z"
tags:
  - automl
  - ui
  - feature-store
aliases:
  - automl-ui-feature-table-selection
  - AUFTS
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# AutoML UI Feature Table Selection

**AutoML UI Feature Table Selection** is the process of augmenting the original input dataset of an AutoML experiment with features from existing feature tables directly through the Databricks UI. This integration uses features stored in [[Unity Catalog]] feature tables or the legacy [[Workspace Feature Store UI|Workspace Feature Store]], allowing reuse of curated features across experiments. ^[automl-feature-store-integration-databricks-on-aws.md]

## Requirements

- Classification and regression experiments require Databricks Runtime 11.3 LTS ML and above.
- Forecasting experiments require Databricks Runtime 12.2 LTS ML and above.

^[automl-feature-store-integration-databricks-on-aws.md]

## Select a Feature Table Using the AutoML UI

After configuring your AutoML experiment with a training dataset, follow these steps:

1. **Open the feature table selector.**  
   Click **Join features (optional)** on the experiment configuration page. This button appears below the primary dataset settings. ^[automl-feature-store-integration-databricks-on-aws.md]

2. **Choose a feature table.**  
   On the **Join additional features** page, select a feature table from the **Feature Table** field. The table must exist in Unity Catalog or the legacy Workspace Feature Store. ^[automl-feature-store-integration-databricks-on-aws.md]

3. **Map primary keys to lookup keys.**  
   For each **Feature table primary key**, select the corresponding lookup key. The lookup key must be a column in the training dataset you provided for your AutoML experiment. This mapping tells AutoML how to join the feature table to your data. ^[automl-feature-store-integration-databricks-on-aws.md]

4. **(For time series feature tables) Map timestamp keys.**  
   If the selected feature table is a [[Time Series Feature Tables|time series feature table]], also select the corresponding timestamp lookup key. Like the lookup key, the timestamp lookup key must be a column in your training dataset. ^[automl-feature-store-integration-databricks-on-aws.md]

5. **Add more feature tables (optional).**  
   To include additional feature tables, click **Add another feature table** and repeat the key mapping steps for each table. ^[automl-feature-store-integration-databricks-on-aws.md]

## Use Feature Tables with the AutoML API

As an alternative to the UI, you can specify feature table lookups programmatically using the [[AutoML Python API|AutoML API]]. Set the `feature_store_lookups` parameter in your AutoML run specification. The following example shows a list of lookup dictionaries: ^[automl-feature-store-integration-databricks-on-aws.md]

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

## Related Concepts

- AutoML – Automated machine learning experiment framework
- [[Feature Store]] – Central repository for curated features
- [[Unity Catalog]] – Data governance catalog for feature tables
- [[Workspace Feature Store UI|Workspace Feature Store]] – Legacy feature store in the workspace
- [[Time Series Feature Tables]] – Feature tables that include a timestamp dimension
- [[AutoML Python API|AutoML API]] – Programmatic interface for AutoML experiments
- [[FeatureEngineeringClient API|Feature Engineering]] – Creating features from raw data

## Sources

- automl-feature-store-integration-databricks-on-aws.md
```

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
