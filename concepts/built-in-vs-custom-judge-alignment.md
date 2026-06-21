---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f60b218e3ccde854c7f9ed032d80b1be08f56385fbd2cfd7461b8d2ac17e7d0d
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - built-in-vs-custom-judge-alignment
    - BVCJA
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Built-in vs Custom Judge Alignment
description: The distinction that alignment applies to both built-in judges (generic criteria adapted to domain) and custom judges (refined specialized evaluation logic), using the same align() method.
tags:
  - llm-evaluation
  - mlflow
  - judges
timestamp: "2026-06-18T14:24:30.602Z"
---

# Built-in vs Custom Judge Alignment

**Built-in vs Custom Judge Alignment** refers to the process of adapting both pre-defined and user-defined [LLM Judges](/concepts/llm-judges.md) to match human evaluation standards through systematic feedback. The same alignment workflow applies to both types of judges, allowing teams to transform generic evaluators into domain-specific experts that understand unique quality criteria. ^[align-judges-with-humans-databricks-on-aws.md]

## Overview

Judge alignment improves agreement with human assessments by 30 to 50 percent compared to baseline judges. The alignment process works identically for [Built-in Judges](/concepts/built-in-judges.md) (such as `RelevanceToQuery`, `Safety`, or `Correctness`) and [Custom Judges](/concepts/custom-judges.md) created with `make_judge()`. ^[align-judges-with-humans-databricks-on-aws.md]

Use alignment with built-in judges to adapt their generic criteria to your domain, or with custom judges to refine specialized evaluation logic. ^[align-judges-with-humans-databricks-on-aws.md]

## Alignment Workflow

Both built-in and custom judges follow the same three-step alignment workflow:

1. **Generate initial assessments**: Use a built-in or custom judge to evaluate traces and establish a baseline.
2. **Collect human feedback**: Domain experts review and correct judge assessments.
3. **Align and deploy**: Invoke the judge's `align()` method to create a new judge that is more aligned with human feedback.

^[align-judges-with-humans-databricks-on-aws.md]

## Requirements

- MLflow 3.4.0 or above to use judge alignment features.
- A judge to align — either a built-in judge (e.g., `RelevanceToQuery` or `Correctness`) or a custom judge created with `make_judge()`.
- The human feedback assessment name must exactly match the judge's `name` attribute. For built-in judges, this is the default snake_case name (e.g., `relevance_to_query` for `RelevanceToQuery`) unless you override it by passing `name=` when instantiating the class. For custom judges, it's the `name` you passed to `make_judge()` (e.g., `product_quality`).
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.

^[align-judges-with-humans-databricks-on-aws.md]

## Step 1: Set Up the Judge and Generate Traces

### Built-in Judge

Instantiate a built-in judge directly. Built-in judges expose a `name` attribute (the default is a snake_case string such as `relevance_to_query`) that you'll use when logging human feedback in Step 2.

```python
from mlflow.genai.scorers import RelevanceToQuery
import mlflow

experiment = mlflow.set_experiment("/Shared/relevance-alignment")
experiment_id = experiment.experiment_id

initial_judge = RelevanceToQuery()
```

^[align-judges-with-humans-databricks-on-aws.md]

### Custom Judge

For custom judges, use the `name` you passed to `make_judge()` (e.g., `product_quality`) as the feedback name when logging assessments. ^[align-judges-with-humans-databricks-on-aws.md]

### Generating Traces

You can achieve reasonable alignment with at least 10 traces, but 50-100 traces yield better results. Generate traces and run the judge, using the judge's `name` attribute as the feedback `name`:

```python
for i in range(50):
    query = f"Tell me about product {i}"
    description = generate_product_description(query)
    trace_id = mlflow.get_last_active_trace_id()
    trace = mlflow.get_trace(trace_id)
    judge_result = initial_judge(trace=trace)
    mlflow.log_feedback(
        trace_id=trace_id,
        name=initial_judge.name,
        value=judge_result.value,
        rationale=judge_result.rationale,
    )
```

^[align-judges-with-humans-databricks-on-aws.md]

## Step 2: Collect Human Feedback

Collect human feedback to teach the judge your quality standards. You can use the Databricks UI to manually review traces and provide feedback, or use programmatic feedback approaches. ^[align-judges-with-humans-databricks-on-aws.md]

### Best Practices for Feedback Collection

- **Diverse reviewers**: Include multiple domain experts to capture varied perspectives.
- **Balanced examples**: Include at least 30% negative examples (poor/fair ratings).
- **Clear rationales**: Provide detailed explanations for ratings.
- **Representative samples**: Cover edge cases and common scenarios.

^[align-judges-with-humans-databricks-on-aws.md]

## Step 3: Align and Register the Judge

The same `align()` method is used for both built-in and custom judges. When you call `align()` without specifying an optimizer, the MemAlign optimizer is used automatically:

```python
traces_for_alignment = mlflow.search_traces(
    experiment_ids=[experiment_id],
    max_results=100,
    return_type="list"
)

if len(traces_for_alignment) >= 10:
    aligned_judge = initial_judge.align(traces_for_alignment)
    aligned_judge.register(
        experiment_id=experiment_id,
        name=f"{initial_judge.name}_aligned",
        tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}
    )
```

^[align-judges-with-humans-databricks-on-aws.md]

## Key Differences Between Built-in and Custom Judge Alignment

| Aspect | Built-in Judge Alignment | Custom Judge Alignment |
|--------|-------------------------|----------------------|
| **Purpose** | Adapt generic criteria to your domain | Refine specialized evaluation logic |
| **Initial setup** | Instantiate directly from `mlflow.genai.scorers` | Create with `make_judge()` |
| **Name attribute** | Default snake_case name (e.g., `relevance_to_query`) | Name passed to `make_judge()` (e.g., `product_quality`) |
| **Alignment method** | Same `align()` method | Same `align()` method |

^[align-judges-with-humans-databricks-on-aws.md]

## Custom Alignment Optimizers

For specialized alignment strategies, extend the `AlignmentOptimizer` base class from `mlflow.genai.judges.base`. The system supports the optimizers available in the package `mlflow.genai.judges.optimizers`. ^[align-judges-with-humans-databricks-on-aws.md]

## Limitations

- Judge alignment does not support agent-based or expectation-based evaluation.
- Alignment is not supported for session-level (multi-turn) judges such as `ConversationCompleteness`.

^[align-judges-with-humans-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — The evaluators that can be aligned
- [Built-in Judges](/concepts/built-in-judges.md) — Pre-defined judges like `RelevanceToQuery`, `Safety`, `Correctness`
- [Custom Judges](/concepts/custom-judges.md) — User-defined judges created with `make_judge()`
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying aligned judges at scale
- Human Feedback Alignment — The broader process of aligning AI systems with human preferences

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
