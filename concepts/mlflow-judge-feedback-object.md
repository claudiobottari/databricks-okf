---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80228f817e92e1569f9b122e7347fa657c8717747b3fdbc2f9247102a5a3d7eb
  pageDirectory: concepts
  sources:
    - answer-and-context-relevance-judges-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-judge-feedback-object
    - MJFO
  citations:
    - file: answer-and-context-relevance-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Judge Feedback Object
description: The output schema returned by MLflow LLM judges containing a 'value' field ('yes' or 'no') indicating relevance and a 'rationale' field providing an explanation for the judge's decision.
tags:
  - mlflow
  - llm-evaluation
  - schema
  - output
timestamp: "2026-06-19T14:01:33.778Z"
---

```markdown
---
title: MLflow Judge Feedback Object
summary: The container returned by an MLflow judge, holding the judgment value and a rationale explaining the scoring decision.
sources:
  - answer-and-context-relevance-judges-databricks-on-aws.md
  - create-a-custom-judge-using-make_judge-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - mlflow
  - genai
  - evaluation
  - judges
aliases:
  - mlflow-judge-feedback-object
  - MJFO
confidence: 1.0
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow Judge Feedback Object

The **MLflow Judge Feedback Object** is the structured result returned by an MLflow LLM judge (either built‑in or custom) after evaluating a GenAI application’s output. It encapsulates the judge’s decision and the reasoning behind it, enabling developers to interpret and compare evaluation scores programmatically. ^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Structure

The feedback object contains two primary fields:

| Field | Type | Description |
|-------|------|-------------|
| `value` | depends on the judge | The judgment itself. For built‑in judges like [[RelevanceToQuery]] and [[RetrievalRelevance]], the value is a string (`"yes"` or `"no"`). Custom judges created with make_judge()|make_judge can return any type set in `feedback_value_type` (e.g., `bool`, `str`, or a custom enum). ^[answer-and-context-relevance-judges-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md] |
| `rationale` | `str` | A free‑text explanation of why the judge arrived at the given value. This is always a human‑readable string. ^[answer-and-context-relevance-judges-databricks-on-aws.md] |

## Usage

When a judge is invoked directly (e.g., calling a built‑in scorer instance on a single input) or passed to `mlflow.genai.evaluate()`, the result for each evaluation input is a feedback object. These objects are collected and can be aggregated to compute metrics across a dataset. ^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Direct invocation example

```python
from mlflow.genai.scorers import RelevanceToQuery

judge = RelevanceToQuery(name="my_relevance")
feedback = judge(
    inputs={"question": "What is the capital of France?"},
    outputs="The capital of France is Paris.",
)
print(feedback.value)      # "yes"
print(feedback.rationale)  # "The response directly answers the user's question."
```

^[answer-and-context-relevance-judges-databricks-on-aws.md]

### Custom judge example

When creating a custom judge with `make_judge`, the feedback value type is defined by the developer. For a boolean judge that checks tool‑call correctness:

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions="Analyze the execution {{ trace }} to determine if the agent called appropriate tools.",
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

The resulting feedback object for each evaluation sample will have `value` as either `True` or `False`, and a string `rationale`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Comparison across configurations

Because feedback objects from different evaluation runs share the same structure, they can be used to perform [[A/B Comparison of Agent Configurations]]. By running the same evaluation dataset against two agent variants with identical judges, you can compare the distributions of `value` fields to determine which configuration performs better. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [[RelevanceToQuery]] – A built‑in judge that returns a feedback object.
- [[RetrievalRelevance]] – A built‑in judge that returns a feedback object.
- [[Custom Judges]] – How to define your own judge that returns a feedback object.
- make_judge()|Make Judge API – The `make_judge()` function used to create custom judges.
- [[A/B Comparison of Agent Configurations]] – Using feedback objects to compare agent variants.
- [[MLflow Evaluation UI|MLflow Evaluation]] – The `mlflow.genai.evaluate()` API that collects feedback objects.

## Sources

- answer-and-context-relevance-judges-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md
```

# Citations

1. [answer-and-context-relevance-judges-databricks-on-aws.md](/references/answer-and-context-relevance-judges-databricks-on-aws-5f3620ab.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
