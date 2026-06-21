---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c55e09e38905e825dd1f74603c1c6736b9d6e240852b214f7ffdbb79efa10ef
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - object-ownership-in-unity-catalog
    - OOIUC
    - Ownership in Unity Catalog
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: Object Ownership in Unity Catalog
description: Every securable object has an owner who possesses all privileges on that object and can grant privileges to others. Ownership can be transferred by the current owner, a metastore admin, or a user with MANAGE privilege.
tags:
  - unity-catalog
  - ownership
  - security
timestamp: "2026-06-19T19:27:04.642Z"
---

# Object Ownership in Unity Catalog

**Object Ownership** is a core concept in [Unity Catalog](/concepts/unity-catalog.md)'s permission model. Every securable object in Unity Catalog—such as catalogs, schemas, tables, views, volumes, external locations, models, and functions—has exactly one owner. The owner has all privileges on that object, including the ability to grant or revoke privileges to other principals. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Owner Privileges

Object owners have full control over their securable objects. This includes the implicit grant of every privilege on the object, as well as the ability to delegate privilege management by granting the `MANAGE` privilege to other users. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

Privileges on an object can be granted by:
- The owner of the object.
- The owner of the catalog or schema that contains the object.
- A user with the `MANAGE` privilege on the object.
- A [Metastore Admin](/concepts/metastore-admin-role.md).

Account admins can also grant privileges directly on a [Metastore](/concepts/metastore.md). ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Workspace Catalog Ownership

When a workspace is automatically enabled for Unity Catalog, a workspace catalog is created in the [Metastore](/concepts/metastore.md). [Workspace Admin|Workspace admins](/concepts/restrictworkspaceadmins-setting.md) are the default owners of the workspace catalog and can manage privileges on the catalog and all its child objects. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Viewing an Object's Owner

Any user with the `BROWSE` privilege on an object (or a parent of the object) can view the object's owner. In **Catalog Explorer**, the owner is displayed on the **Overview** tab for most objects; for some objects such as external locations, the owner appears at the top of the details page. The owner can also be viewed using SQL statements. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Transferring Ownership

Ownership can be transferred to another user, service principal, or group. The following principals are authorized to transfer ownership:
- The current owner of the object.
- A [Metastore](/concepts/metastore.md) admin.
- The owner of the container object (the catalog owner for a schema, or the schema owner for a table).
- A user with the `MANAGE` privilege on the object.

**OpenSharing share objects** are an exception: only a [Metastore](/concepts/metastore.md) admin can transfer share ownership. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Transfer Restrictions for Views, Functions, and Models

To prevent privilege escalations, only a [Metastore](/concepts/metastore.md) admin can transfer ownership of a view, function, or model to any user, service principal, or group in the account. Current owners and users with the `MANAGE` privilege are restricted to transferring ownership only to their own username or to a group they belong to. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Collaborative Editing with Group Ownership

Transferring ownership of a view or metric view to a group enables collaborative editing. When a group owns a view or metric view, all group members can edit its definition while data access remains limited to what the group has permission to see. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Special Cases: Materialized Views and Streaming Tables

- **Databricks SQL materialized views and streaming tables** can have ownership transferred directly. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]
- **Lakeflow Spark Declarative Pipeline materialized views and streaming tables** cannot have ownership directly transferred. Instead, change the run-as user of the pipeline that owns the datasets; the owner updates to the run-as user with the next refresh. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Transferring Ownership via Catalog Explorer

1. In your Databricks workspace, open **Catalog** and select the object.
2. Click the edit icon next to the **Owner** field.
3. Search for and select a group, user, or service principal.
4. Click **Save**. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Permission Model](/concepts/unity-catalog-permissions-model.md)
- Privilege Types in Unity Catalog
- [Metastore Admin](/concepts/metastore-admin-role.md)
- [Catalog Explorer](/concepts/catalog-explorer.md)
- Manage Privileges in Unity Catalog
- [Unity Catalog Securable Objects](/concepts/unity-catalog-securable-objects.md)

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
