---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8a45d77bda6feb0751ebf03b4d11012a86fea8b7842a82dedda93ee2d46ea25
  pageDirectory: concepts
  sources:
    - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-platform-databricks
    - MP(
  citations:
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
title: ML Platform (Databricks)
description: Combined infrastructure, tooling, and governance layer supporting the full ML lifecycle — including data assets, experimentation tools, training infrastructure, deployment/monitoring infrastructure, and MLOps/governance tools.
tags:
  - ml-platform
  - infrastructure
  - mlops
timestamp: "2026-06-19T17:49:56.140Z"
---

---
title: ML Platform (Databricks)
summary: The combined infrastructure, tooling, and governance layer that supports the full machine learning lifecycle on Databricks.
sources:
  - concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:50:00.000Z"
updatedAt: "2026-06-19T14:50:00.000Z"
tags:
  - databricks
  - ml-platform
  - machine-learning
  - mlops
aliases:
  - ml-platform-databricks
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# ML Platform (Databricks)

The **ML Platform (Databricks)** is the combined infrastructure, tooling, and governance layer that supports the full machine learning lifecycle on Databricks, from raw data to production models. A well-designed ML platform connects data engineering, interactive data science, and production ML in a single governed system. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## The ML Lifecycle

The ML lifecycle on Databricks covers the end-to-end journey from raw data to a production model and back again through monitoring and retraining. Key stages include:

1. **Scope the use case** by defining the prediction target, success metrics, and production requirements.  
2. **Run exploratory data analysis (EDA)** to understand data distributions, predictive signals, and data quality issues before modeling.  
3. **Prepare data and features**, managed within a feature store.  
4. **Train models and track experiments**, logging experiment metadata for analysis and for deployment.  
5. **Evaluate** model quality against held-out data and stakeholder criteria.  
6. **Register, stage and test** models before promoting to production.  
7. **Deploy to production** in real-time endpoints or batch inference jobs.  
8. **Monitor and retrain** to adapt models to changing data or user behavior.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## AI-Assisted Development and Operations

Databricks provides Genie Code, an AI assistant integrated across notebooks and the workspace. It can be used for development, debugging, and ongoing operations, drawing on specialized knowledge of enterprise context. Genie Code assists at every step: discovering relevant models, data, and features via Genie chat; prototyping pipelines for featurization, training, tuning, evaluation, and deployment; and analyzing model serving endpoints to diagnose production issues. Third-party coding tools can also be used to develop and maintain ML pipelines. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Key Components

The ML platform includes the following key components:

- **Data assets** such as files, tables, processing pipelines, and feature stores.  
- **Experimentation tools** such as notebooks and visualizations, with simple collaboration and AI assistance.  
- **Training infrastructure** with customizable environments and flexible compute resources.  
- **Deployment and monitoring infrastructure** for batch and real-time serving, with production dashboards and alerts.  
- **MLOps and governance tools** for orchestration, CI/CD, lineage, access management, and audit logging.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Governance Capabilities

Unified governance is provided across data and ML assets through:

- [Unity Catalog](/concepts/unity-catalog.md) for unified governance of data and ML assets.  
- [Unity AI Gateway](/concepts/unity-ai-gateway.md) for governing model serving endpoints.  
- Databricks AI Security for a unified security approach.  
- Unified administration of data and ML tooling (see Administration).

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## ML vs. Deep Learning vs. GenAI

While the platform documentation focuses on ML and deep learning, Databricks’ platform features support all three paradigms: classical ML, deep learning, and generative AI (GenAI). Supported features include:

- [Model Serving](/concepts/model-serving.md) for classic ML, deep learning, and custom GenAI models (real-time and batch).  
- ai_query|`ai_query` for SQL queries and batch inference workloads.  
- [AI Runtime](/concepts/ai-runtime.md) and GPU-enabled [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) for training and fine-tuning.  
- [MLflow Experiment Tracking](/concepts/mlflow-experiment-tracking.md) for tracking runs and experiments.  
- Databricks AI Search for serving unstructured data.

^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- Machine Learning Lifecycle — Detailed guide to each stage.  
- Databricks Data Science and ML Capabilities — Features organized by workflow stage.  
- [Generative AI on Databricks](/concepts/ai-runtime-ai-v5-on-databricks.md) — Separate concepts for GenAI workflows.  

## Sources

- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md

# Citations

1. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
