---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b2880418a3ed29af70d6d2b621d43e7fe4e113c0694711c70ae3782f992346c
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - user-to-machine-u2m-authentication-flow
    - U(AF
    - User-to-Machine (U2M) Flow
    - User‑to‑Machine (U2M) OIDC Flow
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: User-to-Machine (U2M) Authentication Flow
description: OIDC-based authentication flow for interactive applications like Power BI and Tableau accessing Delta Sharing data
tags:
  - delta-sharing
  - authentication
  - oidc
  - u2m
timestamp: "2026-06-19T20:09:14.345Z"
---

```markdown
---
title: User-to-Machine (U2M) Authentication Flow
summary: OIDC authentication flow where a human user authenticates via their IdP to access shared data through client applications like Power BI or Tableau using the OAuth Authorization Code Grant.
sources:
  - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:11:10.211Z"
updatedAt: "2026-06-18T12:11:10.211Z"
tags:
  - authentication
  - delta-sharing
  - oidc
  - u2m
aliases:
  - user-to-machine-u2m-authentication-flow
  - U2M
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

# User-to-Machine (U2M) Authentication Flow

**User-to-Machine (U2M) Authentication Flow** is an authentication pattern in which a human user authenticates through their identity provider (IdP) to access shared data via a client application, such as Power BI or Tableau. In the context of [OpenSharing](/concepts/opensharing.md) with OIDC Federation, the U2M flow enables data recipients to access shared datasets without managing long-lived credentials, while the recipient's IdP enforces security policies like Multi-Factor Authentication (MFA). ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Overview

In a U2M authentication flow, a user from the recipient organization authenticates using their IdP. The IdP is responsible for issuing JSON Web Tokens (JWTs) and enforcing security policies, such as MFA. Databricks does not generate or manage these tokens — it only federates authentication to the recipient's IdP and validates the JWT against the recipient's configured federation policy. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md, read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

The U2M client application (e.g., Power BI) uses the **OAuth Authorization Code Grant** flow to obtain access tokens from the IdP. Once authenticated, users can access shared data using their preferred platform. The data provider can define access policies that restrict data access to specific users or groups within the recipient organization. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

OIDC federation is an alternative to using long-lived Databricks-issued bearer tokens. It enables fine-grained access control, supports MFA, and reduces security risks by eliminating the need for recipients to manage and secure shared credentials. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md, read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## How U2M Authentication Works in OpenSharing

The U2M authentication flow in OpenSharing follows these steps from the provider's perspective: ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

1. **Policy Creation**: When a data provider creates a recipient in OpenSharing on Databricks, they configure an OIDC token federation policy. For U2M flows, this policy specifies the issuer URL of the recipient IdP (such as Microsoft Entra ID or Okta) and defines the individual user or group that should have access to the share.

2. **Profile URL Generation**: Databricks generates an OIDC profile web portal URL based on the policy, and the provider shares that URL with the recipient. For U2M authentication, the recipient inputs the recipient endpoint from the OIDC profile web portal into their U2M application.

3. **Authentication**: When the recipient attempts to access shared data, authentication is federated to their IdP. The recipient's IdP generates a JWT containing identity claims. The lifetime of this short-lived token is enforced by the recipient's IdP.

4. **Token Validation**: The OpenSharing service validates the JWT against the recipient's policy to ensure it matches the expected claims, including issuer, audience, and subject. If validation succeeds, the request is authenticated, and access is granted based on Unity Catalog permissions.

## Recipient Workflow

From the recipient's perspective, the U2M flow involves providing IdP information to the provider and then using the OIDC portal to connect to the share. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
2. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
