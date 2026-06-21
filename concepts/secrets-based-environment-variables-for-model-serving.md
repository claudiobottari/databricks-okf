---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d74dd7468f23e530ce6409fb18cd8152afff7ddd096416ba03ae95cf630967df
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secrets-based-environment-variables-for-model-serving
    - SEVFMS
    - Environment Variables for Model Serving
    - Environment variables for model serving
    - Store environment variables for model serving
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Secrets-Based Environment Variables for Model Serving
description: Using Databricks secrets to securely inject sensitive credentials like API keys into model serving endpoints at runtime
tags:
  - model-serving
  - secrets
  - security
  - configuration
timestamp: "2026-06-19T17:51:22.083Z"
---

# Secrets-Based Environment Variables for Model Serving

**Secrets-based environment variables** allow you to securely pass credentials — such as API keys, tokens, or database passwords — to [Model Serving endpoints](/concepts/model-serving-endpoint.md) without exposing them as plain text. Instead, the values are stored in [Databricks secrets](/concepts/databricks-secret-scopes.md) and referenced via a special syntax. The serving infrastructure fetches the secret at runtime and populates the environment variable for the model’s inference code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

This feature is recommended for deploying OpenAI and LangChain MLflow model flavors to serving, as well as any SaaS model that requires credentials accessed through environment variables and API keys. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

Before you can use secrets-based environment variables with a model serving endpoint:

- The endpoint creator must have **READ** access to the Databricks secrets being referenced in the configuration.
- Credentials (such as API keys or tokens) must be stored as a Databricks secret inside a [secret scope](/concepts/databricks-secret-scopes.md). ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## How to set up secrets-based environment variables

### Step 1: Create a secret scope and store the secret

First, create a secret scope using the Databricks CLI, API, or workspace UI. For example:

```bash
databricks secrets create-scope my_secret_scope
```

Then store the credential under a key within that scope:

```bash
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Reference the secret in the endpoint configuration

When creating or updating a model serving endpoint, add an environment variable whose value is the secret reference in the format:

```
{{secrets/scope/key}}
```

If the value does not follow this syntax, it is treated as a plain text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

You can configure the environment variable through any of the following interfaces:

- **Serving UI** – Under **Advanced configurations**, click **+ Add environment variables** and enter the variable name and the `{{secrets/scope/key}}` value.
- **REST API** – Include the environment variable in the endpoint creation or update payload.
- **WorkspaceClient SDK** – Set the environment variable in the `EndpointCoreConfigInput` object.
- **MLflow Deployments SDK** – Pass the environment variable as part of the `create_endpoint()` or `update_endpoint()` call.

After the endpoint is created or updated, Model Serving automatically fetches the secret from the Databricks secret scope and populates the environment variable for the model’s inference code at serving time. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Example notebook

A notebook example demonstrating how to configure an OpenAI API key for a LangChain Retrieval QA Chain deployed behind Model Serving endpoints with secrets-based environment variables is available in the Databricks documentation. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [Plain text environment variables for Model Serving](/concepts/plain-text-environment-variables-in-model-serving.md) – For non-sensitive configuration values.
- [Feature Tracing with Inference Tables](/concepts/feature-tracing-with-inference-tables.md) – Use the plain text variable `ENABLE_FEATURE_TRACING=true` to log automatic feature lookup data frames to inference tables (requires MLflow 2.14.0 or above). ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- [Add an instance profile to a model serving endpoint](/concepts/instance-profile-for-model-serving-endpoints.md) – Another way to grant access to external resources.
- MLflow deployments – Workflow for deploying MLflow models to serving endpoints.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
