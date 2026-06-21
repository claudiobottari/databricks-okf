---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ab585aece8557edab0dd0c889e5a7f42da0b451d8e7a20cdd3f9a73322ed02d7
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-code-based-scorers
    - MCS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: MLflow Code-based Scorers
description: Custom Python functions (decorator-based or class-based) that define flexible evaluation metrics for GenAI applications within MLflow Evaluation.
tags:
  - mlflow
  - evaluation
  - genai
  - scorers
timestamp: "2026-06-19T14:12:28.655Z"
---

# MLflow Code-based Scorers

**MLflow Code-based Scorers** are flexible, programmatically defined evaluation metrics for AI agents and applications within MLflow Evaluation for GenAI. Unlike predefined [LLM Judges](/concepts/llm-judges.md), code-based scorers allow you to implement arbitrary logic in Python to assess outputs, trace data, expectations, or any combination thereof.

## Overview

Code-based scorers give you full control over the evaluation process. They can inspect the full [[MLflow Trace]] object, access inputs and outputs, use ground-truth [expectations](/concepts/expectation-vs-feedback-labels.md), call external LLMs, or combine multiple quality checks into a single scorer. Scorers are used with `mlflow.genai.evaluate()` for offline evaluation and, with some restrictions, can be registered for [Production Monitoring](/concepts/production-monitoring.md).^[code-based-scorer-examples-databricks-on-aws.md]

## Defining a Code-based Scorer

### The `@scorer` Decorator

The simplest way to create a code-based scorer is the `@scorer` decorator. A decorated function receives typed parameters (such as `trace`, `inputs`, `outputs`, `expectations`) and returns a primitive value (e.g., `int`, `bool`, `str`, `float`) or an `mlflow.entities.Feedback` object. If the function returns a primitive value, the metric name defaults to the function name; if it returns a `Feedback` object, the metric name is the `name` field of the `Feedback` (or the function name if no name is given).^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    return len(outputs)
```

### Class-based Scorer (Offline Only)

For scorers that require state (e.g., configuration fields), use the `Scorer` base class. It is a Pydantic model; you define additional fields and implement the logic in `__call__`. Class-based scorers are supported only for offline evaluation (`mlflow.genai.evaluate()`) and cannot be used in production monitoring. Use the `@scorer` decorator for production-ready scorers.^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer

class ResponseQualityScorer(Scorer):
    name: str = "response_quality"
    min_length: int = 50
    required_sections: list[str] = []

    def __call__(self, outputs: str) -> Feedback:
        # evaluation logic
        return Feedback(value=True, rationale="All criteria met")
```

## Scorer Inputs and Outputs

A scorer function can accept any combination of the following named parameters:
- `trace: Trace` – the full [[MLflow Trace]] object, including spans, timings, and attributes.
- `inputs: dict` – the input data passed during evaluation.
- `outputs: str` – the predicted output text.
- `expectations: dict` – ground-truth values provided in the evaluation dataset.

The return type can be a primitive Python type (`int`, `float`, `bool`, `str`), a single `Feedback`, or a `list[Feedback]`. When returning multiple `Feedback` objects, each must have a unique `name`.^[code-based-scorer-examples-databricks-on-aws.md]

## Using Trace Data in Scorers

The `trace` parameter gives access to spans, their timing, and attributes. For example, you can check whether an LLM call’s response time is within an acceptable range by inspecting the start and end times of a `CHAT_MODEL` span.^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def llm_response_time_good(trace: Trace) -> Feedback:
    llm_span = trace.search_spans(span_type=SpanType.CHAT_MODEL)[0]
    response_time = (llm_span.end_time_ns - llm_span.start_time_ns) / 1e9
    # ... evaluate threshold
```

## Wrapping Predefined LLM Judges

You can wrap built-in [judges](/concepts/llm-judges.md) (like `is_context_relevant`) inside a code-based scorer to preprocess data or post-process results. This is useful when your app’s input format differs from what the judge expects.^[code-based-scorer-examples-databricks-on-aws.md]

## Using Expectations (Ground Truth)

Expectations are provided in the evaluation dataset as an `expectations` column or field. A code-based scorer can access them via the `expectations` parameter. This enables exact-match checking, keyword presence validation, or any custom comparison against ground truth. If the same scorer is intended for production monitoring (where expectations are unavailable), design it to handle the absence of expectations gracefully.^[code-based-scorer-examples-databricks-on-aws.md]

## Returning Multiple Feedback Objects

A single scorer can return a list of `Feedback` objects to assess multiple dimensions (e.g., emptiness check and character length) in one pass. Each `Feedback` must have a distinct `name`; that name becomes the metric column name in the evaluation results.^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def comprehensive_response_checker(outputs: str) -> list[Feedback]:
    return [
        Feedback(name="is_not_empty_check", value="yes" if outputs else "no"),
        Feedback(name="response_char_length", value=len(outputs)),
    ]
```

## Integrating a Custom LLM Judge

Code-based scorers can call any LLM (e.g., via OpenAI SDK) to perform semantic assessment. The scorer handles API calls, input formatting, and parses the LLM’s structured output (e.g., JSON) into a `Feedback` object. Setting the `source` field of `Feedback` to `AssessmentSource(source_type=AssessmentSourceType.LLM_JUDGE, ...)` attributes the assessment to the external judge.^[code-based-scorer-examples-databricks-on-aws.md]

## Error Handling

MLflow surfaces scorer errors gracefully. Two approaches are available:
- Return a `Feedback` with an `AssessmentError` object (error code and message) for expected failures.
- Raise an exception to let MLflow handle the error internally and continue evaluation of other scorers.

Uses the `AssessmentError` class from `mlflow.entities`.^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions

Metric names are derived as follows:
- **Primitive or unnamed `Feedback` return**: The function name (for `@scorer`) or the `name` field of the class (for `Scorer` subclass).
- **Single `Feedback` with explicit name**: The `Feedback.name` is used.
- **Multiple `Feedback` objects**: Each `Feedback.name` becomes a separate metric column; they must be unique. The class/function name is ignored for multiple returns.

See [custom scorer reference](/concepts/custom-scorers-mlflow-genai.md) for full details.^[code-based-scorer-examples-databricks-on-aws.md]

## Chaining Evaluations

After an initial evaluation (e.g., with the built-in `Safety` scorer), you can filter traces that failed a check and re-evaluate with different scorers or an updated app. Use `mlflow.search_traces()` to retrieve the subset of problematic traces for iterative refinement.^[code-based-scorer-examples-databricks-on-aws.md]

## Conditional Logic with Guidelines

You can wrap the [Guidelines judge](/concepts/guidelines-llm-judge.md) inside a code-based scorer to apply different judgment criteria based on user attributes (e.g., user tier). The scorer extracts context from `inputs` and instantiates a `Guidelines` judge with appropriate rules, returning its feedback.^[code-based-scorer-examples-databricks-on-aws.md]

## Production Monitoring Support

Code-based scorers defined with the `@scorer` decorator can be registered for [Production Monitoring](/concepts/production-monitoring.md) on live traffic. Class-based scorers are not supported in production. When designing scorers for online use, avoid relying on expectations (which are typically unavailable) and handle missing data gracefully.^[code-based-scorer-examples-databricks-on-aws.md]

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
