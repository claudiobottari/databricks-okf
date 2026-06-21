---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 958444bc80f1ebe56e817c9905186b3c8d5e01ad570275ef9eead9249470d05a
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-workload-creation-policy-tag
    - MEWCPT
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Workload Creation Policy Tag
description: The mlflow.workload_creation_policy_id experiment tag used to bind a serverless budget policy to an MLflow experiment via API.
tags:
  - mlflow
  - api
  - tag
  - configuration
timestamp: "2026-06-19T14:23:52.227Z"
---

# MLflow Experiment Workload Creation Policy Tag

The **MLflow Experiment Workload Creation Policy Tag** (`mlflow.workload_creation_policy_id`) is an [MLflow Experiment](/concepts/mlflow-experiment.md) tag that specifies which [Serverless Budget Policy](/concepts/serverless-budget-policy.md) MLflow should use for serverless workloads it creates on behalf of that experiment. When set, MLflow applies the designated policy to every serverless workload — including scheduled scorers, synthetic evaluation set generation, and agent evaluation — that originates from the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Purpose

By default, MLflow serverless workloads use the workspace’s default serverless budget policy. If a workspace disables that default policy — for example, requiring each user or service principal to select a dedicated policy — MLflow cannot fall back to any policy. This causes operations like registering a scorer or running an evaluation to fail with a `403 PERMISSION_DENIED` error. Setting the `mlflow.workload_creation_policy_id` tag on the experiment unblocks these workflows by explicitly assigning a policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the Tag

### Using the MLflow API

The tag is set with `mlflow.set_experiment_tag()`:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment — such as `Scorer.register()` — use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Using the Databricks UI

The same effect can be achieved without code:

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** dropdown to a policy you have access to use.

MLflow then uses that policy for all serverless workloads it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Users and service principals must have permission to use the budget policy they intend to assign. Only policies that the entity is entitled to use can be set. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no policy is available.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The broader mechanism for controlling serverless spending.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational container for runs, models, and evaluations.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — A workload type affected by this tag.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Another affected workload type.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Also subject to the policy.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
