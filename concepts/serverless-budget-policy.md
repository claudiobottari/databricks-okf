---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6ad49ebb39d970660a40df50a3716a4649c57a145028aad964a5cc768fd67ef3
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-budget-policy
    - SBP
    - Serverless budget policies
    - Serverless budget policy (general)
    - serverless budget policies
    - serverless usage policy
    - Budget Policies
    - Databricks serverless budget policy
    - serverless-budget-policy-databricks
    - SBP(
    - serverless-budget-policy-for-mlflow-experiments
    - SBPFME
    - Configure a Serverless Budget Policy for an MLflow Experiment
    - Configure a serverless budget policy for an MLflow experiment
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless Budget Policy
description: A Databricks policy that controls cost and resource allocation for serverless workloads, which can be assigned to MLflow experiments to govern serverless compute usage.
tags:
  - databricks
  - serverless
  - cost-management
  - mlflow
timestamp: "2026-06-18T14:43:03.119Z"
---

# Serverless Budget Policy

A **Serverless Budget Policy** is a mechanism in Databricks that governs the spending of serverless workloads, such as those created by MLflow for scoring, evaluation, and synthetic data generation. When a serverless budget policy is applied to an MLflow experiment, MLflow uses that policy for every serverless workload it runs against that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Purpose

By default, serverless workloads use the workspace’s default serverless budget policy. If the workspace disables the default policy — for example, to require each user or service principal to select a dedicated policy — MLflow cannot fall back to a default and will fail with a **403 PERMISSION_DENIED** error when attempting to register a scorer, run an agent evaluation, or generate a synthetic evaluation set. Setting an explicit budget policy on the experiment prevents this error and ensures that serverless workloads can proceed. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Which workloads are affected?

The following serverless workloads created by MLflow are subject to the budget policy:

- **Scheduled scorers** used in production monitoring.
- **Synthetic evaluation set generation**.
- **Agent evaluation** (offline evaluation of GenAI agents).

All of these workloads require a budget policy to be assigned either at the workspace level (default) or explicitly on the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Users and service principals must have permission to use the budget policy they intend to assign. They can only set a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the budget policy

### In the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

After this, MLflow uses the selected policy for all serverless workloads it creates on behalf of that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### With the API

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

## Related concepts

- 403 PERMISSION_DENIED Serverless Budget Policy Error – the error that occurs when no policy is available.
- [MLflow experiments](/concepts/mlflow-experiment.md) – the organizational unit that holds the policy assignment.
- [Serverless workloads](/concepts/mlflow-serverless-workloads.md) – the compute resources governed by the budget policy.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – an example workload that requires a budget policy.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – another workload affected by this policy.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) – a third workload type.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
