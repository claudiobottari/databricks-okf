---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 243ca3eb7114d5472f1ba19d76a87145aae0b3363a305e5a6db5443bbcd687ff
  pageDirectory: concepts
  sources:
    - manage-privileges-in-unity-catalog-databricks-on-aws.md
    - unity-catalog-privileges-reference-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - manage-privilege
    - Manage Privileges
    - Manage privileges
    - Manage entitlements
  citations:
    - file: unity-catalog-privileges-reference-databricks-on-aws.md
    - file: manage-privileges-in-unity-catalog-databricks-on-aws.md
title: MANAGE Privilege
description: A special privilege in Unity Catalog that allows users to manage (grant/revoke) privileges on an object without owning it, though currently MANAGE users cannot see all grants via INFORMATION_SCHEMA.
tags:
  - unity-catalog
  - privileges
  - security
  - governance
timestamp: "2026-06-19T19:27:22.855Z"
---

## MANAGE Privilege

**MANAGE** is a Unity Catalog privilege that grants a user the ability to administer a securable object—including managing its privileges, transferring ownership, and deleting the object—without requiring object ownership. It is intended for delegated administration scenarios where a user needs administrative control over specific objects but should not become the full owner.^[unity-catalog-privileges-reference-databricks-on-aws.md, manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Capabilities

A user granted the `MANAGE` privilege on an object can perform the following actions:

- Grant and revoke any privilege on the object to other principals.^[manage-privileges-in-unity-catalog-databricks-on-aws.md]
- Transfer ownership of the object to another user, service principal, or group (subject to the special restrictions described in Transfer Ownership).^[manage-privileges-in-unity-catalog-databricks-on-aws.md]
- Delete the object.^[unity-catalog-privileges-reference-databricks-on-aws.md]

Users with `MANAGE` are **not** automatically granted all functional privileges on the object—they do not, for example, automatically get `SELECT` on a table or `EXECUTE` on a function. They must either be granted those privileges explicitly or grant them to themselves using the `MANAGE` privilege.^[unity-catalog-privileges-reference-databricks-on-aws.md]

To exercise `MANAGE` on an object, the user must also have the appropriate usage privileges on the object itself and on all its parent objects. For instance, to exercise `MANAGE` on a schema, the user needs `USE SCHEMA` on that schema and `USE CATALOG` on the parent catalog.^[unity-catalog-privileges-reference-databricks-on-aws.md]

### Applicable Objects

`MANAGE` can be granted on the following securable objects and container objects:

- **Securable objects:** `CLEAN ROOM`, `CONNECTION`, `EXTERNAL LOCATION`, `EXTERNAL METADATA`, `FUNCTION` (including registered models), `MATERIALIZED VIEW`, `SERVICE CREDENTIAL`, `STORAGE CREDENTIAL`, `TABLE`, `VIEW`, `VOLUME`.^[unity-catalog-privileges-reference-databricks-on-aws.md]
- **Container objects:** `SCHEMA`, `CATALOG`.^[unity-catalog-privileges-reference-databricks-on-aws.md]

When `MANAGE` is granted on a container (e.g., a catalog or schema), it also explicitly grants `MANAGE` on all child objects contained within that container.^[unity-catalog-privileges-reference-databricks-on-aws.md]

### Comparison with Object Ownership

Object Ownership and `MANAGE` share several administrative capabilities, but they differ in important ways. The following table summarises the key differences:

| Capability / Attribute | Object Owner | User with `MANAGE` |
|---|---|---|
| Has all privileges on the object (e.g., `SELECT`, `MODIFY`) | Yes | No; must be granted separately (or self-granted) |
| Can grant privileges on the object | Yes | Yes |
| Can transfer ownership | Yes | Yes (with same restrictions as owners for views, functions, and models) |
| Can delete the object | Yes | Yes |
| Privilege inheritance to child objects | Automatically owns children | Explicit `MANAGE` grants are created on each child when granted on a container |

`MANAGE` is explicitly **excluded** from the `ALL PRIVILEGES` grant—`ALL PRIVILEGES` does not imply `MANAGE`.^[unity-catalog-privileges-reference-databricks-on-aws.md] Similarly, to prevent accidental data exfiltration, the `EXTERNAL USE LOCATION` and `EXTERNAL USE SCHEMA` privileges are not included in `ALL PRIVILEGES`; only a user with `MANAGE` on an external location can grant `EXTERNAL USE LOCATION`.^[unity-catalog-privileges-reference-databricks-on-aws.md]

### Who Can Grant `MANAGE`

The `MANAGE` privilege can be granted by any of the following principals:^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

- The owner of the object.
- The owner of the catalog or schema that contains the object.
- A user who already holds the `MANAGE` privilege on the object.
- A [Metastore](/concepts/metastore.md) admin.

### Viewing Grants with `MANAGE`

Users who hold the `MANAGE` privilege on an object can see all grants on that object using SQL commands (e.g., `SHOW GRANTS`) or Catalog Explorer. As of the current implementation, the `INFORMATION_SCHEMA` only shows the user’s own grants; this is expected to be corrected in a future release.^[manage-privileges-in-unity-catalog-databricks-on-aws.md]

### Related Concepts

- [Object Ownership in Unity Catalog](/concepts/object-ownership-in-unity-catalog.md)
- ALL PRIVILEGES Privilege
- Transfer Ownership
- Unity Catalog Privileges Reference
- [External Use Location](/concepts/external-location.md)
- External Use Schema

### Sources

- manage-privileges-in-unity-catalog-databricks-on-aws.md
- unity-catalog-privileges-reference-databricks-on-aws.md

# Citations

1. [unity-catalog-privileges-reference-databricks-on-aws.md](/references/unity-catalog-privileges-reference-databricks-on-aws-21b03803.md)
2. [manage-privileges-in-unity-catalog-databricks-on-aws.md](/references/manage-privileges-in-unity-catalog-databricks-on-aws-f0868c6d.md)
