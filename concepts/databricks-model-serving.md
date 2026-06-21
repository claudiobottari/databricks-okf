---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0e9380cfd5013f2e832290cc21ed0780cf6a912093a87c74d14881967884e924
  pageDirectory: concepts
  sources:
    - deploy-models-for-batch-inference-and-prediction-databricks-on-aws.md
    - deploy-models-using-model-serving-databricks-on-aws.md
    - how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
    - migrate-to-model-serving-databricks-on-aws.md
    - mlflow-on-databricks-databricks-on-aws.md
    - structured-outputs-on-databricks-databricks-on-aws.md
    - tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
    - use-features-in-online-workflows-databricks-on-aws.md
  confidence: 0.7
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-model-serving
    - DMS
    - Validate with model serving
  citations:
    - file: deploy-models-using-model-serving-databricks-on-aws.md
    - file: databricks-data-science-and-ml-capabilities-databricks-on-aws.md
    - file: tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md
    - file: supported-foundation-models-on-model-serving-databricks-on-aws.md
    - file: how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
title: Databricks Model Serving
description: Databricks' real-time model serving solution, distinct from batch inference, for deploying models for low-latency predictions
tags:
  - databricks
  - model-serving
  - deployment
  - machine-learning
timestamp: "2026-06-19T18:30:59.629Z"
---

# Databricks Model Serving

**Databricks Model Serving** is the platform's unified solution for deploying, governing, and querying AI and ML models for real-time and batch inference. Each served model is available as a REST API that can be integrated into web or client applications. The service automatically scales up or down to meet demand changes, saving infrastructure costs while optimizing latency performance. Model Serving uses serverless compute and provides a single UI to manage all models and their respective serving endpoints. ^[deploy-models-using-model-serving-databricks-on-aws.md]

Model Serving is part of the broader Databricks ML platform, which also supports [batch inference](/concepts/batch-inference-on-databricks.md), experiment tracking with [MLflow](/concepts/mlflow.md), and production monitoring with [AI Gateway](/concepts/ai-gateway.md). ^[databricks-data-science-and-ml-capabilities-databricks-on-aws.md]

## Supported Model Types

Model Serving supports three broad categories of models: ^[deploy-models-using-model-serving-databricks-on-aws.md]

- **Custom models** – Python models packaged in MLflow format and registered in [Unity Catalog](/concepts/unity-catalog.md) or the workspace model registry. Examples include scikit-learn, XGBoost, PyTorch, and Hugging Face transformers models. Agent serving for generative AI applications is also supported as a custom model. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **Foundation models** – Databricks-hosted open models (e.g., Meta Llama, Mistral) available via [Foundation Model APIs](/concepts/foundation-model-apis.md). Base models are available with **pay-per-token** pricing for experimentation, and workloads requiring performance guarantees and fine-tuned variants can be deployed with **provisioned throughput**. ^[deploy-models-using-model-serving-databricks-on-aws.md]
- **External models** – Models hosted outside of Databricks, such as GPT-4 from OpenAI, accessible through [External Models](/concepts/external-models.md) endpoints. These endpoints can be centrally governed from Databricks, streamlining the use and management of various LLM providers within your organization. ^[deploy-models-using-model-serving-databricks-on-aws.md]

You can interact with supported large language models using the [AI Playground](/concepts/ai-playground.md), a chat-like environment for testing, prompting, and comparing LLMs directly within your Databricks workspace. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Key Capabilities

### Automatic Scaling

Endpoints automatically scale compute based on demand. For custom models, available compute scale-out sizes are **Small** (0–4 concurrent requests), **Medium** (8–16), and **Large** (16–64). The scale-out size should be roughly equal to queries per second multiplied by model execution time. Endpoints can also be configured to scale to zero when not in use. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

### Governance and Security

All served models are governed by [Unity Catalog](/concepts/unity-catalog.md), which provides fine-grained access controls, security policies, and governance for data and AI assets. Model Serving encrypts all data at rest (AES-256) and in transit (TLS 1.2+). Network access to endpoints can be controlled by configuring network policies for serverless egress control. ^[deploy-models-using-model-serving-databricks-on-aws.md]

For Databricks Foundation Model APIs, as part of providing the service, Databricks may temporarily process and store inputs and outputs for the purposes of preventing, detecting, and mitigating abuse or harmful uses. Inputs and outputs are isolated from those of other customers, stored in the same region as the workspace for up to thirty (30) days, and only accessible for detecting and responding to security or abuse concerns. ^[deploy-models-using-model-serving-databricks-on-aws.md]

For all paid accounts, Model Serving does not use user inputs submitted to the service or outputs from the service to train any models or improve any Databricks services. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Monitoring and Quality

The Serving UI provides a central location to manage all endpoints, set usage limits, and monitor model quality using [AI Gateway](/concepts/ai-gateway.md). Real-time inference logs can be captured in inference tables governed in Unity Catalog for monitoring, auditing, and A/B comparison. ^[deploy-models-using-model-serving-databricks-on-aws.md]

### Performance

Model Serving is designed for high-availability, low-latency production use and can support over 25,000 queries per second with an overhead latency of less than 50 ms. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Deployment Workflow

Deploying a custom model involves three main steps: ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

1. **Log the model** – Register the model in [Unity Catalog](/concepts/unity-catalog.md) or the [MLflow Model Registry](/concepts/mlflow-model-registry.md).
2. **Create an endpoint** – Use the Serving UI or the Databricks Serving API. Name the endpoint, configure the served entity (model and version), traffic split, compute size, and whether to scale to zero.
3. **Query the endpoint** – Send JSON-formatted requests from the **Query endpoint** tab. For external access, a Databricks API token is required. ^[tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md]

## Batch Inference

For batch workloads, Model Serving integrates with [AI Functions](/concepts/ai-functions.md), including `ai_query` and task-specific functions like `ai_translate`. Batch inference is recommended when processing large tables or entire datasets. If you use a pre-provisioned model that is hosted and managed by Databricks, you don't need to configure a model serving endpoint yourself. ^[deploy-models-using-model-serving-databricks-on-aws.md] ^[supported-foundation-models-on-model-serving-databricks-on-aws.md]

## CI/CD Integration

Model Serving fits into an automated MLOps pipeline. Databricks supports: ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

- [MLflow Model Registry](/concepts/mlflow-model-registry.md) for managing model versions and lifecycle (staging, serving).
- [Declarative Automation Bundles](/concepts/declarative-automation-bundles.md) for deploying serving endpoints programmatically.
- Databricks Terraform provider for infrastructure-as-code automation across clouds.
- Git folders and REST APIs for integrating with CI/CD tools like GitHub Actions or Jenkins. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

The integration of [Databricks Feature Store](/concepts/databricks-feature-store.md) with MLflow ensures consistency of features for training and serving; MLflow models can automatically look up features from the Feature Store, even for low-latency online serving. ^[how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md]

## Requirements

- Registered model in [Unity Catalog](/concepts/unity-catalog.md) or the [Workspace Model Registry](/concepts/workspace-model-registry.md).
- Permissions on the registered models as described in [Serving endpoint ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#serving-endpoints).
- MLflow 1.29 or higher.
- Workspace entitlements configured. ^[deploy-models-using-model-serving-databricks-on-aws.md]

## Related Concepts

- [MLflow](/concepts/mlflow.md) – Open-source framework for experiment tracking and model management.
- [Unity Catalog](/concepts/unity-catalog.md) – Data governance platform for fine-grained access control over data and AI assets.
- [Foundation Model APIs](/concepts/foundation-model-apis.md) – Pay-per-token and provisioned throughput access to Databricks-hosted foundation models.
- [External Models](/concepts/external-models.md) – Serving models hosted on third-party platforms like OpenAI and Anthropic.
- [AI Functions](/concepts/ai-functions.md) – Built-in SQL functions for batch inference.
- [AI Gateway](/concepts/ai-gateway.md) – Central management of usage limits, permissions, and monitoring for model endpoints.
- [MLflow Model Registry](/concepts/mlflow-model-registry.md) – Central repository for model versions and lifecycle management.
- MLOps – Best practices for CI/CD in machine learning on Databricks.
- [AI Playground](/concepts/ai-playground.md) – Chat-like environment for testing and comparing LLMs.
- [Databricks Feature Store](/concepts/databricks-feature-store.md) – Managed feature store integrated with Model Serving for online inference.

## Sources

- databricks-data-science-and-ml-capabilities-databricks-on-aws.md
- deploy-models-using-model-serving-databricks-on-aws.md
- how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md
- log-load-and-register-mlflow-models-databricks-on-aws.md
- machine-learning-on-databricks-databricks-on-aws.md
- supported-foundation-models-on-model-serving-databricks-on-aws.md
- tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md

# Citations

1. [deploy-models-using-model-serving-databricks-on-aws.md](/references/deploy-models-using-model-serving-databricks-on-aws-7a559b74.md)
2. [databricks-data-science-and-ml-capabilities-databricks-on-aws.md](/references/databricks-data-science-and-ml-capabilities-databricks-on-aws-8cf8bf4a.md)
3. [tutorial-deploy-and-query-a-custom-model-databricks-on-aws.md](/references/tutorial-deploy-and-query-a-custom-model-databricks-on-aws-16c7ace5.md)
4. [supported-foundation-models-on-model-serving-databricks-on-aws.md](/references/supported-foundation-models-on-model-serving-databricks-on-aws-87287248.md)
5. [how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws.md](/references/how-does-databricks-support-cicd-for-machine-learning-databricks-on-aws-48551477.md)
