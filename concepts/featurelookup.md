---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 487b1cea656b1b12cd6127936957df3553571755f7f37b6447dd009c501d831c
  pageDirectory: concepts
  sources:
    - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - feature-governance-and-lineage-databricks-on-aws.md
    - feature-serving-endpoints-databricks-on-aws.md
    - train-models-with-feature-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - featurelookup
    - Feature Lookups
    - FeatureLookup API
    - FeatureLookups
    - feature lookups
    - Look up features|Look up features
    - Online Feature Lookup
    - feature lookup DataFrame
  citations:
    - file: databricks-feature-store-overview-and-glossary-databricks-on-aws.md
    - file: train-models-with-feature-tables-databricks-on-aws.md
    - file: feature-serving-endpoints-databricks-on-aws.md
title: FeatureLookup
description: A construct that specifies which features to select from a feature table and defines the join keys used to link feature tables with label data during training set creation.
tags:
  - feature-store
  - api
  - machine-learning
timestamp: "2026-06-19T18:12:14.231Z"
---

```markdown
---
title: FeatureLookup
summary: A mechanism that specifies which features to select from a feature table and defines the join keys used to combine feature tables with label data for creating training datasets.
sources:
  - databricks-feature-store-overview-and-glossary-databricks-on-aws.md
  - feature-serving-endpoints-databricks-on-aws.md
  - train-models-with-feature-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:38:30.510Z"
updatedAt: "2026-06-19T14:49:38.675Z"
tags:
  - feature-engineering
  - machine-learning
  - databricks
aliases:
  - featurelookup
confidence: 0.95
provenanceState: merged
inferredParagraphs: 0
---

# FeatureLookup

**FeatureLookup** is a core construct in [[Databricks Feature Store]] that specifies which features to select from a feature table and defines the keys used to join that table with label data when creating a training dataset. It is the primary mechanism for declaring which columns from which feature tables a machine learning model requires for training and inference.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Overview

When training a model, you typically need only a subset of columns from each feature table. A `FeatureLookup` object declares exactly which features to use from a given feature table and the lookup keys that map the feature table’s primary keys to columns in your training DataFrame.^[train-models-with-feature-tables-databricks-on-aws.md]

The system uses these definitions to perform a left join between the feature table and the training data when creating a training set via `create_training_set`. At inference time, the same lookup logic is used automatically to retrieve the required features.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Structure

A `FeatureLookup` has the following key parameters:^[train-models-with-feature-tables-databricks-on-aws.md, feature-serving-endpoints-databricks-on-aws.md]

| Parameter | Description | Required |
|-----------|-------------|----------|
| `table_name` | The qualified name of the feature table in Unity Catalog (e.g., `ml.recommender_system.customer_features`). | Yes |
| `feature_names` | A single feature name (string), a list of feature names, or `None` to select all features except primary keys at the time the training set is created. | Yes |
| `lookup_key` | The column name (or list of column names) in the training DataFrame used to join with the feature table’s primary keys. The type and order must match the primary keys (excluding timestamp keys) of the feature table. Required unless using a view. | Yes (unless view) |
| `output_name` | Optional alias for the feature in the output DataFrame. Required when selecting the same feature from multiple tables or the same feature with different lookup keys. | Optional |
| `default_values` | Optional dictionary of default values for features when no matching row is found in the feature table. Keys must match feature column names (or renamed names if `rename_outputs` is used). | Optional |
| `timestamp_lookup_key` | Optional timestamp column for point‑in‑time lookups with [[Time Series Feature Tables]]. | Optional |

### Feature Names

The `feature_names` parameter specifies which columns to retrieve from the feature table. You can provide:^[train-models-with-feature-tables-databricks-on-aws.md]
- A single feature name as a string.
- A list of feature names as a list of strings.
- `None` to look up all features in the feature table (excluding primary keys) at the time the training set is created.

### Lookup Keys

The `lookup_key` parameter defines how to join the feature table with the training DataFrame. When the lookup key column name differs from the feature table’s primary key column name, you specify the training DataFrame column name in `lookup_key`. The system performs an ordered join mapping the training columns to the primary keys in the order the primary keys were defined when the feature table was created.^[train-models-with-feature-tables-databricks-on-aws.md]

### Output Names

Use the `output_name` parameter when:^[train-models-with-feature-tables-databricks-on-aws.md]
- Two features from different tables have the same name.
- The same feature is needed multiple times with different lookup keys.

Provide unique aliases to avoid column name conflicts in the resulting training DataFrame.

### Default Values

The `default_values` parameter specifies fallback values for features when the feature table does not contain a matching row for a given lookup key. The dictionary uses feature column names as keys. If the feature columns are renamed using `rename_outputs`, the dictionary must use the renamed feature names.^[train-models-with-feature-tables-databricks-on-aws.md, feature-serving-endpoints-databricks-on-aws.md]

### Timestamp Lookup Key

When working with [[Time Series Feature Tables]], include the `timestamp_lookup_key` parameter to specify the timestamp column from the training DataFrame. This enables point‑in‑time lookups — the system performs an as‑of join, matching each row with the latest known feature values as of the row’s timestamp.^[databricks-feature-store-overview-and-glossary-databricks-on-aws.md]

## Usage in Training

To create a training dataset, define one or more `FeatureLookup` objects and pass them to `create_training_set`. The training DataFrame must contain all lookup keys referenced by the feature lookups, plus any label columns.^[train-models-with-feature-tables-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup

fe = FeatureEngineeringClient()

feature_lookups = [
    FeatureLookup(
        table_name='ml.recommender_system.customer_features',
        feature_names=['total_purchases_30d', 'total_purchases_7d'],
        lookup_key='customer_id'
    ),
    FeatureLookup(
        table_name='ml.recommender_system.product_features',
        feature_names=['category'],
        lookup_key='product_id'
    )
]

training_set = fe.create_training_set(
    df=training_df,
    feature_lookups=feature_lookups,
    label='rating',
    exclude_columns=['customer_id', 'product_id']
)
training_df = training_set.load_df()
```

## Usage in Serving

In a `FeatureSpec` definition for a [[Feature Serving endpoint]], `FeatureLookup` objects define which pre‑materialized features the endpoint will serve. The tables specified in a `FeatureSpec` must be published to an online feature store or a third‑party online store.^[feature-serving-endpoints-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureLookup, FeatureFunction

features = [
    FeatureLookup(
        table_name="main.default.customer_profile",
        lookup_key="user_id",
        feature_names=["average_yearly_spend", "country"]
    ),
    FeatureFunction(
        udf_name="main.default.difference",
        output_name="spending_gap",
        input_bindings={"num_1": "ytd_spend", "num_2": "average_yearly_spend"}
    ),
]
```

## Handling Feature Name Conflicts

When two feature tables contain columns with the same name, use the `output_name` parameter to disambiguate. The resulting training DataFrame uses the aliases instead of the original column names.^[train-models-with-feature-tables-databricks-on-aws.md]

```python
feature_lookups = [
    FeatureLookup(
        table_name='ml.recommender_system.customer_features',
        feature_names=['height'],
        lookup_key='customer_id',
        output_name='customer_height',
    ),
    FeatureLookup(
        table_name='ml.recommender_system.product_features',
        feature_names=['height'],
        lookup_key='product_id',
        output_name='product_height'
    ),
]
```

## Same Feature with Multiple Lookup Keys

To use the same feature joined by different lookup keys, create multiple `FeatureLookup` objects with unique `output_name` values.^[train-models-with-feature-tables-databricks-on-aws.md]

```python
feature_lookups = [
    FeatureLookup(
        table_name='ml.taxi_data.zip_features',
        feature_names=['temperature'],
        lookup_key=['pickup_zip'],
        output_name='pickup_temp'
    ),
    FeatureLookup(
        table_name='ml.taxi_data.zip_features',
        feature_names=['temperature'],
        lookup_key=['dropoff_zip'],
        output_name='dropoff_temp'
    )
]
```

## Feature Lookup in Inference

When a model is logged using the `log_model` method of [[FeatureEngineeringClient API|FeatureEngineeringClient]], it retains references to the `FeatureLookup` definitions used during training. At inference time:^[train-models-with-feature-tables-databricks-on-aws.md]
- **Batch inference**: `score_batch` automatically retrieves the required features from the offline feature store and joins them with the provided batch data before scoring.
- **Real‑time inference**: When the model is served with [[Model Serving]], the serving endpoint automatically looks up features from the [[Online Feature Store]] using the entity IDs in the request.
- **Custom feature values**: If you include a column in the batch DataFrame that matches a feature name, the system uses the provided value instead of looking up the feature from the store.

## Related Concepts

- [[Databricks Feature Store]] – Centralized repository for features.
- [[Feature Engineering in Unity Catalog]] – The workspace‑level feature store for Unity Catalog‑enabled workspaces.
- [[Workspace Feature Store UI|Workspace Feature Store]] – The legacy feature store for workspaces not enabled for Unity Catalog.
- [[FeatureSpec]] – A reuse unit combining `FeatureLookup`s and `FeatureFunction`s.
- [[Time Series Feature Tables]] – Feature tables with timestamp‑based point‑in‑time lookup.
- [[FeatureFunction]] – On‑demand feature computation using Unity Catalog functions.
- [[Feature Serving Endpoint]] – Real‑time serving of features via Databricks Feature Serving.
- [[Training Set (Feature Store)|Training Set]] – The dataset created from feature lookups for model training.

## Sources

- databricks-feature-store-overview-and-glossary-databricks-on-aws.md
- train-models-with-feature-tables-databricks-on-aws.md
- feature-serving-endpoints-databricks-on-aws.md
```

# Citations

1. [databricks-feature-store-overview-and-glossary-databricks-on-aws.md](/references/databricks-feature-store-overview-and-glossary-databricks-on-aws-368c726e.md)
2. [train-models-with-feature-tables-databricks-on-aws.md](/references/train-models-with-feature-tables-databricks-on-aws-a4118a38.md)
3. [feature-serving-endpoints-databricks-on-aws.md](/references/feature-serving-endpoints-databricks-on-aws-7fa246c9.md)
