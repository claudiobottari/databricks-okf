---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 713fde5a9f6330badb69bf1d2684a37d9d533fa35eb4e1ba34d33f538fc0e17e
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - internal-vs-external-identity-provider-patterns
    - IVEIPP
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Internal vs External Identity Provider Patterns
description: "Two deployment patterns for OIDC federation: provider-managed IdP for intra-organization sharing and recipient-managed IdP for cross-organization sharing, each with different security and control characteristics."
tags:
  - architecture
  - identity-provider
  - delta-sharing
  - patterns
timestamp: "2026-06-18T12:11:04.852Z"
---

# Internal vs External Identity Provider Patterns

**Internal vs External Identity Provider Patterns** describe two deployment models for OIDC Federation in [OpenSharing](/concepts/opensharing.md) when a data provider shares data with recipients who do not have access to a [Unity Catalog](/concepts/unity-catalog.md)-enabled Databricks workspace. Both patterns use JSON Web Token (JWT) federation, where the recipient's or provider’s identity provider (IdP) issues short-lived tokens that Databricks validates against a configured federation policy. The choice between internal and external IdP determines who controls authentication policies (such as Multi-Factor Authentication (MFA)) and who manages the recipient identities. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Internal Identity Provider (Provider-Managed)

In the **internal** pattern, the data provider uses their own IdP to govern access to the share. This is typically used for sharing data within a large organization where different departments do not have direct Databricks access but share the same corporate IdP. The provider manages all access decisions on behalf of the recipient—setting policies, defining who can access the data, and enforcing security controls such as MFA and role-based access control. The recipient does not need to configure their own federation; the provider's IdP authenticates the recipient's users. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## External Identity Provider (Recipient-Managed)

In the **external** pattern, the data provider configures the sharing policy to trust the recipient’s own IdP. The recipient organization retains full control over which users, groups, or applications can access the shared data. Security policies such as MFA and role-based access control are enforced by the recipient’s IdP. The provider does not manage recipient identities or tokens; Databricks only validates JWTs issued by the recipient's IdP against the federation policy. This pattern is suitable for sharing data across organizational boundaries where the recipient wants to maintain its own authentication governance. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison

| Aspect | Internal IdP (Provider-Managed) | External IdP (Recipient-Managed) |
|--------|----------------------------------|-----------------------------------|
| Who controls access | Data provider | Recipient organization |
| Who enforces MFA and RBAC | Provider's IdP | Recipient's IdP |
| Typical use case | Intra-organization sharing between departments without Databricks access | Cross-organization sharing where recipient wants to manage identities |
| Recipient setup | Minimal – only needs to authenticate against provider's IdP | Requires configuring their own IdP and providing federation details to provider |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Relationship to Authentication Flows

Both internal and external IdP patterns support [User-to-Machine (U2M)](/concepts/user-to-machine-u2m-authentication.md) and Machine-to-Machine (M2M) authentication flows.

### U2M (User-to-Machine)

In a U2M flow, a human user from the recipient organization authenticates through the IdP. If MFA is configured, it is enforced at login. After authentication, the user can access shared data using tools like Power BI or Tableau. The Manual OAuth token fetch with authorization_details|OAuth Authorization Code Grant flow is used by the client application to obtain access tokens from the IdP. This applies equally whether the IdP is internal or external. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### M2M (Machine-to-Machine)

In an M2M flow, automated workloads (nightly jobs, background services) authenticate without user interaction. The recipient organization registers a Service Principal in its IdP. The [OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) flow is used to retrieve access tokens. No secrets or credentials are exchanged between Databricks, the provider, or the recipient; all secret management remains internal to each organization. This flow works identically for internal and external IdPs. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Creating a Recipient with OIDC Federation

When a data provider creates a recipient in Databricks, they choose the authentication method as OIDC Federation. Regardless of whether the IdP is internal or external, the provider must gather the following information from the IdP (their own for internal, or from the recipient for external):

- **Issuer URL**: The HTTPS URL of the IdP that issues the JWT.
- **Subject claim**: The claim identifying the authenticating identity type (e.g., `oid` for a user, `groups` for a group, `azp` for an OAuth application).
- **Subject**: The specific user, group, or application allowed to access the share.
- **Audiences**: One or more resource identifiers the JWT must match.

If using an external IdP, this information must be transmitted securely from the recipient to the provider. If using an internal IdP, the provider retrieves it from their own identity system. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Security Considerations

- **Token lifetime**: The lifetime of the JWT is governed solely by the issuing IdP, whether internal or external. Databricks does not generate or manage tokens; it only validates them. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **No shared secrets**: OIDC federation eliminates the need to share long-lived bearer tokens. All secret management remains within the provider's or recipient's organization depending on the pattern chosen. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Policy enforcement**: In the internal pattern, the provider enforces policies; in the external pattern, the recipient does. The choice affects who can modify access rules and audit logs. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Choosing a Pattern

Select an internal IdP pattern when:
- Sharing data within the same organization (departments, business units).
- The provider already manages a centralized IdP.
- The provider wants to control all access policies without involving the recipient in identity management.

Select an external IdP pattern when:
- Sharing data across different organizations.
- The recipient requires full control over who can access the data.
- The recipient's compliance or security policies demand that their own IdP enforce MFA and RBAC.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md)
- [Bearer Token Authentication for OpenSharing](/concepts/bearer-token-authentication-for-opensharing.md)
- [Delta Sharing (Databricks-to-Open)](/concepts/open-sharing-databricks-to-open.md)
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)
- Manual OAuth token fetch with authorization_details|OAuth Authorization Code Grant
- [OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md)

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
