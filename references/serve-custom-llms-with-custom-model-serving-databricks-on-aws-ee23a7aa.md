---
title: Serve custom LLMs with Custom Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/serve-custom-llms
ingestedAt: "2026-06-18T08:12:47.339Z"
---

This page shows you how to deploy custom large language models (LLMs) on [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) using a [vLLM](https://docs.vllm.ai/) engine. Use this workflow to serve fine-tuned models, PEFT variants, multimodal models, and other foundation models that are not available in [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/) (FMAPI). The [starter notebook](#notebook) at the end of this page contains all runnable code for the following steps.

## When to use custom LLM serving[​](#when-to-use-custom-llm-serving "Direct link to When to use custom LLM serving")

Databricks recommends custom LLM serving when you have one of the following use cases:

*   Fully fine-tuned models with custom weights that you trained on Databricks.
*   Models from Hugging Face that are not available in FMAPI.
*   Custom PEFT recipes that FMAPI does not support.
*   Specialized models outside the FMAPI catalog, such as MedGemma.
*   Multimodal (vision-language) models such as `Qwen/Qwen2.5-VL-3B-Instruct`.
*   Any model that fits on a 1xH100 (80 GB of GPU memory).

## Requirements[​](#requirements "Direct link to Requirements")

*   Custom LLM serving is in Beta. Workspace admins can enable or turn off this feature from the **Previews** page. See [Manage Databricks previews](https://docs.databricks.com/aws/en/admin/workspace-settings/manage-previews).
    
*   [Serverless GPU compute](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/). An A10 GPU is the recommended development environment for smaller models, H100 for larger models.
    
*   MLflow 3.12 or above. The starter notebook pins `mlflow==3.12.0`. If you build your own environment, match this version.
    

## Step 1: Set up your environment[​](#step-1-set-up-your-environment "Direct link to Step 1: Set up your environment")

Create a notebook on serverless GPU compute with an A10 GPU. Install vLLM and its dependencies. The starter notebook pins a tested vLLM version.

You can also specify dependencies through a [serverless environment](https://docs.databricks.com/aws/en/compute/serverless/dependencies) instead of using `%pip install`.

important

Set your working directory to local hard drive (for example, using `tempfile.mkdtemp()`). The `/Workspace` file system does not support large files like model weights.

## Step 2: Download your model[​](#step-2-download-your-model "Direct link to Step 2: Download your model")

Download model weights from Hugging Face with `snapshot_download`. The starter notebook uses `Qwen/Qwen3-4B` as an example, but you can substitute any model that fits your selected GPU's memory budget, including the following:

*   Multimodal models such as `Qwen/Qwen2.5-VL-3B-Instruct` for vision-language use cases.
*   Larger models that fit on a 1xH100, such as `openai/gpt-oss-120b`.

Select a GPU based on your model's memory and performance needs.

## Step 3: Test the model locally with vLLM[​](#step-3-test-the-model-locally-with-vllm "Direct link to Step 3: Test the model locally with vLLM")

Before you deploy, test the model directly in your serverless GPU notebook by launching a local vLLM server. Local testing enables you to verify the model, experiment with vLLM parameters, and troubleshoot issues before you create a serving endpoint.

Key things to know:

*   Serverless GPU compute allows only ports 3000–3999 for local testing. Select a port in that range; the starter notebook uses 3080.
*   The vLLM server exposes an OpenAI-compatible API at `/invocations`.
*   You can test both regular and streaming requests.
*   Tune parameters such as `--dtype`, `--max-model-len`, and `--gpu-memory-utilization` for your model.
*   Add `--enforce-eager` for faster startup, at the cost of some inference performance.
*   For larger models, use an H100 serverless GPU variant for local testing.

When you are satisfied with the configuration, stop the local server before you continue.

## Step 4: Log the model with a custom entrypoint[​](#step-4-log-the-model-with-a-custom-entrypoint "Direct link to Step 4: Log the model with a custom entrypoint")

This step connects your local setup to Model Serving and has the following configuration requirements:

*   The `task` must be `"llm/v1/chat"`.
*   The entrypoint must open on port 8080, the port that Model Serving expects.
*   The entrypoint command must mirror what you tested in Step 3, with port 8080 instead of your local port.
*   The entrypoint launches from the MLflow model artifacts folder, so model paths are relative to that folder.

Python

    metadata = {    "task": "llm/v1/chat",    "entrypoint": (        "python -u -m vllm.entrypoints.openai.api_server "        "--model qwen3 --served-model-name qwen "        "--host 0.0.0.0 --port 8080 "        "--dtype float16 --max-model-len 16384 "        "--gpu-memory-utilization 0.85"    ),}

## Step 5: Register the model to Unity Catalog[​](#step-5-register-the-model-to-unity-catalog "Direct link to Step 5: Register the model to Unity Catalog")

Register the model to Unity Catalog using `mlflow.register_model`. Custom LLM serving depends on [express deployments](https://docs.databricks.com/aws/en/machine-learning/model-serving/express-deployments). Use the `env_pack="databricks_model_serving"` parameter to enable it.

For example, add the following to your notebook:

Python

    model_version = mlflow.register_model(model_info.model_uri, UC_MODEL_NAME, env_pack="databricks_model_serving")

## Step 6: Create a serving endpoint[​](#step-6-create-a-serving-endpoint "Direct link to Step 6: Create a serving endpoint")

[Create the endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) from the UI or programmatically with the Databricks SDK. The key decisions are compute type, workload size, and scale-to-zero behavior.

Select a `workload_type` based on your model and cloud:

`workload_size` (`Small`, `Medium`, or `Large`) controls the number of provisioned replicas behind the endpoint. Use `Small` for development and low-traffic workloads.

The following example shows a typical configuration:

Python

    ServedEntityInput(    entity_name="main.<catalog>.<model_name>",    entity_version="<version>",    workload_type=ServingModelWorkloadType.GPU_MEDIUM,    workload_size="Small",    scale_to_zero_enabled=True,)

### Scale-to-zero and capacity planning[​](#scale-to-zero-and-capacity-planning "Direct link to scale-to-zero-and-capacity-planning")

Custom LLM serving in Beta provisions a fixed number of replicas behind your endpoint. **Autoscaling between more than zero replicas is not yet supported**, so you must size `workload_type` and `workload_size` for your peak traffic. The endpoint queues requests that exceed the capacity of provisioned replicas.

Set `scale_to_zero_enabled=True` to let the endpoint scale down to zero replicas when idle. Cold starts are slow — loading model weights and starting vLLM typically takes one to several minutes.

For latency-sensitive or production-critical workloads, set `scale_to_zero_enabled=False` and size `workload_size` for your peak traffic up front.

warning

**Scale-up capacity is not guaranteed.** Whenever Databricks needs to acquire a new GPU for your endpoint—on creation, on `workload_size` increase, or when an endpoint wakes up from zero—the request can stop responding if the cloud provider has no GPU capacity in your region. This applies to all GPU types but is most constrained for `GPU_XLARGE` (H100). Databricks mitigates this with warm pools and prereservation, which keep GPU capacity available and ready.

`GPU_XLARGE` (1xH100) endpoints do not support `scale_to_zero_enabled=True` during Beta. H100 capacity is too constrained to guarantee a successful cold-start scale-up.

## Step 7: Query your endpoint[​](#step-7-query-your-endpoint "Direct link to Step 7: Query your endpoint")

After the endpoint is ready, it appears automatically in the [AI Playground](https://docs.databricks.com/aws/en/large-language-models/ai-playground) from the endpoint's page. You can also query it [programmatically](https://docs.databricks.com/aws/en/machine-learning/model-serving/score-custom-model-endpoints) using the Databricks SDK, the OpenAI SDK, or curl.

*   Databricks SDK
*   OpenAI SDK
*   curl

Python

    w.serving_endpoints.query(    name="<endpoint-name>",    messages=[ChatMessage(role=ChatMessageRole.USER, content="Hello")],)

## Monitor your endpoint[​](#monitor-your-endpoint "Direct link to Monitor your endpoint")

Custom LLM serving uses the same observability infrastructure as standard [custom model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-models) endpoints, but with a few vLLM-specific extras described in the following sections.

### Live logs[​](#live-logs "Direct link to Live logs")

The **Logs** tab of the endpoint page in the Serving UI shows `stdout` and `stderr` from your vLLM process in real time. You can also open this output through the [logs API](https://docs.databricks.com/api/workspace/servingendpoints/logs).

### Persisted logs and metrics[​](#persisted-logs-and-metrics "Direct link to Persisted logs and metrics")

When telemetry is enabled, both logs and metrics are persisted to Unity Catalog Delta tables for long-term retention, SQL querying, and compliance. See [Persist custom model serving data to Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs) for full setup instructions, requirements, and table schemas.

For custom LLM serving specifically:

*   **Logs**: `stdout` and `stderr` from the vLLM process are captured automatically. No application-side logging code is required.
*   **Metrics**: Databricks automatically scrapes the vLLM server's Prometheus `/metrics` endpoint and persists the metrics alongside logs. By default, you get per-request latency, throughput, token counts, queue depth, and KV-cache utilization.

### Query telemetry data[​](#query-telemetry-data "Direct link to Query telemetry data")

During Beta, there is no UI for visualizing logs or metrics. Query the persisted data directly in Unity Catalog using SQL or a notebook. See the metric and log schemas documented in [Persist custom model serving data to Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/model-serving/custom-model-serving-uc-logs).

The following notebook shows how to parse and visualize the persisted vLLM metrics:

#### Custom LLM serving metrics notebook

## Example notebook[​](#example-notebook "Direct link to Example notebook")

Develop and test the model in a [serverless GPU](https://docs.databricks.com/aws/en/machine-learning/ai-runtime/) notebook, then log and deploy the same configuration as a serving endpoint. The following notebook contains the complete runnable flow from this guide.

#### Custom LLM serving starter notebook

## Limitations[​](#limitations "Direct link to Limitations")

The following limitations apply during Beta.

*   `GPU_XLARGE` (1xH100) endpoints are available only in `us-west-2` and require additional enrollment with your Databricks account team. They do not enable scale-to-zero during Beta.
*   No autoscaling between replicas. Scale-to-zero is supported on all GPU types except `GPU_XLARGE`. See [Scale-to-zero and capacity planning](#scale-to-zero) for cloud-provider capacity caveats.
*   Only the LLM chat task (`llm/v1/chat`) is supported, including multimodal.
*   No route optimization.
*   No UI for visualizing logs or metrics. Query telemetry directly in Unity Catalog.

Reach out to your Databricks account team for feedback or questions.
