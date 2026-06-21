---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08487f1518ce94e56d942da775c70b885b11be08f62b27dd2c486ad120e23a4d
  pageDirectory: concepts
  sources:
    - query-route-optimized-serving-endpoints-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - serving-ui-token-fetch
    - SUTF
  citations:
    - file: query-route-optimized-serving-endpoints-databricks-on-aws.md
title: Serving UI token fetch
description: Fetching a short-lived OAuth token (valid for 1 hour) directly from the Databricks Serving UI for development and testing of route-optimized endpoints.
tags:
  - UI
  - testing
  - development
timestamp: "2026-06-19T20:04:32.846Z"
---

# Serving UI Token Fetch

**Serving UI Token Fetch** is the process of obtaining an OAuth token through the Databricks Serving UI to authenticate requests against a [route-optimized serving endpoint](/concepts/route-optimized-serving-endpoints.md). This token is required when querying model serving or feature serving endpoints that have route optimization enabled.

## Overview

Route-optimized serving endpoints require OAuth tokens for authentication and do not support personal access tokens (PATs). ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

The Serving UI provides a built-in mechanism for fetching a temporary OAuth token that is valid for **one hour**. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

This method is primarily recommended for **development and testing** purposes. For production use cases, Databricks recommends fetching OAuth tokens programmatically using service principals. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Fetching a Token from the Serving UI

To obtain an OAuth token through the Serving UI:

1. Navigate to the **Serving** page in your Databricks workspace.
2. Select your route-optimized endpoint to view its details.
3. On the endpoint details page, click the **Use** button.
4. Select the **Fetch Token** tab.
5. Click **Fetch OAuth Token**.

The system returns a token that is valid for one hour. If your token expires, you must fetch a new one. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Using the Token

After obtaining the OAuth token, include it in the `Authorization` header of your requests and combine it with the [Route-optimized endpoint URL](/concepts/route-optimized-endpoint-url.md) to query the endpoint. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

### REST API Example

```bash
URL="<endpoint-url>"
OAUTH_TOKEN="<token>"

curl -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OAUTH_TOKEN" \
  --data "@data.json" \
  "$URL"
```

## Production Alternative

For production applications, Databricks recommends setting up service principals and fetching OAuth tokens programmatically rather than using the Serving UI method. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Important Notes

- Tokens fetched through the Serving UI expire after **one hour**. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]
- From **September 22, 2025**, all newly created route-optimized endpoints must be queried exclusively through the route-optimized URL. ^[query-route-optimized-serving-endpoints-databricks-on-aws.md]

## Related Concepts

- OAuth token
- [Route-optimized serving endpoint](/concepts/route-optimized-serving-endpoints.md)
- Service principal
- [Model Serving Endpoint](/concepts/model-serving-endpoint.md)
- [Feature Serving Endpoint](/concepts/feature-serving-endpoint.md)

## Sources

- query-route-optimized-serving-endpoints-databricks-on-aws.md

# Citations

1. [query-route-optimized-serving-endpoints-databricks-on-aws.md](/references/query-route-optimized-serving-endpoints-databricks-on-aws-d31d8879.md)
