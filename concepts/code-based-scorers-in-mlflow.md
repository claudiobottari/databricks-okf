---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 958e477584da59d6a322d7509a8bbd5645e957140c8bb90726ec1599f5766657
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-based-scorers-in-mlflow
    - CSIM
    - code-based-scorers-for-mlflow-genai-evaluation
    - CSFMGE
    - code-based-scorers-for-mlflow-genai
    - CSFMG
    - code-based-scorers-in-mlflow-genai
    - CSIMG
    - code-based-scorers-mlflow-genai
    - CS(G
    - Code-based Scorer Reference
    - code-based scorer reference
    - custom-code-based-scorers-mlflow-genai
    - CCS(G
    - Custom code-based scorers|custom scorer
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Code-based scorers in MLflow
description: Custom Python functions or classes that define flexible evaluation metrics for GenAI agent evaluation, supporting primitive returns, Feedback objects, trace data access, and error handling.
tags:
  - mlflow
  - evaluation
  - genai
timestamp: "2026-06-19T17:44:12.581Z"
---

# Code-based scorers in MLflow

**Code-based scorers** in MLflow allow you to define flexible evaluation metrics for your AI agent or application using Python code. They are a core component of MLflow Evaluation for GenAI, enabling custom assessment logic that goes beyond built-in metrics and judges. ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

Code-based scorers are Python functions or classes that evaluate the quality of outputs from your generative AI application. They can access the [[MLflow Trace]] object, input data, output responses, and expectations to compute metrics. Scorers can return primitive values, single [Feedback](/concepts/feedback-object.md) objects, or lists of Feedback objects for multi-faceted assessment. ^[code-based-scorer-examples-databricks-on-aws.md]

## Scorer Definition Patterns

### Decorator-based scorers

The `@scorer` decorator from `mlflow.genai.scorers` is the simplest way to define a custom scorer. The decorated function can accept various parameters including `trace`, `inputs`, `outputs`, and `expectations`. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer
from mlflow.entities import Feedback

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

### Class-based scorers

For scorers that require state, you can subclass the `Scorer` base class from `mlflow.genai.scorers`. Class-based scorers are Pydantic objects, allowing you to define additional fields and use them in the `__call__` method. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Scorer
from mlflow.entities import Feedback

class ResponseQualityScorer(Scorer):
    name: str = "response_quality"
    min_length: int = 50
    required_sections: Optional[list[str]] = None

    def __call__(self, outputs: str) -> Feedback:
        issues = []
        if len(outputs.split()) < self.min_length:
            issues.append(f"Too short (minimum {self.min_length} words)")
        missing = [s for s in self.required_sections if s not in outputs]
        if missing:
            issues.append(f"Missing sections: {', '.join(missing)}")
        if issues:
            return Feedback(value=False, rationale="; ".join(issues))
        return Feedback(value=True, rationale="Response meets all quality criteria")
```

^[code-based-scorer-examples-databricks-on-aws.md]

**Note:** Class-based `Scorer` subclasses are supported for offline evaluation with `mlflow.genai.evaluate()` only. They cannot be registered for [Production Monitoring](/concepts/production-monitoring.md). To use custom scorers in production, use the `@scorer` decorator. ^[code-based-scorer-examples-databricks-on-aws.md]

### Wrapping predefined LLM judges

You can create custom scorers that wrap MLflow's built-in [LLM Judges](/concepts/llm-judges.md), such as `is_context_relevant`. This allows you to preprocess trace data before passing it to the judge or post-process the feedback it returns. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.judges import is_context_relevant

@scorer
def is_message_relevant(inputs: dict[str, Any], outputs: str) -> Feedback:
    last_user_message_content = None
    for message in reversed(inputs["messages"]):
        if message.get("role") == "user" and "content" in message:
            last_user_message_content = message["content"]
            break
    return is_context_relevant(
        request=last_user_message_content,
        context={"response": outputs},
    )
```

^[code-based-scorer-examples-databricks-on-aws.md]

### Using your own LLM as a judge

Scorers can integrate custom or externally hosted LLMs for evaluation. The scorer handles API calls, input/output formatting, and generates Feedback from your LLM's response. Set the `source` field in the Feedback object to indicate the assessment source is an LLM judge. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.entities import AssessmentSource, AssessmentSourceType

@scorer
def answer_quality(inputs: dict[str, Any], outputs: str) -> Feedback:
    user_query = inputs["messages"][-1]["content"]
    judge_llm_response_obj = client.chat.completions.create(
        model="databricks-claude-sonnet-4-5",
        messages=[
            {"role": "system", "content": judge_system_prompt},
            {"role": "user", "content": judge_user_prompt.format(
                user_query=user_query, llm_response_from_app=outputs
            )},
        ],
        temperature=0.0,
    )
    # Parse JSON output and return Feedback
    return Feedback(
        value=parsed_score,
        rationale=parsed_rationale,
        source=AssessmentSource(
            source_type=AssessmentSourceType.LLM_JUDGE,
            source_id="claude-sonnet-4-5",
        )
    )
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Using Expectations

Expectations are ground truth values or labels for offline evaluation. You can specify expectations in the `data` argument of `mlflow.genai.evaluate()` using either an `expectations` column/field or a `trace` column/field. Expectations are passed directly to your custom scorer function. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {"messages": [{"role": "user", "content": "What is 2+2?"}]},
        "expectations": {
            "expected_response": "2+2 equals 4.",
            "expected_keywords": ["4", "four", "equals"],
        }
    },
]
```

^[code-based-scorer-examples-databricks-on-aws.md]

**Note:** Production monitoring typically does not include expectations since you are evaluating live traffic without ground truth. Design your scorers to handle expectations gracefully if they will be used for both offline and online evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Returning Multiple Feedback Objects

A single scorer can return a list of `Feedback` objects, allowing one scorer to assess multiple quality facets simultaneously. Each Feedback object should have a unique `name`, which becomes the metric name in the results. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def comprehensive_response_checker(outputs: str) -> list[Feedback]:
    feedbacks = [
        Feedback(name="is_not_empty_check", value="yes" if outputs != "" else "no"),
        Feedback(name="response_char_length", value=len(outputs)),
    ]
    return feedbacks
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Naming Conventions

The metric name for a scorer is determined by the following rules: ^[code-based-scorer-examples-databricks-on-aws.md]

- **Primitive value or single Feedback without a name:** The scorer function name becomes the metric name.
- **Single Feedback with an explicit name:** The name specified in the `Feedback` object is used.
- **Multiple Feedback objects:** Names specified in each `Feedback` object are preserved — you must specify a unique name for each.
- **Class-based scorers:** The `name` field of the class is used as the metric name, or individual Feedback names if multiple objects are returned.

## Error Handling

Scorers can return errors gracefully using the `AssessmentError` class within a Feedback object, or let exceptions propagate for MLflow to handle. Errors in one scorer do not prevent other scorers from running. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.entities import Feedback, AssessmentError

@scorer
def resilient_scorer(outputs, trace=None):
    try:
        response = outputs.get("response")
        if not response:
            return Feedback(
                value=None,
                error=AssessmentError(
                    error_code="MISSING_RESPONSE",
                    error_message="No response field in outputs"
                )
            )
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        raise
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Chaining Evaluation Results

You can chain evaluation results by collecting traces from one evaluation and using them as input to a subsequent evaluation. This is useful for drilling down into problematic subsets of traces for further analysis with more specialized scorers. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
# Find safety failures from initial evaluation
safety_failures = traces[traces['assessments'].apply(
    lambda x: any(a['assessment_name'] == 'Safety' 
                  and a['feedback']['value'] == 'no' for a in x)
)]

# Re-evaluate the problematic subset
results2 = mlflow.genai.evaluate(
    data=safety_failures,
    predict_fn=updated_app,
    scorers=[Guidelines(
        name="content_policy",
        guidelines="Response must follow our content policy"
    )]
)
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Conditional Logic with Guidelines

You can wrap Guidelines judges in custom code-based scorers to apply different guidelines based on user attributes or other context from the inputs or trace. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def premium_service_validator(inputs, outputs, trace=None):
    user_tier = inputs.get("user_tier", "standard")
    if user_tier == "premium":
        premium_judge = Guidelines(
            name="premium_experience",
            guidelines=[
                "The response must acknowledge the user's premium status",
                "The response must provide detailed explanations with at least 3 specific examples",
            ]
        )
        return premium_judge(inputs=inputs, outputs=outputs)
    else:
        standard_judge = Guidelines(
            name="standard_experience",
            guidelines=[
                "The response must be helpful and professional",
                "The response must be concise (under 100 words)",
            ]
        )
        return standard_judge(inputs=inputs, outputs=outputs)
```

^[code-based-scorer-examples-databricks-on-aws.md]

## Prerequisites

To use code-based scorers, update `mlflow[databricks]` to version 3.1 or later, and define your generative AI application. For examples that use traces, generate traces using `mlflow.genai.evaluate()` with a placeholder scorer. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- MLflow Evaluation for GenAI
- [[MLflow Trace]]
- [Feedback objects](/concepts/feedback-objects.md)
- [LLM Judges](/concepts/llm-judges.md)
- [Guidelines judges](/concepts/guidelines-llm-judges.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [Custom LLM scorers](/concepts/custom-judge-scorers.md)
- Build evaluation datasets

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
