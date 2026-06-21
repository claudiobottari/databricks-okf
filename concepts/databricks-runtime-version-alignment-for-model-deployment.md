---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e4dd46e5b286d4144e013210c1ab5438af2e8f59ad82f56db53fa0e32c2ec40f
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-runtime-version-alignment-for-model-deployment
    - DRVAFMD
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: Databricks Runtime Version Alignment for Model Deployment
description: The recommendation to run inference on the same Databricks Runtime version used during training, leveraging the saved databricks_runtime field in MLmodel metadata to ensure dependency compatibility.
tags:
  - databricks
  - deployment
  - runtime-management
timestamp: "2026-06-19T19:17:29.775Z"
---

# Databricks Runtime Version Alignment for Model Deployment

**Databricks Runtime Version Alignment for Model Deployment** is the practice of running inference on the same Databricks Runtime version that was used during model training. This alignment ensures that the deployment environment has the correct libraries and dependencies installed, reducing compatibility issues and deployment failures.^[log-model-dependencies-databricks-on-aws.md]

## Rationale

The Databricks Runtime in which a model is trained has various libraries already installed. MLflow in Databricks automatically saves that runtime version in the `MLmodel` metadata file under a `databricks_runtime` field — for example, `databricks_runtime: 10.2.x-cpu-ml-scala2.12`. By aligning the deployment runtime with this recorded value, you ensure that the environment matches the training environment as closely as possible.^[log-model-dependencies-databricks-on-aws.md]

## Implementation for Batch and Streaming Jobs

For batch and streaming scoring, which should be run as [Lakeflow Jobs](/concepts/lakeflow-jobs.md), the recommended process is:^[log-model-dependencies-databricks-on-aws.md]

1. **Start a scoring cluster with the same Databricks Runtime version used during training.** Read the `databricks_runtime` field from the `MLmodel` metadata file and start a cluster with that runtime version. This can be done manually in the cluster configuration or automated using the Jobs API and Clusters API.^[log-model-dependencies-databricks-on-aws.md]

2. **Install any non-Python dependencies.** Ensure non-Python dependencies (such as Java packages, R packages, or native Linux packages) are accessible to your deployment environment. Options include:^[log-model-dependencies-databricks-on-aws.md]
   - Manually installing them on the Databricks cluster as part of the cluster configuration before running inference.
   - Automating installation using the Libraries API or writing custom logic to generate a cluster-scoped initialization script.

3. **Install Python dependencies in the job execution environment.** When you use the Databricks Model Registry to generate a scoring notebook, the notebook contains code to install the Python dependencies from the model's `requirements.txt` file. This code initializes the notebook environment so model dependencies are installed and ready for inference.^[log-model-dependencies-databricks-on-aws.md]

4. **Handle custom Python code.** MLflow handles any custom Python code included via `code_paths` (or `code_path` in MLflow 2.x) in `log_model` — this code is automatically added to the Python path when the model's `predict()` method is called. You can also handle this manually by calling `mlflow.pyfunc.spark_udf` with the `env_manager=['virtualenv'/'conda']` argument, or by extracting requirements using `mlflow.pyfunc.get_model_dependencies` and installing them using `%pip install`.^[log-model-dependencies-databricks-on-aws.md]

## Implementation for Online Serving

For [Model Serving](/concepts/model-serving.md), Databricks and MLflow handle Python dependencies from the `requirements.txt` file automatically for public PyPI dependencies. Similarly, any `.py` files or [Python Wheel Files](/concepts/python-wheel-files.md) specified when logging the model via `code_paths` (or `code_path` in MLflow 2.x) are loaded automatically.^[log-model-dependencies-databricks-on-aws.md]

**Important note:** Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. When logging a `pyfunc` model on these runtimes without specifying `pip_requirements`, MLflow captures `mlflow-skinny` in the model's `conda.yaml`, and Model Serving cannot build the container image because it requires `mlflow`. You must specify `mlflow==<version>` in `pip_requirements` when logging the model.^[log-model-dependencies-databricks-on-aws.md]

## Implementation for Third-Party Systems

For third-party serving solutions or Docker-based deployments, Databricks recommends:^[log-model-dependencies-databricks-on-aws.md]

- MLflow's Docker integration for Docker-based serving: `mlflow models build-docker`
- MLflow's SageMaker integration: `mlflow.sagemaker` API

These approaches handle Python dependencies automatically, but non-Python dependencies require manual modification of the container.^[log-model-dependencies-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Online serving of MLflow models as REST API endpoints
- Databricks Model Registry — Central repository for managing model lifecycle
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) — Batch and streaming job execution framework
- [MLflow](/concepts/mlflow.md) — Machine learning lifecycle management platform
- Model Dependencies — Python and non-Python packages required by a model
- Requirements.txt — Standard file for Python dependency specification
- Cluster-Scoped Init Scripts — Customization mechanism for Databricks clusters

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
