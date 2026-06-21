---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f02b80716530a4324c8d9cbcd040b73f98c4113acff86d7befb88e688cc53194
  pageDirectory: concepts
  sources:
    - delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-error-message-reference
    - DEMR
    - Databricks Error Reference
    - Databricks Error Messages
    - Databricks error messages
    - MLflow Error Reference
  citations:
    - file: delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
    - file: serverless_customer_action_required-error-condition-databricks-on-aws.md
    - file: org_mismatch-error-condition-databricks-on-aws.md
    - file: schema_evolution_not_supported-error-condition-databricks-on-aws.md
    - file: stream_failed-error-condition-databricks-on-aws.md
    - file: workbench_capability_restricted-error-condition-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Databricks Error Message Reference
description: The curated collection of documented error conditions in Databricks, each with a unique error class, description, cause, and remediation
tags:
  - databricks
  - error-messages
  - reference
timestamp: "2026-06-18T15:24:24.274Z"
---

# Databricks Error Message Reference

Databricks returns structured error messages for many service and query failures. Each error class includes a machine‑readable name, a human‑readable message, a root cause, and recommended troubleshooting steps. The sections below document error classes that appear in common Databricks workflows, drawn from the official error‑condition references. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md, serverless_customer_action_required-error-condition-databricks-on-aws.md, org_mismatch-error-condition-databricks-on-aws.md, schema_evolution_not_supported-error-condition-databricks-on-aws.md, stream_failed-error-condition-databricks-on-aws.md, workbench_capability_restricted-error-condition-databricks-on-aws.md, configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

---

## DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT

**Error class**: `DELTA_UNIFORM_REFRESH_INVALID_ARGUMENT`

**Error message**: *Delta Uniform Refresh cannot run with invalid arguments.* ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

This error occurs when the `delta uniform refresh` operation is invoked with arguments that are not valid for the target table’s underlying format. For example, a table backed by Parquet files may require additional arguments that were omitted. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Cause

The command `delta uniform refresh` expects a set of arguments specific to the data source format (e.g., Parquet, Iceberg). If the provided arguments do not match, or if required arguments are missing, the operation fails with this error class. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Solution

Review the table’s source format and provide the correct arguments for that format. Consult the [Uniform refresh documentation](https://docs.databricks.com/aws/en/delta-uniform/refresh) for the required parameters. ^[delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md]

### Related Concepts

- [Delta Uniform](/concepts/delta-uniform.md)
- [Delta Lake](/concepts/delta-lake.md)

---

## SERVERLESS_CUSTOMER_ACTION_REQUIRED

**Error class**: `SERVERLESS_CUSTOMER_ACTION_REQUIRED`

**Error message**: *Serverless SQL warehouse request failed due to an Azure Storage limitation. Please see troubleshooting steps.* ^[serverless_customer_action_required-error-condition-databricks-on-aws.md]

This error is raised when a serverless SQL warehouse cannot execute a query because an Azure Storage request was throttled or failed due to account limitations. The error is specific to Azure deployments of Databricks. ^[serverless_customer_action_required-error-condition-databricks-on-aws.md]

### Cause

The serverless SQL warehouse makes requests to the customer’s Azure Storage account. If the account exceeds its request limits or is configured with restrictive network rules (e.g., a firewall that blocks the Databricks control plane), the warehouse returns this error. ^[serverless_customer_action_required-error-condition-databricks-on-aws.md]

### Solution

1. Check the Azure Storage account’s request limits and increase them if necessary.
2. Ensure the storage account’s firewall allows requests from the Databricks control plane IPs.
3. Verify that the Azure Storage account has the `Storage Blob Data Contributor` role assigned to the Databricks managed identity. ^[serverless_customer_action_required-error-condition-databricks-on-aws.md]

If the issue persists, contact Databricks support for further assistance. ^[serverless_customer_action_required-error-condition-databricks-on-aws.md]

### Related Concepts

- Serverless SQL Warehouses
- Azure Storage Integration

---

## ORG_MISMATCH

**Error class**: `ORG_MISMATCH`

**Error message**: *Cannot assign [Metastore](/concepts/metastore.md) because the metastore’s organization does not match the workspace’s organization.* ^[org_mismatch-error-condition-databricks-on-aws.md]

This error occurs when trying to assign a [Metastore](/concepts/metastore.md) to a workspace that belongs to a different organization (Databricks account). Metastores are scoped to a single account and cannot be shared across accounts. ^[org_mismatch-error-condition-databricks-on-aws.md]

### Cause

The [Metastore](/concepts/metastore.md) you are attempting to assign is already owned by another Databricks account. Workspaces in a different account cannot use that [Metastore](/concepts/metastore.md). ^[org_mismatch-error-condition-databricks-on-aws.md]

### Solution

Ensure the [Metastore](/concepts/metastore.md) is in the same account as the workspace. To use a [Metastore](/concepts/metastore.md) from a different account, you must first re‑create it in the target account or use a cross‑account sharing mechanism (if supported). ^[org_mismatch-error-condition-databricks-on-aws.md]

### Related Concepts

- [Unity Catalog Metastore](/concepts/unity-catalog-metastore.md)
- Workspace Assignment

---

## SCHEMA_EVOLUTION_NOT_SUPPORTED

**Error class**: `SCHEMA_EVOLUTION_NOT_SUPPORTED`

**Error message**: *Schema evolution is not supported for the specified format.* ^[schema_evolution_not_supported-error-condition-databricks-on-aws.md]

This error appears when using `COPY INTO` with a source format that does not support automatic schema evolution. For example, `COPY INTO` from a CSV source does not allow adding new columns automatically. ^[schema_evolution_not_supported-error-condition-databricks-on-aws.md]

### Cause

The `COPY INTO` command was configured with `COPY_OPTIONS ('mergeSchema' = 'true')` or similar options that require schema evolution, but the source file format (e.g., CSV, JSON) does not support it. ^[schema_evolution_not_supported-error-condition-databricks-on-aws.md]

### Solution

Remove or set to `false` the schema‑evolution option, or use a format such as Parquet that supports schema evolution. If you need to add columns, manually alter the target table schema. ^[schema_evolution_not_supported-error-condition-databricks-on-aws.md]

### Related Concepts

- [COPY INTO](/concepts/copy-into-command.md)
- Schema Evolution

---

## STREAM_FAILED

**Error class**: `STREAM_FAILED`

**Error message**: *The streaming update for table `<table-name>` failed.* ^[stream_failed-error-condition-databricks-on-aws.md]

This error is raised in Delta Live Tables when a streaming pipeline encounters a failure that prevents it from processing data. The pipeline stops and cannot automatically resume. ^[stream_failed-error-condition-databricks-on-aws.md]

### Cause

Common causes include corrupt input data, transient resource exhaustion, or misconfigured streaming sources. The underlying exception is logged in the pipeline’s event log. ^[stream_failed-error-condition-databricks-on-aws.md]

### Solution

1. Inspect the pipeline event log to identify the specific failure reason.
2. Fix the underlying issue (e.g., repair corrupt source files, increase cluster resources).
3. Restart the pipeline manually after resolving the cause. ^[stream_failed-error-condition-databricks-on-aws.md]

### Related Concepts

- Delta Live Tables
- Pipeline Monitoring

---

## WORKBENCH_CAPABILITY_RESTRICTED

**Error class**: `WORKBENCH_CAPABILITY_RESTRICTED`

**Error message**: *Workbench capability is restricted for this environment.* ^[workbench_capability_restricted-error-condition-databricks-on-aws.md]

This error occurs when a user tries to use a Databricks Workbench feature that has been disabled by the workspace administrator. Workbench capabilities can be toggled on a per‑workspace basis. ^[workbench_capability_restricted-error-condition-databricks-on-aws.md]

### Cause

The workspace administrator has disabled the specific capability (e.g., notebook execution, scheduling) for the current environment. Users cannot override this restriction. ^[workbench_capability_restricted-error-condition-databricks-on-aws.md]

### Solution

Contact the workspace administrator to request that the required capability be enabled. Administrators can adjust settings under the Workspace settings page. ^[workbench_capability_restricted-error-condition-databricks-on-aws.md]

### Related Concepts

- Databricks Workbench
- [Workspace Administration](/concepts/workspace-admin-unity-catalog.md)

---

## 403 PERMISSION_DENIED: Serverless Budget Policy

**Scenario**: When [MLflow](/concepts/mlflow.md) tries to run a serverless workload (e.g., scheduled scorer, synthetic evaluation generation) against an experiment, it may return:

```
403 Client Error: Forbidden
PERMISSION_DENIED: Unable to use fallback policies, please manually select a policy.
```

This occurs if the workspace’s default serverless budget policy has been disabled and no alternative policy is assigned to the experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Cause

By default, MLflow uses the workspace’s default serverless budget policy. When that policy is turned off (e.g., because each user must select a dedicated policy), MLflow has no fallback and the serverless workload is denied. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Solution

Set a serverless budget policy on the MLflow experiment by using the UI or the API:

- In the experiment’s **Details** panel, select a budget policy.
- Or use `mlflow.set_experiment_tag(experiment_id, key="mlflow.workload_creation_policy_id", value="<policy-id>")`. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

After setting the policy, MLflow will use it for all serverless workloads created for that experiment. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Related Concepts

- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)

---

## Sources

- delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md
- serverless_customer_action_required-error-condition-databricks-on-aws.md
- org_mismatch-error-condition-databricks-on-aws.md
- schema_evolution_not_supported-error-condition-databricks-on-aws.md
- stream_failed-error-condition-databricks-on-aws.md
- workbench_capability_restricted-error-condition-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws.md](/references/delta_uniform_refresh_invalid_argument-error-condition-databricks-on-aws-592e817e.md)
2. serverless_customer_action_required-error-condition-databricks-on-aws.md
3. org_mismatch-error-condition-databricks-on-aws.md
4. schema_evolution_not_supported-error-condition-databricks-on-aws.md
5. stream_failed-error-condition-databricks-on-aws.md
6. workbench_capability_restricted-error-condition-databricks-on-aws.md
7. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
