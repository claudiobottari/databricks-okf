---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b5b32099d07c55967d949c94c0376c332bb5d7e3370039f1be1a09a9f9bbceef
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - governed-tags-for-advanced-approvals
    - GTFAA
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Governed Tags for Advanced Approvals
description: Using Databricks governed tag policies to control who can approve deployment jobs, enabling multi-group approval workflows (e.g., separate Legal and Security gates) and preventing model owner self-approval.
tags:
  - governance
  - tags
  - mlops
timestamp: "2026-06-19T19:37:03.380Z"
---

# Governed Tags for Advanced Approvals

**Governed Tags for Advanced Approvals** is a feature in Databricks MLflow deployment jobs that allows administrators to control who can approve model versions by using governed tag policies. This enables fine-grained access control over the approval process in ML pipelines. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Overview

When using [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md), the approval mechanism relies on Unity Catalog tags to determine whether an approval task should pass or fail. By default, any user with the `APPLY TAG` permission on a Unity Catalog model can approve a model version by setting the required tag. Governed tags add an additional layer of security by allowing administrators to specify exactly which users or groups have permission to set specific approval tags. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## How It Works

Governed tags for advanced approvals build on the standard approval mechanism for deployment jobs. Approval tasks are identified by job task names that start with "approval" (case-insensitive). When an approver clicks the **Approve** button on the model version page, a Unity Catalog tag is set on the model version with the tag key matching the name of the approval task and the tag value set to `Approved`. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

With a governed tag policy applied to a specific tag name, only users or groups with `APPLY_TAG` permissions as specified in the policy can set that tag. This ensures that only authorized approvers can mark a model version as approved. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Use Cases

### Multiple Independent Approval Groups

Governed tags enable deployment jobs with multiple independent approval gates. For example, you can create two separate approval tags — `Approval_Legal` and `Approval_Security` — each with its own governed tag policy. This allows: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- The Legal team to set only the `Approval_Legal` tag.
- The Security team to set only the `Approval_Security` tag.
- A deployment job to have two separate approval tasks, one for Legal and one for Security.
- Both teams to have `APPLY_TAG` on the model, but each can only approve their respective checks. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Separation of Duties

You can set a tag policy to prevent the model owner from approving their own job. This enforces a two-person approval process, where a different person must review and approve the model version before deployment. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Standardization Across the Organization

Governed tag policies allow you to standardize approval checks across the [Metastore](/concepts/metastore.md), catalog, and schema levels. By using consistent tag names and policies, you can enforce uniform approval workflows throughout your organization. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Requirements

To use governed tags for advanced approvals, the following permissions are required: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- `APPLY TAG` permission on the Unity Catalog model (granted to the users or groups that need to approve).
- `CAN MANAGE RUN` permission on the deployment job (to trigger the repair of the job run after approval).

Additionally, a governed tag policy must be configured for the specific tag name(s) used in the approval process. See the governed tag policy documentation for instructions on setting up these policies. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) — The automated pipeline for model evaluation, approval, and deployment.
- [Approval mechanism for deployment jobs](/concepts/mlflow-deployment-jobs.md) — The standard approval process using Unity Catalog tags.
- Governed tag policy — The administrative policy controlling who can set specific tags.
- [Unity Catalog model permissions](/concepts/unity-catalog-permissions-model.md) — Access control for models and model versions.
- [MLflow 3](/concepts/mlflow-3.md) — The recommended MLflow client for use with deployment jobs.

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
