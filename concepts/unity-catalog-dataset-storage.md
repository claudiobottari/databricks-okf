---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d4c81e1680a6bd00a0bee64e5403f17277ced6e267dae89c3fee075717a10ea
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-dataset-storage
    - UCDS
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Unity Catalog Dataset Storage
description: MLflow evaluation datasets are stored in Unity Catalog, which provides built-in versioning, lineage, sharing, and governance for the datasets.
tags:
  - unity-catalog
  - mlflow
  - storage
  - governance
timestamp: "2026-06-18T10:54:25.500Z"
---

# Unity Catalog Dataset Storage

**Unity Catalog Dataset Storage** refers to the storage of [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) as managed tables in [Unity Catalog](/concepts/unity-catalog.md). Evaluation datasets are selected sets of example inputs used to test and improve GenAI applications. Storing them in Unity Catalog provides built-in versioning, lineage, sharing, and governance capabilities. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Key Features

| Feature | Description |
|---------|-------------|
| **Versioning** | Unity Catalog automatically tracks dataset versions, enabling rollback and history review. |
| **Lineage** | The origin of each dataset (e.g., from traces, synthetic generation) is recorded for auditability. |
| **Sharing** | Datasets can be shared across workspaces and teams via Unity Catalog’s access controls. |
| **Governance** | Permissions and tagging policies apply to dataset tables just like any other Unity Catalog object. |

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

An evaluation dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md) and stored as a Unity Catalog table in a schema where the creator has `CREATE TABLE` permission. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

- The user must have `CREATE TABLE` permission on a Unity Catalog schema.
- An MLflow experiment must already exist (see [Create an MLflow Experiment](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment#create-expt)).
- The dataset cannot be stored in a catalog encrypted with [customer-managed keys (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md). Workspaces using CMK are supported as long as the dataset resides in a non-CMK catalog. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating a Dataset

Evaluation datasets can be created from three types of sources: ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **Existing traces**—real-world interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md).
- **Existing datasets or manually entered examples**—useful for quick prototyping or targeted testing.
- **Synthetic data**—automatically generated from documents for broad test coverage.

Both a UI workflow and an SDK workflow are supported. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the UI

1. Open your experiment in the Databricks workspace (click **Experiments** in the sidebar, then select the experiment).
2. In the left sidebar, click **Traces**.
3. Select traces using checkboxes, then click **Actions > Add to evaluation dataset**.
4. If no evaluation dataset exists, click **Create new dataset**, choose the Unity Catalog schema, enter a name, and click **Create Dataset**.
5. Click **Export** and then **Done**.

Alternatively, you can export selected traces to an existing dataset by clicking **Export** next to its name. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK

The SDK workflow uses `mlflow.genai.datasets.create_dataset()` to create an empty table in Unity Catalog, then adds records using `merge_records()`—for example, from traces returned by `mlflow.search_traces()`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

Python example:

```python
import mlflow

# Create an empty evaluation dataset in Unity Catalog
eval_dataset = mlflow.genai.datasets.create_dataset(
    name="workspace.default.email_generation_eval",
)

# Search for traces (e.g., successful production traces)
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    tags.environment = 'production',
    max_results=10
)

# Merge traces into the dataset
eval_dataset = eval_dataset.merge_records(traces)
```

The resulting table can be previewed with `eval_dataset.to_df()`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

- **Via UI**: Open the dataset page (from the experiment’s **Datasets** tab), click **Add record**, edit the new row, and save changes.
- **Via SDK**: Use `merge_records()` to append new records to an existing dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in customer-managed key (CMK) catalogs.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record.

If these limits are a concern, contact your Databricks representative. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that stores evaluation dataset tables.
- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) — The broader concept of evaluation datasets in MLflow.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Source of trace data used to build datasets.
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The experiment to which datasets are attached.
- [Customer-Managed Keys (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md) — Encryption key management that restricts dataset storage.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
