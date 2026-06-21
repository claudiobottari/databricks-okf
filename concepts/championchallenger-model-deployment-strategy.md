---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c78b40b0e3e6eab5dc1404292cb29675a96e3090caf1b762d87405a2cf376118
  pageDirectory: concepts
  sources:
    - mlops-workflows-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - championchallenger-model-deployment-strategy
    - CMDS
    - Champion vs Challenger Model Deployment
    - Champion/Challenger Model Strategy
  citations:
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: Champion/Challenger Model Deployment Strategy
description: A pattern where a newly trained and validated model is given the 'Challenger' alias and compared against the current production model (the 'Champion') before being promoted to production status.
tags:
  - mlops
  - deployment
  - model-governance
timestamp: "2026-06-19T19:41:42.062Z"
---

# Champion/Challenger Model Deployment Strategy

The **Champion/Challenger Model Deployment Strategy** is an MLOps pattern for managing model versions in production. In this strategy, the currently deployed production model is designated as the "Champion", while a newly developed and validated candidate model is designated as the "Challenger". The challenger is compared to the champion before it can replace the champion in production. This approach enables controlled rollouts, A/B testing, and gradual deployment of model updates. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Key Concepts

### Champion Alias

The **Champion** alias is assigned to the model version that is currently serving as the production model. In Databricks, this alias is managed through [Models in Unity Catalog](/concepts/models-in-unity-catalog.md). Inference pipelines and Model Serving endpoints are configured to load the model version with the `Champion` alias. When the champion is updated to a new version, the inference pipeline automatically uses the new version on its next execution, decoupling model deployment from inference. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

### Challenger Alias

The **Challenger** alias is assigned to a newly trained and validated model version that is a candidate to replace the champion. After a model passes all validation checks (e.g., format, metadata, performance on data slices, compliance), the deployment pipeline assigns the `Challenger` alias to it in [Unity Catalog](/concepts/unity-catalog.md). The challenger is then compared to the champion before promotion. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Comparison and Validation

The comparison between the challenger and champion can be performed offline or online:

* **Offline comparison**: Both models are evaluated against a held-out data set. Results are tracked using the MLflow Tracking server. If there is no existing champion, the challenger may be compared against a business heuristic or other baseline. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

* **Online comparison**: For real-time serving scenarios, longer-running tests such as A/B tests or gradual rollouts can be used. Databricks Model Serving can create a single endpoint that hosts multiple models and specifies the traffic split between them, enabling online champion-versus-challenger comparisons. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Deployment to Production

If the challenger performs at least as well as the champion in the comparison, the deployment pipeline updates the alias: it reassigns the `Champion` alias to the challenger model version, effectively promoting it to production. The previous champion may be retired or retained for rollback. This process can be fully automated, or manual approval steps can be added using workflow notifications or CI/CD callbacks. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Model Serving and Traffic Splitting

When configuring a Mod Serving endpoint, you specify the model name and version to serve. To conduct online champion-versus-challenger experiments, you can create a single endpoint that hosts both models and set a traffic split percentage (e.g., 90% champion, 10% challenger). Model Serving performs zero-downtime updates when changing the model version. ^[mlops-workflows-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Tracking and logging model metrics, parameters, and artifacts.
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) – Central registry for model versioning, aliases, and governance.
- [Model Serving](/concepts/model-serving.md) – Infrastructure for deploying models as REST API endpoints.
- A/B Testing – Online evaluation strategy for comparing model versions.
- [CI/CD for Machine Learning](/concepts/cicd-for-machine-learning.md) – Automating the promotion of challenger to champion.
- Production MLOps Workflow – End-to-end pipeline including training, validation, deployment, and monitoring.

## Sources

- mlops-workflows-on-databricks-databricks-on-aws.md

# Citations

1. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
