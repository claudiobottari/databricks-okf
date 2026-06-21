---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bb4a654de6e70155463483f5b4d8c376aa75a453486900407a4a1973426e6328
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-budget-policy-databricks
    - SBP(
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless Budget Policy (Databricks)
description: A policy that controls which budget policy is used for serverless workloads in Databricks, including those run by MLflow experiments.
tags:
  - databricks
  - serverless
  - cost-management
  - budget-policy
timestamp: "2026-06-19T17:50:36.653Z"
---

```markdown
---
title: Serverless Budget Policy (Databricks)
summary: A policy that controls which budget constraints are applied to serverless workloads associated with an MLflow experiment in Databricks.
sources:
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:22:33.551Z"
updatedAt: "2026-06-19T09:22:33.551Z"
tags:
  - databricks
  - budget-management
  - serverless
  - mlflow
aliases:
  - serverless-budget-policy-databricks
  - SBP
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Serverless Budget Policy (Databricks)

A **serverless budget policy** in Databricks is a configuration that controls spending on serverless workloads by specifying which budget constraints apply. When assigned to an [[MLflow experiment]], the policy determines how MLflow manages resource usage and cost limits for all serverless workloads it creates for that experiment, such as scheduled scorers, synthetic evaluation set generation, and agent evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Overview

By default, serverless workloads created by MLflow use the workspace’s default serverless budget policy. If the workspace administrator disables the default policy — for example, to require each user or service principal to select a dedicated policy — MLflow cannot automatically fall back to a policy and will fail when attempting to register a scorer or run evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Error and Cause

When the default policy is disabled and no alternative policy is set on the experiment, MLflow returns the following 403 error:

```
403 Client Error: Forbidden  
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

This error blocks the creation of serverless workloads including:

- [[Production monitoring|Scheduled scorers (production monitoring)]]
- [[Synthetic Evaluation Data Generation|Synthetic evaluation generation]]
- [[MLflow Agent Evaluation|Agent evaluation]]

## Setting the Budget Policy

To resolve the error and control which policy MLflow uses, set a serverless budget policy on the experiment. Once set, MLflow applies that policy to every serverless workload it creates for the experiment thereafter. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Requirements

- The user or service principal assigning the policy must have permission to use that budget policy. They can only assign a policy they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Using the UI

1. Open the MLflow experiment.
2. In the **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow uses the selected policy for subsequent serverless workloads. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Using the API

Use `mlflow.set_experiment_tag()` to set the tag `mlflow.workload_creation_policy_id` on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

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

- [[Serverless Budget Policy|Serverless budget policy (general)]] – The broader concept of budget policies for serverless workloads in Databricks.
- [[MLflow Experiment|MLflow experiments]] – The organizational unit for MLflow runs and evaluations.
- [[Production monitoring]] – Scheduled scoring workflows affected by this policy.
- [[Synthetic Evaluation Data Generation|Synthetic evaluation generation]] – Workflow that generates evaluation sets, affected by the policy.
- [[MLflow Agent Evaluation|Agent evaluation]] – Evaluation workflow for GenAI agents, affected by the policy.
- Scorer management – Management of production scorers that rely on budget policies.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
```

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
