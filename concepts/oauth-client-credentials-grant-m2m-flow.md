---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 411d14d8f9eeb78dc7d337a48d30e34750f251a5679e01fe78948f7dc321daef
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oauth-client-credentials-grant-m2m-flow
    - OCCG(F
    - M2M OAuth Client Credentials Grant
    - OAuth 2.0 Client Credentials Grant
    - OAuth Client Credentials Grant
    - OAuth Client Credentials Grant Flow
    - OAuth Client Credentials Grant flow
    - Machine-to-Machine (M2M) OAuth Client Credentials Grant Flow
    - OAuth Client Credentials
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: OAuth Client Credentials Grant (M2M) Flow
description: A machine-to-machine authentication flow where an application (nightly job, VM) uses client credentials to obtain short-lived JWTs from an IdP, used as OAuth tokens to access Databricks Delta Sharing endpoints.
tags:
  - oauth
  - authentication
  - m2m
  - databricks
timestamp: "2026-06-19T20:09:43.868Z"
---

# OAuth Client Credentials Grant (M2M) Flow

The **OAuth Client Credentials Grant (M2M) Flow** is a machine-to-machine authentication method used by non-Databricks recipients to access [Delta Sharing](/concepts/delta-sharing.md) shares opened by a Databricks provider. It relies on OIDC Federation and OpenSharing, allowing a client application registered in the recipient’s own [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md) to obtain short-lived OAuth tokens (JSON Web Tokens) that Databricks validates. This flow is an alternative to using long-lived, Databricks-issued Bearer Tokens for Databricks-to-Open sharing. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Overview

The M2M flow is designed for autonomous applications—such as a nightly job running on a virtual machine—that need to read shared data without user intervention. The recipient’s IdP issues short-lived JWTs that act as OAuth tokens, eliminating the need to exchange long-lived secrets or credentials between Databricks, the provider, and the recipient. This flow is intended for recipients who do **not** have access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. For recipients who do have such a workspace, a different, Databricks-to-Databricks flow is available. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

A companion flow, the [User-to-Machine (U2M) Flow](/concepts/user-to-machine-u2m-authentication-flow.md), handles interactive user authentication instead of application-level access.

## Prerequisites and Workflow

To set up an M2M flow, the recipient must:

1. Register an OAuth application in their own IdP (for example, Microsoft Entra ID).
2. Share specific information (issuer URL, subject claim, subject, and audience) with the Databricks data provider.
3. Obtain an OIDC profile portal URL from the provider.
4. Download and modify the `oauth_config.share` file, adding the application’s `clientId`, `clientSecret`, and `scope`.
5. Use the modified profile file with the OpenSharing Python OSS client to connect and read shares.

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Registering an App in the Identity Provider (Microsoft Entra ID Example)

The source provides a specific example for Microsoft Entra ID. The recipient must:

- Sign in to the Microsoft Entra admin center as at least an Application Developer.
- Create a new app registration (no redirect URL is needed).
- Under **Certificates & Secrets**, create a client secret and store its value securely.
- Copy the **Application (client) ID** from the **Overview** page.
- Update the app manifest to set `accessTokenAcceptedVersion` to `2` (V2 application).

For other IdPs, the recipient should follow their respective documentation. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Providing Information to the Databricks Data Provider

After registration, the recipient must supply the following fields to the provider:

| Field | Description | Microsoft Entra ID Example |
|-------|-------------|----------------------------|
| **Issuer URL** | The URL that identifies the IdP’s token issuer. | `https://login.microsoftonline.com/{tenantId}/v2.0` (replace `{tenantId}` with the tenant ID) |
| **Subject Claim** | The JWT payload field that identifies the entity accessing the data. For M2M in Entra ID, this is `azp` (the authorized party, i.e., the client ID). | `azp` |
| **Subject** | The unique identifier of the registered OAuth application in the recipient’s IdP. | The **Application (client) ID** |
| **Audience** | The resource identifier that the token is intended for. Typically the application’s `clientId`, but any valid resource ID can be used. | The **Application (client) ID** |

The provider uses these values to set up the recipient’s OIDC federation configuration on the Databricks side. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Configuring the OAuth Profile File

Once the provider shares the OIDC profile portal URL, the recipient must:

1. Navigate to the portal URL, select the **M2M** tile, and click **Download file** under **For OAuth**.
2. Open the downloaded `oauth_config.share` JSON file and replace the placeholder values for `clientId`, `clientSecret`, and `scope`.

The `scope` must be `{clientId}/.default` when using the application’s client ID as the audience. A sample profile file looks like:

```json
{
  "shareCredentialsVersion": 2,
  "endpoint": "https://oregon.cloud.databricks.com/api/2.0/delta-sharing/metastores/.../recipients/...",
  "tokenEndpoint": "https://login.microsoftonline.com/.../oauth2/v2.0/token",
  "type": "oauth_client_credentials",
  "clientId": "[REPLACE_WITH_YOUR_CLIENT_ID]",
  "clientSecret": "[REPLACE_WITH_YOUR_CLIENT_SECRET]",
  "scope": "[REPLACE_WITH_YOUR_SCOPE]"
}
```

The file must then be saved in a secure location accessible to the client application. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Testing the Configuration

The recipient should install the latest OpenSharing Python OSS client (`delta-sharing>=1.3.1`) and create a test script. The script uses the profile file to create a `SharingClient`, list all shared tables, and optionally read sample data:

```python
import delta_sharing

profile_file = "oauth_config.share"
client = delta_sharing.SharingClient(profile_file)
tables = client.list_all_tables()
print(tables)
```

Running the script successfully lists the shared tables, confirming that the OAuth Client Credentials grant flow is properly configured. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for secure real-time data sharing.
- OpenID Connect (OIDC) – Authentication layer used for federation.
- [OAuth 2.0 Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) – The underlying OAuth flow.
- Bearer Tokens – Long-lived alternative used in Databricks-to-Open sharing without OIDC.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ [Metastore](/concepts/metastore.md); presence of Unity Catalog changes the recommended recipient flow.
- [User-to-Machine (U2M) Flow](/concepts/user-to-machine-u2m-authentication-flow.md) – The interactive counterpart to M2M.
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md) – The system that issues identity tokens (e.g., Microsoft Entra ID).
- Service Principal – Representation of an application in an IdP.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
