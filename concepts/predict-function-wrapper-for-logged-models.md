---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08bb60823712b561d398433c528e3c38241366cf5697ab5fc7210a7bedb9aac6
  pageDirectory: concepts
  sources:
    - migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - predict-function-wrapper-for-logged-models
    - PFWFLM
  citations:
    - file: migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md
title: Predict Function Wrapper for Logged Models
description: MLflow 3 requires wrapping logged MLflow models in a predict function that maps named input parameters to the model's expected input format, serving as a translation layer between the evaluation framework and the model.
tags:
  - mlflow
  - model-serving
  - evaluation
timestamp: "2026-06-19T19:35:14.242Z"
---

# Predict Function Wrapper for Logged Models

A **Predict Function Wrapper for Logged Models** is a translation layer required when using `mlflow.genai.evaluate()` in MLflow 3 to evaluate a previously logged MLflow model (such as a PyFunc model or one logged by Custom Agents). The wrapper adapts the model's expected input format to the named parameter interface that the evaluation framework expects. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Why a Wrapper Is Needed

`mlflow.genai.evaluate()` accepts a `predict_fn` parameter that expects a function accepting keys from the `inputs` dict in the evaluation dataset as keyword arguments. However, most logged models accept a single input parameter — for example, `model_inputs` for [PyFunc models](/concepts/custom-mlflow-pyfunc-model.md) or similar interfaces for LangChain models. The predict function wrapper serves as a translation layer between the evaluation framework's named parameters and the model's expected input format. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Example Usage

The following example demonstrates how to create a predict function wrapper for a logged PyFunc model and use it with `mlflow.genai.evaluate()`:

```python
import mlflow
from mlflow.genai.scorers import Safety

# Make sure to load your logged model outside of the predict_fn so MLflow only loads it once!
model = mlflow.pyfunc.load_model("models:/chatbot/staging")

def evaluate_model(question: str) -> dict:
    return model.predict({"question": question})

results = mlflow.genai.evaluate(
    data=[{"inputs": {"question": "Tell me about MLflow"}}],
    predict_fn=evaluate_model,
    scorers=[Safety()]
)
```

^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

The predict function wrapper should be defined so that each key in the evaluation dataset's `inputs` dictionary maps to a corresponding parameter in the function. Internally, the function converts those named parameters into the input format expected by the loaded model. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Key Design Considerations

- **Load the model once outside the wrapper**: As shown in the example, the `model = mlflow.pyfunc.load_model(...)` call should occur outside the `predict_fn` definition. This ensures MLflow loads the model only once, avoiding redundant loading during evaluation. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]
- **Return type**: The predict function wrapper must return a dictionary, which mirrors the output format expected by the evaluation framework. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]
- **Parameter naming**: The parameter names in the wrapper function must match the keys used in the evaluation dataset's `inputs` dictionary. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Migration Context

In MLflow 2.x, you could pass a logged MLflow model directly to `mlflow.evaluate()` without a wrapper. MLflow 3.x requires the explicit predict function wrapper because `mlflow.genai.evaluate()` expects a function that maps named parameters from the dataset to the model's input interface. ^[migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md]

## Related Concepts

- [MLflow 3 GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — Overview of the MLflow 3 evaluation framework.
- [Custom Scorers Documentation](/concepts/custom-scorers-for-llm-evaluation.md) — Guidance on creating scoring functions for evaluation.
- PyFunc Models — MLflow's Python Function model flavor, which requires the wrapper pattern.
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) — The evaluation system that the wrapper supports.
- [LLM Judges](/concepts/llm-judges.md) — Built-in and custom judges used during evaluation.

## Sources

- migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md

# Citations

1. [migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws.md](/references/migrate-to-mlflow-3-from-agent-evaluation-databricks-on-aws-7eefbe86.md)
