---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8bd60f6c81e2fdcc4cac487972c7e9450ee260b7a9360bf3e796cff0c4bba8b2
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - non-python-package-dependency-logging
    - NPDL
    - Package Dependencies
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: Non-Python Package Dependency Logging
description: The challenge and recommended approach for logging non-Python dependencies (Java, R, native/Linux packages) as artifacts alongside MLflow models, since MLflow does not automatically capture them.
tags:
  - mlflow
  - dependency-management
  - cross-language
timestamp: "2026-06-19T19:16:59.021Z"
---

## Non-Python Package Dependency Logging

**Non-Python package dependency logging** refers to the process of explicitly recording dependencies that are not Python packages—such as Java libraries, R packages, or native (Linux) system packages—when saving an MLflow model. MLflow does not automatically detect or capture these dependencies, so they must be logged manually to ensure the model can be reproduced and served correctly in deployment environments. ^[log-model-dependencies-databricks-on-aws.md]

### MLflow’s Limitation

MLflow’s built-in dependency tracking (via `requirements.txt` or `conda.yaml` in the model artifact) covers only Python packages. Non-Python dependencies such as Java JARs, R packages, and native libraries are **not** automatically inferred by MLflow. When a model relies on such dependencies, extra steps are required to make them available at prediction time. ^[log-model-dependencies-databricks-on-aws.md]

### Recommended Approach

Databricks recommends two complementary practices for managing non-Python dependencies:

1. **Log a dependency artifact** – Store a manifest (e.g., a `.txt` or `.json` file) in the model artifact that lists all non-Python dependencies and their versions. This can be accomplished using the `artifacts` argument of [`mlflow.pyfunc.log_model`](https://www.mlflow.org/docs/latest/python_api/mlflow.pyfunc.html#mlflow.pyfunc.log_model). The manifest serves as documentation and as a guide for deployment automation. ^[log-model-dependencies-databricks-on-aws.md]

2. **Ensure package availability in the deployment environment** – For packages hosted in a central repository (such as Maven Central for Java or CRAN for R), the deployment environment must be able to reach that repository during scoring or serving. For private packages that are not hosted externally, the package binary itself can be logged as a model artifact alongside the model. ^[log-model-dependencies-databricks-on-aws.md]

### Deployment Considerations

#### Batch and Streaming Jobs

For batch or streaming inference using [Lakeflow Jobs](/concepts/lakeflow-jobs.md) (or legacy Jobs), the following workflow is recommended:

- Start a cluster with the same Databricks Runtime version that was used during training. The runtime version is automatically saved in the model’s `MLmodel` metadata file under the field `databricks_runtime`. ^[log-model-dependencies-databricks-on-aws.md]
- Install non-Python dependencies on the cluster **before** running inference. This can be done:
  - **Manually** through the cluster configuration UI.
  - **Automatically** via the Libraries API or by writing a cluster-scoped initialization script. Both approaches can use the dependency manifest logged with the model to determine what to install. ^[log-model-dependencies-databricks-on-aws.md]

MLflow handles Python dependencies automatically (e.g., via `requirements.txt` and `code_paths`), but non-Python dependencies require this separate cluster-level setup.

#### Online Serving (Model Serving)

Databricks [Model Serving](/concepts/model-serving.md) provides managed REST endpoints for MLflow models. For Python dependencies, public PyPI packages and custom Python code logged via `code_paths` are handled automatically. Non-Python dependencies, however, are not automatically provisioned by Model Serving. Databricks recommends running inference on the same Databricks Runtime version used during training to minimise missing library issues, because the runtime bundles many native and Java libraries. For specific non-Python dependencies not present in the runtime, you may need to explore custom container images or additional configuration; consult the documentation on custom artifacts for Model Serving. ^[log-model-dependencies-databricks-on-aws.md]

#### Third-Party Serving Systems

When exporting a model to a third-party serving solution or a custom Docker container, the container must be modified to include any non-Python dependencies. MLflow provides Docker integration via `mlflow models build-docker`, and SageMaker integration via the `mlflow.sagemaker` API. In both cases, you must manually add the required non-Python libraries to the image or environment. ^[log-model-dependencies-databricks-on-aws.md]

### Related Concepts

- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) – Built-in flavors that automatically log Python dependencies.
- MLflow pyfunc – Generic Python function model flavor used for custom and non‑Python dependencies.
- Model artifacts – Files and directories stored alongside an MLflow model.
- cluster-scoped initialization script – Mechanism to install system-level packages on Databricks clusters.
- Libraries API – Programmatic interface for installing cluster libraries.

### Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
