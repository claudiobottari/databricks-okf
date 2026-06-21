---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 161f9dbb85eb28c9f75fbb7c1e424fef524d44b509bb57b1e9ad0bdc7ce07d7f
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - unity-catalog-privilege-management
    - UCPM
    - Unity Catalog Privileges
    - Unity Catalog privileges
  citations:
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: Unity Catalog Privilege Management
description: The overall system for granting, revoking, and inspecting permissions on Unity Catalog securable objects (catalogs, schemas, tables, views, volumes, etc.) using SQL commands, Catalog Explorer, CLI, or Terraform.
tags:
  - unity-catalog
  - privileges
  - security
  - access-control
timestamp: "2026-06-19T19:27:58.247Z"
---

# Unity Catalog Privilege Management

**Unity Catalog Privilege Management** refers to the system of granting, revoking, inspecting, and controlling permissions on securable objects within [Unity Catalog](/concepts/unity-catalog.md) on Databricks. It encompasses the privileges model, object ownership, and the various methods available for administering access control across the [Metastore](/concepts/metastore.md) hierarchy.

## Overview

Privileges in Unity Catalog control which users, service principals, and groups can access or manipulate data assets. The system follows a hierarchical model where privileges can be inherited from parent objects (catalogs, schemas) to child objects (tables, views, volumes, functions, models). Initially, users have no access to data in a [Metastore](/concepts/metastore.md) until privileges are explicitly granted. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Who Can Manage Privileges

Privileges can be granted by any of the following principals:

- The **owner** of the object.
- The **owner of the catalog or schema** that contains the object.
- A user with the `MANAGE` privilege on the object.
- A **metastore admin**.
- **Account admins** can grant privileges directly on a [Metastore](/concepts/metastore.md).

Databricks account admins, workspace admins, and [Metastore](/concepts/metastore.md) admins have default privileges for managing Unity Catalog. Object owners have all privileges on their objects, including the ability to grant privileges to other principals. Owners can also grant the `MANAGE` privilege to other users, allowing them to manage privileges on the object. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Workspace Catalog Privileges

If a workspace was enabled for Unity Catalog automatically, it is attached to a [Metastore](/concepts/metastore.md) by default and a workspace catalog is created. Workspace admins are the default owners of the workspace catalog and can manage privileges on it and all child objects. All workspace users automatically receive the `USE CATALOG` privilege on the workspace catalog, along with `USE SCHEMA`, `CREATE TABLE`, `CREATE VOLUME`, `CREATE MODEL`, `CREATE FUNCTION`, and `CREATE MATERIALIZED VIEW` privileges on the `default` schema within that catalog. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Granting, Revoking, and Showing Privileges

Privileges can be managed using SQL Commands, the Databricks CLI, the Databricks Terraform provider, or [Catalog Explorer](/concepts/catalog-explorer.md). The core operations are:

### Showing Grants on an Object

Users with the `MANAGE` privilege, the object owner, the owner of the containing catalog or schema, or [Metastore](/concepts/metastore.md) admins can see all grants on an object. Other users can view only their own grants on the object. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Granting Permissions

To grant permissions, a user must be a [Metastore](/concepts/metastore.md) admin, have the `MANAGE` privilege, be the object owner, or be the owner of the containing catalog or schema. In Catalog Explorer, users can navigate to the object's **Permissions** tab, click **Grant**, enter the user or group email, select the privileges, and confirm. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Revoking Permissions

The same principals who can grant can also revoke. In Catalog Explorer, select the privilege granted to a user, service principal, or group, click **Revoke**, and confirm. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Metastore-Level Privileges

Only [Metastore](/concepts/metastore.md) admins or account admins can show, grant, or revoke privileges directly on a [Metastore](/concepts/metastore.md). ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Manage Object Ownership

Every securable object in Unity Catalog has an **owner**. Object owners have all privileges on the object and can grant privileges to others.

### Viewing an Object's Owner

Any user with the `BROWSE` privilege on the object or a parent of the object can view the object owner. In Catalog Explorer, owners are displayed on the **Overview** tab for most objects, or at the top of the details page for some objects like external locations. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Transferring Ownership

Ownership can be transferred if the user is:
- The current owner.
- A [Metastore](/concepts/metastore.md) admin.
- The owner of the container (catalog for a schema, schema for a table).
- A user with the `MANAGE` privilege on the object.

**Important restriction for views, functions, and models:** To prevent privilege escalations, only a [Metastore](/concepts/metastore.md) admin can transfer ownership of a view, function, or model to any user, service principal, or group in the account. Current owners and `MANAGE` privilege holders are restricted to transferring ownership to their own username or to a group they belong to. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

**OpenSharing shares** are an exception: only a [Metastore](/concepts/metastore.md) admin can transfer share ownership. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

**Materialized views and streaming tables** created with Databricks SQL can have ownership transferred. However, those created with Lakeflow Spark Declarative Pipelines cannot have ownership directly transferred—instead, change the run-as user of the pipeline, and the owner updates on the next refresh. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Collaborative Editing with Group Ownership

Transferring ownership of a view or metric view to a group enables collaborative editing. When a group owns a view or metric view, all group members can edit its definition while data access remains limited to what the group has permission to see. ^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog Permissions Model Concepts](/concepts/unity-catalog-permissions-model.md) — Conceptual background on inheritance and privilege types.
- Admin Privileges in Unity Catalog — Default privileges for admin roles.
- [Securable objects in Unity Catalog](/concepts/securable-objects-in-unity-catalog.md) — The hierarchy of catalogs, schemas, tables, views, volumes, and other objects.
- Privilege Types — The full list of privilege types (SELECT, CREATE, MODIFY, etc.).
- SQL REF Privileges — SQL reference for privilege syntax.
- [Catalog Explorer](/concepts/catalog-explorer.md) — UI tool for managing permissions.
- [Metastore](/concepts/metastore.md) — The top-level container for Unity Catalog metadata.
- [External location](/concepts/external-location.md) — Securable object for accessing cloud storage.

## Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md

# Citations

1. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
