---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dd4569bfda1ec1e21ff040e92928226722cce6932d75484ab9244d114031d64c
  pageDirectory: concepts
  sources:
    - serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-endpoint-configuration-for-custom-llms
    - SECFCL
  citations:
    - file: serve-custom-llms-with-custom-model-serving-databricks-on-aws.md
title: Serving Endpoint Configuration for Custom LLMs
description: The configuration decisions for creating a custom LLM serving endpoint on Databricks, including workload_type (GPU selection), workload_size (Small/Medium/Large), and programmatic creation via Databricks SDK.
tags:
  - endpoint-configuration
  - deployment
  - databricks-sdk
timestamp: "2026-06-19T23:02:37.705Z"
---

# Serving Endpoint Configuration for Custom LLMs

**Serving Endpoint Configuration for Custom LLMs** refers to the process of deploying and configuring custom large language models (LLMs) on [Databricks Model Serving](/concepts/databricks-model-serving.md) using a vLLM engine. This workflow enables serving fine-tuned models, PEFT variants, multimodal models, and other foundation models not available through [Foundation Model APIs](/concepts/foundation-model-apis.md) (FMAPI). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## When to Use Custom LLM Serving

Custom LLM serving is recommended for the following use cases:

- Fully fine-tuned models with custom weights trained on Databricks
- Models from Hugging Face that are not available in FMAPI
- Custom PEFT recipes that FMAPI does not support
- Specialized models outside the FMAPI catalog, such as MedGemma
- Multimodal (vision-language) models such as `Qwen/Qwen2.5-VL-3B-Instruct`
- Any model that fits on a 1xH100 (80 GB of GPU memory)

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Requirements

Custom LLM serving is in Beta. Workspace admins can enable or disable this feature from the **Previews** page. Additional requirements include:

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) — An A10 GPU is recommended for smaller models, H100 for larger models
- [MLflow 3](/concepts/mlflow-3.md).12 or above

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Configuration Steps

### Step 1: Set Up Your Environment

Create a notebook on [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) with an A10 GPU. Install vLLM and its dependencies. Set your working directory to a local hard drive (for example, using `tempfile.mkdtemp()`), as the `/Workspace` file system does not support large files like model weights. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Step 2: Download Your Model

Download model weights from Hugging Face using `snapshot_download`. You can substitute any model that fits your selected GPU's memory budget, including multimodal models and larger models that fit on a 1xH100. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Step 3: Test the Model Locally with vLLM

Before deployment, test the model directly in your serverless GPU notebook by launching a local vLLM server. Key considerations:

- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md) allows only ports 3000–3999 for local testing
- The vLLM server exposes an OpenAI-compatible API at `/invocations`
- You can test both regular and streaming requests
- Tune parameters such as `--dtype`, `--max-model-len`, and `--gpu-memory-utilization`
- Add `--enforce-eager` for faster startup, at the cost of some inference performance

Stop the local server before continuing to deployment. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Step 4: Log the Model with a Custom Entrypoint

To connect your local setup to [Model Serving](/concepts/model-serving.md), log the model with specific configuration requirements:

- The `task` must be `"llm/v1/chat"`
- The entrypoint must open on port 8080, the port that [Model Serving](/concepts/model-serving.md) expects
- The entrypoint command must mirror what you tested locally, with port 8080 instead of your local port
- The entrypoint launches from the [MLflow](/concepts/mlflow.md) model artifacts folder, so model paths are relative to that folder

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

### Step 5: Register the Model to [Unity Catalog](/concepts/unity-catalog.md)

Register the model to [Unity Catalog](/concepts/unity-catalog.md) using `mlflow.register_model`. Custom LLM serving depends on [express deployments](/concepts/express-deployments-databricks.md). Use the `env_pack="databricks_model_serving"` parameter to enable it. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

```python
model_version = [[mlflow|MLflow]].register_model(
    model_info.model_uri, 
    UC_MODEL_NAME, 
    env_pack="databricks_model_serving"
)
```

### Step 6: Create a Serving Endpoint

Create the endpoint from the UI or programmatically with the Databricks SDK. The key configuration decisions are compute type, workload size, and [scale-to-zero behavior](/concepts/scale-to-zero-in-model-serving.md). ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

Select a `workload_type` based on your model and cloud. The `workload_size` (`Small`, `Medium`, or `Large`) controls the number of provisioned replicas behind the endpoint. Use `Small` for development and low-traffic workloads. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

```python
ServedEntityInput(
    entity_name="main.<catalog>.<model_name>",
    entity_version="<version>",
    workload_type=ServingModelWorkloadType.GPU_MEDIUM,
    workload_size="Small",
    scale_to_zero_enabled=True,
)
```

### Step 7: Query Your Endpoint

After the endpoint is ready, it appears automatically in the [AI Playground](/concepts/ai-playground.md). You can also query it programmatically using the Databricks SDK, the OpenAI SDK, or curl. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

```python
w.serving_endpoints.query(
    name="<endpoint-name>",
    messages=[ChatMessage(role=ChatMessageRole.USER, content="Hello")],
)
```

## Scale-to-Zero and Capacity Planning

Custom LLM serving in Beta provisions a fixed number of replicas behind your endpoint. **Autoscaling between more than zero replicas is not yet supported**, so you must size `workload_type` and `workload_size` for your peak traffic. The endpoint queues requests that exceed the capacity of provisioned replicas. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

Set `scale_to_zero_enabled=True` to let the endpoint scale down to zero replicas when idle. Cold starts are slow — loading model weights and starting vLLM typically takes one to several minutes. For latency-sensitive or production-critical workloads, set `scale_to_zero_enabled=False` and size `workload_size` for your peak traffic up front. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

**Scale-up capacity is not guaranteed.** Whenever Databricks needs to acquire a new GPU for your endpoint, the request can stop responding if the cloud provider has no GPU capacity in your region. This applies to all GPU types but is most constrained for `GPU_XLARGE` (H100). Databricks mitigates this with warm pools and prereservation, which keep GPU capacity available and ready. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

`GPU_XLARGE` (1xH100) endpoints do not support `scale_to_zero_enabled=True` during Beta due to constrained H100 capacity. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Monitoring

Custom LLM serving uses the same observability infrastructure as standard [custom model serving](/concepts/custom-model-serving-endpoint-support.md) endpoints, with vLLM-specific extras. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Live Logs

The **Logs** tab of the endpoint page in the [Serving UI](/concepts/serving-ui.md) shows `stdout` and `stderr` from your vLLM process in real time. You can also access this output through the logs API. ^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

### Persisted Logs and Metrics

When telemetry is enabled, both logs and metrics are persisted to [Unity Catalog](/concepts/unity-catalog.md) Delta tables for long-term retention, SQL querying, and compliance. For custom LLM serving specifically:

- **Logs**: `stdout` and `stderr` from the vLLM process are captured automatically
- **Metrics**: Databricks automatically scrapes the vLLM server's Prometheus `/metrics` endpoint and persists the metrics alongside logs, providing per-request latency, throughput, token counts, queue depth, and KV-cache utilization

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Beta Limitations

The following limitations apply during Beta:

- `GPU_XLARGE` (1xH100) endpoints are available only in `us-west-2` and require additional enrollment
- No autoscaling between replicas
- Scale-to-zero is supported on all GPU types except `GPU_XLARGE`
- Only the LLM chat task (`llm/v1/chat`) is supported, including multimodal
- No route optimization
- No UI for visualizing logs or metrics — query telemetry directly in [Unity Catalog](/concepts/unity-catalog.md)

^[serve-custom-llms-with-custom-model-serving-databricks-on-aws.md]

## Related Concepts

- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- vLLM
- [Unity Catalog](/concepts/unity-catalog.md)
- [Express Deployments](/concepts/express-deployments-databricks.md)
- [Serverless GPU Compute](/concepts/serverless-gpu-compute.md)
- [MLflow](/concepts/mlflow.md)
- [AI Playground](/concepts/ai-playground.md)

## Sources

- serve-custom-llms-with-custom-model-serving-databricks-on-aws.md

# Citations

1. [serve-custom-llms-with-custom-model-serving-databricks-on-aws.md](/references/serve-custom-llms-with-custom-model-serving-databricks-on-aws-ee23a7aa.md)
