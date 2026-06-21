---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2412d28143b2a84621802e38ebe001428149868d672fd184a343199a5db208a8
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-budget-policy-configuration
    - MEBPC
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: MLflow Experiment Budget Policy Configuration
description: The mechanism to assign a serverless budget policy to an MLflow experiment via UI or API to control serverless workloads.
tags:
  - mlflow
  - databricks
  - configuration
  - serverless
timestamp: "2026-06-19T17:50:49.397Z"
---

```markdown
---
title: MLflow Experiment Budget Policy Configuration
summary: The process of assigning a serverless budget policy to an MLflow experiment via the UI Details panel or the mlflow.set_experiment_tag() API.
sources:
  - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:22:29.415Z"
updatedAt: "2026-06-19T09:22:29.415Z"
tags:
  - mlflow
  - configuration
  - databricks
aliases:
  - mlflow-experiment-budget-policy-configuration
  - MEBPC
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 1
---

# MLflow Experiment Budget Policy Configuration

**MLflow Experiment Budget Policy Configuration** refers to the process of assigning a [[serverless budget policy]] to an [[MLflow experiment]] to control which policy MLflow uses for serverless workloads it runs against that experiment. This configuration is necessary when a workspace disables its default serverless budget policy, preventing MLflow from automatically selecting a fallback policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Overview

By default, serverless workloads created by MLflow use the workspace's default serverless budget policy. If the workspace disables the default policy — for example, when each user and service principal must select a dedicated policy — MLflow cannot pick a fallback. This results in a 403 PERMISSION_DENIED Serverless Budget Policy Error when attempting to register a scorer or run an evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

Setting a budget policy on the experiment unblocks these workflows. MLflow then uses that policy for every serverless workload it creates for the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Affected Workloads

The following serverless workloads are affected by budget policy configuration:

- [[Scheduled Scorers (MLflow GenAI)|Scheduled scorers]] for production monitoring
- [[Synthetic Evaluation Data Generation|Synthetic evaluation set generation]]
- [[MLflow Agent Evaluation|Agent evaluation]]

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Requirements

Users and service principals must have permission to use the budget policy they want to set. They can only assign a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Configuration Methods

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

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [[Serverless budget policy]] — The control mechanism for serverless workload spending
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no policy is configured
- [[MLflow Experiment|MLflow experiments]] — The organizational unit for MLflow runs and evaluations
- [[Production monitoring]] — Scheduled scoring workflows affected by this policy
- [[MLflow Agent Evaluation|Agent evaluation]] — Evaluation workflow affected by this policy
- [[Synthetic Evaluation Data Generation|Synthetic evaluation generation]] — Another affected workload type

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
```

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
