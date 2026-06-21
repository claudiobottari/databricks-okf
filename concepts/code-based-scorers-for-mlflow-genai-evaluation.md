---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a35a4450f1ce45870afd066c6292b410caabfb607d91c7448395853c63a02e0d
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-based-scorers-for-mlflow-genai-evaluation
    - CSFMGE
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Code-based Scorers for MLflow GenAI Evaluation
description: Custom Python functions decorated with @scorer that define flexible evaluation metrics for AI agents and applications in MLflow Evaluation for GenAI.
tags:
  - mlflow
  - evaluation
  - genai
  - scorers
timestamp: "2026-06-19T10:12:52.209Z"
---

Here is the wiki page for "Code-based Scorers for MLflow GenAI Evaluation".

---

# Code-based Scorers for MLflow GenAI Evaluation

**Code-based scorers** are custom evaluation metrics written in Python for use with `mlflow.genai.evaluate()`. They allow you to define arbitrary, fine-grained quality checks for your AI agent or application – going beyond the built-in LLM judges. A scorer is a function or class that receives evaluation data (inputs, outputs, traces, expectations) and returns a scalar value or structured feedback.^[code-based-scorer-examples-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]

## How scorers are used in evaluation

During `mlflow.genai.evaluate()`, each scorer is called once per evaluation record. The scorer can inspect the raw `inputs`, the generated `outputs`, the full [[MLflow Trace]] object, and any `expectations` (ground truth) provided in the evaluation dataset. The scorer returns a numeric or boolean result, an `AssessmentError`, or a `Feedback` object (or a list of `Feedback` objects).^[develop-code-based-scorers-databricks-on-aws.md, code-based-scorer-examples-databricks-on-aws.md]

## Defining a code-based scorer

There are two ways to define a code-based scorer:

### Using the `@scorer` decorator

The simplest approach. Decorate a function with `@mlflow.genai.scorers.scorer`. The function can accept any subset of the following keyword arguments: `inputs`, `outputs`, `trace`, `expectations`. It must return a primitive (`int`, `float`, `bool`, `str`), a `Feedback` object, a list of `Feedback` objects, or raise an exception.^[code-based-scorer-examples-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def response_length(outputs: str) -> int:
    return len(outputs)
```

### Using the `Scorer` base class (stateful, offline only)

For scorers that need configuration or state (e.g., parameters like `min_length`), subclass `mlflow.genai.scorers.Scorer`. The class extends Pydantic and requires a `name` field. Implement the `__call__` method. Class-based scorers are **only supported for offline evaluation**; they cannot be used in [Production Monitoring](/concepts/production-monitoring.md).^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback
from typing import Optional

class QualityScorer(Scorer):
    name: str = "quality"
    min_length: int = 50

    def __call__(self, outputs: str) -> Feedback:
        if len(outputs.split()) < self.min_length:
            return Feedback(value=False, rationale="Too short")
        return Feedback(value=True, rationale="Meets criteria")
```

## Inputs to a scorer

| Parameter | Type | Description |
|-----------|------|-------------|
| `inputs` | `dict` | The original evaluation data for the record (e.g., `{"messages": [...]}`). ^[code-based-scorer-examples-databricks-on-aws.md] |
| `outputs` | `str` | The generated output from the application (or from the stored trace). ^[code-based-scorer-examples-databricks-on-aws.md] |
| `trace` | `mlflow.entities.Trace` | The full trace object, granting access to spans, timing, attributes, etc. ^[code-based-scorer-examples-databricks-on-aws.md] |
| `expectations` | `dict` | Ground truth data provided in the evaluation dataset (common for offline evaluation). ^[code-based-scorer-examples-databricks-on-aws.md] |

A scorer can accept any combination of these parameters by name.^[develop-code-based-scorers-databricks-on-aws.md, code-based-scorer-examples-databricks-on-aws.md]

## Return types and metric naming

- **Primitive value (int, float, bool, str)** – The metric name is the function (or class) name.
- **Single `Feedback` without a `name`** – The metric name is the function/class name.
- **Single `Feedback` with a `name`** – The `Feedback.name` becomes the metric name.
- **List of `Feedback` objects** – Each must have a unique `name`; those names become separate metrics.^[code-based-scorer-examples-databricks-on-aws.md]

## Error handling

Scorer errors can be handled in two ways:

1. **Return `Feedback` with an `AssessmentError`** – This marks the result as erroneous without halting evaluation.
2. **Raise an exception** – MLflow catches the exception gracefully, marking the metric as failed, and continues evaluating other scorers.^[code-based-scorer-examples-databricks-on-aws.md]

## Development workflow (fast iteration)

To avoid re-running the application every time you tweak a scorer, use the recommended four-step workflow:^[develop-code-based-scorers-databricks-on-aws.md]

1. **Define evaluation data** – Create a list of records with `inputs` (and optionally `expectations`).
2. **Generate traces from your app** – Run `mlflow.genai.evaluate()` with a placeholder scorer (returns a constant) to produce traces.
3. **Query and store traces** – Use `mlflow.search_traces(run_id=eval_results.run_id)` to get a Pandas DataFrame of traces.
4. **Iterate on the scorer** – Call `mlflow.genai.evaluate(data=traces_df, scorers=[my_scorer])` **without `predict_fn`**. This runs the scorer on the precomputed traces instantly.

## Common patterns

- **Access trace details** – Inspect span timing, content, or attributes using the `trace` parameter.^[code-based-scorer-examples-databricks-on-aws.md]
- **Wrap a built-in LLM judge** – Call a predefined judge like `is_context_relevant` from inside a custom scorer, optionally preprocessing inputs.^[code-based-scorer-examples-databricks-on-aws.md]
- **Use expectations** – Check exact match or keyword presence against ground truth.^[code-based-scorer-examples-databricks-on-aws.md]
- **Return multiple feedback objects** – Have one scorer produce several named metrics (e.g., `is_not_empty` and `response_length`).^[code-based-scorer-examples-databricks-on-aws.md]
- **Use your own LLM as a judge** – Make an API call to a custom or third-party LLM within the scorer. Set the `source` field on `Feedback` to tag the assessment as LLM-judged.^[code-based-scorer-examples-databricks-on-aws.md]
- **Conditional guidelines** – Use different [Guidelines judges](/concepts/guidelines-llm-judges.md) based on user attributes such as `user_tier`.^[code-based-scorer-examples-databricks-on-aws.md]
- **Chain evaluations** – Filter traces that failed a safety check and re-evaluate them with a more focused scorer.^[code-based-scorer-examples-databricks-on-aws.md]

## Limitations

Class-based `Scorer` subclasses are not supported in [Production Monitoring](/concepts/production-monitoring.md); only `@scorer`-decorated functions can be deployed for continuous evaluation.^[code-based-scorer-examples-databricks-on-aws.md]

## Related concepts

- MLflow Evaluation for GenAI
- [@scorer decorator](/concepts/scorer-decorator.md)
- [Feedback Object](/concepts/feedback-object.md)
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Guidelines judges](/concepts/guidelines-llm-judges.md)
- Production monitoring with MLflow

## Sources

- code-based-scorer-examples-databricks-on-aws.md
- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
2. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
