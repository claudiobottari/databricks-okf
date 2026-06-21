---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6fbd935afcf2d3da707cb528797bf2122d26b7d9ea86431f4264fb923a34a02
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - 403-permission_denied-serverless-budget-policy-error
    - 4PSBPE
    - 101 403 PERMISSION_DENIED Serverless Budget Policy Error
    - 403 PERMISSION_DENIED Serverless Budget Policy Error
    - 403 PERMISSION_DENIED Serverless Budget Policy Error|403 PERMISSION_DENIED error
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: 403 PERMISSION_DENIED Serverless Budget Policy Error
description: An error that occurs when a workspace disables the default serverless budget policy and no fallback policy is available for MLflow serverless workloads.
tags:
  - databricks
  - error
  - troubleshooting
  - mlflow
timestamp: "2026-06-18T11:08:33.206Z"
---

# 403 PERMISSION_DENIED Serverless Budget Policy Error

The **403 PERMISSION_DENIED Serverless Budget Policy Error** occurs when [MLflow](/concepts/mlflow.md) attempts to run a serverless workload — such as a scheduled scorer, synthetic evaluation set generation, or agent evaluation — against an experiment, but the workspace's default serverless budget policy is disabled and no alternative policy has been assigned to the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error Message

When this error occurs, MLflow returns the following message:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Cause

By default, serverless workloads created by MLflow use the workspace's default serverless budget policy. If the workspace disables the default policy — for example, when each user and service principal must select a dedicated policy — MLflow cannot pick a fallback. This results in a permission denied error when attempting to register a scorer or run an evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:

- Scheduled scorers (production monitoring)
- Synthetic evaluation set generation
- Agent evaluation

## Solution

Set a serverless budget policy on the MLflow experiment to control which policy MLflow uses for serverless workloads it runs against that experiment. MLflow will then use the specified policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow will use this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy with the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

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

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring workflows affected by this policy
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow affected by this policy
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
