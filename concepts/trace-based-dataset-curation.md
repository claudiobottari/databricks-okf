---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d06d3e8181d66d86da53a38127e6147e3038613849bf9542bcc5634de79b987c
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-based-dataset-curation
    - TDC
    - trace-based-dataset-creation
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Trace-Based Dataset Curation
description: The practice of building evaluation datasets by selecting and curating traces from an application's historical interactions captured by MLflow Tracing, using either the UI or SDK.
tags:
  - mlflow
  - tracing
  - evaluation
  - dataset-creation
timestamp: "2026-06-19T17:41:58.340Z"
---

# Trace-Based Dataset Curation

**Trace-based dataset curation** is the process of selecting and exporting existing MLflow traces — historical records of GenAI application interactions — to form representative evaluation datasets. This approach ensures that evaluation data reflects real-world usage patterns, including edge cases, failures, and high-value interactions, rather than relying solely on synthetic or manually crafted examples.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

An evaluation dataset is a selected set of example inputs — either labeled (with known expected outputs) or unlabeled (without ground-truth answers) — used to systematically test and improve a GenAI application. Evaluation datasets help improve application quality by testing fixes against known problematic examples, prevent regressions through a "golden set" of examples that must always work correctly, compare different application versions against the same data, target specific features with specialized datasets, and validate performance across different environments as part of [LLMOps](/concepts/large-language-models-llms-on-databricks.md).^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

MLflow evaluation datasets created through trace curation are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create an evaluation dataset from traces, you must have `CREATE TABLE` permissions on a Unity Catalog schema. Additionally, each evaluation dataset is attached to an [MLflow Experiment](/concepts/mlflow-experiment.md); if you do not already have an experiment, you must create one first.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources

While trace-based curation is a primary method, you can create evaluation datasets from three sources:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **Existing traces**: Historical GenAI application interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md), forming the basis of trace-based dataset curation.
- **Existing datasets or directly entered examples**: Useful for quick prototyping or targeted testing of specific features.
- **Synthetic data**: Databricks can automatically generate a representative evaluation set from your documents for quick evaluation with good coverage.

## Selecting Traces for Evaluation Datasets

Before adding traces to a dataset, identify which traces represent important test cases. Both quantitative and qualitative analysis help select representative traces.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Quantitative Trace Selection

Use the MLflow UI or SDK to filter and analyze traces based on measurable characteristics:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **In the MLflow UI**: Filter by tags (e.g., `tag.quality_score < 0.7`), search for specific inputs or outputs, or sort by latency or token usage.
- **Programmatically**: Query traces using `mlflow.search_traces()` to perform advanced analysis, such as checking correlations between quality issues and token usage.

### Qualitative Trace Selection

Review individual traces to identify patterns requiring human judgment:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- Examine inputs that led to low-quality outputs.
- Look for patterns in how the application handled edge cases.
- Identify missing context or faulty reasoning.
- Compare high-quality versus low-quality traces to understand differentiating factors.

## Creating Datasets from Traces Using the UI

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click on the name of your experiment to open it.
3. In the left sidebar, click **Traces**.
4. Use the checkboxes to select the traces you want to add. To select all traces on the current page, click the checkbox next to **Trace ID** in the column header.
5. Click **Actions**. The button label shows the number of selected traces.
6. Under **Use for evaluation**, select **Add to evaluation dataset**.
7. If no evaluation datasets exist for the experiment, click **Create new dataset**, select the Unity Catalog schema, enter a name, and click **Create Dataset**, then **Export** and **Done**. If evaluation datasets already exist, click **Export** to the right of the dataset you want to add traces to.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating Datasets from Traces Using the SDK

### Step 1: Create the Dataset

Use `mlflow.genai.datasets.create_dataset()` to create an evaluation dataset in a Unity Catalog schema where you have `CREATE TABLE` permissions.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

```python
import mlflow
import mlflow.genai.datasets

uc_schema = "workspace.default"
evaluation_dataset_table_name = "email_generation_eval"

eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.{evaluation_dataset_table_name}",
)
```

### Step 2: Search and Add Traces

Programmatically search for traces using `mlflow.search_traces()` with filters such as status, environment, or other properties. Then add the traces to the dataset using `eval_dataset.merge_records(traces)`.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

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

### Step 3: Enrich with Expected Outputs

Traces can be enriched with expected outputs or quality indicators to enable ground truth comparison. Use domain expert feedback to add human labels to existing traces, as described in [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md).^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Updating Existing Datasets

You can use the UI or SDK to update an evaluation dataset:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **Using the UI**: Navigate to your experiment, click **Datasets** in the sidebar, click on the dataset name, click **Add record**, edit the new row with input and expectations, and click **Save changes**.
- **Using the SDK**: Continue adding traces or records programmatically to an existing dataset reference.

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with customer-managed keys (CMK). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Best Practices

- **Balance coverage and quality**: Include both common cases and edge cases from production traces to ensure comprehensive testing.
- **Maintain a golden set**: Curate a stable set of high-quality traces that must always pass, used for regression testing.
- **Enrich with human feedback**: Add expert annotations to traces to enable ground-truth comparison and judge alignment.
- **Version your datasets**: Unity Catalog's built-in versioning allows you to track changes and roll back if needed.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The mechanism for capturing GenAI application traces
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that uses curated datasets
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — The general concept of curated test data for LLM evaluation
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) — Operational practices that include trace-based testing
- [Unity Catalog](/concepts/unity-catalog.md) — Governance layer for storing and managing evaluation datasets
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Containers for organizing evaluation dataset metadata
- [Synthetic Evaluation Generation](/concepts/synthetic-evaluation-data-generation.md) — Alternative approach when traces are unavailable
- [Custom Judges](/concepts/custom-judges.md) — LLM-based scorers used with evaluation datasets

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
