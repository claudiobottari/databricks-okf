---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0320d58b0b412cb7e53d3bddbbdaadb2d07a1c1d4655c424def12b83c77fe76d
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sdk-based-dataset-management-in-mlflow
    - SDMIM
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: SDK-Based Dataset Management in MLflow
description: Programmatic creation, updating, and management of evaluation datasets using the MLflow Python SDK, including methods like create_dataset(), merge_records(), search_traces(), and to_df().
tags:
  - mlflow
  - sdk
  - python
  - dataset-management
timestamp: "2026-06-19T17:42:07.604Z"
---

# SDK-Based Dataset Management in MLflow

**SDK-Based Dataset Management in MLflow** refers to the programmatic creation, population, and maintenance of evaluation datasets using the MLflow Python SDK. These datasets are stored in Unity Catalog and are used to systematically test and improve GenAI applications. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

An evaluation dataset is a curated set of example inputs—either labeled (with known expected outputs) or unlabeled—that helps improve application quality by testing fixes against known problems, preventing regressions via a “golden set,” comparing app versions, targeting specific features, and validating across environments. MLflow evaluation datasets are stored in Unity Catalog, which provides built-in versioning, lineage, sharing, and governance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create an evaluation dataset using the SDK, you must have `CREATE TABLE` permissions on a Unity Catalog schema. The dataset is attached to an MLflow experiment; if you do not already have an experiment, create one first. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating a Dataset Using the SDK

The SDK allows you to create an evaluation dataset programmatically. After connecting to a Spark session (for local development, use `DatabricksSession.builder.remote(serverless=True).getOrCreate()`), call `mlflow.genai.datasets.create_dataset()` with a fully qualified table name in the form `<schema>.<table_name>`. The dataset is stored in Unity Catalog. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

```python
import mlflow.genai.datasets
from databricks.connect import [[databrickssession|DatabricksSession]]

spark = [[databrickssession|DatabricksSession]].builder.remote(serverless=True).getOrCreate()
uc_schema = "workspace.default"
dataset_name = "my_eval_dataset"
eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.{dataset_name}"
)
```

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Adding Records to a Dataset

After creating the dataset, you can populate it with records from several sources, including existing traces, domain expert labels, direct entries, synthetic data, or conversation simulation. The most effective approach is to curate examples from historical application interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Adding Records from Traces

You can programmatically search for traces using `mlflow.search_traces()` with filters such as status, tags, or environment. The returned traces can then be merged into the dataset using `eval_dataset.merge_records(traces)`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

```python
import mlflow

traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    order_by=["attributes.timestamp_ms DESC"],
    tags.environment = 'production',
    max_results=10
)
eval_dataset = eval_dataset.merge_records(traces)
```

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Selecting Traces for Datasets

Both quantitative and qualitative analysis can guide trace selection:

- **Quantitative**: Use the MLflow UI or SDK to filter by tags (e.g., `tag.quality_score < 0.7`), sort by latency or token usage, and analyze patterns. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Qualitative**: Review individual traces to identify patterns requiring human judgment—such as inputs that led to low-quality outputs, edge cases, or missing context. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

You can enrich traces with expected outputs or quality indicators before adding them, enabling ground truth comparison. See [collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) for adding human labels. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

Existing evaluation datasets can be updated using the SDK. For example, you can add new records via `merge_records()` as shown above, or modify records programmatically. The UI also supports adding records via the **Add record** button. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

The following limitations apply to MLflow evaluation datasets:

- Datasets cannot be stored in catalogs encrypted with [customer‑managed keys (CMK)](/concepts/customer-managed-keys-for-online-feature-stores.md). Workspaces with CMK are supported only if the dataset resides in a non-CMK catalog. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- Maximum of 2000 rows per evaluation dataset. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- Maximum of 20 expectations per dataset record. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

If these limits are too restrictive, contact your Databricks representative for assistance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – Capturing application interactions for evaluation.
- [Unity Catalog](/concepts/unity-catalog.md) – Governance and storage layer for evaluation datasets.
- [Evaluation Dataset UI](/concepts/evaluation-dataset-ui.md) – Graphical interface for dataset management.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Using datasets to run evaluations.
- [Custom LLM Judges](/concepts/custom-llm-judges.md) – Evaluating outputs with custom judges.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
