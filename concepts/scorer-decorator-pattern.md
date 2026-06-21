---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9fa6037d1b0cf9fde288efc9a725daa48d0686823c943bb26554afcae1b58fda
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - scorer-decorator-pattern
    - SDP
  citations:
    - file: code-based-scorers-databricks-on-aws.md
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Scorer decorator pattern
description: The @scorer decorator for defining lightweight, stateless custom evaluation functions in MLflow's GenAI evaluation framework
tags:
  - mlflow
  - python
  - decorator
timestamp: "2026-06-18T10:57:56.583Z"
---

# Scorer decorator pattern

The **scorer decorator pattern** is a Python programming pattern used in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for GenAI that defines evaluation metrics as modular, reusable functions decorated with `@scorer`. This pattern allows developers to create custom [Code-based Scorers](/concepts/code-based-scorers.md) that evaluate the quality of AI responses without requiring predefined or built-in [LLM Judges](/concepts/llm-judges.md).^[code-based-scorers-databricks-on-aws.md]

## Overview

The `@scorer` decorator is provided by `mlflow.genai.scorers` and transforms a standard Python function into an evaluation metric that can be passed to `mlflow.genai.evaluate()`. Decorated functions accept arguments such as `outputs`, `inputs`, or [[MLflow Trace]] objects and return either primitive values (`bool`, `int`, `float`, `str`) or [Feedback](/concepts/feedback-object.md) objects.^[code-based-scorer-examples-databricks-on-aws.md]

A `@scorer`-decorated function must be defined and registered from a **Databricks notebook** when used with [Production Monitoring](/concepts/production-monitoring.md). The monitoring service serializes the function code for remote execution, which requires the notebook environment. Class-based `Scorer` subclasses are **not supported** for production monitoring.^[code-based-scorers-databricks-on-aws.md]

## Function signature

A `@scorer`-decorated function can accept any combination of the following parameters, resolved by keyword argument:

- `outputs` — the output from the AI application
- `inputs` — the input dictionary provided to the application
- `predictions` — model predictions (for non-generative AI use cases)
- `targets` — ground truth labels for supervised evaluation
- `expectations` — ground truth values or labels provided in the evaluation dataset
- `trace` — an optional [[MLflow Trace]] object for access to spans and span-level metadata

^[code-based-scorer-examples-databricks-on-aws.md]

The decorator resolves each parameter automatically based on its name. This allows the same scorer to work with different data structures in the evaluation dataset.

## Return types

A `@scorer`-decorated function can return:

- **A primitive value** (`bool`, `int`, `float`, `str`) — the function name becomes the metric name. If the value is `None`, the evaluation is marked as an error.
- **A single [Feedback](/concepts/feedback-object.md) object** — the `name` field in the `Feedback` object determines the metric name. If no `name` is provided, the function name becomes the metric name.
- **A list of [Feedback](/concepts/feedback-object.md) objects** — returned as multiple assessments from a single scorer. Each `Feedback` object must have a unique `name`, which becomes the metric name in the evaluation results. This pattern allows one scorer to assess multiple quality facets (such as PII, sentiment, and conciseness) simultaneously.
- **`None`** — indicates the scorer could not compute a result, and the evaluation is marked as an error.

^[code-based-scorer-examples-databricks-on-aws.md]

## Naming conventions

The metric name in evaluation results depends on the return type and whether a `name` is specified:

- **Primitive value or single `Feedback` without a name**: The function name becomes the metric name.
- **Single `Feedback` with an explicit `name`**: The name specified in the `Feedback` object is used as the metric name.
- **Multiple `Feedback` objects**: The `name` specified in each `Feedback` object is preserved. A unique name must be specified for each `Feedback`.
- **Class-based `Scorer` subclass**: The `name` field defined on the class determines the metric name. If the class returns `Feedback` objects, those names override the class name.

^[code-based-scorer-examples-databricks-on-aws.md]

## Error handling

The `@scorer` decorator pattern supports two error handling approaches:

1. **Return `None` or a `Feedback` with an AssessmentError** — allows the scorer to report a failure without raising an exception.
2. **Raise an exception** — MLflow catches the exception and marks the evaluation as failed, continuing evaluation for other scorers.

Both approaches allow evaluation to continue even if some scorers fail.^[code-based-scorer-examples-databricks-on-aws.md]

## Production monitoring requirements

`@scorer`-decorated functions used in production monitoring must:

- Be defined and registered from a **Databricks notebook**.
- Use the decorator form (not class-based `Scorer` subclasses).
- Manage any required state inside the function body, since class-based `Scorer` subclasses are not supported for production monitoring.

^[code-based-scorers-databricks-on-aws.md]

## Examples

Below are examples extracted from the [code-based scorer examples](/concepts/code-based-scorers.md) documentation. These illustrate common patterns.

### Example: Access data from the Trace

The following scorer checks if the total execution time of a trace is within an acceptable range by accessing SpanType information:

```python
@scorer
def llm_response_time_good(trace: Trace) -> Feedback:
    llm_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
    response_time = (llm_span.end_time_ns - llm_span.start_time_ns) / 1e9
    max_duration = 5.0
    if response_time <= max_duration:
        return Feedback(
            value="yes",
            rationale=f"LLM response time {response_time:.2f}s is within the {max_duration}s limit."
        )
    else:
        return Feedback(
            value="no",
            rationale=f"LLM response time {response_time:.2f}s exceeds the {max_duration}s limit."
        )
```

^[code-based-scorer-examples-databricks-on-aws.md]

### Example: Keyword check from expectations

The following scorer checks if all `expected_keywords` from the `expectations` are present in the assistant's response:

```python
@scorer
def keyword_presence_scorer(outputs: str, expectations: dict[str, Any]) -> Feedback:
    expected_keywords = expectations.get("expected_keywords")
    if expected_keywords is None:
        return Feedback(value="yes", rationale="No keywords were expected in the response.")
    missing_keywords = []
    for keyword in expected_keywords:
        if keyword.lower() not in outputs.lower():
            missing_keywords.append(keyword)
    if not missing_keywords:
        return Feedback(value="yes", rationale="All expected keywords are present in the response.")
    else:
        return Feedback(value="no", rationale=f"Missing keywords: {', '.join(missing_keywords)}.")
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [code-based scorer examples](/concepts/code-based-scorers.md) — Detailed examples demonstrating various patterns for the `@scorer` decorator
- custom LLM scorers — Alternative approach using LLM-as-a-judge for semantic evaluation
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation framework that consumes decorated scorers
- [[MLflow Trace]] — The data object accessible within `@scorer`-decorated functions
- [Feedback](/concepts/feedback-object.md) — The value object returned by scorers
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying scorers for continuous evaluation

## Sources

- code-based-scorer-examples-databricks-on-aws.md
- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
2. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
