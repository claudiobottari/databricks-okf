---
title: Read MLflow experiments | Databricks on AWS
source: https://docs.databricks.com/aws/en/query/formats/mlflow-experiment
ingestedAt: "2026-06-18T08:18:34.612Z"
---

The `mlflow-experiment` data source provides a Spark DataFrameReader API for loading MLflow experiment run data into a DataFrame. Databricks users commonly use it to analyze training run results, compare metrics across experiments, and build dashboards on top of experiment history. For more information, see [Organize training runs with MLflow experiments](https://docs.databricks.com/aws/en/mlflow/experiments).

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Reading MLflow experiment run data requires Databricks Runtime 6.0 ML and above.

## Usage[​](#usage "Direct link to Usage")

The following examples show how to load and filter MLflow experiment data using the Spark DataFrame API.

### Load data from the notebook experiment[​](#load-data-from-the-notebook-experiment "Direct link to Load data from the notebook experiment")

To load data from the current notebook's experiment, call `load()` with no arguments.

*   Python
*   Scala

Python

    df = spark.read.format("mlflow-experiment").load()display(df)

### Load data using experiment IDs[​](#load-data-using-experiment-ids "Direct link to Load data using experiment IDs")

To load data from one or more workspace experiments, pass the experiment IDs as a comma-separated string to `load()`.

*   Python
*   Scala

Python

    df = spark.read.format("mlflow-experiment").load("3270527066281272")display(df)

### Load data using an experiment name[​](#load-data-using-an-experiment-name "Direct link to Load data using an experiment name")

To load data by experiment name, resolve the name to an ID using the MLflow client, then pass the ID to `load()`.

*   Python
*   Scala

Python

    expId = mlflow.get_experiment_by_name("/Shared/diabetes_experiment/").experiment_iddf = spark.read.format("mlflow-experiment").load(expId)display(df)

### Filter data based on metrics and parameters[​](#filter-data-based-on-metrics-and-parameters "Direct link to Filter data based on metrics and parameters")

After loading experiment data, use standard DataFrame filter expressions to query across metrics and parameters.

*   Python
*   Scala

Python

    df = spark.read.format("mlflow-experiment").load("3270527066281272")filtered_df = df.filter("metrics.loss < 0.01 AND params.learning_rate > '0.001'")display(filtered_df)

## Output schema[​](#output-schema "Direct link to Output schema")

The schema returned by the `mlflow-experiment` data source is fixed regardless of the experiment loaded:

    root|-- run_id: string|-- experiment_id: string|-- metrics: map|    |-- key: string|    |-- value: double|-- params: map|    |-- key: string|    |-- value: string|-- tags: map|    |-- key: string|    |-- value: string|-- start_time: timestamp|-- end_time: timestamp|-- status: string|-- artifact_uri: string

## Additional resources[​](#additional-resources "Direct link to Additional resources")

*   [Read OpenSharing shared tables using Apache Spark DataFrames](https://docs.databricks.com/aws/en/query/formats/deltasharing): If your data is shared via Delta Sharing rather than stored in MLflow, use the `deltasharing` format to read shared tables with the same DataFrameReader API.
