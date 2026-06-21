---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 46a5306569e4344ed8f451369f5eba6e63076849732131695de7086da30dd723
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-for-evaluation-data
    - UCFED
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Unity Catalog for Evaluation Data
description: Storage of MLflow evaluation datasets in Unity Catalog, providing built-in versioning, lineage, sharing, and governance capabilities for GenAI evaluation artifacts.
tags:
  - unity-catalog
  - governance
  - storage
timestamp: "2026-06-18T14:34:30.257Z"
---

# Unity Catalog for Evaluation Data

**Unity Catalog for Evaluation Data** refers to the use of [Unity Catalog](/concepts/unity-catalog.md) as the central storage and governance layer for [MLflow](/concepts/mlflow.md) evaluation datasets used in [GenAI](/concepts/mlflow-genai-evaluate-api.md) application testing and improvement. Evaluation datasets stored in Unity Catalog benefit from built-in versioning, lineage tracking, sharing capabilities, and governance controls. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

An evaluation dataset is a selected set of example inputs — either labeled (with known expected outputs) or unlabeled (without ground-truth answers) — used to systematically test and improve a GenAI application. These datasets help improve quality by testing fixes against known problematic examples from production, prevent regressions by creating a "golden set" of examples that must always work correctly, compare app versions across different prompts or models, target specific features for safety or domain knowledge, and validate the app across different environments as part of LLMOps. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

MLflow evaluation datasets are stored in Unity Catalog tables, which provides built-in versioning, lineage, sharing, and governance for the data. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create an evaluation dataset, you must have `CREATE TABLE` permissions on a Unity Catalog schema. An evaluation dataset is also attached to an [MLflow Experiment](/concepts/mlflow-experiment.md). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating Evaluation Datasets

You can create evaluation datasets using any of the following data sources:

- **Existing traces** – Captured traces from a GenAI application can be used to create an evaluation dataset based on real-world scenarios. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **An existing dataset or directly entered examples** – Useful for quick prototyping or targeted testing of specific features. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Synthetic data** – Databricks can automatically generate a representative evaluation set from your documents to quickly evaluate your agent with good coverage of test cases. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Creating a Dataset Using the UI

To create a dataset from existing traces using the UI:

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click on the name of your experiment to open it.
3. In the left sidebar, click **Traces**.
4. Use the checkboxes to select the traces you want to add.
5. Click **Actions** and select **Add to evaluation dataset**. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

If no evaluation datasets exist for the experiment, you can create a new dataset by clicking **Create new dataset**, selecting a Unity Catalog schema, entering a name, and clicking **Create Dataset**. Then click **Export** to add the selected traces. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Creating a Dataset Using the SDK

To create a dataset using the SDK, first create the evaluation dataset:

```python
import mlflow
import mlflow.genai.datasets
from databricks.connect import [[databrickssession|DatabricksSession]]

# Connect to Serverless Spark
spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()

# Create an evaluation dataset
uc_schema = "workspace.default"
evaluation_dataset_table_name = "email_generation_eval"
eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.{evaluation_dataset_table_name}",
)
```

Then add records to the dataset from existing traces:

```python
import mlflow

traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    order_by=["attributes.timestamp_ms DESC"],
    max_results=10,
)

eval_dataset = eval_dataset.merge_records(traces)
```

You can also add records from domain expert labels, build from scratch or import existing data, seed using synthetic data, or use conversation simulation. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources

- **[Unity Catalog](/concepts/unity-catalog.md)** – The governance and storage layer for evaluation datasets, providing versioning, lineage, sharing, and governance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **[MLflow experiments](/concepts/mlflow-experiment.md)** – Evaluation datasets are attached to MLflow experiments for organization and tracking. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **[MLflow Tracing](/concepts/mlflow-tracing.md)** – Captures application traces that can be used to create evaluation datasets from real-world scenarios. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with customer-managed keys (CMK). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- Maximum of 2000 rows per evaluation dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- Maximum of 20 expectations per dataset record. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

You can use the UI or the SDK to update an evaluation dataset. In the UI, open the dataset page, click **Add record**, edit the new row, and click **Save changes**. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Best Practices for Dataset Curation

- **Select representative traces** – Identify traces that represent important test cases using both quantitative analysis (filtering by tags, quality scores, latency, or token usage) and qualitative analysis (examining inputs that led to low-quality outputs, identifying patterns in edge case handling, and comparing high-quality vs. low-quality traces). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Enrich with ground truth** – Add expected outputs or quality indicators to enable ground truth comparison by collecting domain expert feedback. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Curate from production** – The most effective evaluation datasets are curated from your application's historical interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The central governance and storage layer for evaluation datasets
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational units for MLflow runs and evaluations
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Using evaluation datasets to assess agent quality
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Capturing application traces for dataset curation
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) – Lifecycle management for LLM applications
- Synthetic Data Generation – Creating representative evaluation sets from documents

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
