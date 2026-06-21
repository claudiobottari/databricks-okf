---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1df78979a672de92e002eae867412b61654f97a3f14c9c2fd87fec5509ddf3bc
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - synthetic-evaluation-set-generation-databricks
    - SESG(
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Synthetic Evaluation Set Generation (Databricks)
description: A serverless workload that generates synthetic evaluation datasets for GenAI agent evaluation, controlled via budget policies on experiments.
tags:
  - databricks
  - genai
  - evaluation
  - serverless
timestamp: "2026-06-18T11:08:11.301Z"
---

# Synthetic Evaluation Set Generation (Databricks)

**Synthetic Evaluation Set Generation** is a Databricks feature that creates synthetic evaluation datasets for assessing generative AI applications. It is part of the MLflow GenAI evaluation and monitoring ecosystem and runs serverless workloads against an MLflow experiment.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Overview

Synthetic evaluation set generation automatically produces test data (e.g., question‑answer pairs or prompt‑response examples) that can be used to evaluate the quality, safety, or correctness of a generative AI application. The generated sets are stored in the experiment and can be consumed by [agent evaluation](/concepts/mlflow-agent-evaluation.md) or other evaluation workflows.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Because the generation process uses serverless compute, it is subject to workspace budget policies. By default, the generation uses the workspace’s default serverless budget policy. If that policy is disabled (for example, because each user or service principal must manually select a dedicated policy), the generation fails with a `403 PERMISSION_DENIED` error. To unblock the workflow, you must explicitly assign a budget policy to the experiment.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

- You must have permission to use the serverless budget policy you intend to assign. Users and service principals can only assign a policy they are entitled to use.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Configuring the Budget Policy for an Experiment

You can set the budget policy on an MLflow experiment either through the UI or via the MLflow API. Once set, all serverless workloads created from that experiment – including synthetic evaluation set generation, [scheduled scorers](/concepts/scheduled-scorers-mlflow-genai.md), and [agent evaluation](/concepts/mlflow-agent-evaluation.md) – will use the specified policy.

### Using the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, locate the **Budget policy** dropdown.
3. Select a policy that you have access to use.

MLflow uses the selected policy for all subsequent serverless workloads created on behalf of the experiment.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Using the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment – such as synthetic evaluation set generation – use the specified policy. To find the ID of a budget policy, see [Attribute usage with serverless usage policies](https://docs.databricks.com/aws/en/admin/usage/budget-policies).^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Integration with Other Workloads

Synthetic evaluation set generation is one of several serverless workloads that share the same experiment-level budget policy configuration. The same policy also governs:

- [Scheduled scorers](/concepts/scheduled-scorers-mlflow-genai.md) used for production monitoring.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) runs that evaluate generative AI applications.

Setting the policy once on the experiment covers all three workload types.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) – the container for runs, evaluations, and generated datasets.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – controls cost and resource allocation for serverless compute.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – evaluation of generative AI agents using synthetic or real data.
- [Scheduled Scorers](/concepts/scheduled-scorers-mlflow-genai.md) – automated scoring functions for production monitoring.
- [Production Monitoring](/concepts/production-monitoring.md) – ongoing assessment of generative AI apps in production.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
