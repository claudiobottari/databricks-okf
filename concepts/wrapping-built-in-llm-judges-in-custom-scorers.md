---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 88ae34990f49e461581657e6185c1f45fa9d97be7c039453219f335ad9f1d7c4
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - wrapping-built-in-llm-judges-in-custom-scorers
    - WBLJICS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Wrapping built-in LLM judges in custom scorers
description: Technique of wrapping MLflow's predefined LLM judges (like is_context_relevant) inside a custom code-based scorer to preprocess trace data or post-process judge feedback before returning results.
tags:
  - mlflow
  - judges
  - scorers
  - evaluation
timestamp: "2026-06-19T17:44:50.054Z"
---

# Wrapping Built-in LLM Judges in Custom Scorers

**Wrapping built-in LLM judges in custom scorers** refers to the pattern of creating a custom [Code-based Scorer](/concepts/code-based-scorers.md) that invokes an MLflow built-in [LLM Judge](/concepts/llm-judges.md) and then optionally preprocesses or post-processes the judge's evaluation. This technique allows developers to adapt predefined evaluation metrics—such as relevance, safety, or guidelines checks—to the specific input/output structure of their own GenAI applications.

## Motivation

MLflow provides a set of [Built-in LLM Judges](/concepts/built-in-llm-judges.md) (e.g., `is_context_relevant`, `Safety`, `Guidelines`) that return a [Feedback](/concepts/feedback-object.md) object. These judges are designed to work with a standard set of arguments (typically `request`, `context`, and `outputs`). When your application's data model differs from that standard format—for example, when the `inputs` field is a dictionary containing a `"messages"` list rather than a flat `"request"` string—you cannot pass the raw trace data directly to the built-in judge. Instead, you write a custom scorer that **wraps** the built-in judge, extracting and transforming the relevant fields before calling it. ^[code-based-scorer-examples-databricks-on-aws.md]

## General Pattern

A wrapper custom scorer is a function decorated with `@scorer` that:

1. Accepts the application's own input/output signature (e.g., `inputs: dict[str, Any]` and `outputs: str`).
2. Extracts the specific piece of data that the built-in judge expects (e.g., the last user message from the `"messages"` list).
3. Calls the built-in judge, passing the extracted data as its standard argument.
4. Returns the judge's [Feedback](/concepts/feedback-object.md) object (optionally modified) as the scorer's output.

The wrapper can also add Rationale or [AssessmentSource](/concepts/assessmentsource-entity.md) metadata to the feedback before returning it. ^[code-based-scorer-examples-databricks-on-aws.md]

## Concrete Example: Wrapping `is_context_relevant`

The following example wraps the `is_context_relevant` judge to evaluate whether an assistant's response is relevant to the user's query. The built-in judge expects a `request` (the user's query) and a `context` dictionary containing a `"response"` key. The custom scorer `is_message_relevant` extracts the content of the last user message from the `inputs["messages"]` list and passes it as the `request`:

```python
@scorer
def is_message_relevant(inputs: dict[str, Any], outputs: str) -> Feedback:
    last_user_message_content = None
    if "messages" in inputs and isinstance(inputs["messages"], list):
        for message in reversed(inputs["messages"]):
            if message.get("role") == "user" and "content" in message:
                last_user_message_content = message["content"]
                break
    if not last_user_message_content:
        raise Exception("Could not extract the last user message from inputs to evaluate relevance.")
    return is_context_relevant(
        request=last_user_message_content,
        context={"response": outputs},
    )
```
^[code-based-scorer-examples-databricks-on-aws.md]

The wrapper handles a potential mismatch: the application's `inputs` may be structured as `{"messages": [{"role": ..., "content": ...}, ...]}` while the judge expects a flat string. The wrapper also provides an explicit error when the extraction fails, which MLflow surfaces as an AssessmentError in the results table. ^[code-based-scorer-examples-databricks-on-aws.md]

## Other Wrapable Judges

The same pattern applies to any built-in LLM judge. Common judges that are frequently wrapped include:

- **Guidelines judge** — accepts guidelines as a list of strings and evaluates the response against them. A wrapper can apply different guidelines based on user attributes (e.g., user tier) extracted from the inputs. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Safety judge** — evaluates whether the response contains harmful content. A wrapper can pass specific `outputs` or `inputs` fields as the subject of evaluation.

Because these judges all follow the same [Feedback](/concepts/feedback-object.md)-returning interface, the wrapping pattern is consistent regardless of which judge is used. ^[code-based-scorer-examples-databricks-on-aws.md]

## Advanced Use: Conditional Logic with Guidelines

A more sophisticated wrapper can apply **different** guidelines depending on context. For example, a `premium_service_validator` scorer checks the user's tier (from the `inputs` dictionary) and selects a tailored set of guidelines for that tier:

```python
@scorer
def premium_service_validator(inputs, outputs, trace=None):
    user_tier = inputs.get("user_tier", "standard")
    if user_tier == "premium":
        premium_judge = Guidelines(
            name="premium_experience",
            guidelines=[...]  # specific to premium
        )
        return premium_judge(inputs=inputs, outputs=outputs)
    else:
        standard_judge = Guidelines(
            name="standard_experience",
            guidelines=[...]  # specific to standard
        )
        return standard_judge(inputs=inputs, outputs=outputs)
```
^[code-based-scorer-examples-databricks-on-aws.md]

This pattern lets you reuse a single custom scorer for multiple user segments while still leveraging the built-in guidelines enforcement logic.

## Benefits

- **Reusability** – Avoid reimplementing evaluation logic that already exists in built-in judges. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Adaptability** – Bridge the gap between your application's data schema and the judge's expected interface. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Transparency** – The wrapper's rationale and source metadata are preserved in the [MLflow UI](/concepts/mlflow.md), making it clear which judge was used and why it returned a particular score. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Extensibility** – You can add custom preprocessing (e.g., extracting the last user message) or post-processing (e.g., chaining evaluation results for further iteration) around the judge's output. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [Custom Code-based Scorers](/concepts/code-based-scorers.md) – The general framework for defining custom evaluation metrics.
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) – The set of predefined judges that can be wrapped.
- [Feedback Object](/concepts/feedback-object.md) – The data structure returned by judges and scorers.
- [AssessmentSource](/concepts/assessmentsource-entity.md) – Metadata that can be attached to feedback to identify the judge model.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The evaluation framework that runs custom scorers against traces.
- [Production Monitoring](/concepts/production-monitoring.md) – Deploying wrapped scorers for continuous evaluation of live traffic.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
