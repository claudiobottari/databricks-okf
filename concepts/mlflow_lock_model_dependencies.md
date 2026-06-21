---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 26595300da91cf83be33dfd6b5da0e68944b209fbadb5694a3d2a3dfff6aaa74
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow_lock_model_dependencies
    - MLFLOW_LOCK_MODEL_DEPENDENCIES
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: MLFLOW_LOCK_MODEL_DEPENDENCIES
description: An environment variable in MLflow 3 that, when set to 'true', causes MLflow to capture both direct and transitive Python dependencies when logging a model.
tags:
  - mlflow
  - environment-variables
  - dependency-management
timestamp: "2026-06-19T19:16:55.665Z"
---

# MLFLOW_LOCK_MODEL_DEPENDENCIES

**MLFLOW_LOCK_MODEL_DEPENDENCIES** is an environment variable introduced in MLflow 3 that controls whether MLflow captures both direct and transitive (locked) Python dependencies when logging a model. When enabled, MLflow resolves and records the full dependency tree, including all transitive dependencies, rather than only the top-level packages. ^[log-model-dependencies-databricks-on-aws.md]

## Overview

By default, MLflow logs only the direct Python package dependencies of a model — the packages explicitly imported or required by the model code. However, production deployments may fail if transitive dependencies (dependencies of dependencies) are missing or have incompatible versions. Setting `MLFLOW_LOCK_MODEL_DEPENDENCIES` to `"true"` instructs MLflow to perform a full dependency resolution, capturing the complete, locked set of packages required to reproduce the model's environment. ^[log-model-dependencies-databricks-on-aws.md]

## Usage

To enable locked dependency logging, set the environment variable before calling any `log_model` function:

```python
import os
os.environ["MLFLOW_LOCK_MODEL_DEPENDENCIES"] = "true"

# Now when you log your model, MLflow captures
# both direct and transitive dependencies
mlflow.sklearn.log_model(
    model,
    "my_model",
)
```

^[log-model-dependencies-databricks-on-aws.md]

## Behavior

When `MLFLOW_LOCK_MODEL_DEPENDENCIES` is set to `"true"`, MLflow resolves the full dependency graph at model logging time. This includes:

- **Direct dependencies**: Packages explicitly required by the model (e.g., `scikit-learn`, `pandas`).
- **Transitive dependencies**: Packages that direct dependencies themselves depend on (e.g., `joblib`, `numpy`, `scipy`).

The resulting dependency list is written to the model's `requirements.txt` file as a locked set of exact versions, ensuring reproducible environments for deployment. ^[log-model-dependencies-databricks-on-aws.md]

## Use Cases

Locked dependencies are particularly valuable for:

- **Production model serving**: Ensuring that the serving environment exactly matches the training environment, preventing version conflicts.
- **Compliance and auditability**: Providing a complete, verifiable record of all software dependencies used by a model.
- **Reproducibility**: Guaranteeing that model inference produces identical results across different environments and time points.

## Related Concepts

- [Log model dependencies](/concepts/mlflow-model-dependency-logging.md) — General guide for logging model dependencies in MLflow.
- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) — Built-in support for common ML libraries with automatic dependency logging.
- mlflow.pyfunc.log_model — The primary method for logging custom Python models with dependency tracking.
- [Model Serving](/concepts/model-serving.md) — Deployment environment where locked dependencies ensure reliable inference.
- requirements.txt — The artifact file where MLflow stores logged dependencies.

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
