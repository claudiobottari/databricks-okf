---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9f78540791da6575f26a10594862a11318f5087ad6df5aa977007fb74f4a2990
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - vllm-engine-integration-for-model-serving
    - VEIFMS
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: vLLM Engine Integration for Model Serving
description: The use of vLLM as the inference engine powering custom LLM deployments on Databricks, including local testing, entrypoint configuration, and OpenAI-compatible API at /invocations.
tags:
  - vllm
  - inference-engine
  - model-serving
timestamp: "2026-06-19T23:02:26.007Z"
---

# vLLM Engine Integration for [Model Serving](/concepts/model-serving.md)

**vLLM Engine Integration for Model Serving** is a Databricks feature (currently in Beta) that allows you to deploy custom large language models (LLMs) on [Model Serving](/concepts/model-serving.md) using a vLLM inference engine. This integration is designed for models that are not available through [Foundation Model APIs](/concepts/foundation-model-apis.md) (FMAPI), such as fully fine-tuned models, PEFT variants, multimodal (vision-language) models, and any foundation model that fits on a single H100 GPU (80 GB of GPU memory). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## When to Use Custom LLM Serving

Databricks recommends custom LLM serving for the following use cases:

- Fully fine-tuned models with custom weights trained on Databricks.
- Models from Hugging Face that are not available in FMAPI.
- Custom PEFT recipes that FMAPI does not support.
- Specialized models outside the FMAPI catalog (e.g., MedGemma).
- Multimodal models such as `Qwen/Qwen2.5-VL-3B-Instruct`.
- Any model that fits on a 1xH100 (80 GB of GPU memory). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Requirements

- Custom LLM serving is in Beta. Workspace admins can enable or turn off the feature from the **Previews** page.
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) is required. Databricks recommends an A10 GPU as the development environment for smaller models and an H100 for larger models.
- [MLflow](/concepts/mlflow.md) version 3.12 or above. The starter notebook pins `mlflow==3.12.0`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Workflow Overview

### 1. Set Up the Environment

Create a notebook on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) (A10 or H100). Install vLLM and its dependencies. Dependencies can also be specified through a [serverless environment configuration](/concepts/serverless-environment-versioning.md). The working directory must be on the local hard drive (e.g., using `tempfile.mkdtemp()`), because the `/Workspace` file system does not support large files like model weights. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 2. Download the Model

Download model weights from Hugging Face using `snapshot_download`. The example notebook uses `Qwen/Qwen3-4B`, but any model that fits the selected GPU’s memory budget can be substituted, including multimodal models or larger models that fit on a 1xH100. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 3. Test the Model Locally with vLLM

Launch a local vLLM server directly in the serverless GPU notebook to test the model before deployment. Key points:

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) allows only ports **3000–3999** for local testing.
- The vLLM server exposes an OpenAI-compatible API at `/invocations`.
- Both regular and streaming requests can be tested.
- Parameters such as `--dtype`, `--max-model-len`, and `--gpu-memory-utilization` can be tuned for the model.
- Adding `--enforce-eager` speeds up startup at the cost of some inference performance.
- For larger models, use an H100 serverless GPU variant.

Stop the local server before proceeding to the next step. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 4. Log the Model with a Custom Entrypoint

Log the model to [Unity Catalog](/concepts/unity-catalog.md) via [MLflow](/concepts/mlflow.md) with a custom entrypoint. The configuration requirements are:

- The `task` must be `"llm/v1/chat"`.
- The entrypoint must open on **port 8080**, the port that [Model Serving](/concepts/model-serving.md) expects.
- The entrypoint command should mirror the local test configuration, using port 8080 instead of the local port.
- Model paths in the entrypoint are relative to the [MLflow](/concepts/mlflow.md) model artifacts folder.

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

### 5. Register the Model to [Unity Catalog](/concepts/unity-catalog.md)

Register the logged model to [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.register_model` with the `env_pack="databricks_model_serving"` parameter. This enables [express deployments](/concepts/express-deployments-databricks.md) for the custom LLM.

```python
model_version = [[mlflow|MLflow]].register_model(model_info.model_uri, UC_MODEL_NAME, env_pack="databricks_model_serving")
```

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 6. Create a Serving Endpoint

Create a serving endpoint from the UI or programmatically using the Databricks SDK. Key decisions include compute type, workload size, and scale-to-zero behavior.

- `workload_type` is selected based on model and cloud provider (e.g., `GPU_MEDIUM`).
- `workload_size` (`Small`, `Medium`, `Large`) controls the number of provisioned replicas. Use `Small` for development and low-traffic workloads.
- `scale_to_zero_enabled=True` allows the endpoint to scale down to zero replicas when idle, but cold starts (loading model weights and starting vLLM) typically take one to several minutes.

**Capacity planning note:** During Beta, custom LLM serving provisions a fixed number of replicas; **autoscaling between more than zero replicas is not yet supported**. The endpoint queues requests that exceed the provisioned capacity. For latency-sensitive or production-critical workloads, set `scale_to_zero_enabled=False` and size `workload_size` for peak traffic upfront. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

**GPU_XLARGE (1xH100) endpoints** do not support scale-to-zero during Beta because H100 capacity is too constrained to guarantee successful cold-start scale-up. These endpoints are available only in `us-west-2` and require additional enrollment with the Databricks account team. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 7. Query the Endpoint

Once the endpoint is ready, it appears automatically in the [AI Playground](/concepts/ai-playground.md). It can also be queried programmatically using the Databricks SDK, the OpenAI SDK, or curl.

```python
w.serving_endpoints.query(
    name="<endpoint-name>",
    messages=[ChatMessage(role=ChatMessageRole.USER, content="Hello")],
)
```

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Monitoring

Custom LLM serving uses the same observability infrastructure as standard custom [Model Serving](/concepts/model-serving.md), with additional vLLM-specific capabilities:

- **Live logs**: The **Logs** tab of the endpoint page shows `stdout` and `stderr` from the vLLM process in real time. The same output can be retrieved through the Serving Endpoint Logs API.
- **Persisted logs and metrics**: When telemetry is enabled, logs and metrics are persisted to [Unity Catalog](/concepts/unity-catalog.md) Delta tables. vLLM’s Prometheus `/metrics` endpoint is automatically scraped by Databricks, capturing per-request latency, throughput, token counts, queue depth, and KV-cache utilization.
- **Querying telemetry data**: During Beta there is no UI for visualizing logs or metrics; users query the persisted data directly in [Unity Catalog](/concepts/unity-catalog.md) using SQL or a notebook. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Limitations (Beta)

- `GPU_XLARGE` (1xH100) endpoints are available only in `us-west-2` and do not enable scale-to-zero. Additional enrollment is required.
- No autoscaling between replicas. Scale-to-zero is supported on all GPU types except `GPU_XLARGE` (subject to cloud-provider capacity).
- Only the LLM chat task (`llm/v1/chat`) is supported, including multimodal inputs.
- No route optimization.
- No UI for visualizing logs or metrics; query telemetry directly in [Unity Catalog](/concepts/unity-catalog.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- vLLM
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [MLflow](/concepts/mlflow.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- Prometheus
- [AI Playground](/concepts/ai-playground.md)
- [Express Deployments](/concepts/express-deployments-databricks.md)
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
