---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: db52f03f1c16fc3a2238699975c2dcc408277801a680f2c8b9d669d6718baed7
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-3-genai-evaluation-api
    - M3GEA
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: MLflow 3 GenAI Evaluation API
description: The new mlflow.genai.evaluate() API that replaces mlflow.evaluate() for agent and LLM evaluation, with cleaner parameter names and explicit scorer selection.
tags:
  - mlflow
  - evaluation
  - api-migration
timestamp: "2026-06-19T19:34:42.031Z"
---

# MLflow 3 GenAI Evaluation API

The **MLflow 3 GenAI Evaluation API** is the new evaluation framework for generative AI applications on Databricks, replacing the earlier Agent Evaluation SDK. It is exposed through the `mlflow[databricks]>=3.1` SDK under the `mlflow.genai` namespace and introduces a refreshed UI, simplified APIs, enhanced tracing, streamlined human feedback collection, and improved LLM judges. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Key Features

The GenAI Evaluation API provides several major improvements over the previous Agent Evaluation (MLflow 2.x) design:

- **Refreshed UI** that mirrors all SDK functionality.  
- **New SDK** with simplified APIs for running evaluation, collecting human labels, and managing evaluation datasets.  
- **Enhanced tracing** backed by a production-scale trace ingestion backend that offers real-time observability.  
- **Streamlined human feedback** collection.  
- **Improved LLM judges** delivered as built-in scorers.  

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Core Evaluation Function: `mlflow.genai.evaluate()`

The main entry point for evaluating generative AI models is `mlflow.genai.evaluate()`. It replaces `mlflow.evaluate()` from MLflow 2.x and uses cleaner, more explicit parameter names. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Parameter Changes

| MLflow 2.x (`mlflow.evaluate`) | MLflow 3.x (`mlflow.genai.evaluate`) | Description |
|--------------------------------|--------------------------------------|-------------|
| `model`                        | `predict_fn`                         | The function or model to evaluate. |
| `extra_metrics`                 | `scorers`                            | List of scorers (the new name for custom metrics). |
| `evaluator_config`              | Removed; configuration is now per-scorer. | Judge configuration moved to the scorer itself. |
| `model_type="databricks-agent"` | Removed.                             | No longer needed; the API is dedicated to GenAI. |

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Data Field Mapping

The data format for evaluation examples has been restructured. The table below shows the mapping from MLflow 2.x to MLflow 3.x:

| MLflow 2.x field    | MLflow 3.x field      | Notes |
|---------------------|-----------------------|-------|
| `request`           | `inputs`              | A dictionary containing the input parameters. |
| `response`          | `outputs`             | A dictionary containing the model output. |
| `expected_response` | `expectations`        | A dictionary containing ground-truth fields. |
| `retrieved_context` | (extracted from trace)| Retrieved context is now automatically extracted from the trace data by predefined scorers. |

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Custom Scorers vs. Old Custom Metrics

Custom evaluation functions, previously defined with the `@metric` decorator from `databricks.agents.evals`, are now defined with `@scorer` from `mlflow.genai.scorers`. The function signature is simplified: instead of individual parameters like `request`, `response`, and `expected_response`, the scorer receives an `inputs` dict, `outputs` dict, an optional `expectations` dict, and an optional `traces` object. Return values are either a string (`"yes"`/`"no"`) for pass/fail scorers or a `Feedback` object (from `mlflow.entities`) for numeric scorers. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
# Old style (MLflow 2.x)
from databricks.agents.evals import metric
@metric
def response_length_check(request, response, expected_response=None):
    length = len(response)
    return "yes" if 50 <= length <= 500 else "no"

# New style (MLflow 3.x)
from mlflow.genai.scorers import scorer
@scorer
def response_length_check(inputs, outputs, expectations=None, traces=None):
    length = len(outputs)
    return "yes" if 50 <= length <= 500 else "no"
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Accessing Evaluation Results

In MLflow 3, evaluation results are stored as [[MLflow Trace|MLflow Traces]] with assessments. Use `mlflow.search_traces()` to retrieve them, iterating over the assessments attached to each trace. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

```python
traces = mlflow.search_traces(run_id=results.run_id)
for trace in traces:
    for assessment in trace.info.assessments:
        print(f"Scorer: {assessment.name}, Value: {assessment.value}, Rationale: {assessment.rationale}")
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## LLM Judges

MLflow 2.x automatically selected and ran all applicable LLM judges based on available data fields. MLflow 3 requires you to **explicitly list the scorers** you want to run, giving more control but requiring explicit specification. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

### Predefined Scorers

The following predefined scorers are available from `mlflow.genai.scorers`: ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

- `Correctness()` – requires `expectations.expected_response`.
- `RelevanceToQuery()` – no ground truth needed.
- `Safety()` – checks for unsafe content.
- `RetrievalGroundedness()` – automatically extracts context from traces.
- `RetrievalRelevance()` – checks relevance of retrieved context.
- `RetrievalSufficiency()` – requires ground truth.
- `Guidelines(name, guidelines)` – checks user‑defined guidelines (as a string or list of strings).
- `ExpectationsGuidelines()` – uses per‑example guidelines stored in `expectations.guidelines`.

### Direct Judge Calls

For advanced use cases, judges can still be called directly via `mlflow.genai.judges`: `judges.correctness()`, `judges.meets_guidelines()`, etc. The old `judges.guideline_adherence()` has been renamed to `judges.meets_guidelines()`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Human Feedback

The labeling and review app functionality moved from `databricks.agents.review_app` to `mlflow.genai.labeling` and `mlflow.genai.label_schemas`. Label schemas are created with `schemas.create_label_schema()`, and labeling sessions with `labeling.create_labeling_session()`. Previously built‑in schemas (e.g., `EXPECTED_FACTS`) must now be explicitly created with the appropriate constant names. Syncing feedback to datasets uses `mlflow.genai.datasets.get_dataset()` instead of `spark.read.table()`. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Important Notes

- MLflow 3 with Agent Evaluation works only on **Managed MLflow**, not open‑source MLflow. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]
- By default, MLflow 3 does **not** automatically run any judges – all scorers must be explicitly specified. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]
- Custom scorers must return valid values: `"yes"`/`"no"` for pass/fail, or a `Feedback` object for numeric scores. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]]
- [LLM Judges](/concepts/llm-judges.md)
- Managed MLflow vs. Open Source MLflow
- [Agent Evaluation (MLflow 2.x)](/concepts/genai-agent-evaluation-workflow.md)
- [Custom Scorers](/concepts/custom-scorers-mlflow-genai.md)

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
