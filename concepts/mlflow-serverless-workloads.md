---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d8e4865c6b8a8829e32de6ef78c43e6966a41da323c478c2208ea24efb5a65c3
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-serverless-workloads
    - MSW
    - Serverless workloads
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Serverless Workloads
description: Serverless workloads that MLflow can run against an experiment, including scheduled scorers, synthetic evaluation set generation, and agent evaluation.
tags:
  - mlflow
  - serverless
  - workloads
  - gen-ai
timestamp: "2026-06-19T17:51:16.006Z"
---

# MLflow Serverless Workloads

**MLflow Serverless Workloads** are automated compute tasks that run on serverless infrastructure, triggered by [MLflow experiments](/concepts/mlflow-experiment.md) for activities like [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md), [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md), and [Agent Evaluation](/concepts/mlflow-agent-evaluation.md). These workloads require explicit budget policy configuration to control spending and resource allocation.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Overview

MLflow automatically creates serverless workloads when performing evaluation and monitoring tasks on behalf of experiments. These workloads execute on Databricks Serverless Compute, which provides on-demand, managed infrastructure without requiring users to provision or manage clusters.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Types of Serverless Workloads

The following MLflow operations generate serverless workloads:

- **Scheduled scorers** — Continuously evaluate model performance in production environments using [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md).^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Synthetic evaluation set generation** — Creates synthetic datasets for testing and evaluating GenAI agents and models.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Agent evaluation** — Runs offline evaluations of GenAI agents using [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) APIs.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Budget Policy Requirements

By default, MLflow serverless workloads use the workspace's default [Serverless Budget Policy](/concepts/serverless-budget-policy.md). If the workspace disables this default policy — requiring each user or service principal to select a dedicated policy — MLflow cannot use a fallback. This results in a 403 PERMISSION_DENIED Serverless Budget Policy Error and the workload fails.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting a Budget Policy

To unblock serverless workloads, assign a budget policy to the MLflow experiment. This can be done through the UI or the API:

**UI Method:** Open the MLflow experiment and set the **Budget policy** in the experiment **Details** panel to a policy you have access to use.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

**API Method:** Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment:^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they wish to assign. They can only set a policy that they are entitled to use.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Scheduled scoring workflows that use serverless compute
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Offline evaluation workflows that use serverless compute
- [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md) — Dataset creation workflows that use serverless compute
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no budget policy is available

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
