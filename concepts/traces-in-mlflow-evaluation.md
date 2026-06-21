---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e2c636a438cfb7213222891c49ede87cc65c596d1290c0b77cb3a87921e3b919
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traces-in-mlflow-evaluation
    - TIME
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Traces in MLflow Evaluation
description: Per-input evaluation records within an evaluation run, each containing inputs, outputs, and associated feedback for one example in the evaluation dataset.
tags:
  - mlflow
  - evaluation
  - traces
  - genai
timestamp: "2026-06-19T10:24:40.094Z"
---

# Traces in MLflow Evaluation

A **trace** is a per-example record created during an [Evaluation Run](/concepts/evaluation-run.md) in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for a GenAI application. Each trace corresponds to one input from the evaluation dataset and captures the full input-output cycle along with any quality feedback assigned to it. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Structure

Every trace stored in an evaluation run contains the following components: ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

- **`inputs`** – The raw example from the evaluation dataset (e.g. a question or prompt).
- **`outputs`** – The response produced by the GenAI application for that input.
- **`feedbacks`** – Quality scores from the scorers (judges) attached to the evaluation, such as correctness, relevance, or safety ratings.

## Role in Evaluation Runs

When you call `mlflow.genai.evaluate()`, MLflow automatically creates one trace for every row in the provided dataset. The collection of all traces, together with aggregate metrics and metadata, forms the evaluation run. Traces provide granular, example-level insight into application behavior, complementing the summary statistics. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Related Concepts

- [Evaluation runs in MLflow](/concepts/evaluation-run-mlflow.md) – The parent structure that organizes traces, metrics, and metadata.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The overall framework for assessing GenAI applications.
- [Feedbacks in MLflow Evaluation](/concepts/feedback-mlflow-evaluation.md) – The per-trace quality assessments from scorers.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
