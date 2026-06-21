---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 721132777323d64b676edc07f0cad752b375d7604d368efbdf62365237c278ba
  pageDirectory: concepts
  sources:
    - query-with-the-google-gemini-api-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-token-based-authentication-for-external-api-calls
    - DTAFEAC
  citations:
    - file: query-with-the-google-gemini-api-databricks-on-aws.md
title: Databricks Token-Based Authentication for External API Calls
description: Using a Databricks personal access token (DATABRICKS_TOKEN) as a Bearer token in HTTP headers to authenticate requests made to Databricks serving endpoints from external clients or SDKs.
tags:
  - databricks
  - authentication
  - security
timestamp: "2026-06-19T20:06:43.360Z"
---

# Databricks Token-Based Authentication for External API Calls

**Databricks Token-Based Authentication for External API Calls** is the standard method for programmatically authenticating requests to Databricks APIs, including [Model Serving](/concepts/model-serving.md) endpoints, [MLflow](/concepts/mlflow.md) APIs, and other Databricks REST APIs. This mechanism uses a personal access token or service principal token passed as an HTTP header to authorize external applications and scripts. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

## Overview

When making external API calls to Databricks — such as querying a [Foundational Model Serving](/concepts/foundation-model-serving-modes.md) endpoint like Google Gemini — the client must include a valid Databricks API token in the request headers. The token is passed using the `Authorization` header with a `Bearer` token scheme. Without proper authentication, the API returns an HTTP 403 Forbidden or HTTP 401 Unauthorized error. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

## Implementation

### Token Retrieval

The Databricks token is typically stored as an environment variable named `DATABRICKS_TOKEN` and retrieved at runtime. This pattern keeps credentials out of source code and configuration files. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

```python
import os
DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
```

### Header Injection

The token is passed in the HTTP headers of every API request. The standard format is:

```
Authorization: Bearer <DATABRICKS_TOKEN>
```

This header is injected into the client's HTTP options, either through an HTTP library's built-in header support or by explicitly setting the header in a custom HTTP client configuration. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

### Example: Querying a Gemini Model Serving Endpoint

The following example demonstrates how to authenticate and query a Gemini model deployed on a Databricks serving endpoint using the Google GenAI Python SDK with a Databricks token: ^[query-with-the-google-gemini-api-databricks-on-aws.md]

```python
from google import genai
from google.genai import types
import os

DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')

client = genai.Client(
    api_key="databricks",
    http_options=types.HttpOptions(
        base_url="https://example.staging.cloud.databricks.com/serving-endpoints/gemini",
        headers={
            "Authorization": f"Bearer {DATABRICKS_TOKEN}",
        },
    ),
)

response = client.models.generate_content(
    model="databricks-gemini-2-5-pro",
    contents=[
        types.Content(
            role="user",
            parts=[types.Part(text="What is a mixture of experts model?")],
        ),
    ],
    config=types.GenerateContentConfig(
        max_output_tokens=256,
    ),
)

print(response.text)
```

Key points about this implementation:

- The `api_key` parameter is set to `"databricks"` as a placeholder; the actual authentication is handled by the `Authorization` header. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
- The `base_url` points to the specific serving endpoint path on the Databricks workspace. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
- The `Authorization` header contains the Bearer token retrieved from the environment variable. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

## Token Types

Databricks supports two types of tokens for external API authentication:

- **Personal Access Tokens**: Created by individual users for their own API access. These are tied to the user's permissions and can be managed through the Databricks workspace UI. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
- **Service Principal Tokens**: Created for automated workflows and service accounts. These provide non-human authentication for production systems and CI/CD pipelines. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

## Best Practices

1. **Environment Variables**: Always store tokens in environment variables rather than hardcoding them in source code. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
2. **Token Rotation**: Rotate tokens regularly and revoke compromised tokens immediately. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
3. **Minimum Permissions**: Create tokens with the minimum permissions needed for the specific API calls being made. ^[query-with-the-google-gemini-api-databricks-on-aws.md]
4. **Secure Storage**: Use secret management tools like Databricks Secrets or cloud provider secret managers for production deployments. ^[query-with-the-google-gemini-api-databricks-on-aws.md]

## Error Handling

If the token is missing, expired, or invalid, the API returns an HTTP error. Common error responses include:

- **401 Unauthorized**: The token is missing or invalid.
- **403 Forbidden**: The token is valid but lacks permission for the requested resource.

## Related Concepts

- [Model Serving](/concepts/model-serving.md) — Deploying and querying models via REST APIs
- [Foundational Model Serving](/concepts/foundation-model-serving-modes.md) — Accessing pre-built foundation models through Databricks
- [Google Gemini API (on Databricks)](/concepts/google-gemini-api-on-databricks.md) — Specific integration for Gemini models
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The underlying API framework
- Databricks Secrets — Secure credential management
- Service Principals in Databricks — Non-human authentication entities

## Sources

- query-with-the-google-gemini-api-databricks-on-aws.md

# Citations

1. [query-with-the-google-gemini-api-databricks-on-aws.md](/references/query-with-the-google-gemini-api-databricks-on-aws-8dbd37cc.md)
