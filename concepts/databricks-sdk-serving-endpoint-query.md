---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e69978f6c78d1526eec89bf12a32bf8fc68d40f643922944ebd26b8d58eaaa9d
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sdk-serving-endpoint-query
    - DSSEQ
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Databricks SDK serving endpoint query
description: Using the Databricks Python SDK's WorkspaceClient.serving_endpoints_data_plane.query() method to directly query route-optimized endpoints with service principal credentials.
tags:
  - SDK
  - Python
  - querying
timestamp: "2026-06-19T20:05:17.120Z"
---

# Databricks SDK Serving Endpoint Query

**Databricks SDK serving endpoint query** refers to the programmatic method of sending inference requests to a route-optimized model or feature serving endpoint using the Databricks Python SDK. This approach is recommended for production applications that need to authenticate with OAuth tokens and take advantage of the performance benefits of [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md). ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Requirements

To use the Databricks SDK to query a serving endpoint, the endpoint must have route optimization enabled. Additionally, querying route-optimized endpoints only supports OAuth tokens; personal access tokens are not supported. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

For production scenarios, Databricks recommends using a service principal to programmatically fetch OAuth tokens. The service principal must be given at least **Query permission** on the endpoint. The service principal client ID and secret are used in the SDK configuration. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Fetching the Route-Optimized URL

When a route-optimized endpoint is created, it receives a dedicated URL:

```
https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations
```

This URL can be retrieved from the Serving UI, REST API, or Databricks SDK. The SDK, however, can infer the correct URL from the endpoint name, so fetching it manually is optional when using the SDK’s `query` method. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

> **Note**: Starting September 22, 2025, all newly created route-optimized endpoints must be queried exclusively through the route-optimized URL. Endpoints created before that date also support the standard workspace URL, but that path does not provide route-optimization benefits. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Querying with the Databricks SDK

The Databricks Python SDK provides the `serving_endpoints_data_plane.query()` method to directly query a route-optimized endpoint. This method accepts the endpoint name and the request payload (e.g., `dataframe_records`).

### Example

```python
from databricks.sdk import WorkspaceClient
import databricks.sdk.core as client

endpoint_name = "<Serving-Endpoint-Name>"  # Replace with your endpoint name

# Initialize SDK with service principal credentials
config = client.Config(
    host="<Workspace-Host>",          # e.g., my-workspace.cloud.databricks.com
    client_id="<Client-Id>",          # Service principal client ID
    client_secret="<Client-Secret>"   # Service principal secret
)
w = WorkspaceClient(config=config)

# Query the endpoint
response = w.serving_endpoints_data_plane.query(
    endpoint_name,
    dataframe_records=[{"col1": "value1", "col2": 42}]
)
```

The SDK automatically fetches the required OAuth token and constructs the correct route-optimized URL based on the endpoint name. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Fetching an OAuth Token Manually

For scenarios where the SDK or Serving UI cannot be used, an OAuth token can be fetched manually by making a POST request to the workspace’s token endpoint. The request must include `authorization_details` specifying the endpoint ID and the desired action (`query_inference_endpoint` or `manage_inference_endpoint`).

Example using `curl`:

```bash
curl --request POST \
  --url https://<databricks-instance>/oidc/v1/token \
  --user "$CLIENT_ID:$CLIENT_SECRET" \
  --data 'grant_type=client_credentials&scope=all-apis' \
  --data-urlencode 'authorization_details=[{"type":"workspace_permission","object_type":"serving-endpoints","object_path":"/serving-endpoints/<ENDPOINT_ID>","actions": ["query_inference_endpoint"]}]'
```

After obtaining the token, query the endpoint with:

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OAUTH_TOKEN" \
  --data "@data.json" \
  "<endpoint-url>"
```

The endpoint ID is the alpha‑numeric portion of the route-optimized URL’s hostname (e.g., `abcdefg` from `abcdefg.serving.cloud.databricks.com`). ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Testing in the Serving UI

For development and testing, the Serving UI provides a **Fetch Token** button that generates a temporary OAuth token (valid for 1 hour). This token can be used to test queries via REST API or Python code. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md)
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md)
- [Feature serving on Databricks](/concepts/feature-serving-endpoints-databricks.md)
- OAuth authentication for Databricks
- Service principals in Databricks
- Databricks Python SDK

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
