---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 32bd6837e6b8b9e72dc89f1297c7985ecdfbfa2bea019bb600c9ce25b0aea201
  pageDirectory: concepts
  sources:
    - manage-data-recipients-for-opensharing-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - opensharing-recipient-object
    - ORO
    - recipient object
  citations:
    - file: manage-data-recipients-for-opensharing-databricks-on-aws.md
title: OpenSharing Recipient Object
description: "A named object in Databricks Unity Catalog that represents the identity of a user or group with whom data is shared via Delta Sharing/OpenSharing. It supports multiple authentication types: DATABRICKS (Databricks-to-Databricks), TOKEN (bearer token for non-Databricks users), OAUTH_CLIENT_CREDENTIALS, and OIDC_FEDERATION."
tags:
  - delta-sharing
  - opensharing
  - databricks
  - identity-management
timestamp: "2026-06-19T19:23:43.293Z"
---

---

title: OpenSharing Recipient Object
summary: A Unity Catalog object that represents the identity of a user or group with whom data is shared via the OpenSharing protocol.
sources:
  - manage-data-recipients-for-opensharing-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T15:36:28.238Z"
updatedAt: "2026-06-18T15:36:28.238Z"
tags:
  - delta-sharing
  - recipient-management
  - unity-catalog
aliases:
  - opensharing-recipient-object
  - ORO
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0

---

# OpenSharing Recipient Object

An **OpenSharing Recipient Object** is a named entity in [Unity Catalog](/concepts/unity-catalog.md) that represents the identity of a user or group with whom you share data via the [OpenSharing](/concepts/opensharing.md) (Delta Sharing) protocol. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Authentication Types

Recipient objects support several authentication methods for confirming the identity of the data consumer: `DATABRICKS` for [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md), `TOKEN` for bearer-token-based [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md), `OAUTH_CLIENT_CREDENTIALS`, and `OIDC_FEDERATION` for OIDC Federation|OpenID Connect federation-based access. The authentication type is set when the recipient is created and affects how the recipient obtains credentials and accesses shares. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Viewing Recipients

To list all recipients in the [Metastore](/concepts/metastore.md), providers can use Catalog Explorer, the Databricks Unity Catalog CLI, or the `SHOW RECIPIENTS` SQL command. Users must have the `USE RECIPIENT` privilege to see all recipients; otherwise, they see only recipients they own. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

Recipient details (available via Catalog Explorer, `DESCRIBE RECIPIENT`, or the CLI) include the creator, creation timestamp, comment, and authentication type. Depending on the authentication method, details also include token lifetime and activation link (for bearer-token recipients), recipient endpoint and federation policies (for OIDC recipients), or cloud, region, and [Metastore](/concepts/metastore.md) ID (for Databricks-to-Databricks recipients). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

To view the list of shares granted to a particular recipient, providers can use Catalog Explorer, the CLI, or the `SHOW GRANTS TO RECIPIENT` SQL command. [Metastore](/concepts/metastore.md) admins, users with `USE RECIPIENT`, and recipient owners can perform these queries. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Granting Access to Shares

After a recipient object exists and shares have been created, providers grant access to shares via Catalog Explorer, the Unity Catalog CLI, or the `GRANT ON SHARE` SQL command. Required permissions include [Metastore](/concepts/metastore.md) admin privileges or delegated permissions (`USE SHARE` + `SET SHARE PERMISSION` or share ownership) combined with (`USE RECIPIENT` or recipient ownership). ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Updating a Recipient

Providers can update recipient properties such as name, owner, comment, and custom properties using Catalog Explorer, `ALTER RECIPIENT`, or the CLI. Only [Metastore](/concepts/metastore.md) admins or the recipient owner can change the owner; renaming requires `CREATE RECIPIENT` privilege *and* ownership; updating the comment or custom properties requires ownership. Token-authenticated recipients allow token rotation, and OIDC recipients allow adding federation policies. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Recipient Properties

Recipient objects include predefined properties (starting with `databricks.`) that refine data-sharing access. These are `databricks.accountId` and `databricks.metastoreId` (for Databricks-to-Databricks sharing) and `databricks.name` (the recipient name). Providers can also add custom properties—for example, a `country` property—to support partition filtering or dynamic views that restrict row or column access based on the property value. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

Requirements for managing properties include a SQL warehouse or compute running Databricks Runtime 12.2 or above. Properties can be added during creation or updated later by [Metastore](/concepts/metastore.md) admins or users with the `CREATE RECIPIENT` privilege. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Deleting a Recipient

To delete a recipient, the owner uses Catalog Explorer, `DROP RECIPIENT`, or the CLI. Deletion is irreversible: the represented users can no longer access shared data, and any bearer tokens used in a Databricks-to-Open sharing scenario are invalidated. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## IP Access Lists (Optional)

For Databricks-to-Open sharing recipients, providers can optionally restrict recipient access to a defined set of IP addresses using IP access lists. ^[manage-data-recipients-for-opensharing-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [OpenSharing](/concepts/opensharing.md)
- [Databricks-to-Databricks Sharing](/concepts/databricks-to-databricks-sharing.md)
- [Databricks-to-Open Sharing](/concepts/databricks-to-open-sharing.md)
- Bearer Token Recipient
- OIDC Federation
- [Share (Delta Sharing)](/concepts/delta-sharing.md)

## Sources

- manage-data-recipients-for-opensharing-databricks-on-aws.md

# Citations

1. [manage-data-recipients-for-opensharing-databricks-on-aws.md](/references/manage-data-recipients-for-opensharing-databricks-on-aws-073afd50.md)
