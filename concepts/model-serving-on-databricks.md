---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ddc46fdf0084f6dde6a67d5bab563a5b451959557352bab43de321937edc0343
  pageDirectory: concepts
  sources:
    - computer-vision-databricks-on-aws.md
    - databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - machine-learning-on-databricks-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving-on-databricks
    - MSOD
    - Model Serving (Databricks)
    - Model Serving with Databricks
    - OpenAI Model Serving on Databricks
  citations:
    - file: machine-learning-on-databricks-databricks-on-aws.md
    - file: concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
    - file: best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - file: databricks-foundation-model-apis-databricks-on-aws.md
    - file: mlops-workflows-on-databricks-databricks-on-aws.md
title: Model Serving on Databricks
description: Databricks platform supports deploying trained models (e.g., YOLO) to production via Model Serving, a capability demonstrated in AI Runtime tutorials.
tags:
  - model-serving
  - deployment
  - databricks
  - mlops
timestamp: "2026-06-19T17:49:20.653Z"
---

# Model Serving on Databricks

**Model Serving on Databricks** is a managed inference infrastructure that deploys machine learning models as REST API endpoints for both real-time and batch inference. It provides automatic scaling, GPU acceleration, and enterprise-grade governance through integration with [Unity Catalog](/concepts/unity-catalog.md) and [AI Gateway](/concepts/ai-gateway.md). The platform supports classic ML models, deep learning models, and custom generative AI workloads. ^[machine-learning-on-databricks-databricks-on-aws.md, concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

## Overview

Model Serving allows data scientists and ML engineers to put models into production without provisioning or managing servers. Models are exposed via REST APIs and can be consumed by applications, dashboards, or downstream services. The platform automatically handles scaling, health checks, and failover. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

Databricks supports both batch inference and real-time serving. Batch inference applies models efficiently to large datasets, while real-time serving provides models as low-latency API endpoints. ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Supported Model Types

Model Serving provides a unified interface for several deployment paradigms:

- **Classic ML models** (scikit‑learn, XGBoost, LightGBM) for regression, classification, and forecasting.
- **Deep learning models** (PyTorch, TensorFlow, Hugging Face transformers) for computer vision, NLP, and recommendation systems.
- **Large language models (LLMs)** and custom generative AI models, including fine-tuned models and agent-based architectures.

All model types are served through the same endpoint infrastructure, with GPU instance types allocated automatically when required. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]

## Key Features

### Scalable REST Endpoints

Endpoints scale compute resources up or down based on request volume. Concurrency limits and latency targets can be configured. Models packaged in [MLflow](/concepts/mlflow.md) format are supported natively. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md, machine-learning-on-databricks-databricks-on-aws.md]

### GPU Acceleration

For deep learning and LLM workloads, endpoints can run on GPU instances including [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) and H100 GPUs. This enables low-latency inference for large models without manual GPU scheduling. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md, machine-learning-on-databricks-databricks-on-aws.md]

### Foundation Model APIs

[Foundation Model APIs](/concepts/foundation-model-apis.md) provide access to state-of-the-art open models hosted by Databricks. Two modes are offered:

- **Pay-per-token** – recommended for getting started and evaluation. Not designed for high-throughput production but usable in production.
- **Provisioned throughput** – recommended for all production workloads that require performance guarantees, fine-tuned models, or HIPAA compliance.

The APIs are compatible with OpenAI, so the OpenAI client can be used for querying. ^[databricks-foundation-model-apis-databricks-on-aws.md, machine-learning-on-databricks-databricks-on-aws.md]

### External Models

Databricks supports integrating third-party models hosted outside Databricks (such as GPT-4, Claude, and others) with unified governance and monitoring through the External Models feature. ^[machine-learning-on-databricks-databricks-on-aws.md]

### Unified Governance via AI Gateway

Serving endpoints are governed through [AI Gateway](/concepts/ai-gateway.md). This provides usage tracking (token counts, request numbers), payload logging, rate limits, IP allowlists, and access policies. Real-time serving logs to inference tables governed in Unity Catalog. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

### Batch Inference

Batch inference can be performed using `ai_query` – a SQL function that applies AI to data stored in Databricks. Batch inference applies models efficiently to large datasets without requiring an active endpoint. ^[databricks-foundation-model-apis-databricks-on-aws.md, concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]

### Monitoring and Observability

Production endpoints offer monitoring capabilities including data quality monitoring with custom metrics, dashboards, and alerts. Real-time serving logs to inference tables governed in Unity Catalog. [Genie Code](/concepts/genie-code.md) can help diagnose and investigate serving issues and performance for model serving endpoints. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Deployment Workflow

1. **Register the model** – Models are logged and registered in Unity Catalog as versioned MLflow models, providing lineage and access control. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md]
2. **Choose serving mode** – Select real-time serving (REST endpoint) or batch inference via `ai_query` or Spark jobs. ^[concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md, best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
3. **Configure the endpoint** – Select compute type (CPU/GPU), scaling policy, and concurrency. Databricks provisions and manages the infrastructure. ^[best-practices-for-deep-learning-on-databricks-databricks-on-aws.md]
4. **Deploy and monitor** – The endpoint is available via REST API. Continuous monitoring evaluates model quality and performance.

## MLOps Integration

Model Serving integrates with MLOps workflows. For A/B testing, a single endpoint can serve multiple model versions with traffic splits. Model version aliases (e.g., "Champion" / "Challenger") allow zero-downtime updates. Data, features, models, and endpoints are fully governed by Unity Catalog and AI Gateway. ^[mlops-workflows-on-databricks-databricks-on-aws.md, databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Related Concepts

- [AI Gateway](/concepts/ai-gateway.md) – Governance layer for serving endpoints
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pre-served open-weight models
- [MLflow](/concepts/mlflow.md) – Model packaging and experiment tracking
- Batch Inference – Offline scoring with `ai_query`
- [Custom Model Serving](/concepts/custom-model-serving-endpoint-support.md) – Deploying custom Python models
- [Genie Code](/concepts/genie-code.md) – AI assistant for operations and debugging
- [Unity Catalog](/concepts/unity-catalog.md) – Governance for models and data
- [External Models](/concepts/external-models.md) – Third-party model integration
- [A100 GPU Support on Databricks](/concepts/a100-gpu-support-on-databricks.md) – GPU infrastructure for inference

## Sources

- best-practices-for-deep-learning-on-databricks-databricks-on-aws.md
- concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md
- databricks-data-science-and-ml-capabilities-databricks-on-aws.md
- databricks-foundation-model-apis-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md
- mlops-workflows-on-databricks-databricks-on-aws.md
- computer-vision-databricks-on-aws.md

# Citations

1. [machine-learning-on-databricks-databricks-on-aws.md](/references/machine-learning-on-databricks-databricks-on-aws-34650b43.md)
2. [concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws.md](/references/concepts-data-science-and-machine-learning-on-databricks-databricks-on-aws-6175a64a.md)
3. [best-practices-for-deep-learning-on-databricks-databricks-on-aws.md](/references/best-practices-for-deep-learning-on-databricks-databricks-on-aws-4a84d373.md)
4. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
5. [databricks-foundation-model-apis-databricks-on-aws.md](/references/databricks-foundation-model-apis-databricks-on-aws-f789bf37.md)
6. [mlops-workflows-on-databricks-databricks-on-aws.md](/references/mlops-workflows-on-databricks-databricks-on-aws-a1b056b9.md)
