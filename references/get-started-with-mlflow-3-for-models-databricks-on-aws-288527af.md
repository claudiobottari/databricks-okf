---
title: Get started with MLflow 3 for models | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/mlflow-3-install
ingestedAt: "2026-06-18T08:14:06.673Z"
---

note

This article focuses on MLflow 3 features for traditional machine learning and deep learning models. MLflow 3 also offers comprehensive features for GenAI application development including tracing, evaluation, and human feedback collection. See [MLflow 3 for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/) for details.

This article gets you started with MLflow 3 for developing machine learning models. It describes how to install MLflow 3 for models and includes several demo notebooks to get started. It also includes links to pages that cover the new features of MLflow 3 for models in more detail.

## What is MLflow 3 for models?[​](#what-is-mlflow-3-for-models "Direct link to What is MLflow 3 for models?")

MLflow 3 for models on Databricks delivers state-of-the-art experiment tracking, performance evaluation, and production management for machine learning models. MLflow 3 introduces significant new capabilities while preserving core tracking concepts, making migration from MLflow 2.x quick and simple.

## What is MLflow 3 for GenAI?[​](#what-is-mlflow-3-for-genai "Direct link to What is MLflow 3 for GenAI?")

Beyond MLflow 3 for Models, MLflow 3 for GenAI introduces a wide variety of new features and improvements for agent and GenAI application development. For a comprehensive overview, see [MLflow 3 for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/).

Core features in MLflow 3 for GenAI include:

*   **[Tracing and observability](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)** - End-to-end observability for GenAI applications with automatic instrumentation for 20+ frameworks including OpenAI, LangChain, LlamaIndex, and Anthropic
*   **[Evaluation and monitoring](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/)** - Comprehensive GenAI evaluation capabilities to measure and improve quality from development through production. Includes built-in LLM judges, customizable judges, evaluation dataset management, and real-time monitoring.
*   **[Human feedback collection](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/)** - Customizable Review UI for collecting domain expert feedback and interactively testing agents, with structured [labeling sessions](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-sessions) for organizing and tracking review progress
*   **[Prompt Registry](https://docs.databricks.com/aws/en/mlflow3/genai/prompt-version-mgmt/prompt-registry/)** - Centralized prompt versioning, management, and A/B testing with Unity Catalog integration

## How is MLflow 3 for models different from MLflow 2[​](#how-is-mlflow-3-for-models-different-from-mlflow-2 "Direct link to How is MLflow 3 for models different from MLflow 2")

MLflow 3 for models on Databricks enables you to:

*   Centrally track and analyze the performance of your models across all environments, from interactive queries in a development notebook through production batch or real-time serving deployments.

![Model tracking UI.](https://docs.databricks.com/aws/en/assets/images/mlflow-model-tracking-ui-719f2224cc10087b4371b8d4496c066a.png)

*   View and access model metrics and parameters from the model version page in Unity Catalog and from the REST API, across all workspaces and experiments.

![Model version page in Unity Catalog showing metrics from multiple runs.](https://docs.databricks.com/aws/en/assets/images/uc-model-version-page-674574ad9423349aee3915e8a7a92e3d.png)

*   Orchestrate evaluation and deployment workflows using Unity Catalog and access comprehensive status logs for each version of your model.

![A complex deployment job that includes staged rollout and metrics collection.](https://docs.databricks.com/aws/en/assets/images/complex-deployment-job-9ea629abdeae12c52b0fd7f079d78a7e.png)

These capabilities simplify and streamline machine learning model development, evaluation, and production deployment.

### Logged Models[​](#logged-models "Direct link to Logged Models")

Much of the new functionality of MLflow 3 derives from the new concept of a `LoggedModel`. For deep learning and traditional machine learning models, `LoggedModels` elevates the concept of a model produced by a training run, establishing it as a dedicated object to track the model lifecycle across different training and evaluation runs.

`LoggedModels` capture metrics, parameters, and traces across phases of development (training and evaluation) and across environments (development, staging, and production). When a `LoggedModel` is promoted to Unity Catalog as a Model Version, all performance data from the original `LoggedModel` becomes visible on the UC Model Version page, providing visibility across all workspaces and experiments. For more details, see [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).

### Deployment jobs[​](#deployment-jobs "Direct link to Deployment jobs")

MLflow 3 also introduces the concept of a deployment job. Deployment jobs use Lakeflow Jobs to manage the model lifecycle, including steps like evaluation, approval, and deployment. These model workflows are governed by Unity Catalog, and all events are saved to an activity log that is available on the model version page in Unity Catalog.

## Migrating from MLflow 2.x[​](#migrating-from-mlflow-2x "Direct link to Migrating from MLflow 2.x")

Although there are many new features in MLflow 3, the core concepts of experiments and runs, along with their metadata such as parameters, tags, and metrics, all remain the same. Migration from MLflow 2.x to 3.0 is very straightforward and should require minimal code changes in most cases. This section highlights some key differences from MLflow 2.x and what you should be aware of for a seamless transition.

### Logging Models[​](#logging-models "Direct link to Logging Models")

When logging models in 2.x, the `artifact_path` parameter is used.

    with mlflow.start_run():    mlflow.pyfunc.log_model(        artifact_path="model",        python_model=python_model,        ...    )

In MLflow 3, use `name` instead, which allows the model to later be searched by name. The `artifact_path` parameter is still supported but has been deprecated. Additionally, MLflow no longer requires a run to be active when logging a model, because models have become first-class citizens in MLflow 3. You can directly log a model without first starting a run.

    mlflow.pyfunc.log_model(    name="model",    python_model=python_model,    ...)

### Model artifacts[​](#model-artifacts "Direct link to Model artifacts")

In MLflow 2.x, model artifacts are stored as run artifacts under the run's artifact path. In MLflow 3, model artifacts are now stored in a different location, under the model's artifact path instead.

    # MLflow 2.xexperiments/  └── <experiment_id>/    └── <run_id>/      └── artifacts/        └── ... # model artifacts are stored here# MLflow 3experiments/  └── <experiment_id>/    └── models/      └── <model_id>/        └── artifacts/          └── ... # model artifacts are stored here

It is recommended to load models with `mlflow.<model-flavor>.load_model` using the model URI returned by `mlflow.<model-flavor>.log_model` to avoid any issues. This model URI is of the format `models:/<model_id>` (rather than `runs:/<run_id>/<artifact_path>` as in MLflow 2.x) and can also be constructed manually if only the model ID is available.

### Model registry[​](#model-registry "Direct link to Model registry")

In MLflow 3, the default registry URI is now `databricks-uc`, meaning the MLflow Model Registry in Unity Catalog will be used (see [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) for more details). The names of models registered in Unity Catalog are of the form `<catalog>.<schema>.<model>`. When calling APIs that require a registered model name, such as `mlflow.register_model`, this full, three-level name is used.

For workspaces that have Unity Catalog enabled and whose [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is in Unity Catalog, you can also use `<model>` as the name and the default catalog and schema will be inferred (no change in behavior from MLflow 2.x). If your workspace has Unity Catalog enabled but its [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is not configured to be in Unity Catalog, you will need to specify the full three-level name.

Databricks recommends using the MLflow Model Registry in Unity Catalog for managing the lifecycle of your models.

If you want to continue using the [Workspace Model Registry (legacy)](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry), use one of the following methods to set the registry URI to `databricks`:

*   Use `mlflow.set_registry_uri("databricks")`.
*   Set the environment variable [MLFLOW\_REGISTRY\_URI](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.environment_variables.html#mlflow.environment_variables.MLFLOW_REGISTRY_URI).
*   To set the environment variable for registry URI at scale, you can use [init scripts](https://docs.databricks.com/aws/en/init-scripts/). This requires [all-purpose compute](https://docs.databricks.com/aws/en/compute/).

### Other important changes[​](#other-important-changes "Direct link to Other important changes")

*   MLflow 3 clients can load all runs, models, and traces logged with MLflow 2.x clients. However, the reverse is not necessarily true, so models and traces logged with MLflow 3 clients may not be able to be loaded with older 2.x client versions.
*   The `mlflow.evaluate` API has been deprecated. For traditional ML or deep learning models, use `mlflow.models.evaluate` which maintains full compatibility with the original `mlflow.evaluate` API. For LLMs or GenAI applications, use the `mlflow.genai.evaluate` API instead.
*   The `run_uuid` attribute has been removed from the `RunInfo` object. Use `run_id` instead in your code.

## Install MLflow 3[​](#install-mlflow-3 "Direct link to Install MLflow 3")

To use MLflow 3, you must update the package to use the correct (>= 3.0) version. The following lines of code must be executed each time a notebook is run:

Python

    %pip install mlflow>=3.0 --upgradedbutils.library.restartPython()

## Example notebooks[​](#example-notebooks "Direct link to Example notebooks")

The following pages illustrate the MLflow 3 model tracking workflow for traditional ML and deep learning. Each page includes an example notebook.

*   [MLflow 3 traditional ML workflow](https://docs.databricks.com/aws/en/mlflow/mlflow3-ml-workflow).
*   [MLflow 3 deep learning workflow](https://docs.databricks.com/aws/en/mlflow/mlflow3-dl-workflow).

## Limitation[​](#limitation "Direct link to Limitation")

While Spark model logging (`mlflow.spark.log_model`) continues to work in MLflow 3, it does not use the new `LoggedModel` concept. Models logged using Spark model logging continue to use MLflow 2.x runs and run artifacts.

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about the new features of MLflow 3, see the following articles:

*   [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).
*   [Model Registry improvements with MLflow 3](https://docs.databricks.com/aws/en/mlflow/model-registry-3).
*   [MLflow 3 deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job).
