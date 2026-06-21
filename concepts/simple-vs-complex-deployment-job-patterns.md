---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 131bfba03ed5ba2df0c249a7533bc164bdc6892dce71e33054eeb0f88d09a586
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - simple-vs-complex-deployment-job-patterns
    - SVCDJP
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Simple vs Complex Deployment Job Patterns
description: "Two common deployment job patterns: a simple 3-step pipeline (evaluation, approval, deployment) and a complex staged rollout with gradual deployment percentages, metrics collection, and rollback logic."
tags:
  - mlops
  - deployment
  - patterns
timestamp: "2026-06-19T19:37:16.635Z"
---

# Simple vs Complex Deployment Job Patterns

**Simple vs Complex Deployment Job Patterns** describes two approaches to structuring [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) for automating model version lifecycle management. The choice between patterns depends on deployment requirements such as staged rollouts, metrics collection, and rollback capabilities.

## Simple Deployment Job Pattern

A simple deployment job consists of three fundamental steps: evaluation, approval, and deployment. This pattern is suitable for straightforward model deployment workflows where a model version moves directly from evaluation to production after approval. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Structure

The simple pattern includes the following tasks:
- **Evaluation**: Calls `mlflow.evaluate` to produce validation metrics on the inputted model version.
- **Approval**: Allows a privileged user to determine if the metrics are satisfactory and, if so, approve the model.
- **Deployment**: Deploys the approved model version to a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint.

### Visual Representation

![A simple deployment job consisting of evaluation, approval, and deployment tasks.](https://docs.databricks.com/aws/en/assets/images/simple-deployment-job-b9fca062d7a71439d2273cf1e8672e4f.png)

## Complex Deployment Job Pattern

A complex deployment job extends the simple pattern by introducing staged rollouts and metrics collection. This pattern is designed for production environments that require gradual deployment, monitoring, and rollback capabilities. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Structure

A complex deployment job might include additional tasks after the approval step:
- Deploy the model to 1% of traffic.
- Deploy the model to 10% of traffic.
- Collect and check metrics.
- Decide whether to proceed or rollback.
- Either deploy the model to 100% of traffic or rollback the model.

### Visual Representation

![A complex deployment job that includes staged rollout and metrics collection.](https://docs.databricks.com/aws/en/assets/images/complex-deployment-job-9ea629abdeae12c52b0fd7f079d78a7e.png)

## When to Use Each Pattern

| Pattern | When to Use |
|---------|-------------|
| **Simple** | Straightforward model deployments where the model moves directly to production after approval. Suitable for lower-risk scenarios or when staged rollouts are not required. |
| **Complex** | Production environments requiring gradual rollout, metrics monitoring, and automated rollback decisions. Recommended for high-stakes deployments where risk mitigation is critical. |

## Customization

Both patterns can be customized to fit specific use cases. The example notebooks provided in the deployment job template can be adapted with additional tasks or modified task sequences. For instance, you may want to include more tasks if you have a more complex rollout plan. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md)
- [Unity Catalog Models](/concepts/unity-catalog-for-ml-models.md)
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Databricks Model Serving](/concepts/databricks-model-serving.md)
- [MLflow Model Evaluation](/concepts/mlflow-evaluation-ui.md)
- Model Approval Workflow
- Staged Rollout

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
