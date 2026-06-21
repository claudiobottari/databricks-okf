---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 587cf34dec3425875219d938381ea0e33e2c72b1582b963acb1105e9b86a6de6
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - oidc-federation-policy
    - OFP
    - OIDC federation
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: OIDC Federation Policy
description: A configuration policy specifying issuer URL, subject claim (oid, groups, azp), subject identifier, and audience(s) that the JWT must match for authentication to succeed.
tags:
  - policy
  - configuration
  - security
timestamp: "2026-06-19T18:40:19.618Z"
---

# OIDC Federation Policy

**OIDC Federation Policy** is a configuration object within [OpenSharing](/concepts/opensharing.md) on Databricks that defines the identity provider (IdP) issuer URL, subject claim, subject value, and audiences used to authenticate recipients via OpenID Connect (OIDC). The policy governs which identities from the recipient's IdP are authorized to access shared data, enabling short-lived JSON Web Token (JWT) authentication as an alternative to long-lived bearer tokens. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Purpose

When a data provider creates a recipient in OpenSharing, they configure an OIDC token federation policy that specifies the issuer URL of the recipient IdP (such as Microsoft Entra ID or Okta) and defines the recipient user, group, service principal, or OAuth application that should have access to the share. Databricks does not generate or manage tokens; it only federates authentication to the recipient's IdP and validates the JWT against the recipient's configured federation policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

The policy enforces that the JWT’s claims — including issuer, audience, and subject — match the expected values. If validation succeeds, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Configuration Fields

When creating an OIDC federation policy, the data provider must configure the following fields: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **Policy name**: A human-readable name for the policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Issuer URL**: The HTTPS URL of the IdP issuing the JWT token. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Subject claim**: The claim in the JWT that identifies the authenticating identity type. In Microsoft Entra ID, `oid` (Object ID) is used for U2M user access, `groups` for group access, and `azp` for M2M OAuth application access. In other IdPs, claims such as `sub` may be used. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Subject**: The specific user, group, or application allowed to access the share. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
- **Audiences**: One or more resource identifiers the JWT must match. A token is considered valid if its `aud` claim matches any of the listed audiences. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Example Configurations

### U2M with Entra ID

For sharing with a specific user (Object ID `11111111-2222-3333-4444-555555555555`) in an Entra ID tenant (`aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`): ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `oid` (Object ID)
- Subject: `11111111-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138` (the multi-tenant app ID registered by Databricks in Entra ID)

### U2M with Group in Entra ID

For sharing with a group (Object ID `66666666-2222-3333-4444-555555555555`) in the same tenant: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `groups`
- Subject: `66666666-2222-3333-4444-555555555555`
- Audiences: `64978f70-f6a6-4204-a29e-87d74bfea138`

### M2M with Entra ID

For an OAuth application (Application (client) ID `11111111-2222-3333-4444-555555555555`) in the same tenant: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- Issuer: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- Subject claim: `azp`
- Subject: `11111111-2222-3333-4444-555555555555` (the client ID of the registered OAuth application)
- Audiences: `66666666-2222-3333-4444-555555555555` (a valid audience identifier defined by the recipient, such as the client ID)

## Relationship to Authentication Flows

The policy is used in both [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md) and [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md) flows. In U2M, the subject claim is typically `oid` or `groups`; the audience must be the Databricks multi-tenant app ID (`64978f70-f6a6-4204-a29e-87d74bfea138`). In M2M, the subject claim is `azp` and the audience is defined by the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that uses OIDC federation.
- [Unity Catalog](/concepts/unity-catalog.md) — The permissions system that governs access after authentication.
- [Delta Sharing](/concepts/delta-sharing.md) — Broader data sharing protocol.
- [Identity Provider (IdP)](/concepts/internal-vs-external-identity-providers.md) — External authentication authority.
- JSON Web Token (JWT) — The token format used for authentication.
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md)
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md)

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
