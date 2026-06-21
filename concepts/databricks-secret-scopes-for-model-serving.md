---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 85d7aa7cc85d0ab3ac7cbf5011a00e49e599db93bdba99b97a3f59d65eada89a
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-secret-scopes-for-model-serving
    - DSSFMS
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Databricks Secret Scopes for Model Serving
description: Creating and managing secret scopes (via CLI or API) that model serving endpoints read from at serving time to populate secrets-based environment variables.
tags:
  - secrets
  - security
  - databricks
  - model-serving
timestamp: "2026-06-19T09:22:59.976Z"
---

# Databricks Secret Scopes for Model Serving

**Databricks Secret Scopes for Model Serving** provide a secure mechanism for passing credentials and sensitive configuration values to model serving endpoints at inference time. Instead of hard-coding API keys in model source code or endpoint configuration, you store secrets in Databricks and reference them through scoped environment variables that the serving infrastructure resolves automatically. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## How Secret Scopes Work for Model Serving

Model Serving supports two kinds of environment variables:

- **Plain text** – for non-sensitive values such as feature-flag names (`ENABLE_FEATURE_TRACING`).
- **Secrets-based** – for credentials, API keys, and tokens. The serving process fetches the secret value from the Databricks [secrets](https://docs.databricks.com/aws/en/security/secrets/) store at deploy or update time and populates the corresponding environment variable for the model's inference code to use. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

A secrets-based environment variable is declared with the syntax `{{secrets/scope/key}}`. Without that wrapper, the variable is treated as a plain-text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

The endpoint creator must have `READ` access to the Databricks secrets being referenced in the configuration. If they lack that permission, the endpoint creation or update will fail. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Step-by-Step Workflow

### Step 1 – Create a Secret Scope

First, create a secret scope in Databricks. Use the CLI or UI to define the scope and store the secret value.

```bash
databricks secrets create-scope my_secret_scope
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 2 – Add the Secret Scope to an Endpoint Configuration

When you create or update a model serving endpoint via the Serving UI, REST API, or SDK, specify the environment variable using the `{{secrets/scope/key}}` syntax:

- **Serving UI**: In the **Advanced configuration** section, add an environment variable with name `{{secrets/my_secret_scope/my_secret_key}}` and map it to a variable name such as `OPENAI_API_KEY`.
- **REST API / SDK**: Include the `env_vars` field in the endpoint payload with the same syntax.

After the endpoint is created or updated, Model Serving automatically fetches the secret from the scoped key and injects it into the environment for the model's inference code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Use Cases

This pattern is particularly useful when you need to serve models that call external APIs:

- **OpenAI / other LLM APIs** – pass an API key for a gateway or endpoint.
- **LangChain models** – provide credentials for vector stores, retrievers, or custom chain components.
- **External data storage** – access credentials for reading or writing to external stores during inference.

Databricks recommends this feature for deploying [OpenAI](https://mlflow.org/docs/latest/python_api/openai/index.html) and [LangChain](https://mlflow.org/docs/latest/python_api/mlflow.langchain.html) MLflow model flavors, though it works with any SaaS model that requires credentials. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Comparison with Other Secret-Access Patterns

| Pattern | Description |
|---------|-------------|
| **{{secrets/scope/key}}** | Resolved at endpoint creation/update time; used by model serving infrastructure |
| **[Accessing Databricks secrets in scorers](/concepts/accessing-secrets-in-scorers.md)** | Uses `dbutils.secrets.get()` inside a custom scorer function; used during evaluation |
| **Plain-text env vars** | No security; use only for non-sensitive values |

Both serving-side and scorer-side secret patterns use the same Databricks secret store, but the serving-side pattern is resolved by the platform rather than by user code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Databricks secrets](/concepts/databricks-secret-scopes.md) – the underlying key-value store for sensitive data
- [Model Serving endpoints](/concepts/model-serving-endpoint.md) – the serving infrastructure that consumes these environment variables
- [Secret scopes](/concepts/databricks-secret-scopes.md) – containers that organize secrets and control access
- [Accessing Databricks secrets in scorers](/concepts/accessing-secrets-in-scorers.md) – an alternative secret-access pattern for custom evaluation functions
- [Code-based Scorers](/concepts/code-based-scorers.md) – custom evaluation functions that may also need secret access

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
