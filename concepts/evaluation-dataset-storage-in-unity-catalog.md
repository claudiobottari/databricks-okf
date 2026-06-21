---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8dce7eb8d122c2206189aa4af00fd40116b41e1dfa0ad35bc4a06c863ffb24f
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-storage-in-unity-catalog
    - EDSIUC
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Evaluation Dataset Storage in Unity Catalog
description: MLflow evaluation datasets are stored as tables in Unity Catalog, which provides versioning, lineage tracking, sharing across workspaces, and governance controls.
tags:
  - unity-catalog
  - storage
  - governance
  - databricks
timestamp: "2026-06-19T14:10:31.896Z"
---

# Evaluation Dataset Storage in Unity Catalog

**Evaluation Dataset Storage in Unity Catalog** refers to the system by which [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) are persisted, versioned, and governed within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. These datasets are the primary mechanism for systematically testing and improving [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications by providing a curated set of example inputs — either labeled (with known expected outputs) or unlabeled.

## Overview

An evaluation dataset helps improve a GenAI application’s quality by:
- Testing fixes against known problematic examples from production.
- Preventing regressions by maintaining a “golden set” of examples.
- Comparing app versions by testing different prompts, models, or app logic against the same data.
- Targeting specific features (safety, domain knowledge, edge cases).
- Validating the app across different environments as part of LLMOps.

MLflow evaluation datasets are stored in Unity Catalog, which provides built-in **versioning**, **lineage**, **sharing**, and **governance**. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create an evaluation dataset, you must have `CREATE TABLE` permissions on a Unity Catalog schema. The dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md). If you do not already have an experiment, see [Create an MLflow Experiment](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment#create-expt) to create one. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources

You can create an evaluation dataset from any of the following sources:
- **Existing traces**: Captured from a GenAI application to reflect real-world scenarios.
- **An existing dataset or directly entered examples**: Useful for quick prototyping or targeted testing.
- **Synthetic data**: Databricks can automatically generate a representative evaluation set from your documents. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating a Dataset

### Using the UI
1. Open an MLflow experiment, click **Traces** in the sidebar, and select traces using checkboxes.
2. Click **Actions** → **Add to evaluation dataset**.
3. If no evaluation datasets exist, click **Create new dataset**, specify the Unity Catalog schema and name, then **Export** the traces.
4. If datasets already exist, click **Export** next to the target dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK
Use the `mlflow.genai.datasets.create_dataset()` function, specifying the Unity Catalog table name in three‑part notation (catalog.schema.table). Then add records via `merge_records()`, for example from traces returned by `mlflow.search_traces()`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

You can update an evaluation dataset by adding records through the UI (click **Add record**, edit the row, **Save changes**) or programmatically with the SDK. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets **cannot** be stored in catalogs encrypted with [customer-managed keys (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md). Workspaces with CMK are supported only if the dataset is stored in a non‑CMK catalog.
- **Maximum of 2000 rows** per evaluation dataset.
- **Maximum of 20 expectations** per dataset record.

If you need any of these limitations relaxed, contact your Databricks representative. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [GenAI evaluation](/concepts/mlflow-genai-evaluation.md)
- [Synthetic data generation](/concepts/synthetic-data-generation-for-evaluation.md)
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md)

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
