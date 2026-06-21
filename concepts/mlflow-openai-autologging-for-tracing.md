---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 06e154141384836e0904558d795825b89f43fb410149d4c5580379bfa0934d59
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autologging-for-tracing
    - MOAFT
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow OpenAI Autologging for Tracing
description: Automatically instrumenting OpenAI-based applications with MLflow Tracing via mlflow.openai.autolog(), which captures traces for use as scorer inputs during evaluation.
tags:
  - mlflow
  - openai
  - tracing
  - instrumentation
timestamp: "2026-06-19T10:13:30.121Z"
---

# MLflow OpenAI Autologging for Tracing

**MLflow OpenAI Autologging for Tracing** is a feature of [MLflow](/concepts/mlflow.md) that automatically instruments applications using the OpenAI client with [MLflow Tracing](/concepts/mlflow-tracing.md). When enabled via `mlflow.openai.autolog()`, it records traces of interactions with the OpenAI API without requiring manual instrumentation of each call. This is especially useful in evaluation workflows where traces serve as inputs to [Code-based Scorers](/concepts/code-based-scorers.md) or [Custom Judges](/concepts/custom-judges.md).

## Overview

The `mlflow.openai.autolog()` call configures MLflow to capture tracing data from any OpenAI API client used in the application. This includes calls made through the standard `openai` Python package or through cloud-provider-specific wrappers such as `databricks_openai`. The recorded traces capture the inputs to and outputs from the LLM, along with associated metadata. ^[develop-code-based-scorers-databricks-on-aws.md]

Autologging simplifies the developer workflow for building and evaluating GenAI agents. Instead of manually adding `@mlflow.trace` decorators to every LLM call, you enable autologging once at the start of your script or notebook. Subsequent invocations of the OpenAI client are automatically traced, and the traces become available for visualization in the [MLflow UI](/concepts/mlflow.md) and for use in [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md).

## Setup

To use OpenAI autologging, ensure you have the necessary packages installed and configured:

```python
%pip install -q --upgrade "mlflow[databricks]>=3.1" openai
```

Then enable autologging:

```python
import mlflow

mlflow.openai.autolog()
```

If running outside of Databricks, set the tracking URI to point to your Databricks workspace:

```python
mlflow.set_tracking_uri("databricks")
```

^[develop-code-based-scorers-databricks-on-aws.md]

A common pattern is to combine autologging with explicit `@mlflow.trace` decoration on the calling function. The autologging captures the low-level OpenAI API calls, while the decorator captures higher-level application logic.

```python
@mlflow.trace
def sample_app(messages: list[dict[str, str]]):
    messages_for_llm = [
        {"role": "system", "content": "You are a helpful assistant."},
        *messages,
    ]
    response = client.chat.completions.create(
        model=model_name,
        messages=messages_for_llm,
    )
    return response.choices[0].message.content
```

^[develop-code-based-scorers-databricks-on-aws.md]

## Usage in Evaluation Workflows

Traces generated via autologging can be directly consumed by [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md). The recommended workflow is:

1. **Define evaluation data** – A list of input dictionaries (e.g., conversation histories).
2. **Generate traces** – Use `mlflow.genai.evaluate()` with your application function and a placeholder scorer to run the app over the evaluation data. The traces are automatically recorded.
3. **Query the traces** – Retrieve the traces using `mlflow.search_traces()`.
4. **Iterate on scorers** – Pass the stored traces DataFrame directly to `mlflow.genai.evaluate()` as the dataset, without re-running the application. This allows rapid iteration on scoring logic.

```python
# Step 1: Define eval dataset
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"}
            ]
        }
    },
    # ... more entries
]

# Step 2: Generate traces using autologging
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=sample_app,
    scorers=[placeholder_metric]
)

# Step 3: Query stored traces
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)

# Step 4: Evaluate with new scorers without re-running the app
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length]
)
```

^[develop-code-based-scorers-databricks-on-aws.md]

When autologging is active, each LLM response produced during evaluation is visible in the MLflow Experiment UI under the **Response** column, and detailed traces appear in the notebook's trace visualization. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) – The tracing subsystem that records execution details.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The framework for evaluating LLM applications, which consumes traces.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Metrics defined in code that can operate on traces.
- [Custom Judges](/concepts/custom-judges.md) – LLM-as-a-judge evaluators that benefit from trace data.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Where traces and evaluation results are stored.
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md) – Pre-configured environment with MLflow and autologging support.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
