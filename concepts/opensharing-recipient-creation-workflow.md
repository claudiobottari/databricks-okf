---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 09644cf1289b42b407caa9a2118288623c74a1479afff6564ab957da03785535
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-recipient-creation-workflow
    - ORCW
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: OpenSharing Recipient Creation Workflow
description: Step-by-step process for data providers to create an OIDC-based recipient in Databricks, configure federation policy, and share an OIDC profile portal URL with the recipient.
tags:
  - workflow
  - delta-sharing
  - administration
timestamp: "2026-06-19T18:40:42.461Z"
---

# OpenSharing Recipient Creation Workflow

The **OpenSharing Recipient Creation Workflow** describes the process by which a data provider on Databricks creates a recipient object that uses Open ID Connect (OIDC) federation to authenticate access to [OpenSharing](/concepts/opensharing.md) shares. This workflow enables providers to delegate authentication to a recipient’s identity provider (IdP), eliminating the need for long-lived bearer tokens and supporting features such as Multi-Factor Authentication (MFA) and fine-grained access control. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Prerequisites

To create a recipient, the provider must meet the following requirements:

- Have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered.
- Create the recipient using a Databricks workspace that is attached to that [Metastore](/concepts/metastore.md).
- If using a notebook, the compute must run Databricks Runtime 11.3 LTS or above and use standard or dedicated access mode. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Provider Workflow

### Step 1: Create the Recipient

1. In the Databricks workspace, navigate to **Catalog** and click the gear icon, then select **OpenSharing** (or use **Share > OpenSharing** in the top-right corner).
2. Go to the **Shared by me** tab and click **New recipient**.
3. Enter a **Recipient name**.
4. For **Recipient type**, select **Open**.
5. Choose **OIDC Federation** as the **Authentication method**.
6. Click **Create**.
7. (Optional) Add custom recipient properties under the recipient’s **Details** tab by clicking **Edit properties > +Add property** and entering a key and value.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 2: Create an OIDC Federation Policy

Before configuring the policy, gather from the recipient (or from your own internal IdP if sharing internally) the necessary information about the IdP, users, groups, service principals, or OAuth applications that should have access.

1. On the recipient edit page, under **OIDC federation policies**, click **Add policy**.
2. Enter the following fields:
   - **Policy name**: A human-readable name.
   - **Issuer URL**: The HTTPS URL of the IdP that issues the JWT (e.g., `https://login.microsoftonline.com/<tenant-id>/v2.0`).
   - **Subject claim**: The JWT claim that identifies the authenticating identity. For Microsoft Entra ID:
     - `oid` (Object ID) for a specific user in a U2M flow.
     - `groups` for a group in a U2M flow.
     - `azp` for an OAuth application in an M2M flow.
     Other IdPs may use claims like `sub`.
   - **Subject**: The specific user, group, or application identifier (e.g., the Object ID of a user or Application (client) ID of an OAuth app).
   - **Audiences**: One or more resource identifiers the JWT’s `aud` claim must match. For U2M applications like Power BI or Tableau, use Databricks’ multi-tenant app ID (`64978f70-f6a6-4204-a29e-87d74bfea138`). For M2M, use a valid audience defined by the recipient.
3. Click **Save**.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 3: Grant Access to Shares

After the recipient is created, the provider must grant access to specific shares. Permissions required: [Metastore](/concepts/metastore.md) admin, or delegated permissions/ownership on both the share and the recipient objects (`USE SHARE` + `SET SHARE PERMISSION` or share owner, and `USE RECIPIENT` or recipient owner). Access can be granted using Catalog Explorer, the Unity Catalog CLI, or the SQL command `GRANT ON SHARE`. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

The provider then shares the **OIDC profile generation portal** URL with the recipient. This URL is found under the recipient’s **OIDC federation policies** section (click **Default OIDC policy**). The link also includes the names of the shares. For Iceberg REST catalog use cases, share the **Iceberg OIDC profile generation portal** link instead. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Recipient Workflow

Recipients authenticate and access shares using the OIDC federation URL or profile file provided by the data provider. The authentication flow depends on the scenario:

- **User-to-Machine (U2M)**: The end user enters the endpoint URL into their application (e.g., Power BI, Tableau). The application uses the Manual OAuth token fetch with authorization_details|OAuth Authorization Code Grant flow to obtain tokens from the recipient’s IdP.
- **Machine-to-Machine (M2M)**: The application developer downloads the profile file and references it in the client app. The app uses the [OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) flow to obtain tokens from the IdP.

The recipient’s IdP is responsible for generating short-lived JWTs and enforcing security policies such as MFA. Databricks validates the JWT against the federation policy to confirm the expected claims (issuer, audience, subject) before granting access. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Detailed recipient instructions are provided in the following pages:

- [Read data shared using OIDC federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m)
- [Read data shared using OIDC federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m)

## Examples

### U2M with Microsoft Entra ID

When sharing with a specific user (Object ID `11111111-2222-3333-4444-555555555555`) in tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `oid`
- **Subject**: `11111111-2222-3333-4444-555555555555`
- **Audiences**: `64978f70-f6a6-4204-a29e-87d74bfea138`

When sharing with a group (Object ID `66666666-2222-3333-4444-555555555555`):

- **Issuer**: same as above
- **Subject claim**: `groups`
- **Subject**: `66666666-2222-3333-4444-555555555555`
- **Audiences**: `64978f70-f6a6-4204-a29e-87d74bfea138`

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### M2M with Microsoft Entra ID

When sharing with an OAuth application (Application (client) ID `11111111-2222-3333-4444-555555555555`) in tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `azp`
- **Subject**: `11111111-2222-3333-4444-555555555555` (the Application ID)
- **Audiences**: `66666666-2222-3333-4444-555555555555` (a valid audience defined by the recipient)

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- OIDC Federation
- JSON Web Token (JWT)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)
- Recipient Object
- Share Access Control (GRANT ON SHARE)
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md)

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
