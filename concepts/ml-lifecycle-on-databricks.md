---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 24a19b8e358cb405c18574e6296e9e0c16f114f3eb457b73b841afc1c2a14c69
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-lifecycle-on-databricks
    - MLOD
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: ML Lifecycle on Databricks
description: "The end-to-end journey from raw data to production model, covering eight key stages: scoping, EDA, data/feature preparation, training, evaluation, registration, deployment, and monitoring/retraining."
tags:
  - machine-learning
  - mlops
  - lifecycle
timestamp: "2026-06-19T17:49:38.792Z"
---

Here is the wiki page for "ML Lifecycle on Databricks", written based solely on the provided source material.

---

## ML Lifecycle on Databricks

The **ML Lifecycle on Databricks** covers the end-to-end journey from raw data to a production model and back again through monitoring and retraining. Databricks provides a unified platform that connects data engineering, interactive data science, and production ML within a single governed system. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Key Stages

The ML lifecycle on Databricks consists of the following key stages:

1.  **Scope the use case** by defining the prediction target, success metrics, and production requirements.
2.  **Run exploratory data analysis (EDA)** to understand data distributions, predictive signals, and data quality issues before modeling.
3.  **Prepare data and features**, managed within a feature store.
4.  **Train models and track experiments**, logging experiment metadata for analysis and for deployment.
5.  **Evaluate** model quality against held-out data and stakeholder criteria.
6.  **Register, stage and test** models before promoting to production.
7.  **Deploy to production** in real-time endpoints or batch inference jobs.
8.  **Monitor and retrain** to adapt models to changing data or user behavior.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Platform Components

A well-designed ML platform on Databricks includes several key components that support the full lifecycle:

- **Data assets** such as files, tables, processing pipelines, and feature stores.
- **Experimentation tools** such as notebooks and visualizations, with simple collaboration and AI assistance.
- **Training infrastructure** with customizable environments and flexible compute resources.
- **Deployment and monitoring infrastructure** for batch and real-time serving, with production dashboards and alerts.
- **MLOps and governance tools** for orchestration, CI/CD, lineage, access management, and audit logging.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Governance Capabilities

Key governance capabilities that unify the ML lifecycle include:

- **Unified governance of data and ML assets** through [Unity Catalog](/concepts/unity-catalog.md).
- **Unified governance of model endpoints** through the Unity AI Gateway for serving endpoints.
- **Unified security approach** through Databricks AI Security.
- **Unified administration** of data and ML tooling.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### AI-Assisted Development

Databricks provides [Genie Code](/concepts/genie-code.md), an AI assistant integrated across notebooks and the workspace. It can be used at every step of the workflow, including discovering relevant models and data, prototyping pipelines for featurization and model training, and analyzing model serving endpoints to diagnose production issues. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Related Concepts

- Machine Learning Lifecycle – Detailed guide to each stage of the lifecycle.
- Databricks Data Science and ML Capabilities – Capabilities organized by workflow stage.
- [Model Serving](/concepts/model-serving.md) – Supports classic ML, deep learning, and custom GenAI models.
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) – Tracks runs and experiments across all ML paradigms.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – GPU-enabled runtime for training and fine-tuning.
- [AI Runtime](/concepts/ai-runtime.md) – Runtime supporting training and fine-tuning across ML paradigms.

### Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
