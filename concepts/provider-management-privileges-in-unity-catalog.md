---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 475a3e02c475d1a8c4abb458fce15d9d3aa5719fae67535007fe6c0920156001
  pageDirectory: concepts
  sources:
    - manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - provider-management-privileges-in-unity-catalog
    - PMPIUC
  citations:
    - file: manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
    - file: |-
        manage-opensharing-providers-for-data-recipients-databricks-on-aws.md>

        > **Important:** Do not drop and recreate a provider object to apply a new credential. Catalogs bind to the provider's internal ID
    - file: not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
title: Provider Management Privileges in Unity Catalog
description: "The permission hierarchy for managing provider objects: USE PROVIDER for viewing, CREATE PROVIDER for creating, and owner privileges for updating and deleting providers in Unity Catalog."
tags:
  - unity-catalog
  - permissions
  - databricks
  - access-control
timestamp: "2026-06-19T19:26:47.189Z"
---

# Provider Management Privileges in Unity Catalog

**Provider Management Privileges** refer to the set of Unity Catalog permissions that govern how data recipients can view, create, update, and delete provider objects representing organizations that share data via OpenSharing. These privileges enable administrators to control access to shared data and manage the provider securable objects within a [Metastore](/concepts/metastore.md).

## Overview

In OpenSharing on Databricks, the term "provider" has two meanings: the organization that is sharing data with you, and a securable object in a recipient's Unity Catalog [Metastore](/concepts/metastore.md) that represents that organization. The existence of that securable object enables recipients to manage their team's access to shared data using Unity Catalog. Recipients with access to a Unity Catalog [Metastore](/concepts/metastore.md) typically do **not** need to create provider objects manually, because [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) creates them automatically. Manual provider creation is only required when the sharing protocol is Databricks-to-Open (using bearer tokens). ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## The Provider Object

A provider object is a [securable object](https://docs.databricks.com/aws/en/data-governance/unity-catalog/) stored in the recipient's Unity Catalog [Metastore](/concepts/metastore.md). It records the authentication type used by the sharing organization:

- `TOKEN` – Providers using the OpenSharing Databricks-to-Open sharing protocol (bearer tokens).
- `DATABRICKS` – Providers using the Databricks-to-Databricks sharing protocol (automatic rotation).
- `OAUTH_CLIENT_CREDENTIALS` and `OIDC_FEDERATION` – Additional authentication types for OpenSharing.

For TOKEN providers, the object contains the recipient profile endpoint and bearer token. For DATABRICKS providers, it stores the provider's cloud, region, and [Metastore](/concepts/metastore.md) ID. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Required Privileges

To manage providers, a user must have specific Unity Catalog privileges, typically granted by a [Metastore](/concepts/metastore.md) admin. The following table summarises the permissions needed for each operation:

| Operation | Required Privileges |
|-----------|---------------------|
| View a provider | `USE PROVIDER` privilege (globally) or be the provider owner |
| Create a provider | `CREATE PROVIDER` privilege |
| Update a provider | Owner of the provider object *and* `CREATE PROVIDER` privilege |
| Rename a provider | Owner of the provider object *and* `CREATE PROVIDER` privilege |
| Change owner | Owner of the provider object |
| Delete a provider | Owner of the provider object |
| Rotate credentials | Provider object owner or [Metastore](/concepts/metastore.md) admin |

If a workspace was created without a [Metastore](/concepts/metastore.md) admin, a Databricks account admin must grant a user or group the [Metastore](/concepts/metastore.md) admin role before any provider operations can be performed. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Viewing Providers

Recipients can view the list of providers in their [Metastore](/concepts/metastore.md) using [Catalog Explorer](/concepts/catalog-explorer.md), the Databricks Unity Catalog CLI, or the `SHOW PROVIDERS` SQL command in a notebook or SQL query editor. Users with the `USE PROVIDER` privilege can see all providers; other users see only the providers they own. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

To view details about a specific provider — including its authentication type, creation metadata, and the shares it has made available — recipients use DESCRIBE PROVIDER or the equivalent UI and CLI commands. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Viewing Shares from a Provider

The shares that a provider has shared with the recipient can be listed with the `SHOW SHARES IN PROVIDER` command or through Catalog Explorer. Permissions required: [Metastore](/concepts/metastore.md) admin, `USE PROVIDER` privilege, or provider object owner. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Updating Providers

Recipients can modify a provider object to rename it, change its owner, or add/update comments. This is done via `ALTER PROVIDER`, the Databricks CLI, or Catalog Explorer. To rename a provider, you must be both the owner and have the `CREATE PROVIDER` privilege. To change the owner, you must be the current owner. To update the comment, ownership alone is sufficient. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md>

> **Important:** Do not drop and recreate a provider object to apply a new credential. Catalogs bind to the provider's internal ID, not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Rotating Credentials for Open Recipients

When a provider using the Databricks-to-Open protocol rotates the bearer token and sends a new credential file, the recipient must update the provider object using the Databricks REST API (`PATCH` to the provider endpoint) with the new `recipient_profile_str`. `ALTER PROVIDER`, the Databricks CLI, and Catalog Explorer do **not** support updating credentials. After rotation, verify that the catalog, schemas, and tables remain accessible. For Databricks-to-Databricks providers, credential rotation happens automatically. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Deleting a Provider

To delete a provider object, the user must be the provider object owner. Deletion can be performed using Catalog Explorer, the Databricks CLI, or the `DROP PROVIDER` SQL command. Once deleted, all users in the recipient organization lose access to the data shared by that provider. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance platform that secures provider objects.
- [OpenSharing](/concepts/opensharing.md) – The data sharing protocol that uses provider objects.
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md) – Automatic provider creation method.
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md) – Manual provider creation required.
- [Catalog Explorer](/concepts/catalog-explorer.md) – A UI tool for managing providers.
- [Delta Sharing](/concepts/delta-sharing.md) – The underlying open protocol for data sharing.

## Sources

- manage-opensharing-providers-for-data-recipients-databricks-on-aws.md

# Citations

1. [manage-opensharing-providers-for-data-recipients-databricks-on-aws.md](/references/manage-opensharing-providers-for-data-recipients-databricks-on-aws-48fabb10.md)
2. manage-opensharing-providers-for-data-recipients-databricks-on-aws.md>

> **Important:** Do not drop and recreate a provider object to apply a new credential. Catalogs bind to the provider's internal ID
3. not its name. Recreating a provider with the same name breaks the catalog's connection to the shared data. ^[manage-opensharing-providers-for-data-recipients-databricks-on-aws.md
