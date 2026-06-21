---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a13afde9446233444de1d90f15c8b18f06608f5217527e79e3d3aca317cbf94
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-provider-object
    - OPO
    - OpenSharing Provider
    - OpenSharing provider setup
    - Data Sharing Provider Setup
    - OpenSharing setup for providers
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: OpenSharing Provider Object
description: A securable object in a recipient's Unity Catalog metastore that represents a data provider organization sharing data via OpenSharing on Databricks.
tags:
  - delta-sharing
  - unity-catalog
  - databricks
  - opensharing
timestamp: "2026-06-19T19:26:50.924Z"
---

# OpenSharing Provider Object

An **OpenSharing Provider Object** is a securable object in a recipient's Unity Catalog [Metastore](/concepts/metastore.md) that represents an organization sharing data with them using [OpenSharing](/concepts/opensharing.md) on Databricks. The term "provider" can refer both to the sharing organization itself and to this [Metastore](/concepts/metastore.md) object that represents it. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Purpose

The provider object enables recipients to manage their team's access to shared data using [Unity Catalog](/concepts/unity-catalog.md). Its existence in the recipient's [Metastore](/concepts/metastore.md) allows for governance of who within the recipient organization can view and query the shared datasets. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Automatic Creation

As a recipient with access to a Unity Catalog [Metastore](/concepts/metastore.md), you typically do not need to create provider objects manually. When data is shared using [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), provider objects are created automatically in your Unity Catalog [Metastore](/concepts/metastore.md). Most recipients should never need to create a provider object themselves. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Prerequisites

To manage providers in your Databricks workspace:

- Your workspace must be enabled for Unity Catalog.
- To **view** a provider, you need the `USE PROVIDER` privilege (or be a [Metastore](/concepts/metastore.md) admin).
- To **create** a provider, you need the `CREATE PROVIDER` privilege (or be a [Metastore](/concepts/metastore.md) admin).
- To **update** a provider, you must be the owner of the provider object and have the `CREATE PROVIDER` privilege.

If your workspace was created without a [Metastore](/concepts/metastore.md) admin, a Databricks account admin must grant a user or group the [Metastore](/concepts/metastore.md) admin role before you can work with provider objects. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Viewing Providers

You can view a list of available data providers using Catalog Explorer, the Databricks Unity Catalog CLI, or the `SHOW PROVIDERS` SQL command. Users with the `USE PROVIDER` privilege can see all providers in the [Metastore](/concepts/metastore.md); other users see only the providers they own. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

### Provider Details

Viewing provider details (via Catalog Explorer, `DESCRIBE PROVIDER`, or CLI) reveals:

- Shares shared by the provider.
- The provider's creator, creation timestamp, comments, and authentication type.
- For [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) (`DATABRICKS` authentication type): the cloud, region, and [Metastore](/concepts/metastore.md) ID of the provider's Unity Catalog [Metastore](/concepts/metastore.md).
- For [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) (`TOKEN` authentication type): your recipient profile endpoint hosting the OpenSharing sharing server. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Updating a Provider

You can modify a provider object to:

- Rename the provider for better user visibility.
- Change the owner of the provider object.
- Add or modify comments.

The initial owner is the [Metastore](/concepts/metastore.md) admin. Updating the owner requires being the current owner; renaming requires both the `CREATE PROVIDER` privilege and ownership. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Credential Rotation

For providers with authentication type `TOKEN`, `OAUTH_CLIENT_CREDENTIALS`, or `OIDC_FEDERATION`, a provider using the Databricks-to-Open sharing protocol may rotate your bearer token. When this happens, use the Databricks REST API to update the provider object's credentials via a `PATCH` request to the provider endpoint. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

**Important**: Do not drop and recreate the provider to apply new credentials. Catalogs bind to the provider's internal ID, not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

Databricks-to-Databricks providers (`DATABRICKS` authentication type) rotate credentials automatically. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Deleting a Provider

Deleting a provider removes access to all data shared by that provider for the recipient organization. You must be the provider object owner to delete it. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)
- [Delta Sharing](/concepts/delta-sharing.md)
- [OpenSharing Share Object](/concepts/opensharing-share-object.md)

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
