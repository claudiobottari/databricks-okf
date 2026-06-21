---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ea2a6e12820cf2ebf70003a31601163d49b298207ebc4713a8dcaa847917480d
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - short-lived-jwt-tokens-for-delta-sharing
    - SJTFDS
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Short-lived JWT Tokens for Delta Sharing
description: JWT tokens issued by the recipient's IdP with lifetimes enforced by that IdP, validated by Databricks against the federation policy, eliminating the need for recipients to manage long-lived shared credentials.
tags:
  - security
  - token-management
  - authentication
timestamp: "2026-06-19T10:21:42.695Z"
---

# Short-lived JWT Tokens for Delta Sharing

**Short-lived JWT Tokens for Delta Sharing** are JSON Web Tokens used as temporary credentials in [OpenSharing](/concepts/opensharing.md) authentication flows. In the [Open ID Connect (OIDC) federation](/concepts/opensharing-with-oidc-federation.md) model, these tokens are issued by the recipient’s own identity provider (IdP) and have a lifetime enforced only by that IdP — Databricks neither generates nor manages them. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

Short-lived JWT tokens replace long-lived [bearer tokens](/concepts/oidc-vs-bearer-token-authentication.md) as an authentication method for non-Databricks recipients accessing OpenSharing data shares. Because the token lifetime is controlled by the recipient’s IdP, data sharing gains stronger security properties: fine-grained access control, mandatory Multi-Factor Authentication (MFA), and elimination of shared secrets between provider and recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Databricks acts only as a validation endpoint: it federates authentication to the recipient’s IdP and checks that the presented JWT matches the claims defined in the recipient’s OIDC federation policy (issuer, audience, subject). If validation succeeds, access is granted based on Unity Catalog permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How the Short-Lived JWT Flow Works

1. **Provider creates a recipient with OIDC policy** – The data provider configures a federation policy specifying the IdP’s issuer URL, the expected subject claim (e.g., `oid` for a user, `azp` for an application), the subject value, and one or more audience identifiers. Databricks generates an OIDC profile URL based on this policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

2. **Recipient obtains profile** – The provider shares the OIDC profile URL (or a downloadable profile file) with the recipient. The profile file contains no sensitive credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

3. **Recipient authenticates via IdP** – When the recipient attempts to access shared data, the authentication request is redirected to the recipient’s IdP. The IdP issues a short-lived JWT containing the identity claims. For [User-to-Machine (U2M)](/concepts/user-to-machine-u2m-authentication.md) flows, the user authenticates interactively (e.g., through Power BI); for Machine-to-Machine (M2M) flows, a service principal obtains the token via the client credentials grant. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

4. **Databricks validates the JWT** – The OpenSharing service checks that the JWT’s claims match the policy (issuer, audience, subject). A successful validation allows access based on the privileges granted on the share. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Key Characteristics

- **Lifetime controlled by IdP** – The token’s expiry is determined by the recipient’s identity provider, not by Databricks. This allows the recipient organization to enforce its own security policies, including token refresh intervals. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **No shared secrets** – Unlike long-lived bearer tokens, short-lived JWTs require no credential exchange between provider and recipient. All credential management stays inside each organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **MFA support** – The recipient’s IdP can enforce MFA at login time, adding an extra layer of security before the JWT is issued. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Fine-grained identity** – The provider can restrict access to specific users, groups, or OAuth applications by configuring the subject and subject claim in the federation policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison with Long-Lived Bearer Tokens

| Feature | Short-Lived JWT (OIDC) | Long-Lived Bearer Token |
|---------|------------------------|-------------------------|
| Credential management | Recipient managed via IdP | Provider generates and shares |
| Lifetime | Short, enforced by IdP | Long, set by provider |
| MFA support | Yes (via IdP) | No |
| Secret sharing | None | Must exchange secret |
| Rotation | Automatic via IdP | Manual |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) – The configuration that defines which IdP and which identities are trusted.
- [Bearer Tokens for Delta Sharing](/concepts/bearer-token-authentication-for-delta-sharing.md) – The alternative, long-lived authentication method.
- [OpenSharing](/concepts/opensharing.md) – The cross-platform sharing protocol that supports OIDC federation.
- [Identity Provider](/concepts/internal-vs-external-identity-providers.md) – The external system (e.g., Microsoft Entra ID, Okta) that issues the JWT.
- [Unity Catalog](/concepts/unity-catalog.md) – The permission system underlying access control for shares.

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
