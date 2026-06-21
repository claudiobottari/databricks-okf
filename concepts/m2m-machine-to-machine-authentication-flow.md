---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 17855aa43a69c79af6178a634a14fbe566e3042d1c344db70c1d18978e0338ff
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - m2m-machine-to-machine-authentication-flow
    - M(AF
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: M2M (Machine-to-Machine) Authentication Flow
description: Authentication flow for automated workloads using service principals registered in the recipient's IdP, using the OAuth Client Credentials Grant flow with no user interaction required.
tags:
  - authentication
  - oauth
  - automation
timestamp: "2026-06-19T18:40:32.469Z"
---

# M2M (Machine-to-Machine) Authentication Flow

**M2M (Machine-to-Machine) Authentication Flow** refers to the authentication method used in OpenSharing where automated workloads, services, or applications authenticate to access shared data without requiring direct user interaction. This flow uses OIDC federation, allowing the recipient's identity provider (IdP) to issue short-lived JSON Web Tokens (JWTs) that are validated by Databricks.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

M2M authentication is designed for automated workloads such as nightly jobs, background services, or programmatic data access. The recipient organization registers a Service Principal in its IdP, which enables applications or scripts to securely access resources programmatically. No secrets or credentials are exchanged between Databricks, the provider, or the recipient — all secret management remains internal to each organization.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How It Works

1. The data provider creates a recipient in OpenSharing and configures an OIDC token federation policy specifying the recipient's IdP issuer URL and the OAuth application that should have access to the share.
2. Databricks generates an OIDC profile web portal URL or downloadable profile file, which the provider shares with the recipient.
3. For M2M authentication, the recipient application developer downloads the profile file and references it in the recipient client app.
4. When the recipient application attempts to access shared data, the authentication is federated to the recipient's IdP.
5. The recipient's IdP generates a JWT containing identity claims using the OAuth Client Credentials Grant flow.
6. The OpenSharing service validates the JWT against the recipient's policy to ensure it matches expected claims (issuer, audience, and subject). If validation succeeds, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## OIDC Federation Policy Configuration for M2M

When configuring an OIDC federation policy for M2M authentication, the following values are required:

- **Issuer URL**: The HTTPS URL of the IdP issuing the JWT token.
- **Subject claim**: For M2M flows in Microsoft Entra ID, use `azp` to identify the OAuth application.
- **Subject**: The Application (client) ID of the registered OAuth application.
- **Audiences**: One or more resource identifiers that the JWT must match.

### Example for M2M with Microsoft Entra ID

For an M2M OAuth application with Application (client) ID `11111111-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `azp`
- **Subject**: `11111111-2222-3333-4444-555555555555` (the Application client ID)
- **Audiences**: `66666666-2222-3333-4444-555555555555` (any valid audience identifier, such as the client ID of the registered OAuth application)

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Comparison with U2M Authentication

| Aspect | M2M Authentication | U2M Authentication |
|---|---|---|
| **Use case** | Automated workloads, background services | Interactive user tools (Power BI, Tableau) |
| **Identity type** | Service Principal or OAuth application | User or group |
| **OAuth flow** | Client Credentials Grant | Authorization Code Grant |
| **Subject claim** | `azp` (in Entra ID) | `oid` or `groups` (in Entra ID) |
| **Token source** | IdP, no user interaction required | IdP, requires user login |

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- OpenID Connect (OIDC) Federation
- [OpenSharing](/concepts/opensharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- Service Principal
- [OAuth 2.0 Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md)

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
