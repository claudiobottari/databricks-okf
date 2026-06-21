---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9eeb169268f8f7a5e816ade168177f156cae5e97b96a1e92f3524dedf92c51c6
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - openai-and-langchain-credential-injection-for-model-serving
    - LangChain Credential Injection for Model Serving and OpenAI
    - OALCIFMS
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: OpenAI and LangChain Credential Injection for Model Serving
description: Using secrets-based environment variables to securely pass credentials when deploying OpenAI and LangChain MLflow model flavors to Databricks serving endpoints
tags:
  - machine-learning
  - llm
  - langchain
  - openai
  - databricks
timestamp: "2026-06-18T14:43:35.818Z"
---

Here is the wiki page for "OpenAI and LangChain Credential Injection for Model Serving", written based solely on the provided source material.

---

## OpenAI and LangChain Credential Injection for Model Serving

**OpenAI and LangChain Credential Injection for Model Serving** refers to the secure practice of passing API keys and other secrets to [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoints so that deployed OpenAI or LangChain models can authenticate with external services at inference time. Instead of hardcoding credentials in model code or configuration, the recommended approach uses [Databricks secrets](/concepts/databricks-secret-scopes.md) to store sensitive values and injects them as environment variables into the serving environment. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Overview

When deploying LangChain chains or OpenAI models behind Model Serving, the serving code must call external APIs that require credentials (typically an API key). Databricks recommends storing these credentials as Databricks secrets and referencing them through secrets-based environment variables in the endpoint configuration. The serving infrastructure fetches the secret value automatically at serving time and populates an environment variable that the model code can read. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

This pattern is recommended specifically for deploying the MLflow OpenAI flavor and the MLflow LangChain flavor to model serving, and is applicable to any SaaS model that authenticates via environment variables and API keys or tokens. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The endpoint creator must have READ access to the Databricks secrets being referenced in the endpoint configuration. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials such as API keys or tokens must be stored as Databricks secrets before they can be referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Workflow

The credential injection process follows three steps:

### Step 1: Create a Secret Scope and Store the Credential

First, create a secret scope using the Databricks CLI or API. Then store the credential (for example, the OpenAI API key) under a chosen key within that scope. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```bash
databricks secrets create-scope my_secret_scope
databricks secrets put-secret my_secret_scope my_secret_key
```

### Step 2: Reference the Secret in the Endpoint Configuration

When creating or updating the model serving endpoint, add a secrets-based environment variable using the syntax `{{secrets/<scope>/<key>}}`. For example, to set an environment variable named `OPENAI_API_KEY` from the secret stored above: ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

```
OPENAI_API_KEY = {{secrets/my_secret_scope/my_secret_key}}
```

This can be configured through the Serving UI in **Advanced configurations**, or via the Model Serving REST API or WorkspaceClient SDK. If a variable is not provided using the `{{secrets/scope/key}}` syntax, it is treated as a plain text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 3: Automatic Injection at Serving Time

After the endpoint is created or updated, Model Serving automatically fetches the secret value from the specified Databricks secrets scope and populates the environment variable. The model's inference code can then read the environment variable (e.g., `os.environ["OPENAI_API_KEY"]`) without needing to know the actual value. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Plain Text Environment Variables

For variables that do not need to be hidden (e.g., a model name or a non-sensitive configuration flag), plain text environment variables can be set directly without using the secrets syntax. These are configured in the same **Advanced configurations** section. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Availability

Secrets-based environment variables on Model Serving endpoints are available on all Databricks clouds (AWS, Azure, GCP). ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets — The secure storage mechanism for credentials and tokens
- [Model Serving](/concepts/model-serving.md) — The serving infrastructure for deploying ML models
- [MLflow LangChain Flavor](/concepts/mlflow-model-flavors.md) — The MLflow integration for LangChain models
- [MLflow OpenAI Flavor](/concepts/mlflowopenaiautolog.md) — The MLflow integration for OpenAI models
- [Environment Variables in Model Serving](/concepts/plain-text-environment-variables-in-model-serving.md) — The broader configuration mechanism for endpoint environment variables
- LangChain Retrieval QA Chain — An example LangChain chain commonly deployed with credential injection

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
