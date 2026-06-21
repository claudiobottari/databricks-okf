---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c6b9daf5513386bce10f947f637d21f51f099d6e0662d0a6824727f3a68b90c
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - workspace-default-serverless-budget-policy
    - WDSBP
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Workspace Default Serverless Budget Policy
description: The fallback budget policy applied to MLflow serverless workloads when no specific policy is assigned to an experiment; if disabled, workloads fail with a 403 error.
tags:
  - databricks
  - serverless
  - default-policy
  - error-handling
timestamp: "2026-06-18T14:43:01.557Z"
---

# Workspace Default Serverless Budget Policy

**Workspace Default Serverless Budget Policy** refers to the budget policy that a Databricks workspace applies by default to serverless workloads, including those created by [MLflow](/concepts/mlflow.md) for tasks such as scheduled scoring, synthetic evaluation set generation, and agent evaluation. When this default policy is enabled, MLflow automatically uses it for serverless workloads it runs against experiments. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Behavior

By default, serverless workloads created by MLflow use the workspace's default serverless budget policy. This allows MLflow to automatically select a policy without requiring manual configuration on each experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Disabling the Default Policy

Some workspaces disable the default serverless budget policy — for example, when each user and service principal must select a dedicated policy. When the default policy is disabled and no alternative policy has been assigned to the experiment, MLflow cannot pick a fallback. This results in a 403 PERMISSION_DENIED Serverless Budget Policy Error when attempting to register a scorer or run an evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

The error message returned is:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Resolution

When the workspace default policy is disabled, you must set a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) directly on the MLflow experiment. This can be done either through the UI (in the experiment **Details** panel) or via the API using `mlflow.set_experiment_tag()` with the `mlflow.workload_creation_policy_id` tag. After the policy is set, MLflow uses that specified policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when the default policy is disabled and no fallback is available
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring workflows affected by this policy
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow affected by this policy
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
