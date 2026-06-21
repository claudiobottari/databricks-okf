---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b0a89cbf4f9cd3a54790a9d342c17f5134370c448009a6f83628d771aede2ec0
  pageDirectory: concepts
  sources:
    - regression-with-automl-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-automl-regression
    - DAR
  citations:
    - file: regression-with-automl-databricks-on-aws.md
title: Databricks AutoML Regression
description: Automated machine learning process for predicting continuous numeric values using Databricks AutoML
tags:
  - automl
  - regression
  - databricks
timestamp: "2026-06-19T20:13:13.612Z"
---

# Databricks AutoML Regression

Databricks AutoML Regression provides an automated workflow to identify the best regression algorithm and hyperparameter configuration for predicting continuous numeric values. The service manages trial runs, data preparation, and model evaluation, returning an optimal model along with notebooks that document the process. ^[regression-with-automl-databricks-on-aws.md]

## Set Up a Regression Experiment with the UI

To configure a regression experiment using the AutoML UI:

1. In the sidebar, select **Experiments**.
2. On the **Regression** card, select **Start training**.
   The **Configure AutoML experiment** page opens, where you set the dataset, problem type, target column, evaluation metric, and stopping conditions.
3. Under **Compute**, select a cluster running Databricks Runtime ML.
4. Under **Dataset**, select **Browse** and navigate to the desired table, then click **Select**.
   The table schema appears. In Databricks Runtime 10.3 ML and above, you can choose which columns AutoML should use for training (the prediction target and time column cannot be removed). In Databricks Runtime 10.4 LTS ML and above, you can specify how null values are imputed via the **Impute with** dropdown.
5. Click the **Prediction target** field and select the column to predict.
6. The **Experiment name** field shows a default name; you can change it.

Optional steps include specifying additional configuration options or using existing feature tables in Feature Store to augment the input dataset. ^[regression-with-automl-databricks-on-aws.md]

## Advanced Configurations

Open the **Advanced Configuration (optional)** section to adjust the following parameters:

- **Evaluation metric** – The primary metric used to score the runs.
- **Excluded training frameworks** – In Databricks Runtime 10.4 LTS ML and above, you can exclude specific frameworks from consideration. By default, AutoML trains models using the frameworks listed under AutoML algorithms.
- **Stopping conditions** – Default values: for forecasting experiments, stop after 120 minutes; for classification and regression experiments in Databricks Runtime 10.4 LTS ML and below, stop after 60 minutes or after 200 trials (whichever comes first). In Databricks Runtime 11.0 ML and above, the number of trials is not used as a stopping condition. In Databricks Runtime 10.4 LTS ML and above, early stopping is enabled: training and tuning stop if the validation metric no longer improves.
- **Time column** – In Databricks Runtime 10.4 LTS ML and above, you can select a time column to split data for training, validation, and testing in chronological order (applies to classification and regression).
- **Data directory** – Databricks recommends leaving this field empty to store the dataset securely as an MLflow artifact. Specifying a DBFS path is possible but the dataset will not inherit the AutoML experiment's access permissions.

^[regression-with-automl-databricks-on-aws.md]

## Run the Experiment and Monitor Results

Click **Start AutoML** to begin the experiment. The AutoML training page displays a runs table that can be refreshed. You can:

- Stop the experiment at any time.
- Open the data exploration notebook.
- Monitor individual runs.
- Navigate to the run page for any trial.

In Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential dataset issues (e.g., unsupported column types, high cardinality columns). These warnings can be reviewed on the **Warnings** tab of the training page or the experiment page after the experiment completes. Note that Databricks does its best to indicate potential errors but may not capture all issues. ^[regression-with-automl-databricks-on-aws.md]

### View Results

When the experiment finishes, you can:

- Register and deploy a model from the best run.
- Select **View notebook for best model** to review and edit the notebook that generated the best model.
- Select **View data exploration notebook** to open the corresponding notebook.
- Search, filter, and sort runs in the runs table.
- Click into any run to see its details. The generated notebook is stored in the **Artifacts** section of the [MLflow Run](/concepts/mlflow-run.md) page; you can download it if your workspace administrators allow artifact downloads. The run page also includes code snippets for making predictions with the model.

To return to an experiment later, find it in the table on the Experiments page. All results—including data exploration and training notebooks—are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. ^[regression-with-automl-databricks-on-aws.md]

## Register and Deploy a Model

From the completed experiment, the top row in the runs table shows the best model based on the primary metric. To register and deploy:

1. Select the link in the **Models** column for the desired model.
2. Click the **Register model** button to register it to Unity Catalog or the Model Registry (Databricks recommends Unity Catalog for the latest features).
3. After registration, you can deploy the model to a custom model serving endpoint.

^[regression-with-automl-databricks-on-aws.md]

## Troubleshooting

### No module named 'pandas.core.indexes.numeric'

When serving a model built with AutoML using Model Serving, an incompatible `pandas` version may cause the error: `No module named 'pandas.core.indexes.numeric`. To resolve this, run the provided `add-pandas-dependency.py` script, which edits the `requirements.txt` and `conda.yaml` of the logged model to include the appropriate `pandas` version (`pandas==1.5.3`). After modifying the script with the correct `run_id`, re‑register the model to Unity Catalog or the model registry, then try serving the new version. ^[regression-with-automl-databricks-on-aws.md]

## Related Concepts

- [AutoML on Databricks](/concepts/automl-on-databricks.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Model Registry](/concepts/mlflow-model-registry.md)
- [Model Serving](/concepts/model-serving.md)
- [Feature Store](/concepts/feature-store.md)
- DBFS

## Sources

- regression-with-automl-databricks-on-aws.md

# Citations

1. [regression-with-automl-databricks-on-aws.md](/references/regression-with-automl-databricks-on-aws-cc5aa3d0.md)
