---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0bebf5f95d882008c1e53f92345906f1534bf9a7761c9d63346fa31661b8fca2
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-federation-for-m2m-delta-sharing
    - OFFMDS
    - OIDC Federation for U2M Delta Sharing
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: OIDC Federation for M2M Delta Sharing
description: Using Open ID Connect federation with the OAuth Client Credentials grant flow to let non-Databricks recipients authenticate to Delta Sharing shares without long-lived bearer tokens.
tags:
  - delta-sharing
  - authentication
  - oidc
  - databricks
timestamp: "2026-06-19T20:10:49.315Z"
---

# OIDC Federation for M2M Delta Sharing

**OIDC Federation for M2M Delta Sharing** is an authentication mechanism that enables data recipients to access [OpenSharing](/concepts/opensharing.md) shares created in Databricks using OpenID Connect (OIDC) federation with a machine-to-machine (M2M) OAuth Client Credentials grant flow. This approach allows applications—such as nightly batch jobs running on virtual machines—to autonomously access shared data without requiring long-lived secrets or bearer tokens. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Overview

In the M2M OIDC federation flow, the recipient's identity provider (IdP) issues JSON Web Tokens (JWTs) that serve as short-lived OAuth tokens. Databricks authenticates these tokens, enabling secure access to shared data. This flow is designed for recipients who do not have access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace, making it suitable for non-Databricks recipients connecting to Databricks providers. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

Open OIDC federation serves as an alternative to using long-lived Databricks-issued bearer tokens for connecting non-Databricks recipients to providers. In the OAuth Client Credentials grant flow, an OAuth application is registered as a Service Principal (SP) in the recipient's IdP. No long-lived secrets or credentials are shared between Databricks, the provider, and the recipient. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Prerequisites

Before using OIDC federation for M2M Delta Sharing, the recipient must:

1. **Register an OAuth application** in their identity provider (IdP).
2. **Send required information** to the Databricks data provider.
3. **Configure the app** using the OAuth profile file shared by the provider.

## Registering an App in Your IdP

The first step is to register an OAuth application in your IdP. The documentation provides specific guidance for Microsoft Entra ID.

### Registering in Microsoft Entra ID

1. Sign in to the Microsoft Entra admin center as at least an Application Developer.
2. Go to **App registrations** and create a new registration without a redirect URL.
3. Go to **Certificates & Secrets > Create a secret** for your app.
4. Copy the secret value and store it securely.
5. On the **App registrations > Overview** page, copy the **Application (client) ID**.
6. Modify the app to be a V2 application by updating the manifest:
   - In the app's **Manage** section, select **Manifest**.
   - Set `accessTokenAcceptedVersion` to `2`.
   - Save the changes.

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Providing Information to the Databricks Provider

The recipient must share the following fields with the Databricks data provider, who will use them to configure the recipient's OIDC federation settings:

- **Issuer URL**: For Microsoft Entra ID, this is `https://login.microsoftonline.com/{tenantId}/v2.0`, replacing `{tenantId}` with your Entra tenant ID.
- **Subject Claim**: The field in the JWT payload that identifies the entity accessing the data. For M2M applications in Microsoft Entra ID, the subject claim is `azp`, which represents the client ID of the authorized application.
- **Subject**: The unique identifier of the registered OAuth application in the recipient's IdP. In Microsoft Entra ID, this is the **Application (client) ID**.
- **Audience**: For machine-to-Databricks authentication, typically the resource's `clientId` is used, but any other valid resource identifier can be specified.

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Configuring the App with the OAuth Profile File

After the provider has configured the recipient, the recipient receives an OIDC profile portal URL. The configuration process is as follows:

1. Go to the OIDC profile portal URL shared by the provider.
2. On the portal page, select the **M2M** tile and, under **For OAuth**, click **Download file**.
3. Modify the downloaded `oauth_config.share` JSON file to add your `clientId`, `clientSecret`, and `scope`.

If the audience is set to the app's `{clientId}`, the scope should be `{clientId}/.default`. For example, if the audience is `61a80fb9-ce0c-4794-9f7f-2ba42a7b76f6`, the scope should be `61a80fb9-ce0c-4794-9f7f-2ba42a7b76f6/.default`. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Sample Profile

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

## Setting Up the OpenSharing Python Client

You must have the latest version of the OpenSharing Python OSS client installed:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install "delta-sharing>=1.3.1"
```

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Testing the Configuration

Create a test script to verify the connection:

```python
import delta_sharing

# Point to the profile file
profile_file = "oauth_config.share"

# Create a SharingClient
client = delta_sharing.SharingClient(profile_file)

# List all shared tables
tables = client.list_all_tables()
print(tables)
```

Save the file as `test.py` and run it. The script should successfully list the shared tables, confirming that the OIDC federation configuration is working correctly. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms.
- [Open Sharing Recipient](/concepts/opensharing-recipient.md) — The recipient entity that receives shared data.
- [Bearer Token Authentication for Delta Sharing](/concepts/bearer-token-authentication-for-delta-sharing.md) — An alternative authentication method using long-lived tokens.
- OIDC Federation for U2M Delta Sharing — The user-to-machine variant of this authentication flow.
- Service Principal (SP) — The identity used by applications to authenticate in OAuth flows.
- JSON Web Token (JWT) — The token format used in OIDC federation.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
