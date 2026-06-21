---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: deaad1a1b0d2dc898796acd096bcc43d84bd72772b27c8fe4937034fb9a7b318
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - answer-sheet-evaluation-mode
    - ASEM
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Answer Sheet Evaluation Mode
description: Evaluation mode for scoring pre-computed outputs or existing traces without running the app directly, useful for external systems or historical data.
tags:
  - mlflow
  - evaluation
  - offline
timestamp: "2026-06-19T10:24:32.397Z"
---

# Answer Sheet Evaluation Mode

**Answer Sheet Evaluation Mode** is a configuration of `mlflow.genai.evaluate()` that scores pre-computed outputs or existing traces without calling the GenAI application directly. This mode is useful when outputs are already available from external systems, historical traces, batch jobs, or any scenario where running the app during evaluation is undesirable or impossible.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Overview

In answer sheet evaluation, you supply evaluation data consisting of either (a) inputs and their corresponding pre-computed outputs, or (b) existing traces. The `evaluate()` function applies the specified [[scorers]] (including [LLM Judges](/concepts/llm-judges.md)) to assess quality, creates feedback entries, and stores the results in an [Evaluation Run](/concepts/evaluation-run.md) within the active MLflow experiment.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

This mode contrasts with [Direct Evaluation](/concepts/direct-evaluation.md), where MLflow calls the app itself (via a `predict_fn`) to generate traces for scoring. In answer sheet evaluation no live app call is made; the outputs or traces are provided directly.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## When to Use

- You already have outputs from an external system, a batch job, or a previous run.
- You want to score historical traces that were captured from production.
- You cannot or prefer not to run the GenAI app during evaluation for cost, latency, or access reasons.

## Important Considerations

If you use an answer sheet with traces that differ from those produced in your production environment, you may need to rewrite your scorer functions before using them for [Production Monitoring](/concepts/production-monitoring.md). The evaluation relies on the structure and content of the provided traces, and mismatches can cause scorers to behave differently.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Data Formats

### Inputs and Outputs

Each record must contain an `inputs` dictionary and an `outputs` dictionary. The function constructs traces from these pairs and then applies the scorers.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Existing Traces

You can supply a list of existing traces (e.g., retrieved via `mlflow.search_traces()`). The function applies the scorers directly on those traces.^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Examples

### Using Inputs and Outputs

```python
import mlflow
from mlflow.genai.scorers import Safety, RelevanceToQuery

# Pre-computed results from your GenAI app
results_data = [
    {
        "inputs": {"question": "What is MLflow?"},
        "outputs": {"response": "MLflow is an open-source platform for managing machine learning workflows, including tracking experiments, packaging code, and deploying models."},
    },
    {
        "inputs": {"question": "How do I get started?"},
        "outputs": {"response": "To get started with MLflow, install it using 'pip install mlflow' and then run 'mlflow ui' to launch the web interface."},
    }
]

# Evaluate pre-computed outputs
evaluation = mlflow.genai.evaluate(
    data=results_data,
    scorers=[Safety(), RelevanceToQuery()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Using Existing Traces

```python
import mlflow

# Retrieve traces from production
traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
)

# Evaluate problematic traces
evaluation = mlflow.genai.evaluate(
    data=traces,
    scorers=[Safety(), RelevanceToQuery()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
