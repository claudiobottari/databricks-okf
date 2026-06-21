---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac24bfd10cc2356a3fcc67ff2e902213955f64f2008351a07bb7785cafb201c3
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-feedback-object
    - MFO
    - Feedback (MLflow)|Feedback
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: MLflow Feedback Object
description: The structured output returned by MLflow LLM judges containing a 'value' field ('yes' or 'no') indicating relevance and a 'rationale' field explaining the reasoning for the assessment.
tags:
  - mlflow
  - llm-evaluation
  - output-format
timestamp: "2026-06-19T17:34:00.869Z"
---

# MLflow Feedback Object

The **MLflow `Feedback` object** (in `mlflow.entities`) represents a single evaluation assessment produced by a [Custom code-based scorers|custom scorer](/concepts/custom-code-based-scorers-mlflow-genai.md) during [MLflow Evaluation for GenAI|GenAI evaluation](/concepts/mlflow-genai-evaluation.md). It encapsulates the evaluation result, an optional rationale, error information, and metadata such as the source of the assessment. Custom code-based scorers return `Feedback` objects (or lists of them) to communicate structured evaluation outcomes to the MLflow evaluation framework. ^[code-based-scorer-examples-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md]

## Properties

A `Feedback` object carries the following fields: ^[code-based-scorer-examples-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md]

| Field | Type | Description |
|-------|------|-------------|
| `name` | `str` (optional) | The metric name for the assessment. If omitted, the scorer function name is used. When returning multiple `Feedback` objects, each must have a unique `name`. |
| `value` | `bool`, `int`, `float`, `str`, or `None` | The evaluation outcome. Common patterns: `"yes"`/`"no"` for binary judgments, integer scores (e.g., 1–5), numeric metrics (e.g., character count). |
| `rationale` | `str` (optional) | A human-readable explanation of the assessment. |
| `error` | `AssessmentError` (optional) | An error object indicating that the assessment could not be computed. See [Error handling in scorers](/concepts/error-handling-in-scorers.md). |
| `source` | `AssessmentSource` (optional) | Metadata about the assessment origin, containing `source_type` (an `AssessmentSourceType` enum) and `source_id` (a string identifier for the judge model or tool). |
| `metadata` | `dict` (optional) | Additional key-value metadata (e.g., annotator email). |

## Using `Feedback` in a custom scorer

Custom scorers defined with the `@scorer` decorator or the `Scorer` base class must return either a single `Feedback` object, a primitive value (which MLflow wraps into a `Feedback`), or a list of `Feedback` objects. The choice affects how the metric is named and presented in results. ^[code-based-scorer-examples-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md]

### Single `Feedback` without explicit name

When a scorer returns a `Feedback` object with no `name` set, MLflow uses the scorer function name as the metric name. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def response_quality(outputs: str) -> Feedback:
    return Feedback(value=True, rationale="Response is complete")
```

The metric appears as `response_quality` in evaluation results.

### Single `Feedback` with explicit name

If the `Feedback` object includes a `name`, that name overrides the function name for the metric. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def custom_check(outputs: str) -> Feedback:
    return Feedback(name="custom_metric_name", value=0.9, rationale="Clarity score")
```

The metric is stored under `custom_metric_name`.

### Multiple `Feedback` objects

A scorer can return a list of `Feedback` objects. Each object must have a unique `name`; these names become separate metric columns in the evaluation output. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def comprehensive_check(outputs: str) -> list[Feedback]:
    return [
        Feedback(name="not_empty", value="yes" if outputs else "no"),
        Feedback(name="char_length", value=len(outputs)),
    ]
```

### Specifying the assessment source

The `source` field enables trackability of which judge or tool produced the feedback. Set it to an `AssessmentSource` instance with a `source_type` (an `AssessmentSourceType` enum value such as `LLM_JUDGE`) and a `source_id` string (e.g., the model name). ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentSource, AssessmentSourceType, Feedback

@scorer
def llm_judge_score(inputs, outputs) -> Feedback:
    return Feedback(
        value=parsed_score,
        rationale=parsed_rationale,
        source=AssessmentSource(
            source_type=AssessmentSourceType.LLM_JUDGE,
            source_id="claude-sonnet-4-5",
        )
    )
```

In the MLflow UI, the source information is visible when inspecting the assessment. Users can also edit the score later; the original assessment is superseded and the edit history is preserved. ^[code-based-scorer-examples-databricks-on-aws.md]

## Error handling

When a scorer cannot produce a valid assessment, it can include an `AssessmentError` in the `Feedback` object's `error` field instead of raising an exception. The evaluation framework continues processing other scorers and records the error. ^[code-based-scorer-examples-databricks-on-aws.md, code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentError, Feedback

@scorer
def safe_check(outputs) -> Feedback:
    try:
        if not outputs:
            return Feedback(
                value=None,
                error=AssessmentError(
                    error_code="MISSING_OUTPUT",
                    error_message="No output provided"
                )
            )
        return Feedback(value=True, rationale="Valid")
    except Exception:
        raise  # Let MLflow handle unexpected errors gracefully
```

Alternatively, let exceptions propagate naturally — MLflow automatically captures the exception and creates a `Feedback` with `value=None` and an `error` containing the exception details. ^[code-based-scorer-reference-databricks-on-aws.md]

## Interaction with pre‑existing traces

When evaluating pre‑generated traces (obtained via `mlflow.search_traces()`), the `Feedback` objects returned by scorers are attached to those traces as assessments. The evaluation results include all feedback columns alongside the original trace data. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) – How to define and register scorers that return `Feedback`
- MLflow Evaluation for GenAI – The overall evaluation framework
- [[MLflow Trace]] – The object representing a GenAI execution, to which feedback assessments are attached
- [AssessmentSource](/concepts/assessmentsource-entity.md) – Metadata class for identifying the source of an assessment
- AssessmentError – Error representation for failed assessments
- Code-based scorer reference – API details for the `@scorer` decorator and `Scorer` class

## Sources

- code-based-scorer-examples-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
