---
title: Log model dependencies | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/log-model-dependencies
ingestedAt: "2026-06-18T08:14:03.422Z"
---

In this article, you learn how to log a model and its dependencies as model artifacts, so they are available in your environment for production tasks like model serving.

## Log Python package model dependencies[​](#log-python-package-model-dependencies "Direct link to Log Python package model dependencies")

MLflow has native support for some Python ML libraries, where MLflow can reliably log dependencies for models that use these libraries. See [built-in model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors).

For example, MLflow supports scikit-learn in the [mlflow.sklearn module](https://mlflow.org/docs/latest/python_api/mlflow.sklearn.html), and the command [mlflow.sklearn.log\_model](https://mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model) logs the sklearn version. The same applies for [autologging](https://mlflow.org/docs/latest/tracking.html#automatic-logging) with those ML libraries. See the [MLflow github repository](https://github.com/mlflow/mlflow/tree/master/examples) for additional examples.

note

To enable trace logging for generative AI workloads, MLflow supports [OpenAI autologging](https://mlflow.org/docs/latest/llms/openai/autologging.html).

For ML libraries that can be installed with `pip install PACKAGE_NAME==VERSION`, but do not have built-in MLflow model flavors, you can log those packages using the [mlflow.pyfunc.log\_model](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model) method. Be sure to log the requirements with the exact library version, for example, `f"nltk=={nltk.__version__}"` instead of just `nltk`.

`mlflow.pyfunc.log_model` supports logging for:

*   Public and custom libraries packaged as Python egg or Python wheel files.
*   Public packages on PyPI and privately hosted packages on your own PyPI server.

With [mlflow.pyfunc.log\_model](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model), MLflow tries to infer the dependencies automatically. MLflow infers the dependencies using [mlflow.models.infer\_pip\_requirements](https://www.mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.infer_pip_requirements), and logs them to a `requirements.txt` file as a model artifact.

In older versions, MLflow sometimes doesn't identify all Python requirements automatically, especially if the library isn't a built-in model flavor. In these cases, you can specify additional dependencies with the `extra_pip_requirements` parameter in the `log_model` command. See an example of using the [extra\_pip\_requirements parameter](https://www.mlflow.org/docs/latest/model/dependencies.html#adding-extra-dependencies-to-an-mlflow-model).

important

You can also overwrite the entire set of requirements with the `conda_env` and `pip_requirements` parameters, but doing so is generally discouraged because this overrides the dependencies which MLflow picks up automatically. See an example of how to use the [`pip_requirements` parameter to overwrite requirements](https://www.mlflow.org/docs/latest/model/dependencies.html).

### Customized model logging[​](#customized-model-logging "Direct link to Customized model logging")

For scenarios where more customized model logging is necessary, you can either:

*   Write a [custom Python model](https://mlflow.org/docs/latest/models.html#custom-python-models). Doing so allows you to subclass `mlflow.pyfunc.PythonModel` to customize initialization and prediction. This approach works well for customization of Python-only models.
    *   For a simple example, see the [add N model example](https://mlflow.org/docs/latest/models.html#example-creating-a-custom-add-n-model).
    *   For a more complex example, see the custom [XGBoost model example](https://mlflow.org/docs/latest/models.html#example-saving-an-xgboost-model-in-mlflow-format).
*   Write a [custom flavor](https://mlflow.org/docs/latest/models.html#custom-flavors). In this scenario, you can customize logging more than the generic `pyfunc` flavor, but doing so requires more work to implement.

### Custom Python code[​](#custom-python-code "Direct link to Custom Python code")

You may have Python code dependencies that can't be installed using the `%pip install` command, such as one or more `.py` files.

When logging a model, you can tell MLflow that the model can find those dependencies at a specified path by using the `code_paths` parameter (or `code_path` in MLflow 2.x) in [mlflow.pyfunc.log\_model](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model). MLflow stores any files or directories passed using `code_paths` or `code_path` as artifacts along with the model in a code directory. When loading the model, MLflow adds these files or directories to the Python path. This route also works with custom Python wheel files, which can be included in the model using `code_paths` or `code_path`, just like `.py` files.

*   MLflow 3
*   MLflow 2.x

Python

    mlflow.pyfunc.log_model(   name=name,   code_paths=[filename.py],   data_path=data_path,   conda_env=conda_env,)

### Log direct and transitive dependencies[​](#log-direct-and-transitive-dependencies "Direct link to Log direct and transitive dependencies")

With MLflow 3, you can choose to log direct and transitive dependencies by setting the `MLFLOW_LOCK_MODEL_DEPENDENCIES` environment variable.

Python

    import osos.environ["MLFLOW_LOCK_MODEL_DEPENDENCIES"] = "true"# Now when you log your model, MLflow captures# both direct and transitive dependenciesmlflow.sklearn.log_model(    model,    "my_model",)

## Log non-Python package model dependencies[​](#log-non-python-package-model-dependencies "Direct link to log-non-python-package-model-dependencies")

MLflow does not automatically pick up non-Python dependencies, such as Java packages, R packages, and native packages (such as Linux packages). For these packages, you need to log additional data.

*   Dependency list: Databricks recommends logging an artifact with the model specifying these non-Python dependencies. This could be a simple `.txt` or `.json` file. [mlflow.pyfunc.log\_model](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model) allows you to specify this additional artifact using the `artifacts` argument.
*   Custom packages: Just as for custom Python dependencies above, you need to ensure that the packages are available in your deployment environment. For packages in a central location such as Maven Central or your own repository, make sure that the location is available at scoring or serving time. For private packages not hosted elsewhere, you can log packages along with the model as artifacts.

## Deploy models with dependencies[​](#deploy-models-with-dependencies "Direct link to deploy-models-with-dependencies")

When deploying a model from the MLflow Tracking Server or Model Registry, you need to ensure that the deployment environment has the right dependencies installed. The simplest path may depend on your deployment mode: batch/streaming or online serving, and on the types of dependencies.

For all deployment modes, Databricks recommends running inference on the same runtime version that you used during training, since the Databricks Runtime in which you created your model has various libraries already installed. MLflow in Databricks automatically saves that runtime version in the `MLmodel` metadata file in a `databricks_runtime` field, such as `databricks_runtime: 10.2.x-cpu-ml-scala2.12`.

### Online serving: Model Serving[​](#online-serving-model-serving "Direct link to Online serving: Model Serving")

Databricks offers [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/), where your MLflow machine learning models are exposed as scalable REST API endpoints.

For Python dependencies in the `requirements.txt` file, Databricks and MLflow handle everything for public PyPI dependencies. Similarly, if you specified `.py` files or Python wheel files when logging the model by using `code_paths` (or `code_path` in MLflow 2.x), MLflow loads those dependencies for you automatically.

important

Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`, and Model Serving cannot build the container image because it requires `mlflow`. Specify `mlflow==<version>` in `pip_requirements` when you log the model. For details, see [Deploy Python code with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/deploy-custom-python-code).

For these model serving scenarios, see the following:

*   [Use custom Python libraries with Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving)
*   [Package custom artifacts and files for Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/model-serving-custom-artifacts)

### Online serving: third-party systems or Docker containers[​](#online-serving-third-party-systems-or-docker-containers "Direct link to Online serving: third-party systems or Docker containers")

If your scenario requires serving to third-party serving solutions or your own Docker-based solution, you can export your model as a Docker container.

Databricks recommends the following for third-party serving that automatically handles Python dependencies. However, for non-Python dependencies, the container needs to be modified to include them.

*   MLflow's Docker integration for Docker-based serving solution: [MLflow models build-docker](https://mlflow.org/docs/latest/cli.html#mlflow-models-build-docker)

*   MLflow's SageMaker integration: [mlflow.sagemaker API](https://mlflow.org/docs/latest/python_api/mlflow.sagemaker.html)

### Batch and streaming jobs[​](#batch-and-streaming-jobs "Direct link to Batch and streaming jobs")

Batch and streaming scoring should be run as [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/). A notebook job often suffices, and the simplest way to prepare code is to use the [Databricks Model Registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry#use-model-for-inference) to generate a scoring notebook.

The following describes the process and the steps to follow to ensure dependencies are installed and applied accordingly:

1.  Start your scoring cluster with the same Databricks Runtime version used during training. Read the `databricks_runtime` field from the `MLmodel` metadata file, and start a cluster with that runtime version.
    
    *   This can be done manually in the cluster configuration or automated with custom logic. For automation, the runtime version format that you read from the metadata file in the [Jobs API](https://docs.databricks.com/api/workspace/jobs) and [Clusters API](https://docs.databricks.com/api/workspace/clusters).
2.  Next, install any non-Python dependencies. To ensure your non-Python dependencies are accessible to your deployment environment, you can either:
    
    *   Manually install the non-Python dependencies of your model on the Databricks cluster as part of the cluster configuration before running inference.
    *   Alternatively, you can write custom logic in your scoring job deployment to automate the installation of the dependencies onto your cluster. Assuming you saved your non-Python dependencies as artifacts as described in [Log non-Python package model dependencies](#log-non-python), this automation can install libraries using the [Libraries API](https://docs.databricks.com/api/workspace/libraries). Or, you can write specific code to generate a [cluster-scoped initialization script](https://docs.databricks.com/aws/en/init-scripts/cluster-scoped) to install the dependencies.
3.  Your scoring job installs the Python dependencies in the job execution environment. In Databricks, the Model Registry allows you to generate a notebook for inference which does this for you.
    
    *   When you use the Databricks Model Registry to [generate a scoring notebook](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry#use-model-for-inference), the notebook contains code to install the Python dependencies in the model's `requirements.txt` file. For your notebook job for batch or streaming scoring, this code initializes your notebook environment, so that the model dependencies are installed and ready for your model.
4.  MLflow handles any custom Python code included in `code_paths` (or `code_path` in MLflow 2.x) in `log_model`. This code is added to the Python path when the model's `predict()` method is called. You can also do this manually by either:
    
    *   Calling [mlflow.pyfunc.spark\_udf](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.spark_udf) with the `env_manager=['virtualenv'/'conda']` argument.
    *   Extracting the requirements using [mlflow.pyfunc.get\_model\_dependencies](https://mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.get_model_dependencies) and installing them using [%pip install](https://docs.databricks.com/aws/en/libraries/notebooks-python-libraries).
    
    note
    
    If you specified `.py` files or Python wheel files when logging the model using `code_paths` or `code_path`, MLflow loads those dependencies for you automatically.
