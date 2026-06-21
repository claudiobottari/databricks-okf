---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ce27c29d92270d0468c5f45eceee387bafa84736b18bf08017c081669c91964c
  pageDirectory: concepts
  sources:
    - machine-learning-lifecycle-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - ml-lifecycle
    - MLOps lifecycle
    - Model lifecycle
    - Manage Model Lifecycle
  citations:
    - file: machine-learning-lifecycle-databricks-on-aws.md
title: ML Lifecycle
description: "The end-to-end journey for taking an ML project from initial scoping to production, encompassing eight stages: scoping, data exploration, data preparation, model training, evaluation, staging, deployment, and monitoring."
tags:
  - machine-learning
  - mlops
  - lifecycle
timestamp: "2026-06-19T19:19:22.915Z"
---

```yaml
---
title: ML Lifecycle
summary: The end-to-end journey from raw data to a production model and back again through monitoring and retraining, encompassing eight key stages from scoping to monitoring.
sources:
  - machine-learning-lifecycle-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:21:51.477Z"
updatedAt: "2026-06-19T09:21:51.477Z"
tags:
  - machine-learning
  - mlops
  - lifecycle
aliases:
  - ml-lifecycle
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# ML Lifecycle

The **ML lifecycle** is the end-to-end journey for taking a machine learning (ML) project from initial scoping to production, and keeping it performing well over time. Code, data, and models pass through three broad stages: development, staging, and production. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Key Stages

The lifecycle is composed of eight key stages:

1. **Scope the use case and define success**: Align on the prediction target, class of ML problem, input data, success metrics, serving requirements (latency, throughput, data freshness), and stakeholder sign-off requirements including explainability. ^[machine-learning-lifecycle-databricks-on-aws.md]
2. **Explore and understand the data**: Run [exploratory data analysis (EDA)](/concepts/exploratory-data-analysis-eda-on-databricks.md) to understand data structure, quality, and relationship to the prediction target. Identify predictive inputs, missing values, outliers, and skewed distributions. Databricks provides collaborative notebooks, dashboards, Genie Chat, and Genie Code for EDA. ^[machine-learning-lifecycle-databricks-on-aws.md]
3. **Prepare data and features**: Turn raw sources and transformations identified during EDA into features for ML models. Use [Unity Catalog](/concepts/unity-catalog.md) for governance and lineage, [Feature Store](/concepts/feature-store.md) for reusable governed feature definitions, and data engineering tools like Lakeflow Designer and [Genie Code](/concepts/genie-code.md). ^[machine-learning-lifecycle-databricks-on-aws.md]
4. **Train models and track experiments**: Use flexible environments (serverless compute with AI Runtime for GPU, classic compute with Databricks Runtime for ML) and [MLflow](/concepts/mlflow.md) tracking to log parameters, metrics, artifacts, and models with full provenance. Genie Code can generate complete ML notebooks from plain-language descriptions. ^[machine-learning-lifecycle-databricks-on-aws.md]
5. **Evaluate**: Define quality evaluation metrics based on scoping requirements, including common ML metrics (accuracy, AUC, RMSE), domain-specific metrics, and derived metrics such as bias and fairness across population segments. Log metrics in MLflow runs to link them to corresponding models. ^[machine-learning-lifecycle-databricks-on-aws.md]
6. **Register, stage and test models**: Register models to the [MLflow Model Registry in Unity Catalog](/concepts/mlflow-model-registry-in-unity-catalog.md) with versioned artifacts linked to original training runs. Use aliases (`Staging`, `Production`) to signal lifecycle state. Run integration tests, A/B or shadow tests on production data, and collect stakeholder sign-off. ^[machine-learning-lifecycle-databricks-on-aws.md]
7. **Deploy to production**: Support two primary serving patterns: [Model Serving](/concepts/model-serving.md) for low-latency real-time REST endpoints, and ai_query for batch inference. Both patterns use the same trained model artifact from the same registered version with the same governance and lineage. ^[machine-learning-lifecycle-databricks-on-aws.md]
8. **Monitor and retrain**: Log inputs and outputs from deployed models using [Inference Tables](/concepts/inference-tables.md) for real-time serving or Delta tables for batch serving. Use [Data Quality Monitoring](/concepts/data-quality-monitoring.md) to track data quality, feature drift, and prediction distribution. Join with ground truth data to compute prediction quality metrics and trigger incident management through anomaly detection alerts. ^[machine-learning-lifecycle-databricks-on-aws.md]

## Related Concepts

- MLOps workflows
- [Feature Store](/concepts/feature-store.md)
- [Model Serving](/concepts/model-serving.md)
- [Batch inference](/concepts/batch-inference-pipelines.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [Genie Code](/concepts/genie-code.md) — AI-assisted development throughout the lifecycle
- [Inference Tables](/concepts/inference-tables.md)
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md)

## Sources

- machine-learning-lifecycle-databricks-on-aws.md

# Citations

1. [machine-learning-lifecycle-databricks-on-aws.md](/references/machine-learning-lifecycle-databricks-on-aws-d195211f.md)
