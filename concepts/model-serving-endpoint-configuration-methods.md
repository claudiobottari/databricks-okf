---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3d3b97a542401bfacd7696d102df8dad60aff87f0852609dca7a10f25e147939
  pageDirectory: concepts
  sources:
    - configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-endpoint-configuration-methods
    - MSECM
  citations:
    - file: configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md
title: Model Serving Endpoint Configuration Methods
description: "The four interfaces for configuring environment variables on model serving endpoints: Serving UI, REST API, WorkspaceClient SDK, and MLflow Deployments SDK."
tags:
  - model-serving
  - configuration
  - api
  - sdk
timestamp: "2026-06-19T09:23:00.630Z"
---

# Model Serving Endpoint Configuration Methods

**Model Serving Endpoint Configuration Methods** refers to the supported approaches for passing configuration data, credentials, and settings to [model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints) on Databricks. Endpoints can be configured with environment variables in plain text, secrets-based variables that reference Databricks secrets, and a special flag to enable feature tracing to inference tables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Requirements

- For plain text environment variables, no special permissions are required beyond endpoint creation privileges.
- For secrets-based environment variables, the endpoint creator must have `READ` permission to the Databricks secrets being referenced. Credentials such as API keys or tokens must be stored as Databricks secrets before being used. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Configuration Methods

### Plain Text Environment Variables

Use plain text environment variables for settings that do not need to be hidden. They can be added during endpoint creation or update through the Serving UI (under **Advanced configurations**), the REST API, the WorkspaceClient SDK, or the MLflow Deployments SDK. Any value provided without the `{{secrets/scope/key}}` syntax is treated as plain text. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Secrets-Based Environment Variables

Credentials such as API keys for OpenAI or LangChain models, or tokens for external services, can be passed securely using Databricks secrets. The process involves two steps:

1. **Create a secret scope** and store the credential using a key (e.g., via the Databricks CLI: `databricks secrets create-scope my_secret_scope` and `databricks secrets put-secret my_secret_scope my_secret_key`). ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]
2. **Add the secret scope to the endpoint configuration** by specifying an environment variable with the syntax `{{secrets/scope/key}}`. This can be done in the Serving UI under **Advanced configurations**, or via REST API, SDKs. At serving time, Databricks automatically fetches the secret and populates the environment variable for the model inference code. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

This method is recommended for deploying MLflow models that use OpenAI or LangChain flavors, and is also applicable to any SaaS model that authenticates via API keys or tokens. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

### Feature Tracing to Inference Tables

If inference tables are enabled on the endpoint, you can log automatic feature lookup DataFrames to the inference table by setting the environment variable `ENABLE_FEATURE_TRACING` to `true`. This requires MLflow 2.14.0 or above. The variable is added like any other environment variable (plain text) in the Serving UI, REST API, or SDK. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Example Notebook

Databricks provides a notebook example demonstrating how to configure an OpenAI API key for a LangChain Retrieval QA Chain deployed behind a model serving endpoint using secrets-based environment variables. ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Additional Resources

- [Add an instance profile to a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/add-model-serving-instance-profile) ^[configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Model Serving Endpoints](/concepts/model-serving-endpoint.md)
- Secrets in Databricks
- [Feature Lookup](/concepts/feature-lookup.md)
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md)
- LangChain on Databricks

## Sources

- configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md

# Citations

1. [configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws.md](/references/configure-access-to-resources-from-model-serving-endpoints-databricks-on-aws-dab8a5e3.md)
