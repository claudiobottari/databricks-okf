---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc4009bd83dd88418fb0dd017f8c6d487b724e26e58b69e8f2a2db9dc2282684
  pageDirectory: concepts
  sources:
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - modelops-on-databricks
    - MOD
    - DevOps on Databricks
    - MLOps on Databricks
  citations:
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: ModelOps on Databricks
description: Model development and lifecycle management using MLflow tracking and Model Registry, with monitoring of model performance and input data changes.
tags:
  - mlops
  - machine-learning
  - model-management
timestamp: "2026-06-19T19:06:50.950Z"
---

```markdown
---
title: ModelOps on Databricks
summary: Model development and lifecycle management using MLflow for experiment tracking and the Model Registry for staging, serving, and storing model artifacts.
sources:
  - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:48:55.390Z"
updatedAt: "2026-06-19T10:48:55.390Z"
tags:
  - mlops
  - model-lifecycle
  - mlflow
aliases:
  - modelops-on-databricks
  - MOD
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# ModelOps on Databricks

**ModelOps on Databricks** refers to the set of practices and tools for managing the end-to-end lifecycle of machine learning models: from development and experimentation through staging, deployment, serving, and ongoing monitoring. On the Databricks Data Intelligence Platform, ModelOps is supported primarily through [[MLflow]] for experiment tracking and the [[MLflow Model Registry]] for model lifecycle governance. After a model is released to production, the platform also provides capabilities to monitor changes in input data and model performance that might require retraining.^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Model development and experimentation

Developing a model requires a series of experiments and a way to track and compare the conditions and results of those experiments. Databricks includes MLflow for model development tracking, enabling data scientists to log parameters, metrics, and artifacts for every run and to compare different iterations.^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Lifecycle management with the Model Registry

After experimentation, the MLflow Model Registry is used to manage the model lifecycle, including staging, serving, and storing model artifacts. The registry provides a central repository where models can be transitioned through stages (e.g., Staging → Production → Archived), with versioning and approval workflows to ensure governance and reproducibility.^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Monitoring after production release

Once a model is deployed to production, many factors can change that might affect its performance. Databricks supports ongoing monitoring in two key areas:

- **Model prediction performance** – tracking accuracy, latency, and other operational metrics.
- **Input data quality and distribution** – monitoring for changes in schema, statistical characteristics, or data drift that could degrade the model’s effectiveness.

These monitoring capabilities help teams detect when retraining is necessary, closing the loop between production and development.^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Common ModelOps tasks

The Databricks platform addresses common ModelOps tasks with the tools listed below (a more detailed table is available in the product documentation):

| Task | Tool / Capability |
|------|-------------------|
| Experiment tracking | MLflow Tracking |
| Model versioning and lifecycle management | MLflow Model Registry |
| Model deployment to production | Model Serving (batch, online, edge) |
| Consistency between training and serving features | Databricks Feature Store |
| Automated retraining triggers | Monitoring pipelines and scheduled jobs |

^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Relationship to other "Ops" practices

ModelOps is one pillar of a broader CI/CD framework for machine learning on Databricks, alongside [[DataOps on Databricks]] and [[DevOps for ML on Databricks|DevOps on Databricks]]. Together they cover reliable data pipelines, reproducible model development, and automated production deployment. The entire lifecycle is supported on a single platform, which facilitates cross-team collaboration and troubleshooting.^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Related concepts

- [[MLflow]] – open-source platform for the ML lifecycle
- [[MLflow Model Registry]] – centralized model store for versioning and stage transitions
- [[Model Serving on Databricks]] – deployment options for batch, real-time, and edge inference
- Feature Store on Databricks – consistent feature management for training and serving
- [[CI/CD for Machine Learning]] – automated pipelines integrating ModelOps, DataOps, and DevOps
- MLOps – broader discipline of operationalizing machine learning

## Sources

- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
```

# Citations

1. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
