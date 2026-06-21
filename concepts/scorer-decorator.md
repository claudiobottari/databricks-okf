---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6b4675349d0087e4db5c3fac1b924c047af347e0494f3f5fe0f314732499f8eb
  pageDirectory: concepts
  sources:
    - code-based-scorer-reference-databricks-on-aws.md
    - code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - scorer-decorator
  citations:
    - file: code-based-scorer-reference-databricks-on-aws.md
    - file: code-based-scorers-databricks-on-aws.md
title: "@scorer decorator"
description: The primary way to define custom code-based scorers for MLflow GenAI evaluation, using a decorator-based function signature with keyword-only arguments.
tags:
  - mlflow
  - scoring
  - evaluation
timestamp: "2026-06-19T17:44:25.094Z"
---

# `@scorer` decorator

The **`@scorer` decorator** is the primary decorator-based API for defining custom code-based scorers for evaluating and monitoring generative AI applications in MLflow. It transforms a Python function into a scoring function that can assess the quality, safety, or other characteristics of model inputs and outputs. ^[code-based-scorer-reference-databricks-on-aws.md]

Most code-based scorers should be defined using the `@scorer` decorator rather than the equivalent [Scorer class](/concepts/scorer-class.md) because it requires less boilerplate and is simpler to use. For cases where internal state or additional customization is needed, the `Scorer` class can be used instead. ^[code-based-scorer-reference-databricks-on-aws.md]

## Signature

Scorers defined with the `@scorer` decorator accept all arguments as keyword-only parameters. All input arguments are optional, so you declare only what your scorer needs: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer
from typing import Optional, Any
from mlflow.entities import Feedback

@scorer
def my_custom_scorer(
    *,
    inputs: Optional[dict[str, Any]],       # App's raw input
    outputs: Optional[Any],                 # App's raw output
    expectations: Optional[dict[str, Any]], # Ground truth or labels
    trace: Optional[mlflow.entities.Trace]  # Complete trace with all spans
) -> Union[int, float, bool, str, Feedback, List[Feedback]]:
    # Your evaluation logic here
```

Scorers receive the complete [[MLflow trace]] containing all spans, attributes, and outputs. MLflow also extracts commonly needed data and passes it as the named arguments shown above. ^[code-based-scorer-reference-databricks-on-aws.md]

## Inputs

The `@scorer` decorator provides the following optional input arguments: ^[code-based-scorer-reference-databricks-on-aws.md]

- **`inputs`**: The request sent to your app (for example, user query, context).
- **`outputs`**: The response from your app (for example, generated text, tool calls).
- **`expectations`**: Ground truth or labels (for example, expected response, guidelines).
- **`trace`**: The complete MLflow trace including all spans, allowing analysis of intermediate steps, latency, tool usage, and more. The trace is passed as an instantiated `mlflow.entities.Trace` class.

When running `mlflow.genai.evaluate()`, the `inputs`, `outputs`, and `expectations` parameters can be specified in the `data` argument, or parsed from the trace. ^[code-based-scorer-reference-databricks-on-aws.md]

For [Production Monitoring](/concepts/production-monitoring.md), registered scorers always parse the `inputs` and `outputs` parameters from the trace. The `expectations` parameter is not available in production monitoring. ^[code-based-scorer-reference-databricks-on-aws.md]

## Output types

Scorers can return either simple values or rich [Feedback](/concepts/feedback-object.md) objects. ^[code-based-scorer-reference-databricks-on-aws.md]

### Simple values

Simple return types (`int`, `float`, `bool`, or `str`) are used for straightforward pass/fail or numeric assessments: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def response_length(outputs: str) -> int:
    return len(outputs.split())

@scorer
def contains_citation(outputs: str) -> str:
    return "yes" if "[source]" in outputs else "no"
```

### Rich Feedback objects

Return a `Feedback` object or list of `Feedback` objects for detailed assessments with scores, rationales, and metadata: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import Feedback, AssessmentSource

@scorer
def content_quality(outputs):
    return Feedback(
        value=0.85,
        rationale="Clear and accurate, minor grammar issues",
        source=AssessmentSource(
            source_type="HUMAN",
            source_id="grammar_checker_v1"
        ),
        metadata={
            "annotator": "me@example.com"
        },
    )
```

Multiple feedback objects can be returned as a list. Each feedback should have the `name` field specified, and those names appear as separate metrics in the evaluation results: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def comprehensive_check(inputs, outputs):
    return [
        Feedback(name="relevance", value=True, rationale="Directly addresses query"),
        Feedback(name="tone", value="professional", rationale="Appropriate for audience"),
        Feedback(name="length", value=150, rationale="Word count within limits")
    ]
```

## Metric naming behavior

When using the `@scorer` decorator, metric names in evaluation runs follow these rules: ^[code-based-scorer-reference-databricks-on-aws.md]

1. If the scorer returns one or more `Feedback` objects, `Feedback.name` fields take precedence when specified.
2. For primitive return values or unnamed `Feedback` objects, the function name is used.

All metrics must have distinct names. If a scorer returns `List[Feedback]`, each `Feedback` in the list must have a distinct name. ^[code-based-scorer-reference-databricks-on-aws.md]

## Accessing secrets

Custom scorers can access [Databricks secrets](/concepts/databricks-secret-scopes.md) to securely use API keys and credentials, which is useful for integrating external services like Azure OpenAI or AWS Bedrock. By default, `dbutils` is not available in the scorer runtime environment, so you must import it from within the scorer function: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
@scorer
def custom_llm_scorer(trace: Trace) -> Feedback:
    from databricks.sdk.runtime import dbutils
    api_key = dbutils.secrets.get(scope='my-scope', key='api-key')
    # Use API key to call custom LLM endpoint
    return Feedback(
        value="yes",
        rationale="Evaluation completed using custom endpoint"
    )
```

This approach works for both development evaluation and production monitoring. ^[code-based-scorer-reference-databricks-on-aws.md]

## Error handling

When a scorer encounters an error for a trace, MLflow captures error details for that trace and continues execution gracefully. MLflow provides two approaches: ^[code-based-scorer-reference-databricks-on-aws.md]

### Let exceptions propagate (recommended)

The simplest approach is to let exceptions throw naturally. MLflow automatically captures the exception and creates a `Feedback` object with `value=None` and `error` containing the exception details, error message, and stack trace. The error information is displayed in the evaluation results. ^[code-based-scorer-reference-databricks-on-aws.md]

### Handle exceptions explicitly

For custom error handling, catch exceptions and return a `Feedback` with `None` value and error details: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentError, Feedback

@scorer
def is_valid_response(outputs):
    import json
    try:
        data = json.loads(outputs)
        return Feedback(value=True, rationale="Valid JSON")
    except json.JSONDecodeError as e:
        return Feedback(error=e)
```

The `error` parameter accepts Python exception objects directly or structured `AssessmentError` objects for structured error reporting with error codes. ^[code-based-scorer-reference-databricks-on-aws.md]

## Registration and production monitoring

Scorers defined with the `@scorer` decorator must be registered and started to be used in production monitoring: ^[code-based-scorer-reference-databricks-on-aws.md]

```python
custom_llm_scorer.register()
custom_llm_scorer.start(sampling_config=ScorerSamplingConfig(sample_rate=1))
```

`@scorer`-decorated functions used in production monitoring must be defined and registered from a **Databricks notebook**. The monitoring service serializes the function code for remote execution, and this serialization requires the notebook environment. ^[code-based-scorers-databricks-on-aws.md]

Production monitoring supports built-in LLM judges and `@scorer`-decorated functions. Class-based `Scorer` subclasses are **not supported** for production monitoring. If you need stateful scorers in production, use the `@scorer` decorator and manage state inside the function body. ^[code-based-scorers-databricks-on-aws.md]

## When to use the `Scorer` class instead

For most cases, the `@scorer` decorator is recommended. If your logic requires internal state or additional customization, use the [Scorer class](/concepts/scorer-class.md) base class instead. However, scorers defined using the `Scorer` class are not supported for production monitoring. ^[code-based-scorer-reference-databricks-on-aws.md, code-based-scorers-databricks-on-aws.md]

The `Scorer` class is a Pydantic object, so you can define additional fields and use them in the `__call__` method. When using the class, pay attention to state management: use instance attributes rather than mutable class attributes to avoid sharing state across instances. ^[code-based-scorer-reference-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) — Overview of the scoring system for AI evaluation
- [Scorer class](/concepts/scorer-class.md) — Alternative class-based approach for scorers with internal state
- [[MLflow trace]] — The complete execution trace passed to scorers
- [Feedback](/concepts/feedback-object.md) — The rich feedback object for detailed assessments
- [MLflow genai evaluate](/concepts/mlflow-genai-evaluation.md) — The evaluation function that uses scorers
- [AssessmentSource](/concepts/assessmentsource-entity.md) — Source metadata for feedback assessments
- AssessmentError — Structured error reporting for feedback
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring

## Sources

- code-based-scorer-reference-databricks-on-aws.md
- code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
2. [code-based-scorers-databricks-on-aws.md](/references/code-based-scorers-databricks-on-aws-2a1f1dbe.md)
