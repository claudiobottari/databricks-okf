---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 068bd9b062196a6ec1196adc84f1c7727188b2577422601592aab9b24bb2fc35
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - synthetic-evaluation-data-generation
    - SEDG
    - Synthetic Evaluation Generation
    - Synthetic Evaluation Set Generation
    - Synthetic evaluation generation
    - Synthetic evaluation set generation
    - synthetic evaluation generation
    - synthetic evaluation set generation
    - Synthetic Data
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Synthetic Evaluation Data Generation
description: Databricks' ability to automatically generate a representative evaluation set from source documents, enabling quick coverage of test cases without manually curating examples.
tags:
  - synthetic-data
  - evaluation
  - genai
  - databricks
timestamp: "2026-06-19T14:10:37.286Z"
---

# Synthetic Evaluation Data Generation

**Synthetic Evaluation Data Generation** is a Databricks feature within [MLflow](/concepts/mlflow.md) that automatically creates a representative evaluation dataset from a user’s documents. This allows you to build a coverage‑rich set of test cases for evaluating a GenAI application without manually curating examples. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Overview

Evaluation datasets are essential for systematically testing and improving GenAI applications. They help improve quality, prevent regressions, compare app versions, target specific features, and validate across environments as part of [LLMOps](/concepts/large-language-models-llms-on-databricks.md). Databricks offers several ways to create an evaluation dataset: from existing [traces](/concepts/mlflow-tracing.md), from an existing dataset or directly entered examples, or by generating synthetic data from your documents. The synthetic data approach is designed to produce a representative evaluation set with good coverage of test cases. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

MLflow evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built‑in versioning, lineage, sharing, and governance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Requirements

To create any evaluation dataset—including one generated synthetically—you must have `CREATE TABLE` permissions on a Unity Catalog schema. The dataset is attached to an MLflow experiment. If you do not already have an experiment, you must create one before proceeding. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## How It Works

When you choose the synthetic data option during evaluation dataset creation, Databricks analyzes the documents you provide and generates a set of input examples that represent typical usage scenarios for your application. These examples are then stored as records in the evaluation dataset. The exact method of generation is handled automatically by the platform. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

The synthetic dataset can be created using either the Databricks UI or the MLflow SDK. In the SDK workflow, after calling `mlflow.genai.datasets.create_dataset()`, you can seed the dataset with synthetic data during the “add records” step—this option is documented as **Seed using synthetic data**. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Benefits

- **Speed**: Eliminates the manual effort of writing test cases one by one.
- **Coverage**: Produces a diverse set of inputs that exercise different parts of your application.
- **Representativeness**: Leverages your actual documents to generate examples that mirror real‑world usage.
- **Integration**: The resulting dataset is stored in Unity Catalog with full governance and is immediately usable for evaluation inside MLflow.

These benefits are implied by the feature description and the general advantages of evaluation datasets. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Limitations

Synthetic evaluation datasets are subject to the same general limitations as all MLflow evaluation datasets:

- Datasets cannot be stored in catalogs encrypted with customer‑managed keys (CMK), though non‑CMK catalogs are supported.
- Maximum of 2000 rows per evaluation dataset.
- Maximum of 20 expectations per dataset record.

If any of these limits are restrictive for your use case, contact your Databricks representative. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The broader concept of curated test examples for GenAI evaluation.
- [MLflow](/concepts/mlflow.md) – The open‑source platform underlying this feature.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer storing evaluation datasets.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Captures real‑world interactions that can also seed evaluation datasets.
- [Synthetic Data](/concepts/synthetic-evaluation-data-generation.md) – The general category of artificially generated data for testing and training.
- [GenAI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) – The process of assessing quality, safety, and performance of generative AI apps.
- [LLMOps](/concepts/large-language-models-llms-on-databricks.md) – Operational practices for managing LLM applications, of which evaluation is a key part.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
