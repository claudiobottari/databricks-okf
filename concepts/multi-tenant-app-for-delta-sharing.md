---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d05f3fb1490f5cb2624798e36c9ab897de648d532514b3e7d1aedbd0e13f71ca
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-tenant-app-for-delta-sharing
    - MAFDS
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md
title: Multi-Tenant App for Delta Sharing
description: Databricks-registered multi-tenant OAuth app (DeltaSharing) with client ID 64978f70-f6a6-4204-a29e-87d74bfea138 used by Power BI and Tableau recipients
tags:
  - delta-sharing
  - oauth
  - multi-tenant
  - entra-id
timestamp: "2026-06-19T20:09:24.754Z"
---

# Multi-Tenant App for Delta Sharing

The **Multi-Tenant App for Delta Sharing** is an OAuth-registered client application published by Databricks in Microsoft Entra ID (formerly Azure Active Directory). Identified by the client ID `64978f70-f6a6-4204-a29e-87d74bfea138`, this application enables user-to-machine (U2M) authentication flows for accessing Delta Sharing data through tools like Microsoft Power BI and Tableau. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Purpose and Use

The Multi-Tenant App serves as the OAuth client for recipients using U2M applications to access OpenSharing shares created in Databricks. When a recipient configures an OpenSharing connection in Power BI or Tableau, the application facilitates the OAuth authentication flow, directing the user to their identity provider (IdP) for sign-in. The app's client ID is used as the **Audience** value in the OIDC federation policy configuration. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

### Audience Configuration

For U2M authentication with Power BI and Tableau, the Databricks provider always uses the multi-tenant app ID `64978f70-f6a6-4204-a29e-87d74bfea138` as the audience. Recipients do not need to provide this value themselves; it is configured by the provider when setting up the OIDC federation policy. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Admin Consent Requirement

Before users in an organization can use the Multi-Tenant App for Delta Sharing, an Entra ID tenant administrator must grant admin consent for the application. This is a one-time action performed by opening the following URL in a browser and signing in with admin credentials: ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

```
https://login.microsoftonline.com/{organization}/adminconsent?client_id=64978f70-f6a6-4204-a29e-87d74bfea138
```

Replace `{organization}` with the Azure tenant ID. After admin consent is granted, users in that tenant can authenticate using the Multi-Tenant App to access shared Delta Sharing data. ^[read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for sharing data across platforms
- [OpenSharing](/concepts/opensharing.md) — The Delta Sharing protocol variant used for non-Databricks recipients
- OIDC Federation — The authentication method using JSON Web Tokens issued by a recipient's IdP
- [User-to-Machine (U2M) Authentication](/concepts/user-to-machine-u2m-authentication.md) — The OAuth flow for applications like Power BI and Tableau
- [Machine-to-Machine (M2M) Authentication](/concepts/machine-to-machine-m2m-authentication.md) — The alternative OAuth flow for service-to-service communication

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-a-u2m-flow-databricks-on-aws-89402a4e.md)
