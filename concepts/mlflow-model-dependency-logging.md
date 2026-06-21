---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1255b81fd1958a4ee6a2fca207335865264518e4d0e73ddbdae87e99f74ce5cb
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-model-dependency-logging
    - MMDL
    - Log Model Dependencies
    - Log model dependencies
    - MLflow Dependencies
    - Model dependencies
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
    - file: log-model-dependencies-databricks-on-aws.md
      start: 12
      end: 18
    - file: log-model-dependencies-databricks-on-aws.md
      start: 21
      end: 27
    - file: log-model-dependencies-databricks-on-aws.md
      start: 29
      end: 33
    - file: log-model-dependencies-databricks-on-aws.md
      start: 35
      end: 44
    - file: log-model-dependencies-databricks-on-aws.md
      start: 46
      end: 57
    - file: log-model-dependencies-databricks-on-aws.md
      start: 63
      end: 72
    - file: log-model-dependencies-databricks-on-aws.md
      start: 78
      end: 84
    - file: log-model-dependencies-databricks-on-aws.md
      start: 87
      end: 90
    - file: log-model-dependencies-databricks-on-aws.md
      start: 92
      end: 96
    - file: log-model-dependencies-databricks-on-aws.md
      start: 98
      end: 100
    - file: log-model-dependencies-databricks-on-aws.md
      start: 102
      end: 105
    - file: log-model-dependencies-databricks-on-aws.md
      start: 107
      end: 114
    - file: log-model-dependencies-databricks-on-aws.md
      start: 116
      end: 134
title: MLflow Model Dependency Logging
description: The practice of logging a machine learning model along with its Python and non-Python dependencies as artifacts, ensuring reproducibility and portability across environments.
tags:
  - mlflow
  - machine-learning
  - dependency-management
timestamp: "2026-06-19T19:17:09.289Z"
---

# MLflow Model Dependency Logging

**MLflow Model Dependency Logging** refers to the process of capturing and storing a model's software dependencies (Python packages, custom code, and non-Python libraries) as part of the model artifact. This ensures that the exact environment used during training is reproducible for production tasks such as batch inference, streaming scoring, or online [Model Serving](/concepts/model-serving.md). ^[log-model-dependencies-databricks-on-aws.md]

## Logging Python Package Dependencies

MLflow provides native support for many popular Python ML libraries (known as built-in model flavors) and can automatically log their versions when those libraries are used. For example, `mlflow.sklearn.log_model` automatically captures the scikit-learn version. The same applies to [autologging](/concepts/mlflow-autologging.md) when used with supported libraries. For a list of built-in flavors, see the MLflow documentation on [built-in model flavors](https://mlflow.org/docs/latest/models.html#built-in-model-flavors). ^[log-model-dependencies-databricks-on-aws.md:12-18]

For libraries that are installable via `pip install PACKAGE_NAME==VERSION` but do not have a built-in model flavor, you can log dependencies using `mlflow.pyfunc.log_model`. This method supports public PyPI packages, privately hosted packages, and custom libraries packaged as Python egg or wheel files. When you call `mlflow.pyfunc.log_model`, MLflow attempts to infer dependencies automatically using `mlflow.models.infer_pip_requirements` and logs them to a `requirements.txt` file as a model artifact. ^[log-model-dependencies-databricks-on-aws.md:21-27]

If MLflow does not automatically identify all Python requirements (particularly for libraries without built-in flavors), you can specify additional dependencies with the `extra_pip_requirements` parameter in the `log_model` command. Overwriting the entire set of requirements with `conda_env` or `pip_requirements` is generally discouraged, as it overrides the dependencies that MLflow picks up automatically. ^[log-model-dependencies-databricks-on-aws.md:29-33]

### Customized Model Logging

For scenarios requiring more control, you can write a custom Python model by subclassing `mlflow.pyfunc.PythonModel` to customize initialization and prediction. Alternatively, you can write a custom flavor, which provides more extensive customization but requires more implementation work. ^[log-model-dependencies-databricks-on-aws.md:35-44]

### Custom Python Code

If your model depends on Python code that cannot be installed with `%pip install` (e.g., one or more `.py` files), you can use the `code_paths` parameter (or `code_path` in MLflow 2.x) in `mlflow.pyfunc.log_model`. MLflow stores these files or directories as artifacts alongside the model in a code directory. When the model is loaded, those files are added to the Python path. This approach also works for custom [Python Wheel Files](/concepts/python-wheel-files.md). ^[log-model-dependencies-databricks-on-aws.md:46-57]

### Logging Direct and Transitive Dependencies (MLflow 3)

With MLflow 3, you can capture both direct and transitive Python dependencies by setting the environment variable `MLFLOW_LOCK_MODEL_DEPENDENCIES` to `"true"` before logging the model. ^[log-model-dependencies-databricks-on-aws.md:63-72]

## Logging Non-Python Package Dependencies

MLflow does not automatically capture non-Python dependencies such as Java packages, R packages, or native Linux packages. For these, you must log additional data manually:

- **Dependency list**: Log an artifact (e.g., a `.txt` or `.json` file) with the model specifying the non-Python dependencies. `mlflow.pyfunc.log_model` supports this via the `artifacts` argument.
- **Custom packages**: Ensure that these packages are available in the deployment environment. For packages hosted in a central repository (e.g., Maven Central), ensure that location is reachable at scoring time. For private packages not hosted elsewhere, log them as artifacts alongside the model.

^[log-model-dependencies-databricks-on-aws.md:78-84]

## Deploying Models with Dependencies

When deploying a model from the [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md) or [Model Registry](/concepts/mlflow-model-registry.md), you must ensure the deployment environment has the correct dependencies installed. Databricks recommends running inference on the same Databricks Runtime version used during training, as that runtime already includes many of the required libraries. MLflow on Databricks automatically saves the runtime version in the `MLmodel` metadata file as `databricks_runtime`. ^[log-model-dependencies-databricks-on-aws.md:87-90]

### Online Serving: Model Serving

For Databricks [Model Serving](/concepts/model-serving.md), MLflow handles public PyPI dependencies listed in `requirements.txt` automatically. Custom Python code specified via `code_paths` (or `code_path`) is also loaded automatically. ^[log-model-dependencies-databricks-on-aws.md:92-96]

> **Important**: Databricks Runtime ML runtimes include `mlflow-skinny` by default, not the full `mlflow` package. If you log a `pyfunc` model on such a runtime without specifying `pip_requirements`, MLflow captures `mlflow-skinny`, which prevents Model Serving from building the container image. Always specify `mlflow==<version>` in `pip_requirements` when logging the model. ^[log-model-dependencies-databricks-on-aws.md:98-100]

For custom Python libraries or custom artifacts, see the dedicated documentation on [using custom Python libraries with Model Serving](/concepts/custom-libraries-for-databricks-model-serving.md) and packaging custom artifacts for Model Serving. ^[log-model-dependencies-databricks-on-aws.md:102-105]

### Online Serving: Third-Party Systems or Docker

For third-party serving solutions or Docker-based deployments, you can export the model as a Docker container using MLflow's `mlflow models build-docker` command. For Amazon SageMaker, use the `mlflow.sagemaker` API. Python dependencies are handled automatically, but non-Python dependencies must be added separately to the container. ^[log-model-dependencies-databricks-on-aws.md:107-114]

### Batch and Streaming Jobs

Batch and streaming scoring should be run as [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md). A common approach is to use the Model Registry to generate a scoring notebook. The recommended workflow:

1. **Start the scoring cluster** with the same Databricks Runtime version used during training (read from the `MLmodel` file's `databricks_runtime` field).
2. **Install non-Python dependencies** manually on the cluster (e.g., through cluster configuration, the Libraries API, or a cluster-scoped init script).
3. **Install Python dependencies** from the model's `requirements.txt`. When generating a scoring notebook from the Model Registry, the notebook includes code to install these dependencies automatically.
4. **Handle custom Python code** – MLflow automatically adds code specified via `code_paths` or `code_path` to the Python path when the model’s `predict()` method is called. You can also manually install dependencies using `mlflow.pyfunc.get_model_dependencies` and `%pip install`, or use `mlflow.pyfunc.spark_udf` with `env_manager` set to `'virtualenv'` or `'conda'`.

^[log-model-dependencies-databricks-on-aws.md:116-134]

## Related Concepts

- [mlflow.pyfunc.PythonModel](/concepts/mlflow-pyfunc-custom-python-model.md) – Custom model class for dependency logging.
- [Model Flavors](/concepts/mlflow-model-flavors.md) – Built-in and custom flavor integration.
- [Model Serving](/concepts/model-serving.md) – Online REST API serving with automatic dependency handling.
- [Model Registry](/concepts/mlflow-model-registry.md) – Central model storage and deployment.
- Databricks Runtime – Pre-installed environment for training and inference.
- pip_requirements – Parameter to specify exact Python dependencies.
- extra_pip_requirements – Parameter to supplement inferred dependencies.
- code_paths / code_path – Parameter to include custom Python files.
- MLFLOW_LOCK_MODEL_DEPENDENCIES – Environment variable for transitive dependency logging.

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
2. [log-model-dependencies-databricks-on-aws.md:12-18](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
3. [log-model-dependencies-databricks-on-aws.md:21-27](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
4. [log-model-dependencies-databricks-on-aws.md:29-33](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
5. [log-model-dependencies-databricks-on-aws.md:35-44](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
6. [log-model-dependencies-databricks-on-aws.md:46-57](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
7. [log-model-dependencies-databricks-on-aws.md:63-72](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
8. [log-model-dependencies-databricks-on-aws.md:78-84](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
9. [log-model-dependencies-databricks-on-aws.md:87-90](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
10. [log-model-dependencies-databricks-on-aws.md:92-96](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
11. [log-model-dependencies-databricks-on-aws.md:98-100](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
12. [log-model-dependencies-databricks-on-aws.md:102-105](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
13. [log-model-dependencies-databricks-on-aws.md:107-114](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
14. [log-model-dependencies-databricks-on-aws.md:116-134](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
