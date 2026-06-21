---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 775848e642ccf3034dacec5bef08b43f4fb5d38e2adeb50fc8c542d8b42894eb
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-idp-app-registration-for-delta-sharing
    - RIARFDS
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: Recipient IdP App Registration for Delta Sharing
description: The process of registering an OAuth application in a recipient's identity provider (e.g., Microsoft Entra ID) to enable OIDC-based authentication for Delta Sharing, including capturing issuer URL, subject claim, subject, and audience.
tags:
  - identity-provider
  - app-registration
  - microsoft-entra-id
  - databricks
timestamp: "2026-06-19T20:09:46.427Z"
---

# Recipient IdP App Registration for Delta Sharing

**Recipient IdP App Registration for Delta Sharing** describes the process a data recipient follows to register an OAuth application in their own identity provider (IdP) and configure it for OpenID Connect (OIDC) federation. This registration enables a secure, machine‑to‑machine (M2M) authentication flow between the recipient’s application and a Databricks provider that shares data via Delta Sharing (OpenSharing). ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

The M2M OAuth Client Credentials grant flow is typically used by autonomous applications—such as a nightly job running on a virtual machine—that need to access shared data without human interaction. The recipient’s IdP issues short‑lived JSON Web Tokens (JWTs) that Databricks authenticates. This approach is an alternative to using long‑lived Databricks bearer tokens for [Databricks‑to‑open sharing](/concepts/databricks-to-open-sharing.md) connections with non‑Databricks recipients. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Register an app in your IdP

Before a recipient can use OIDC federation to give a client application access to OpenSharing shares, the recipient must register an OAuth application in their IdP. The source material provides detailed steps for Microsoft Entra ID; for other IdPs, refer to their own documentation. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Register an app in Microsoft Entra ID

These steps are general guidance and should be verified against the latest Microsoft documentation:

1. Sign in to the Microsoft Entra admin center as at least an Application Developer.
2. Go to **App registrations** and create a new registration without a redirect URL.
3. Go to **Certificates & Secrets > Create a secret** for your app.
4. Copy and securely store the secret value.
5. On the **App registrations > Overview** page for the app, copy the **Application (client) ID**.
6. Modify the app to be a V2 application by updating the manifest:
   - In the app’s **Manage** section, select **Manifest**.
   - In the editor, set `accessTokenAcceptedVersion` to `2`.
   - Save the changes. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Send required information to the Databricks data provider

The recipient must share the following fields with the Databricks provider so the provider can configure OIDC federation for the recipient:

- **Issuer URL**: `https://login.microsoftonline.com/{tenantId}/v2.0`, replacing `{tenantId}` with the Entra tenant ID.
- **Subject Claim**: The field in the JWT payload that identifies the entity accessing the data. For M2M applications in Microsoft Entra ID, the subject claim is `azp`, representing the client ID of the authorized application.
- **Subject**: The unique identifier of the registered OAuth application in the recipient’s IdP. For Microsoft Entra ID, this is the **Application (client) ID**.
- **Audience**: A resource identifier for the Databricks endpoint. Typically the application’s `clientId` is used, but any valid resource identifier is acceptable.

The recipient sends these four values to the provider. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Configure the app to use the OAuth profile file

After the provider shares an OIDC profile portal URL with the recipient, the recipient configures the client application as follows:

1. Open the OIDC profile portal URL provided by the Databricks provider.
2. On the portal page, select the **M2M** tile and, under **For OAuth**, click **Download file**.
3. Modify the downloaded `oauth_config.share` JSON file by adding the recipient’s `clientId`, `clientSecret`, and `scope`.
   - The `clientId` and `clientSecret` come from the app registration.
   - If the audience is set to the `clientId`, the scope should be `{clientId}/.default`.
4. Save the updated `oauth_config.share` file.
5. Install the latest OpenSharing Python OSS client (version >= 1.3.1).
6. Create a test script that uses `delta_sharing.SharingClient(profile_file)` to list shared tables and verify the configuration.

Example profile file structure:

```json
{
  "shareCredentialsVersion": 2,
  "endpoint": "https://oregon.cloud.databricks.com/api/2.0/delta-sharing/metastores/...",
  "tokenEndpoint": "https://login.microsoftonline.com/.../oauth2/v2.0/token",
  "type": "oauth_client_credentials",
  "clientId": "[REPLACE_WITH_YOUR_CLIENT_ID]",
  "clientSecret": "[REPLACE_WITH_YOUR_CLIENT_SECRET]",
  "scope": "[REPLACE_WITH_YOUR_SCOPE]"
}
```

^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Related concepts

- [Open Sharing](/concepts/opensharing.md) – Databricks’ Delta Sharing protocol for sharing with non‑Databricks recipients.
- OIDC Federation – OpenID Connect federation for authentication.
- [Delta Sharing](/concepts/delta-sharing.md) – The open standard for secure data sharing.
- [Databricks‑to‑open sharing](/concepts/databricks-to-open-sharing.md) – Sharing data from Databricks to non‑Databricks consumers.
- [M2M OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) – The authentication flow used for autonomous applications.
- U2M Flow – User‑to‑machine OIDC flow for interactive access.

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
