---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d39132e2c6ffffb857f9db7ac78b20f3d90ec8c1880dbc18535cd5baeb3df03
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - entra-id-configuration-for-delta-sharing-recipients
    - EICFDSR
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: Entra ID Configuration for Delta Sharing Recipients
description: Configuration steps for Microsoft Entra ID users to provide issuer, subject claim, subject, and audience values for OIDC federation setup
tags:
  - delta-sharing
  - entra-id
  - configuration
  - identity-provider
timestamp: "2026-06-19T20:10:47.945Z"
---

# Entra ID Configuration for Delta Sharing Recipients

**Entra ID Configuration for Delta Sharing Recipients** refers to the setup required for data recipients who use Microsoft Entra ID as their identity provider (IdP) to authenticate and access [Delta Sharing](/concepts/delta-sharing.md) shares from Databricks providers using Open ID Connect (OIDC) Federation. This configuration is part of the user-to-machine (U2M) authentication flow, where applications like Power BI or Tableau connect to OpenSharing shares using short-lived JWT tokens issued by the recipient's IdP. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Overview

In the U2M OIDC federation flow, the recipient's IdP (in this case, Microsoft Entra ID) is responsible for issuing JWT tokens and enforcing security policies such as Multi-Factor Authentication (MFA). Databricks does not generate or manage these tokens; it only federates authentication to the recipient's IdP and validates the JWT against the configured federation policy. This approach serves as an alternative to using long-lived Databricks-issued bearer tokens, offering fine-grained access control, MFA support, and reduced security risks. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Required Configuration Fields

To set up OIDC federation with Entra ID, recipients must provide the following values to the Databricks provider:

### Issuer URL

The token issuer, specified in the `iss` claim of OIDC JWT tokens. For Entra ID, the format is:

```
https://login.microsoftonline.com/{tenantId}/v2.0
```

Replace `{tenantId}` with your Entra tenant ID. To find your tenant ID, refer to the Microsoft Entra ID documentation. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Subject Claim

The field in the JWT payload that identifies the entity accessing the data. For U2M scenarios with Entra ID, common values include:

- **`oid` (Object ID)**: Select when a single user requires access.
- **`groups`**: Select when a group of users requires access.

^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Subject

The unique identifier of the identity that can access the shared data:

- If using `oid` as the subject claim, provide the Object ID of the user from Entra ID.
- If using `groups` as the subject claim, provide the Object ID of the group from Entra ID. The group object ID can be found in the Entra ID console by selecting **Groups** and locating the group in the list.

^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Audience

For U2M authentication, the recipient does not need to provide this value. The Databricks provider always uses:

```
64978f70-f6a6-4204-a29e-87d74bfea138
```

This is the client ID for the `Databricks published multi-tenant App(DeltaSharing)` OAuth-registered client app that recipients use to access Databricks shares using Power BI and Tableau. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Example Configurations

### Sharing with a Single User

For sharing with a specific user with Object ID `11111111-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `oid`
- **Subject**: `11111111-2222-3333-4444-555555555555`
- **Audience**: `64978f70-f6a6-4204-a29e-87d74bfea138`

^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Sharing with a Group

For sharing with a specific group with Object ID `66666666-2222-3333-4444-555555555555` in Entra ID tenant `aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee`:

- **Issuer**: `https://login.microsoftonline.com/aaaaaaaa-bbbb-4ccc-dddd-eeeeeeeeeeee/v2.0`
- **Subject claim**: `groups`
- **Subject**: `66666666-2222-3333-4444-555555555555`
- **Audience**: `64978f70-f6a6-4204-a29e-87d74bfea138`

^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Admin Consent Requirement

To use the Databricks published multi-tenant app (DeltaSharing), the Entra ID tenant admin must grant admin consent. This is a one-time action performed by opening the following URL in a browser and signing in with admin identity:

```
https://login.microsoftonline.com/{organization}/adminconsent?client_id=64978f70-f6a6-4204-a29e-87d74bfea138
```

Replace `{organization}` with your Azure tenant ID. For more information, see the Microsoft Entra admin consent documentation. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Accessing Shares

After the provider creates the OIDC policy, they share an OIDC profile portal URL. Recipients can access this URL from anywhere and multiple times, as it does not contain sensitive information. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Power BI

1. Ensure Power BI Desktop is version 2.141.1253.0 (released March 31, 2025) or later.
2. Go to the OIDC profile portal URL and select the **U2M** tile.
3. Under **To use on Power BI**, copy the serving endpoint.
4. In Power BI, go to **Get data**, search for **Delta Sharing**, and select **OpenSharing**.
5. Paste the serving endpoint URL and authenticate using OAuth, signing in with your IdP credentials.

### Tableau

1. Go to the OIDC profile portal URL and select the **U2M** tile.
2. Under **To use on Tableau**, download the profile file.
3. Open the Tableau OpenSharing OAuth connector to authenticate automatically with your IdP.
4. Paste the OpenSharing endpoint URL; the bearer token is prepopulated.

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- Open ID Connect (OIDC) Federation — Authentication framework using JWT tokens
- [Delta Sharing Recipients](/concepts/delta-sharing-recipient-object.md) — Entities that receive shared data
- [Machine-to-Machine (M2M) Flow](/concepts/machine-to-machine-m2m-authentication.md) — Authentication for service-to-service communication
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-open-sharing.md) — Alternative authentication method using long-lived tokens

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
