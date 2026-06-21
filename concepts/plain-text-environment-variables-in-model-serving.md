---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e894d55f26cdc99d5bd6a04845573c3b26c0ff56d763e9f9fa73f7081057f61f
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - plain-text-environment-variables-in-model-serving
    - PTEVIMS
    - Environment Variables in Model Serving
    - Plain text environment variables for Model Serving
    - Add plain text environment variables
    - how to add plain text environment variables
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Plain Text Environment Variables in Model Serving
description: Setting non-sensitive configuration variables directly on a model serving endpoint via UI, REST API, or SDK without encryption
tags:
  - model-serving
  - environment-variables
  - configuration
timestamp: "2026-06-19T17:51:06.542Z"
---

# Plain Text Environment Variables in Model Serving

**Plain text environment variables** in Model Serving allow you to configure non-sensitive key-value pairs for model serving endpoints without using Databricks secrets. These variables are stored directly in the endpoint configuration and are visible in the UI and logs, making them appropriate only for settings that do not require confidentiality.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## When to Use Plain Text vs. Secrets

| Variable Type | Use Case | Example |
|--------------|----------|---------|
| **Plain text** | Non-sensitive configuration values (feature flags, debug settings, operational parameters) | `ENABLE_FEATURE_TRACING=true` |
| **Secrets-based** | Credentials, API keys, tokens | `OPENAI_API_KEY={{secrets/my_scope/my_key}}` |

Use plain text variables for settings that do not contain sensitive information. For any credential, API key, or token, use [Secrets-based Environment Variables in Model Serving](/concepts/secrets-based-environment-variables-in-model-serving.md) with the `{{secrets/scope/key}}` syntax.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Adding Plain Text Environment Variables

You can configure plain text environment variables in the **Serving UI**, the **REST API**, or the **SDK** when creating or updating an endpoint.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the Serving UI

1. Navigate to the **Serving** page in your Databricks workspace.
2. Create or select an existing model serving endpoint.
3. Click on **Advanced configurations**.
4. Select **+ Add environment variables**.
5. Enter the environment variable name in the key field and its value in the value field.
6. Click **Create** or **Confirm** to apply the changes.

Variables entered without the `{{secrets/scope/key}}` syntax are treated as plain text.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the REST API

```bash
POST /api/2.0/serving-endpoints
{
  "name": "my-endpoint",
  "config": {
    "served_models": [{
      "model_name": "my-model",
      "model_version": "1"
    }],
    "environment_variables": {
      "ENABLE_FEATURE_TRACING": "true",
      "MODEL_TIMEOUT": "30"
    }
  }
}
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the WorkspaceClient SDK

```python
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

w.serving_endpoints.create(
    name="my-endpoint",
    config={
        "served_models": [{
            "model_name": "my-model",
            "model_version": "1"
        }],
        "environment_variables": {
            "ENABLE_FEATURE_TRACING": "true",
            "MODEL_TIMEOUT": "30"
        }
    }
)
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Using the MLflow Deployments SDK

```python
import mlflow

client = mlflow.deployments.get_deploy_client("databricks")

client.create_endpoint(
    name="my-endpoint",
    config={
        "served_models": [{
            "model_name": "my-model",
            "model_version": "1"
        }],
        "environment_variables": {
            "ENABLE_FEATURE_TRACING": "true",
            "MODEL_TIMEOUT": "30"
        }
    }
)
```

^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Common Use Case: Feature Tracing

If you have inference tables enabled on your endpoint, you can log automatic feature lookup DataFrames to the inference table by setting `ENABLE_FEATURE_TRACING` to `true`. This feature requires **MLflow 2.14.0 or above**.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Configuring Feature Tracing

- **Serving UI**: In **Advanced configurations**, select **+ Add environment variables**, type `ENABLE_FEATURE_TRACING` as the environment name, and set the value to `true`.
- **REST API/SDK**: Include `"ENABLE_FEATURE_TRACING": "true"` in the `environment_variables` object.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Security Considerations

- **Plain text environment variables are visible** in endpoint configuration and logs. Do not use them for passwords, API keys, or tokens.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- **For sensitive credentials**, always use [Secrets-based Environment Variables in Model Serving](/concepts/secrets-based-environment-variables-in-model-serving.md) with the `{{secrets/scope/key}}` syntax.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
- No special permissions are required to set plain text environment variables beyond the ability to create or update serving endpoints. Secrets-based variables additionally require READ access to the referenced Databricks secrets.^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving endpoints](/concepts/model-serving-endpoint.md) — The serving infrastructure where environment variables are applied
- [Secrets-based Environment Variables in Model Serving](/concepts/secrets-based-environment-variables-in-model-serving.md) — Secure credential storage for model serving
- [Databricks secrets](/concepts/databricks-secret-scopes.md) — Secure storage service for sensitive configuration values
- Feature lookup inference tables — Integration with MLflow feature store for automatic feature tracing
- [Create custom model serving endpoints](/concepts/custom-model-serving-endpoint-support.md) — Guide for endpoint creation with environment variable support
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) — SDK for managing serving endpoints programmatically

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
