---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 314b056cf7f94cc95aabeddecbfaad02f8cafb58a55b6f4c958867f3b0c06eef
  pageDirectory: concepts
  sources:
    - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - create-recipient-privilege
    - CRP
  citations:
    - file: create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
title: CREATE RECIPIENT Privilege
description: A Unity Catalog privilege required to create recipient objects in OpenSharing, granted at the metastore level.
tags:
  - databricks
  - permissions
  - access-control
timestamp: "2026-06-19T18:01:28.245Z"
---

---
title: CREATE RECIPIENT Privilege
summary: A metastore-level privilege in Unity Catalog that allows users to create recipient objects for Delta Sharing (OpenSharing) in Databricks.
sources:
  - create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T15:00:00.000Z"
updatedAt: "2026-06-19T15:00:00.000Z"
tags:
  - databricks
  - privileges
  - unity-catalog
  - delta-sharing
  - opensharing
aliases:
  - create-recipient-privilege
  - CRP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# CREATE RECIPIENT Privilege

The **CREATE RECIPIENT** privilege is a metastore-level permission in [Unity Catalog](/concepts/unity-catalog.md) that controls the ability to create recipient objects for [Delta Sharing](/concepts/delta-sharing.md) (OpenSharing). A recipient is a named object that represents the identity of a user or group of users who will consume shared data. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Required Permission

To create a recipient, you must have the `CREATE RECIPIENT` privilege on the Unity Catalog [Metastore](/concepts/metastore.md) where the data you want to share is registered. This privilege is required regardless of whether you are creating a Databricks-to-Databricks recipient or a Databricks-to-Open sharing recipient. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Scope

The privilege applies at the [Metastore](/concepts/metastore.md) level. Users or groups who are granted `CREATE RECIPIENT` can create recipient objects within that [Metastore](/concepts/metastore.md). [Metastore](/concepts/metastore.md) administrators implicitly have this privilege. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Additional Requirements

In addition to possessing the `CREATE RECIPIENT` privilege, you must: ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

- Use a Databricks workspace that has the Unity Catalog [Metastore](/concepts/metastore.md) attached.
- If using a Databricks notebook, the compute resource must run Databricks Runtime 11.3 LTS or above and use either standard or dedicated access mode (formerly shared and single user access modes).

## Creating a Recipient

You can create a recipient using [Catalog Explorer](/concepts/catalog-explorer.md), the Databricks Unity Catalog CLI, or the `CREATE RECIPIENT` SQL command in a notebook or the Databricks SQL query editor. The `CREATE RECIPIENT` privilege is checked at the time the recipient is created. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

### Recipient Types

- **Databricks-to-Databricks sharing** – For recipients with access to a Unity Catalog-enabled Databricks workspace. You create a recipient object with authentication type `DATABRICKS` using the recipient's [Sharing Identifier](/concepts/sharing-identifier.md) (format `<cloud>:<region>:<uuid>`). ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]
- **Databricks-to-Open sharing** – For recipients without access to a Unity Catalog-enabled Databricks workspace. You use token-based authentication (bearer tokens or [OIDC federation](/concepts/oidc-federation-policy.md)). The same `CREATE RECIPIENT` privilege is required. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Privileges

Other recipient operations (viewing, updating, deleting, granting share access, managing properties, or restricting access with IP lists) require different privileges. See [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) for details. ^[create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that manages metastore-level privileges.
- [Delta Sharing](/concepts/delta-sharing.md) – The data sharing protocol that uses recipient objects.
- [OpenSharing](/concepts/opensharing.md) – Databricks' implementation of Delta Sharing.
- [Data Recipient](/concepts/data-recipient.md) – The named object representing a consumer of shared data.
- [Sharing Identifier](/concepts/sharing-identifier.md) – The [Metastore](/concepts/metastore.md) identifier used for Databricks-to-Databricks sharing.
- CREATE SHARE Privilege – Privilege for creating shares.
- [Manage data recipients for OpenSharing](/concepts/data-recipient-opensharing.md) – Operations on existing recipients.

## Sources

- create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md

# Citations

1. [create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws.md](/references/create-data-recipients-for-opensharing-databricks-to-databricks-sharing-databricks-on-aws-a4778c5e.md)
