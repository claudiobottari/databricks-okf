---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5e361fb62427c768fbc4e8fd7ca32a948ea6f1d615b6c55080a81a9de3f739bf
  pageDirectory: concepts
  sources:
    - log-model-dependencies-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-skinny-vs-full-mlflow-for-model-serving
    - MVFMFMS
  citations:
    - file: log-model-dependencies-databricks-on-aws.md
title: mlflow-skinny vs full mlflow for Model Serving
description: A Databricks-specific consideration where Databricks Runtime ML includes mlflow-skinny by default, requiring explicit specification of mlflow in pip_requirements to avoid container build failures in Model Serving.
tags:
  - databricks
  - mlflow
  - model-serving
timestamp: "2026-06-19T19:17:14.850Z"
---

# mlflow-skinny vs full mlflow for Model Serving

The choice between **mlflow-skinny** and the full **mlflow** package is critical when deploying models to [Model Serving](/concepts/model-serving.md) on Databricks, because the wrong choice can cause container image build failures.

## The Problem

Databricks Runtime ML runtimes include `mlflow-skinny` by default rather than the full `mlflow` package. `mlflow-skinny` is a lightweight version of MLflow that contains only the core logging and tracking functionality, without the full MLflow model serving and deployment dependencies. ^[log-model-dependencies-databricks-on-aws.md]

When you log a `pyfunc` model on one of these runtimes without specifying `pip_requirements`, MLflow automatically captures `mlflow-skinny` in the model's `conda.yaml`. This becomes a problem at deployment time: Model Serving cannot build the container image because it requires the full `mlflow` package, not the skinny version. ^[log-model-dependencies-databricks-on-aws.md]

## The Solution

To ensure Model Serving can successfully build the container image, you must explicitly specify `mlflow==<version>` in `pip_requirements` when you log the model. This overrides the automatic dependency capture of `mlflow-skinny` and ensures the full MLflow package is included in the model's deployment environment. ^[log-model-dependencies-databricks-on-aws.md]

```python
import mlflow

mlflow.pyfunc.log_model(
    model,
    "my_model",
    pip_requirements=["mlflow==<version>"]  # Specify full mlflow, not mlflow-skinny
)
```

## Implications

- **Automatic dependency capture is insufficient**: Because `mlflow-skinny` is the default on Databricks Runtime ML, you cannot rely on MLflow's automatic dependency inference to produce a deployable model for Model Serving. You must always specify the full `mlflow` version in `pip_requirements`. ^[log-model-dependencies-databricks-on-aws.md]
- **Version alignment matters**: When specifying `pip_requirements`, you should use an `mlflow` version that is compatible with your Databricks Runtime version to avoid conflicts. ^[log-model-dependencies-databricks-on-aws.md]
- **This applies specifically to Model Serving**: For batch and streaming jobs, different dependency management approaches may be acceptable. The `mlflow-skinny` issue is most critical for online serving via Model Serving endpoints. ^[log-model-dependencies-databricks-on-aws.md]

## Best Practices

1. Always log your model with explicit `pip_requirements` that includes the full `mlflow` package when you plan to deploy to Model Serving.
2. If you are using `code_paths` or `code_path` to include custom Python code, MLflow handles those dependencies automatically, but the `mlflow-skinny` issue remains for the core MLflow dependency.
3. For non-Python dependencies (Java, R, native packages), MLflow does not automatically capture them, and you must handle those separately regardless of whether you use `mlflow-skinny` or full `mlflow`.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — The primary deployment target affected by this distinction
- [Log model dependencies](/concepts/mlflow-model-dependency-logging.md) — How to properly specify dependencies when logging models
- Deploy Python code with Model Serving — Additional considerations for custom code deployment
- [Model Registry](/concepts/mlflow-model-registry.md) — Where logged models are stored before deployment

## Sources

- log-model-dependencies-databricks-on-aws.md

# Citations

1. [log-model-dependencies-databricks-on-aws.md](/references/log-model-dependencies-databricks-on-aws-e09b3b6d.md)
