---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d0da598e7a31e0af49f5cac8d6150f905ab03cd724f58dfc9f01e713136311a
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - golden-dataset
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Golden Dataset
description: A 'golden set' of evaluation examples that must always work correctly, used to prevent regressions when testing fixes and changes to prompts, models, or app logic.
tags:
  - evaluation
  - testing
  - quality
timestamp: "2026-06-18T14:33:55.961Z"
---

# Golden Dataset

A **Golden Dataset** (also called a golden test set or golden evaluation set) is a curated collection of example inputs used to systematically evaluate and improve a GenAI application. Golden datasets are a core component of the MLflow evaluation framework, providing a standardized benchmark for testing model quality, preventing regressions, and comparing application versions. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Purpose

Golden datasets serve several key functions in the GenAI development lifecycle:

- **Improve quality** by testing fixes against known problematic examples from production. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Prevent regressions** by maintaining a set of examples that must always work correctly. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Compare app versions** by testing different prompts, models, or app logic against the same data. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Target specific features** by building specialized datasets for safety, domain knowledge, or edge cases. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Validate across environments** as part of LLMOps. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Data Sources

You can create a golden dataset from several sources:

- **Existing traces** – If you have captured traces from a GenAI application, you can use them to create an evaluation dataset based on real-world scenarios. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **An existing dataset or directly entered examples** – Useful for quick prototyping or targeted testing of specific features. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Synthetic data** – Databricks can automatically generate a representative evaluation set from your documents, allowing you to quickly evaluate your agent with good coverage of test cases. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Storage and Governance

MLflow evaluation datasets are stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The evaluation framework that uses golden datasets
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – Broader concept encompassing golden datasets
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for quality analysis
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing agent versions against golden datasets
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers used with golden datasets

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
