---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f93b7284b76b96d6b8aa0ad7966fae3cb8800050511aa8baaa2bee3f50b0752c
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - logged-model-evaluation-with-mlflow
    - LMEWM
    - Model Evaluation with MLflow
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: Logged Model Evaluation with MLflow
description: Loading logged MLflow models with pyfunc and wrapping them for evaluation using mlflow.genai.evaluate() with named parameters.
tags:
  - mlflow
  - model-registry
  - evaluation
timestamp: "2026-06-19T19:38:30.552Z"
---

# Logged Model Evaluation with MLflow

**Logged Model Evaluation with MLflow** refers to the pattern of evaluating a model that has been logged to the [MLflow Model Registry](/concepts/mlflow-model-registry.md) using `mlflow.genai.evaluate()`. Because most logged models accept a single input parameter (e.g., `model_inputs` for PyFunc or a single dictionary for logged LangChain flavors), while the evaluation harness expects named parameters that correspond to the keys in the evaluation dataset, a wrapper function is typically required to translate between the two interfaces. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Why Wrap the Model?

The `predict_fn` argument of `mlflow.genai.evaluate()` expects a callable whose keyword arguments match the keys in the evaluation dataset’s `inputs` field. For example, if the dataset contains `{"inputs": {"question": "..."}}`, the `predict_fn` must accept a `question` parameter. However, models loaded via `mlflow.pyfunc.load_model()` or a flavor such as LangChain usually expose a single-parameter method like `predict()` that takes a single DataFrame, dict, or similar container. Wrapping the logged model in a function that extracts the named input from the dataset and passes it to the model’s single-parameter interface reconciles this mismatch. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## How to Evaluate a Logged Model

The recommended pattern is to load the logged model **once** outside the wrapper function to avoid reloading the model on every evaluation call. The wrapper then translates the named parameter to the model’s input format and returns a dictionary (or other structure) that the chosen scorers can consume. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

```python
import mlflow
from mlflow.genai.scorers import Safety

# Load the logged model once outside the predict_fn
model = mlflow.pyfunc.load_model("models:/catalog.schema.chatbot@staging")

def evaluate_model(question: str) -> dict:
    return model.predict({"question": question})

results = mlflow.genai.evaluate(
    data=[{"inputs": {"question": "Tell me about MLflow"}}],
    predict_fn=evaluate_model,
    scorers=[Safety()],
)
```

In this example, the logged model (registered in Unity Catalog under the `staging` stage) expects a dictionary with a `"question"` key. The wrapper `evaluate_model` accepts the `question` parameter, repackages it as the model expects, and returns the model’s prediction. The evaluation harness then applies the `Safety` scorer to the results. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Supported Model Flavors

The wrapping technique applies to any logged model that follows a single-parameter interface, including:

- **PyFunc models** – loaded via `mlflow.pyfunc.load_model()`; the `predict()` method accepts a single argument (typically a Pandas DataFrame or dict).
- **LangChain models** – logged with the `langchain` flavor; often expose a single `invoke()` or `run()` method.
- Other custom flavors that accept a single input container.

The same wrapper approach works regardless of whether the evaluation data is provided as an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md), a list of dictionaries, a Pandas DataFrame, or a Spark DataFrame. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Best Practices

- **Load the model outside the wrapper** to ensure it is loaded only once per evaluation run, avoiding repeated loading overhead. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]
- **Match the input format exactly** to what the logged model expects. If the model expects a DataFrame with a specific column name, the wrapper should construct that DataFrame.
- **Return a dictionary or object** that the scorers can interpret. Many built-in scorers look for keys like `"response"`, `"output"`, or `"predictions"`; consult the scorer documentation for expected output formats.
- **Use Unity Catalog model URIs** (e.g., `models:/catalog.schema.chatbot@staging`) to reference models by stage or version for production evaluation.

## Related Concepts

- [MLflow Evaluation Harness](/concepts/mlflow-genai-evaluation-harness.md) – Overview of `mlflow.genai.evaluate()` and its components.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Central repository for logged models and their versions.
- [PyFunc Model Flavor](/concepts/custom-mlflow-pyfunc-model.md) – The standard Python function wrapper used by many MLflow models.
- [GenAI Scorers](/concepts/mlflow-genai-scorers.md) – Built-in scorers like `Safety`, `Correctness`, and `RelevanceToQuery`.
- [Evaluation Dataset Schema](/concepts/evaluation-dataset-schema.md) – Required structure for evaluation data inputs.

## Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
