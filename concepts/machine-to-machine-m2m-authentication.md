---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0d9ccbba90809e7e8e4e7d657ba116a46a5bb0ab1f2320e60f0d5930a735a00b
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - machine-to-machine-m2m-authentication
    - M(A
    - Machine-to-Machine Authentication
    - OAuth Machine-to-Machine (M2M) Authentication
    - OAuth machine-to-machine (M2M) authentication
    - OAuth machine-to-machine authentication
    - OAuth (machine-to-machine)
    - OAuth M2M Authentication
    - OAuth M2M authentication
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: Machine-to-Machine (M2M) Authentication
description: Authentication flow for automated workloads where a service principal registered in the recipient's IdP enables applications or scripts to access shared data programmatically using the OAuth Client Credentials Grant flow without user interaction.
tags:
  - authentication
  - delta-sharing
  - automation
timestamp: "2026-06-19T10:21:19.761Z"
---

# Machine-to-Machine (M2M) Authentication

**Machine-to-Machine (M2M) Authentication** refers to authentication flows in which automated services, scripts, or applications authenticate without direct user interaction. In the context of [OpenSharing](/concepts/opensharing.md) on Databricks, M2M authentication is implemented using Open ID Connect (OIDC) Federation, allowing recipients to access shared data programmatically. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

M2M authentication is ideal for automated workloads such as nightly jobs or background services that require access to shared data without user interaction. The recipient organization registers a Service Principal in its identity provider (IdP). This service identity enables applications or scripts to securely access resources programmatically. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

No secrets or credentials are exchanged between Databricks, the provider, or the recipient. All secret management remains internal to each organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Authentication Flow

M2M clients use the [OAuth Client Credentials Grant](/concepts/oauth-client-credentials-grant-m2m-flow.md) flow to retrieve access tokens from the recipient’s IdP. Common clients include the Python OpenSharing Client and the Spark OpenSharing Client. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

1. The recipient application (client) obtains a JWT from its IdP using the client credentials grant.
2. The application presents the JWT to Databricks’ OpenSharing service.
3. Databricks validates the JWT against the recipient’s configured [OIDC Federation Policy](/concepts/oidc-federation-policy.md), checking claims such as issuer, audience, and subject.
4. If validation succeeds, the request is authenticated and access is granted based on [Unity Catalog](/concepts/unity-catalog.md) permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Configuration Example (Microsoft Entra ID)

For an M2M OAuth application with Application (client) ID `11111111-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`, the policy is configured as follows: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

| Field | Value |
|-------|-------|
| **Issuer** | `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0` |
| **Subject claim** | `azp` |
| **Subject** | `11111111-2222-3333-4444-555555555555` (the Application client ID, found in the recipient’s Entra ID portal) |
| **Audiences** | `66666666-2222-3333-4444-555555555555` (any valid audience identifier defined by the recipient, such as the client ID of the registered OAuth application) |

## Use Cases

- Automated nightly jobs that need to read shared datasets for reporting.
- Background services that process streaming or batch data from shares.
- Integration pipelines that consume shared data without human intervention.

## Related Concepts

- Open ID Connect (OIDC) Federation – The authentication protocol used for M2M in OpenSharing.
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md) – The counterpart flow for interactive users.
- Service Principal – The identity used by the application in the recipient’s IdP.
- JWT – The token type exchanged during authentication.
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) – The policy object that defines allowed issuers, subjects, and audiences.
- [OpenSharing](/concepts/opensharing.md) – Databricks’ open data sharing protocol.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that governs permissions on shared data.

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
