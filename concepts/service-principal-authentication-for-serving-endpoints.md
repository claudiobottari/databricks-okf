---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ae254f293acaaa270c395e8850c926c0caa568ecc1ad2a8d23859ae3c9653bc0
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-for-serving-endpoints
    - SPAFSE
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Service principal authentication for serving endpoints
description: Using Databricks service principals to programmatically fetch OAuth tokens for production applications that query route-optimized serving endpoints.
tags:
  - authentication
  - service-principals
  - production
timestamp: "2026-06-19T20:04:34.437Z"
---

# Service Principal Authentication for Serving Endpoints

**Service principal authentication** is the recommended method for programmatically querying [Route-Optimized Model Serving Endpoints](/concepts/route-optimized-model-serving-endpoints.md) and [feature serving endpoints](/concepts/feature-serving-endpoint.md) in production environments on Databricks. This approach uses OAuth 2.0 tokens obtained through a service principal's credentials, bypassing the need for interactive user sessions.

## Overview

For production applications that query serving endpoints, Databricks recommends using service principals rather than individual user accounts. Service principals allow you to embed authentication credentials directly within your application, enabling automated and secure token acquisition without manual intervention. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Requirements

Before setting up service principal authentication, you must meet the following prerequisites:

- A [Model Serving Endpoint](/concepts/model-serving-endpoint.md) or [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md) with route optimization enabled. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- Route-optimized endpoints **only** support OAuth tokens for querying; [personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md) (PATs) are not supported. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- The service principal must have at least **Query permission** on the serving endpoint. See Manage permissions on a model serving endpoint for details. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Setting Up a Service Principal

To use service principal authentication, follow the steps in the [Authorize service principal access to Databricks with OAuth](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) documentation through step 2. This involves:

1. Creating a service principal.
2. Assigning appropriate permissions to the service principal.
3. Creating an OAuth secret for the service principal.

After creation, the service principal must be granted at least **Can Query** permission on the target serving endpoint. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Programmatic Token Fetching

For production scenarios, you can fetch OAuth tokens programmatically using either the Databricks Python SDK or a custom REST API client.

### Using the Databricks Python SDK

The Databricks SDK provides a direct API for querying route-optimized endpoints without manually constructing token requests. The following example requires:

- The serving endpoint name (the SDK resolves the correct route-optimized URL).
- The service principal's client ID and secret.
- The workspace hostname.

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

^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Manual OAuth Token Fetching

For scenarios where the Databricks SDK cannot be used (e.g., custom clients), you can manually fetch an OAuth token by constructing a request to the OIDC token endpoint. This method requires specifying `authorization_details` in the request body. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

#### Components of the Manual Token Request

The manual token request requires:

- **Token endpoint URL**: Constructed as `https://<databricks-instance>/oidc/v1/token`, where `<databricks-instance>` is your workspace URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- **Client ID**: The service principal's application ID. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- **Client secret**: The OAuth secret created for the service principal. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- **Endpoint ID**: The alphanumeric ID found in the endpoint URL's `hostName`. For example, if the URL is `https://abcdefg.serving.cloud.databricks.com/9999999/serving-endpoints/test`, the endpoint ID is `abcdefg`. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- **Action**: The permission granted to the service principal. Valid values are `query_inference_endpoint` or `manage_inference_endpoint`. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

#### Example: REST API Request

```bash
export CLIENT_ID=<client-id>
export CLIENT_SECRET=<client-secret>
export ENDPOINT_ID=<endpoint-id>
export ACTION=<action>

curl --request POST \
--url <token-endpoint-URL> \
--user "$CLIENT_ID:$CLIENT_SECRET" \
--data 'grant_type=client_credentials&scope=all-apis' \
--data-urlencode 'authorization_details=[{"type":"workspace_permission","object_type":"serving-endpoints","object_path":"'"/serving-endpoints/$ENDPOINT_ID"'","actions": ["'"$ACTION"'"]}]'
```

The response contains an OAuth token valid for **1 hour**. After expiration, you must fetch a new token. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Querying the Endpoint

Once you have an OAuth token, include it in the `Authorization` header as a Bearer token when making requests to the serving endpoint URL.

### Example: REST API with Token

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

### Example: Python with SDK

When using the Databricks SDK, the token is automatically managed by the SDK client, so no manual header construction is required. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## URL Considerations for Route-Optimized Endpoints

Route-optimized endpoints created **after September 22, 2025** must be queried exclusively through the route-optimized URL (`https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations`). Endpoints created before this date continue to support both the route-optimized URL and the standard workspace URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- OAuth 2.0 — The authentication framework used by service principals.
- Service principal — The non-human identity used for programmatic access.
- [Route-optimized serving endpoints](/concepts/route-optimized-serving-endpoints.md) — Endpoints that require OAuth tokens for querying.
- [Model Serving](/concepts/model-serving.md) — The broader concept of deploying and querying ML models.
- Feature serving — Serving feature tables for online inference.
- OIDC — OpenID Connect, the protocol used for token exchange.
- Databricks SDK — The Python library for programmatic access.

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
