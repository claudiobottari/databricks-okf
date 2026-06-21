---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e3b15756ef534426165673b9e914a55e9b0aae1f5bde2deddf79fd059167ff73
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-integration-for-evaluation-datasets
    - UCIFED
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Unity Catalog Integration for Evaluation Datasets
description: Infrastructure layer where MLflow evaluation datasets are stored in Unity Catalog tables, providing built-in versioning, lineage tracking, sharing across workspaces, and governance controls via Unity Catalog permissions.
tags:
  - unity-catalog
  - governance
  - infrastructure
timestamp: "2026-06-19T09:11:19.190Z"
---

# Unity Catalog Integration for Evaluation Datasets

**Unity Catalog Integration for Evaluation Datasets** refers to the storage, governance, and management of [MLflow Evaluation Datasets](/concepts/evaluation-datasets.md) within [Unity Catalog](/concepts/unity-catalog.md). By default, MLflow evaluation datasets are stored as Delta tables in Unity Catalog, which provides built-in versioning, lineage, sharing, and governance capabilities. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Benefits

Storing evaluation datasets in Unity Catalog enables:

- **Versioning**: Datasets can be versioned, allowing teams to track changes over time and reproduce past evaluations.
- **Lineage**: Automatic tracking of how datasets were created (e.g., from traces, synthetic generation, or manual entry) and how they are used.
- **Sharing**: Datasets can be easily shared across workspaces and teams using Unity Catalog’s fine-grained access controls.
- **Governance**: Compliance with data governance policies through Unity Catalog’s tagging, masking, and auditing features.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create an evaluation dataset in Unity Catalog, the user must have `CREATE TABLE` permission on a Unity Catalog schema. The dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md); if no experiment exists, one must be created first. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources for Evaluation Datasets

Evaluation datasets can be built from several sources:

- **Existing traces**: Historical interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md) can be curated into a dataset.
- **Domain expert labels**: Human-annotated records with expected outputs.
- **Direct examples**: Manually entered records for targeted testing or quick prototyping.
- **Synthetic data**: Automatically generated representative examples from documents to ensure broad coverage.
- **Conversation simulation**: Programmatically generated dialogue-based test cases.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating a Dataset

### Using the UI

1. Navigate to the experiment in the Databricks workspace.
2. Click **Traces** in the left sidebar.
3. Select the traces you want to add using checkboxes.
4. Click **Actions** and choose **Add to evaluation dataset**.
5. Either create a new dataset (specifying a Unity Catalog schema, name, and table) or add traces to an existing dataset.
6. Export the traces and confirm.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK

1. Connect to Serverless Spark (if using a local environment) via `DatabricksSession.builder.remote(serverless=True).getOrCreate()`.
2. Call `mlflow.genai.datasets.create_dataset(name="<catalog.schema.table>")`.
3. Add records from traces using `eval_dataset.merge_records(traces)`, or add manually via other methods.
4. Preview the dataset with `eval_dataset.to_df()`.

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

Datasets can be updated through the UI or SDK. In the UI, open the dataset page, click **Add record**, edit the new row, and save. The SDK provides methods to merge new records or modify existing ones. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with Customer-managed keys (CMK). Workspaces with CMK are supported as long as the dataset resides in a non-CMK catalog.
- Maximum 2000 rows per evaluation dataset.
- Maximum 20 expectations per dataset record.

If these limits are restrictive, contact a Databricks representative. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The broader evaluation framework for GenAI applications.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs and evaluations.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Captures runtime traces that can serve as dataset sources.
- [GenAI Agents](/concepts/genai-agent-observability.md) – The applications evaluated with these datasets.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance, storage, and sharing layer.
- [Delta Tables](/concepts/delta-lake-table.md) – The underlying storage format for evaluation datasets.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
