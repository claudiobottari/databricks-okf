---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4b6d9b578f82c1bccfc6cea2c143ffca3f90330d0509a1a62cc517398c525206
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
    - what-is-the-opensharing-databricks-to-open-sharing-protocol-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - oidc-federation-for-opensharing
    - OFFO
    - OIDC Federation for OpenSharing Recipients
    - OIDC federation for OpenSharing recipients
    - Enable OIDC federation for OpenSharing recipients
    - Enable Open ID Connect (OIDC) federation for OpenSharing recipients
    - Enable OpenID Connect (OIDC) federation for OpenSharing recipients
    - Open ID Connect (OIDC) Federation for OpenSharing
    - OpenID Connect (OIDC) Federation for OpenSharing
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
    - file: access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
title: OIDC Federation for OpenSharing
description: Authentication method that allows data providers to federate identity verification to a recipient's IdP using OIDC, enabling short-lived JWT tokens instead of long-lived bearer tokens for OpenSharing.
tags:
  - delta-sharing
  - authentication
  - security
timestamp: "2026-06-19T18:40:14.971Z"
---

```yaml
---
title: OIDC Federation for OpenSharing
summary: An authentication method using OpenID Connect federation for Databricks-to-Open sharing, supporting both user-to-machine (U2M) and machine-to-machine (M2M) flows.
sources:
  - access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md
  - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:10:46.303Z"
updatedAt: "2026-06-19T08:50:15.291Z"
tags:
  - authentication
  - oidc
  - federation
aliases:
  - oidc-federation-for-opensharing
  - OFFO
confidence: 0.98
provenanceState: merged
inferredParagraphs: 1
---

# OIDC Federation for OpenSharing

**OIDC Federation** is an authentication method for the [OpenSharing Databricks-to-Open sharing protocol](/concepts/opensharing-databricks-to-open-protocol.md) that lets data providers delegate authentication to a recipient’s identity provider (IdP) using OpenID Connect (OIDC). Instead of issuing long-lived bearer tokens, Databricks validates short-lived JSON Web Tokens (JWTs) issued by the recipient’s IdP. This enables fine-grained access control, support for Multi-Factor Authentication (MFA), and eliminates the need to manage shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How it works

In OIDC Federation, the data provider configures a federation policy on the recipient object. The policy specifies the IdP’s issuer URL and the identities (users, groups, service principals, or OAuth applications) allowed to access the share. When the recipient attempts to read shared data, authentication is federated to their IdP; the IdP issues a JWT, and Databricks validates the JWT against the policy. Databricks never generates or manages tokens — the token lifetime and security policies (e.g., MFA) are governed entirely by the recipient’s IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

OIDC Federation is an alternative to the bearer‑token authentication model for non-Databricks recipients. It reduces risk by removing the need to share long‑lived secrets. Data providers can also use OIDC Federation with their own internal IdP when sharing data within the same organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

The authentication flow follows these steps: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

1. The provider creates a recipient with an OIDC federation policy that includes the IdP’s issuer URL, the expected JWT claims (subject, audience), and the subject value (e.g., a user’s object ID or a group ID).
2. Databricks generates an OIDC profile portal URL (and an Iceberg‑specific portal link if needed). The provider shares this URL with the recipient over a secure channel. The profile file downloaded from the portal does not contain sensitive information.
3. The recipient authenticates through their IdP when accessing the shared data. The IdP issues a JWT containing the configured claims.
4. Databricks validates the JWT against the policy (issuer, audience, subject). If valid, access is granted based on Unity Catalog permissions on the share.

## Authentication scenarios

OIDC Federation supports two authentication flows: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### User-to-Machine (U2M)

A human user authenticates via their IdP (e.g., Microsoft Entra ID) using the OAuth Authorization Code Grant flow. MFA is enforced by the IdP. The user can then access shared data through tools like Power BI or Tableau. The subject claim is typically `oid` (user object ID) or `groups` (group object ID). For Entra ID, the audience must be the multi‑tenant app ID registered by Databricks: `64978f70-f6a6-4204-a29e-87d74bfea138`. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Machine-to-Machine (M2M)

Intended for automated workloads (e.g., scheduled jobs, background services). The recipient registers a service principal in their IdP. The application uses the OAuth Client Credentials Grant flow to obtain a JWT. The subject claim is `azp` (authorized party – the client ID of the OAuth application). The audience can be any identifier defined by the recipient, such as the same client ID. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Creating a recipient with an OIDC federation policy

Providers use Catalog Explorer or SQL commands to create the recipient and define the OIDC policy. The following sections describe the steps and configuration details. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 1: Create the recipient object

Navigate to **Catalog > OpenSharing > Recipients > New recipient**. Set the recipient type to **Open** and authentication method to **OIDC Federation**. Provide a recipient name and optionally add custom recipient properties. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 2: Add an OIDC federation policy

On the recipient edit page, click **Add policy** and enter: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **Policy name**: A human‑readable name.
- **Issuer URL**: The HTTPS URL of the recipient’s IdP (e.g., `https://login.microsoftonline.com/<tenant-id>/v2.0` for Entra ID).
- **Subject claim**: The JWT claim that identifies the identity type. For Entra ID: `oid` (user), `groups` (group), or `azp` (application).
- **Subject**: The specific value of the subject claim (e.g., the user’s object ID, group object ID, or application client ID).
- **Audiences**: One or more resource identifiers the JWT must match. At least one must be present.

#### Example: U2M with Entra ID (single user)

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `oid`
- Subject: `11111111-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138`

#### Example: U2M with Entra ID (group)

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `groups`
- Subject: `66666666-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138`

#### Example: M2M with Entra ID

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `azp`
- Subject: `11111111-2222-3333-4444-555555555555` (application client ID)
- Audiences: `66666666-2222-3333-4444-555555555555` (any valid audience)

### Step 3: Grant share access

After the recipient is created, grant it access to the desired shares using Catalog Explorer or the `GRANT ON SHARE` SQL command. Permissions required: [Metastore](/concepts/metastore.md) admin, or `USE SHARE` + `SET SHARE PERMISSION` (or share ownership) and `USE RECIPIENT` (or recipient ownership). ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Step 4: Share the OIDC profile portal link

For recipients using Iceberg REST catalog access, copy the **Iceberg OIDC profile generation portal** link from the recipient details page and share it securely. The link includes the share names. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Recipient workflow

Recipients use the OIDC profile portal URL to authenticate and access shared data. Detailed instructions for both U2M and M2M flows are available: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md, access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md]

- [Read data shared using Open ID Connect (OIDC) federation in a U2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-u2m)
- [Read data shared using Open ID Connect (OIDC) federation in an M2M flow](https://docs.databricks.com/aws/en/delta-sharing/sharing-over-oidc-m2m)

## Related concepts

- [OpenSharing Databricks-to-Open sharing protocol](/concepts/opensharing-databricks-to-open-protocol.md) — The overall sharing model
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md) — The alternative authentication method
- Open ID Connect (OIDC) — The underlying standard
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer managing shares and recipients
- [Recipient objects](/concepts/recipient-object-delta-sharing.md) — The named objects representing external users or groups

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
- access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
2. [access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws.md](/references/access-data-shared-with-you-using-opensharing-for-recipients-databricks-on-aws-7bb360b8.md)
