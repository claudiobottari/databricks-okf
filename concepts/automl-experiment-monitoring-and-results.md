---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9e8bdb2639301a43783fcaf32abea47643f878c2d41d849ee13259850fa40f22
  pageDirectory: concepts
  sources:
    - classification-with-automl-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automl-experiment-monitoring-and-results
    - Results and AutoML Experiment Monitoring
    - AEMAR
  citations:
    - file: classification-with-automl-databricks-on-aws.md
title: AutoML Experiment Monitoring and Results
description: How to monitor AutoML experiment progress, view warnings, explore generated notebooks, and interpret trial run results
tags:
  - databricks
  - automl
  - monitoring
timestamp: "2026-06-19T17:43:41.732Z"
---

# AutoML Experiment Monitoring and Results

**AutoML Experiment Monitoring and Results** refers to the tools and workflows provided by Databricks AutoML for tracking the progress of automated machine learning experiments, inspecting warnings, and reviewing the outputs after training completes. These capabilities help users understand how the experiment is performing, identify potential dataset issues, and take action on the best models.

## Monitor Experiment Progress

While an AutoML experiment is running, the training page provides real-time visibility into the process. You can stop the experiment at any time, open the data exploration notebook, and monitor individual trial runs. The runs table can be refreshed to see the latest results. For each run, you can navigate to its run page for detailed information. ^[classification-with-automl-databricks-on-aws.md]

To start an experiment, click **Start AutoML** from the configuration page. The training page then appears with controls and a runs table.

## View Warnings

In Databricks Runtime 10.1 ML and above, AutoML displays warnings for potential issues with the dataset, such as unsupported column types or high cardinality columns. These warnings are available on a **Warnings** tab during training and also after the experiment completes. Databricks notes that while it does its best to indicate potential errors or issues, the warnings may not be comprehensive. ^[classification-with-automl-databricks-on-aws.md]

## View Results

When the experiment finishes, the results page offers several actions:

- **Register and deploy** one of the models using the UI. You can register the best model (top row based on the primary metric) to Unity Catalog or the Model Registry, then deploy it to a custom model serving endpoint. ^[classification-with-automl-databricks-on-aws.md]
- **View notebook for best model** – review and edit the notebook that produced the best model. ^[classification-with-automl-databricks-on-aws.md]
- **View data exploration notebook** – open the data exploration notebook that AutoML generated. ^[classification-with-automl-databricks-on-aws.md]
- **Search, filter, and sort** the runs table to compare performance. ^[classification-with-automl-databricks-on-aws.md]
- **View run details** – click on the **Models** or **Start Time** column of any run to open its [MLflow Run](/concepts/mlflow-run.md) page. There you can see parameters, metrics, tags, and artifacts, including the saved model and code snippets for making predictions. The generated notebook for that trial run is saved in the **Artifacts** section of the run page; you can download and import it into the workspace if downloading artifacts is enabled by workspace administrators. ^[classification-with-automl-databricks-on-aws.md]

All results of an AutoML experiment, including the data exploration notebook and training notebooks, are stored in a `databricks_automl` folder in the home folder of the user who ran the experiment. To revisit an experiment later, find it in the table on the Experiments page. ^[classification-with-automl-databricks-on-aws.md]

## Troubleshooting: Pandas Version Error During Model Serving

When serving a model built using AutoML with Model Serving, you may encounter the error `No module named 'pandas.core.indexes.numeric'`. This is caused by an incompatible `pandas` version between AutoML and the model serving endpoint environment. To resolve it, run the [add-pandas-dependency.py script](https://docs.databricks.com/aws/en/assets/files/add-pandas-dependency-4808dc9dcdfb035bdca6ebce6b86d719.py), which edits the `requirements.txt` and `conda.yaml` files of the logged model to include `pandas==1.5.3`. After modifying the script with the appropriate `run_id`, re-register the model to Unity Catalog or the Model Registry, then retry serving the new version. ^[classification-with-automl-databricks-on-aws.md]

## Related Concepts

- Classification with AutoML – The specific AutoML problem type described in the source.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The underlying tracking system for AutoML runs.
- [Model Serving](/concepts/model-serving.md) – Deployment endpoint for registered AutoML models.
- [Unity Catalog](/concepts/unity-catalog.md) – Recommended model registry for latest features.
- Data Exploration Notebook – AutoML-generated notebook for dataset analysis.

## Sources

- classification-with-automl-databricks-on-aws.md
- regression-with-automl-databricks-on-aws.md

# Citations

1. [classification-with-automl-databricks-on-aws.md](/references/classification-with-automl-databricks-on-aws-61813bfe.md)
