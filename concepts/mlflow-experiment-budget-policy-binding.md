---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f97747328900cb3b9a5cda8655fb571190bdccab21208184bf292839d57f847
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-budget-policy-binding
    - MEBPB
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Budget Policy Binding
description: The practice of assigning a serverless budget policy to an MLflow experiment so that all serverless workloads spawned from that experiment use the designated policy instead of the workspace default.
tags:
  - mlflow
  - experiment-management
  - databricks
timestamp: "2026-06-18T14:43:07.100Z"
---

# MLflow Experiment Budget Policy Binding

**MLflow Experiment Budget Policy Binding** refers to assigning a specific [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to an [MLflow Experiment](/concepts/mlflow-experiment.md) so that [MLflow](/concepts/mlflow.md) uses that policy whenever it creates serverless workloads on behalf of the experiment. This binding is required when the workspace’s default serverless budget policy is disabled and MLflow cannot automatically select a fallback policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Purpose

By default, MLflow serverless workloads — such as [scheduled scorers](/concepts/scheduled-scorers-mlflow-genai.md) for [Production Monitoring](/concepts/production-monitoring.md), [synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md), and [agent evaluation](/concepts/mlflow-agent-evaluation.md) — use the workspace’s default serverless budget policy. If an organization disables the default policy (e.g., requiring each user or service principal to choose a dedicated policy), MLflow cannot pick a fallback. In this scenario, attempts to register a scorer or run an evaluation fail with a `403 PERMISSION_DENIED` error: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

Binding a policy to the experiment unblocks these workflows. MLflow then uses the specified policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Users and service principals must have permission to use the budget policy they intend to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Methods

### Set in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow will use this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Set with the API

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

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – The policy that governs spending for serverless workloads.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – The exact error that occurs when no valid policy is bound.
- [Production Monitoring](/concepts/production-monitoring.md) – Scheduled scoring workflow affected by this binding.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Evaluation workflow affected by this binding.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) – Another workload type that requires a budget policy.
- [MLflow experiments](/concepts/mlflow-experiment.md) – The organizational unit to which the policy is bound.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
