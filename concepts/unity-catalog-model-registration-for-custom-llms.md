---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3122e1986cbd4d235112f53fff3b41322041e46aac82867ff6f9fe833758a87
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-model-registration-for-custom-llms
    - UCMRFCL
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Unity Catalog Model Registration for Custom LLMs
description: The process of registering custom LLMs to Unity Catalog using MLflow with the databricks_model_serving environment pack to enable express deployments for custom LLM serving.
tags:
  - unity-catalog
  - mlflow
  - model-registry
timestamp: "2026-06-19T23:02:54.468Z"
---

# [Unity Catalog Model Registration](/concepts/unity-catalog-model-registration.md) for Custom LLMs

**Unity Catalog Model Registration for Custom LLMs** is the step in the custom LLM serving workflow where a model that has been logged with a vLLM-based entrypoint is registered to [Unity Catalog](/concepts/unity-catalog.md) using [MLflow](/concepts/mlflow.md). This registration makes the model available for deployment as a serving endpoint on [Databricks Model Serving](/concepts/databricks-model-serving.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Prerequisites

Before registering a model, you must complete the preceding steps in the custom LLM serving workflow:

- [Set up a serverless GPU notebook](## "see custom_LLM_serving_environment") – use an A10 or H100 GPU depending on model size.
- [Download model weights](## "see custom_LLM_snapshot_download") from Hugging Face or another source.
- [Test the model locally](## "see custom_LLM_local_test") in the notebook using a local vLLM server on a port in the 3000–3999 range.
- [Log the model](## "see custom_LLM_log_model") with a custom entrypoint using `mlflow.log_model()`. The entrypoint must:
  - Set `task = "llm/v1/chat"`.
  - Bind to port 8080 (the port expected by [Model Serving](/concepts/model-serving.md)).
  - Mirror the command you tested locally, substituting `--port 8080` for your local port.
  - Use model paths relative to the [MLflow](/concepts/mlflow.md) model artifacts folder. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

The environment must use [MLflow 3](/concepts/mlflow-3.md).12 or above. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Registration Process

After logging the model, register it to [Unity Catalog](/concepts/unity-catalog.md) with `mlflow.register_model`. To enable custom LLM serving, you must pass the parameter `env_pack="databricks_model_serving"`. This triggers an **express deployment** that packages the model specifically for serving. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

```python
model_version = [[mlflow|MLflow]].register_model(
    model_info.model_uri,
    UC_MODEL_NAME,
    env_pack="databricks_model_serving"
)
```

## After Registration

Once registered, the model version appears in [Unity Catalog](/concepts/unity-catalog.md). You can then [create a serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) for the model, either from the UI or programmatically using the Databricks SDK. The endpoint configuration requires selecting a `workload_type` (e.g., `GPU_MEDIUM`), a `workload_size` (`Small`, `Medium`, or `Large`), and optionally enabling `scale_to_zero_enabled`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

The endpoint automatically appears in the [AI Playground](/concepts/ai-playground.md) after it is ready. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Important Notes

- The `env_pack` parameter is mandatory for custom LLM serving. Omitting it prevents the express deployment from being used. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- Only the chat task (`llm/v1/chat`) is supported, including multimodal models. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- During Beta, autoscaling between more than zero replicas is not supported. Scale-to-zero is supported on all GPU types except `GPU_XLARGE` (1xH100). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance and cataloging layer for data and AI assets.
- [Model Serving](/concepts/model-serving.md) – Infrastructure for deploying models as REST endpoints.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Component that manages model versions and lifecycle.
- vLLM – The inference engine powering custom LLM serving.
- [Express Deployments](/concepts/express-deployments-databricks.md) – Rapid packaging and deployment mechanism used by custom LLM serving.
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) – Broader capability for serving any custom model.

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
