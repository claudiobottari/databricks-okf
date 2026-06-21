---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ceeac60e6c76687e3f931bec5185af2196611a931374edff948368b316a66809
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - synthetic-data-generation-for-evaluation
    - SDGFE
    - Synthetic data generation
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Synthetic Data Generation for Evaluation
description: Databricks' capability to automatically generate a representative evaluation set from documents, enabling quick evaluation of agents with good coverage of test cases without requiring pre-existing labeled data.
tags:
  - synthetic-data
  - genai
  - evaluation
timestamp: "2026-06-19T09:11:14.589Z"
---

## Synthetic Data Generation for Evaluation

**Synthetic Data Generation for Evaluation** is a feature of [MLflow](/concepts/mlflow.md) on Databricks that automatically creates a representative evaluation dataset from a set of input documents. This allows developers to quickly test and improve a GenAI agent without requiring manually curated examples or historical traces.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Overview

An [Evaluation Dataset](/concepts/evaluation-dataset.md) is a selected set of example inputs used to systematically test the quality of a GenAI application. Synthetic data generation helps populate such a dataset automatically, providing **good coverage of test cases** from source documents. This is particularly useful during rapid prototyping or when historical application traces are not yet available.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

The generated dataset is stored in [Unity Catalog](/concepts/unity-catalog.md), which provides built-in versioning, lineage, sharing, and governance. It can be attached to an [MLflow Experiment](/concepts/mlflow-experiment.md) for ongoing evaluation workflows.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Use Cases

- **Quick prototyping** – Generate a test set from documentation or sample data to evaluate an early-stage agent.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Coverage of edge cases** – Synthetic generation can produce varied inputs that exercise different parts of the application, helping to identify blind spots.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Seed for iterative improvement** – The synthetic dataset can be used as a starting point and later enriched with human-labelled examples or real traces.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### How It Works

The exact mechanism of synthetic data generation is not detailed in the source material, but the feature is described as a method to seed an evaluation dataset: the platform “can automatically generate a representative evaluation set from your documents.”^[building-mlflow-evaluation-datasets-databricks-on-aws.md] It is available as one of several options for creating or adding records to a dataset (alongside importing from traces, domain expert labels, or building from scratch).^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Related Concepts

- [Building MLflow evaluation datasets](/concepts/mlflow-evaluation-datasets.md) – The broader dataset creation workflow.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The organizational unit that evaluation datasets are attached to.
- Evaluation dataset from traces – An alternative method using captured application logs.
- [Human feedback alignment](/concepts/human-feedback-for-llm-judge-alignment.md) – Enriching synthetic data with expert annotations.
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md) – A prerequisite for serverless workloads that generate synthetic data; misconfiguration can cause a 403 PERMISSION_DENIED Serverless Budget Policy Error.^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

### Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
