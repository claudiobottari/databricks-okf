---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cf471f38a3c9a57ccea6e732d12418e92c5aff90619afba7b4f2b6d4ff4b70a1
  pageDirectory: concepts
  sources:
    - best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-for-deep-learning-model-lifecycle
    - MFDLML
  citations:
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
title: MLflow for Deep Learning Model Lifecycle
description: Integrated MLflow support in Databricks for tracking model development, autologging, model deployment, and serving — enabling management of deep learning models including custom preprocessing logic across batch, streaming, and online inference.
tags:
  - mlflow
  - model-management
  - deep-learning
timestamp: "2026-06-19T14:10:04.002Z"
---

Here is the wiki page for "MLflow for Deep Learning Model Lifecycle", written based solely on the provided source material.

---

# MLflow for Deep Learning Model Lifecycle

**MLflow for Deep Learning Model Lifecycle** refers to the use of [MLflow](/concepts/mlflow.md) to manage the end‑to‑end lifecycle of deep learning models on Databricks, from experiment tracking and model logging to deployment and serving. Databricks Runtime for Machine Learning (Databricks Runtime ML) includes built‑in deep learning libraries (TensorFlow, PyTorch, Keras) and integrates MLflow as the central tool for tracking, packaging, and deploying models. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Tracking Deep Learning Training

Databricks recommends using [MLflow Tracking](/concepts/mlflow-tracking.md) and [Databricks Autologging](/concepts/databricks-autologging.md) for all model training. Autologging automatically captures parameters, metrics, and artifacts without manual logging calls, making it easy to reproduce and compare deep learning experiments. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Monitoring with TensorBoard

TensorBoard is pre‑installed in Databricks Runtime ML and can be used within a notebook or a separate tab to visualize training progress. Cluster metrics (network, processor, memory, GPU usage) are also available to inspect for bottlenecks. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Model Logging and Registration

MLflow can log any deep learning model, including custom preprocessing and postprocessing logic. This ensures the full inference pipeline is captured in a single deployable artifact. Models can be registered in [Models in Unity Catalog](/concepts/models-in-unity-catalog.md) or in the [Workspace Model Registry](/concepts/workspace-model-registry.md) for centralized governance and versioning. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Deployment Options

### Online Serving

For low‑latency inference, Databricks [Model Serving](/concepts/model-serving.md) provides a unified REST API interface. It supports three categories of models:

- **Custom models** — Python models packaged in the MLflow format (e.g., PyTorch, Hugging Face, scikit‑learn).
- **Foundation Model APIs** — state‑of‑the‑art open models (e.g., Meta‑Llama, Gemma) available with pay‑per‑token or provisioned throughput.
- **External models** — models hosted outside Databricks (e.g., OpenAI, Anthropic) that can be centrally governed with rate limits and access controls.

Alternatively, MLflow provides APIs for deploying to various managed services for online inference, as well as APIs for creating Docker containers for custom serving solutions. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

### Batch and Streaming Inference

Batch and streaming inference leverage Spark for high‑throughput, low‑cost scoring. When a model is logged from Databricks, MLflow automatically provides inference code to apply the model as a Spark Pandas UDF. This scales inference across a cluster. For large deep learning models, further optimization is possible (see the reference solution for image ETL). ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Best Practices

- **Use Databricks Runtime ML** to get pre‑configured GPU support, deep learning libraries, and integrated MLflow out of the box. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Start with a Single Node GPU cluster** for fast iterative development; move to distributed training (e.g., TorchDistributor, DeepSpeed, Ray) when data size warrants it. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Separate ETL from inference**: preprocess data into a [Delta Lake Table](/concepts/delta-lake-table.md) before running inference so costs are shared across multiple reads, and use different hardware for ETL (CPUs) and inference (GPUs) to optimize cost and performance. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
- **Optimize batch size and learning rate** together, and use early stopping to avoid unnecessary epochs. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- [MLflow Model Registry](/concepts/mlflow-model-registry.md)
- [Databricks Runtime for Machine Learning](/concepts/databricks-runtime-for-machine-learning.md)
- [Databricks Autologging](/concepts/databricks-autologging.md)
- [Model Serving](/concepts/model-serving.md)
- [Models in Unity Catalog](/concepts/models-in-unity-catalog.md)
- Spark Pandas UDFs

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md

# Citations

1. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
