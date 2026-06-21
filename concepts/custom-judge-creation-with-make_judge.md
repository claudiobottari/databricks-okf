---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 113bb38b8123b82939d9bcf2dc5bcc9dfb4d3fc9c6ea962def4e864a452b7793
  pageDirectory: concepts
  sources:
    - evaluate-conversations-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judge-creation-with-make_judge
    - CJCWM
    - custom judges created with `make_judge()`
    - Custom Judge Creation
    - custom-multi-turn-judges-with-make_judge
    - CMJWM
  citations:
    - file: evaluate-conversations-databricks-on-aws.md
title: Custom Judge Creation with make_judge
description: API for building custom multi-turn LLM judges using make_judge, with access to the full conversation history via the {{ conversation }} template variable.
tags:
  - mlflow
  - judges
  - customization
  - evaluation
timestamp: "2026-06-19T18:42:11.074Z"
---

# Custom Judge Creation with `make_judge`

**Custom Judge Creation with `make_judge`** refers to the process of building bespoke LLM-as-judge evaluators using the `mlflow.genai.judges.make_judge` function. This function allows you to define custom grading criteria, feedback types, and template variables for both single-turn and multi-turn evaluation scenarios. ^[evaluate-conversations-databricks-on-aws.md]

## Overview

`make_judge` is a factory function that accepts a set of instructions (the "prompt" for the judge LLM) and a structured output type, returning a callable scorer object. This scorer can then be passed to `mlflow.genai.evaluate()` to automatically grade model responses or entire conversations. ^[evaluate-conversations-databricks-on-aws.md]

The primary use case described in the source material is for [Multi-turn Judges](/concepts/multi-turn-judge.md)—evaluating whole conversation sessions rather than individual turns. The function is flexible enough to create judges for any custom criterion that an LLM can assess. ^[evaluate-conversations-databricks-on-aws.md]

## Parameters

`make_judge` takes at least three arguments:

| Parameter | Description |
|-----------|-------------|
| `name` | A human-readable string identifier for the judge (e.g., `"politeness"`). |
| `instructions` | A string containing the grading rubric and template variables. The instructions tell the LLM judge what to evaluate and how to format its response. |
| `feedback_value_type` | A type annotation that defines the set of allowed output values. Typically expressed using `typing.Literal` (e.g., `Literal["consistently_polite", "mostly_polite", "impolite"]`). The judge LLM must return one of these exact values. |

All three parameters are required. ^[evaluate-conversations-databricks-on-aws.md]

## Template Variables

Inside the `instructions` string, you can use template variables that will be replaced at evaluation time with the actual data.

- **`{{ conversation }}`** – Injects the full conversation history in a readable format. This variable is designed for multi-turn evaluation and can *only* be used together with `{{ expectations }}`. It cannot be used with `{{ inputs }}`, `{{ outputs }}`, or `{{ trace }}`. ^[evaluate-conversations-databricks-on-aws.md]
- **`{{ expectations }}`** – (Available but not shown in the example) Can be combined with `{{ conversation }}` to provide reference answers or expected behavior. ^[evaluate-conversations-databricks-on-aws.md]

> **Note**: The `{{ conversation }}` variable is specifically for multi-turn contexts. For single-turn judges, use `{{ inputs }}` and `{{ outputs }}` as documented in the MLflow predefined scorers reference. ^[evaluate-conversations-databricks-on-aws.md]

## Multi-turn Example

The following example creates a custom multi-turn judge that evaluates whether an assistant maintained a polite tone throughout a conversation:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

politeness_judge = make_judge(
    name="politeness",
    instructions=(
        "Evaluate whether the assistant maintained a polite and professional "
        "tone throughout this conversation:\n\n{{ conversation }}\n\n"
        "Rate as 'consistently_polite', 'mostly_polite', or 'impolite'."
    ),
    feedback_value_type=Literal["consistently_polite", "mostly_polite", "impolite"],
)
```

Once created, the judge can be used with pre‑recorded conversation traces:

```python
traces = mlflow.search_traces(
    filter_string="attributes.status = 'OK'",
    return_type="list",
)

results = mlflow.genai.evaluate(
    data=traces,
    scorers=[politeness_judge],
)
```

^[evaluate-conversations-databricks-on-aws.md]

## Integration with Evaluation

The resulting judge object behaves like any other MLflow scorer. It can be passed inside a list to the `scorers` parameter of `mlflow.genai.evaluate()`. For multi-turn evaluation, MLflow automatically groups traces by session ID (tagged with `mlflow.trace.session`) before invoking the judge. ^[evaluate-conversations-databricks-on-aws.md]

The assessment is stored on the first trace (chronologically) in each conversation session, along with a `session_id` metadata field. This design keeps the evaluation stable even when new turns are added later. ^[evaluate-conversations-databricks-on-aws.md]

## Related Concepts

- [Multi-turn Judges](/concepts/multi-turn-judge.md) – Built‑in and custom judges for conversation‑level evaluation.
- MLflow evaluate – The main evaluation API that consumes custom judges.
- [LLM Judges](/concepts/llm-judges.md) – The general concept of using an LLM as an evaluator.
- [Conversation Evaluation](/concepts/conversation-evaluation.md) – Overview of evaluating multi‑turn sessions.
- [Predefined scorers](/concepts/mlflow-genai-predefined-scorers.md) – Ready‑to‑use judges that require no custom code.

## Sources

- evaluate-conversations-databricks-on-aws.md

# Citations

1. [evaluate-conversations-databricks-on-aws.md](/references/evaluate-conversations-databricks-on-aws-f530405b.md)
