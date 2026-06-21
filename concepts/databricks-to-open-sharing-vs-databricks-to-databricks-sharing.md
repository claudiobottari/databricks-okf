---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 555b51da2eedd0ab79c34cba56d7d2916218cb12f39696c3182aed604e6747a7
  pageDirectory: concepts
  sources:
    - read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-open-sharing-vs-databricks-to-databricks-sharing
    - DSVDS
    - Open Sharing vs Databricks-to-Databricks sharing
  citations:
    - file: read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md
title: Databricks-to-Open Sharing vs Databricks-to-Databricks Sharing
description: Distinction between sharing data to recipients without a Unity Catalog-enabled Databricks workspace (Open Sharing) and recipients with such a workspace, with OIDC federation being an alternative to bearer tokens for the former.
tags:
  - delta-sharing
  - databricks
  - sharing-models
  - opensharing
timestamp: "2026-06-19T20:10:15.407Z"
---

# Databricks-to-Open Sharing vs Databricks-to-Databricks Sharing

**Databricks-to-Open Sharing** and **Databricks-to-Databricks Sharing** are two [Delta Sharing](/concepts/delta-sharing.md) patterns that differ primarily in the recipient’s computing environment and authentication method. Both allow a Databricks provider to share data with external consumers, but the choice depends on whether the recipient has direct access to a Unity Catalog-enabled Databricks workspace.

## Overview

Databricks-to-Databricks sharing is used when the data recipient has a Unity Catalog-enabled Databricks workspace. The recipient can consume shared data natively within their Databricks environment using existing workspace credentials and Unity Catalog policies. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

Databricks-to-Open sharing, by contrast, is designed for recipients who **do not** have access to a Unity Catalog-enabled Databricks workspace. These recipients may be external applications, non-Databricks platforms, or automated processes that need to read shared data using their own identity and access management stack. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

## Authentication Methods

Databricks-to-Open sharing supports two authentication mechanisms for non-Databricks recipients:

- **Bearer tokens**: Long-lived tokens issued by Databricks. The provider creates a recipient object and shares a connection profile containing the token. The recipient uses this token to authenticate and read shared data. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]
- **Open ID Connect (OIDC) federation**: A more secure alternative that avoids long-lived secrets. The recipient registers an OAuth 2.0 application (e.g., a service principal) in their own identity provider (IdP). The provider configures OIDC federation for the recipient, who then obtains short-lived JSON Web Tokens (JWTs) via the OAuth Client Credentials grant flow (for machine-to-machine, M2M, scenarios) or a user-to-machine (U2M) flow. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

In the OIDC M2M flow, no long-lived secrets or credentials are exchanged between Databricks and the recipient; authentication is fully delegated to the recipient’s IdP. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

Databricks-to-Databricks sharing typically uses the native Unity Catalog sharing model, which relies on workspace-level authentication and does not require the recipient to manage external tokens or OIDC configurations.

## Use Cases

| Sharing Type | Typical Recipient | Example Scenario |
|--------------|------------------|------------------|
| Databricks-to-Databricks | Another Databricks workspace with Unity Catalog | A data provider shares a curated dataset with a partner organization that also uses Databricks. The recipient accesses the data directly from their notebooks. |
| Databricks-to-Open (Bearer Token) | Non-Databricks clients (e.g., Python, Spark, pandas) | A nightly ETL job on a virtual machine reads shared data using a Databricks-issued bearer token. |
| Databricks-to-Open (OIDC Federation) | Applications with their own IdP (e.g., Microsoft Entra ID) | A third-party analytics application authenticates via its own Azure AD service principal to read shared data without sharing secrets. |

## Setting Up Databricks-to-Open Sharing with OIDC

The recipient must:

1. Register an OAuth application in their IdP (e.g., Microsoft Entra ID) and obtain a client ID, client secret, and tenant ID.
2. Send the issuer URL, subject claim, subject ID, and audience to the Databricks provider.
3. Download an OAuth profile file (`oauth_config.share`) from the provider’s portal.
4. Edit the profile to add `clientId`, `clientSecret`, and `scope`.
5. Use the OpenSharing Python OSS client (`delta-sharing>=1.3.1`) to connect. ^[read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md]

The provider, in turn, must enable OIDC federation for the recipient and generate the profile URL. For detailed provider instructions, see [Enable Open ID Connect (OIDC) federation for OpenSharing recipients](/concepts/oidc-federation-for-opensharing.md).

## Key Differences

| Aspect | Databricks-to-Databricks | Databricks-to-Open |
|--------|--------------------------|---------------------|
| Recipient environment | Unity Catalog-enabled workspace | Any non-Databricks system |
| Authentication | Workspace-native (Unity Catalog) | Bearer token or OIDC federation |
| Credential lifetime | Managed by workspace | Long-lived (bearer) or short-lived (OIDC) |
| Recipient identity management | Databricks workspace identity | Recipient’s own IdP (for OIDC) |
| Profile file | Typically none | `.share` or `oauth_config.share` file needed |

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md)
- OIDC Federation
- [Unity Catalog](/concepts/unity-catalog.md)
- [Bearer Token Authentication](/concepts/bearer-token-authentication-for-open-sharing.md)
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)
- [OpenSharing Python OSS Client](/concepts/opensharing-python-client-for-delta-sharing.md)

## Sources

- read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md

# Citations

1. [read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws.md](/references/read-data-shared-using-open-id-connect-oidc-federation-in-an-m2m-flow-databricks-on-aws-cf8699ed.md)
