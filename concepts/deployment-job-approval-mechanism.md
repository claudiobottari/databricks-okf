---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 438e02bf1e52c72146b8d35ec162f85e825ba0c561bc1e0b3ca7f1b7faa7275b
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-job-approval-mechanism
    - DJAM
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Deployment Job Approval Mechanism
description: An experimental human-in-the-loop approval process for deployment jobs that uses Unity Catalog tags to gate progression from evaluation to deployment, with automatic job repair on approval.
tags:
  - mlflow
  - approval
  - governance
timestamp: "2026-06-19T19:36:55.373Z"
---

# Deployment Job Approval Mechanism

The **Deployment Job Approval Mechanism** is a human-in-the-loop feature in Databricks that enables controlled approval of model versions within an ML deployment pipeline. It integrates with [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md) and [Unity Catalog](/concepts/unity-catalog.md) to provide governed workflows with clear visibility into progress and historical context for each model version. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Overview

The approval mechanism allows privileged users to review evaluation metrics for a model version and then approve or reject it, enabling automated deployment pipelines with human oversight. When a deployment job has been triggered, metrics from the evaluation run appear on the model version page, allowing approvers to assess quality and readiness before making a decision. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## How Approval Works

The approval process uses Unity Catalog tags to determine whether the approval task should pass or fail. Approval tasks are identified by job task names that start with "approval" (case-insensitive). A task passes when the corresponding Unity Catalog tag is set to `Approved`. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Approval Workflow

The approval process follows these steps: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

1. **Initial run**: The first run of the deployment job always fails on an approval task because the model version has not been approved yet and thus does not have the required Unity Catalog tag.

2. **Approval evaluation**: The approver reviews the model version and its evaluation metrics, which are displayed on the model version page.

3. **Approval action**: If the approver deems the model version satisfactory, they click the **Approve** button in the deployment job sidebar on the model version page.

4. **Automatic repair**: The approval action automatically repairs the job run and adds a Unity Catalog tag to the model version, where:
   - The tag key matches the name of the approval task.
   - The tag value is set to `Approved`.

5. **Job continuation**: The repaired deployment job run automatically resumes from the approval task. This time, it passes because the required Unity Catalog tag is now present, and then proceeds to subsequent tasks such as deployment.

## Required Permissions

To use the approval mechanism, the following permissions are required: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- **APPLY TAG** on the Unity Catalog model
- **CAN MANAGE RUN** on the deployment job

## Governed Tags for Advanced Approvals

The approval mechanism supports advanced configurations using [governed tag policies](/concepts/governed-tags-for-abac-policies.md). With governed tags, you can: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- **Multiple independent approval groups**: Create separate tags for different approval groups. For example, you can have `Approval_Legal` and `Approval_Security` tags with separate governed tag policies so that only the Legal team can set the `Approval_Legal` tag and only the Security team can set the `Approval_Security` tag. You can then have two approval tasks in your deployment job corresponding to each approval.

- **Prevent self-approval**: Set a tag policy to prevent the model owner from approving the job, ensuring a second-person approval requirement.

- **Standardize approval checks**: Use consistent tag names with tag policies to standardize approval checks across the [Metastore](/concepts/metastore.md), catalog, and schema.

## Best Practices

Databricks recommends the following best practices for deployment job approvals: ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

- If using a deployment job notebook, set the **Run As** field to a service principal with minimal permissions.
- For the approval task, [disable retries](https://docs.databricks.com/aws/en/jobs/run-serverless-jobs#retry) as the task is expected to fail at first on the initial run. This prevents a longer wait and multiple error logs being reported.

## Related Concepts

- [MLflow 3 Deployment Jobs](/concepts/mlflow-3-deployment-jobs.md)
- Unity Catalog tags
- [Governed tag policies](/concepts/governed-tags.md)
- MLflow 3 Model Tracking
- Unity Catalog Model Version ACL
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md)
- [Model Serving](/concepts/model-serving.md)

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
