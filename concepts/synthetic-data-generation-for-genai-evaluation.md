---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ccaac1c8cc3c9a21a1165c7905ce42bf4fbdca6c37d1a93636c63e21839c352e
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - synthetic-data-generation-for-genai-evaluation
    - SDGFGE
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Synthetic Data Generation for GenAI Evaluation
description: Databricks can automatically generate representative evaluation datasets from documents, enabling quick evaluation of GenAI agents with broad test case coverage without manual curation.
tags:
  - mlflow
  - synthetic-data
  - genai
  - evaluation
timestamp: "2026-06-19T17:42:10.115Z"
---

# Synthetic Data Generation for GenAI Evaluation

**Synthetic Data Generation for GenAI Evaluation** is the process of automatically creating representative evaluation datasets from source documents or other reference material. Databricks can automatically generate a synthetic evaluation set from your documents, allowing you to quickly evaluate a GenAI agent with good coverage of test cases without the need for manually curated examples. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

Synthetic data generation provides an efficient way to build evaluation datasets for GenAI applications. Instead of manually creating test cases or relying solely on production traces, you can seed an evaluation dataset with synthetically generated records derived from your source documents. This approach is particularly valuable when you need rapid prototyping or want to ensure broad coverage of potential inputs. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources for Evaluation Datasets

MLflow evaluation datasets can be created from several sources:

- **Existing traces**: Historical interactions captured by [MLflow Tracing](/concepts/mlflow-tracing.md) from a GenAI application
- **Existing datasets or directly entered examples**: Useful for quick prototyping or targeted testing
- **Synthetic data**: Automatically generated from documents to provide representative coverage
- **Domain expert labels**: Human-curated examples with expected outputs

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Use Cases

Synthetic data generation supports several evaluation goals:

- **Quality improvement**: Test fixes against known problematic patterns derived from source documents
- **Regression prevention**: Create a "golden set" of examples that must always work correctly
- **Version comparison**: Test different prompts, models, or app logic against consistent synthetic data
- **Targeted feature testing**: Build specialized datasets for safety, domain knowledge, or edge cases
- **Cross-environment validation**: Validate the app across different environments as part of [LLMOps](/concepts/large-language-models-llms-on-databricks.md)

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Creating Evaluation Datasets

### Prerequisites

- `CREATE TABLE` permissions on a [Unity Catalog](/concepts/unity-catalog.md) schema
- An existing [MLflow Experiment](/concepts/mlflow-experiment.md) to attach the dataset to

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the UI

To create a dataset from existing traces:

1. Navigate to **Experiments** in the sidebar and open your experiment
2. Click **Traces** in the left sidebar
3. Select the traces to include using checkboxes
4. Click **Actions** and select **Add to evaluation dataset**
5. Either create a new dataset or export to an existing one

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the SDK

To create a dataset programmatically:

```python
import mlflow
import mlflow.genai.datasets

# Create an evaluation dataset
uc_schema = "workspace.default"
eval_dataset = mlflow.genai.datasets.create_dataset(
    name=f"{uc_schema}.email_generation_eval",
)
```

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

To add records from traces:

```python
# Search for traces
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    order_by=["attributes.timestamp_ms DESC"],
    max_results=10,
)

# Add traces to the dataset
eval_dataset = eval_dataset.merge_records(traces)
```

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Storage and Governance

MLflow evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance capabilities. This ensures that synthetic datasets are tracked and managed alongside other data assets. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

- Evaluation datasets cannot be stored in catalogs encrypted with [customer-managed keys (CMK)](https://docs.databricks.com/aws/en/security/keys/cmek-unity-catalog). Workspaces with CMK are supported as long as the dataset is stored in a non-CMK catalog.
- Maximum of 2000 rows per evaluation dataset
- Maximum of 20 expectations per dataset record

^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Systematic testing of GenAI application quality
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — The structured collections used for GenAI evaluation
- [LLM Judges](/concepts/llm-judges.md) — Automated evaluation using LLMs as evaluators
- [Custom Judges](/concepts/custom-judges.md) — Building custom LLM judges for specific evaluation criteria
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — Incorporating domain expert labels to enrich evaluation data

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
