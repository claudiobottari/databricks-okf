---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 69314172361dbe1428d3979763187dd494fe2e302d350bbb3790c9d60933e12c
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - short-lived-jwt-token-authentication
    - SJTA
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Short-lived JWT Token Authentication
description: Security model where JWTs are issued and lifetime-enforced by the recipient's IdP, not by Databricks, eliminating the need to manage shared credentials or long-lived bearer tokens.
tags:
  - jwt
  - security
  - token-management
timestamp: "2026-06-19T18:41:00.022Z"
---

# Short-lived JWT Token Authentication

**Short-lived JWT Token Authentication** is an authentication method for secure data sharing that uses JSON Web Tokens (JWTs) with a limited lifetime, generated and managed by an external identity provider (IdP). In the context of OpenSharing, this approach federates authentication to a recipient's IdP, which issues short-lived JWTs that Databricks validates to grant access to shared data. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

In this authentication model, the recipient's IdP is responsible for issuing JWT tokens and enforcing security policies, including Multi-Factor Authentication (MFA). The lifetime of the JWT token is governed by the recipient's IdP. Databricks does not generate or manage these tokens — it only federates authentication to the recipient's IdP and validates the JWT against the recipient's configured federation policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

Short-lived JWT token authentication serves as an alternative to using long-lived Databricks-issued bearer tokens for connecting non-Databricks recipients to providers. It enables fine-grained access control, supports MFA, and reduces security risks by eliminating the need for recipients to manage and secure shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How It Works

The authentication flow involves three main steps:

1. **Policy Configuration**: When a data provider creates a recipient in OpenSharing on Databricks, they configure an OIDC token federation policy specifying the issuer URL of the recipient IdP (such as Microsoft Entra ID or Okta) and defining which user, group, service principal, or OAuth application should have access to the share. Databricks then generates an OIDC profile web portal URL based on the policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

2. **Token Generation**: When the recipient attempts to access shared data, authentication is federated to their IdP. The recipient's IdP generates a JWT containing identity claims, and the lifetime of this short-lived token is enforced by the recipient's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

3. **Token Validation**: The OpenSharing service validates the JWT against the recipient's policy to ensure it matches the expected claims, including issuer, audience, and subject. If validation is successful, the request is authenticated, and access is granted based on Unity Catalog permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Flows

### User-to-Machine (U2M) Authentication

In U2M authentication, a user from the recipient organization authenticates using their IdP. If MFA is configured, it is enforced during login. Once authenticated, users can access shared data using tools like Power BI or Tableau. The U2M client application uses the OAuth Authorization Code Grant flow to obtain access tokens from the IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Machine-to-Machine (M2M) Authentication

M2M authentication is designed for automated workloads such as nightly jobs or background services that require access without user interaction. The recipient organization registers a Service Principal in its IdP, enabling applications or scripts to securely access resources programmatically. M2M clients use the OAuth Client Credentials Grant flow to retrieve access tokens from the IdP. No secrets or credentials are exchanged between Databricks, the provider, or the recipient. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Identity Provider Options

You can use OIDC federation with either an internal or external identity provider:

- **Internal Identity Provider (Provider-Managed)**: Useful for sharing data within organizations where different departments share the same IdP but do not have direct Databricks access. Security policies are enforced by the provider's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

- **External Identity Provider (Recipient-Managed)**: The provider sets up the sharing policy to trust the recipient's IdP, and the recipient organization retains full control over who can access the shared data. Security policies are enforced by the recipient's IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Policy Configuration

To configure a recipient that uses short-lived JWT authentication, the data provider specifies the following in an OIDC federation policy:

- **Issuer URL**: The HTTPS URL of the IdP issuing the JWT token.
- **Subject claim**: The claim in the JWT that identifies the authenticating identity type. In Microsoft Entra ID, this can be `oid` (Object ID) for users, `groups` for user groups, or `azp` for OAuth applications.
- **Subject**: The specific user, group, or application allowed to access the share.
- **Audiences**: One or more resource identifiers the JWT must match.

^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- OIDC Federation — The underlying protocol for identity federation
- [OpenSharing](/concepts/opensharing.md) — The data sharing framework that uses this authentication method
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages permissions for shared data
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — The alternative authentication method using long-lived tokens
- Microsoft Entra ID — A common identity provider used with OIDC federation

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
