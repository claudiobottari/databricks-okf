---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4989187f98b27d82585c8888b60dfbbabf97c054b5dc40fc309d11f815ff4b03
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflowworkload_creation_policy_id-tag
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: mlflow.workload_creation_policy_id Tag
description: An MLflow experiment tag used to specify the serverless budget policy ID that MLflow will use for serverless workloads created from that experiment.
tags:
  - mlflow
  - api
  - tag
  - budget-policy
timestamp: "2026-06-19T17:51:21.987Z"
---

# `mlflow.workload_creation_policy_id` Tag

The **`mlflow.workload_creation_policy_id`** tag is a special MLflow experiment tag that associates a specific [Serverless Budget Policy](/concepts/serverless-budget-policy.md) ID with an [MLflow Experiment](/concepts/mlflow-experiment.md). When set, MLflow uses the specified policy for all serverless workloads it creates for that experiment, overriding the workspace's default policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Purpose

This tag is essential when a workspace disables its default serverless budget policy — for example, when each user and service principal must select a dedicated policy. Without a fallback policy, operations like registering a scorer or running an evaluation fail with a 403 PERMISSION_DENIED Serverless Budget Policy Error:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

Setting the tag unblocks these workflows by instructing MLflow to use the designated policy for every serverless workload launched for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Affected workloads include:
- Scheduled scorers for [Production Monitoring](/concepts/production-monitoring.md)
- [Synthetic evaluation set generation](/concepts/synthetic-evaluation-data-generation.md)
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md)

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Only users and service principals that are entitled to use a budget policy can assign it via this tag. You must have permission to use the policy you intend to set. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the Tag

### Via the UI

1. Open the MLflow experiment.
2. In the experiment's **Details** panel, set the **Budget policy** field to a policy you have access to use.

MLflow will use this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Via the API

Use [`mlflow.set_experiment_tag()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment_tag) to set the `mlflow.workload_creation_policy_id` tag on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment — such as `Scorer.register()` — use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Finding the Policy ID

To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The Databricks resource that controls serverless compute costs.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The container that this tag applies to.
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no policy is set.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — A workflow that uses this tag for scheduling scorers.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — An evaluation workflow affected by this tag.
- [Synthetic Evaluation Set Generation](/concepts/synthetic-evaluation-data-generation.md) — Another workload that respects the tag.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
