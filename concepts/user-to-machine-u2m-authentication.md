---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 14b7853c4217e71e5c0cb81e89bf745da0ae4f1f2404e3417b80b6a6b9e48a6d
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-to-machine-u2m-authentication
    - U(A
    - OAuth user-to-machine (U2M) authentication
    - OAuth user-to-machine authentication
    - User-to-Machine Authentication
    - OAuth U2M Authentication
    - OAuth U2M authentication
    - OAuth User-to-Machine (U2M)
    - OAuth authentication
    - User-to-Machine (U2M)
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: User-to-Machine (U2M) Authentication
description: Authentication flow where a human user authenticates via their IdP (with MFA if configured) and accesses shared data through tools like Power BI or Tableau using the OAuth Authorization Code Grant flow.
tags:
  - authentication
  - delta-sharing
  - user-experience
timestamp: "2026-06-19T10:21:14.942Z"
---

# User-to-Machine (U2M) Authentication

**User-to-Machine (U2M) Authentication** refers to an authentication flow in which a human user authenticates through their organization's identity provider (IdP) to access shared data programmatically or through client applications. In the context of OpenSharing (Delta Sharing) and OIDC federation, U2M authentication enables data recipients to access shared datasets using tools like Power BI or Tableau without managing long-lived credentials.

## Overview

In a U2M authentication flow, a user from the recipient organization authenticates using their identity provider. If multi-factor authentication (MFA) is configured, it is enforced during login. Once authenticated, the user can access shared data using client applications such as Power BI or Tableau. The data provider can define access policies that restrict data access to specific users or groups within the recipient organization, ensuring precise control over who can access shared resources. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

U2M authentication uses the **OAuth Authorization Code Grant** flow. The client application (e.g., Power BI) obtains access tokens from the IdP on behalf of the authenticated user. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How U2M Authentication Works in OpenSharing

1. The data provider creates a [recipient object](/concepts/opensharing-recipient-object.md) in OpenSharing and configures an [OIDC Federation Policy](/concepts/oidc-federation-policy.md) that specifies the issuer URL of the recipient's IdP (such as Microsoft Entra ID or Okta) and defines the user or group that should have access to the share.

2. Databricks generates an OIDC profile web portal URL based on the policy. The provider shares this URL with the recipient. For U2M authentication, the recipient inputs the recipient endpoint from the OIDC profile web portal into their U2M application (e.g., Power BI or Tableau).

3. When the recipient user attempts to access shared data, authentication is federated to their IdP. The IdP generates a JSON Web Token (JWT) containing identity claims. Databricks validates the JWT against the recipient's policy to ensure it matches expected claims including issuer, audience, and subject. If validation is successful, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Key Characteristics

- **Short-lived tokens**: Token lifetime is governed entirely by the recipient's IdP, not by Databricks. Databricks does not generate or manage any tokens or credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Security policy enforcement**: The recipient's IdP enforces security policies including MFA and role-based access control during authentication. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **No shared credentials**: U2M authentication eliminates the need for recipients to manage and secure long-lived bearer tokens or shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Fine-grained access control**: Providers can define policies that restrict data access to specific users or groups within the recipient organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison with M2M Authentication

| Aspect | U2M Authentication | M2M Authentication |
|--------|-------------------|-------------------|
| Authenticating entity | Human user via IdP | Service principal or OAuth application |
| OAuth flow | Authorization Code Grant | Client Credentials Grant |
| Typical clients | Power BI, Tableau | Python OpenSharing Client, Spark OpenSharing Client |
| IdP claim type | `oid` (user Object ID) or `groups` | `azp` (application ID) |
| Use case | Interactive user access | Automated workloads, background services |

U2M is designed for interactive scenarios where a human user needs to access shared data through tools, while [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md) is for automated workloads that require access without user interaction. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Configure for U2M: Example with Microsoft Entra ID

When sharing with a specific user in an Entra ID tenant, the OIDC federation policy should use:

- **Issuer**: `https://login.microsoftonline.com/<tenant-id>/v2.0`
- **Subject claim**: `oid` (Object ID)
- **Subject**: The user's Object ID (e.g., `11111111-2222-3333-4444-555555555555`)
- **Audiences**: `64978f70-f6a6-4204-a29e-87d74bfea138` (The multi-tenant app ID registered by Databricks in Entra ID)

When sharing with a group, use `groups` as the subject claim and the group's Object ID as the subject. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

> **Note**: For U2M applications like Power BI and Tableau, the audience must be the multi-tenant app ID registered by Databricks in Entra ID: `64978f70-f6a6-4204-a29e-87d74bfea138`. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md) — Automated authentication for programmatic access
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) — The policy configuration governing token validation
- [OpenSharing Recipients](/concepts/opensharing-recipient.md) — Recipient objects in Delta Sharing
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying data sharing protocol
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md) — The entity responsible for user authentication and token issuance

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
