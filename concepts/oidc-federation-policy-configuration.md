---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4f241b104a5c2c457cc390035c9fa1f71c5d9b279c92e74dcd7fb91f9c68cb76
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-federation-policy-configuration
    - OFPC
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: OIDC Federation Policy Configuration
description: A policy object in Databricks that maps JWT claims (issuer, subject, audience) from a recipient's IdP to access permissions, specifying the issuer URL, subject claim type (oid, groups, or azp), subject value, and allowed audiences.
tags:
  - configuration
  - policy
  - delta-sharing
timestamp: "2026-06-18T15:37:00.450Z"
---

# OIDC Federation Policy Configuration

**OIDC Federation Policy Configuration** enables data providers in Databricks to federate authentication to an identity provider (IdP) for governing access to OpenSharing shares. Using OpenID Connect (OIDC) federation, JSON Web Tokens (JWTs) issued by the recipient’s IdP serve as short-lived OAuth tokens authenticated by Databricks. This authentication method is designed for recipients who do not have access to a Unity Catalog–enabled Databricks workspace. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

OIDC federation is an alternative to using long-lived Databricks-issued bearer tokens. It enables fine-grained access control, supports Multi-Factor Authentication (MFA), and reduces security risks by eliminating the need for recipients to manage and secure shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How OIDC Federation Works in OpenSharing

1. The data provider creates a recipient in OpenSharing and configures an OIDC token federation policy that specifies the issuer URL of the recipient IdP (for example, Microsoft Entra ID or Okta) and defines which recipient user, group, service principal, or OAuth application should have access to the share.
2. Databricks generates an OIDC profile web portal URL based on the policy. The provider shares this URL with the recipient. For user-to-machine (U2M) authentication, the recipient inputs the endpoint into their U2M application. For machine-to-machine (M2M) authentication, the recipient application developer downloads a profile file and references it in the client app.
3. When the recipient attempts to access shared data, authentication is federated to their IdP. The recipient’s IdP generates a JWT containing identity claims. The OpenSharing service validates the JWT against the recipient’s policy to ensure it matches expected claims (issuer, audience, subject). If validation succeeds, access is granted based on Unity Catalog permissions.

Databricks does not generate or manage tokens; the lifetime of the JWT is enforced by the recipient’s IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Identity Provider Options

Data providers can use either an **internal IdP** (provider-managed) or an **external IdP** (recipient-managed):

- **Internal (Provider-Managed):** Useful for sharing within large organizations where different departments do not have direct Databricks access but share the same IdP. Security policies like MFA and role-based access control are enforced by the provider’s IdP.
- **External (Recipient-Managed):** The provider configures the policy to trust the recipient’s IdP. The recipient organization retains full control over who can access shared data, and security policies are enforced by the recipient’s IdP.

## Authentication Scenarios

OIDC federation supports two flows:

- **User-to-Machine (U2M):** A user from the recipient organization authenticates via their IdP (MFA enforced if configured). After authentication, users can access shared data using tools like Power BI or Tableau. U2M clients use the OAuth Authorization Code Grant flow.
- **Machine-to-Machine (M2M):** For automated workloads, the recipient organization registers a service principal in its IdP. No secrets or credentials are exchanged between parties. M2M clients (e.g., Python OpenSharing Client, Spark OpenSharing Client) use the OAuth Client Credentials Grant flow.

## Before You Begin

To create a recipient, you must have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data is registered. You must create the recipient using a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached. If you use a Databricks notebook, your compute must use Databricks Runtime 11.3 LTS or above and either standard or dedicated access mode. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Create a Recipient That Uses an OIDC Federation Policy

### Step 1: Create an Open OIDC Federation Recipient

1. In your Databricks workspace, click **Catalog**.
2. At the top of the Catalog pane, click the gear icon and select **OpenSharing**. Alternatively, click **Share > OpenSharing** in the upper-right corner.
3. On the **Shared by me** tab, click **New recipient**.
4. Enter a **Recipient name**, select **Open** as the **Recipient type**, and choose **OIDC Federation** as the **Authentication method**.
5. Click **Create**.
6. (Optional) Create custom **Recipient properties** on the recipient **Details** tab.

### Step 2: Create the OIDC Federation Policy

Gather from the recipient (or from your own IdP for internal sharing) the necessary information about the IdP, including which users, groups, service principals, or OAuth applications should have access.

1. On the recipient edit page, under **OIDC federation policies**, click **Add policy**.
2. Enter the following fields:

| Field | Description |
|-------|-------------|
| **Policy name** | Human-readable name for the policy. |
| **Issuer URL** | The HTTPS URL of the IdP that issues the JWT. |
| **Subject claim** | The claim in the JWT that identifies the authenticating identity type. For Microsoft Entra ID, common values are `oid` (Object ID) for individual users, `groups` for groups, and `azp` for OAuth applications. Other IdPs may use `sub` or other claims. |
| **Subject** | The specific user, group, or application allowed to access the share. |
| **Audiences** | One or more resource identifiers the JWT must match. A token is valid if its `aud` claim matches any listed audience. |

3. Click **Save**.

After the recipient is created, you can [create shares](https://docs.databricks.com/aws/en/delta-sharing/create-share) and grant the recipient access using Catalog Explorer, the Databricks Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin, or delegated permissions/ownership on both the share and the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

If the OIDC recipient is reading shared data using an Iceberg REST catalog, share the **Iceberg OIDC profile generation portal** link. Copy this link from the recipient’s default OIDC policy page and send it to the recipient securely. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Example Policy Configurations for Microsoft Entra ID

### U2M – Sharing with a Specific User

- **Issuer:** `https://login.microsoftonline.com/<tenant-id>/v2.0`
- **Subject claim:** `oid` (Object ID)
- **Subject:** The user’s Object ID (e.g., `11111111-2222-3333-4444-555555555555`)
- **Audiences:** `64978f70-f6a6-4204-a29e-87d74bfea138` (multi-tenant app ID registered by Databricks in Entra ID)

### U2M – Sharing with a Group

- **Issuer:** `https://login.microsoftonline.com/<tenant-id>/v2.0`
- **Subject claim:** `groups`
- **Subject:** The group’s Object ID (e.g., `66666666-2222-3333-4444-555555555555`)
- **Audiences:** `64978f70-f6a6-4204-a29e-87d74bfea138`

For U2M applications like Power BI and Tableau, the audience must be the Databricks multi-tenant app ID. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### M2M – Sharing with an OAuth Application (Service Principal)

- **Issuer:** `https://login.microsoftonline.com/<tenant-id>/v2.0`
- **Subject claim:** `azp`
- **Subject:** The Application (client) ID of the registered OAuth application (e.g., `11111111-2222-3333-4444-555555555555`)
- **Audiences:** Any valid audience identifier defined by the recipient (e.g., the same client ID). For more information, see [Read data shared using OIDC federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m).

## Recipient Workflow

For details on how recipients authenticate and access shares using OIDC token federation, see:

- [U2M OIDC Data Access](/concepts/unity-catalog-access-control-models.md) – Read data shared using OIDC federation in a U2M flow
- M2M OIDC Data Access – Read data shared using OIDC federation in an M2M flow

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – Databricks-to-open sharing authentication methods
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md) – Alternative use of long-lived tokens
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying data sharing protocol
- OAuth 2.0 – The authorization framework used by OIDC flows
- JSON Web Token (JWT) – The token format issued by the IdP
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that enforces access after authentication

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
