---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d04c23e82215d771b53d93a14986b2b405198cbab189684cbce9c8fed669ca3
  pageDirectory: concepts
  sources:
    - evaluation-runs-in-mlflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-mlflow-evaluation
    - T(E
    - Trace location
  citations:
    - file: evaluation-runs-in-mlflow-databricks-on-aws.md
title: Trace (MLflow Evaluation)
description: A per-input record within an evaluation run that captures the input prompt, model output, and any associated feedback from scorers.
tags:
  - mlflow
  - evaluation
  - traces
  - genai
timestamp: "2026-06-18T12:13:35.811Z"
---

# Trace (MLflow Evaluation)

A **Trace** in [MLflow](/concepts/mlflow.md) [evaluation runs](/concepts/evaluation-runs.md) is a record of a single evaluation example’s execution. Each trace captures the inputs provided to the GenAI application, the outputs generated, and the quality assessments (feedback) produced by the [[Scorers]] attached to the evaluation. Traces are the fundamental unit of analysis within an evaluation run. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Structure

Every trace corresponds to one row in the evaluation dataset. The trace contains:

- **inputs** – The example passed to the application (e.g., a question or prompt).
- **outputs** – The response returned by the application.
- **feedbacks** – A list of scores or verdicts produced by the evaluation scorers (e.g., correctness, relevance, safety).

A trace is created automatically when `mlflow.genai.evaluate()` executes for each dataset entry. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Relationship to Evaluation Runs

An evaluation run organises multiple traces alongside aggregate metrics and metadata. The trace-level feedback is aggregated into summary statistics (e.g., mean correctness, pass rate) that appear in the run’s metrics. Traces are stored under the run’s ID and can be retrieved for detailed inspection. ^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Example

The following conceptual structure shows two traces within an evaluation run:

```
Evaluation Run
├── run_id: ...
├── Traces (one per dataset row)
│   ├── Trace 1
│   │   ├── inputs: {"question": "What is MLflow?"}
│   │   ├── outputs: {"response": "MLflow is..."}
│   │   └── feedbacks: [correctness: 0.8, relevance: 1.0]
│   ├── Trace 2
│   │   ├── inputs: {"question": "How to log a model?"}
│   │   ├── outputs: {"response": "Use mlflow.log_model..."}
│   │   └── feedbacks: [correctness: 0.9, relevance: 0.9]
└── Aggregate Metrics
    ├── correctness_mean: 0.85
    └── relevance_mean: 0.95
```

^[evaluation-runs-in-mlflow-databricks-on-aws.md]

## Use Cases

- **Debugging**: Inspect individual traces to understand why a scorer gave a low or unexpected rating.
- **Trace-based evaluation**: Some [Custom Judges](/concepts/custom-judges.md) analyse the full execution trace – including tool calls and intermediate steps – to assess agent behaviour. See [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) for an example of trace-based judges.
- **Quality monitoring**: Traces collected in production can be compared with evaluation traces to detect drift.

## Related Concepts

- [Evaluation Runs](/concepts/evaluation-runs.md) – The parent container for traces.
- [[Scorers]] – Functions that produce the feedback values stored in each trace.
- [Feedback (MLflow Evaluation)](/concepts/feedback-mlflow-evaluation.md) – The per-trace quality assessments.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework that creates evaluation runs and traces.

## Sources

- evaluation-runs-in-mlflow-databricks-on-aws.md

# Citations

1. [evaluation-runs-in-mlflow-databricks-on-aws.md](/references/evaluation-runs-in-mlflow-databricks-on-aws-05902839.md)
