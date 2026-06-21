---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 337999bbb5134db48a163d5215989e88c3a773b83a330f2e293d24e6e91b78b8
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - manual-oauth-token-fetch-with-authorization_details
    - MOTFWA
    - OAuth Authorization Code Grant
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Manual OAuth token fetch with authorization_details
description: The process of manually requesting an OAuth token from the OIDC token endpoint with an authorization_details payload specifying the endpoint ID, object type, and action permission.
tags:
  - authentication
  - OAuth
  - API
timestamp: "2026-06-19T20:03:55.088Z"
---

# Manual OAuth Token Fetch with `authorization_details`

**Manual OAuth Token Fetch with `authorization_details`** is a technique for obtaining an OAuth token to query a [Route-Optimized Serving Endpoint](/concepts/route-optimized-serving-endpoints.md) when automated methods like the Databricks SDK or the Serving UI are not available. It is intended for custom clients or production scenarios where the user needs fine-grained control over the token request. This method requires specifying an `authorization_details` JSON parameter in the token request, which scopes the token to a specific serving endpoint and action. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## When to Use

The manual fetch is recommended for users who have a customized client and want to query a route-optimized endpoint in production without relying on the Databricks SDK or the Serving UI’s built-in token fetch. It is also used when the workspace’s default OAuth token flow is insufficient because the token must be restricted to a particular endpoint and permission level. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Requirements

- A route-optimized serving endpoint or feature serving endpoint. See [Route Optimization on Serving Endpoints](/concepts/route-optimization-for-serving-endpoints.md).
- Querying route-optimized endpoints only supports OAuth tokens; [Personal Access Tokens](/concepts/databricks-personal-access-token-pat-authentication.md) are not allowed. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- A Service Principal with at least **Query permission** on the endpoint. The service principal must have an OAuth secret created. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- The endpoint ID (the alphanumeric portion from the route‑optimized URL’s hostname) and the desired action (`query_inference_endpoint` or `manage_inference_endpoint`). ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Steps to Fetch the Token

1. **Construct the token endpoint URL**  
   Replace `<databricks-instance>` with the workspace URL of your Databricks deployment (e.g., `https://my-workspace.cloud.databricks.com`). The resulting URL is:  
   `https://<databricks-instance>/oidc/v1/token`  
   ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

2. **Provide client credentials**  
   Use the service principal’s client ID (application ID) as the username and its OAuth secret as the password for HTTP Basic Authentication. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

3. **Set the `grant_type` and `scope`**  
   The request body must include:  
   `grant_type=client_credentials&scope=all-apis`  
   ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

4. **Add `authorization_details`**  
   URL‑encode a JSON array that specifies the target endpoint and action. The structure is:

   ```json
   [
     {
       "type": "workspace_permission",
       "object_type": "serving-endpoints",
       "object_path": "/serving-endpoints/<endpoint-id>",
       "actions": ["<action>"]
     }
   ]
   ```

   - `object_path` uses the endpoint **ID** (e.g., `abcdefg`), not the endpoint name.
   - `actions` can be `"query_inference_endpoint"` or `"manage_inference_endpoint"`. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

5. **Send the request**  
   Issue a `POST` request to the token endpoint with the above parameters. The response will contain an OAuth token valid for 1 hour. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Examples

### REST API (cURL)

```bash
export CLIENT_ID=<client-id>
export CLIENT_SECRET=<client-secret>
export ENDPOINT_ID=<endpoint-id>
export ACTION=<action>  # e.g., 'query_inference_endpoint'

curl --request POST \
  --url https://<databricks-instance>/oidc/v1/token \
  --user "$CLIENT_ID:$CLIENT_SECRET" \
  --data 'grant_type=client_credentials&scope=all-apis' \
  --data-urlencode 'authorization_details=[{"type":"workspace_permission","object_type":"serving-endpoints","object_path":"'"/serving-endpoints/$ENDPOINT_ID"'","actions": ["'"$ACTION"'"]}]'
```

^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### Python (using `requests`)

```python
import requests

client_id = "<client-id>"
client_secret = "<client-secret>"
endpoint_id = "<endpoint-id>"
action = "query_inference_endpoint"

token_url = "https://<databricks-instance>/oidc/v1/token"
auth = (client_id, client_secret)
data = {
    "grant_type": "client_credentials",
    "scope": "all-apis",
    "authorization_details": [
        {
            "type": "workspace_permission",
            "object_type": "serving-endpoints",
            "object_path": f"/serving-endpoints/{endpoint_id}",
            "actions": [action],
        }
    ],
}

response = requests.post(token_url, auth=auth, json=data)
token = response.json()["access_token"]
```

^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Querying the Endpoint

After obtaining the token, use it in the `Authorization` header when calling the route‑optimized endpoint URL:

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

## Related Concepts

- [Route-Optimized Serving Endpoint](/concepts/route-optimized-serving-endpoints.md)
- [OAuth Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)
- Service Principal OAuth Secrets
- [Serving Endpoint Permissions](/concepts/serving-endpoint-acls.md)
- Databricks SDK (for programmatic querying without manual token fetch)

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
