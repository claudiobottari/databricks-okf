---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e34fafdb9a371fef093d1f3f973c59927c9b6a061905c6f9def372699b98ceab
  pageDirectory: concepts
  sources:
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-experiment-tracking-and-model-registry
    - Model Registry and MLflow for Experiment Tracking
    - MFETAMR
    - Experiment tracking and observability
  citations:
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
title: MLflow for Experiment Tracking and Model Registry
description: Databricks-managed MLflow provides reproducible, auditable ML development with tracking, registry, and full audit trails linking model versions to training runs, datasets, environments, and git commits.
tags:
  - mlops
  - experiment-tracking
  - model-registry
timestamp: "2026-06-18T15:05:36.431Z"
---

# MLflow for Experiment Tracking and Model Registry

**MLflow** is an open-source platform that manages the full [machine learning lifecycle](/concepts/cicd-for-machine-learning.md), including experiment tracking, reproducibility, model packaging, deployment, and a central model registry. Created by Databricks and used by over 10,000 organizations, MLflow integrates with any ML framework and stores artifacts in open formats that can be exported and run outside the platform. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Experiment Tracking

MLflow provides a robust system for tracking ML experiments, recording parameters, metrics, code versions, and artifacts for each run. The platform enables data scientists to compare multiple runs systematically, identify the best performing configurations, and reproduce results exactly. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Key Features

- **Automatic logging**: MLflow can automatically log parameters, metrics, and models from supported frameworks (scikit-learn, XGBoost, PyTorch, TensorFlow, and others) with minimal code changes.
- **Open format**: Experiment data is stored in open formats (JSON, Parquet, YAML), ensuring portability and interoperability with external tools.
- **Unity Catalog integration**: On Databricks, experiment tracking integrates with [Unity Catalog](/concepts/unity-catalog.md) to provide full lineage for data and code assets, linking each model version back to the training run, dataset, environment, and git commit that produced it.

### Running Experiments

```python
import mlflow

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

## Model Registry

The **Model Registry** is a centralized repository that manages ML model versions, stages, and annotations. It provides a structured workflow for promoting models through development, staging, and production environments, with full versioning and audit trail support. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Lifecycle Stages

| Stage | Description |
|-------|-------------|
| **None** | Unregistered model |
| **Staging** | Models ready for testing or validation |
| **Production** | Models deployed for serving |
| **Archived** | Previously used models superseded by newer versions |

Each stage transition is logged, providing a complete history of changes for compliance and governance requirements.

### Model Versioning

Every model registered in MLflow receives:
- A unique version number
- Links to the originating training run and experiment
- Full parameter, metric, and artifact metadata
- Environment snapshots for reproducibility
- Git commit references for code lineage

### Registry Operations

```python
# Register a model
mlflow.register_model(
    model_uri="runs:/<run-id>/model",
    name="churn-prediction"
)

# Transition to production
client = mlflow.tracking.MlflowClient()
client.transition_model_version_stage(
    name="churn-prediction",
    version=3,
    stage="Production"
)
```

## Governance and Audit Trails

MLflow's integration with [Unity Catalog](/concepts/unity-catalog.md) and Git provides complete governance for ML assets. Each model version in the registry includes: ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

- **Data provenance**: Track which datasets, features, and tables were used in training.
- **Code provenance**: Link to the exact git commit and notebook version that produced the model.
- **Runtime environment**: Snapshot of library versions, dependencies, and compute configuration.
- **Deployment history**: Record of when, where, and by whom each model was deployed.

This audit trail satisfies compliance requirements across regulated industries, including financial services and healthcare.

## Open Source Ecosystem

MLflow is fully open-source and framework-agnostic: ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

- Supports any ML framework: scikit-learn, PyTorch, TensorFlow, Hugging Face, XGBoost, LightGBM, and more
- Stores artifacts in open, portable formats (MLflow format, PyTorch, ONNX, etc.)
- Can be self-hosted or used on Databricks with managed infrastructure
- Integrates with external CI/CD pipelines for automated model promotion

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Recording parameters, metrics, and artifacts
- MLflow Models — Standard format for packaging ML models
- [MLflow Projects](/concepts/mlflow-projects.md) — Packaging data science code in a reusable format
- [Databricks Runtime for ML](/concepts/databricks-runtime-for-ml.md) — Pre-configured environment with MLflow and common libraries
- [MLflow Autologging](/concepts/mlflow-autologging.md) — Automatic instrumentation for popular frameworks

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md

# Citations

1. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
