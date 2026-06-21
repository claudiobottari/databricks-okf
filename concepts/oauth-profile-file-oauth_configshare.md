---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 607563e0e95837b6683191148e6c0615812de864316707eca70cb8040f30eb72
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oauth-profile-file-oauth_configshare
    - OPF(
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: OAuth Profile File (oauth_config.share)
description: A JSON configuration file downloaded from the OIDC profile portal containing endpoint, tokenEndpoint, client credentials, and scope, used to configure the Delta Sharing Python client for OIDC-based access.
tags:
  - configuration
  - delta-sharing
  - oauth
  - profile-file
timestamp: "2026-06-19T20:09:55.186Z"
---

# OAuth Profile File (oauth_config.share)

The **OAuth Profile File** (`oauth_config.share`) is a JSON configuration file used in [Delta Sharing](/concepts/delta-sharing.md) to enable Open ID Connect (OIDC) Federation authentication for data recipients who do not have access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. This file is downloaded from the OIDC profile portal URL provided by the Databricks data provider and must be modified by the recipient before use. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## File Structure

The `oauth_config.share` file contains the following fields:

- `shareCredentialsVersion`: The version of the credentials format (typically `2`).
- `endpoint`: The Databricks API endpoint URL for the Delta Sharing recipient.
- `tokenEndpoint`: The OAuth token endpoint URL from the recipient's identity provider (IdP), such as Microsoft Entra ID.
- `type`: The authentication flow type, set to `oauth_client_credentials` for machine-to-machine (M2M) flows.
- `clientId`: The application (client) ID from the recipient's registered OAuth application in their IdP. This field must be filled in by the recipient.
- `clientSecret`: The secret value generated during app registration in the recipient's IdP. This field must be filled in by the recipient.
- `scope`: The OAuth scope for the token request, typically formatted as `{clientId}/.default`. This field must be filled in by the recipient.

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Usage

To use the OAuth profile file:

1. Request the OIDC profile portal URL from the Databricks data provider if not already received.
2. Navigate to the portal URL and select the **M2M** tile, then under **For OAuth**, click **Download file** to obtain the `oauth_config.share` file.
3. Modify the downloaded file by replacing the placeholder values for `clientId`, `clientSecret`, and `scope` with the actual values from your registered OAuth application in your IdP.
4. Save the updated file.
5. Use the file with the OpenSharing Python OSS client (version 1.3.1 or later) to create a `SharingClient` and access shared data.

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Sample Configuration

```json
{
  "shareCredentialsVersion": 2,
  "endpoint": "https://oregon.cloud.databricks.com/api/2.0/delta-sharing/metastores/11a11aaa-11aa-11a12-11aa-111a1aa11111/recipients/a11da11aa1-a1a1-11a1-a11a-1111a11111aa",
  "tokenEndpoint": "https://login.microsoftonline.com/a111a111-1111-1aaa-1aa1-1aa1111aa1/oauth2/v2.0/token",
  "type": "oauth_client_credentials",
  "clientId": "[REPLACE_WITH_YOUR_CLIENT_ID]",
  "clientSecret": "[REPLACE_WITH_YOUR_CLIENT_SECRET]",
  "scope": "[REPLACE_WITH_YOUR_SCOPE]"
}
```

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Authentication Flow

The OAuth profile file enables a [Machine-to-Machine (M2M) OAuth Client Credentials Grant Flow](/concepts/oauth-client-credentials-grant-m2m-flow.md), where an application (such as a nightly job running on a virtual machine) accesses data autonomously. The recipient's IdP issues JSON Web Tokens (JWTs) that serve as short-lived OAuth tokens, which Databricks authenticates. This approach eliminates the need for long-lived Databricks-issued bearer tokens or shared secrets between Databricks, the provider, and the recipient. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- Open ID Connect (OIDC) Federation — The authentication framework used by this profile
- [OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) — The authorization flow type specified in the profile
- Service Principal (SP) — The identity type registered in the recipient's IdP
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — An alternative authentication method for Delta Sharing recipients
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) — The sharing model that uses this authentication approach

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
