---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 04cd1c97bae62a323bfd6742ed4df81b5c6a9369b3d381adf7df6110b9ddd6e5
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-based-dataset-creation
    - TDC
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Trace-Based Dataset Creation
description: The practice of building evaluation datasets by selecting and merging existing MLflow traces (real historical application interactions) using the UI or SDK, enabling datasets grounded in production scenarios.
tags:
  - mlflow
  - tracing
  - evaluation
  - databricks
timestamp: "2026-06-19T14:10:31.403Z"
---

# Trace-Based Dataset Creation

**Trace-Based Dataset Creation** is the process of constructing [Evaluation Datasets](/concepts/evaluation-datasets.md) for GenAI applications by curating examples from historical [MLflow trace](/concepts/mlflow-tracing.md) data. This method allows developers to build realistic, production-relevant test sets without manually authoring each input, and is one of the primary data sources supported by MLflow evaluation datasets. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

An evaluation dataset is a selected set of example inputs — either labeled (with known expected outputs) or unlabeled — used to systematically test and improve a GenAI app. Building datasets from traces helps improve quality by testing fixes against known problematic examples from production, prevents regressions by creating a "golden set" of examples that must always work correctly, and enables comparison of different prompts, models, or app logic against the same data. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

MLflow evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating a Dataset from Traces

Both the MLflow UI and the SDK support creating a dataset from existing traces.

### Using the UI

1. Open the experiment, then click **Traces** in the left sidebar.
2. Select the traces you want to add using the checkboxes.
3. Click **Actions** and choose **Add to evaluation dataset**.
4. If no evaluation datasets exist, click **Create new dataset**, select a Unity Catalog schema, enter a name, and click **Create Dataset**. Then click **Export** and **Done**.
5. If datasets already exist, click **Export** next to the target dataset and then **Done**. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK

Programmatically, you can search for traces using `mlflow.search_traces()` and then add them to an evaluation dataset with `merge_records()`. For example:

```python
import mlflow

eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.{evaluation_dataset_table_name}"
)

traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    order_by=["attributes.timestamp_ms DESC"],
    tags.environment = 'production',
    max_results=10
)

eval_dataset = eval_dataset.merge_records(traces)
```

Filters can be applied to identify traces by success, failure, production environment, or other properties. See mlflow.search_traces() API|Search traces programmatically for complete syntax. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Selecting Traces for a Dataset

Before adding traces, identify which traces represent important test cases using both quantitative and qualitative analysis.

### Quantitative Selection

Use the MLflow UI or SDK to filter and analyze traces based on measurable characteristics:

- In the UI, filter by tags (e.g., `tag.quality_score < 0.7`), search for specific inputs/outputs, or sort by latency or token usage.
- Programmatically, query traces to perform advanced analysis, such as checking correlation between token usage and quality. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Qualitative Selection

Review individual traces to identify patterns requiring human judgment:

- Examine inputs that led to low-quality outputs.
- Look for patterns in how the application handled edge cases.
- Identify missing context or faulty reasoning.
- Compare high-quality vs. low-quality traces to understand differentiating factors. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

Once representative traces are identified, add them using search and merge methods.

---

**Tip:** Enrich traces with expected outputs or quality indicators by collecting [domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) to enable ground truth comparison. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

Datasets can be updated via the UI or SDK.

- **UI:** Open the dataset page, click **Add record**, edit the new row with input and expectations, optionally set tags, then click **Save changes**.
- **SDK:** Use `merge_records()` (as shown above) to add new traces to an existing dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with [customer-managed keys (CMK)](/concepts/customer-managed-keys-cmk-for-online-feature-stores.md). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md)
- mlflow.search_traces() API|Search traces programmatically
- [Domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md)
- [Unity Catalog](/concepts/unity-catalog.md)

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
