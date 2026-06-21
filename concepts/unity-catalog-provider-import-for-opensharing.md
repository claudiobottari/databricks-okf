---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b1ef69a0f19a4dffe6fec9015deee0bb08454444ecec915cc87ca919a1ffbe69
  pageDirectory: concepts
  sources:
    - read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-provider-import-for-opensharing
    - UCPIFO
  citations:
    - file: read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
    - file: |-
        read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md>

        ## Credential Rotation

        If the provider rotates the credential
    - file: you can apply the new credential to the existing provider object in Unity Catalog without recreating the catalog. This is done using the Databricks REST API — see Rotate credentials for open recipients. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
title: Unity Catalog Provider Import for OpenSharing
description: A UI-based workflow in Databricks Catalog Explorer that allows recipients to import provider credentials, create catalogs from shares, and use Unity Catalog access controls without manually handling credential files.
tags:
  - unity-catalog
  - databricks
  - data-sharing
timestamp: "2026-06-19T20:11:00.143Z"
---

# Unity Catalog Provider Import for OpenSharing

**Unity Catalog Provider Import for OpenSharing** is the process of importing an external data provider into [Unity Catalog](/concepts/unity-catalog.md) using the OpenSharing protocol with bearer tokens. This enables users to read data shared through the Databricks-to-Open sharing model without manually managing credential files, while leveraging Unity Catalog's access control and query capabilities. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Overview

After a data provider shares a credential file with your team, you can import that provider directly into Unity Catalog using the **Import provider** UI in Catalog Explorer. This integration offers several advantages over direct connector usage:

- Create catalogs from shares with a single click.
- Use Unity Catalog access controls to grant or restrict access to shared tables.
- Query shared data using standard Unity Catalog SQL syntax.
- Apply rotated credentials to the existing provider object without recreating the catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Prerequisites

Before importing a provider, a member of your team must download the credential file shared by the data provider and share that file or its location with you via a secure channel. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

**Permissions required**: You must be a [Metastore](/concepts/metastore.md) admin, or have both the `CREATE PROVIDER` and `USE PROVIDER` privileges for your [Unity Catalog](/concepts/unity-catalog.md) [Metastore](/concepts/metastore.md). ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Importing a Provider via Catalog Explorer

1. In your Databricks workspace, click the **Catalog** icon to open Catalog Explorer.
2. At the top of the **Catalog** pane, click the gear icon and select **OpenSharing** (alternatively, click **Share > OpenSharing** in the upper-right corner).
3. On the **Shared with me** tab, click **Install share**.
4. Enter the provider name. The name cannot include spaces.
5. Upload the credential file that the provider shared with you.
6. (Optional) Enter a comment.
7. Click **Import**. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Creating Catalogs from Shares

After importing the provider:

1. On the **Shares** tab, click **Create catalog** on the share row.
2. Grant access to the catalogs using standard Unity Catalog permission management.
3. Read the shared data objects just as you would any data object registered in Unity Catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md>

## Credential Rotation

If the provider rotates the credential, you can apply the new credential to the existing provider object in Unity Catalog without recreating the catalog. This is done using the Databricks REST API — see Rotate credentials for open recipients. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Access Control

Shared data accessed through Unity Catalog Provider Import can be managed using Unity Catalog's permission model. See:

- How do I make shared data available to my team?
- Manage permissions for schemas, tables, and volumes in an OpenSharing catalog ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Relationship to Direct Connector Access

If your workspace is enabled for Unity Catalog and you have imported the provider via the UI, you do **not** need to install the `delta-sharing` Python connector or provide the path to the credential file when querying shared tables. You can access shared tables just as you would any other table registered in Unity Catalog. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

For workspaces that are **not** enabled for Unity Catalog, the Python notebook approach (using `delta-sharing` libraries) is required instead. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md]

## Related Concepts

- [OpenSharing Protocol](/concepts/opensharing-protocol.md) — The open standard for data sharing with bearer tokens
- [Databricks-to-Open Sharing Model](/concepts/databricks-to-open-sharing-model.md) — The provider-recipient model used for data sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The catalog system that manages imported providers and shared data
- Credential File — The file shared by the provider containing endpoint and token information
- [Delta Sharing](/concepts/delta-sharing.md) — The underlying sharing protocol

## Sources

- read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md

# Citations

1. [read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md](/references/read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws-9252dd38.md)
2. read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md>

## Credential Rotation

If the provider rotates the credential
3. you can apply the new credential to the existing provider object in Unity Catalog without recreating the catalog. This is done using the Databricks REST API — see Rotate credentials for open recipients. ^[read-data-shared-using-opensharing-databricks-to-open-sharing-with-bearer-tokens-databricks-on-aws.md
