---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a42fcf563aa2df71f01cf98e245940aaf1b9f98a98d9a17bad77c462add22a97
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-serverless-budget-policy-fallback-error
    - DSBPFE
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Default Serverless Budget Policy Fallback Error
description: A 403 Forbidden error that occurs when a workspace has disabled the default serverless budget policy and MLflow cannot automatically select a policy for an experiment.
tags:
  - databricks
  - error-handling
  - serverless
  - budget-policy
timestamp: "2026-06-19T17:50:56.685Z"
---

# Default Serverless Budget Policy Fallback Error

The **Default Serverless Budget Policy Fallback Error** is a 403 permission-denied failure that occurs when [MLflow](/concepts/mlflow.md) attempts to run serverless workloads—such as scheduled scorers, synthetic evaluation set generation, or agent evaluation—against an experiment, but the workspace's default serverless budget policy is disabled and no alternative policy has been assigned to the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error Message

When this error occurs, MLflow returns:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Cause

By default, MLflow serverless workloads use the workspace's default serverless budget policy. If the workspace disables that default policy—for example, when each user and service principal must choose a dedicated policy—MLflow cannot select a fallback policy. As a result, registering a scorer or running an evaluation fails with the 403 error shown above. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:

- Scheduled scorers (production monitoring)
- Synthetic evaluation set generation
- Agent evaluation

## Solution

Set a serverless budget policy on the MLflow experiment. Once a policy is assigned, MLflow uses that policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow will use this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy with the API

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

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations.
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring workflows affected by this policy.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow affected by this policy.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
