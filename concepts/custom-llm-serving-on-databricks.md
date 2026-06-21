---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1826dce16e814455ed1f5b42a1301abd2e82077ae8d6bb014ec93fdca290616
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-serving-on-databricks
    - CLSOD
    - Custom model serving on Databricks
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Custom LLM Serving on Databricks
description: A workflow for deploying custom large language models on Databricks Model Serving using a vLLM engine, supporting fine-tuned models, PEFT variants, multimodal models, and foundation models not available in FMAPI.
tags:
  - model-serving
  - llm
  - databricks
timestamp: "2026-06-19T23:02:24.912Z"
---

# Custom LLM Serving on Databricks

**Custom LLM Serving** enables deployment of custom large language models (LLMs) on [Databricks Model Serving](/concepts/databricks-model-serving.md) using a vLLM engine. This workflow is intended for models that are not available through [Foundation Model APIs](/concepts/foundation-model-apis.md) (FMAPI), such as fine‑tuned variants, PEFT adapters, multimodal (vision‑language) models, and other foundation models that fit within a single GPU’s memory budget. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## When to Use Custom LLM Serving

Custom LLM serving is recommended when you have one of the following use cases:
- Fully fine-tuned models with custom weights that you trained on Databricks.
- Models from Hugging Face that are not available in FMAPI.
- Custom PEFT recipes that FMAPI does not support.
- Specialized models outside the FMAPI catalog, such as MedGemma.
- Multimodal (vision‑language) models such as `Qwen/Qwen2.5-VL-3B-Instruct`.
- Any model that fits on a 1×H100 (80 GB of GPU memory).

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Requirements

- Custom LLM serving is in Beta. Workspace admins can enable or disable the feature from the **Previews** page. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) is required. An A10 GPU is recommended for smaller models; an H100 for larger models. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]
- [MLflow 3](/concepts/mlflow-3.md).12 or above must be used. The starter notebook pins `mlflow==3.12.0`. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Deployment Steps

The deployment process consists of six main steps, which are available as a runnable starter notebook.

### 1. Set Up Your Environment
Create a notebook on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) with an A10 GPU and install vLLM and its dependencies. The working directory must be set to the local hard drive (e.g., using `tempfile.mkdtemp()`) because the `/Workspace` file system does not support large model weight files. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 2. Download Your Model
Download model weights from Hugging Face using `snapshot_download`. The example model is `Qwen/Qwen3-4B`, but any model fitting the GPU memory budget can be substituted, including multimodal models (e.g., `Qwen/Qwen2.5-VL-3B-Instruct`) or larger models that fit on a 1×H100 (e.g., `openai/gpt-oss-120b`). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 3. Test the Model Locally with vLLM
Before deploying, launch a local vLLM server inside the serverless GPU notebook. Local testing allows you to verify the model and tune vLLM parameters. Key points:
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) only allows ports 3000–3999 for local testing; the starter notebook uses port 3080.
- The vLLM server exposes an OpenAI‑compatible API at `/invocations`.
- Parameters such as `--dtype`, `--max-model-len`, and `--gpu-memory-utilization` can be adjusted.
- Adding `--enforce-eager` speeds up startup at the cost of some inference performance.
- For larger models, use an H100 serverless GPU variant.

Stop the local server before proceeding. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 4. Log the Model with a Custom Entrypoint
The model must be logged to [MLflow](/concepts/mlflow.md) with a custom entrypoint that connects to [Model Serving](/concepts/model-serving.md). Configuration requirements:
- The `task` must be `"llm/v1/chat"`.
- The entrypoint must open on port 8080, the port that [Model Serving](/concepts/model-serving.md) expects.
- The command mirrors what was tested locally, but uses port 8080 and relative paths from the [MLflow](/concepts/mlflow.md) model artifacts folder.

Example metadata:
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
Register the model to [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.register_model`. Custom LLM serving depends on [Express Deployments](/concepts/express-deployments-databricks.md). Use the `env_pack="databricks_model_serving"` parameter to enable this. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 6. Create a Serving Endpoint
Create the serving endpoint from the UI or programmatically with the Databricks SDK. Key decisions:
- **Workload type** (e.g., `GPU_MEDIUM`) and **workload size** (`Small`, `Medium`, `Large`) control the number of provisioned replicas.
- **Scale‑to‑zero** can be enabled to let the endpoint scale down to zero when idle.

> **Important**: Custom LLM serving in Beta provisions a fixed number of replicas; autoscaling between more than zero replicas is not yet supported. Endpoints queue requests that exceed provisioned capacity. Scale‑to‑zero is supported on all GPU types except `GPU_XLARGE` (1×H100). For latency‑sensitive or production workloads, set `scale_to_zero_enabled=False` and size for peak traffic upfront.

Example configuration:
```python
ServedEntityInput(
    entity_name="main.<catalog>.<model_name>",
    entity_version="<version>",
    workload_type=ServingModelWorkloadType.GPU_MEDIUM,
    workload_size="Small",
    scale_to_zero_enabled=True,
)
```
^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### 7. Query Your Endpoint
After the endpoint is ready, it appears automatically in the [AI Playground](/concepts/ai-playground.md). It can also be queried programmatically using the Databricks SDK, OpenAI SDK, or curl. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Monitoring and Observability

Custom LLM serving uses the same observability infrastructure as standard custom [Model Serving](/concepts/model-serving.md), with vLLM‑specific additions. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Live Logs
The **Logs** tab of the endpoint page shows `stdout` and `stderr` from the vLLM process in real time. These logs are also accessible via the Logs API. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Persisted Logs and Metrics
When telemetry is enabled, logs and metrics are persisted to [Unity Catalog](/concepts/unity-catalog.md) Delta tables for long‑term retention and SQL querying. For custom LLM serving:
- **Logs**: `stdout` and `stderr` are captured automatically.
- **Metrics**: Databricks automatically scrapes the vLLM server’s Prometheus `/metrics` endpoint and persists per‑request latency, throughput, token counts, queue depth, and KV‑cache utilization.

During Beta, there is no UI for visualizing logs or metrics; data must be queried directly in [Unity Catalog](/concepts/unity-catalog.md) using SQL or a notebook. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Limitations (Beta)

- `GPU_XLARGE` (1×H100) endpoints are available only in `us-west-2` and require additional enrollment with the Databricks account team. Scale‑to‑zero is not enabled on this GPU type during Beta.
- No autoscaling between replicas. Scale‑to‑zero is supported on all GPU types except `GPU_XLARGE`.
- Only the LLM chat task (`llm/v1/chat`) is supported, including multimodal.
- No route optimization.
- No UI for visualizing logs or metrics.

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

## Related Concepts

- [Model Serving](/concepts/model-serving.md)
- vLLM
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow](/concepts/mlflow.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Express Deployments](/concepts/express-deployments-databricks.md)
- [AI Playground](/concepts/ai-playground.md)

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
