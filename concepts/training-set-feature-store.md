---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cb7b5646052aa82ca23c20d702738dc92f430180a0bf24847cd8f61879502dd1
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - training-set-feature-store
    - TS(S
    - Model Training with Features
    - Training Set
    - Training Set Creation
    - TrainingSet
    - training set
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
title: Training Set (Feature Store)
description: A dataset composed of a list of features and a DataFrame containing raw training data, labels, and primary keys used to look up features during model training.
tags:
  - machine-learning
  - feature-store
  - model-training
timestamp: "2026-06-19T09:51:14.174Z"
---

# Training Set (Feature Store)

A **training set** in a [Feature Store](/concepts/feature-store.md) is a structured dataset that combines raw training data (labels and primary keys) with features retrieved from feature tables. It serves as the input to model training, ensuring that the same feature definitions and computations used during training are available for inference. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Composition

A training set consists of three components:

- A **DataFrame** containing raw training data, ground-truth labels, and primary key columns.
- One or more **[FeatureLookup](/concepts/featurelookup.md)** objects that specify which features to extract from [Feature Tables](/concepts/feature-table.md) and the join keys to use.
- Optionally, **[FeatureFunction](/concepts/featurefunction.md)** objects that compute features on-demand from real-time inputs.

The raw training data must include columns that correspond to the primary keys of the feature tables. The system joins the feature table values onto the input DataFrame using these keys. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Creation

You create a training set by calling `create_training_set` (the API name varies by Feature Store version). This method accepts:

- The raw-label DataFrame.
- The list of `FeatureLookup` and `FeatureFunction` definitions.
- The label column name.

The result is a training dataset ready for model training. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Role in the ML Workflow

After creating the training set, you train a model and log it using the Feature Store client’s `log_model()` method. The logged model retains references to the features used. At inference time, the model can retrieve feature values automatically from the offline store (for batch) or online store (for real-time). ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

When using [Unity Catalog](/concepts/unity-catalog.md), lineage is automatically tracked: the tables and functions that contributed to the training set are recorded and visible in Catalog Explorer. This provides governance and reproducibility. ^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Related Concepts

- [Feature Store](/concepts/feature-store.md)
- [Feature Table](/concepts/feature-table.md)
- [FeatureLookup](/concepts/featurelookup.md)
- [FeatureFunction](/concepts/featurefunction.md)
- [FeatureSpec](/concepts/featurespec.md)
- [Offline Store](/concepts/offline-feature-store.md)
- [Online Feature Store](/concepts/online-feature-store.md)
- [Model Training](/concepts/databricks-model-training.md)
- [Model Packaging](/concepts/model-packaging.md)
- [Lineage](/concepts/data-lineage.md)

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
