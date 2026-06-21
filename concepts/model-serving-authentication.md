---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 19de42c86ab28ca3cd6f499570a72b705059906942dc8ba292aa4836faab4f00
  pageDirectory: concepts
  sources:
    - query-serving-endpoints-for-custom-models-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - model-serving-authentication
    - MSA
  citations:
    - file: query-serving-endpoints-for-custom-models-databricks-on-aws.md
title: Model Serving Authentication
description: Authentication mechanism for Databricks Model Serving endpoints requiring a Databricks REST API token, sent via HTTP basic auth with 'token:' as the username and the API token as the password
tags:
  - databricks
  - authentication
  - security
  - api
timestamp: "2026-06-19T20:04:48.653Z"
---

## Model Serving Authentication

**Model Serving Authentication** refers to the credentials and methods required to submit scoring requests to a Databricks **model serving endpoint**. All requests to a served model must be authenticated to ensure only authorized users and applications can invoke the endpoint. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Authentication Methods

Databricks Model Serving supports authentication using a **Databricks API token**. The token is passed with the request as part of the HTTP Authorization header. The two primary ways to send authenticated requests are:

- **REST API** – Use basic authentication with the literal username `token` and the API token as the password. For example, the `curl` option `-u token:$DATABRICKS_API_TOKEN` sets the `Authorization` header to `Basic <encoded-token>`. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]
- **MLflow Deployments SDK** – Requires MLflow 2.9 or above and a Databricks API token. The SDK handles authentication internally when the token is configured in the environment or passed directly. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Token Requirements

- The token must be a valid Databricks API token with sufficient permissions to query the serving endpoint.
- The token is typically stored as an environment variable (e.g., `DATABRICKS_API_TOKEN`) and passed securely in the request.
- For REST API calls, the endpoint URL follows the pattern: `https://<databricks-instance>/serving-endpoints/<endpoint-name>/invocations`. ^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Example: Authenticated Scoring Request

The following `curl` command sends a scoring request with authentication using a token:

```bash
curl -X POST -u token:$DATABRICKS_API_TOKEN $ENDPOINT_INVOCATION_URL \
  -H 'Content-Type: application/json' \
  -d '{"dataframe_split": {"columns": [...], "data": [...]}}'
```

^[query-serving-endpoints-for-custom-models-databricks-on-aws.md]

### Related Concepts

- Databricks API token – The credential used for authentication.
- [Model Serving](/concepts/model-serving.md) – The platform that hosts and serves models.
- [Serving Endpoints](/concepts/serving-endpoint-acls.md) – The REST API endpoints for model invocation.
- REST API – The primary interface for custom model scoring.
- [MLflow Deployments SDK](/concepts/mlflow-deployments-sdk.md) – A Python SDK for managing and querying serving endpoints.
- Foundation Model Authentication – Authentication specifics for generative AI and LLM endpoints.

### Sources

- query-serving-endpoints-for-custom-models-databricks-on-aws.md

# Citations

1. [query-serving-endpoints-for-custom-models-databricks-on-aws.md](/references/query-serving-endpoints-for-custom-models-databricks-on-aws-6a253872.md)
