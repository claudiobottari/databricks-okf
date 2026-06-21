---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d4afbed7f1ceb86ead4f59500ab43f8548114bec9ff1732dfad4de1516196bd
  pageDirectory: concepts
  sources:
    - read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-data-permission-model
    - SDPM
  citations:
    - file: read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md
title: Shared Data Permission Model
description: A hierarchical privilege model for OpenSharing catalogs where catalog owners can grant read-only privileges (SELECT, READ VOLUME, USE CATALOG) while write/update privileges cannot be granted on shared assets.
tags:
  - unity-catalog
  - access-control
  - data-sharing
timestamp: "2026-06-19T20:07:49.112Z"
---

# Shared Data Permission Model

The **Shared Data Permission Model** defines how access control works for data shared via [OpenSharing](/concepts/opensharing.md) on Databricks, specifically the [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md) protocol. In this model, data providers make tables, views, volumes, notebooks, and models available through shares, and recipients consume that data through catalogs created from those shares. The permission model is built on [Unity Catalog](/concepts/unity-catalog.md)’s privilege hierarchy but enforces read-only access and special rules for sharing operations.

## Requirements for the Recipient

To receive shared data under this model, the recipient must meet two conditions:

1. The recipient must have access to a Databricks workspace that is [enabled for Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/enable-workspaces).
2. The provider must use the **Databricks-to-Databricks** OpenSharing protocol (not the credential-file-based open sharing protocol). ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Key Roles and Privileges

### Provider-Side Privileges (Recipient Workspace)

A user in the recipient workspace must first discover the provider and the shares that have been shared with the workspace. To list and view details about all providers and provider shares, the user needs the `USE PROVIDER` privilege. Users without this privilege can only see providers and shares they own. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Catalog Creation and Mounting

To make shared data accessible, a user must create a catalog from a share or mount the share to an existing catalog. The following users are authorized to **create a catalog** from a share:

- A [Metastore](/concepts/metastore.md) admin
- A user with both `CREATE CATALOG` and `USE PROVIDER` privileges on the recipient [Metastore](/concepts/metastore.md)
- A user with `CREATE CATALOG` privilege and ownership of the provider object

Similarly, to **mount a share to an existing catalog**, the user must have `USE PROVIDER` (or own the provider object) and also either own the existing shared catalog or have both `MANAGE` and `USE CATALOG` privileges on that catalog. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Data Access Privileges

Once a catalog is created, data access follows the ordinary Unity Catalog privilege model, with the constraint that only **read operations** are permitted. The key privileges are:

- `SELECT` – required to read tables and views.
- `READ VOLUME` – required to read volumes.
- `USE CATALOG` – required to view and clone notebooks in the catalog.
- `EXECUTE` (plus `USE SCHEMA` and `USE CATALOG`) – required to load and use shared models for inference.

These privileges are inherited downward: granting `SELECT` on the catalog automatically grants `SELECT` on all schemas and tables in the catalog unless explicitly revoked. The same inheritance applies to `READ VOLUME` for volumes. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

### Ownership and Delegation

By default, the catalog creator becomes the owner of all data objects under the OpenSharing catalog and can manage permissions for those objects. The catalog owner can **delegate ownership** of individual objects to other users or groups, granting them the ability to manage permissions and lifecycles. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Read-Only Constraint

The model is strictly read-only for recipients. You cannot grant privileges that provide write or update access to an OpenSharing catalog or any objects inside it. Recipients can perform:

- `DESCRIBE`, `SHOW`, and `SELECT` for tables
- `DESCRIBE VOLUME`, `LIST <volume-path>`, `SELECT * FROM <format>.'<volume_path>'`, and `COPY INTO` for volumes
- Transactions if the provider shared the table with history (subject to limitations)
- Stream reads if history is enabled
- Preview and clone notebooks
- Load models for batch inference

Write operations are never allowed. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Attribute-Based Access Control (ABAC)

Recipients can create [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies on shared tables, schemas, and catalogs created from a share. Specifically, they can apply:

- Row filters
- Column mask policies

These policies are supported for regular tables and foreign tables, with the following **limitations**:

- ABAC policies **cannot** be applied to shared streaming tables or materialized views.
- Column masks cannot be applied to streaming tables or materialized views. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Unmounting a Share

To remove a shared catalog’s connection to the share (unmount), the user must have both `USE CATALOG` and `MANAGE` privileges on the shared catalog. ^[read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md]

## Summary of Permission Model

| Action | Required Privilege(s) |
|--------|------------------------|
| List providers and shares | `USE PROVIDER` |
| Create catalog from share | [Metastore](/concepts/metastore.md) admin, or `CREATE CATALOG` + `USE PROVIDER`, or `CREATE CATALOG` + provider ownership |
| Mount share to existing catalog | `USE PROVIDER` (or provider ownership) + `MANAGE` and `USE CATALOG` on the existing catalog |
| Read table data | `SELECT` (inherited from catalog if not revoked) |
| Read volume data | `READ VOLUME` (inherited) |
| View/clone notebooks | `USE CATALOG` |
| Load shared model for inference | `EXECUTE` on model + `USE SCHEMA` + `USE CATALOG` |
| Manage permissions on objects | Ownership (creator is default owner; can be delegated) |
| Unmount share | `USE CATALOG` + `MANAGE` on the shared catalog |

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md)
- [OpenSharing](/concepts/opensharing.md)
- [Databricks-to-Databricks OpenSharing](/concepts/databricks-to-databricks-sharing.md)
- [Privilege Inheritance](/concepts/privilege-inheritance-hierarchy.md)
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- Catalogs in Unity Catalog
- Read-Only Data Sharing

## Sources

- read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md

# Citations

1. [read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws.md](/references/read-data-shared-using-databricks-to-databricks-opensharing-for-recipients-databricks-on-aws-21150d4f.md)
