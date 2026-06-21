---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c5c46381a0721733784c50eccda590f23522c9d8fa53f61dcb32f48e235fa99c
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - external-model-credential-management-via-environment-variables
    - EMCMVEV
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: External Model Credential Management via Environment Variables
description: Pattern of storing API keys and tokens as Databricks secrets and exposing them as environment variables to serve OpenAI, LangChain, and other SaaS models.
tags:
  - databricks
  - model-serving
  - openai
  - langchain
  - credentials
timestamp: "2026-06-18T11:08:56.862Z"
---

Here is the wiki page for "External Model Credential Management via Environment Variables."

---

## External Model Credential Management via Environment Variables

**External Model Credential Management via Environment Variables** is a feature of [Databricks Model Serving](/concepts/databricks-model-serving.md) that allows you to pass configuration values—including sensitive credentials—to a model serving endpoint at creation or update time, without hardcoding them in the model code or bundling them in the model artifact. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Overview

When deploying an MLflow model that integrates with an external service (such as OpenAI, Anthropic, or a custom LLM endpoint), the model typically needs an API key or authentication token at inference time. Model Serving supports two types of environment variables to supply these values: ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

1. **Plain text environment variables** – for non-sensitive configuration (e.g., a feature flag or a log level).
2. **Secrets-based environment variables** – for credentials and other sensitive values, where the value is a reference to a [Databricks secrets](/concepts/databricks-secret-scopes.md) scope and key using the syntax `{{secrets/scope/key}}`. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Adding plain text environment variables

Plain text environment variables are used for settings that do not need to be hidden. You can set them via the Serving UI, the REST API, the WorkspaceClient SDK, or the MLflow Deployments SDK when you create or update an endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

#### Example: Logging feature lookup DataFrames to inference tables

If you have [Inference Tables](/concepts/inference-tables.md) enabled on your endpoint, you can log your automatic feature lookup DataFrame to the inference table by setting the `ENABLE_FEATURE_TRACING` environment variable to `true`. This requires MLflow 2.14.0 or above. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Adding secrets-based environment variables

Secrets-based environment variables allow you to securely store credentials in Databricks secrets and reference them in the endpoint configuration. The credentials are fetched from the secret store at serving time and made available to the model inference code as environment variables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

Databricks recommends this approach for deploying OpenAI and LangChain MLflow model flavors, as well as any other SaaS model that requires an API key or token. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

#### Requirements

- The endpoint creator must have **READ** access to the Databricks secrets being referenced in the configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials (e.g., API keys) must be stored as a Databricks secret before they can be referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

#### Workflow

1. **Create a secret scope** (e.g., using the CLI: `databricks secrets create-scope my_secret_scope`).
2. **Add your secret** to the scope (e.g., `databricks secrets put-secret my_secret_scope my_secret_key`).
3. **Add the secret scope to the endpoint configuration** by specifying an environment variable in **Advanced configurations** using the syntax `{{secrets/scope/key}}`.

   After the endpoint is created or updated, Model Serving automatically fetches the secret key from the Databricks secrets scope and populates the environment variable for your model inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Example

The following example shows how to pass an OpenAI API key to a LangChain Retrieval QA Chain deployed behind a model serving endpoint:

```bash
# CLI commands
databricks secrets create-scope my_openai_scope
databricks secrets put-secret my_openai_scope openai_api_key
```

Then, when creating the endpoint, specify the environment variable as:

```
OPENAI_API_KEY={{secrets/my_openai_scope/openai_api_key}}
```

This allows the deployed model to call the OpenAI API without the API key being present in the model code or the endpoint logs. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [Databricks Model Serving](/concepts/databricks-model-serving.md)
- [Databricks secrets](/concepts/databricks-secret-scopes.md)
- [Secrets-based environment variables](/concepts/secrets-based-environment-variables-in-model-serving.md)
- External model credentials
- [MLflow](/concepts/mlflow.md)
- [Inference Tables](/concepts/inference-tables.md)

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
