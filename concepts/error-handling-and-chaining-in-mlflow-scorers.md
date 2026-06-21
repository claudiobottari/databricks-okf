---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a50ae4ea426b6edb6ffb49286bd802062efcce5e0c57b1cc7b2e8d8fc5ea7ac6
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - error-handling-and-chaining-in-mlflow-scorers
    - chaining in MLflow scorers and Error handling
    - EHACIMS
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Error handling and chaining in MLflow scorers
description: Patterns for handling scorer errors gracefully via AssessmentError and try/except, and for chaining evaluation results to iteratively refine datasets and applications.
tags:
  - mlflow
  - scorers
  - error-handling
  - evaluation-workflow
timestamp: "2026-06-18T14:36:46.788Z"
---

# Error handling and chaining in MLflow scorers

**Error handling and chaining in MLflow scorers** refers to two complementary patterns for building robust evaluation pipelines: gracefully managing failures within individual scorers, and sequentially re-evaluating subsets of traces based on prior scorer results.

## Error handling approaches

MLflow provides two mechanisms for handling errors in custom code-based scorers: returning an explicit error feedback object, or raising an exception that MLflow handles gracefully. Both approaches allow evaluation to continue even when individual scorer calls fail. ^[code-based-scorer-examples-databricks-on-aws.md]

### Returning an AssessmentError

A scorer can return a `Feedback` object containing an `AssessmentError` to signal a problem without raising an exception. This is useful for expected failure modes such as missing data fields. The `AssessmentError` includes an error code and a human-readable message. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer
from mlflow.entities import Feedback, AssessmentError

@scorer
def resilient_scorer(outputs, trace=None):
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
```

### Raising exceptions

When an unexpected error occurs, the scorer can raise an exception. MLflow catches the exception and continues evaluating the remaining scorers on the same trace, as well as the current scorer on subsequent traces. ^[code-based-scorer-examples-databricks-on-aws.md]

```python
@scorer
def resilient_scorer(outputs, trace=None):
    try:
        # evaluation logic
        return Feedback(value=True, rationale="Valid response")
    except Exception as e:
        # Let MLflow handle the error gracefully
        raise
```

## Chaining evaluation results

Chaining evaluation results allows you to run an initial set of scorers across all traces, identify a problematic subset, and then re-evaluate those traces with different or more targeted scorers. This pattern is particularly useful for focusing computational resources on challenging cases or for iterative development of your AI application. ^[code-based-scorer-examples-databricks-on-aws.md]

### Workflow

The chaining workflow proceeds in two stages:

1. **Initial evaluation**: Run broad, general-purpose scorers (e.g., `Safety()`) across the full evaluation dataset using [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md).
2. **Filtered re-evaluation**: Use mlflow.search_traces() to retrieve the results, filter to traces flagged by the initial scorer, and re-evaluate that subset with more specialized scorers or an updated application. ^[code-based-scorer-examples-databricks-on-aws.md]

### Example

```python
from mlflow.genai.scorers import Safety, Guidelines

# Stage 1: Initial evaluation with a broad safety checker
results1 = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[Safety()]
)

# Retrieve results and filter to problematic traces
traces = mlflow.search_traces(run_id=results1.run_id)
safety_failures = traces[traces['assessments'].apply(
    lambda x: any(
        a['assessment_name'] == 'Safety' and a['feedback']['value'] == 'no'
        for a in x
    )
)]

# Stage 2: Re-evaluate failures with a targeted content policy checker
if len(safety_failures) > 0:
    results2 = mlflow.genai.evaluate(
        data=safety_failures,
        predict_fn=updated_app,
        scorers=[
            Guidelines(
                name="content_policy",
                guidelines="Response must follow our content policy"
            )
        ]
    )
```

### Use cases for chaining

Chaining is valuable in several scenarios:

- **Iterative app improvement**: After identifying failures with a general-purpose scorer, you can iterate on your AI application and re-run the evaluation on only the problematic subset to verify improvements. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Cost optimization**: Expensive LLM-based judges can be reserved for traces that fail cheaper, faster heuristic scorers.
- **Multi-stage quality gates**: Apply increasingly strict or specific evaluation criteria as traces progress through filtering stages.

## Related concepts

- [Custom code-based scorers](/concepts/code-based-scorers.md) — Defining flexible evaluation metrics for AI agents
- MLflow Evaluation for GenAI — The evaluation framework for generative AI applications
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers for continuous quality monitoring
- AssessmentError — Error reporting object for scorer failures
- [Feedback Object](/concepts/feedback-object.md) — The structured return value for scorer assessments

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
