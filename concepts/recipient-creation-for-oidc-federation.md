---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b71f33be3a5fc1b05eb67f578f8f1a60fed2a410e48c22ba70d6d38f5129bbad
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-creation-for-oidc-federation
    - RCFOF
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Recipient Creation for OIDC Federation
description: Step-by-step process in Databricks Catalog for creating an Open recipient with OIDC authentication method, configuring federation policy, and sharing the OIDC profile portal URL with the recipient.
tags:
  - administration
  - delta-sharing
  - workflow
timestamp: "2026-06-19T10:21:41.086Z"
---

# Recipient Creation for OIDC Federation

**Recipient Creation for OIDC Federation** refers to the process by which a data provider in Databricks creates a recipient object configured to use OpenID Connect (OIDC) token federation for authentication to [OpenSharing](/concepts/opensharing.md) shares. This method allows recipients without a Unity Catalog-enabled Databricks workspace to authenticate using JSON Web Tokens (JWTs) issued by their own identity provider (IdP), eliminating the need for long-lived bearer tokens. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How OIDC Federation Works in OpenSharing

When the data provider creates a recipient, they configure an OIDC token federation policy that specifies the issuer URL of the recipient’s IdP and defines the identities (user, group, service principal, or OAuth application) that should have access to the share. Databricks generates an OIDC profile web portal URL based on the policy. The provider shares this URL (or a downloadable profile file) with the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

When the recipient attempts to access shared data, their IdP issues a short-lived JWT containing identity claims. Databricks does not generate or manage these tokens; it validates the JWT against the recipient’s policy to ensure it matches expected claims (issuer, audience, subject). Upon successful validation, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

OIDC federation supports two authentication flows:

- **User-to-Machine (U2M)**: A user authenticates via their IdP (with MFA if configured) and accesses data using tools like Power BI or Tableau, using the OAuth Authorization Code Grant flow. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Machine-to-Machine (M2M)**: A service principal in the recipient’s IdP enables automated workloads (e.g., nightly jobs) to access data programmatically using the OAuth Client Credentials Grant flow. No secrets are exchanged between Databricks and the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Prerequisites

To create a recipient that uses OIDC federation, you must meet the following requirements: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- You must have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data is registered.
- You must create the recipient using a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached.
- If using a notebook, compute must use Databricks Runtime 11.3 LTS or above with standard or dedicated access mode.

## Step 1: Create an Open OIDC Federation Recipient

1. In your Databricks workspace, click **Catalog**.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (or click **Share > OpenSharing**).
3. On the **Shared by me** tab, click **New recipient**.
4. Enter a **Recipient name**.
5. For **Recipient type**, select **Open**.
6. Choose **OIDC Federation** as the authentication method.
7. Click **Create**.
8. (Optional) Add custom recipient properties on the **Details** tab.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Step 2: Create an OIDC Federation Policy

Before creating the policy, obtain information from the recipient (or your own internal IdP for internal sharing) about the IdP and the identities to be granted access. The policy defines the following: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **Policy name**: Human-readable name.
- **Issuer URL**: The HTTPS URL of the IdP issuing the JWT.
- **Subject claim**: The claim identifying the authenticating identity type:
  - For U2M in Microsoft Entra ID: use `oid` (object ID) for a user, `groups` for a group.
  - For M2M: use `azp` for an OAuth application.
- **Subject**: The specific user, group, or application allowed access (e.g., the object ID or client ID).
- **Audiences**: One or more resource identifiers the JWT’s `aud` claim must match.

After gathering the details, click **Add policy** under **OIDC federation policies**, enter the values, and save. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Example: U2M with Microsoft Entra ID

Sharing with a specific user (object ID `11111111-2222-3333-4444-555555555555`) in tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `oid`
- Subject: `11111111-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138` (multi-tenant app ID registered by Databricks in Entra ID)

Sharing with a group (object ID `66666666-2222-3333-4444-555555555555`): ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Subject claim: `groups`
- Subject: `66666666-2222-3333-4444-555555555555`

### Example: M2M with Microsoft Entra ID

For a service principal with application (client) ID `11111111-2222-3333-4444-555555555555` in the same tenant: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Subject claim: `azp`
- Subject: `11111111-2222-3333-4444-555555555555` (client ID of the registered OAuth application)
- Audiences: `66666666-2222-3333-4444-555555555555` (any valid audience defined by the recipient, such as the same client ID)

## Granting Access to Shares

After creating the recipient and creating shares, grant the recipient access to those shares using Catalog Explorer, the Databricks Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin, or delegated permissions/ownership on both the share and recipient objects. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Sharing the Iceberg OIDC Profile Portal Link

If the recipient will read data using an Iceberg REST catalog, provide them with the Iceberg OIDC profile generation portal link: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

1. In Catalog > OpenSharing > **Recipients**, select the OIDC recipient.
2. Under **OIDC federation policies**, click **Default OIDC policy**.
3. Copy the **Iceberg OIDC profile generation portal** link and share it securely with the recipient. The link includes share names needed to read data.

## Recipient Workflow

Recipients authenticate using OIDC token federation as described in the following guides: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- [Read data shared using OIDC federation in a U2M flow](/concepts/opensharing-using-oidc-federation.md)
- Read data shared using OIDC federation in an M2M flow

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol used.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that governs access.
- JWT – The token format used by the recipient’s IdP.
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md) – The external or internal provider issuing JWTs.
- Bearer Token Recipient Creation – The alternative authentication method using long-lived tokens.

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
