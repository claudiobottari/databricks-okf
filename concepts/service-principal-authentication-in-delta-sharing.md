---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb5b0fca0726f3089f527a7b70a6d974ec7c461a987543da01a90f34e472ba11
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.8
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - service-principal-authentication-in-delta-sharing
    - SPAIDS
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: Service Principal Authentication in Delta Sharing
description: Registering an OAuth application as a Service Principal (SP) in the recipient's IdP to authenticate M2M access to Delta Sharing shares without sharing long-lived secrets between parties.
tags:
  - service-principal
  - authentication
  - security
  - databricks
timestamp: "2026-06-19T20:10:22.431Z"
---

## Service Principal Authentication in Delta Sharing

**Service Principal Authentication in Delta Sharing** refers to the machine‑to‑machine (M2M) OAuth Client Credentials grant flow that uses OpenID Connect (OIDC) federation to authenticate data recipients. In this flow, an OAuth application is registered as a **Service Principal (SP)** in the recipient’s identity provider (IdP), and short‑lived JSON Web Tokens (JWTs) are issued to access OpenSharing shares created in Databricks. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

This authentication method is typically used by autonomous applications—such as nightly jobs running on a virtual machine—that need to access Delta Sharing data without human intervention. It is an alternative to using long‑lived Databricks‑issued bearer tokens; no long‑lived secrets or credentials are shared between Databricks, the provider, and the recipient. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### How It Works

1. The recipient registers an OAuth application in their own IdP (e.g., Microsoft Entra ID) and configures it as a V2 application.
2. The recipient shares the following fields with the Databricks data provider:
   - **Issuer URL** – e.g., `https://login.microsoftonline.com/{tenantId}/v2.0`
   - **Subject claim** – the JWT payload field identifying the entity (for M2M in Entra ID, typically `azp`)
   - **Subject** – the unique identifier of the registered application (e.g., the Application (client) ID in Entra ID)
   - **Audience** – usually the resource’s `clientId`
3. The provider creates a recipient object in Databricks using OIDC federation and provides an OIDC profile portal URL to the recipient.
4. The recipient downloads an `oauth_config.share` profile file from the portal, adds their own `clientId`, `clientSecret`, and `scope` (e.g., `{clientId}/.default`), and uses the file to configure the [OpenSharing Python OSS client](/concepts/opensharing-python-client-for-delta-sharing.md).
5. The client authenticates by requesting an access token from the IdP’s token endpoint, using the Client Credentials grant. The token is presented to Databricks to access the shared tables. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Benefits

- **No long‑lived secrets** – Credentials are short‑lived and managed by the IdP.
- **No Databricks‑issued bearer tokens** – Authentication is fully delegated to the recipient’s own identity provider.
- **Suitable for automated workloads** – The flow requires no user interaction after initial configuration. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Prerequisites

- The recipient must have an identity provider that supports OIDC and the Client Credentials grant (e.g., Microsoft Entra ID, Okta, Auth0).
- The Databricks provider must have enabled OIDC federation for the recipient (see [Enable OIDC federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md)).
- The latest version of the `delta-sharing` Python client (≥1.3.1) must be installed. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

### Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) – Open protocol for secure data sharing.
- OIDC Federation – Using OpenID Connect to establish trust between IdPs and Databricks.
- [Bearer Token Authentication in Delta Sharing](/concepts/bearer-token-authentication-for-open-sharing.md) – Alternative authentication for non‑Databricks recipients.
- [User‑to‑Machine (U2M) OIDC Flow](/concepts/user-to-machine-u2m-authentication-flow.md) – Human‑mediated authentication for Delta Sharing.
- Recipient Object – Databricks entity that defines access permissions for a share.

### Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
