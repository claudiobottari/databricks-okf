---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 03dac7bcb7bbe8b88984c34d4b360700bbc8f4d77915e15eb8492d150ca831e4
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-budget-policy-for-mlflow-experiments
    - SBPFME
    - Configure a Serverless Budget Policy for an MLflow Experiment
    - Configure a serverless budget policy for an MLflow experiment
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless Budget Policy for MLflow Experiments
description: A policy that controls which Databricks serverless budget policy MLflow uses for serverless workloads associated with an MLflow experiment.
tags:
  - databricks
  - mlflow
  - budget-policy
  - serverless
timestamp: "2026-06-18T11:07:56.154Z"
---

# Serverless Budget Policy for MLflow Experiments

A **serverless budget policy** on an [MLflow Experiment](/concepts/mlflow-experiment.md) controls which budget policy [MLflow](/concepts/mlflow.md) uses for serverless workloads it creates against that experiment. Affected workloads include [scheduled scorers](/concepts/scheduled-scorers-mlflow-genai.md) for production monitoring, [synthetic evaluation set generation](/concepts/synthetic-evaluation-data-generation.md), and [agent evaluation](/concepts/mlflow-agent-evaluation.md). ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Why a dedicated policy is needed

By default, these serverless workloads use the workspace's default serverless budget policy. If the workspace disables the default policy (for example, when each user and service principal must select a dedicated policy), MLflow cannot pick a fallback. In that case, registering a scorer or running an evaluation fails with the following error: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

Setting a budget policy directly on the experiment unblocks these workflows. MLflow then uses that policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

You must have permission to use the budget policy you intend to set. Users and service principals can only assign a policy they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the budget policy in the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow uses this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the budget policy with the API

Use [`mlflow.set_experiment_tag()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.set_experiment_tag) to set the `mlflow.workload_creation_policy_id` tag on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see Attribute usage with serverless usage policies in the Databricks documentation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — general concept of budget policies for serverless workloads
- [MLflow Experiment](/concepts/mlflow-experiment.md) — the experiment that hosts MLflow runs and evaluations
- [Production Monitoring](/concepts/production-monitoring.md) — using scheduled scorers on inference tables
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — evaluating GenAI applications
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — the `mlflow.genai.evaluate()` API

## Next steps

- Monitor GenAI apps in production
- Manage production scorers

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
