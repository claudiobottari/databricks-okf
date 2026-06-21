---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4eba53237b17d7b863fc0a2ae3cfe3066d1a3c50d580d01ae0920bd25c9aef5d
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oauth-token-authentication-for-serving-endpoints
    - OTAFSE
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: OAuth token authentication for serving endpoints
description: OAuth tokens are the only supported authentication method for querying route-optimized endpoints; personal access tokens are not supported.
tags:
  - authentication
  - security
  - OAuth
timestamp: "2026-06-19T20:04:09.205Z"
---

# OAuth Token Authentication for Serving Endpoints

**OAuth Token Authentication for Serving Endpoints** is the required method for authenticating API requests to [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md) on Databricks. Unlike standard serving endpoints, route-optimized endpoints do not support [personal access tokens (PATs)](/concepts/databricks-personal-access-token-pat-authentication.md) and must be queried exclusively using OAuth tokens. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Requirements

To query a route-optimized serving endpoint, you must have:

- A model serving endpoint or [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) that has route optimization enabled. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- An OAuth token for authentication. Personal access tokens are not supported for route-optimized endpoints. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Fetching an OAuth Token

### Using the Serving UI (Testing)

For development and testing purposes, you can fetch an OAuth token directly from the Databricks Serving UI:

1. Navigate to the **Serving** page in your workspace.
2. Select your route-optimized endpoint.
3. On the endpoint details page, click the **Use** button.
4. Select the **Fetch Token** tab.
5. Click **Fetch OAuth Token**.

The fetched token is valid for **1 hour**. You must fetch a new token if the current one expires. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Programmatic Token Fetching (Production)

For production applications, Databricks recommends using service principals to fetch OAuth tokens programmatically. Follow these steps:

1. Create a service principal and assign it permissions as described in [Authorize service principal access to Databricks with OAuth](/concepts/service-principal-authorization-for-databricks-apps.md)^[query-route-optimized-serving-endpoints-databricks-on-aws.md].
2. Grant the service principal at least **Query permission** on the serving endpoint. See Manage permissions on a model serving endpoint. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

The Databricks Python SDK provides a direct API for querying route-optimized endpoints using service principal credentials: ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

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
response = w.serving_endpoints_data_plane.query(
    endpoint_name, 
    dataframe_records=....
)
```

### Manual Token Fetching

If you cannot use the Databricks SDK or the Serving UI, you can fetch an OAuth token manually by making a direct request to the OAuth token endpoint. This approach is primarily for custom clients in production environments. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

When fetching an OAuth token manually, you must specify `authorization_details` in the request: ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

```bash
export CLIENT_ID=<client-id>
export CLIENT_SECRET=<client-secret>
export ENDPOINT_ID=<endpoint-id>
export ACTION=<action>  # e.g., 'query_inference_endpoint'

curl --request POST \
--url https://<databricks-instance>/oidc/v1/token \
--user "$CLIENT_ID:$CLIENT_SECRET" \
--data 'grant_type=client_credentials&scope=all-apis' \
--data-urlencode 'authorization_details=[{"type":"workspace_permission","object_type":"serving-endpoints","object_path":"/serving-endpoints/$ENDPOINT_ID","actions": ["$ACTION"]}]'
```

Replace:
- `<databricks-instance>` with your workspace URL
- `<client-id>` with the service principal's client ID
- `<client-secret>` with the service principal's OAuth secret
- `<endpoint-id>` with the endpoint ID from the route-optimized URL (e.g., `abcdefg` from `https://abcdefg.serving.cloud.databricks.com/9999999/serving-endpoints/test`)
- `<action>` with either `query_inference_endpoint` or `manage_inference_endpoint` ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Querying the Endpoint

After obtaining an OAuth token, include it in the `Authorization` header of your API request: ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

```bash
URL="<endpoint-url>"
OAUTH_TOKEN="<token>"

curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OAUTH_TOKEN" \
  --data "@data.json" \
  "$URL"
```

## Routes and URLs

Route-optimized endpoints use a dedicated URL format:

```
https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations
```

You can retrieve this URL from the Serving UI, REST API, or Databricks SDK. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

> **Warning:** Starting **September 22, 2025**, all newly created route-optimized endpoints must be queried exclusively through the route-optimized URL. Endpoints created after this date do not support querying through the standard workspace URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md)
- [Model serving endpoints](/concepts/model-serving-endpoint.md)
- [Feature serving endpoints](/concepts/feature-serving-endpoint.md)
- Service principals
- OAuth 2.0 authentication
- Databricks SDK
- [Serving endpoint permissions](/concepts/serving-endpoint-acls.md)

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
