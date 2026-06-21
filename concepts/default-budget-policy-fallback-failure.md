---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e521b0dbbc4fae6011bd03e74d329508a4e97b2d8838b6baff991240dd0c2c04
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - default-budget-policy-fallback-failure
    - DBPFF
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Default Budget Policy Fallback Failure
description: When a Databricks workspace disables the default serverless budget policy, MLflow fails to register scorers or run evaluations unless a policy is explicitly set on the experiment.
tags:
  - databricks
  - error-handling
  - budget-policies
timestamp: "2026-06-19T09:22:40.496Z"
---

---

title: Default Budget Policy Fallback Failure
summary: An error that occurs when MLflow serverless workloads (e.g., scheduled scorers, synthetic evaluation generation, agent evaluation) cannot find a fallback budget policy because the workspace has disabled the default serverless budget policy.
sources:
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:08:33.206Z"
updatedAt: "2026-06-18T11:08:33.206Z"
tags:
  - databricks
  - error
  - troubleshooting
  - mlflow
  - serverless
aliases:
  - default-budget-policy-fallback-failure
  - DBFF
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Default Budget Policy Fallback Failure

The **Default Budget Policy Fallback Failure** is a specific 403 PERMISSION_DENIED Serverless Budget Policy Error that occurs when MLflow attempts to run a serverless workload — such as a scheduled scorer for production monitoring, synthetic evaluation set generation, or agent evaluation — but the workspace’s default serverless budget policy has been disabled and no alternative (fallback) policy is available. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error Message

When this failure occurs, MLflow returns the following HTTP 403 error:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Cause

By default, serverless workloads created by MLflow use the workspace's default serverless budget policy. If the workspace disables the default policy — for example, to enforce that each user or service principal must select a dedicated policy — MLflow cannot automatically select a fallback policy. This results in a permission denied error when attempting to register a scorer or run an evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:

- Scheduled scorers (production monitoring)
- Synthetic evaluation set generation
- Agent evaluation

## Solution

Set a serverless budget policy directly on the MLflow experiment. MLflow will then use that specified policy for every serverless workload it creates for the experiment, bypassing the need for a fallback to the default policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

Users and service principals must have permission to use the budget policy they intend to assign. They can only set a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Budget Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow uses this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

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

After the tag is set, subsequent calls that create serverless workloads from the experiment (e.g., `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit for MLflow runs and evaluations.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Scheduled scoring workflows that are affected by this failure.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow that can trigger this failure.
- [Synthetic evaluation set generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type.
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The broader error class; this page covers the specific fallback failure scenario.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
