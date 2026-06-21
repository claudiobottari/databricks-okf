---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 970a02d67f59cdf98578deb73054fa1edc8c742217bd7459f2a8fe3291118d74
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-vs-bearer-token-authentication
    - OVBTA
    - Bearer Token Authentication
    - Bearer token authentication
    - Bearer Token
    - OAuth token authentication
    - bearer tokens
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: OIDC vs Bearer Token Authentication
description: Comparison between OIDC federation and long-lived Databricks-issued bearer tokens for OpenSharing, highlighting trade-offs in security, MFA support, and credential management.
tags:
  - authentication
  - comparison
  - delta-sharing
  - security
timestamp: "2026-06-18T12:11:33.345Z"
---

# OIDC vs Bearer Token Authentication

**OIDC (OpenID Connect) Federation** and **Bearer Token Authentication** are two authentication methods used in Databricks OpenSharing to govern access to shared data for non-Databricks recipients who do not have access to a Unity Catalog-enabled Databricks workspace. OIDC Federation uses short-lived JSON Web Tokens (JWTs) issued by the recipient's identity provider (IdP), while bearer token authentication uses long-lived Databricks-issued tokens. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison Overview

| Aspect | OIDC Federation | Bearer Token Authentication |
|--------|-----------------|-----------------------------|
| Token Issuer | Recipient's or provider's IdP | Databricks |
| Token Lifetime | Short-lived; governed by the receiving IdP | Long-lived |
| Multi-Factor Authentication (MFA) | Supported and enforced by the IdP | Not supported |
| Security Model | Federated identity; no shared credentials | Shared credential (bearer token) |
| Credential Management | Managed entirely within each organization | Recipient must manage and secure a Databricks-issued token |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## OIDC Federation

### How It Works

In OIDC Federation, authentication is delegated to the recipient's identity provider (IdP), such as Microsoft Entra ID or Okta. The recipient's IdP is responsible for issuing JWT tokens and enforcing security policies such as MFA. The lifetime of the JWT token is governed by the recipient's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

The flow proceeds as follows:

1. The data provider creates an OIDC federation recipient in OpenSharing, configuring a policy that specifies the IdP issuer URL and defines which user, group, service principal, or OAuth application has access.
2. Databricks generates an OIDC profile portal URL based on the policy, which the provider shares with the recipient.
3. When the recipient attempts to access shared data, authentication is federated to the recipient's IdP.
4. The recipient's IdP generates a JWT containing identity claims.
5. The OpenSharing service validates the JWT against the recipient's configured policy.
6. If validation succeeds, access is granted based on Unity Catalog permissions.

Databricks does not generate or manage any tokens or credentials in this flow. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Authentication Scenarios

OIDC Federation supports two authentication scenarios: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**User-to-Machine (U2M) Authentication**: A user authenticates using their IdP, with MFA enforced if configured. Uses the OAuth Authorization Code Grant flow. Suitable for tools like Power BI or Tableau.

**Machine-to-Machine (M2M) Authentication**: The recipient organization registers a Service Principal in its IdP. Uses the [OAuth Client Credentials Grant flow](/concepts/oauth-client-credentials-grant-m2m-flow.md). Suitable for automated workloads such as nightly jobs or background services.

### Identity Provider Options

OIDC Federation can use either an internal or external IdP: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **Internal Identity Provider (Provider-Managed)**: Used for sharing within large organizations where departments share the same IdP. The provider manages access on behalf of the recipient.
- **External Identity Provider (Recipient-Managed)**: The provider trusts the recipient's IdP. The recipient retains full control over who can access shared data.

## Bearer Token Authentication

Bearer token authentication is the alternative method for connecting non-Databricks recipients to shares. In this model, Databricks issues a long-lived bearer token to the recipient. The recipient must manage and secure this shared credential to access shared data. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Bearer tokens do not support MFA, do not provide fine-grained access control, and require the recipient to manage a shared secret that could be compromised. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Key Differences

### Security

**OIDC Federation** provides enhanced security through federation. No secrets or credentials are exchanged between Databricks, the provider, or the recipient — all secret management remains internal to each organization. MFA and other security policies are enforced by the recipient's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Bearer Token Authentication** relies on shared credentials (long-lived bearer tokens) that must be managed and secured by the recipient. This introduces risk if the token is compromised. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Token Lifetime

**OIDC Federation** uses short-lived JWT tokens whose lifetime is governed by the recipient's IdP. This reduces the window of exposure if a token is leaked. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Bearer Token Authentication** uses long-lived tokens that remain valid until explicitly revoked, increasing the risk of unauthorized access if a token is compromised. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Access Control

**OIDC Federation** enables fine-grained access control. The data provider can define access policies that restrict data access to specific users, groups, or service principals within the recipient organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Bearer Token Authentication** does not provide the same level of granularity — a single bearer token grants access to all shares it is authorized for, without distinguishing between different identities within the recipient organization.

### Credential Management

**OIDC Federation** eliminates the need for recipients to manage shared credentials. All secret management is handled within each organization's existing identity infrastructure. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Bearer Token Authentication** requires recipients to manage and secure Databricks-issued tokens, adding operational overhead and security risk. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## When to Use Each

### When to Use OIDC Federation

- You need MFA support for accessing shared data.
- You want fine-grained access control over who can access shares.
- You want to reduce security risks from shared credentials.
- Recipients use their own IdP (e.g., Microsoft Entra ID, Okta).
- Either U2M (user-driven) or M2M (automated) scenarios apply.
- You are sharing data with organizations that do not have Databricks workspaces.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### When to Use Bearer Token Authentication

- Recipients cannot or will not use OIDC Federation.
- Simpler, non-federated authentication is acceptable.
- The security requirements do not mandate MFA or short-lived tokens.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The data sharing protocol underlying OpenSharing
- [OpenSharing Recipients](/concepts/opensharing-recipient.md) — Recipient objects that define access to shares
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) — The policy configuration for OIDC-based authentication
- [Bearer Token](/concepts/oidc-vs-bearer-token-authentication.md) — Long-lived tokens issued by Databricks for authentication
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer enforcing access permissions
- [Identity Provider](/concepts/internal-vs-external-identity-providers.md) — The external system that issues identity tokens

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
