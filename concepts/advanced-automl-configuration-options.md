---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 500d21fcdb441393acc65b94cc1d8955b10bebe26b7a81ef95f70fa1a7f6b2df
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - advanced-automl-configuration-options
    - AACO
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: Advanced AutoML Configuration Options
description: Advanced parameters for AutoML experiments including evaluation metrics, training framework exclusion, stopping conditions (time-based or early stopping), and time-based data splitting.
tags:
  - automl
  - configuration
  - databricks
timestamp: "2026-06-19T14:11:59.955Z"
---

# Advanced AutoML Configuration Options

**Advanced AutoML Configuration Options** refer to the set of parameters that allow users to fine‑tune the behavior of AutoML experiments on Databricks. These options are available through the **Advanced Configuration (optional)** section in the UI and enable control over evaluation metrics, training frameworks, stopping conditions, data splitting, and data storage. ^[classification-with-automl-databricks-on-aws.md]

## Evaluation Metric

Users can select the primary metric used to score and rank AutoML runs. The chosen metric determines how the “best” model is identified during the experiment. ^[classification-with-automl-databricks-on-aws.md]

See the AutoML API Reference for a list of supported metrics.

## Excluding Training Frameworks

By default, AutoML trains models using all frameworks listed under AutoML Algorithms. In Databricks Runtime 10.4 LTS ML and above, you can exclude specific training frameworks from consideration, limiting the search space to only those frameworks you want to evaluate. ^[classification-with-automl-databricks-on-aws.md]

## Stopping Conditions

Stopping conditions control when an AutoML experiment ends. Default and configurable conditions include:

- **Forecasting experiments**: stop after 120 minutes.
- **Classification and regression experiments** (Databricks Runtime 10.4 LTS ML and below): stop after 60 minutes or after completing 200 trials, whichever comes first. For Databricks Runtime 11.0 ML and above, the number of trials is no longer used as a stopping condition; only time‑based stopping applies.
- **Early stopping** (Databricks Runtime 10.4 LTS ML and above for classification and regression): training and tuning halts automatically when the validation metric stops improving. ^[classification-with-automl-databricks-on-aws.md]

## Time Column for Data Splitting

In Databricks Runtime 10.4 LTS ML and above, classification and regression experiments can use a `time column` to split the data chronologically into training, validation, and test sets. This is useful for time‑series‑aware model evaluation. See [Classification Data Preparation Settings](/concepts/automl-classification-data-preparation.md) and Regression Data Preparation Settings for more details. ^[classification-with-automl-databricks-on-aws.md]

## Data Directory

Databricks recommends leaving the **Data directory** field empty. When not populated, the dataset is stored securely as an MLflow artifact. If a DBFS path is specified, the dataset does **not** inherit the AutoML experiment’s access permissions. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- AutoML API Reference
- AutoML Algorithms
- Classification with AutoML
- Regression with AutoML
- Forecasting with AutoML
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md)

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
