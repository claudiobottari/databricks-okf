---
title: Track model development using MLflow | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/tracking
ingestedAt: "2026-06-18T08:14:17.079Z"
---

MLflow tracking lets you log notebooks and training datasets, parameters, metrics, tags, and artifacts related to training a machine learning or deep learning model. For an example notebook to get started with MLflow, see [Tutorial: End-to-end classic ML models on Databricks](https://docs.databricks.com/aws/en/mlflow/end-to-end-example).

## MLflow tracking with experiments, runs, and models[​](#mlflow-tracking-with-experiments-runs-and-models "Direct link to MLflow tracking with experiments, runs, and models")

The model development process is iterative, and it can be challenging to keep track of your work as you develop and optimize a model. In Databricks, you can use [MLflow tracking](https://mlflow.org/docs/latest/tracking.html) to help you keep track of the model development process, including parameter settings or combinations you have tried and how they affected the model's performance.

MLflow tracking uses _experiments_, _runs_, and _models_ to log and track your ML and deep learning model development. A run is a single execution of model code. During an MLflow run, you can log model parameters and results. An experiment is a collection of related runs. In an experiment, you can compare and filter runs to understand how your model performs and how its performance depends on the parameter settings, input data, and so on. A model is a collection of artifacts that represent a trained machine learning model.

With [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install), `LoggedModels` elevates the concept of a model produced by a run, establishing it as a distinct entity to track the model lifecycle across different training and evaluation runs.

*   [Organize training runs with MLflow experiments](https://docs.databricks.com/aws/en/mlflow/experiments)
*   [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model)
*   [View training results with MLflow runs](https://docs.databricks.com/aws/en/mlflow/runs)
*   [Build dashboards with MLflow metadata in system tables](https://docs.databricks.com/aws/en/mlflow/build-dashboards)

note

Starting March 27, 2024, MLflow imposes a quota limit on the number of total parameters, tags, and metric steps for all existing and new runs, and the number of total runs for all existing and new experiments, see [Resource limits](https://docs.databricks.com/aws/en/resources/limits). If you hit the runs per experiment quota, Databricks recommends you delete runs that you no longer need [using the delete runs API in Python](https://docs.databricks.com/aws/en/mlflow/runs#bulk-delete). If you hit other quota limits, Databricks recommends adjusting your logging strategy to keep under the limit. If you require an increase to this limit, reach out to your Databricks account team with a brief explanation of your use case, why the suggested mitigation approaches do not work, and the new limit you request.

## MLflow tracking API[​](#mlflow-tracking-api "Direct link to MLflow tracking API")

The [MLflow Tracking API](https://www.mlflow.org/docs/latest/tracking.html) logs parameters, metrics, tags, and artifacts from a model run. The Tracking API communicates with an MLflow [tracking server](https://www.mlflow.org/docs/latest/tracking.html#tracking-server). When you use Databricks, a Databricks-hosted tracking server logs the data. The hosted MLflow tracking server has Python, Java, and R APIs.

MLflow is pre-installed on Databricks Runtime ML clusters. To use MLflow on a Databricks Runtime cluster, you must install the `mlflow` library. For instructions on installing a library onto a cluster, see [Install a library on a cluster](https://docs.databricks.com/aws/en/libraries/cluster-libraries#install-libraries). To use MLflow 3 and its state-of-the-art tracking capabilities, make sure to upgrade to the latest version (see [Install MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install#install-mlflow-3)).

## Where MLflow runs are logged[​](#where-mlflow-runs-are-logged "Direct link to where-mlflow-runs-are-logged")

Databricks provides a hosted MLflow tracking server that stores your experiment data in your workspace with no setup required. You can also configure MLflow to use different tracking servers when needed.

MLflow tracking is controlled by two settings:

*   **Tracking URI**: Determines which server to use (defaults to current Databricks workspace)
*   **Experiment**: Determines which experiment in that server to log to

Python

    import mlflow# By default MLflow logs to the Databricks-hosted workspace tracking server. You can connect to a different server using the tracking URI.mlflow.set_tracking_uri("databricks://remote-workspace-url")# Set experiment in the tracking servermlflow.set_experiment("/Shared/my-experiment")

If no active experiment is set, runs are logged to the [notebook experiment](https://docs.databricks.com/aws/en/mlflow/experiments#mlflow-notebook-experiments).

For more information about controlling where your MLflow data is stored, see [Choose where your MLflow data is stored](https://docs.databricks.com/aws/en/mlflow/tracking-server-configuration).

## Log runs and models to an experiment[​](#log-runs-and-models-to-an-experiment "Direct link to log-runs-and-models-to-an-experiment")

MLflow can automatically log training code written in many machine learning and deep learning frameworks. This is the easiest way to get started using MLflow tracking. See the [example notebook](#autologging).

For more control over which parameters and metrics are logged, or to log additional artifacts such as CSV files or plots, use the MLflow logging API. See the [example notebook](#logging-api).

### Use autologging to track model development[​](#use-autologging-to-track-model-development "Direct link to use-autologging-to-track-model-development")

This example notebook shows how to use autologging with [scikit-learn](https://scikit-learn.org/stable/index.html). For information about autologging with other Python libraries, see [the MLflow autologging documentation](https://mlflow.org/docs/latest/tracking/autolog.html?highlight=autolog#supported-libraries).

*   MLflow 3
*   MLflow 2.x

#### MLflow autologging Python notebook for MLflow 3

### Use the logging API to track model development[​](#use-the-logging-api-to-track-model-development "Direct link to use-the-logging-api-to-track-model-development")

This example notebook shows how to use the [Python logging API](https://mlflow.org/docs/latest/python_api/index.html). MLflow also has [REST, R, and Java APIs](https://mlflow.org/docs/latest/tracking.html).

*   MLflow 3
*   MLflow 2.x

#### MLflow logging API Python notebook for MLflow 3

### Log runs to a workspace experiment[​](#log-runs-to-a-workspace-experiment "Direct link to Log runs to a workspace experiment")

By default, when you train a model in a Databricks notebook, runs are logged to the notebook experiment. Only MLflow runs initiated within a notebook can be logged to the notebook experiment.

MLflow runs launched from any notebook or from the APIs can be logged to a workspace experiment. To log runs to a workspace experiment, use code similar to the following in your notebook or API call:

Python

    experiment_name = "/Shared/name_of_experiment/"mlflow.set_experiment(experiment_name)

For instructions on creating a workspace experiment, see [Create workspace experiment](https://docs.databricks.com/aws/en/mlflow/experiments#workspace-expt). For information about viewing logged runs, see [View notebook experiment](https://docs.databricks.com/aws/en/mlflow/experiments#view-notebook-experiment) and [View workspace experiment](https://docs.databricks.com/aws/en/mlflow/experiments#view-workspace-experiment).

## Analyze MLflow runs programmatically[​](#analyze-mlflow-runs-programmatically "Direct link to analyze-mlflow-runs-programmatically")

You can access MLflow run data programmatically using the following two DataFrame APIs:

*   The MLflow Python client [search\_runs API](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.search_runs) returns a pandas DataFrame.
*   The [Read MLflow experiments](https://docs.databricks.com/aws/en/query/formats/mlflow-experiment) data source returns an Apache Spark DataFrame.

This example demonstrates how to use the MLflow Python client to build a dashboard that visualizes changes in evaluation metrics over time, tracks the number of runs started by a specific user, and measures the total number of runs across all users:

*   [Build dashboards with MLflow metadata in system tables](https://docs.databricks.com/aws/en/mlflow/build-dashboards)

## Why model training metrics and outputs may vary[​](#why-model-training-metrics-and-outputs-may-vary "Direct link to Why model training metrics and outputs may vary")

Many of the algorithms used in ML have a random element, such as sampling or random initial conditions within the algorithm itself. When you train a model using one of these algorithms, the results might not be the same with each run, even if you start the run with the same conditions. Many libraries offer a seeding mechanism to fix the initial conditions for these stochastic elements. However, there may be other sources of variation that are not controlled by seeds. Some algorithms are sensitive to the order of the data, and distributed ML algorithms may also be affected by how the data is partitioned. This variation is not significant and not important in the model development process.

To control variation caused by differences in ordering and partitioning, use the PySpark functions [repartition](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.repartition.html) and [sortWithinPartitions](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.sortWithinPartitions.html).

## MLflow tracking examples[​](#mlflow-tracking-examples "Direct link to mlflow-tracking-examples")

The following notebooks demonstrate how to track model development using MLflow.

*   [Tutorial: End-to-end classic ML models on Databricks](https://docs.databricks.com/aws/en/mlflow/end-to-end-example)
*   [Track Keras model training with MLflow](https://mlflow.org/docs/latest/deep-learning/keras/quickstart/quickstart_keras.html)
