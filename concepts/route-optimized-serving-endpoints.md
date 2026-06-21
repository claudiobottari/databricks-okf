---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c365d07a5805de9145bd392192f1655b54cf75b8852be90a1beadebc2a33fe04
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - route-optimized-serving-endpoints
    - RSE
    - Route-Optimized Serving Endpoint
    - Route-optimized serving endpoint
    - route-optimized serving endpoint
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Route-optimized serving endpoints
description: Serving endpoints on Databricks with route optimization enabled for improved query performance, requiring dedicated URLs and OAuth authentication.
tags:
  - machine-learning
  - serving
  - optimization
timestamp: "2026-06-19T20:03:36.060Z"
---

# Route-optimized serving endpoints

**Route-optimized serving endpoints** are model serving or feature serving endpoints on Databricks that have route optimization enabled. These endpoints are accessed through a dedicated route-optimized URL that provides benefits not available through the standard workspace URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Requirements

To query a route-optimized serving endpoint, you must meet the following requirements:

- The endpoint must have route optimization enabled. This applies to both [Model Serving](/concepts/model-serving.md) and feature serving endpoints.
- Querying route-optimized endpoints supports **only OAuth tokens**; personal access tokens are not supported.

^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Route-optimized URL

When you create a route-optimized endpoint, a dedicated URL is generated in the following format:

```
https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations
```

You can retrieve this URL from the Serving UI, the REST API, or the Databricks SDK. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Important date: September 22, 2025

Starting **September 22, 2025**, all newly created route-optimized endpoints must be queried exclusively through this route-optimized URL. Endpoints created after this date do not support querying through the standard workspace URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

For route-optimized endpoints created **before September 22, 2025**:
- The standard workspace URL (`https://<databricks-workspace>/serving-endpoints/<endpoint-name>/invocations`) can still be used.
- However, the standard workspace URL path does **not** provide the benefits of route optimization.
- Endpoints created before this date continue to support both invocation URLs. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Authentication

All requests to route-optimized endpoints must use an OAuth token. Databricks recommends using service principals in production applications to fetch tokens programmatically. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Fetching an OAuth token using the Serving UI (testing / development)

1. On the **Serving** page, select your route-optimized endpoint.
2. On the endpoint details page, click **Use**.
3. Select the **Fetch Token** tab.
4. Click **Fetch OAuth Token**.

The token is valid for **1 hour**. Fetch a new token if it expires. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Fetching an OAuth token programmatically (production)

For production scenarios, set up a service principal with at least **Query permission** on the endpoint. Follow the steps in [Authorize service principal access to Databricks with OAuth](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) to create the service principal, assign permissions, and create an OAuth secret.

The Databricks Python SDK provides a direct API to query route-optimized endpoints:

```python
from databricks.sdk import WorkspaceClient
import databricks.sdk.core as client

endpoint_name = "<Serving-Endpoint-Name>"

c = client.Config(
    host="<Workspace-Host>",
    client_id="<Client-Id>",
    client_secret="<Secret>"
)

w = WorkspaceClient(config=c)
response = w.serving_endpoints_data_plane.query(endpoint_name, dataframe_records=...)
```

The SDK automatically fetches the correct endpoint URL based on the endpoint name. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Fetching an OAuth token manually

For custom clients, you can manually obtain an OAuth token by making a POST request to the token endpoint:

```
POST https://<databricks-instance>/oidc/v1/token
```

Include the following parameters:
- `client_id` – service principal client ID.
- `client_secret` – service principal OAuth secret.
- `grant_type=client_credentials`
- `scope=all-apis`
- `authorization_details` – a JSON payload specifying the endpoint ID and action (`query_inference_endpoint` or `manage_inference_endpoint`).

The endpoint ID is the alphanumeric identifier in the route-optimized URL’s hostname (e.g., `abcdefg` from `https://abcdefg.serving.cloud.databricks.com/...`). ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Querying the endpoint

After obtaining the route-optimized URL and an OAuth token, make a POST request with the token in the `Authorization` header.

Example using `curl`:

```bash
URL="<endpoint-url>"
OAUTH_TOKEN="<token>"
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OAUTH_TOKEN" \
  --data "@data.json" \
  "$URL"
```

^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Related concepts

- [Model Serving](/concepts/model-serving.md) – Serving machine learning models as REST APIs.
- Feature serving – Serving feature values for online inference.
- OAuth tokens – Token-based authentication for Databricks APIs.
- Service principals – Non-human identities for automated access.
- [Route optimization on serving endpoints](/concepts/route-optimization-for-serving-endpoints.md) – The enabling feature for route-optimized URLs.

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
