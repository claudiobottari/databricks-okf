---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a1dc8122217ee2ff04a755ada35f26613a0ecec5383712c996d3e1e630d37a78
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-llm-judge-feedback-object
    - MLJFO
  citations:
    - file: correctness-judge-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: MLflow LLM Judge Feedback Object
description: The structured return type from MLflow LLM judges containing a binary 'value' (yes/no) indicating correctness and a 'rationale' providing detailed explanation of which facts were supported or missing.
tags:
  - mlflow
  - llm-evaluation
  - api-design
timestamp: "2026-06-18T11:12:44.557Z"
---

# MLflow LLM Judge Feedback Object

The **MLflow LLM Judge Feedback Object** is the structured output returned by all built-in and custom [LLM Judges](/concepts/llm-judges.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) when evaluating a GenAI application's response. It encapsulates the judge's verdict and reasoning in a standardized format that can be used both in offline evaluation (via `mlflow.genai.evaluate()`) and in production monitoring (via registered scorers in the inference table pipeline).^[correctness-judge-databricks-on-aws.md]

## Structure

Every LLM judge returns a `Feedback` object with the following fields:

- **`value`**: A string representing the judge's verdict. For built-in judges like [Correctness Judge](/concepts/correctness-judge.md), this is typically `"yes"` if the response meets the evaluation criterion, or `"no"` if it does not.^[correctness-judge-databricks-on-aws.md]
- **`rationale`**: A detailed natural language explanation of the judge's reasoning. For a correctness judge, this includes which facts are supported or missing, providing transparency into the evaluation decision.^[correctness-judge-databricks-on-aws.md]

## Usage in Evaluation

The Feedback object is returned directly when you invoke a judge, and it is also the format that the evaluate API expects from each scorer in its results:^[correctness-judge-databricks-on-aws.md]

**Direct invocation:**

```python
from mlflow.genai.scorers import Correctness

correctness_judge = Correctness()
feedback = correctness_judge(
    inputs={"request": "What is MLflow?"},
    outputs={"response": "MLflow is the largest open source AI engineering platform for agents, LLMs, and ML models."},
    expectations={
        "expected_facts": [
            "MLflow is open-source",
            "MLflow is an AI engineering platform"
        ]
    }
)

print(feedback.value)     # "yes"
print(feedback.rationale) # Explanation of which facts are supported
```

^[correctness-judge-databricks-on-aws.md]

**In evaluation with `evaluate()`:**

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[Correctness()]
)
```

The Feedback objects produced by each scorer are collected and stored as part of the evaluation run's results.^[correctness-judge-databricks-on-aws.md]

## Custom Scorers and the Feedback Object

When defining a [code-based scorer](/concepts/code-based-scorers.md) or a custom judge, the function must return a `Feedback` object:^[code-based-scorer-reference-databricks-on-aws.md]

```python
from mlflow.entities import Trace, Feedback

@scorer
def custom_llm_scorer(trace: Trace) -> Feedback:
    # ... evaluation logic ...
    return Feedback(
        value="yes",
        rationale="Evaluation completed using custom endpoint"
    )
```

The `Feedback` type is imported from `mlflow.entities` and requires at least the `value` and `rationale` fields.^[code-based-scorer-reference-databricks-on-aws.md]

## Relation to the Scorer Class

The Feedback object is also the return type for the [Scorer class](/concepts/scorer-class.md) approach. Whether you use the `@scorer` decorator pattern or the class-based approach, the evaluation function must produce a `Feedback` object.^[code-based-scorer-reference-databricks-on-aws.md]

## Availability

The Feedback object is available in MLflow version 3.4.0 and above.^[correctness-judge-databricks-on-aws.md]

## Use in Production Monitoring

When a scorer is registered and started for [Production Monitoring](/concepts/production-monitoring.md), each time the scorer runs against an incoming trace in the inference table pipeline, it produces a `Feedback` object. These objects are then stored as part of the monitoring results, allowing teams to track evaluation outcomes over time.^[code-based-scorer-reference-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — Overview of built-in and custom evaluation judges
- [Correctness Judge](/concepts/correctness-judge.md) — A built-in judge that returns Feedback objects
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions that return Feedback objects
- [Scorer class](/concepts/scorer-class.md) — Alternative method for defining scorers
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API
- [Production Monitoring](/concepts/production-monitoring.md) — Using scorers in the inference table pipeline

## Sources

- correctness-judge-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
