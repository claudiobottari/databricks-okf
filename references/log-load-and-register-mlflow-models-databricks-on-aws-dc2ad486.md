---
title: Log, load, and register MLflow models | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/models
ingestedAt: "2026-06-18T08:14:13.363Z"
---

An MLflow [Model](https://mlflow.org/docs/latest/models.html) is a standard format for packaging machine learning models that can be used in a variety of downstream tools—for example, batch inference on Apache Spark or real-time serving through a REST API. The format defines a convention that lets you save a model in different [flavors](https://www.mlflow.org/docs/latest/models.html#built-in-model-flavors) (python-function, pytorch, sklearn, and so on), that can be understood by different model [serving and inference platforms](https://www.mlflow.org/docs/latest/models.html#built-in-deployment-tools).

To learn how to log and score a streaming model, see [How to save and load a streaming model](https://mlflow.org/docs/latest/models.html#demonstrating-predict-stream).

[MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) introduces significant enhancements to MLflow models by introducing a new, dedicated `LoggedModel` object with its own metadata such as metrics and parameters. For more details, see [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).

## Log and load models[​](#log-and-load-models "Direct link to log-and-load-models")

When you log a model, MLflow automatically logs `requirements.txt` and `conda.yaml` files. You can use these files to recreate the model development environment and reinstall dependencies using `virtualenv` (recommended) or `conda`.

important

Anaconda Inc. updated their [terms of service](https://www.anaconda.com/terms-of-service) for anaconda.org channels. Based on the new terms of service you may require a commercial license if you rely on Anaconda's packaging and distribution. See [Anaconda Commercial Edition FAQ](https://www.anaconda.com/blog/anaconda-commercial-edition-faq) for more information. Your use of any Anaconda channels is governed by their terms of service.

MLflow models logged before [v1.18](https://mlflow.org/news/2021/06/18/1.18.0-release/index.html) (Databricks Runtime 8.3 ML or earlier) were by default logged with the conda `defaults` channel ([https://repo.anaconda.com/pkgs/](https://repo.anaconda.com/pkgs/)) as a dependency. Because of this license change, Databricks has stopped the use of the `defaults` channel for models logged using MLflow v1.18 and above. The default channel logged is now `conda-forge`, which points at the community managed [https://conda-forge.org/](https://conda-forge.org/).

If you logged a model before MLflow v1.18 without excluding the `defaults` channel from the conda environment for the model, that model may have a dependency on the `defaults` channel that you may not have intended. To manually confirm whether a model has this dependency, you can examine `channel` value in the `conda.yaml` file that is packaged with the logged model. For example, a model's `conda.yaml` with a `defaults` channel dependency may look like this:

YAML

    channels:- defaultsdependencies:- python=3.8.8- pip- pip:    - mlflow    - scikit-learn==0.23.2    - cloudpickle==1.6.0      name: mlflow-env

Because Databricks can not determine whether your use of the Anaconda repository to interact with your models is permitted under your relationship with Anaconda, Databricks is not forcing its customers to make any changes. If your use of the Anaconda.com repo through the use of Databricks is permitted under Anaconda's terms, you do not need to take any action.

If you would like to change the channel used in a model's environment, you can re-register the model to the model registry with a new `conda.yaml`. You can do this by specifying the channel in the `conda_env` parameter of `log_model()`.

For more information on the `log_model()` API, see the MLflow documentation for the model flavor you are working with, for example, [log\_model for scikit-learn](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model).

For more information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files).

### API commands[​](#api-commands "Direct link to API commands")

To log a model to the MLflow [tracking server](https://docs.databricks.com/aws/en/mlflow/tracking), use `mlflow.<model-type>.log_model(model, ...)`.

To load a previously logged model for inference or further development, use `mlflow.<model-type>.load_model(modelpath)`, where `modelpath` is one of the following:

*   a model path (such as `models:/{model_id}`) ([MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) only)
*   a run-relative path (such as `runs:/{run_id}/{model-path}`)
*   a Unity Catalog volumes path (such as `dbfs:/Volumes/catalog_name/schema_name/volume_name/{path_to_artifact_root}/{model_path}`)
*   an MLflow-managed artifact storage path beginning with `dbfs:/databricks/mlflow-tracking/`
*   a [registered model](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry) path (such as `models:/{model_name}/{model_stage}`).

For a complete list of options for loading MLflow models, see [Referencing Artifacts in the MLflow documentation](https://www.mlflow.org/docs/latest/tracking/artifacts-stores/).

For Python MLflow models, an additional option is to use `mlflow.pyfunc.load_model()` to load the model as a generic Python function.

You can use the following code snippet to load the model and score data points.

Python

    model = mlflow.pyfunc.load_model(model_path)model.predict(model_input)

As an alternative, you can export the model as an Apache Spark UDF to use for scoring on a Spark cluster, either as a batch job or as a real-time [Spark Streaming](https://docs.databricks.com/aws/en/structured-streaming/concepts) job.

Python

    # load input data table as a Spark DataFrameinput_data = spark.table(input_table_name)model_udf = mlflow.pyfunc.spark_udf(spark, model_path)df = input_data.withColumn("prediction", model_udf())

### Log model dependencies[​](#log-model-dependencies "Direct link to Log model dependencies")

To accurately load a model, you should make sure the model dependencies are loaded with the correct versions into the notebook environment. In Databricks Runtime 10.5 ML and above, MLflow warns you if a mismatch is detected between the current environment and the model's dependencies.

Additional functionality to simplify restoring model dependencies is included in Databricks Runtime 11.0 ML and above. In Databricks Runtime 11.0 ML and above, for `pyfunc` flavor models, you can call `mlflow.pyfunc.get_model_dependencies` to retrieve and download the model dependencies. This function returns a path to the dependencies file which you can then install by using `%pip install <file-path>`. When you load a model as a PySpark UDF, specify `env_manager="virtualenv"` in the `mlflow.pyfunc.spark_udf` call. This restores model dependencies in the context of the PySpark UDF and does not affect the outside environment.

You can also use this functionality in Databricks Runtime 10.5 or below by manually installing [MLflow version 1.25.0 or above](https://www.mlflow.org/docs/latest/index.html):

Python

    %pip install "mlflow>=1.25.0"

For additional information on how to log model dependencies (Python and non-Python) and artifacts, see [Log model dependencies](https://docs.databricks.com/aws/en/mlflow/log-model-dependencies).

Learn how to log model dependencies and custom artifacts for model serving:

*   [Deploy models with dependencies](https://docs.databricks.com/aws/en/mlflow/log-model-dependencies#deploy-dependencies)
*   [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving)
*   [Package custom artifacts for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-custom-artifacts)

*   [Log model dependencies](https://docs.databricks.com/aws/en/mlflow/log-model-dependencies)
*   [Databricks Autologging](https://docs.databricks.com/aws/en/mlflow/databricks-autologging)

### Automatically generated code snippets in the MLflow UI[​](#-automatically-generated-code-snippets-in-the-mlflow-ui "Direct link to -automatically-generated-code-snippets-in-the-mlflow-ui")

When you log a model in a Databricks notebook, Databricks automatically generates code snippets that you can copy and use to load and run the model. To view these code snippets:

1.  Navigate to the Runs screen for the run that generated the model. (See [View notebook experiment](https://docs.databricks.com/aws/en/mlflow/experiments#view-notebook-experiment) for how to display the Runs screen.)
2.  Scroll to the **Artifacts** section.
3.  Click the name of the logged model. A panel opens to the right showing code you can use to load the logged model and make predictions on Spark or pandas DataFrames.

![Artifact panel code snippets](https://docs.databricks.com/aws/en/assets/images/code-snippets-8a4c2cdbac138567636e4ff5c38f6b7b.png)

### Examples[​](#examples "Direct link to Examples")

For examples of logging models, see the examples in [Track machine learning training runs examples](https://docs.databricks.com/aws/en/mlflow/tracking#tracking-examples).

## Register models in the Model Registry[​](#register-models-in-the-model-registry "Direct link to register-models-in-the-model-registry")

You can register models in the MLflow Model Registry, a centralized model store that provides a UI and set of APIs to manage the full lifecycle of MLflow Models. For instructions on how to use the Model Registry to manage models in Databricks Unity Catalog, see [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/). To use the Workspace Model Registry, see [Manage model lifecycle using the Workspace Model Registry (legacy)](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry).

When models created with [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) are registered to the Unity Catalog model registry, you can view data such as parameters and metrics in one central location, across all experiments and workspaces. For information, see [Model Registry improvements with MLflow 3](https://docs.databricks.com/aws/en/mlflow/model-registry-3).

To register a model using the API, use the following command:

*   MLflow 3
*   MLflow 2.x

Python

    mlflow.register_model("models:/{model_id}", "{registered_model_name}")

## Save models to Unity Catalog volumes[​](#save-models-to-unity-catalog-volumes "Direct link to Save models to Unity Catalog volumes")

To save a model locally, use `mlflow.<model-type>.save_model(model, modelpath)`. `modelpath` must be a [Unity Catalog volumes](https://docs.databricks.com/aws/en/volumes/) path. For example, if you use a Unity Catalog volumes location `dbfs:/Volumes/catalog_name/schema_name/volume_name/my_project_models` to store your project work, you must use the model path `/dbfs/Volumes/catalog_name/schema_name/volume_name/my_project_models`:

Python

    modelpath = "/dbfs/Volumes/catalog_name/schema_name/volume_name/my_project_models/model-%f-%f" % (alpha, l1_ratio)mlflow.sklearn.save_model(lr, modelpath)

For MLlib models, use [ML Pipelines](https://spark.apache.org/docs/latest/ml-pipeline.html#ml-persistence-saving-and-loading-pipelines).

## Download model artifacts[​](#download-model-artifacts "Direct link to Download model artifacts")

You can download the logged model artifacts (such as model files, plots, and metrics) for a registered model with various APIs.

[Python API](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.artifacts.html#mlflow.artifacts.download_artifacts) example:

Python

    mlflow.set_registry_uri("databricks-uc")mlflow.artifacts.download_artifacts(f"models:/{model_name}/{model_version}")

[Java API](https://mlflow.org/docs/latest/java_api/org/mlflow/tracking/MlflowClient.html#downloadModelVersion-java.lang.String-java.lang.String-) example:

Java

    MlflowClient mlflowClient = new MlflowClient();// Get the model URI for a registered model version.String modelURI = mlflowClient.getModelVersionDownloadUri(modelName, modelVersion);// Or download the model artifacts directly.File modelFile = mlflowClient.downloadModelVersion(modelName, modelVersion);

[CLI command](https://www.mlflow.org/docs/latest/cli.html#mlflow-artifacts-download) example:

    mlflow artifacts download --artifact-uri models:/<name>/<version|stage>

## Deploy models for online serving[​](#deploy-models-for-online-serving "Direct link to Deploy models for online serving")

note

Prior to deploying your model, it is beneficial to verify that the model is capable of being served. See the MLflow documentation for how you can use `mlflow.models.predict` to [validate models before deployment](https://www.mlflow.org/docs/latest/models.html#validate-models-before-deployment).

Use [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) to host machine learning models registered in Unity Catalog model registry as REST endpoints. These endpoints are updated automatically based on the availability of model versions.
