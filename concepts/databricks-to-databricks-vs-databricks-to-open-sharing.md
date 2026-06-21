---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9287ee0f80d1491453e0939c24b61a78b331e85b899a6bc32b9d6c4e514f561c
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-to-databricks-vs-databricks-to-open-sharing
    - DVDS
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: Databricks-to-Databricks vs Databricks-to-Open Sharing
description: "Two OpenSharing protocols: Databricks-to-Databricks (DATABRICKS auth) for cross-Databricks sharing, and Databricks-to-Open (TOKEN/OAUTH/OIDC auth) for sharing with non-Databricks recipients."
tags:
  - delta-sharing
  - authentication
  - databricks
  - opensharing
timestamp: "2026-06-19T19:26:27.750Z"
---

# Databricks-to-Databricks vs Databricks-to-Open Sharing

**Databricks-to-Databricks sharing** and **Databricks-to-Open sharing** are two protocols for sharing data via [Delta Sharing](/concepts/delta-sharing.md) on Databricks. The key difference lies in how the recipient accesses the shared data and whether a provider object is automatically created in the recipient's [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md).

## Overview

In OpenSharing on Databricks, the term "provider" can refer both to the organization sharing data and to a securable object in a recipient's Unity Catalog [Metastore](/concepts/metastore.md) that represents that organization. The existence of this securable object enables recipients to manage their team's access to shared data using Unity Catalog. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Databricks-to-Databricks Sharing

Databricks-to-Databricks sharing is the recommended protocol for sharing data between Databricks workspaces. When data is shared using this method, provider objects are created automatically in the recipient's Unity Catalog [Metastore](/concepts/metastore.md). As a recipient with access to a Unity Catalog [Metastore](/concepts/metastore.md), you typically do not need to create provider objects manually. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

The authentication type for Databricks-to-Databricks providers is `DATABRICKS`. When viewing provider details, the system displays the cloud, region, and [Metastore](/concepts/metastore.md) ID of the provider's Unity Catalog [Metastore](/concepts/metastore.md). ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

Credentials for Databricks-to-Databricks providers rotate automatically, requiring no manual intervention from the recipient. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Databricks-to-Open Sharing

Databricks-to-Open sharing is used when the provider is not a Databricks workspace or when sharing with recipients who do not have Unity Catalog-enabled workspaces. This protocol uses bearer tokens, OAuth client credentials, or OIDC federation for authentication. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

The authentication type for Databricks-to-Open providers is `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`. When viewing provider details, the system displays the recipient's profile endpoint, which is where the OpenSharing sharing server is hosted. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

### Credential Rotation

Unlike Databricks-to-Databricks sharing, credentials for Databricks-to-Open providers do not rotate automatically. When a provider rotates the bearer token and sends a new credential file, the recipient must update the provider object using the Databricks REST API. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

Important: Do not drop and recreate the provider to apply a new credential. Catalogs bind to the provider's internal ID, not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Comparison Table

| Feature | Databricks-to-Databricks | Databricks-to-Open |
|---|---|---|
| Authentication type | `DATABRICKS` | `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION` |
| Provider object creation | Automatic | May require manual creation |
| Credential rotation | Automatic | Manual (via REST API) |
| Provider details shown | Cloud, region, [Metastore](/concepts/metastore.md) ID | Recipient profile endpoint |
| Recommended for | Databricks-to-Databricks sharing | Sharing with non-Databricks recipients |

## When to Use Each Protocol

- **Databricks-to-Databricks**: Use when both the provider and recipient are Databricks workspaces with Unity Catalog enabled. This is the recommended approach as it simplifies management with automatic provider object creation and credential rotation. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

- **Databricks-to-Open**: Use when the provider is not a Databricks workspace, or when recipients do not have Unity Catalog-enabled workspaces. This protocol requires more manual management, including credential rotation. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The open protocol for secure data sharing across platforms
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that manages provider objects
- [OpenSharing](/concepts/opensharing.md) — The Databricks feature for managing shared data
- [Provider objects](/concepts/sap-bdc-provider-object.md) — Securable objects representing data providers in Unity Catalog
- [Credential rotation](/concepts/provider-credential-rotation.md) — The process of updating authentication tokens for OpenSharing providers

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
