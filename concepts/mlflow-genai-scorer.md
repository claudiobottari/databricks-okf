---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69bce8e1cbb570edad325d0027c3fba292d98cce5da8a7e87e664df423c4cb6d
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-scorer
    - MGS
    - GenAI Scoring
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: MLflow GenAI Scorer
description: A function that evaluates a trace's quality by extracting relevant data fields and passing them to evaluation logic (deterministic code or LLM judge), returning feedback assessments.
tags:
  - mlflow
  - evaluation
  - scoring
timestamp: "2026-06-18T11:05:51.573Z"
---

# MLflow GenAI Scorer

**MLflow GenAI Scorer** is a function that evaluates the quality of a trace produced by a generative AI application. Scorers parse a trace for relevant data fields, evaluate quality using either deterministic code or an LLM judge, and return structured feedback entities with the results. The same scorer can be used for both development evaluation and production monitoring.^[concepts-data-model-databricks-on-aws.md]

## Overview

Scorers are a core component of MLflow for GenAI's quality evaluation framework. They serve as the "adapter" that connects [Traces](/concepts/traces.md) to evaluation logic. While an LLM judge (such as `mlflow.genai.judges.is_correct`) evaluates text based on specific criteria, it cannot directly process traces — it only understands text inputs. Scorers extract the relevant data from a trace (such as the request, response, and retrieved context) and pass it to the judge for evaluation.^[concepts-data-model-databricks-on-aws.md]

Scorers are used in two key contexts:

- **Development evaluation**: Called by `mlflow.genai.evaluate()` to assess traces generated during systematic testing against an evaluation dataset.
- **Production monitoring**: Scheduled via `mlflow.genai.Scorer.start()` to automatically evaluate traces from a deployed application.

In both contexts, scorers produce [feedback assessments](/concepts/mlflow-human-feedback-assessments.md) that are attached to the source trace.^[concepts-data-model-databricks-on-aws.md]

## How Scorers Work

A scorer performs the following steps:

1. **Parse** the trace for relevant data fields (e.g., input, output, retrieved context).
2. **Evaluate** quality using either:
   - Deterministic code (e.g., checking for keywords, computing metrics).
   - An LLM judge (e.g., evaluating correctness, helpfulness, or safety).
3. **Return** a `Feedback` entity containing the evaluation result and an optional rationale.

Scorers can access external resources, such as [Databricks secrets](/concepts/databricks-secret-scopes.md), to authenticate with third-party evaluation endpoints.^[code-based-scorer-reference-databricks-on-aws.md]

## Built-in vs. Custom Scorers

### Built-in Scorers

MLflow provides several built-in scorers via the `mlflow.genai.scorers` module. These cover common evaluation criteria such as correctness, helpfulness, and safety. Built-in scorers require minimal configuration and work out of the box with MLflow's evaluation framework.

### Custom Scorers

When built-in scorers do not meet your evaluation needs, you can define custom scorers using either:

- **The `@scorer` decorator**: A function-based approach that is simpler to define. This is the recommended method for most use cases.
- **The `Scorer` class**: An object-oriented approach that provides more control. This method is not recommended for [Production Monitoring](/concepts/production-monitoring.md).

For detailed implementation guidance, see the [code-based scorer reference](/concepts/code-based-scorers-mlflow-genai.md).^[code-based-scorer-reference-databricks-on-aws.md]

## Feedback Output

Each scorer returns a `Feedback` object with the following structure:

- **value**: The evaluation result (e.g., `"yes"`, `"no"`, a numeric score, or a categorical judgment).
- **rationale**: An optional explanation of the evaluation result, providing interpretability.

Multiple scorers can be applied to the same trace, producing multiple feedback assessments that together give a comprehensive quality picture.^[concepts-data-model-databricks-on-aws.md]

## Scorers vs. Judges

| Aspect | Scorer | Judge |
|--------|--------|-------|
| Input | A [trace](/concepts/traces.md) object | Text strings |
| Purpose | Extracts trace data and feeds it to evaluation logic | Evaluates text based on specific criteria |
| Output | A `Feedback` entity | A judgment value |
| Example | `custom_llm_scorer(trace)` | `mlflow.genai.judges.is_correct` |

Scorers wrap judges to make them compatible with MLflow's trace-based evaluation pipeline.^[concepts-data-model-databricks-on-aws.md]

## Evaluation in Development

In development, scorers are used with `mlflow.genai.evaluate()`. The evaluation harness:

1. Runs the application for every record in an [Evaluation Dataset](/concepts/evaluation-dataset.md), producing traces.
2. Runs each scorer on the resulting traces to assess quality, producing feedback.
3. Attaches each feedback to the appropriate trace.

This produces an [Evaluation Run](/concepts/evaluation-run.md) containing traces with feedback assessments and aggregated metrics.^[concepts-data-model-databricks-on-aws.md]

## Evaluation in Production

In production, scorers can be scheduled to automatically evaluate traces from deployed applications via `mlflow.genai.Scorer.start()`. The production monitoring service:

1. Runs the scorers on production traces, producing feedback.
2. Attaches each feedback to the source trace.

This enables continuous quality monitoring and rapid detection of regressions or problematic queries.^[concepts-data-model-databricks-on-aws.md]

## Accessing External Resources

Custom scorers may need to access external services for evaluation. Scorers can securely retrieve API keys and credentials from [Databricks secrets](/concepts/databricks-secret-scopes.md) by importing `dbutils` from `databricks.sdk.runtime`:

```python
from databricks.sdk.runtime import dbutils
api_key = dbutils.secrets.get(scope='my-scope', key='api-key')
```

This allows scorers to call external LLM endpoints (e.g., Azure OpenAI, AWS Bedrock, Anthropic) or other authenticated services during evaluation.^[code-based-scorer-reference-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) — The execution logs that scorers evaluate
- Feedback (MLflow) — The output object produced by scorers
- [Assessments](/concepts/assessments.md) — Quality measurements attached to traces, including feedback from scorers
- [Evaluation Runs](/concepts/evaluation-runs.md) — Results of testing an application version with scorers
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated test cases used with scorers
- [Production Monitoring](/concepts/production-monitoring.md) — Scheduling scorers on production traces
- [Code-based Scorers](/concepts/code-based-scorers.md) — Reference for implementing custom scorers
- [Accessing Databricks secrets in scorers](/concepts/accessing-databricks-secrets-in-scorers.md) — How to securely retrieve credentials
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API
- [Scorer sampling config](/concepts/scorersamplingconfig.md) — Configuration for controlling which traces are evaluated

## Sources

- concepts-data-model-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
