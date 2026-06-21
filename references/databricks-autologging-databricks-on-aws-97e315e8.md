---
title: Databricks Autologging | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/databricks-autologging
ingestedAt: "2026-06-18T08:13:55.707Z"
---

This page covers how to customize [Databricks Autologging](#), which automatically captures model parameters, metrics, files, and lineage information when you train models from a variety of popular machine learning libraries. Training sessions are recorded as [MLflow tracking runs](https://docs.databricks.com/aws/en/mlflow/tracking). Model files are also tracked so you can easily log them to the [MLflow Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).

note

To enable trace logging for generative AI workloads, MLflow supports [OpenAI autologging](https://mlflow.org/docs/latest/llms/openai/autologging.html).

The following video shows Databricks Autologging with a scikit-learn model training session in an interactive Python notebook. Tracking information is automatically captured and displayed in the Experiment Runs sidebar and in the MLflow UI.

![Autologging example](https://docs.databricks.com/aws/en/assets/images/autologging-example-c01545935da4acfc2edff5916f419e07.gif)

## Requirements[​](#requirements "Direct link to Requirements")

*   Databricks Autologging is generally available in all regions with Databricks Runtime 10.4 LTS ML or above.
*   Databricks Autologging is available in select preview regions with Databricks Runtime 9.1 LTS ML or above.

## How it works[​](#how-it-works "Direct link to How it works")

When you attach an interactive Python notebook to a Databricks cluster, Databricks Autologging calls [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) to set up tracking for your model training sessions. When you train models in the notebook, model training information is automatically tracked with [MLflow Tracking](https://docs.databricks.com/aws/en/mlflow/tracking). For information about how this model training information is secured and managed, see [Security and data management](#security-and-data-management).

note

Autologging is not automatically enabled on serverless compute. For serverless compute clusters, you must explicitly call [`mlflow.autolog()`](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) to enable autologging functionality.

The default configuration for the [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) call is:

Python

    mlflow.autolog(    log_input_examples=False,    log_model_signatures=True,    log_models=True,    disable=False,    exclusive=False,    disable_for_unsupported_versions=True,    silent=False)

You can [customize the autologging configuration](#customize-logging-behavior).

## Usage[​](#usage "Direct link to Usage")

To use Databricks Autologging, train a machine learning model in a [supported framework](#supported-environments-and-frameworks) using an interactive Databricks Python notebook. Databricks Autologging automatically records model lineage information, parameters, and metrics to [MLflow Tracking](https://docs.databricks.com/aws/en/mlflow/tracking). You can also [customize the behavior of Databricks Autologging](#customize-logging-behavior).

note

Databricks Autologging is not applied to runs created using the [MLflow fluent API](https://www.mlflow.org/docs/latest/python_api/mlflow.html) with `mlflow.start_run()`. In these cases, you must call `mlflow.autolog()` to save autologged content to the MLflow run. See [Track additional content](#track-additional-content).

### Customize logging behavior[​](#customize-logging-behavior "Direct link to Customize logging behavior")

To customize logging, use [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog). This function provides configuration parameters to enable model logging (`log_models`), log datasets (`log_datasets`), collect input examples (`log_input_examples`), log model signatures (`log_model_signatures`), configure warnings (`silent`), and more.

### Track additional content[​](#track-additional-content "Direct link to Track additional content")

To track additional metrics, parameters, files, and metadata with MLflow runs created by Databricks Autologging, follow these steps in a Databricks interactive Python notebook:

1.  Call [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) with `exclusive=False`.
2.  Start an MLflow run using [mlflow.start\_run()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.start_run). You can wrap this call in `with mlflow.start_run()`; when you do this, the run is ended automatically after it completes.
3.  Use [MLflow Tracking methods](https://mlflow.org/docs/latest/python_api/mlflow.html), such as [mlflow.log\_param()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_param), to track pre-training content.
4.  Train one or more machine learning models in a framework supported by Databricks Autologging.
5.  Use [MLflow Tracking methods](https://mlflow.org/docs/latest/python_api/mlflow.html), such as [mlflow.log\_metric()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.log_metric), to track post-training content.
6.  If you did not use `with mlflow.start_run()` in Step 2, end the MLflow run using [mlflow.end\_run()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.end_run).

For example:

Python

    import mlflowmlflow.autolog(exclusive=False)with mlflow.start_run():  mlflow.log_param("example_param", "example_value")  # <your model training code here>  mlflow.log_metric("example_metric", 5)

### Disable Databricks Autologging[​](#disable-databricks-autologging "Direct link to Disable Databricks Autologging")

To disable Databricks Autologging in a Databricks interactive Python notebook, call [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) with `disable=True`:

Python

    import mlflowmlflow.autolog(disable=True)

Administrators can also disable Databricks Autologging for all clusters in a workspace from the **Advanced** tab of the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings). Clusters must be restarted for this change to take effect.

## Supported environments and frameworks[​](#supported-environments-and-frameworks "Direct link to Supported environments and frameworks")

Databricks Autologging is supported in interactive Python notebooks and is available for the following ML frameworks:

*   scikit-learn
*   Apache Spark MLlib
*   TensorFlow
*   Keras
*   PyTorch Lightning
*   XGBoost
*   LightGBM
*   Gluon
*   Fast.ai
*   statsmodels
*   PaddlePaddle
*   [OpenAI](https://mlflow.org/docs/latest/llms/openai/autologging.html)
*   [LangChain](https://mlflow.org/docs/latest/llms/langchain/autologging.html)

For more information about each of the supported frameworks, see [MLflow automatic logging](https://mlflow.org/docs/latest/tracking/autolog.html).

## MLflow Tracing enablement[​](#mlflow-tracing-enablement "Direct link to MLflow Tracing enablement")

MLflow Tracing utilizes the `autolog` feature within respective model framework integrations to control the enabling or disabling of tracing support for integrations that support tracing.

For example, to enable tracing when using a LlamaIndex model, utilize [mlflow.llama\_index.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.llama_index.html#mlflow.llama_index.autolog) with `log_traces=True`:

Python

    import mlflowmlflow.llama_index.autolog(log_traces=True)

note

For serverless compute clusters, autologging for tracing is not automatically enabled. You must explicitly enable autologging for the specific framework integrations you want to trace (for example, `mlflow.openai.autolog()` or `mlflow.langchain.autolog()`).

The supported integrations that have trace enablement within their autolog implementations are:

*   [OpenAI](https://mlflow.org/docs/latest/python_api/openai/index.html#mlflow.openai.autolog)
*   [LangChain](https://mlflow.org/docs/latest/python_api/mlflow.langchain.html#mlflow.langchain.autolog)
*   [LangGraph](https://mlflow.org/docs/latest/python_api/mlflow.langchain.html#mlflow.langchain.autolog)
*   [LlamaIndex](https://mlflow.org/docs/latest/python_api/mlflow.llama_index.html#mlflow.llama_index.autolog)
*   [AutoGen](https://mlflow.org/docs/latest/python_api/mlflow.autogen.html#mlflow.autogen.autolog)

## Security and data management[​](#security-and-data-management "Direct link to Security and data management")

All model training information tracked with Databricks Autologging is stored in MLflow Tracking and is secured by [MLflow Experiment permissions](https://docs.databricks.com/aws/en/security/auth/access-control/#experiments). You can share, modify, or delete model training information using the [MLflow Tracking](https://docs.databricks.com/aws/en/mlflow/tracking) API or UI.

## Administration[​](#administration "Direct link to Administration")

Administrators can enable or disable Databricks Autologging for all interactive notebook sessions across their workspace in the **Advanced** tab of the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings). Changes do not take effect until the cluster is restarted.

## Limitations[​](#limitations "Direct link to Limitations")

*   Databricks Autologging is enabled only on the driver node of your Databricks cluster. To use autologging from worker nodes, you must explicitly call [mlflow.autolog()](https://mlflow.org/docs/latest/python_api/mlflow.html#mlflow.autolog) from within the code executing on each worker.
*   The XGBoost scikit-learn integration is not supported.

## Apache Spark MLlib, Hyperopt, and automated MLflow tracking[​](#apache-spark-mllib-hyperopt-and-automated-mlflow-tracking "Direct link to Apache Spark MLlib, Hyperopt, and automated MLflow tracking")

Databricks Autologging does not change the behavior of existing automated MLflow tracking integrations for [Apache Spark MLlib](https://docs.databricks.com/aws/en/archive/machine-learning/mllib-mlflow-integration) and [Hyperopt](https://docs.databricks.com/aws/en/machine-learning/automl-hyperparam-tuning/hyperopt-spark-mlflow-integration).

note

In Databricks Runtime 10.1 ML, disabling the automated MLflow tracking integration for Apache Spark MLlib `CrossValidator` and `TrainValidationSplit` models also disables the Databricks Autologging feature for all Apache Spark MLlib models.
