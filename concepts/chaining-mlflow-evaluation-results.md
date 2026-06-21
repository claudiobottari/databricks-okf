---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d4c57c3f0d5ee984082a73e84c2da4131d99b50dbdcdc5f122d86d734dd2df55
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - chaining-mlflow-evaluation-results
    - CMER
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Chaining MLflow Evaluation Results
description: A pattern using evaluation results to filter problematic traces and re-evaluate them with different scorers or an updated application for targeted iteration.
tags:
  - mlflow
  - evaluation
  - workflow
  - tracing
timestamp: "2026-06-19T14:12:49.399Z"
---

# Chaining MLflow Evaluation Results

**Chaining MLflow Evaluation Results** refers to a workflow where the output of one [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) run is used to filter or select a subset of traces, which is then fed into a subsequent evaluation with different [[scorers]] or an updated GenAI application. This technique allows teams to progressively narrow down problematic cases and apply more targeted or expensive evaluation criteria only where needed. ^[code-based-scorer-examples-databricks-on-aws.md]

## Overview

In a typical chaining workflow:

1. Run a broad initial evaluation with a general scorer (e.g., `Safety()`).
2. Retrieve the traces from that evaluation using `mlflow.search_traces()`.
3. Filter the traces to those that failed a specific assessment (e.g., where the safety scorer returned `"no"`).
4. Run a second evaluation on the filtered subset, possibly with a different scorer (e.g., `Guidelines`) or after iterating on the AI application itself.

This approach is more efficient than applying expensive or detailed judges to every trace, and it helps focus improvement efforts on the most challenging inputs. ^[code-based-scorer-examples-databricks-on-aws.md]

## Implementation

The following example, adapted from the MLflow code-based scorer examples, demonstrates a chaining pattern:

```python
from mlflow.genai.scorers import Safety, Guidelines

# 1. Initial evaluation with a broad safety scorer
results1 = mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[Safety()]
)

# 2. Retrieve all traces from the first evaluation
traces = mlflow.search_traces(run_id=results1.run_id)

# 3. Filter to traces where the Safety scorer indicated a failure
safety_failures = traces[traces['assessments'].apply(
    lambda x: any(
        a['assessment_name'] == 'Safety' and a['feedback']['value'] == 'no'
        for a in x
    )
)]

# 4. Re-evaluate the problematic subset with a more specific judge
if len(safety_failures) > 0:
    results2 = mlflow.genai.evaluate(
        data=safety_failures,
        predict_fn=updated_app,  # optionally updated after iteration
        scorers=[
            Guidelines(
                name="content_policy",
                guidelines="Response must follow our content policy"
            )
        ]
    )
```

^[code-based-scorer-examples-databricks-on-aws.md]

The `predict_fn` parameter can be left unchanged (as `sample_app` in the original example) or replaced with an improved version of the application that was refined based on the insights from the first evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Use Cases

- **Progressive evaluation**: Start with a cheap, broad scorer (e.g., `Safety`) and escalate failures to a more expensive or detailed judge (e.g., `Guidelines` with custom content policy). ^[code-based-scorer-examples-databricks-on-aws.md]
- **Iterative improvement**: After identifying a set of problematic traces, modify the AI application and re‑evaluate only those traces to verify that the fix works. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Targeted analysis**: Focus detailed evaluation on a specific failure mode (e.g., hallucinations or off‑topic responses) without re‑evaluating all traces with a heavy scorer. ^[code-based-scorer-examples-databricks-on-aws.md]

## Prerequisites

- The initial evaluation must be run with `mlflow.genai.evaluate()` so that traces are logged and searchable. ^[code-based-scorer-examples-databricks-on-aws.md]
- The trace DataFrame returned by `mlflow.search_traces()` includes an `assessments` column that contains the feedback from all scorers used in the evaluation. ^[code-based-scorer-examples-databricks-on-aws.md]

## Best Practices

- **Keep the first evaluation lightweight**: Use a fast, general‑purpose scorer (like `Safety()` or a simple [code-based scorer](/concepts/code-based-scorers.md)) to avoid unnecessary cost. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Design scorers for filtering**: Return structured feedback (e.g., boolean or categorical values) that can be easily queried in the filter step. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Document the chain**: Log which scorer was used at each stage and why, so that results are reproducible. ^[code-based-scorer-examples-databricks-on-aws.md]
- **Consider multi‑stage chaining**: For deep investigations, you can chain more than two evaluations, each narrowing the dataset further. ^[code-based-scorer-examples-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The core API for running scorers against traces.
- [Code‑Based Scorers](/concepts/code-based-scorers.md) — Custom scorers defined with the `@scorer` decorator or the `Scorer` class.
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) — A built‑in MLflow scorer for detecting harmful content.
- [Guidelines Judge](/concepts/guidelines-llm-judge.md) — A judge that checks responses against custom guidelines.
- mlflow.search_traces()|mlflow.search_traces — Function to retrieve logged traces from an evaluation run.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying scorers to continuously monitor live traffic.

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
