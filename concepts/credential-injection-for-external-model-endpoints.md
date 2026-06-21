---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bde3e20293ceae04ae58646634ff5b420cc97e05787186b4ef3bf6e3e3170986
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - credential-injection-for-external-model-endpoints
    - CIFEME
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Credential Injection for External Model Endpoints
description: Using secrets-based environment variables in Databricks Model Serving to pass credentials to external services like OpenAI and LangChain models, enabling secure access from serving endpoints.
tags:
  - model-serving
  - openai
  - langchain
  - security
timestamp: "2026-06-19T09:23:00.005Z"
---

# Credential Injection for External Model Endpoints

**Credential Injection for External Model Endpoints** refers to the practice of securely passing authentication credentials (such as API keys, tokens, or passwords) from Databricks Secrets to a model served on [Model Serving](/concepts/model-serving.md) at runtime, enabling the model to access protected external resources or third‑party model APIs (e.g., OpenAI, LangChain‑hosted models) without exposing the credentials in code or configuration files.

## Overview

When a model deployed on Databricks Model Serving needs to call an external API or access a private data store, the credentials required for that access must be available inside the serving container. Rather than embedding plain‑text secrets in environment variables, Databricks recommends using [secrets‑based environment variables](/concepts/secrets-based-environment-variables-in-model-serving.md). These variables retrieve the actual credential value from a Databricks secret scope at serving time, so the plain text secret never appears in endpoint definitions or model code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

This pattern is particularly recommended for deploying models that use the OpenAI or LangChain MLflow model flavors, as well as any other SaaS model that expects credentials through environment variables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- The endpoint creator must have `READ` permission on the Databricks secret scope and key being referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials such as API keys or tokens must first be stored as a Databricks secret in an appropriate secret scope. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Steps to Inject Credentials

### Step 1: Create a Secret Scope and Store the Credential

Use the Databricks CLI or UI to create a secret scope and store the credential under a key:

```bash
databricks secrets create-scope my_secret_scope
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Step 2: Reference the Secret in the Endpoint Configuration

When creating or updating a model serving endpoint, add an environment variable using the syntax `{{secrets/scope/key}}`. This tells Model Serving to fetch the secret value from Databricks Secrets at runtime and assign it to the environment variable name you specify.

- **Serving UI**: In the **Advanced configurations** section, click **+ Add environment variables**, enter the variable name (e.g., `OPENAI_API_KEY`), and set the value to `{{secrets/my_secret_scope/my_secret_key}}`. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **REST API or SDK**: Provide the environment variable mapping in the endpoint creation or update payload using the same `{{secrets/scope/key}}` syntax. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

If the value does **not** use the `{{secrets/scope/key}}` pattern, it is treated as a plain‑text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

After the endpoint is deployed, Model Serving automatically resolves the secret and populates the environment variable for the model’s inference code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Example: OpenAI API Key for a LangChain Agent

A common use case is deploying a LangChain Retrieval QA Chain that calls OpenAI’s API. By injecting `OPENAI_API_KEY` as a secrets‑based environment variable, the model code can read `os.environ["OPENAI_API_KEY"]` without the key ever being stored in a notebook, script, or endpoint configuration. See the [Configure access to resources from model serving endpoints notebook](https://docs.databricks.com/aws/en/machine-learning/model-serving/store-env-variable-model-serving) for a concrete walkthrough. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- Databricks Secrets – The secure storage mechanism used to hold credentials.
- [Model Serving](/concepts/model-serving.md) – The inference platform that resolves secrets into environment variables.
- [Model Serving Endpoint Configuration](/concepts/model-serving-endpoint-configuration-api.md) – How to specify environment variables during endpoint creation.
- LangChain – An MLflow model flavor that often requires external API credentials.
- OpenAI – A common external model endpoint accessed via API key.
- [Instance Profile for Model Serving](/concepts/instance-profile-for-model-serving-endpoints.md) – Alternative method for granting access to AWS resources.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
