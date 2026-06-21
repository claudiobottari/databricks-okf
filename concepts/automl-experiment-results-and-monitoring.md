---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d54fb283c5866b38d25dd99299c8bf9e343f73cac9ace6f59b5f4cf32a48607
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-results-and-monitoring
    - Monitoring and AutoML Experiment Results
    - AERAM
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Experiment Results and Monitoring
description: How to view, monitor, and interpret results of an AutoML experiment including warnings, runs table, and generated notebooks
tags:
  - automl
  - monitoring
  - results
  - databricks
timestamp: "2026-06-19T09:13:09.669Z"
---

# AutoML Experiment Results and Monitoring

**AutoML Experiment Results and Monitoring** refers to the process of viewing, interpreting, and managing the outcomes of an automated machine learning (AutoML) experiment on Databricks. AutoML automatically searches for the best algorithm and hyperparameter configuration for a given problem type — such as classification, regression, or forecasting — and generates a set of trial runs with associated metrics, notebooks, and models. ^[classification-with-automl-databricks-on-aws.md]

## Viewing Experiment Progress

When an AutoML experiment starts, the AutoML training page displays a runs table that updates as trials complete. You can click the refresh button to see the latest status. From this page, you can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial run.

^[classification-with-automl-databricks-on-aws.md]

With Databricks Runtime 10.1 ML and above, AutoML also displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns. To see any warnings, click the **Warnings** tab on the training page or the experiment page after the experiment completes. ^[classification-with-automl-databricks-on-aws.md]

### Early Stopping

In Databricks Runtime 10.4 LTS ML and above, AutoML incorporates early stopping for classification and regression experiments — it stops training and tuning models if the validation metric is no longer improving. ^[classification-with-automl-databricks-on-aws.md]

## Viewing Results After Completion

When the experiment completes, you can interact with the results in several ways: ^[classification-with-automl-databricks-on-aws.md]

- **Register and deploy** one of the models with MLflow.
- **View the best model's notebook** — select "View notebook for best model" to review and edit the notebook that created the best model.
- **View the data exploration notebook** — select "View data exploration notebook" to open the notebook that explored the input dataset.
- **Search, filter, and sort** the runs in the runs table.
- **See details for any run** — click into the [MLflow Run](/concepts/mlflow-run.md) to view the generated notebook (saved in the **Artifacts** section), parameters, metrics, tags, and code snippets for making predictions.

### Locating Past Experiments

To return to an AutoML experiment later, find it in the table on the [MLflow Experiments](/concepts/mlflow-experiment.md) page. The results of each AutoML experiment — including the data exploration and training notebooks — are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[classification-with-automl-databricks-on-aws.md]

## Stopping Conditions

Default stopping conditions for AutoML experiments are: ^[classification-with-automl-databricks-on-aws.md]

- **Forecasting experiments**: Stop after 120 minutes.
- **Classification and regression experiments (Databricks Runtime 10.4 LTS ML and below)**: Stop after 60 minutes or after completing 200 trials, whichever happens first.
- **Classification and regression experiments (Databricks Runtime 11.0 ML and above)**: Only time-based stopping is used (number of trials is not a stopping condition).

You can edit these stopping conditions in the advanced configuration section when setting up the experiment.

## Best Model Selection

When a run completes, the top row in the runs table shows the best model based on the primary metric selected during experiment setup. The evaluation metric is the primary metric used to score the runs and determine the best configuration. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification](/concepts/automl-classification-classify.md) — Setting up and running classification experiments
- [AutoML Regression](/concepts/automl-regress.md) — Setting up and running regression experiments
- [AutoML Forecasting](/concepts/automl-forecast.md) — Setting up and running forecasting experiments
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing and tracking experiment runs
- MLflow Models — Registering and deploying trained models
- [AutoML Data Preparation](/concepts/automl-data-preparation.md) — Configuring column selection, imputation, and data splitting
- AutoML Algorithms — The frameworks used during automated training

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
