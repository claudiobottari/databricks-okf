---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2cdcc4bbc3c96ddcd90d5f162ad5968cc94d844c453b0aba4e9050a9d87eb514
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - internal-vs-external-identity-provider-models
    - IVEIPM
    - internal-vs-external-identity-provider-patterns
    - IVEIPP
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Internal vs External Identity Provider Models
description: "Two deployment modes for OIDC federation: provider-managed (internal IdP used when sharing within the same organization) and recipient-managed (external IdP where the recipient controls access policies and user identities)."
tags:
  - identity-provider
  - delta-sharing
  - architecture
timestamp: "2026-06-18T15:36:54.682Z"
---

# Internal vs External Identity Provider Models

**Internal vs External Identity Provider Models** refers to two approaches for managing identity federation when sharing data using Open ID Connect (OIDC) Federation in Databricks OpenSharing. The choice determines which organization controls authentication, token issuance, and security policy enforcement for accessing shared data.

## Overview

When configuring an OIDC federation policy for an [OpenSharing](/concepts/opensharing.md) recipient, the data provider can choose to federate authentication to either an internal identity provider (IdP) managed by the provider's organization or an external IdP managed by the recipient's organization. This decision affects who bears responsibility for managing user access, enforcing security policies, and controlling token lifetimes. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Internal Identity Provider (Provider-Managed)

In the internal IdP model, the data provider configures the sharing policy to use their own organization's identity provider. This approach is useful for sharing data within large organizations where different departments do not have direct Databricks access but share the same IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Key characteristics:
- **Provider manages access on behalf of the recipient.** The provider defines which users, groups, or service principals can access shared data.
- **Security policies are enforced by the provider's IdP.** Policies such as Multi-Factor Authentication (MFA) and role-based access control are governed by the provider's identity infrastructure.
- **Suitable for internal sharing scenarios.** When different teams or departments within the same organization need access to shared data but do not have Databricks workspace access, the provider can grant access using their existing IdP.

## External Identity Provider (Recipient-Managed)

In the external IdP model, the data provider configures the sharing policy to trust the recipient's identity provider. This approach is designed for cross-organizational data sharing where the recipient organization retains full control over who can access the shared data. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Key characteristics:
- **Recipient organization retains full control.** The recipient manages user identities, group membership, and application registrations within their own IdP.
- **Security policies are enforced by the recipient's IdP.** The recipient's identity infrastructure governs MFA, role-based access, and token lifetime.
- **Suitable for external sharing scenarios.** When sharing data with external partners, customers, or other organizations, the provider trusts the recipient's IdP to authenticate and authorize end users.

## Comparison

| Aspect | Internal (Provider-Managed) | External (Recipient-Managed) |
|--------|----------------------------|------------------------------|
| Who controls the IdP | Provider's organization | Recipient's organization |
| Who enforces MFA | Provider's IdP | Recipient's IdP |
| Who manages user access | Provider | Recipient |
| Typical use case | Intra-organizational sharing | Cross-organizational sharing |
| Token issuance by | Provider's IdP | Recipient's IdP |
| Security policy governance | Provider | Recipient |

## Token Lifetime and Security

In both models, JSON Web Tokens (JWTs) are short-lived tokens issued by the relevant IdP. Databricks does not generate or manage these tokens — it only federates authentication to the configured IdP and validates the JWT against the recipient's federation policy. The lifetime of the JWT is governed by the issuing IdP, not by Databricks. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Both models eliminate the need for long-lived bearer tokens, reducing security risks by removing the requirement for recipients to manage and secure shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Flows

Both internal and external IdP models support two authentication flows:

- **User-to-Machine (U2M) Authentication:** Users authenticate through their IdP using the OAuth Authorization Code Grant flow. This flow is used by applications like Power BI and Tableau where end users interact directly with the shared data. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Machine-to-Machine (M2M) Authentication:** Service principals authenticate using the [OAuth Client Credentials Grant flow](/concepts/oauth-client-credentials-grant-m2m-flow.md). This flow is used for automated workloads, nightly jobs, or background services that require access without user interaction. No secrets or credentials are exchanged between Databricks, the provider, or the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Choosing Between Internal and External IdP

The decision depends on the sharing scenario:
- **Internal sharing** (same organization, different departments): Use the internal IdP model where the provider manages access through their own identity system.
- **External sharing** (different organizations): Use the external IdP model where the recipient organization controls access through their own identity system.

If using an external IdP, the provider must request information from the recipient about their IdP, including the issuer URL, subject claim, subject identifier, and audience values. This information is transmitted over a secure channel and used to configure the OIDC federation policy in Databricks. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

If using an internal IdP, the provider retrieves this information from their own identity system based on the identities they are sharing with. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Recipients](/concepts/opensharing-recipient.md) – Objects that govern access to shared data
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) – The policy configuration that specifies the IdP and identity claims
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying protocol for data sharing
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-open-sharing.md) – Alternative authentication method using long-lived tokens
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer for managing data sharing permissions

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
