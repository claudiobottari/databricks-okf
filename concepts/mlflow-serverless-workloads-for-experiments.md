---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 114185299d8f94b226c252e06f8842975b99a9c468f59c48f3900bd818d91732
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-serverless-workloads-for-experiments
    - MSWFE
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Serverless Workloads for Experiments
description: Serverless workloads triggered by MLflow experiments, including scheduled scorers, synthetic evaluation set generation, and agent evaluation.
tags:
  - mlflow
  - serverless
  - evaluation
  - monitoring
timestamp: "2026-06-19T14:24:05.637Z"
---

# MLflow Serverless Workloads for Experiments

**MLflow Serverless Workloads for Experiments** are on-demand, serverless compute tasks that MLflow creates automatically to support GenAI evaluation and monitoring workflows. These workloads require a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to control spending, and if no policy is available, the operations fail with a permission error.

## Types of Serverless Workloads

The following MLflow operations trigger serverless workloads against an experiment:

- **Scheduled scorers** used in [production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md).
- **Synthetic evaluation set generation** for creating test datasets.
- **Agent evaluation** for offline assessment of GenAI agents.

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Default Policy Behavior

By default, serverless workloads use the workspace’s default serverless budget policy. If a workspace disables this default — for example, because each user or service principal must select a dedicated policy — MLflow cannot pick a fallback policy. This results in the following error when registering a scorer or running an evaluation: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

## Solution: Assign a Budget Policy to the Experiment

To unblock these workflows, set a serverless budget policy directly on the MLflow experiment. MLflow will then use that policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Set the Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow uses this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Set the Policy with the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – The control mechanism for serverless workload spending.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Scheduled scoring workflows affected by this policy.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) – Automated test data creation affected by this policy.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Offline evaluation of GenAI agents affected by this policy.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – The error that occurs when the policy is missing.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
