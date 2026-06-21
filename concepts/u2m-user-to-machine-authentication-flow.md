---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ad4611d12289c8d99f605e1a555148b99a8aaf80d8f5feb3d221616d9a7c8bc7
  pageDirectory: concepts
  sources:
    - enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - u2m-user-to-machine-authentication-flow
    - U(AF
    - U2M Flow|user-to-machine (U2M) OIDC flow
  citations:
    - file: enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md
title: U2M (User-to-Machine) Authentication Flow
description: Authentication flow where a human user authenticates via their IdP (with optional MFA) and uses tools like Power BI or Tableau to access shared data, using the OAuth Authorization Code Grant flow.
tags:
  - authentication
  - oauth
  - user-experience
timestamp: "2026-06-19T18:40:09.281Z"
---

# U2M (User-to-Machine) Authentication Flow

## Overview

The **User-to-Machine (U2M) authentication flow** is a method for authenticating users from a recipient organization to access [OpenSharing](/concepts/opensharing.md) data shares using OIDC Federation. In this flow, a real user (not an automated service) authenticates through their organisation’s identity provider (IdP). The IdP issues a short-lived JSON Web Token (JWT) that is then validated by Databricks. The U2M flow is designed for recipients who do not have access to a Unity Catalog‑enabled Databricks workspace, and it uses the OAuth Authorization Code Grant flow to obtain access tokens from the IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

U2M authentication enables end users to query shared data through tools such as Power BI or Tableau. The data provider can define access policies that restrict data access to specific users or groups within the recipient organisation, ensuring precise control over who can view shared resources. Security policies, including Multi-Factor Authentication (MFA), are enforced by the recipient’s IdP. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## How It Works

1. The data provider creates a recipient in OpenSharing on Databricks and configures an OIDC token federation policy that specifies the recipient’s IdP issuer URL, the subject claim (e.g., `oid` for a specific user or `groups` for a group), the subject value (the user or group identifier), and one or more audiences. Databricks generates an OIDC portal URL. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

2. The provider shares the OIDC portal URL with the recipient. For U2M flow, the recipient inputs this endpoint into their U2M application (e.g., Power BI). ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

3. When the user attempts to access the shared data, the U2M client (e.g., Power BI) initiates the OAuth Authorization Code Grant flow. The user is redirected to their IdP, where they authenticate (with MFA if configured). The IdP issues a JWT containing identity claims. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

4. Databricks validates the JWT against the recipient’s policy (issuer, audience, subject). If validation succeeds, the request is authenticated and access is granted based on Unity Catalog permissions. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Configuration for Data Providers

When creating a recipient with OIDC Federation, the provider must configure a policy with the following fields:

- **Issuer URL**: The HTTPS URL of the recipient’s IdP (e.g., `https://login.microsoftonline.com/<tenant-id>/v2.0`).
- **Subject claim**: The JWT claim that identifies the authenticating user or group. For U2M, common values are:
  - `oid` (Object ID) – for a specific user.
  - `groups` – for a group of users.
- **Subject**: The actual value of the subject claim (e.g., a user’s object ID or group object ID).
- **Audiences**: One or more resource identifiers that the JWT’s `aud` claim must match. For U2M applications like Power BI and Tableau, the audience must be the multi-tenant app ID registered by Databricks in Entra ID: `64978f70-f6a6-4204-a29e-87d74bfea138`. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

The provider may choose to use their own IdP (internal IdP) for sharing within the same organisation, or trust the recipient’s IdP (external IdP). ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Example: Microsoft Entra ID

For a U2M scenario where the IdP is Microsoft Entra ID:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `oid` (for a specific user) or `groups` (for a group)
- **Subject**: The Object ID of the user or group (e.g., `11111111-2222-3333-4444-555555555555`)
- **Audiences**: `64978f70-f6a6-4204-a29e-87d74bfea138` (Databricks multi-tenant app ID)

The multi-tenant app ID `64978f70-f6a6-4204-a29e-87d74bfea138` is required for U2M applications like Power BI and Tableau. ^[enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md]

## Related Concepts

- [Machine-to-Machine (M2M) Authentication Flow](/concepts/machine-to-machine-m2m-authentication-flow.md) – For automated workloads using service principals.
- [OIDC Federation Policy](/concepts/oidc-federation-policy.md) – The policy object that defines IdP trust settings.
- [OpenSharing](/concepts/opensharing.md) – The Databricks feature for sharing data outside the organisation.
- Power BI Integration with Databricks
- Tableau Integration with Databricks

## Sources

- enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md

# Citations

1. [enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws.md](/references/enable-open-id-connect-oidc-federation-for-opensharing-recipients-databricks-on-aws-bc6cb862.md)
