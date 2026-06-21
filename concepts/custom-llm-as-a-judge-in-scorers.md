---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 644e432718d89f4349fa10f4b6f7e7b4ca902b146f62f3edd83c0db5ffa36ddb
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-as-a-judge-in-scorers
    - CLIS
    - Custom LLM-as-a-Judge Scorers
    - custom LLM-as-a-judge scorers
    - built-in and custom LLM judges and scorers
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Custom LLM-as-a-Judge in scorers
description: Integrating a custom or externally hosted LLM within a scorer to evaluate response quality, with full control over prompts, model selection, and feedback generation.
tags:
  - mlflow
  - llm-as-judge
  - scorers
  - genai
timestamp: "2026-06-18T14:36:38.413Z"
---

# Custom LLM-as-a-Judge in Scorers

**Custom LLM-as-a-Judge in Scorers** refers to the practice of using a large language model (LLM) to evaluate the outputs of another AI system within the MLflow Evaluation for GenAI framework. These custom judges are implemented as [Code-based Scorers](/concepts/code-based-scorers.md) that call an LLM – either a built-in Databricks judge, a third-party model, or a self-hosted model – and return structured feedback (e.g., a score, boolean, or rationale). This approach provides flexible, semantic evaluation that goes beyond simple rule-based metrics.

## Overview

A custom LLM-as-a-judge scorer is a Python function decorated with `@scorer` (or a class inheriting from `Scorer`) that takes one or more of the standard arguments – `inputs`, `outputs`, `trace`, `expectations` – and returns a primitive value (e.g., `int`, `bool`, `str`) or a `Feedback` object. The function uses an LLM to analyze the response and produce a judgement. The LLM can be any model accessible via the OpenAI client or the Databricks foundation model APIs. ^[code-based-scorer-examples-databricks-on-aws.md]

## Approaches for Creating Custom LLM Judges

### Wrapping a Predefined LLM Judge

Use MLflow's [Built-in LLM Judges](/concepts/built-in-llm-judges.md) (e.g., `is_context_relevant`) inside a custom scorer to preprocess trace data or post-process the judge’s feedback. This method reuses existing, tested judges while adapting their inputs to the structure of your application.

**Example:** Extract the last user message from the `inputs` dictionary and pass it to `is_context_relevant` alongside the response as context. The scorer returns a `Feedback` object. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def is_message_relevant(inputs: dict, outputs: str) -> Feedback:
    # extract last user message from inputs
    ...
    return is_context_relevant(request=last_user_message, context={"response": outputs})
```

### Calling Your Own LLM Judge

Integrate any LLM (e.g., `databricks-claude-sonnet-4-5`, `gpt-4o-mini`) directly within the scorer. The scorer handles the API call, formats prompts, parses the LLM’s JSON response, and returns a `Feedback` object. You can set the `source` field to indicate the assessment was made by an LLM judge, preserving traceability. ^[code-based-scorer-examples-databricks-on-aws.md]

**Example:** A judge that scores response quality on a 1‑5 scale asks the LLM for a JSON object with `"score"` and `"rationale"` keys. The scorer parses this and returns a `Feedback` with the numeric value and rationale. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def answer_quality(inputs: dict, outputs: str) -> Feedback:
    # build prompts and call LLM
    response = client.chat.completions.create(...)
    result = json.loads(response.choices[0].message.content)
    return Feedback(value=result["score"], rationale=result["rationale"],
                    source=AssessmentSource(source_type=AssessmentSourceType.LLM_JUDGE, source_id="claude-sonnet-4-5"))
```

### Using Guidelines Judges with Conditional Logic

The [Guidelines judge](/concepts/guidelines-llm-judge.md) can be wrapped inside a custom scorer to apply different evaluation criteria based on context (e.g., user tier, request type). The custom scorer selects a set of guidelines and calls the `Guidelines` scorer programmatically, returning its `Feedback`. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def premium_service_validator(inputs, outputs, trace=None):
    if inputs.get("user_tier") == "premium":
        judge = Guidelines(name="premium_experience", guidelines=[...])
    else:
        judge = Guidelines(name="standard_experience", guidelines=[...])
    return judge(inputs=inputs, outputs=outputs)
```

## Error Handling

Custom LLM judges can include try/except blocks to handle API failures or malformed responses. The `Feedback` object supports an `error` field via `AssessmentError` for graceful degradation. Alternatively, letting the exception propagate causes MLflow to mark that scorer as failed for that row while continuing evaluation of other scorers. ^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions

- For a `@scorer` function returning a single primitive or unnamed `Feedback`, the function name becomes the metric name.
- If the `Feedback` has an explicit `name`, that name is used.
- For multiple `Feedback` objects returned by a single scorer, each must have a unique `name`. ^[code-based-scorer-examples-databricks-on-aws.md]

The metric names appear as columns in evaluation results and in the MLflow UI.

## Related Concepts

- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – Predefined judges such as `is_context_relevant`, `Safety`, and `Guidelines` that can be used inside custom scorers.
- [Code-based Scorers](/concepts/code-based-scorers.md) – The general mechanism for defining custom evaluation logic in MLflow.
- [Trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using the full execution trace to evaluate tool calls and intermediate steps.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying custom LLM judges to continuously monitor live traffic.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing agent variants using the same set of custom judges.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
