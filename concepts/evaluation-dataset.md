---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 315649ef311d1c61072002298f8656be436ec20e4be1bdd4fa2502d2ae8fd199
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset
    - EvaluationDataset
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Evaluation Dataset
description: A curated, versioned collection of test cases with inputs and optional ground truth expectations, used for systematically testing and validating a GenAI application's quality.
tags:
  - mlflow
  - evaluation
  - testing
timestamp: "2026-06-19T14:21:26.806Z"
---

# Evaluation Dataset

An **Evaluation Dataset** is a curated collection of test cases used for systematically testing the quality of a GenAI application. Within the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) data model, evaluation datasets are the primary input for offline quality evaluation, allowing developers to measure and improve application performance before deployment.

## Overview

Evaluation datasets are a key component of the evaluation data hierarchy under an [experiment](/concepts/mlflow-experiment.md). Each dataset contains a set of records, where each record includes the application’s input (such as a conversation history) and, optionally, an expectation — a ground-truth label that defines the correct output for that input. ^[concepts-data-model-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Datasets are typically created by selecting representative [Traces](/concepts/traces.md) from production or development logs. They are versioned over time, allowing teams to track how their test suite evolves alongside the application. ^[concepts-data-model-databricks-on-aws.md]

## Use Cases

Evaluation datasets serve two primary purposes:

1. **Iterative development and improvement.** By running `mlflow.genai.evaluate()` with an evaluation dataset and a set of [[scorers]], developers can measure how well the current version of the application performs and identify specific quality gaps. ^[concepts-data-model-databricks-on-aws.md]
2. **Regression prevention.** When making changes to an application — such as modifying the system prompt, changing the model, or adding new tools — the same evaluation dataset can be re-used to validate that quality has not regressed. ^[concepts-data-model-databricks-on-aws.md]

In an [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), both variants must be evaluated against the identical evaluation dataset to ensure fair comparison of the resulting feedback scores. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Creating an Evaluation Dataset

Evaluation datasets are built by selecting representative traces from the application's execution history. The process includes:

- Choosing inputs that reflect the range of real-world queries the application will encounter.
- Optionally annotating each input with ground-truth expectations. These expectations may come from domain expert labeling sessions or from manually curated test cases.
- Versioning the dataset after each significant change to maintain a clear record of the test suite evolution. ^[concepts-data-model-databricks-on-aws.md]

Datasets can be managed through the MLflow Experiment UI, where they can be searched, viewed, and versioned alongside evaluation results. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Evaluation Dataset](/concepts/evaluation-dataset.md) management in the MLflow Experiment UI
- [Evaluation Run](/concepts/evaluation-run.md) — the result of running `evaluate()` against a dataset
- [[Scorers]] — functions that assess trace quality and produce feedback
- [Traces](/concepts/traces.md) — execution logs that serve as source material for dataset creation
- [Labeling Sessions](/concepts/labeling-sessions.md) — a mechanism for collecting expert annotations used to create ground truth expectations
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — a workflow that depends on a shared evaluation dataset

## Sources

- concepts-data-model-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
