---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 76a335b5ed34a0da785a975af8983cb8500d58ad4c81eeb009cdf13adb2d4711
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-workflow
    - MSECW
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Configuration Workflow
description: The overall process of creating or updating model serving endpoints with environment variables through UI, REST API, WorkspaceClient SDK, or MLflow Deployments SDK
tags:
  - machine-learning
  - deployment
  - databricks
timestamp: "2026-06-18T14:43:27.153Z"
---

Here is the wiki page for "Model Serving Endpoint Configuration Workflow", based solely on the provided source material.

---

## Model Serving Endpoint Configuration Workflow

The **Model Serving Endpoint Configuration Workflow** describes the process of setting up and configuring [model serving endpoints](/concepts/model-serving-endpoint.md) in Databricks, including environment variable management, secret-based credential injection, and feature tracing configuration. This workflow ensures that deployed models have secure access to external resources and internal Databricks services. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Overview

When creating or updating a model serving endpoint, you can configure environment variables that are injected into the model's runtime environment. These variables can be either plain text (for non-sensitive configuration) or secrets-based (for credentials and API keys). The configuration is applied during endpoint creation or update operations through the Serving UI, REST API, or SDK. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Requirements

Before configuring secrets-based environment variables, ensure the following prerequisites are met:

- The endpoint creator must have `READ` access to the Databricks secrets being referenced in the configuration.
- Credentials such as API keys or tokens must be stored as [Databricks secrets](/concepts/databricks-secret-scopes.md) before referencing them in endpoint configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Configuring Environment Variables

#### Plain Text Environment Variables

Use plain text environment variables for configuration values that do not require secrecy. These can be set during endpoint creation or update through any of the following interfaces:

- **Serving UI**: Navigate to **Advanced configurations** and add environment variables.
- **REST API**: Include environment variables in the endpoint configuration payload.
- **WorkspaceClient SDK**: Set environment variables programmatically.
- **MLflow Deployments SDK**: Configure environment variables through the MLflow deployments interface. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

#### Secrets-Based Environment Variables

Secrets-based environment variables allow you to securely inject credentials into the model serving runtime without exposing them in configuration files or source code. This is the recommended approach for deploying models that require API keys, such as OpenAI or LangChain MLflow model flavors. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

##### Step 1: Create a Secret Scope

First, create a secret scope to store your credentials. Use the Databricks CLI to create the scope and add secrets:

```bash
databricks secrets create-scope my_secret_scope
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

##### Step 2: Add Secret Scopes to Endpoint Configuration

When configuring the endpoint, reference the secret using the syntax `{{secrets/scope/key}}`. This syntax distinguishes secrets-based variables from plain text variables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

**Serving UI**: In **Advanced configurations**, add an environment variable with the value formatted as `{{secrets/my_secret_scope/my_secret_key}}`. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

After the endpoint is created or updated, model serving automatically fetches the secret key from the Databricks secrets scope and populates the environment variable for your model inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Feature Tracing Configuration

If inference tables are enabled on your endpoint, you can log automatic feature lookup data frames to the inference table using the `ENABLE_FEATURE_TRACING` environment variable. This requires [MLflow](/concepts/mlflow.md) 2.14.0 or above. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

To enable feature tracing:

1. In **Advanced configurations**, click **+ Add environment variables**.
2. Enter `ENABLE_FEATURE_TRACING` as the environment name.
3. Set the value to `true`. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Use Cases

Secrets-based environment variables are particularly useful for:

- Deploying OpenAI MLflow model flavors that require API keys for inference.
- Deploying LangChain models that need credentials for external LLM providers or vector stores.
- Accessing external data storage locations directly from model serving endpoints.
- Any SaaS model requiring credentials, where the access pattern is based on environment variables and API keys or tokens. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Related Concepts

- [Model serving endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure that hosts deployed models
- [Databricks secrets](/concepts/databricks-secret-scopes.md) — Secure storage for credentials and sensitive values
- [MLflow Model Flavors](/concepts/mlflow-model-flavors.md) — Standardized model packaging formats
- [Inference Tables](/concepts/inference-tables.md) — Logging infrastructure for model serving requests
- [Feature Store](/concepts/feature-store.md) — Feature engineering and serving platform
- [Custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Endpoint creation and management

### Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
