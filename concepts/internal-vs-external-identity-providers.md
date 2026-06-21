---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a3477a9d8d46dc24cf9a7d0f99461c5ec07e78661bdc6fabb5ae982ac57b962
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - internal-vs-external-identity-providers
    - IVEIP
    - Identity Provider
    - Identity Provider (IdP)
    - identity providers
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Internal vs External Identity Providers
description: "Two sharing scenarios: provider-managed (internal IdP for sharing within the same organization) and recipient-managed (external IdP where the recipient controls access policies and MFA)."
tags:
  - identity-management
  - multi-tenant
  - governance
timestamp: "2026-06-19T10:21:31.838Z"
---

# Internal vs External Identity Providers

In the context of Databricks OpenSharing using OIDC (Open ID Connect) federation, an **identity provider (IdP)** can be either internal (provider-managed) or external (recipient-managed). The choice determines who controls user authentication and access policies for shared data.

## Overview

When a data provider creates an OIDC‑federated recipient in OpenSharing, they configure a token federation policy that specifies an issuer URL — the IdP that will issue JSON Web Tokens (JWTs) to authenticate data consumers. That IdP can belong either to the provider’s own organization or to the recipient’s organization. This separation of control is the core of the internal‑vs‑external distinction. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Internal Identity Provider (Provider‑Managed)

An **internal** identity provider is an IdP that the data provider already manages and controls. The provider configures the OIDC policy to trust their own IdP, and then uses that same IdP to authenticate recipients within their own organization or across departments. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Use case:** Sharing data internally within a large organization where different departments do not have direct Databricks access but share the same corporate IdP (e.g., Microsoft Entra ID, Okta). The provider retains full control over authentication, and security policies such as MFA and role‑based access control (RBAC) are enforced by the provider’s IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## External Identity Provider (Recipient‑Managed)

An **external** identity provider is an IdP that the recipient organization controls. The data provider sets up the sharing policy to trust the recipient’s IdP. The recipient then manages who can access the share within their own organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

**Use case:** Cross‑organizational data sharing. The recipient organization retains full control over identity claims, MFA, and RBAC. The provider does not issue or manage any tokens — authentication is entirely delegated to the recipient’s IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Key Differences

| Aspect | Internal IdP | External IdP |
|--------|--------------|--------------|
| Who controls the IdP? | Data provider | Recipient organization |
| Who enforces MFA/RBAC? | Provider’s IdP | Recipient’s IdP |
| Primary use case | Internal sharing across departments | Cross‑organizational sharing |
| Token issuance | Provider’s IdP | Recipient’s IdP |
| Recipient setup complexity | Lower (same IdP) | Higher (coordination with external IdP) |

When using an external IdP, the provider must request information from the recipient about their IdP configuration — issuer URL, subject claim, subject value, and audiences — and enter those details in Databricks. For an internal IdP, the provider already has that information from their own identity system. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Flows

Both internal and external IdP configurations support two OIDC authentication flows:

- **User‑to‑Machine (U2M):** A human user authenticates via the IdP using the OAuth Authorization Code Grant. Tools such as Power BI or Tableau use this flow. The provider can restrict access to specific users or groups within the recipient organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **Machine‑to‑Machine (M2M):** An automated workload (e.g., nightly job, background service) authenticates using a service principal registered in the IdP, using the OAuth Client Credentials Grant. No user interaction is required. This flow is used by clients such as the Python OpenSharing Client or Spark OpenSharing Client. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Policy Configuration Examples

The source material provides concrete examples for Microsoft Entra ID as the IdP. These examples apply to both internal and external configurations, depending on which tenant the issuer URL points to.

### U2M Example (External Recipient with a Specific User)

- Issuer: `https://login.microsoftonline.com/{tenant-id}/v2.0`
- Subject claim: `oid` (Object ID of the user)
- Subject: `11111111-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138` (multi‑tenant app ID registered by Databricks)

### M2M Example (External Recipient with an OAuth Application)

- Issuer: `https://login.microsoftonline.com/{tenant-id}/v2.0`
- Subject claim: `azp` (Authorized party — the client ID of the OAuth application)
- Subject: `11111111-2222-3333-4444-555555555555` (Application client ID)
- Audiences: `66666666-2222-3333-4444-555555555555` (any valid audience defined by the recipient)

## Related Concepts

- [OpenID Connect (OIDC) Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) – How OIDC federation works in Databricks OpenSharing.
- [OpenSharing Recipients](/concepts/opensharing-recipient.md) – Managing recipient objects and policies.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) where shares are registered and permissions are enforced.
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md) – Alternative authentication method using long‑lived tokens.

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
