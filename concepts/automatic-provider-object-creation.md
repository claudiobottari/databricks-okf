---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4c053f396d690e588ba8776dcf7602ed72d0008878144bbd4df02473d75cf5d3
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-provider-object-creation
    - APOC
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: Automatic Provider Object Creation
description: For Databricks-to-Databricks sharing, provider objects are created automatically in the recipient's Unity Catalog metastore, so recipients typically do not need to manually create them.
tags:
  - delta-sharing
  - unity-catalog
  - databricks
  - automation
timestamp: "2026-06-19T19:28:32.359Z"
---

# Automatic Provider Object Creation

**Automatic Provider Object Creation** is a feature of [Unity Catalog](/concepts/unity-catalog.md) in Databricks that automatically creates a provider securable object in a recipient's [Metastore](/concepts/metastore.md) when data is shared using [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md). This mechanism enables recipients to manage their team's access to shared data using Unity Catalog without requiring manual setup. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Overview

In [OpenSharing](/concepts/opensharing.md) on Databricks, the term "provider" can refer to both the organization sharing data and a securable object in a recipient's Unity Catalog [Metastore](/concepts/metastore.md) that represents that organization. When data is shared via Databricks-to-Databricks sharing, these provider objects are created automatically in the recipient's Unity Catalog [Metastore](/concepts/metastore.md). This automation means that recipients with access to a Unity Catalog [Metastore](/concepts/metastore.md) typically do not need to create provider objects manually. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## When Automatic Creation Occurs

Automatic provider object creation happens specifically for [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) scenarios. In this protocol, the provider's workspace and the recipient's workspace both use Unity Catalog, allowing the system to automatically provision the necessary provider object in the recipient's [Metastore](/concepts/metastore.md) when a share is established. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Recipient Requirements

Data recipients must have access to a Databricks workspace that is enabled for Unity Catalog to benefit from automatic provider object creation. This feature does not apply to recipients who do not have Unity Catalog-enabled workspaces. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Manual Provider Object Creation

Most recipients should never need to manually create provider objects because automatic creation handles the typical case. However, manual creation may be necessary in specific scenarios, such as when using [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) protocols (with bearer tokens) instead of Databricks-to-Databricks sharing. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

To manually create a provider, a user must be a [Metastore](/concepts/metastore.md) admin or have the `CREATE PROVIDER` privilege granted by a [Metastore](/concepts/metastore.md) admin. If a workspace was created without a [Metastore](/concepts/metastore.md) admin, a Databricks account admin must grant a user or group the [Metastore](/concepts/metastore.md) admin role before they can work with provider objects. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Viewing Automatically Created Providers

Once created, provider objects can be viewed through several interfaces, provided the user has the appropriate permissions:

- **Catalog Explorer**: Navigate to the **Catalog** pane, click the gear icon, and select **OpenSharing**. The **Shared with me** tab displays all providers sharing data with the organization. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]
- **SQL**: Use the `SHOW PROVIDERS` command in a Databricks notebook or SQL query editor. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]
- **Unity Catalog CLI**: Use the command-line interface to list providers. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Viewing Provider Details

To view details about a provider object, users can use `DESCRIBE PROVIDER` SQL command, Catalog Explorer, or the CLI. Details include:

- Shares shared by the provider
- The provider's creator, creation timestamp, and comments
- Authentication type: `TOKEN` (Databricks-to-Open sharing) or `DATABRICKS` (Databricks-to-Databricks sharing)
- For Databricks-to-Databricks providers: cloud, region, and [Metastore](/concepts/metastore.md) ID of the provider's Unity Catalog [Metastore](/concepts/metastore.md)
- For Databricks-to-Open providers: recipient profile endpoint

Users must be a [Metastore](/concepts/metastore.md) admin, have the `USE PROVIDER` privilege, or be the provider object owner to view these details. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- [Delta Sharing](/concepts/delta-sharing.md) — The underlying protocol for data sharing across platforms
- [OpenSharing](/concepts/opensharing.md) — The Databricks implementation of Delta Sharing
- [Unity Catalog](/concepts/unity-catalog.md) — The governance platform that manages provider objects
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) — The sharing protocol that triggers automatic provider creation
- Provider Object — The securable object representing a data sharing organization
- Recipient Profile — Endpoint configuration for OpenSharing recipients

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
