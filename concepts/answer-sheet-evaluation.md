---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9894df1cadf2649bfb5a016dd14843be2d9b30120e7e92f6933f80e6de5c8680
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - answer-sheet-evaluation
    - ASE
    - answer-sheet-evaluation-mode
    - ASEM
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Answer Sheet Evaluation
description: An evaluation mode for scoring pre-computed outputs or existing traces without running the GenAI app directly during evaluation.
tags:
  - mlflow
  - evaluation
  - offline
timestamp: "2026-06-19T18:42:18.705Z"
---

# Answer Sheet Evaluation

**Answer Sheet Evaluation** is an evaluation mode in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) that allows you to score pre‑computed outputs or existing [traces](/concepts/mlflow-tracing.md) without running your GenAI application directly. Instead of invoking the app via a `predict_fn`, you provide the inputs and the corresponding outputs (the "answer sheet") and `mlflow.genai.evaluate()` applies the selected [[Scorers]] to assess quality. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## When to Use

Use answer sheet evaluation when you already have outputs and do not want—or cannot—call your GenAI app during evaluation. Common scenarios include:

- Scoring outputs from external systems
- Evaluating historical traces stored in MLflow
- Running evaluation on batch‑job results

You provide the inputs and outputs (or existing traces), and the system runs the scorers and logs an [evaluation run](/concepts/evaluation-runs.md) in the active MLflow experiment. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## How It Works

The answer sheet workflow is:

1. You supply evaluation data (either as a list of dictionaries, a Pandas DataFrame, or an [Evaluation Dataset](/concepts/evaluation-dataset.md)).
2. The data can be in two forms:
   - **Inputs and outputs**: MLflow constructs traces from the provided inputs and outputs.
   - **Existing traces**: MLflow uses the traces directly.
3. `mlflow.genai.evaluate()` runs each scorer on the traces and produces feedback annotations.
4. The results are stored in an evaluation run in the active experiment.

No `predict_fn` is required; the app is not called. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Data Formats

### Inputs and Outputs

Each record must contain an `inputs` dictionary and an `outputs` dictionary. Example:

```python
[
    {
        "inputs": {"question": "What is MLflow?"},
        "outputs": {"response": "MLflow is an open-source platform ..."}
    },
    ...
]
```

### Existing traces

Provide a list of trace objects obtained via `mlflow.search_traces()`. Each trace includes the full chain of steps, inputs, and outputs. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Example

The following code evaluates pre‑computed outputs using answer sheet evaluation:

```python
import mlflow
from mlflow.genai.scorers import Safety, RelevanceToQuery

results_data = [
    {
        "inputs": {"question": "What is MLflow?"},
        "outputs": {"response": "MLflow is an open-source platform for managing machine learning workflows, including tracking experiments, packaging code, and deploying models."},
    },
    {
        "inputs": {"question": "How do I get started?"},
        "outputs": {"response": "To get started with MLflow, install it using 'pip install mlflow' and then run 'mlflow ui' to launch the web interface."},
    }
]

evaluation = mlflow.genai.evaluate(
    data=results_data,
    scorers=[Safety(), RelevanceToQuery()]
)
```

To evaluate existing traces:

```python
traces = mlflow.search_traces(
    filter_string="trace.status = 'OK'",
)

evaluation = mlflow.genai.evaluate(
    data=traces,
    scorers=[Safety(), RelevanceToQuery()]
)
```

^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Important Caveat

If you use an answer sheet with traces that differ from those your app would produce in production, you may need to rewrite your scorer functions to use them for [Production Monitoring](/concepts/production-monitoring.md). This is because the answer sheet traces are static and may not match the tracing schema of a live deployment. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Comparison with Direct Evaluation

| Aspect | Answer Sheet Evaluation | [Direct Evaluation](/concepts/direct-evaluation.md) |
|--------|------------------------|-----------------------|
| App invocation | Not required; uses pre‑computed data | Calls the app via `predict_fn` |
| Trace generation | Reconstructed from inputs/outputs or uses existing traces | Captured live from app execution |
| Production monitoring reuse | May require scorer adaptation | Scorers can be reused directly |

Direct evaluation is the recommended mode when you can run your app, because it produces traces identical to those in production. Answer sheet evaluation is useful when the app is unavailable or when you only have historical outputs. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [Direct Evaluation](/concepts/direct-evaluation.md)
- [Evaluation Dataset](/concepts/evaluation-dataset.md)
- [[Scorers]]
- [Evaluation Runs](/concepts/evaluation-runs.md)
- [Production Monitoring](/concepts/production-monitoring.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
