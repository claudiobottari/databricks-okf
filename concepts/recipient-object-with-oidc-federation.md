---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 95c9d49aee77cb77b740c07e67eccfdbed4546804aa7c157904e069b70863df2
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recipient-object-with-oidc-federation
    - ROWOF
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Recipient Object with OIDC Federation
description: A Databricks Unity Catalog recipient object configured for OIDC-based authentication, generated with a profile URL or downloadable profile file that contains no sensitive information.
tags:
  - delta-sharing
  - recipient
  - oidc
  - databricks
timestamp: "2026-06-18T12:11:11.621Z"
---

# Recipient Object with OIDC Federation

A **Recipient Object with OIDC Federation** is a [Delta Sharing](/concepts/delta-sharing.md) recipient in [OpenSharing](/concepts/opensharing.md) that authenticates using OpenID Connect (OIDC) federation. Instead of using long-lived Databricks-issued bearer tokens, the recipient’s identity provider (IdP) issues short-lived JSON Web Tokens (JWTs). Databricks validates the JWT against the recipient’s configured federation policy; it does not generate or manage the tokens. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

OIDC federation enables fine-grained access control, supports multi-factor authentication (MFA), and reduces security risks by eliminating the need to share and manage static credentials across organizations. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How OIDC Federation Works in OpenSharing

1. The data provider creates a recipient in OpenSharing and configures an OIDC token federation policy that specifies:
   - The issuer URL of the recipient’s IdP (e.g., Microsoft Entra ID or Okta).
   - The user, group, service principal, or OAuth application that should have access to the share.
2. Databricks generates an OIDC profile web portal URL based on the policy. The provider shares this URL or a downloadable profile file with the recipient.
   - For [User-to-Machine Authentication](/concepts/user-to-machine-u2m-authentication.md), the recipient inputs the endpoint URL into their U2M application (e.g., Power BI, Tableau).
   - For [Machine-to-Machine Authentication](/concepts/machine-to-machine-m2m-authentication.md), the developer downloads the profile file and references it in the recipient client app.
3. When the recipient attempts to access shared data, the authentication is federated to the recipient’s IdP. The IdP generates a JWT containing identity claims. The OpenSharing service validates the JWT against the recipient’s policy (checking issuer, audience, and subject). If validation succeeds, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Prerequisites

- The provider must have the `CREATE RECIPIENT` privilege for the Unity Catalog [Metastore](/concepts/metastore.md) where the shared data is registered.
- The recipient must be created from a Databricks workspace that has that [Metastore](/concepts/metastore.md) attached.
- If using a notebook, the compute must run Databricks Runtime 11.3 LTS or above with standard or dedicated access mode. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Identity Provider Options

OIDC federation can be configured with either an **internal** or **external** IdP:

- **Internal (Provider-Managed)** – The provider manages access on behalf of the recipient using their own IdP. Useful for sharing within large organizations where departments share the same IdP but do not have direct Databricks access.
- **External (Recipient-Managed)** – The provider trusts the recipient’s IdP. The recipient organization retains full control over user access, MFA, and role-based policies. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Scenarios

### User-to-Machine (U2M) Authentication
A user from the recipient organization authenticates via their IdP, with MFA enforced if configured. Once authenticated, the user can access shared data using tools like Power BI or Tableau. The U2M client uses the OAuth Authorization Code Grant flow. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Machine-to-Machine (M2M) Authentication
Intended for automated workloads such as nightly jobs or background services. The recipient registers a service principal in their IdP. Scripts or apps authenticate without user interaction using the OAuth Client Credentials Grant flow. No secrets are exchanged between Databricks and the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Creating a Recipient with OIDC Federation

### Step 1: Create the Recipient Object

1. In the Databricks workspace, click **Catalog**.
2. Open **OpenSharing** from the gear icon (or click **Share > OpenSharing**).
3. On the **Shared by me** tab, click **New recipient**.
4. Enter a **Recipient name**.
5. Set **Recipient type** to **Open**.
6. Choose **OIDC Federation** as the authentication method.
7. Click **Create**.
8. Optionally add custom **Recipient properties** on the **Details** tab. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 2: Create an OIDC Federation Policy

Before creating the policy, gather from the recipient (or from your own internal IdP) the following details: issuer URL, subject claim, subject value, and audiences.

1. On the recipient edit page, under **OIDC federation policies**, click **Add policy**.
2. Fill in the fields:
   - **Policy name** – Human-readable name.
   - **Issuer URL** – The HTTPS URL of the IdP issuing the JWT (e.g., `https://login.microsoftonline.com/<tenant-id>/v2.0`).
   - **Subject claim** – The JWT claim identifying the authenticating identity. For Microsoft Entra ID:
     - `oid` (Object ID) – for a single user in U2M.
     - `groups` – for a group in U2M.
     - `azp` – for an OAuth application in M2M.
   - **Subject** – The specific user, group, or application allowed to access the share.
   - **Audiences** – One or more resource identifiers the JWT must match. A token is valid if its `aud` claim matches any listed audience.
3. Click **Save**. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

#### Example: U2M with Entra ID (single user)

| Field | Value |
|-------|-------|
| Issuer | `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0` |
| Subject claim | `oid` |
| Subject | `11111111-2222-3333-4444-555555555555` (user Object ID) |
| Audiences | `64978f70-f6a6-4204-a29e-87d74bfea138` (Databricks multi-tenant app client ID) |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

#### Example: U2M with Entra ID (group)

| Field | Value |
|-------|-------|
| Issuer | `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0` |
| Subject claim | `groups` |
| Subject | `66666666-2222-3333-4444-555555555555` (group Object ID) |
| Audiences | `64978f70-f6a6-4204-a29e-87d74bfea138` (Databricks multi-tenant app client ID) |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

#### Example: M2M with Entra ID

| Field | Value |
|-------|-------|
| Issuer | `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0` |
| Subject claim | `azp` |
| Subject | `11111111-2222-3333-4444-555555555555` (Application client ID) |
| Audiences | `66666666-2222-3333-4444-555555555555` (any valid audience defined by the recipient) |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 3: Grant Access to Shares

After creating the recipient and [creating shares](/concepts/opensharing-share.md), grant access using Catalog Explorer, the Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. Required permissions: [Metastore](/concepts/metastore.md) admin, or delegated permissions (`USE SHARE` + `SET SHARE PERMISSION` or share owner, and `USE RECIPIENT` or recipient owner). ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

If the recipient reads data via the Iceberg REST catalog, share the **Iceberg OIDC profile generation portal** link. Copy it from the recipient’s **Default OIDC policy** details in the OpenSharing UI. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Recipient Workflow

For the steps recipients follow to authenticate and access shares using OIDC token federation, see:

- [Read data shared using OIDC federation in a U2M flow](/concepts/opensharing-using-oidc-federation.md)
- Read data shared using OIDC federation in an M2M flow

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – The open data-sharing protocol
- [OpenSharing](/concepts/opensharing.md) – Sharing model for non-Databricks recipients
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) – Alternative authentication method for OpenSharing
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) – The policy object defining JWT validation rules
- [Unity Catalog](/concepts/unity-catalog.md) – Governance layer for Data + AI assets
- [Recipient Properties](/concepts/recipient-properties.md) – Custom metadata for recipients

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
