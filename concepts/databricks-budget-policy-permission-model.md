---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e2d3e2c0d7ff46b6978382b42fe57eb10de03f4ee9f296fc416d4ca34c85af8
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-budget-policy-permission-model
    - DBPPM
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Budget Policy Permission Model
description: The requirement that users and service principals can only assign a budget policy they are entitled to use, governing who can set serverless budget policies on experiments.
tags:
  - databricks
  - permissions
  - access-control
  - budget-policy
timestamp: "2026-06-19T14:24:34.336Z"
---

# Databricks Budget Policy Permission Model

The **Databricks Budget Policy Permission Model** governs how users and service principals interact with [serverless budget policies](/concepts/serverless-budget-policy.md) to control spending on serverless workloads. It defines who can assign policies, which policies they can use, and what happens when no valid policy is available.

## Core Permissions

### Policy Usage Entitlement

Users and service principals can only assign a budget policy that they are **entitled to use**. The system enforces that an entity must have permission to use a policy before they can set it on an experiment or workload. This prevents unauthorized users from assigning policies they should not control. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Default Policy Behavior

By default, serverless workloads — including [scheduled scorers](/concepts/scheduled-scorers-mlflow-genai.md), [synthetic evaluation set generation](/concepts/synthetic-evaluation-data-generation.md), and [agent evaluation](/concepts/mlflow-agent-evaluation.md) — use the workspace's default serverless budget policy. This default policy provides a baseline for all users and service principals who have not explicitly assigned a different policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Fallback Mechanism

When a workspace disables its default serverless budget policy — for example, when organizational policy requires each user or service principal to select a dedicated policy — the fallback mechanism becomes critical. If no default policy exists and no alternative policy has been assigned to the experiment, MLflow cannot proceed with serverless workload creation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Failure Mode: 403 PERMISSION_DENIED

If a user or service principal attempts to create a serverless workload without a valid policy and without an available default, the system returns a 403 PERMISSION_DENIED Serverless Budget Policy Error:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Policy Assignment Model

### Experiment-Level Assignment

The permission model allows policy assignment at the [MLflow Experiment](/concepts/mlflow-experiment.md) level. Users can set a budget policy on an experiment either through the UI or via the API. This assignment overrides any default policy for workloads running against that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### API-Based Assignment

When assigning a policy via the API, the user must provide a valid **policy ID** and have permission to use that policy:

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent serverless workloads created from that experiment (such as `Scorer.register()`) use the specified policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Scope of Policy Enforcement

The permission model applies to the following serverless workloads:

- **Scheduled scorers** — Used in [Production Monitoring](/concepts/production-monitoring.md)
- **Synthetic evaluation set generation** — Automated test data creation
- **Agent evaluation** — Quality assessment of GenAI agents

All of these workloads require a valid budget policy assignment to proceed. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Key Principles

1. **Entitlement-based access**: Users can only assign policies they are entitled to use.
2. **Hierarchical override**: Experiment-level policy assignments override workspace defaults.
3. **No implicit fallback**: If the default policy is disabled and no experiment policy is set, workloads fail with a permission error.
4. **Workload consistency**: Once assigned, MLflow uses the same policy for every serverless workload it creates for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The policy object that controls spending limits
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no valid policy is available
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit that holds policy assignments
- Databricks Usage Policies — Broader framework for cost and resource governance
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Scheduled scoring workflows affected by budget policies
- Attribute usage with serverless usage policies — How to find policy IDs for API assignment

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
