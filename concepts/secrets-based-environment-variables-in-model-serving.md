---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1904339d65181ef5a05d1d8318ce4d7d1259599bf2c2e39e903652f0aef16b2
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - secrets-based-environment-variables-in-model-serving
    - SEVIMS
    - Secrets-based environment variables
    - secrets‑based environment variables
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Secrets-based Environment Variables in Model Serving
description: Using Databricks secrets to securely inject credentials like API keys into model serving endpoints at serving time
tags:
  - machine-learning
  - security
  - databricks
timestamp: "2026-06-18T14:43:24.381Z"
---

# Secrets-Based Environment Variables in Model Serving

**Secrets-based environment variables** allow you to securely pass credentials (API keys, tokens, and other sensitive values) to [Model Serving](/concepts/model-serving.md) endpoints at runtime without exposing them in plain text. Credentials are stored in [Databricks secrets](/concepts/databricks-secret-scopes.md) and referenced by scope and key; at serving time the platform fetches the secret and populates the environment variable for your model inference code.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

This feature is especially useful for deploying MLflow model flavors such as OpenAI and LangChain that require API keys to call external services. It also works with any SaaS model that authenticates via environment variables.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The endpoint creator must have **READ** access to the Databricks secret being referenced.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials (e.g., API keys, tokens) must be stored as a Databricks secret before configuring the endpoint.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Configure secrets-based environment variables

### Step 1: Create a secret scope and store a secret

Create a secret scope using the Databricks CLI, API, or UI. For example:^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```bash
databricks secrets create-scope my_secret_scope
```

Add a secret to that scope:^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```bash
databricks secrets put-secret my_secret_scope my_secret_key
```

### Step 2: Reference the secret in your endpoint configuration

When you create or update a model serving endpoint, provide the secret reference using the following syntax:^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```
{{secrets/<scope>/<key>}}
```

The platform treats any environment variable whose value matches this syntax as a secrets-based variable; otherwise it is treated as plain text.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

You can set secrets-based environment variables using:

- **Serving UI**: In **Advanced configurations**, add an environment variable and enter the `{{secrets/scope/key}}` syntax as its value.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **REST API**: Include the environment variables in the endpoint configuration payload.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **WorkspaceClient SDK / MLflow Deployments SDK**: Pass the environment variables dictionary when creating or updating the endpoint.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

Once the endpoint is deployed, model serving automatically fetches the secret value and makes it available to the inference code as the named environment variable.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Example use cases

- Pass an OpenAI API key to a LangChain Retrieval QA Chain for answering questions.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Authenticate to an external model endpoint (e.g., Anthropic, Azure OpenAI, AWS Bedrock) without hard-coding credentials.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Access external data storage locations that require token-based authentication.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [Databricks secrets](/concepts/databricks-secret-scopes.md) — The secure storage service for sensitive information.
- [Model Serving](/concepts/model-serving.md) — The platform that serves ML models as endpoints.
- [Environment variables](/concepts/model-serving-environment-variables.md) — Plain-text or secrets-based variables passed to serving endpoints.
- OpenAI MLflow flavor — An MLflow flavor that can consume API keys via environment variables.
- LangChain MLflow flavor — An MLflow flavor for LangChain applications.
- [Feature tracing](/concepts/feature-lineage-tracking.md) — A separate environment variable (`ENABLE_FEATURE_TRACING`) for logging feature lookup data to inference tables.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
