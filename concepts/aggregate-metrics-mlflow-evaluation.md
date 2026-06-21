---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f43a606c74fa166bc5e8709fe7f21e553fff49c73f68b837d6706c0cfab325b2
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - aggregate-metrics-mlflow-evaluation
    - AM(E
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Aggregate Metrics (MLflow Evaluation)
description: Summary statistics computed across all evaluated examples in an evaluation run, such as mean correctness or pass rates.
tags:
  - mlflow
  - evaluation
  - metrics
  - statistics
timestamp: "2026-06-18T12:13:43.142Z"
---

---
title: Aggregate Metrics (MLflow Evaluation)
summary: Aggregate statistics computed across all evaluated examples in an MLflow evaluation run, summarizing model performance for each scorer.
sources:
  - evaluation-runs-in-mlflow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - evaluation
  - metrics
  - genai
aliases:
  - aggregate-metrics-mlflow-evaluation
  - AMME
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Aggregate Metrics (MLflow Evaluation)

**Aggregate Metrics** are summary statistics computed across all evaluated examples in an [ evaluation run](/concepts/evaluation-run-mlflow.md) of a GenAI application. They represent the overall performance of the model or agent according to each [[Scorers|scorer]] applied during the evaluation. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## How Aggregate Metrics Are Computed

When you call `mlflow.genai.evaluate()`, MLflow processes each input in the evaluation dataset, collects the model’s output (or trace), and runs each registered scorer against that output. The individual scores from each scorer (one per example) are then aggregated across the entire dataset to produce a single summary statistic, such as a mean or pass rate. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

For example, if a scorer returns a numerical score for each of 100 evaluation examples, MLflow computes the mean of those 100 scores as the aggregate metric. For binary pass/fail scorers, MLflow may compute a pass rate (e.g., the fraction of examples that passed). ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Examples of Aggregate Metrics

The source material provides examples of common aggregate metrics produced during an evaluation run:

- **`correctness_mean`**: 0.85 – The average correctness score across all examples.
- **`relevance_mean`**: 0.92 – The average relevance score across all examples.
- **`safety_pass_rate`**: 1.0 – The fraction of examples that passed a safety check.

These metrics are stored as part of the evaluation run’s MLflow Runs | run metadata and can be compared across different runs to track progress. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Relationship with Traces and Individual Feedback

Each example’s trace contains its own individual feedback from scorers (e.g., `correctness: 0.8`, `relevance: 1.0`). Aggregate metrics summarize those individual feedback values into one number for the whole evaluation run. Together with the per‑trace feedback and the full [[MLflow Trace|traces (MLflow) | traces]], aggregate metrics provide both a high‑level summary and the granular detail needed to diagnose issues. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Role in the Evaluation Run Structure

Aggregate metrics are a top‑level component of an evaluation run, alongside:

- **Run Info**: unique ID, experiment, timestamps, status.
- **Traces**: one trace per dataset row, each with inputs, outputs, and feedbacks.
- **Parameters**: model version, dataset name, list of scorers.

The evaluation run stores these aggregate metrics so that you can retrieve them later via the MLflow Tracking API, use them in dashboards, or compare runs in the MLflow UI. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Usage

Developers commonly use aggregate metrics to:

- Compare the quality of different model versions or prompt configurations in [ A/B tests](/concepts/ab-comparison-of-agent-configurations.md).
- Set quality gates for promoting models to production.
- Detect regressions by monitoring metric trends over time.
- Report overall system performance to stakeholders.

## Related Concepts

- [Evaluation Runs](/concepts/evaluation-runs.md) – The container that organizes traces, feedback, metrics, and parameters for a single evaluation.
- [Scorers / Judges](/concepts/scorers-and-llm-judges.md) – Individual evaluators that produce scores per example, which are then aggregated.
- [Traces (MLflow)](/concepts/trace-tags-mlflow.md) – Detailed records of each example’s inputs, outputs, and intermediate steps.
- [MLflow GenAI Evaluate](/concepts/mlflow-genai-evaluation.md) – The API that creates evaluation runs and computes aggregate metrics.
- [Feedback](/concepts/feedback-object.md) – Per‑example quality scores from scorers, the raw data for aggregation.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
