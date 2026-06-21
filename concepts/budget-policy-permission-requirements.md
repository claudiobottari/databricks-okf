---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0c80ee9128be19f7e7147cd4d217e0c8a09b454b5ab0800b497cd724824d3815
  pageDirectory: concepts
  sources:
    - configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - budget-policy-permission-requirements
    - BPPR
  citations:
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Budget Policy Permission Requirements
description: Users and service principals must have explicit entitlement to use a budget policy before they can assign it to an MLflow experiment.
tags:
  - databricks
  - permissions
  - iam
timestamp: "2026-06-19T09:22:49.191Z"
---

# Budget Policy Permission Requirements

**Budget Policy Permission Requirements** define the access control conditions that users and service principals must satisfy before they can assign a [Serverless Budget Policy](/concepts/serverless-budget-policy.md) to an [MLflow Experiment](/concepts/mlflow-experiment.md). These requirements ensure that only authorized principals can select which budget policy governs serverless workloads such as scheduled scorers, synthetic evaluation generation, and agent evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Permission Requirement

Users and service principals **must have permission to use the budget policy they want to set**. They can only assign a policy to an experiment if they are entitled to use that policy. This entitlement is determined by the workspace’s budget policy configuration and the principal’s role or membership in groups that are authorized for the policy. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

If a workspace disables the default serverless budget policy (for example, when each user and service principal must select a dedicated policy), MLflow cannot pick a fallback policy automatically. In that situation, setting an explicit policy on the experiment—backed by the principal’s permission to use that policy—is required to unblock serverless workflows. Without a correctly assigned policy, attempts to register a scorer or run an evaluation fail with a `403 PERMISSION_DENIED` error. See 403 PERMISSION_DENIED Serverless Budget Policy Error for more detail. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## How to Ensure Compliance

1. **Verify existing entitlements.** Consult your workspace administrator or the documentation on attribute usage with serverless usage policies to confirm which budget policies you are permitted to use.
2. **Assign a permitted policy.** Use the MLflow experiment UI (set the **Budget policy** in the **Details** panel) or the API (`mlflow.set_experiment_tag()` with key `mlflow.workload_creation_policy_id` and a policy ID you are entitled to use).
3. **Test the assignment.** After setting the policy, attempt a serverless workload (e.g., `Scorer.register()`) to confirm that the error no longer occurs.

The permission check is applied at the time of assignment; if a principal later loses access to the policy, new serverless workloads may also fail. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) — The control mechanism for serverless workload spending.
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit on which budget policies are set.
- Attribute usage with serverless usage policies — How to find policy IDs and understand entitlements.
- 403 PERMISSION_DENIED Serverless Budget Policy Error — The error that occurs when no valid policy is available.
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduled scoring workflows affected by budget policy configuration.
- [Agent evaluation](/concepts/mlflow-agent-evaluation.md) — Evaluation workflow affected by budget policy configuration.
- [Synthetic evaluation generation](/concepts/synthetic-evaluation-data-generation.md) — Another affected workload type.

## Sources

- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
