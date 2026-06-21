---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59fc2a31db4cba6ae0934a8960bf92c1c37522efe2f8d2c2f3d16fb71a028405
  pageDirectory: concepts
  sources:
    - automl-feature-store-integration-databricks-on-aws.md
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - unity-catalog-feature-tables
    - UCFT
  citations:
    - file: automl-feature-store-integration-databricks-on-aws.md
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Unity Catalog Feature Tables
description: The modern feature store system in Databricks, managed through Unity Catalog, that AutoML can query to augment training data.
tags:
  - unity-catalog
  - feature-store
  - databricks
timestamp: "2026-06-19T14:07:08.345Z"
---

# Unity Catalog Feature Tables

**Unity Catalog feature tables** are Delta tables registered in [Unity Catalog](/concepts/unity-catalog.md) with a primary key defined. They serve as a shared, governed source of features that can be joined with training data during AutoML experiments, enabling reuse of feature engineering work across models and teams.^[automl-feature-store-integration-databricks-on-aws.md, automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

---

## Key Characteristics

- Feature tables are managed under Unity Catalog, providing centralized governance and lineage.
- Each feature table must define at least one primary key column, which is used to look up features when joining with training datasets.
- Feature tables can be created using the `FeatureEngineeringClient` in Python, SQL, or Delta Live Tables.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

---

## Requirements for AutoML Use

- **Classification and regression** experiments: Databricks Runtime 11.3 LTS ML and above.
- **Forecasting** experiments: Databricks Runtime 12.2 LTS ML and above.^[automl-feature-store-integration-databricks-on-aws.md]

---

## Using Feature Tables with AutoML

AutoML can augment the original input dataset with features from one or more feature tables in Unity Catalog.^[automl-feature-store-integration-databricks-on-aws.md]

### Select a Feature Table via the UI

After configuring your AutoML experiment:

1. Click **Join features (optional)**.
2. On the **Join additional features** page, select a feature table in the **Feature Table** field.
3. For each **Feature table primary key**, select the corresponding lookup key — a column in your training dataset.
4. For [Time Series Feature Tables](/concepts/time-series-feature-tables.md), also select the timestamp lookup key from the training dataset.
5. To add more feature tables, click **Add another feature table** and repeat these steps.^[automl-feature-store-integration-databricks-on-aws.md]

### Use Feature Tables with the AutoML API

Set the `feature_store_lookups` parameter in your AutoML run specification. Each lookup entry requires `table_name` (fully qualified name of the feature table) and `lookup_key` (a list of column names that map from the training dataset to the feature table’s primary keys). Example for a forecasting experiment:^[automl-feature-store-integration-databricks-on-aws.md, automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
feature_store_lookups = [
  {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
  }
]
```

When using AutoML forecasting, you pass this list to the `feature_store_lookups` parameter. The feature table acts as covariates (external regressors) to improve forecast accuracy.^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks import automl
summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    timeout_minutes=30,
    feature_store_lookups=feature_lookups
)
```

For classification and regression experiments, use the corresponding AutoML function (e.g., `automl.classify()` or `automl.regress()`) with the same `feature_store_lookups` parameter.

---

## Creating a Feature Table

Feature tables can be created with the [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) client. The example below creates a table with `date` as the primary key:^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks.feature_engineering import FeatureEngineeringClient
fe = FeatureEngineeringClient()

hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=hotel_weekend_feature_df,
    description='Hotel is_weekend features table'
)
```

Alternatively, you can define feature tables using SQL or Delta Live Tables.

---

## Benefits of Using Feature Tables

- **Feature reuse**: The same feature definitions can be applied across multiple models, reducing duplication.
- **Governance**: Unity Catalog provides access control, auditing, and lineage for features.
- **Simplified AutoML**: AutoML automatically joins the required features during training, scoring, and inference.

---

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer that manages feature tables
- AutoML – Automated machine learning that can join feature tables
- [Feature Engineering in Unity Catalog](/concepts/feature-engineering-in-unity-catalog.md) – API and tools for creating and managing feature tables
- [Workspace Feature Store](/concepts/workspace-feature-store-ui.md) – Legacy feature store (non-Unity Catalog)
- Forecasting with Covariates – Using feature tables as external regressors in forecasting

## Sources

- automl-feature-store-integration-databricks-on-aws.md
- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [automl-feature-store-integration-databricks-on-aws.md](/references/automl-feature-store-integration-databricks-on-aws-f3267d3d.md)
2. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
