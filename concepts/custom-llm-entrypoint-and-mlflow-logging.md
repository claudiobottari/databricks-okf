---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8f4e30b7b5e4860be4ab128fb782942112ecc6c9ff1553c5ee8d9a22ca2a4d8d
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-entrypoint-and-mlflow-logging
    - MLflow Logging and Custom LLM Entrypoint
    - CLEAML
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Custom LLM Entrypoint and MLflow Logging
description: The technique of logging a custom LLM with a custom entrypoint in MLflow, specifying the task as llm/v1/chat and configuring the vLLM server to listen on port 8080 for Model Serving compatibility.
tags:
  - mlflow
  - entrypoint
  - model-logging
timestamp: "2026-06-19T23:02:41.521Z"
---

# Custom LLM Entrypoint and [MLflow](/concepts/mlflow.md) Logging

**Custom LLM Entrypoint and [MLflow](/concepts/mlflow.md) Logging** refers to the process of configuring and logging a custom large language model (LLM) with a user-defined entrypoint command for deployment on [Databricks Model Serving](/concepts/databricks-model-serving.md). This approach enables serving fine-tuned models, PEFT variants, multimodal models, and other foundation models not available through [Foundation Model APIs](/concepts/foundation-model-apis.md).

## Overview

When deploying custom LLMs on [Databricks Model Serving](/concepts/databricks-model-serving.md), you must log the model with a custom entrypoint that defines how the model server should start. The entrypoint specifies the command that launches the [Model Serving](/concepts/model-serving.md) engine — typically vLLM — with the appropriate configuration parameters. This entrypoint is stored as metadata alongside the model in [MLflow](/concepts/mlflow.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Entrypoint Configuration

The custom entrypoint must meet specific requirements for compatibility with [Model Serving](/concepts/model-serving.md):

- The `task` must be set to `"llm/v1/chat"`.
- The entrypoint must open on port **8080**, which is the port that [Model Serving](/concepts/model-serving.md) expects.
- The entrypoint command should mirror the configuration tested locally in Step 3 of the deployment workflow, with port 8080 substituted for the local testing port.
- The entrypoint launches from the [MLflow](/concepts/mlflow.md) model artifacts folder, so model paths are relative to that folder. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Example Entrypoint Metadata

```python
metadata = {
    "task": "llm/v1/chat",
    "entrypoint": (
        "python -u -m vllm.entrypoints.openai.api_server "
        "--model qwen3 --served-model-name qwen "
        "--host 0.0.0.0 --port 8080 "
        "--dtype float16 --max-model-len 16384 "
        "--gpu-memory-utilization 0.85"
    ),
}
```

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## [MLflow](/concepts/mlflow.md) Logging Requirements

To log a custom LLM for serving, the following requirements apply:

- **MLflow version 3.12 or above** is required. The starter notebook pins `mlflow==3.12.0`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- The model must be registered to [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.register_model`.
- Custom LLM serving depends on [Express Deployments](/concepts/express-deployments-databricks.md). Use the `env_pack="databricks_model_serving"` parameter when registering the model to enable this. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Registration Example

```python
model_version = [[mlflow|MLflow]].register_model(
    model_info.model_uri,
    UC_MODEL_NAME,
    env_pack="databricks_model_serving"
)
```

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Workflow Steps

The complete workflow for custom LLM entrypoint and [MLflow](/concepts/mlflow.md) logging follows these steps:

1. **Set up environment**: Create a notebook on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) with an A10 or H100 GPU. Install vLLM and its dependencies. Set the working directory to a local hard drive path (e.g., using `tempfile.mkdtemp()`), as the `/Workspace` file system does not support large files like model weights. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

2. **Download model**: Download model weights from Hugging Face using `snapshot_download`. Select a GPU based on the model's memory and performance needs. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

3. **Test locally**: Launch a local vLLM server in the notebook to verify the model and experiment with parameters. [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) allows only ports 3000–3999 for local testing. The vLLM server exposes an OpenAI-compatible API at `/invocations`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

4. **Log with custom entrypoint**: Define the metadata dictionary with the `task` and `entrypoint` fields, then log the model using [MLflow](/concepts/mlflow.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

5. **Register to Unity Catalog**: Register the model with `mlflow.register_model` and the `env_pack` parameter. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

6. **Create serving endpoint**: Create the endpoint from the UI or programmatically using the Databricks SDK. Select the appropriate `workload_type` and `workload_size`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Supported Models

Custom LLM entrypoint and [MLflow](/concepts/mlflow.md) logging supports:

- Fully fine-tuned models with custom weights trained on Databricks.
- Models from Hugging Face not available in [Foundation Model APIs](/concepts/foundation-model-apis.md).
- Custom PEFT recipes.
- Specialized models outside the FMAPI catalog, such as MedGemma.
- Multimodal (vision-language) models such as `Qwen/Qwen2.5-VL-3B-Instruct`.
- Any model that fits on a 1xH100 (80 GB of GPU memory). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Limitations

During Beta, the following limitations apply:

- Only the LLM chat task (`llm/v1/chat`) is supported, including multimodal.
- No autoscaling between replicas. Scale-to-zero is supported on all GPU types except `GPU_XLARGE` (1xH100).
- `GPU_XLARGE` endpoints are available only in `us-west-2` and require additional enrollment.
- No route optimization.
- No UI for visualizing logs or metrics. Query telemetry directly in [Unity Catalog](/concepts/unity-catalog.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) — The infrastructure for deploying [Custom Models on Databricks](/concepts/custom-models-databricks.md).
- vLLM — The inference engine used for serving custom LLMs.
- [Express Deployments](/concepts/express-deployments-databricks.md) — The deployment mechanism that custom LLM serving depends on.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — The compute environment for developing and testing custom LLMs.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) — The alternative for models already available in the Databricks catalog.
- [Unity Catalog](/concepts/unity-catalog.md) — The governance and catalog system for registering models.
- [MLflow](/concepts/mlflow.md) — The platform for managing the [ML Lifecycle](/concepts/ml-lifecycle.md), including model logging and registration.

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
