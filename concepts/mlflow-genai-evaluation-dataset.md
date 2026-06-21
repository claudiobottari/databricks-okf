---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acc1e607ce73728415f7a4999e2ef0a53be946bfc01660baab9dcea6a9598e81
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-dataset
    - MGED
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: MLflow GenAI Evaluation Dataset
description: A curated, versioned collection of test cases (inputs and optional ground-truth expectations) used to systematically evaluate and improve a GenAI application's quality.
tags:
  - mlflow
  - evaluation
  - dataset
timestamp: "2026-06-18T11:05:37.630Z"
---

# MLflow GenAI Evaluation Dataset

**MLflow GenAI Evaluation Datasets** are curated collections of test cases for systematically testing your generative AI application. They organize the inputs (and optionally ground truth) that you feed to the [evaluation harness](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) to measure quality. ^[concepts-data-model-databricks-on-aws.md]

## Overview

An evaluation dataset is a versioned artifact stored inside an [MLflow Experiment](/concepts/mlflow-experiment.md). It lives alongside other experiment objects such as [Traces](/concepts/traces.md), [Prompts](/concepts/prompt-versioning.md), and [Logged Models](/concepts/logged-models.md). Evaluation datasets are typically created by selecting representative traces from production or development, then using those as test cases.

## How evaluation datasets are used

Evaluation datasets are the primary input to [`mlflow.genai.evaluate()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness), the MLflow SDK for systematic quality evaluation. When you run evaluation:

1. The evaluation harness takes the dataset, your application's prediction function, and a set of [[scorers]] as input.
2. It runs your app for every record in the dataset, producing traces.
3. It runs each scorer on the resulting traces to assess quality, producing feedback.
4. Each feedback is attached to the appropriate trace.

The result is an [Evaluation Run](/concepts/evaluation-run.md) that contains aggregated metrics and per-trace assessments. ^[concepts-data-model-databricks-on-aws.md]

## What datasets contain

Each evaluation dataset record typically includes:

- **Inputs**: The data your app receives at inference time (e.g., a user query).
- **Expectations (optional)**: [Ground truth labels](/concepts/ground-truth-in-llm-evaluation.md) that define the correct output for a given input. These are added by domain experts and serve as a "gold standard" to evaluate if your app produced the right response.

When a dataset includes expectations, evaluation can compare your app's actual outputs against those expectations to detect regressions. ^[concepts-data-model-databricks-on-aws.md]

## Dataset versioning

Evaluation datasets are versioned over time to track how your test suite evolves as your application changes. This allows you to:

- Compare quality across application versions using the same test cases.
- Validate that changes (new prompts, model updates, LLM configuration) haven't introduced regressions.
- Track which test cases catch regressions and which become stale. ^[concepts-data-model-databricks-on-aws.md]

## Building evaluation datasets

Creating an evaluation dataset typically involves:

1. **Selecting representative traces** from production logs or development sessions.
2. **Optionally adding ground truth** (expectations) for systematic evaluation.
3. **Structuring the data** as a collection of records that match your app's input schema.

See the guide to [build evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) for detailed techniques, including how to select and use production traces. ^[concepts-data-model-databricks-on-aws.md]

## Relationship to other entities in the data model

- **Experiments**: The dataset lives within an [Experiment](/concepts/mlflow-experiment.md), which is the container for a single application's data. ^[concepts-data-model-databricks-on-aws.md]
- **Traces**: Datasets are typically sourced from traces — the execution logs captured automatically in development and production. ^[concepts-data-model-databricks-on-aws.md]
- **Scorers**: Scorers evaluate each dataset record's corresponding trace, producing [Feedback](/concepts/feedback-object.md) assessments. ^[concepts-data-model-databricks-on-aws.md]
- **Evaluation runs**: The output of running a dataset through the evaluation harness is an evaluation run that contains aggregated metrics and per-trace assessments. ^[concepts-data-model-databricks-on-aws.md]

## Related concepts

- [Evaluation Run](/concepts/evaluation-run.md) — The result of testing an app version against an evaluation dataset
- [[Scorers|Scorer]] — A function that evaluates a trace's quality
- [Feedback](/concepts/feedback-object.md) — Quality measurement output from a scorer
- [Trace](/concepts/traces.md) — An app execution log that can become a dataset record
- [MLflow Experiment](/concepts/mlflow-experiment.md) — The container for all app artifacts
- Ground truth label — The correct output for a given input

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
