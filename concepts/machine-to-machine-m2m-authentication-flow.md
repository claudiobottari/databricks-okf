---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 865a840b2d736115fff835b5a053a1b1ee8ca50f0ed142d97fe0c526c52bb7d7
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - machine-to-machine-m2m-authentication-flow
    - M(AF
    - Machine-to-Machine (M2M) Flow
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Machine-to-Machine (M2M) Authentication Flow
description: OIDC authentication flow for automated workloads where a service principal registered in the IdP programmatically accesses shared data using the OAuth Client Credentials Grant, with no user interaction required.
tags:
  - authentication
  - delta-sharing
  - m2m
timestamp: "2026-06-18T15:36:21.965Z"
---

# Machine-to-Machine (M2M) Authentication Flow

**Machine-to-Machine (M2M) Authentication Flow** is an authentication method for [OpenSharing](/concepts/opensharing.md) that enables automated workloads, such as nightly jobs or background services, to access shared data without user interaction. The recipient organization registers a Service Principal in its identity provider (IdP), and applications or scripts use the OAuth Client Credentials Grant flow to retrieve access tokens from the IdP. No secrets or credentials are exchanged between Databricks, the provider, or the recipient — all secret management remains internal to each organization.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

M2M authentication is one of two authentication scenarios supported by [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md), alongside [User-to-Machine (U2M) Authentication Flow](/concepts/user-to-machine-u2m-authentication-flow.md). It is designed for programmatic access scenarios where workloads must run autonomously. M2M clients include the Python OpenSharing Client and Spark OpenSharing Client.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How M2M Authentication Works

In the M2M flow, the recipient's identity provider is responsible for issuing JSON Web Tokens (JWTs) and enforcing security policies such as Multi-Factor Authentication (MFA). The lifetime of the JWT token is governed by the recipient's IdP. Databricks does not generate or manage these tokens — it only federates authentication to the recipient's IdP and validates the JWT against the recipient's configured federation policy.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Flow Steps

1. The data provider creates a recipient in OpenSharing on Databricks and configures an OIDC token federation policy specifying the issuer URL of the recipient IdP, the subject claim identifying the service principal or OAuth application, and the subject value.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
2. Databricks generates an OIDC profile web portal URL based on the policy. The recipient application developer downloads the profile file and references it in the recipient client app.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
3. When the recipient application attempts to access shared data, authentication is federated to the recipient's IdP. The recipient's IdP generates a JWT containing identity claims.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]
4. The OpenSharing service validates the JWT against the recipient's policy to ensure it matches the expected claims, including issuer, audience, and subject. If validation is successful, access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Configuration

### Subject Claim for M2M

For M2M authentication, the subject claim in the OIDC federation policy identifies the OAuth application. In Microsoft Entra ID, use `azp` as the subject claim value. The subject is the Application (client) ID of the registered OAuth application, which can be found in the recipient's Entra ID portal.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

### Example: M2M with Entra ID

For an M2M OAuth application with Application (client) ID `11111111-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

| Field | Value |
|-------|-------|
| Issuer | `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0` |
| Subject claim | `azp` |
| Subject | `11111111-2222-3333-4444-555555555555` |
| Audiences | `66666666-2222-3333-4444-555555555555` (any valid audience identifier defined by the recipient, such as the client ID of the registered OAuth application) |

## Requirements

- The recipient must have an identity provider that supports OIDC.
- The recipient must register a Service Principal or OAuth application in their IdP.
- M2M clients (such as the Python OpenSharing Client or Spark OpenSharing Client) use the OAuth Client Credentials Grant flow to retrieve access tokens from the IdP.^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [OIDC Federation for OpenSharing](/concepts/oidc-federation-for-opensharing.md) — Overview of OIDC federation for Delta Sharing
- [User-to-Machine (U2M) Authentication Flow](/concepts/user-to-machine-u2m-authentication-flow.md) — The alternative authentication flow for end-user applications
- [OpenSharing](/concepts/opensharing.md) — Databricks-to-open sharing for non-Databricks recipients
- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- JSON Web Tokens (JWTs) — The token format used for OIDC authentication
- [OAuth Client Credentials Grant Flow](/concepts/oauth-client-credentials-grant-m2m-flow.md) — The OAuth flow used for M2M authentication
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-delta-sharing.md) — The alternative authentication method using long-lived tokens

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
