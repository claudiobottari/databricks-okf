---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 687ee732a566c57ccd4bf9cdc34b1b83ac9a409c26e5d13ce7828ce1ec167566
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-configuration-ui
    - AECU
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Experiment Configuration UI
description: User interface workflow for configuring AutoML classification experiments including dataset selection, prediction target specification, compute cluster choice, and experiment naming.
tags:
  - automl
  - databricks
  - user-interface
timestamp: "2026-06-19T14:12:23.167Z"
---

---
title: AutoML Experiment Configuration UI
summary: Step-by-step UI workflow for setting up a classification AutoML experiment on Databricks, including compute selection, dataset browsing, prediction target selection, and column specification.
sources:
  - classification-with-automl-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:57:03.729Z"
updatedAt: "2026-06-18T10:57:03.729Z"
tags:
  - user-interface
  - automl
  - databricks
  - experiment-setup
aliases:
  - automl-experiment-configuration-ui
  - AECU
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 2
---

# AutoML Experiment Configuration UI

The **AutoML Experiment Configuration UI** is a graphical interface in Databricks that guides you through setting up, configuring, and running an automated machine learning (AutoML) experiment for classification, regression, or forecasting tasks. The interface provides a no-code workflow to define your dataset, select the prediction target, choose evaluation metrics, and configure advanced options like feature selection, missing value imputation, and training framework exclusions.^[classification-with-automl-databricks-on-aws.md]

## Accessing the Configuration UI

To access the AutoML experiment configuration page from the sidebar, select **Experiments**. On the **Classification** card, select **Start training** to open the **Configure AutoML experiment page**.^[classification-with-automl-databricks-on-aws.md]

## Core Configuration Fields

The following primary settings are available on the **Configure AutoML experiment page**:^[classification-with-automl-databricks-on-aws.md]

- **Compute**: Select a cluster running [Databricks Runtime ML](/concepts/databricks-runtime-ml.md).
- **Dataset**: Browse to select a table from the workspace. After you select a table, the table schema displays.
- **Prediction target**: A drop-down list of all columns in the schema. Select the column you want the model to predict.
- **Experiment name**: A default name is shown. You can type a new name to override it.

## Advanced Configuration

Opening the **Advanced Configuration (optional)** section reveals additional parameters:^[classification-with-automl-databricks-on-aws.md]

- **Evaluation metric** — The primary metric used to score and compare the runs.^[classification-with-automl-databricks-on-aws.md]
- **Exclude training frameworks** (Databricks Runtime 10.4 LTS ML and above) — You can exclude specific frameworks from the set of algorithms AutoML will try.^[classification-with-automl-databricks-on-aws.md]
- **Stopping conditions** — In Databricks Runtime 10.4 LTS ML and below, classification and regression experiments stop after 60 minutes or after completing 200 trials, whichever happens first. In Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition. For forecasting experiments, the default is 120 minutes.^[classification-with-automl-databricks-on-aws.md]
- **Time column** (Databricks Runtime 10.4 LTS ML and above) — A column used to split the data for training, validation, and testing in chronological order (applies only to classification and regression).^[classification-with-automl-databricks-on-aws.md]
- **Data directory** — Databricks recommends leaving this field empty. Not populating it triggers the default behavior of securely storing the dataset as an MLflow artifact. A DBFS path can be specified, but in that case the dataset does not inherit the AutoML experiment's access permissions.^[classification-with-automl-databricks-on-aws.md]

## Dataset Configuration Options

After you select a table and click **Select**, the table schema appears. In Databricks Runtime 10.3 ML and above, you can specify which columns AutoML should use for training. You cannot remove the column selected as the prediction target or the time column used to split the data.^[classification-with-automl-databricks-on-aws.md]

In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed by selecting from the **Impute with** dropdown. By default, AutoML selects an imputation method based on the column type and content.^[classification-with-automl-databricks-on-aws.md]

## Running and Monitoring the Experiment

To start the experiment, click **Start AutoML**. The experiment begins to run, and the AutoML training page appears. You can refresh the runs table by clicking the refresh button.^[classification-with-automl-databricks-on-aws.md]

From the training page, you can:^[classification-with-automl-databricks-on-aws.md]

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial run.

In Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns. To see these warnings, click the **Warnings** tab on the training page or the experiment page after the experiment completes.^[classification-with-automl-databricks-on-aws.md]

## Viewing Results

When the experiment completes, the UI provides several ways to review and act on the results:^[classification-with-automl-databricks-on-aws.md]

- **Register and deploy** one of the models using [MLflow](/concepts/mlflow.md).
- **View notebook for best model** — Review and edit the notebook that created the best model.
- **View data exploration notebook** — Open the data exploration notebook.
- **Search, filter, and sort** the runs in the runs table.
- **See details for any run** — The generated notebook containing source code for a trial run is saved in the **Artifacts** section of the [MLflow Run](/concepts/mlflow-run.md) page. You can download this notebook and import it into the workspace if downloading artifacts is enabled by your workspace administrators.

To return to this AutoML experiment later, find it in the table on the [Experiments page](/concepts/mlflow-experiment.md). The results of each AutoML experiment, including the data exploration and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment.^[classification-with-automl-databricks-on-aws.md]

## Register and Deploy a Model

When a run completes, the top row shows the best model based on the primary metric. To register and deploy a model:^[classification-with-automl-databricks-on-aws.md]

1. Select the link in the **Models** column for the model you want to register.
2. Select the register model button to register it to [Unity Catalog](/concepts/unity-catalog.md) or the [Model Registry](/concepts/mlflow-model-registry.md). Databricks recommends you register models to Unity Catalog for the latest features.
3. After registration, you can deploy the model to a [custom model serving endpoint](/concepts/custom-model-serving-endpoint-support.md).^[classification-with-automl-databricks-on-aws.md]

## Troubleshooting: Missing Pandas Dependency

When serving an AutoML model with Model Serving, you may encounter the error `No module named 'pandas.core.indexes.numeric`. This is due to an incompatible `pandas` version between AutoML and the model serving endpoint environment. The recommended fix is to run the `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` for your logged model to include `pandas==1.5.3`. After running the script, re-register the model to Unity Catalog or the Model Registry.^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML Classification API](/concepts/automl-classification-classify.md) — Programmatic interface for configuring AutoML experiments
- [AutoML Classification Data Preparation](/concepts/automl-classification-data-preparation.md) — Detailed data preparation settings for classification experiments
- AutoML Regression UI — The similar interface for regression problems
- AutoML Forecasting UI — The interface for forecasting experiments
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying experiment tracking system
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) — The required runtime for AutoML experiments
- [Feature Store Integration](/concepts/automl-feature-store-integration.md) — Using existing feature tables to augment input datasets

## Sources

- classification-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
