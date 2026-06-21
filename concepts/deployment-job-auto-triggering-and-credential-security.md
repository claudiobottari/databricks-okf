---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7a5668b2957d64464d6fb0c8980ffe95e2e3f9be8ae96bf86facddba7215e289
  pageDirectory: concepts
  sources:
    - mlflow-3-deployment-jobs-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deployment-job-auto-triggering-and-credential-security
    - Credential Security and Deployment Job Auto-Triggering
    - DJAACS
  citations:
    - file: mlflow-3-deployment-jobs-databricks-on-aws.md
title: Deployment Job Auto-Triggering and Credential Security
description: Deployment jobs auto-trigger using the model owner's credentials when a new model version is created, with recommendations to use service principals to prevent privilege escalation.
tags:
  - security
  - mlops
  - service-principals
timestamp: "2026-06-19T19:37:04.104Z"
---

# Deployment Job Auto-Triggering and Credential Security

**Deployment Job Auto-Triggering and Credential Security** refers to the automatic execution behavior of [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) and the associated security implications when a new model version is created in [Unity Catalog](/concepts/unity-catalog.md). Understanding this mechanism is critical for preventing privilege escalation and ensuring governed MLOps workflows.

## Auto-Triggering Behavior

Deployment jobs are designed to trigger automatically whenever a new model version is created in a Unity Catalog registered model. This automation eliminates the need for manual intervention to start the deployment pipeline. The job can also be triggered manually on both existing and previously deployed versions from the model version page by clicking **Start deployment job**, or directly from the Jobs UI or API by specifying the appropriate `model_name` and `model_version` job parameters. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Credential Security and Privilege Escalation Risk

The deployment job auto-triggers using the **model owner's credentials**. This design has a significant security implication: giving a user `CREATE MODEL VERSION` permission on a Unity Catalog model allows that user to execute arbitrary code as part of the job, because the job runs with the model owner's permissions. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

### Recommended Mitigation

To prevent privilege escalation, Databricks recommends that you set up the deployment job using a **service principal with minimal permissions**. The **Run As** field on the deployment job should be configured to this service principal. This ensures that even if a user with `CREATE MODEL VERSION` permission registers a new model version, the resulting job execution is limited to the service principal's scope rather than the model owner's full permissions. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Required Permissions for Auto-Triggering

Because the job automatically triggers when a new version is created and uses the model owner's credentials, the model owner must have **CAN MANAGE RUN or higher** ACLs on the deployment job. This is the same permission level necessary to trigger a job using the Jobs UI. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Manual Trigger Permissions

To manually trigger or repair the deployment job using the model version UI, the user must have **CAN MANAGE RUN or higher** ACLs on the deployment job (the same ACLs necessary to trigger a job using the Jobs UI). ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Best Practices Summary

- **Use a service principal** as the job owner with minimal permissions to prevent privilege escalation. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
- **Grant `CREATE MODEL VERSION` permission cautiously**, as it effectively allows code execution under the model owner's credentials. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
- **Ensure the model owner has CAN MANAGE RUN** on the deployment job for auto-triggering to function. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]
- **Set max concurrent run limit to 1** (the default) to prevent deployment race conditions. ^[mlflow-3-deployment-jobs-databricks-on-aws.md]

## Related Concepts

- [MLflow Deployment Jobs](/concepts/mlflow-deployment-jobs.md) — The job type that manages model version lifecycle
- Unity Catalog CREATE MODEL VERSION ACL — The permission that triggers auto-execution
- Service principals in Databricks — Recommended identity for job ownership
- Human-in-the-loop approvals — Approval mechanism that works alongside auto-triggering
- Model version lifecycle management — The broader MLOps workflow

## Sources

- mlflow-3-deployment-jobs-databricks-on-aws.md

# Citations

1. [mlflow-3-deployment-jobs-databricks-on-aws.md](/references/mlflow-3-deployment-jobs-databricks-on-aws-732ab147.md)
