---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7e21fde7bfbcbf8ea8842100bbcf1469fccd2878c8cc7eb440f083c5e6883bf6
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-serverless-workloads
    - DMSW
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks MLflow Serverless Workloads
description: Serverless workloads managed by MLflow on Databricks, including scheduled scorers, synthetic evaluation set generation, and agent evaluation.
tags:
  - databricks
  - mlflow
  - serverless
  - workloads
timestamp: "2026-06-18T11:08:11.293Z"
---

# Databricks MLflow Serverless Workloads

**Databricks MLflow Serverless Workloads** are serverless compute tasks initiated by MLflow for GenAI evaluation and monitoring. They are automatically created and managed by MLflow, using serverless infrastructure in the Databricks environment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Included Workloads

The following MLflow operations run as serverless workloads:

- **Scheduled scorers** — recurring production monitoring jobs that evaluate model outputs using [Code-based Scorers](/concepts/code-based-scorers.md) registered in MLflow. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Synthetic evaluation set generation** — creation of synthetic data for [agent evaluation](/concepts/mlflow-agent-evaluation.md) pipelines. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]
- **Agent evaluation** — offline or online evaluation of GenAI applications using [MLflow evaluation](/concepts/mlflow-evaluation-ui.md). ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

All of these workloads depend on the same [Databricks serverless budget policy](/concepts/serverless-budget-policy.md) to govern cost and usage limits.

## Controlling the Budget Policy

Each MLflow experiment can be assigned a serverless budget policy that controls which policy MLflow uses for every serverless workload created for that experiment. By default, workloads use the workspace’s **default serverless budget policy**. If the workspace does not have a default policy (for example, when each user or service principal must select a dedicated policy), MLflow cannot pick a fallback and operations fail. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have permission to use.

MLflow will then use that policy for all subsequent serverless workloads created on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Setting the Policy with the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that trigger serverless workloads (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies).

## Error Handling

If no valid budget policy is available — either because the workspace has no default policy and no policy has been set on the experiment — MLflow returns a `403 PERMISSION_DENIED` error with the message:

```
Unable to use fallback policies, please manually select a policy.
```

Setting a budget policy on the experiment unblocks these workflows. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

To assign a budget policy to an experiment, you must have the necessary permissions to use that policy. Users and service principals can only assign a policy they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) — The logical grouping under which serverless workloads run
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — Controls cost and usage for serverless workloads
- [Scheduled Scorers](/concepts/scheduled-scorers-mlflow-genai.md) — Production monitoring jobs that use serverless compute
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation pipeline that may trigger serverless workloads
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions that can run as serverless workloads
- [Synthetic Evaluation Set Generation](/concepts/synthetic-evaluation-data-generation.md) — Data generation feature that uses serverless compute

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
