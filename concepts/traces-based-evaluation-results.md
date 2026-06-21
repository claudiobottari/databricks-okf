---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8fadfd15f86dcfc92da9021e71e92b08dd7d08dd02480fec3d4cec28028596ac
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - traces-based-evaluation-results
    - TER
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: Traces-Based Evaluation Results
description: Evaluation results in MLflow 3 are stored as traces with assessments, accessed via mlflow.search_traces() instead of direct result tables like results.tables['eval_results'].
tags:
  - mlflow
  - tracing
  - evaluation
timestamp: "2026-06-19T19:34:53.860Z"
---

# Traces-Based Evaluation Results

**Traces-Based Evaluation Results** is the storage and retrieval mechanism introduced in MLflow 3 for evaluating generative AI applications. Instead of returning results in a flat table, the evaluation framework records every run as a trace — a structured execution log with spans and attributes — and attaches scorer outputs as assessments to each trace. This design provides real-time observability, granular inspection, and a unified way to access both the model’s behavior and the evaluation outcomes. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## How It Works

When you call `mlflow.genai.evaluate()` with a set of scorers, the framework invokes the predict function and captures each invocation as a [[MLflow Trace]]. The trace contains spans that record intermediate steps (e.g., tool calls, retrieval operations, model inference). Each scorer then runs against the trace and produces a set of assessments — named values with rationales — which are stored directly on the trace object. The result object returned by `evaluate()` includes a `run_id` that can be used to retrieve the full set of traces. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Accessing Evaluations with `search_traces()`

To inspect evaluation results programmatically, use `mlflow.search_traces()` with the `run_id` from the evaluation result. Each trace has an `info.assessments` attribute that lists the scorer outputs:

```python
traces = mlflow.search_traces(run_id=results.run_id)
for trace in traces:
    for assessment in trace.info.assessments:
        print(f"Scorer: {assessment.name}")
        print(f"Value: {assessment.value}")
        print(f"Rationale: {assessment.rationale}")
```

This replaces the old approach of reading a flat `eval_results` table. The trace also exposes its spans via `traces.data.spans`, which custom scorers can read to extract context such as retrieved documents or intermediate model outputs. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Benefits Over Table-Based Storage

- **Observability**: Traces capture the full execution path, not just final inputs and outputs.
- **Granularity**: Each assessment is linked to a specific trace, enabling drill‑down into why a scorer returned a certain value.
- **Real‑time ingestion**: The trace backend is built for production scale, so results are available immediately after evaluation completes.
- **Unified API**: The same `search_traces()` endpoint works for both raw model invocations and evaluation results.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The underlying tracing infrastructure that records execution spans.
- Evaluation Results – The broader concept of collecting and reviewing model quality metrics.
- [[Scorers]] – Functions that produce assessments attached to traces during evaluation.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – End‑to‑end workflow that uses trace‑based evaluation for AI agents.
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md) – User‑defined scorers that can access trace data for custom metrics.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
