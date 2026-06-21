---
title: Query route-optimized serving endpoints | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/query-route-optimization
ingestedAt: "2026-06-18T08:12:38.837Z"
---

This article describes how to fetch the appropriate authentication credentials and URL so you can query your route-optimized [model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) or [feature serving](https://docs.databricks.com/aws/en/machine-learning/feature-store/feature-function-serving) endpoint.

## Requirements[​](#requirements "Direct link to Requirements")

*   A model serving endpoint or feature serving endpoint that has route optimization enabled. See [Route optimization on serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/route-optimization).
*   Querying route-optimized endpoints only support using OAuth tokens. Personal access tokens are not supported.

## Fetch the route-optimized URL[​](#fetch-the-route-optimized-url "Direct link to Fetch the route-optimized URL")

warning

Starting **September 22, 2025**, all newly created route-optimized endpoints must be queried exclusively through the route-optimized URL. Endpoints created after this date do not support querying through the workspace URL.

If your route-optimized endpoint was created **before September 22, 2025**:

*   The standard workspace URL can also be used to query the endpoint. The standard workspace URL path does **not** provide the benefits of route optimization.
    
    `https://<databricks-workspace>/serving-endpoints/<endpoint-name>/invocations`
    
*   Route-optimized endpoints created before this date continue to support both invocations URLs: the route-optimized URL path and the standard workspace URL path.
    

When you create a route-optimized endpoint, the following route-optimized URL is created for the endpoint.

`https://<unique-id>.serving.cloud.databricks.com/<workspace-id>/serving-endpoints/<endpoint-name>/invocations`

You can get this URL from the following:

*   Serving UI
*   REST API
*   Databricks SDK

![route-optimized endpoint URL](https://docs.databricks.com/aws/en/assets/images/route-opt-endpoint-url-4bf21ad831de27b44401832df86bd453.png)

## Fetch an OAuth token and query the endpoint[​](#fetch-an-oauth-token-and-query-the-endpoint "Direct link to Fetch an OAuth token and query the endpoint")

To query your route-optimized endpoint you must use an OAuth token. Databricks recommends using [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) in your production applications to fetch OAuth tokens programmatically. The following sections describes recommended guidance on how to fetch an OAuth token for test and production scenarios.

### Fetch an OAuth token using the Serving UI[​](#fetch-an-oauth-token-using-the-serving-ui "Direct link to Fetch an OAuth token using the Serving UI")

The following steps show how to fetch a token in the Serving UI. These steps are recommended for development and testing your endpoint.

For production use, like using your route-optimized endpoint in an application, your token is fetched using a service principal. See [Fetch an OAuth token programmatically](#oauth-details) for recommended guidance for fetching your OAuth token for production use cases.

From the **Serving** UI of your workspace:

1.  On the Serving endpoints page, select your route-optimized endpoint to see endpoint details.
2.  On the endpoint details page, select the **Use** button.
3.  Select the **Fetch Token** tab.
4.  Select **Fetch OAuth Token** button. This token is valid for 1 hour. Fetch a new token if your current token expires.

After you fetch the OAuth token, query your endpoint using your endpoint URL and OAuth token.

*   REST API
*   Python

The following is a REST API example:

Bash

    URL="<endpoint-url>"OAUTH_TOKEN="<token>"curl -X POST \  -H "Content-Type: application/json" \  -H "Authorization: Bearer $OAUTH_TOKEN" \  --data "@data.json" \  "$URL"

### Fetch an OAuth token programmatically[​](#fetch-an-oauth-token-programmatically "Direct link to fetch-an-oauth-token-programmatically")

For production scenarios, Databricks recommends setting up service principals to embed within your application to programmatically fetch OAuth tokens. These fetched tokens are used to query route-optimized endpoints.

Follow the steps in [Authorize service principal access to Databricks with OAuth](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m) through step 2 to create your service principal, assign permissions and create an OAuth secret for your service principal. After your service principal is created, you must give the service principal at least **Query permission** on the endpoint. See [Manage permissions on a model serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/manage-serving-endpoints#permissions).

The [Databricks Python SDK](https://databricks-sdk-py.readthedocs.io/en/latest/clients/workspace.html) provides an API to directly query a route-optimized endpoint.

The next example requires the following to query a route-optimized endpoint using the Databricks SDK:

*   Serving endpoint name (the SDK fetches the correct endpoint URL based on this name)
*   Service principal client ID
*   Service principal secret
*   Workspace hostname

Python

    from databricks.sdk import WorkspaceClientimport databricks.sdk.core as clientendpoint_name = "<Serving-Endpoint-Name>" ## Insert the endpoint name here# Initialize Databricks SDKc = client.Config(    host="<Workspace-Host>", ## For example, my-workspace.cloud.databricks.com    client_id="<Client-Id>", ## Service principal ID    client_secret="<Secret>"   ## Service principal secret)w = WorkspaceClient(    config = c)response = w.serving_endpoints_data_plane.query(endpoint_name, dataframe_records = ....)

### Fetch an OAuth token manually[​](#fetch-an-oauth-token-manually "Direct link to fetch-an-oauth-token-manually")

For scenarios where the Databricks SDK or the Serving UI can not be used to fetch your OAuth token, you can manually fetch an OAuth token. The guidance in this section mainly applies to scenarios where users have a customized client that they want to use for querying the endpoint in production.

When you fetch an OAuth token manually, you must specify `authorization_details` in the request.

*   Construct the `<token-endpoint-URL>` by replacing `https://<databricks-instance>` with the workspace URL of your Databricks deployment in `https://<databricks-instance>/oidc/v1/token`. For example, `https://my-workspace.cloud.databricks.com/oidc/v1/token`

*   Replace `<client-id>` with the service principal's client ID, which is also known as an application ID.
*   Replace `<client-secret>` with the service principal's OAuth secret that you created.

*   Replace `<endpoint-id>` with the endpoint ID of the route-optimized endpoint. This is the alpha-numeric ID of the endpoint that you can find in the `hostName` of the endpoint URL. For example, if the serving endpoint is `https://abcdefg.serving.cloud.databricks.com/9999999/serving-endpoints/test`, the endpoint ID is `abcdefg`.

*   Replace `<action>` with the action permission given to the service principal. The action can be `query_inference_endpoint` or `manage_inference_endpoint`.

*   REST API
*   Python

The following is a REST API example:

Bash

    export CLIENT_ID=<client-id>export CLIENT_SECRET=<client-secret>export ENDPOINT_ID=<endpoint-id>export ACTION=<action>  # for example, 'query_inference_endpoint'curl --request POST \--url <token-endpoint-URL> \--user "$CLIENT_ID:$CLIENT_SECRET" \--data 'grant_type=client_credentials&scope=all-apis'--data-urlencode 'authorization_details=[{"type":"workspace_permission","object_type":"serving-endpoints","object_path":"'"/serving-endpoints/$ENDPOINT_ID"'","actions": ["'"$ACTION"'"]}]'

After you fetch the OAuth token, query your endpoint using your endpoint URL and OAuth token.

*   REST API
*   Python

The following is a REST API example:

Bash

    URL="<endpoint-url>"OAUTH_TOKEN="<token>"curl -X POST \  -H "Content-Type: application/json" \  -H "Authorization: Bearer $OAUTH_TOKEN" \  --data "@data.json" \  "$URL"
