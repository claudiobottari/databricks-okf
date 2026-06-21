---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c83c7676040d8b65b6209f7dc6a32611831a884e043b57e07dccc9935d7bc12
  pageDirectory: concepts
  sources:
    - forecasting-serverless-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-forecasting-experiment-stages
    - AFES
    - AutoML Forecasting Experiments
    - AutoML forecasting experiments
    - AutoML Experiments
    - Forecasting Experiments
    - automl-forecasting-experiment-lifecycle
    - AFEL
  citations:
    - file: forecasting-serverless-with-automl-databricks-on-aws.md
title: AutoML Forecasting Experiment Stages
description: "The three-phase pipeline of a Databricks forecasting experiment: Preprocessing (validation, imputation, feature generation), Tuning (algorithm exploration), and Training (final model training and registration)."
tags:
  - forecasting
  - AutoML
  - pipeline
  - stages
timestamp: "2026-06-18T12:23:49.645Z"
---

# AutoML Forecasting Experiment Stages

**AutoML Forecasting Experiment Stages** describes the sequential phases that a serverless forecasting experiment passes through from initiation to completion in Databricks Model Training. Understanding these stages helps users monitor experiment progress, diagnose issues, and interpret results effectively.

## Overview

When you run a serverless forecasting experiment using the Databricks Model Training UI, the experiment progresses through three distinct stages: **Preprocessing**, **Tuning**, and **Training**. Each stage performs specific operations to prepare data, explore algorithms, and produce the final forecasting model. ^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Stage 1: Preprocessing

The Preprocessing stage validates and prepares the input table for model training. Key operations during this stage include:

- **Validation:** Checks that the input data meets the required format and types, including verifying that the time column is of type `timestamp` or `date`.
- **Missing value imputation:** Fills in missing time steps with the previous value to ensure regular frequency, which is required for algorithms like Auto-ARIMA.
- **Data splitting:** Divides the data into training, validation, and test sets. If a custom split column is specified, values must be "train", "validate", or "test".
- **Automatic feature generation:** Applies transformations such as one-hot encoding for categorical features to prepare them for model training.

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Stage 2: Tuning

The Tuning stage explores different forecasting algorithms and searches for optimal hyperparameter configurations. During this stage, AutoML:

- Tests multiple forecasting [algorithms](/concepts/hyperopt-search-algorithms.md) based on the selected training framework.
- Evaluates different hyperparameter combinations to identify configurations that minimize the chosen primary metric.
- Considers optional covariates such as holiday region data and weight columns.
- Continues until the specified timeout duration is reached or all configurations are explored.

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Stage 3: Training

The Training stage finalizes the model using the best configuration identified during tuning. Activities in this stage include:

- Training the final model on the full training dataset with the selected hyperparameters.
- Evaluating the trained model on the test set.
- Registering the best model in [Unity Catalog](/concepts/unity-catalog.md) if a model registration path was specified during experiment setup.

^[forecasting-serverless-with-automl-databricks-on-aws.md]

## Monitoring Experiment Progress

From the experiment training page, you can:

- Stop the experiment at any time.
- Monitor individual runs as they progress through each stage.
- Navigate to the run page for detailed information on any completed run.

## Post-Experiment Actions

After training completes, the prediction results are stored in the specified Delta table, and the best model is registered to Unity Catalog. From the experiments page, users can:

- **View predictions:** See the forecasting results table.
- **Generate batch inference notebook:** Open an auto-generated notebook for batch inferencing using the best model.
- **Create serving endpoint:** Deploy the best model to a Model Serving endpoint.

## Related Concepts

- [Serverless Forecasting](/concepts/databricks-serverless-forecasting.md) — The fully-managed compute environment for AutoML forecasting
- [AutoML Experiment Configuration](/concepts/automl-experiment-configuration.md) — Parameters that control experiment behavior
- Model Training UI — The interface for creating and monitoring experiments
- [Forecast Frequency and Horizon](/concepts/forecast-frequency-and-horizon.md) — Configuration of time units and prediction length
- [Time Series Identifier Columns](/concepts/time-series-identifier-columns.md) — Columns for multi-series forecasting

## Sources

- forecasting-serverless-with-automl-databricks-on-aws.md

# Citations

1. [forecasting-serverless-with-automl-databricks-on-aws.md](/references/forecasting-serverless-with-automl-databricks-on-aws-8952bc49.md)
