---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7531403371f8f3ae1fa0eb066d8c055ae900926c49374ae87abc9029f58f791d
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-requirements-and-permissions
    - Permissions and ABAC Policy Requirements
    - APRAP
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policy Requirements and Permissions
description: Prerequisite permissions (MANAGE, object ownership, EXECUTE on UDFs) and compute requirements (Databricks Runtime 16.4+ or serverless) for creating and managing ABAC policies.
tags:
  - data-governance
  - unity-catalog
  - abac
  - prerequisites
timestamp: "2026-06-19T14:34:22.076Z"
---

---
title: ABAC Policy Requirements and Permissions
summary: Permissions and prerequisites needed to create, edit, delete, and view ABAC row filter and column mask policies in Unity Catalog.
sources:
  - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:00:00.000Z"
updatedAt: "2026-06-19T14:00:00.000Z"
tags:
  - databricks
  - unity-catalog
  - abac
  - permissions
  - security
aliases:
  - abac-policy-requirements-and-permissions
  - APRP
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# ABAC Policy Requirements and Permissions

**ABAC Policy Requirements and Permissions** describes the necessary permissions, compute prerequisites, and supporting objects required to create, edit, delete, and view attribute‑based access control (ABAC) [row filter policy|row filter](/concepts/row-filter-policies.md) and [column mask policy|column mask](/concepts/column-mask-policies.md) policies in [Unity Catalog](/concepts/unity-catalog.md).

## Overview

All operations on ABAC policies — create, edit, delete, show (`SHOW POLICIES` / `SHOW EFFECTIVE POLICIES`), and describe (`DESCRIBE POLICY`) — demand specific permissions on the securable object (catalog, schema, or table) to which the policy is attached. Additional prerequisites apply when creating a new policy, including compute requirements, a suitable user‑defined function (UDF), and [Governed Tags](/concepts/governed-tags.md). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Permissions Required by Operation

### Create a Policy

To create a policy, you must have **`MANAGE`** on the securable object where the policy will be attached, **or** own that securable object. Additionally, you need **`EXECUTE`** on the [user‑defined function (UDF)](/concepts/abac-user-defined-functions-udfs.md) that implements the row‑filtering or column‑masking logic (if using an existing UDF). If you define the function inline in the `CREATE POLICY` statement, `EXECUTE` on the inline function is implicitly granted by the policy creation. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Edit a Policy

Editing an existing policy requires **`MANAGE`** on the securable object the policy is attached to, or ownership of that object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Delete a Policy

Deleting a policy also requires **`MANAGE`** on the securable object, or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Show Policies

Use `SHOW POLICIES` to list policies defined directly on a securable object, and `SHOW EFFECTIVE POLICIES` to also include policies inherited from parent scopes (e.g., catalog‑level policies affecting a table). Viewing effective policies for a table **does not** require permissions on the parent catalog or schema, allowing a table admin to see applicable rules without read access to sibling tables’ policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

The operation itself requires **`MANAGE`** or ownership on the target securable object. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Describe a Policy

`DESCRIBE POLICY` displays the details of a specific policy. It requires **`MANAGE`** on the target securable object, or ownership. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Additional Requirements for Creating a Policy

Beyond permissions, creating a policy has the following prerequisites: ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

- **Compute**: Databricks Runtime 16.4 or above, or [serverless compute](/concepts/serverless-gpu-compute.md). See the official compute requirements documentation.
- **Filtering/masking logic**: A UDF in Unity Catalog on which you have `EXECUTE`, or a SQL function defined inline in the `CREATE POLICY` SQL statement.
- **Tags**: [Governed Tags](/concepts/governed-tags.md) must be applied to the target objects (columns, tables, etc.) that the policy will reference.

## Summary Table

| Operation       | Required Permission(s)                                                                                     | Additional Prerequisites                        |
|-----------------|------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Create          | `MANAGE` on securable object (or ownership) + `EXECUTE` on UDF (if using existing UDF)                     | Runtime ≥ 16.4 / serverless; governed tags      |
| Edit            | `MANAGE` on securable object (or ownership)                                                                | None                                            |
| Delete          | `MANAGE` on securable object (or ownership)                                                                | None                                            |
| Show Policies   | `MANAGE` on securable object (or ownership); effective view does *not* require parent‑scope permissions    | None                                            |
| Describe Policy | `MANAGE` on securable object (or ownership)                                                                | None                                            |

## Audit Logging

Operations on governed tags and ABAC policies (e.g., `createPolicy`, `deletePolicy`, `getPolicy`, `listPolicies`) are recorded in the audit log system table under the `unityCatalog` service. For detailed query examples, see audit logs. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- ABAC core concepts
- [Row filter policy](/concepts/row-filter-policies.md)
- [Column mask policy](/concepts/column-mask-policies.md)
- GRANT policies for models (Beta)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog user‑defined functions](/concepts/abac-user-defined-functions-udfs.md)
- [Compute requirements for ABAC policies](/concepts/abac-compute-requirements.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
