---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 469877de47a91b0bd5c06f5abea2f9788ee913e98eb4ef1247a2e7c571027398
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-environment-variables
    - MSEV
    - Environment variables
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Environment Variables
description: Mechanism for configuring access to external and private resources from Databricks model serving endpoints using plain text or secrets-based environment variables.
tags:
  - model-serving
  - configuration
  - databricks
timestamp: "2026-06-19T14:24:10.363Z"
---

# Model Serving Environment Variables

**Model Serving Environment Variables** are configuration parameters that can be passed to Databricks Model Serving endpoints to control runtime behavior, securely inject credentials, and enable optional features. They allow model inference code to access external resources and adjust endpoint behavior without modifying the deployed model itself. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Overview

Model Serving supports two types of environment variables: **plain text** variables for non-sensitive configuration values, and **secrets-based** variables that reference Databricks Secrets for secure credential management. Environment variables can be set during endpoint creation or updated on existing endpoints through the Serving UI, REST API, or SDKs. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Plain Text Environment Variables

Plain text environment variables are used for configuration values that do not require hiding, such as feature flags or non-sensitive settings. They are set directly with their literal string values. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

To add a plain text environment variable:

1. Navigate to the Serving UI.
2. Open **Advanced configurations**.
3. Click **+ Add environment variables**.
4. Enter the variable name and its value.

This can also be done programmatically via the REST API or SDKs. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Secrets-Based Environment Variables

Secrets-based environment variables securely inject credentials — such as API keys, tokens, or connection strings — into model serving endpoints at runtime. Databricks recommends this approach for deploying OpenAI, LangChain, and other SaaS model flavors that require authentication credentials. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Requirements

- The endpoint creator must have **READ** access to the [Databricks secrets](/concepts/databricks-secret-scopes.md) being referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials must be stored as Databricks secrets before being referenced in endpoint configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 1: Create a Secret Scope

First, create a secret scope using the Databricks CLI:

```bash
databricks secrets create-scope my_secret_scope
```

Then add the secret to the desired scope and key:

```bash
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Reference Secrets in Endpoint Configuration

When setting environment variables, reference secrets using the syntax `{{secrets/scope/key}}`. This tells Model Serving to fetch the secret from Databricks Secrets at serving time. If this syntax is not used, the environment variable is treated as plain text. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

From the Serving UI, add an environment variable in **Advanced configurations** with the value formatted as `{{secrets/my_secret_scope/my_secret_key}}`. After the endpoint is created or updated, Model Serving automatically fetches the secret key and populates the environment variable for inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Feature Tracing with Inference Tables

The `ENABLE_FEATURE_TRACING` environment variable controls whether automatic feature lookup DataFrames are logged to [Inference Tables](/concepts/inference-tables.md). This requires MLflow 2.14.0 or above. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

To enable feature tracing:

1. In **Advanced configurations**, click **+ Add environment variables**.
2. Enter `ENABLE_FEATURE_TRACING` as the environment name.
3. Set the value to `true`.

When enabled, Model Serving logs the feature lookup DataFrame used during inference to the endpoint's inference table. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

- **External API access**: Pass API keys to call OpenAI, Hugging Face, or other external model endpoints from within serving code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Storage access**: Provide credentials to access external data storage locations directly from model serving. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Configuration flags**: Toggle optional behaviors like feature tracing without redeploying the model. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **LangChain deployment**: Securely inject API keys when deploying LangChain retrieval-augmented generation (RAG) chains. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure where environment variables are applied.
- Databricks Secrets — The secure storage for credentials referenced by secrets-based variables.
- [Inference Tables](/concepts/inference-tables.md) — Logged inference data that can include feature tracing output.
- Feature Store and Model Serving — Using feature lookup tables during inference.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — Programmatic interface for managing serving endpoints and their environment variables.
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — Creation and management of serving endpoints.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
