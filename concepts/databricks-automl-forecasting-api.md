---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa68af8e47447512af0f970692faed0d7a3d8196d7749b61bce552a463db5c06
  pageDirectory: concepts
  sources:
    - automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
    - train-forecasting-models-with-automl-python-api-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-automl-forecasting-api
    - DAFA
    - Databricks AutoML Forecasting
    - Data Preparation for AutoML Forecasting
  citations:
    - file: train-forecasting-models-with-automl-python-api-databricks-on-aws.md
    - file: automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md
title: Databricks AutoML Forecasting API
description: The automl.forecast() Python function that automates time series model selection, training, and evaluation on Databricks.
tags:
  - databricks
  - automl
  - api
  - forecasting
timestamp: "2026-06-19T17:38:51.796Z"
---

# Databricks AutoML Forecasting API

**Databricks AutoML Forecasting API** is a programmatic interface within the Databricks AutoML library that automates time‑series forecasting. The primary entry point is the `automl.forecast()` Python function, which handles data splitting, algorithm selection, hyperparameter tuning, model training, and evaluation. Users provide a tabular dataset with a time column and a target column, along with forecasting parameters, and receive a summary object containing the best trial results and the trained model. ^[train-forecasting-models-with-automl-python-api-databricks-on-aws.md, automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Core Parameters

The `automl.forecast()` function accepts several key parameters:

- `dataset` — Input DataFrame containing the time series data.
- `target_col` — Name of the column to forecast (e.g., `cases`, `occupancy_rate`).
- `time_col` — Name of the column containing timestamps or dates.
- `frequency` — Frequency of the time series (e.g., `"d"` for daily, `"h"` for hourly).
- `horizon` — Number of time steps to forecast into the future.
- `timeout_minutes` — Maximum time (in minutes) allowed for the AutoML run.
- `primary_metric` — Metric to optimize during training (e.g., `"mdape"`).
- `identity_col` — Optional column identifying different time series in the dataset (for [Multi-Series Forecasting](/concepts/multi-series-forecasting.md)).
- `output_database` — Optional database name; if provided, predictions from the best model are saved as a table.
- `feature_store_lookups` — List of dictionaries referencing [Feature Store](/concepts/feature-store.md) tables for covariates.

For a complete list, see the [AutoML Python API reference](/concepts/automl-python-api.md). ^[train-forecasting-models-with-automl-python-api-databricks-on-aws.md, automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using Covariates (External Regressors)

Covariates are additional variables outside the target time series that can improve forecasting accuracy (e.g., a weekend flag for hotel occupancy). To use covariates, you must register them as [Feature Store](/concepts/feature-store.md) tables and pass them through the `feature_store_lookups` parameter. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Creating and Registering Covariates

1. **Feature engineer** the covariate columns from your dataset (e.g., computing `is_weekend` from a date column).
2. **Create a Feature Store table** using `FeatureEngineeringClient.create_table()`. The table must include a primary key that matches the time column in the forecasting dataset.
3. **Define the lookup** as a dictionary with `table_name` and `lookup_key` fields.

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

hotel_weekend_feature_table = fe.create_table(
    name='ml.default.hotel_weekend_features',
    primary_keys=['date'],
    df=compute_hotel_weekend_features(df),
    description='Hotel is_weekend features table'
)

hotel_weekend_feature_lookup = {
    "table_name": "ml.default.hotel_weekend_features",
    "lookup_key": ["date"]
}
feature_lookups = [hotel_weekend_feature_lookup]
```

^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

### Passing Feature Lookups to AutoML

Pass the `feature_lookups` list to the `feature_store_lookups` parameter of `automl.forecast()`. AutoML automatically joins the covariate tables with the primary training data during model training. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

```python
from databricks import automl

summary = automl.forecast(
    dataset=df,
    target_col="occupancy_rate",
    time_col="date",
    frequency="d",
    horizon=1,
    timeout_minutes=30,
    identity_col=None,
    feature_store_lookups=feature_lookups
)
```

## Requirements for Covariate Tables

- The covariate Feature Store table must have a primary key that aligns with the `time_col` in the main dataset.
- Users may provide multiple feature lookups; `feature_store_lookups` accepts a list of lookup dictionaries.
- Feature tables can be created using the Python `FeatureEngineeringClient`, SQL, or Delta Live Tables. ^[automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md]

## Using the Trained Model for Forecasting

After training, the best model is logged via MLflow. You can load it and call `predict_timeseries()` to generate forecasts. If `output_database` was provided, predictions are also saved as a table. ^[train-forecasting-models-with-automl-python-api-databricks-on-aws.md]

```python
import mlflow.pyfunc

model_uri = f"runs:/{summary.best_trial.mlflow_run_id}/model"
pyfunc_model = mlflow.pyfunc.load_model(model_uri)

# Generate forecasts including history
forecasts = pyfunc_model._model_impl.python_model.predict_timeseries(include_history=True)
```

## Related Concepts

- [AutoML Python API Reference](/concepts/automl-python-api.md) — Full documentation for all AutoML API parameters and return types.
- [Feature Store in Unity Catalog](/concepts/feature-tables-in-unity-catalog.md) — Creating and managing feature tables for covariates.
- [Time Series Forecasting](/concepts/multi-series-forecasting.md) — Core concepts for forecasting tasks.
- [Multi-Series Forecasting](/concepts/multi-series-forecasting.md) — Forecasting multiple related time series simultaneously.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) — Registering and deploying models trained by AutoML.

## Sources

- train-forecasting-models-with-automl-python-api-databricks-on-aws.md
- automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md

# Citations

1. [train-forecasting-models-with-automl-python-api-databricks-on-aws.md](/references/train-forecasting-models-with-automl-python-api-databricks-on-aws-22e8e0b3.md)
2. [automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws.md](/references/automl-improve-forecasting-with-covariates-external-regressors-databricks-on-aws-87541cc8.md)
