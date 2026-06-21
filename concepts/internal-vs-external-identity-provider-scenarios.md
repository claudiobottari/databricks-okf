---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15158effc274f3c7b18763dceb70370ce6d6ceede0f7e5d485d3a93b07358adc
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - internal-vs-external-identity-provider-scenarios
    - IVEIPS
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Internal vs External Identity Provider Scenarios
description: "Two OIDC sharing models: provider-managed (internal IdP for sharing within large organizations) and recipient-managed (external IdP where recipient controls access)."
tags:
  - identity-provider
  - governance
  - sharing
timestamp: "2026-06-19T18:40:23.135Z"
---

# Internal vs External Identity Provider Scenarios

When configuring [OIDC Federation for OpenSharing Recipients](/concepts/oidc-federation-for-opensharing.md), data providers can choose to federate authentication to either an **internal identity provider (IdP)** (provider-managed) or an **external identity provider (IdP)** (recipient-managed). The choice depends on the sharing scenario, organizational boundaries, and where security policy enforcement should reside. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Internal Identity Provider (Provider-Managed)

In an internal IdP scenario, the data provider configures the OIDC federation policy to use their own identity provider. This approach is useful for sharing data within large organizations where different departments do not have direct Databricks access but share the same IdP. The provider manages access on behalf of the recipient, and security policies — such as Multi-Factor Authentication (MFA) and role-based access control — are enforced by the provider's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## External Identity Provider (Recipient-Managed)

In an external IdP scenario, the data provider sets up the sharing policy to trust the recipient's IdP. The recipient organization retains full control over who can access the shared data, and security policies (MFA, role-based access) are enforced by the recipient's IdP. This model is designed for recipients who do not have access to a Unity Catalog-enabled Databricks workspace and need to authenticate using their own identities. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison Summary

| Aspect | Internal IdP (Provider-Managed) | External IdP (Recipient-Managed) |
|--------|--------------------------------|----------------------------------|
| Who controls IdP | The data provider | The recipient organization |
| Typical use case | Intra-organizational sharing across departments that share a common IdP | Cross-organizational sharing with external partners |
| Security policy enforcement | Provider's IdP enforces MFA, RBAC, etc. | Recipient's IdP enforces MFA, RBAC, etc. |
| Token generation and lifecycle | Provider's IdP | Recipient's IdP |
| Databricks role | Validates JWT against policy; does not generate tokens | Same — validates JWT, does not generate tokens |

In both cases, Databricks does **not** generate or manage JWT tokens; it only federates authentication to the designated IdP and validates the JWT token against the configured federation policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Flows

Both internal and external IdP scenarios support two authentication flows:

- **User-to-Machine (U2M)** – A user authenticates via the IdP (e.g., through Power BI or Tableau). MFA is enforced during login. The provider can define access policies restricting data to specific users or groups within the recipient organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Machine-to-Machine (M2M)** – An automated workload (e.g., nightly job) authenticates using a service principal registered in the IdP. No secrets or credentials are exchanged between Databricks, the provider, or the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Recipient](/concepts/opensharing-recipient.md)
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md)
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md)
- [Unity Catalog Permissions for Sharing](/concepts/unity-catalog-permissions-for-opensharing.md)

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
