---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e520902b3486477071e429a5c8a044cd5269c1b64a66eda2d6c40e643086190d
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - code-based-scorers-mlflow-genai
    - CS(G
    - Code-based Scorer Reference
    - code-based scorer reference
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Code-based Scorers (MLflow GenAI)
description: Custom evaluation metrics for GenAI applications defined using the @scorer decorator in MLflow Evaluation.
tags:
  - mlflow
  - evaluation
  - genai
  - scoring
timestamp: "2026-06-19T15:11:14.310Z"
---

# Code-based Scorers (MLflow GenAI)

**Code-based Scorers** in MLflow GenAI allow you to define flexible, custom evaluation metrics for your AI agent or application using Python code. They are implemented via the `@scorer` decorator and are used with `mlflow.genai.evaluate()` to compute metrics on the outputs of a generative AI system. The development workflow is designed for rapid iteration without re-running the entire application each time a scorer is updated. ^[develop-code-based-scorers-databricks-on-aws.md]

## Developer Workflow

The recommended iterative workflow for code-based scorers consists of four steps:

1. **Define evaluation data** – a list of input requests (e.g., a conversation with `messages`).
2. **Generate traces from your app** – use `mlflow.genai.evaluate()` with a placeholder scorer to produce traces.
3. **Query and store the resulting traces** – retrieve the generated traces as a Pandas DataFrame using `mlflow.search_traces()`.
4. **Iterate on your scorer** – call `evaluate()` again, passing the stored traces directly as the `data` argument, without a `predict_fn`. This allows you to test new scorer logic without re-running the app. ^[develop-code-based-scorers-databricks-on-aws.md]

### Prerequisites

Before implementing the workflow, ensure you have:

- `mlflow[databricks]>=3.1` installed (upgraded for the best GenAI experience).
- The `openai` package installed if the application uses the OpenAI client.
- `mlflow.openai.autolog()` called to automatically instrument the application with [MLflow Tracing](/concepts/mlflow-tracing.md).
- (Optional) If running outside Databricks, set the tracking URI to a Databricks workspace and set an experiment. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 1: Define Evaluation Data

Evaluation data is a list of dictionaries, where each dictionary contains an `"inputs"` key whose value is another dictionary with a `"messages"` list. Each message has a `"role"` and `"content"`. For example:

```python
eval_dataset = [
    {"inputs": {"messages": [{"role": "user", "content": "How much does a microwave cost?"}]}},
    ...
]
```

This data represents the requests you will send to your generative AI application. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 2: Generate Traces

Since `mlflow.genai.evaluate()` requires at least one scorer, define a placeholder scorer using the `@scorer` decorator. The placeholder returns a trivial value (e.g., `1`). Then call `evaluate()` with your evaluation data and the application’s prediction function (`predict_fn`). This records one trace per evaluation row in the active [MLflow Experiments|experiment](/concepts/mlflow-experiment.md). ^[develop-code-based-scorers-databricks-on-aws.md]

```python
from mlflow.genai.scorers import scorer

@scorer
def placeholder_metric() -> int:
    return 1

eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)
```

The resulting traces include the LLM’s responses, visible in the notebook Trace UI and the Experiment UI’s **Response** column. ^[develop-code-based-scorers-databricks-on-aws.md]

### Step 3: Query and Store Traces

Use `mlflow.search_traces(run_id=eval_results.run_id)` to retrieve the generated traces as a Pandas DataFrame. This DataFrame becomes the input for subsequent evaluation rounds. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

### Step 4: Iterate on Scorers

Define a new scorer (or modify an existing one) using the `@scorer` decorator. The scorer function can access the `outputs` parameter (the model’s response) and any other trace fields. Then call `mlflow.genai.evaluate()` with the stored traces as the `data` argument and omit the `predict_fn`. This allows you to run the new metric against the precomputed responses without re-executing the application. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
@scorer
def response_length(outputs: str) -> int:
    return len(outputs)

mlflow.genai.evaluate(data=generated_traces, scorers=[response_length])
```

## Example Notebook

The source documentation includes a full example notebook containing all the code from the tutorial. It demonstrates the complete developer workflow end to end. ^[develop-code-based-scorers-databricks-on-aws.md]

## Next Steps

After becoming familiar with code-based scorers, you can explore:

- [Custom LLM Scorers](/concepts/custom-judge-scorers.md) – semantic evaluation using LLM-as-a-judge metrics.
- [Production Monitoring](/concepts/production-monitoring.md) – deploying scorers for continuous production monitoring.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – building comprehensive test data for your scorers.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
