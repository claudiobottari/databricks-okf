---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2b50c0cbe69183c16f36d85c8f7c18ea90da1bcd2824fbf1052d9a927db8014a
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - plain-text-environment-variables-in-databricks-model-serving
    - PTEVIDMS
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Plain Text Environment Variables in Databricks Model Serving
description: Setting non-sensitive environment variables directly in model serving endpoint configurations via the UI, REST API, or SDK.
tags:
  - model-serving
  - configuration
  - databricks
timestamp: "2026-06-19T09:22:51.123Z"
---

# Plain Text Environment Variables in Databricks Model Serving

**Plain Text Environment Variables in Databricks Model Serving** allow you to pass non-sensitive configuration values to your model serving endpoints without the overhead of secret management. These variables are set directly as key-value pairs and are visible in plain text in endpoint configurations.

## Overview

Plain text environment variables are suitable for configuration values that do not require secrecy, such as feature flags, model parameters, or non-sensitive settings. They provide a simple way to customize model behavior at serving time without modifying model code or redeploying. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## When to Use Plain Text vs. Secrets-Based Variables

| Variable Type | Use Case | Example |
|---------------|----------|---------|
| Plain text | Non-sensitive configuration values | `ENABLE_FEATURE_TRACING=true` |
| Secrets-based | Credentials, API keys, tokens | `OPENAI_API_KEY={{secrets/scope/key}}` |

For sensitive information like API keys or tokens, Databricks recommends using [Secrets-Based Environment Variables in Databricks Model Serving](/concepts/secrets-based-environment-variables-in-databricks-model-serving.md) instead. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Adding Plain Text Environment Variables

You can set plain text environment variables when creating or updating a model serving endpoint through the Serving UI, REST API, or SDKs. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the Serving UI

1. Navigate to the model serving endpoint creation or edit page.
2. Expand **Advanced configurations**.
3. Click **+ Add environment variables**.
4. Enter the environment variable name and its value.
5. Save the endpoint configuration.

The UI distinguishes plain text variables from secrets-based variables by the syntax used. Any value that does not follow the `{{secrets/scope/key}}` format is treated as a plain text environment variable. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the REST API

Include environment variables in the endpoint configuration payload when creating or updating an endpoint:

```json
{
  "name": "my-endpoint",
  "config": {
    "served_entities": [
      {
        "entity_name": "my-model",
        "entity_version": "1",
        "workload_size": "Small",
        "scale_to_zero_enabled": true,
        "environment_vars": {
          "ENABLE_FEATURE_TRACING": "true",
          "MODEL_THRESHOLD": "0.85"
        }
      }
    ]
  }
}
```

### Using the WorkspaceClient SDK

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

w.serving_endpoints.create(
    name="my-endpoint",
    config={
        "served_entities": [
            {
                "entity_name": "my-model",
                "entity_version": "1",
                "workload_size": "Small",
                "scale_to_zero_enabled": True,
                "environment_vars": {
                    "ENABLE_FEATURE_TRACING": "true",
                    "MODEL_THRESHOLD": "0.85"
                }
            }
        ]
    }
)
```

### Using the MLflow Deployments SDK

```python
import mlflow.deployments

client = mlflow.deployments.get_deploy_client("databricks")

client.create_endpoint(
    name="my-endpoint",
    config={
        "served_entities": [
            {
                "entity_name": "my-model",
                "entity_version": "1",
                "workload_size": "Small",
                "scale_to_zero_enabled": True,
                "environment_vars": {
                    "ENABLE_FEATURE_TRACING": "true",
                    "MODEL_THRESHOLD": "0.85"
                }
            }
        ]
    }
)
```

## Common Use Case: Enabling Feature Tracing

One notable plain text environment variable is `ENABLE_FEATURE_TRACING`. When set to `true`, this variable logs automatic feature lookup DataFrames to inference tables. This requires MLflow 2.14.0 or above and inference tables enabled on the endpoint. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Limitations

- Plain text environment variables are visible in endpoint configurations and logs.
- They should not be used for credentials, API keys, or any sensitive data.
- For sensitive values, use the `{{secrets/scope/key}}` syntax to reference Databricks Secrets. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Secrets-Based Environment Variables in Databricks Model Serving](/concepts/secrets-based-environment-variables-in-databricks-model-serving.md) — Secure credential management for endpoints
- Databricks Secrets — The underlying secret storage mechanism
- [Model Serving Endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure that consumes these variables
- [Inference Tables](/concepts/inference-tables.md) — Destination for logged feature tracing data
- [Feature Lookup](/concepts/feature-lookup.md) — Automatic feature retrieval at serving time

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
