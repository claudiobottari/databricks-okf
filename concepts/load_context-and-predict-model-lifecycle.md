---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7c4edbd40bfd119f44067a66fb66e2ed3b2a5df93a7a34d4926c6f2aa7e87b9
  pageDirectory: concepts
  sources:
    - deploy-python-code-with-model-serving-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - load_context-and-predict-model-lifecycle
    - predict Model Lifecycle and load_context
    - LAPML
  citations:
    - file: deploy-python-code-with-model-serving-databricks-on-aws.md
title: load_context and predict Model Lifecycle
description: "Custom MLflow pyfunc models require two functions: load_context for one-time initialization and predict for per-request inference logic."
tags:
  - mlflow
  - model-lifecycle
  - python
timestamp: "2026-06-18T15:26:51.649Z"
---

# `load_context` and `predict` Model Lifecycle

The **`load_context` and `predict` model lifecycle** defines how a custom [MLflow Python Function (pyfunc) model](/concepts/mlflow-pyfunc-custom-python-model.md) initialises and serves inference requests. When packaging arbitrary Python code with MLflow, two mandatory functions control the model’s behaviour: `load_context` (called once when the model is loaded) and `predict` (called for every incoming request). This two-phase lifecycle is designed to minimise per-request overhead and maximise inference speed in production environments such as [Model Serving](/concepts/model-serving.md). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## `load_context` – One-Time Initialisation

The `load_context` function is invoked exactly once when the model is loaded into memory (for example, when a Model Serving endpoint starts or a new container is provisioned). Its purpose is to load any artifacts that are needed for the model to operate but do not change per request. Typical use cases include:

- Loading model weights (e.g., with `torch.load`, `transformers`).
- Instantiating tokenizers, embedders, or feature transformers.
- Loading lookup tables or configuration files.

Because these artefacts are loaded once rather than on every call, the overhead is amortised across all subsequent requests, significantly reducing latency. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

```python
class CustomModel(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        self.model = torch.load(context.artifacts["model-weights"])
        from preprocessing_utils.my_custom_tokenizer import CustomTokenizer
        self.tokenizer = CustomTokenizer(context.artifacts["tokenizer_cache"])
```

The `context` object provides access to:

- `context.artifacts` – a dictionary of artifact paths logged with the model.
- `context.model_config` – any custom configuration passed during model logging.

Code from shared modules can be made available via the `code_path` parameter at log time. Any Python code referenced in `code_path` is automatically added to the Python path inside the model’s loaded environment. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## `predict` – Per-Request Inference

The `predict` function is called for every inference request. It contains all the logic that must execute on each request, such as:

- Preprocessing raw inputs (e.g., tokenising text, normalising numbers).
- Running the model’s forward pass.
- Postprocessing raw outputs (e.g., applying a sigmoid, formatting predictions).

```python
    def predict(self, context, model_input):
        model_input = self.format_inputs(model_input)
        outputs = self.model.predict(model_input)
        return self.format_outputs(outputs)
```

The function receives:

- `context` – the same `PythonModelContext` object (so it can access artefacts loaded in `load_context`).
- `model_input` – the input data for the single request (typically a Pandas DataFrame or a NumPy array).

The separation of one‑time setup (`load_context`) from per‑request logic (`predict`) is critical for performance: heavy artefacts are fetched and initialised only once, and every subsequent `predict` call runs with minimal overhead. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Lifecycle Overview

1. **Model logging** – The model is logged with `mlflow.pyfunc.log_model()`, which serialises the Python class, any specified `pip_requirements`, and `code_path` references.
2. **Model loading** – When the serving environment starts, MLflow deserialises the model and calls `load_context` once. This is the only opportunity to load heavy artifacts.
3. **Request processing** – Each incoming HTTP request triggers a call to `predict`. The function can safely use any objects initialised in `load_context`.
4. **Scaling** – If multiple replicas are deployed, each one independently runs `load_context` when it starts, and then handles its own stream of `predict` calls.

This pattern is recommended for any custom model that involves expensive initialisation (model weights, tokenizers, etc.). ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Best Practices

- **Always specify `pip_requirements` when logging on Databricks Runtime ML**. Databricks Runtime ML ships with `mlflow-skinny` by default, which is insufficient for Model Serving. Explicitly include `mlflow==<version>` in `pip_requirements`. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Validate the model before deployment** using `mlflow.models.predict` to ensure the custom `pyfunc` model works correctly in a serving context. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]
- **Use `code_path` to organise shared utilities** and keep the model class clean. All Python files in the `code_path` directories are available at runtime. ^[deploy-python-code-with-model-serving-databricks-on-aws.md]

## Related Concepts

- [Custom MLflow Python Function Model](/concepts/custom-mlflow-pyfunc-model.md)
- [Model Serving](/concepts/model-serving.md)
- MLflow pyfunc
- Deploy Python code with Model Serving
- [Validate models before deployment](/concepts/model-validation-before-deployment.md)

## Sources

- deploy-python-code-with-model-serving-databricks-on-aws.md

# Citations

1. [deploy-python-code-with-model-serving-databricks-on-aws.md](/references/deploy-python-code-with-model-serving-databricks-on-aws-84536f0c.md)
