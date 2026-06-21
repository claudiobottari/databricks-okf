---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1dc5b6e8efa1662d6f89b4f01a64518a6703b2a8c28d9e02dd1c7e1149d0a468
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-with-resource-access
    - MSECWRA
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Configuration with Resource Access
description: The overall pattern of configuring model serving endpoints to access external or private resources such as SaaS APIs and data storage locations
tags:
  - model-serving
  - configuration
  - access-control
  - integration
timestamp: "2026-06-19T17:51:24.980Z"
---

# Model Serving Endpoint Configuration with Resource Access

**Model Serving endpoint configuration with resource access** refers to the set of methods available to provide environment variables — both plain text and secrets-based — to model serving endpoints on Databricks. These variables allow model code to access external APIs, private data storage, and other resources at inference time without hardcoding credentials.

## Requirements

For secrets-based environment variables, the endpoint creator must have READ access to the Databricks secrets referenced in the configuration. All credentials such as API keys or tokens must be stored as Databricks secrets before they can be used. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Plain Text Environment Variables

Plain text environment variables are used for variables that do not need to be hidden. They can be set in the Serving UI, the REST API, or the SDK when creating or updating an endpoint. From the Serving UI, environment variables are added under **Advanced configurations**. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Feature Tracing for Inference Tables

If inference tables are enabled on the endpoint, automatic feature lookup DataFrames can be logged to the inference table by setting the environment variable `ENABLE_FEATURE_TRACING` to `true`. This requires MLflow 2.14.0 or above. The variable can be added via the Serving UI, REST API, or SDK when creating or updating the endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Secrets-Based Environment Variables

Secrets-based environment variables allow credentials to be fetched from Databricks secrets at serving time. This is recommended for deploying MLflow model flavors such as OpenAI and LangChain to serving, and is applicable to any SaaS model that uses API keys and tokens. The credentials are retrieved by secret scope and key at runtime, so they never appear in the endpoint configuration directly. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 1: Create a Secret Scope

A secret scope must be created using the Databricks CLI or other tools. The following CLI commands illustrate the process:

```bash
databricks secrets create-scope my_secret_scope
databricks secrets put-secret my_secret_scope my_secret_key
```

After the scope and key exist, the secret can be referenced in the endpoint configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Add the Secret Scope to the Endpoint Configuration

When creating or updating an endpoint, the environment variable is defined using the syntax `{{secrets/scope/key}}`. This tells the serving infrastructure to fetch the secret from Databricks secrets. In the Serving UI, this syntax is entered in the **Advanced configurations** section. If the syntax is not used, the variable is treated as plain text. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

After the endpoint is created or updated, model serving automatically fetches the secret and populates the environment variable for the model inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Additional Resource

An additional resource is available for adding an instance profile to a model serving endpoint, which provides another mechanism for accessing AWS resources. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets – Securely store and reference credentials.
- [Model Serving](/concepts/model-serving.md) – Overview of serving custom models on Databricks.
- [MLflow](/concepts/mlflow.md) – Tool for packaging models with flavors like OpenAI and LangChain.
- [Inference Tables](/concepts/inference-tables.md) – Table that logs model inference requests and responses.
- [Feature Store](/concepts/feature-store.md) – Automatic feature lookup for serving endpoints.
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) – Endpoint creation and management.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
