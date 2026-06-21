---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 43a6a95247123aa7f27f6e9b1ba9f6bf3a6e1b7805378eddab76f139e65babcc
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secrets-based-environment-variables-in-databricks-model-serving
    - SEVIDMS
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Secrets-Based Environment Variables in Databricks Model Serving
description: Securely storing and referencing API keys, tokens, and other credentials as Databricks secrets, then injecting them into model serving endpoints via the {{secrets/scope/key}} syntax.
tags:
  - model-serving
  - security
  - secrets
  - databricks
timestamp: "2026-06-19T09:22:48.224Z"
---

# Secrets-Based Environment Variables in Databricks Model Serving

**Secrets-Based Environment Variables in Databricks Model Serving** allow you to securely inject credentials and sensitive configuration values into model serving endpoints at runtime. Instead of hardcoding API keys, tokens, or other secrets in your model code or plain text environment variables, you reference them from Databricks Secrets, and the platform automatically resolves them when the endpoint serves requests. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Overview

Model Serving supports two types of environment variables: plain text variables for non-sensitive values and secrets-based variables for credentials. Secrets-based variables are the recommended approach for deploying models that need to call external services — such as OpenAI, LangChain, or other SaaS APIs — because they keep sensitive information out of configuration files and model artifacts. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

To use secrets-based environment variables, the following conditions must be met:

- The endpoint creator must have **READ** access to the Databricks secrets being referenced in the configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials such as API keys or tokens must be stored as Databricks Secrets before they can be referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## How It Works

During model serving, secrets are retrieved from Databricks Secrets by their scope and key. These values are then assigned to environment variable names that your model inference code can read at runtime. The secret information and the environment variable name are passed to the endpoint configuration during endpoint creation or as an update to an existing endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Setup Process

### Step 1: Create a Secret Scope

First, create a secret scope to organize your secrets. This can be done using the Databricks CLI: ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```bash
databricks secrets create-scope my_secret_scope
```

### Step 2: Store Your Secret

Add your secret (e.g., an API key) to the desired secret scope and key: ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```bash
databricks secrets put-secret my_secret_scope my_secret_key
```

### Step 3: Add Secret Scopes to Endpoint Configuration

When creating or updating a model serving endpoint, reference the secret using the following syntax: ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```
{{secrets/scope/key}}
```

This syntax tells Model Serving to resolve the value from Databricks Secrets at serving time. If this syntax is not used, the environment variable is treated as a plain text variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

You can add secrets-based environment variables through any of the following interfaces:

- **Serving UI**: In **Advanced configurations**, add an environment variable using the `{{secrets/scope/key}}` syntax. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **REST API**: Include the environment variable in the endpoint configuration payload. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **WorkspaceClient SDK**: Set environment variables programmatically when creating or updating an endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **MLflow Deployments SDK**: Configure environment variables through the MLflow deployments interface. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

After the endpoint is created or updated, Model Serving automatically fetches the secret key from the Databricks Secrets scope and populates the environment variable for your model inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

Secrets-based environment variables are particularly useful for:

- **External model endpoints**: Passing credentials to call OpenAI, Anthropic, or other third-party model APIs. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **LangChain deployments**: Providing API keys for LangChain chains that call external services. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Data storage access**: Supplying credentials to access external data storage locations directly from model serving. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Any SaaS model**: Any scenario requiring credentials where the access pattern is based on environment variables and API keys or tokens. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Best Practices

- **Always use secrets-based variables for credentials** rather than plain text environment variables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Organize secrets by scope** to manage access permissions effectively. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Grant READ access only** to users and service principals that need to reference the secrets in endpoint configurations. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **Rotate secrets regularly** by updating the secret value in Databricks Secrets without needing to modify the endpoint configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets — The secure storage mechanism for sensitive information
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure that consumes these environment variables
- [Custom Model Serving Endpoints](/concepts/custom-model-serving-endpoint-support.md) — How to create and manage serving endpoints
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — Programmatic interface for model deployment
- LangChain on Databricks — Using LangChain models with secrets-based configuration
- OpenAI Integration on Databricks — Configuring OpenAI API access through secrets

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
