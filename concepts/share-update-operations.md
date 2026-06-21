---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 51409cdbca6428ef97d5251eec0e154b854a9372f5c451451a545be0eed601fd
  pageDirectory: concepts
  sources:
    - manage-shares-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - share-update-operations
    - SUO
  citations:
    - file: manage-shares-for-opensharing-databricks-on-aws.md
title: Share Update Operations
description: Operations that can be performed on an existing OpenSharing share including renaming, removing assets, adding comments, renaming table aliases, enabling history access, managing partitions, and changing ownership.
tags:
  - delta-sharing
  - share-management
  - operations
timestamp: "2026-06-19T19:28:43.439Z"
---

# Share Update Operations

**Share Update Operations** refer to the administrative actions that providers can perform on existing [OpenSharing](/concepts/opensharing.md) shares in [Unity Catalog](/concepts/unity-catalog.md). A share is a securable object that bundles tables, [views](/concepts/shared-views-in-databricks-to-databricks-sharing.md), [volumes](/concepts/ucvolumedataset.md), notebooks, AI models, and other data assets for distribution to one or more recipients. The update operations allow providers to modify share properties, remove assets, change ownership, and control recipient access after the share has been created. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Types of Share Updates

Providers can perform the following update operations on a share:

- **Rename** the share.
- **Remove** tables, views, volumes, and schemas from the share.
- **Add or update** a comment on the share.
- **Rename** a table's alias — the name displayed to the recipient.
- **Enable or disable** access to a table's history data, which allows recipients to perform [time travel queries](/concepts/delta-lake-time-travel.md) or [streaming reads](/concepts/streamingdataset.md) of the table.
- **Add, update, or remove** partition definitions.
- **Change** the share owner.

^[manage-shares-for-opensharing-databricks-on-aws.md]

## Requirements

To perform update operations, users must meet the same requirements as those needed for creating a share. These include having the appropriate [privileges](/concepts/privileges-and-ownership.md) in [Unity Catalog](/concepts/unity-catalog.md) and being an owner of the share for certain operations such as deleting the share or transferring ownership. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Tools for Performing Updates

Providers can use the following tools to update shares:

- **Catalog Explorer** — The Databricks UI for browsing and managing data assets.
- **Databricks Unity Catalog CLI** — The command-line interface for Unity Catalog operations.
- **SQL commands** — Run DDL statements such as `ALTER SHARE` or `DELETE SHARE` in a Databricks notebook or the Databricks SQL query editor.

^[manage-shares-for-opensharing-databricks-on-aws.md]

## Owner Transfer and Security Implications

When transferring share ownership, providers should be aware of the security implications. The share owner determines how authorization and security features — such as [Attribute-Based Access Control](/concepts/attribute-based-access-control-abac.md) (ABAC) policies — are evaluated. Transferring share ownership to an over-privileged user allows recipients to have over-privileged access if a table or schema is secured by ABAC policies. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Deleting a Share

When a share is deleted, recipients can no longer access the shared data. To delete a share, the user must be an owner of the share. Providers can use [Catalog Explorer](/concepts/catalog-explorer.md), the CLI, or the `DELETE SHARE` SQL command. ^[manage-shares-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [OpenSharing](/concepts/opensharing.md) — The sharing framework for distributing data assets in Databricks.
- Create shares for OpenSharing — The process for creating new shares.
- Manage access to OpenSharing data shares — The process for granting recipient access.
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) — The management of data recipients.
- [Shares, providers, and recipients](/concepts/recipient-and-share-concepts.md) — The overall sharing model in Databricks.
- [Time travel queries](/concepts/delta-lake-time-travel.md) — A capability that can be enabled or disabled on shared tables.
- Partition definitions — Data organization that can be added or removed from a share.

## Sources

- manage-shares-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-shares-for-opensharing-databricks-on-aws.md](/references/manage-shares-for-opensharing-databricks-on-aws-a4962f9a.md)
