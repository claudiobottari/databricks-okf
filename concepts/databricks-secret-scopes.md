---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1881cfd9c2b892d2b1b464dc93e86d3238d1042fabfa2bd93f3e94a1f3f0853
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-secret-scopes
    - DSS
    - Create a Databricks secret scope
    - Databricks Secret
    - Databricks Secret Scope
    - Databricks Secrets
    - Databricks secret
    - Databricks secret scope
    - Databricks secrets
    - Databricks Utilities secrets
    - Databricks secrets|Databricks secret scopes
    - Secret Scope
    - Secret Scopes
    - Secret scopes
    - Secrets Scope
    - dbutils.secrets
    - secret scope
    - secret scopes
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Databricks Secret Scopes
description: A secure storage mechanism for credentials that can be referenced by model serving endpoints using the {{secrets/scope/key}} syntax
tags:
  - secrets
  - security
  - databricks
timestamp: "2026-06-19T17:51:13.060Z"
---

Here is the updated wiki page for "Databricks Secret Scopes," incorporating your provided content and style guidelines.

# Databricks Secret Scopes

**Databricks Secret Scopes** are a secure organizational mechanism for managing sensitive credentials such as API keys, tokens, and passwords within the Databricks platform. A secret scope acts as a named container that holds one or more secret keys, each associated with a confidential value. By using secret scopes, users can centrally store and reference secrets from workloads without exposing the secret in plain text, while also enabling fine-grained access control. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Overview

A secret scope is a container that groups related secrets. Each key within a scope is associated with a single secret value. Scopes are managed through the Databricks CLI, UI, or API. At runtime, a workload retrieves a secret by specifying both the scope name and the key. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Creating and Managing a Secret Scope

To create a secret scope, use the Databricks CLI with the following command:

```bash
databricks secrets create-scope my_secret_scope
```

After the scope exists, you can add a secret to it:

```bash
databricks secrets put-secret my_secret_scope my_secret_key
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Related Concepts

- Databricks Secrets – The general secrets management system, including secret scopes.
- [Secret Scopes Management](/concepts/secret-scope-management-for-feature-store.md) – Detailed guide on creating, updating, and managing scopes via CLI, UI, and API.

## Using Secrets in Model Serving Endpoints

Secrets stored in a secret scope can be referenced in [Model Serving Endpoints](/concepts/model-serving-endpoint.md) as environment variables. This is especially useful for securely passing credentials to external services such as OpenAI or LangChain models deployed behind a serving endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Requirements

- The endpoint creator must have **READ** access to the Databricks Secrets being referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- Credentials (API keys, tokens) must be stored as a Databricks secret before being referenced. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Adding a Secrets-Based Environment Variable

When creating or updating a model serving endpoint, environment variables can reference secrets using the following syntax:

```
{{secrets/scope/key}}
```

Replace `scope` with your secret scope name and `key` with the secret key. If this syntax is not used, the variable is treated as a plain text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

You can add such variables through the **Serving UI**, the **REST API**, the **WorkspaceClient SDK**, or the **MLflow Deployments SDK**. In the Serving UI, locate the **Advanced configurations** section while creating or updating an endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

After the endpoint is created or updated, Databricks Model Serving automatically fetches the secret value from the secret scope and populates the environment variable for the model inference code. This allows the model to access credentials securely at serving time. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Related Concepts

- Environment Variables in Serving – A guide to configuring environment variables for endpoints.
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) – Where secrets are commonly consumed.

## Best Practices

- Store only sensitive values (API keys, tokens) as secrets; non-sensitive configuration can use plain text environment variables.
- Ensure that service principals and users have only the necessary permissions on secret scopes (principle of least privilege).
- Use distinct secret scopes for different environments or teams to manage access control cleanly.

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
