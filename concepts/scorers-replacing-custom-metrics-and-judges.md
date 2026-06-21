---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9de839055ccbb0cd63fba14ab51fc229014d4a3025433ca7103cef6614894df1
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - scorers-replacing-custom-metrics-and-judges
    - Judges and Scorers — Replacing Custom Metrics
    - S—RCMAJ
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: Scorers — Replacing Custom Metrics and Judges
description: Scorers are the unified evaluation building block in MLflow 3, replacing both @metric decorators and LLM judge functions, with predefined scorers (Correctness, Safety, Guidelines, etc.) and a @scorer decorator for custom logic.
tags:
  - mlflow
  - evaluation
  - scorers
timestamp: "2026-06-19T19:34:56.169Z"
---

# Scorers — Replacing Custom Metrics and Judges

**Scorers** are the unified evaluation primitive in [MLflow 3](/concepts/mlflow-3.md) that replace both the custom `@metric` decorator and the built‑in LLM judges from Agent Evaluation (MLflow 2.x). They allow you to define pass/fail checks, numeric scores, or LLM‑as‑a‑judge evaluations and use them consistently with `mlflow.genai.evaluate()`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Overview

In MLflow 2.x, custom evaluation functions were decorated with `@metric` and LLM judges (e.g., `judges.correctness`) were invoked directly or run automatically by `mlflow.evaluate()`. MLflow 3 consolidates both patterns into a single concept: **scorers**. A scorer is a function decorated with `@scorer` from `mlflow.genai.scorers`, or a predefined class that wraps an LLM judge. Scorers are passed to `mlflow.genai.evaluate()` via the `scorers` parameter (replacing the `extra_metrics` parameter and the `evaluator_config` judge‑selection mechanism). ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## The `@scorer` Decorator

Custom evaluation metrics are defined by decorating a function with `@scorer`. The function signature has been simplified compared to `@metric`:

```python
from mlflow.genai.scorers import scorer

@scorer
def my_scorer(inputs, outputs, expectations=None, traces=None):
    # Return "yes" or "no" for pass/fail, or a Feedback object for numeric scores
    ...
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Parameter Mapping

| `@metric` parameter      | `@scorer` parameter    |
|--------------------------|------------------------|
| `request`                | `inputs`               |
| `response`               | `outputs`              |
| `expected_response`      | `expectations` (dict)  |
| `retrieved_context`      | extracted from `traces`|
| (not available)          | `traces` (span data)   |

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Return Types

- **Pass/fail**: Return the string `"yes"` or `"no"`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]
- **Numeric scores**: Return a `Feedback` object from `mlflow.entities` with `name`, `value`, and `rationale`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Predefined Scorers (LLM Judges as Scorers)

MLflow 3 provides ready‑to‑use scorer classes that wrap the LLM judges from MLflow 2.x. You instantiate them and add them to the `scorers` list. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

| MLflow 2.x judge          | MLflow 3 predefined scorer         |
|---------------------------|------------------------------------|
| `judges.correctness`      | `Correctness`                     |
| `judges.safety`           | `Safety`                          |
| `judges.relevance_to_query`| `RelevanceToQuery`               |
| `judges.groundedness`     | `RetrievalGroundedness`           |
| `judges.chunk_relevance`  | `RetrievalRelevance`              |
| `judges.context_sufficiency`| `RetrievalSufficiency`          |
| `judges.guideline_adherence`| `Guidelines` (predefined) or `judges.meets_guidelines` (direct) |

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

All predefined scorers are imported from `mlflow.genai.scorers`:

```python
from mlflow.genai.scorers import (
    Correctness, Guidelines, ExpectationsGuidelines,
    RelevanceToQuery, Safety, RetrievalGroundedness,
    RetrievalRelevance, RetrievalSufficiency
)
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Guidelines and ExpectationsGuidelines

The `Guidelines` scorer replaces the old `global_guidelines` configuration. It requires explicit `name` and `guidelines` arguments. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

The `ExpectationsGuidelines` scorer reads per‑example guidelines from the `expectations.guidelines` field in the evaluation data, replacing the MLflow 2.x pattern of including guidelines in the DataFrame. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Using Scorers in Evaluation

In `mlflow.genai.evaluate()`, pass scorers via the `scorers` parameter. MLflow 3 does **not** automatically run any judges—you must explicitly list every scorer you want. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import Correctness, Safety, Guidelines

with mlflow.start_run():
    results = mlflow.genai.evaluate(
        data=eval_data,
        predict_fn=my_agent,
        scorers=[
            Correctness(),
            Safety(),
            Guidelines(name="tone", guidelines="Be professional")
        ]
    )
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

To replicate MLflow 2.x’s automatic selection of all applicable judges, explicitly include all scorers that match your data. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Examples

### Custom Pass/Fail Scorer

```python
@scorer
def response_length_check(inputs, outputs, expectations=None, traces=None):
    length = len(outputs)
    return "yes" if 50 <= length <= 500 else "no"
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Custom Numeric Scorer with Feedback

```python
from mlflow.entities import Feedback

@scorer
def semantic_similarity(outputs, expectations):
    expected = expectations.get("expected_response", "")
    score = compute_similarity(outputs, expected)
    return Feedback(
        name="semantic_similarity",
        value=score,
        rationale=f"Similarity score: {score:.2f}"
    )
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Custom Scorer Using a Judge Directly

You can still call `mlflow.genai.judges` inside a custom scorer for fine‑grained control:

```python
from mlflow.genai import judges

@scorer
def check_no_pii(inputs, outputs, traces):
    context_text = extract_context(traces)
    return judges.meets_guidelines(
        name="no_pii",
        context={"request": inputs, "retrieved_context": context_text},
        guidelines=["The context must not contain PII."]
    )
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Migration Summary

| MLflow 2.x concept               | MLflow 3 replacement                      |
|----------------------------------|-------------------------------------------|
| `@metric` decorator              | `@scorer` decorator                       |
| `extra_metrics` parameter        | `scorers` parameter                       |
| `evaluator_config["metrics"]`    | Explicit `scorers` list                   |
| `judges.guideline_adherence()`   | `Guidelines` scorer or `judges.meets_guidelines()` |
| Automatic judge selection        | Must list scorers explicitly              |
| `global_guidelines` config       | `Guidelines()` scorer instances           |

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow 3](/concepts/mlflow-3.md) — The version that introduces the scorer-based evaluation system.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The framework where scorers are used.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — The legacy system replaced by MLflow 3 scorers.
- [Custom Scorers Documentation](/concepts/custom-scorers-for-llm-evaluation.md) — Official guide for writing custom scorers.
- [MLflow Tracing](/concepts/mlflow-tracing.md) — Trace ingestion used by scorers to inspect complex span data.
- Human Feedback in MLflow — Labeling sessions that work with scorer evaluations.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
