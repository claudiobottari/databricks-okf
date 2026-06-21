---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 278e4de8c1c28f6b2a9d4d618aabe6f968e5b8f4e655174dfc6bd35f3949a874
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serverless-budget-policy-permissions
    - SBPP
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Serverless Budget Policy Permissions
description: The requirement that users and service principals must be entitled to use a budget policy before they can assign it to an MLflow experiment.
tags:
  - databricks
  - permissions
  - iam
  - budget-policy
timestamp: "2026-06-19T17:50:58.666Z"
---

# Serverless Budget Policy Permissions

**Serverless Budget Policy Permissions** control which budget policy [MLflow](/concepts/mlflow.md) uses when it creates serverless workloads on behalf of an experiment. These permissions ensure that MLflow has an authorised policy to bill against, preventing errors when the workspace’s default policy is disabled. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## How the Error Occurs

By default, MLflow serverless workloads — such as scheduled scorers, synthetic evaluation set generation, and agent evaluation — use the workspace’s default serverless budget policy. If the workspace disables that default policy (for example, when each user or service principal must select a dedicated policy), MLflow cannot choose a fallback. Attempting to register a scorer or run an evaluation then fails with: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

## Requirements

Users and service principals must have explicit permission to use the budget policy they intend to assign. They can only set a policy that they are entitled to use. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Setting the Budget Policy

To resolve the error, set a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) on the MLflow experiment. After the policy is set, MLflow uses it for every serverless workload it creates for that experiment.

### Via the UI

1. Open the MLflow experiment.
2. In the experiment **Details** panel, set the **Budget policy** to a policy you have access to use.

MLflow will apply this policy for serverless workloads it creates on behalf of the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Via the API

Use `mlflow.set_experiment_tag()` to set the `mlflow.workload_creation_policy_id` tag on the experiment: ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

```python
import mlflow

mlflow.set_experiment_tag(
    experiment_id="<your-experiment-id>",
    key="mlflow.workload_creation_policy_id",
    value="<your-policy-id>",
)
```

After the tag is set, subsequent calls that create serverless workloads from the experiment (such as `Scorer.register()`) use the specified policy. To find the ID of a budget policy, see the documentation on attribute usage with serverless usage policies. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [MLflow experiments](/concepts/mlflow-experiment.md) – The organisational unit that holds the policy tag.
- [Production Monitoring](/concepts/production-monitoring.md) – A workflow (scheduled scorers) affected by this permission error.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) – Another workflow that requires a valid policy.
- [Synthetic evaluation set generation](/concepts/synthetic-evaluation-data-generation.md) – Also affected when no policy is assigned.
- 403 PERMISSION_DENIED Serverless Budget Policy Error – The specific error returned.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
