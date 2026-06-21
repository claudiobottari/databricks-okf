---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e1e1c6019d4f3374e6d8a633e608b21de83e86ca1ebdbfd129427bd366745cca
  pageDirectory: concepts
  sources:
    - create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-requirements
    - APR
    - abac-policy-requirements-and-prerequisites
    - Prerequisites and ABAC Policy Requirements
    - APRAP
    - abac-policy-requirements-and-permissions
    - Permissions and ABAC Policy Requirements
  citations:
    - file: create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md
title: ABAC Policy Requirements
description: Prerequisites for creating and managing ABAC policies including MANAGE permission on the securable object, EXECUTE on the UDF, Databricks Runtime 16.4+ or serverless compute, and governed tags on target objects.
tags:
  - data-governance
  - unity-catalog
  - abac
  - requirements
timestamp: "2026-06-18T14:52:07.273Z"
---

# ABAC Policy Requirements

**ABAC Policy Requirements** defines the prerequisites and permissions needed to create, edit, or manage [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) row filter and column mask policies in Unity Catalog. These requirements ensure that policies can be applied consistently and securely across catalogs, schemas, and tables.

## Compute Requirements

ABAC policies require one of the following compute environments:

- **Databricks Runtime 16.4 or above**
- **Serverless compute**

Policies cannot be created or enforced on older runtimes. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Permissions

### Creating or editing a policy

To create or edit an ABAC policy, a user or service principal must meet both of the following:

- **`MANAGE` permission or ownership** on the securable object (catalog, schema, or table) where the policy will be attached.
- **`EXECUTE` privilege** on the user-defined function (UDF) that implements the row filter or column mask logic. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

### Deleting, showing, or describing a policy

All policy operations — creation, editing, deletion, listing (`SHOW POLICIES`), and description (`DESCRIBE POLICY`) — require `MANAGE` on the target securable object or ownership of that object. The `SHOW EFFECTIVE POLICIES` command does not require permissions on the parent catalog or schema, allowing a table admin to see applicable rules without access to sibling tables' policies. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## User-Defined Function (UDF) Requirements

The filtering or masking logic must be provided by one of the following:

- A **user-defined function (UDF) registered in Unity Catalog** on which the policy creator has `EXECUTE`.
- A **SQL function defined inline** when creating the policy (no separate UDF required). ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

For row filter policies, the UDF evaluates each row and returns a boolean — rows where the function returns `FALSE` are excluded from query results. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]  

For column mask policies, the UDF returns either the original value or a masked value. The return type must be castable to the target column’s data type. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Tag Requirements

ABAC policies rely on [Governed Tags](/concepts/governed-tags.md) applied to tables and columns. Tags must be present on the objects that the policy conditions reference. Specifically:

- **Row filter policies** use tags on tables or columns in their `MATCH COLUMNS` or `WHEN` clauses.
- **Column mask policies** use tags on columns to identify which columns should be masked.

Tags must be applied before the policy is created; policies cannot reference tags that do not exist. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Additional Considerations

- Policies can be attached at the **catalog, schema, or table** scope. When attached at a higher scope (catalog or schema), they automatically apply to all tables within that scope that match the policy's conditions. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]
- The policy **name** and the **securable object where the policy is applied** cannot be edited after creation. Other properties (description, principals, policy type, conditions, function input mappings) can be modified. ^[create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC Row Filter Policies](/concepts/abac-row-filter-policy.md)
- [ABAC Column Mask Policies](/concepts/abac-column-mask-policy.md)
- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Governed Tags](/concepts/governed-tags.md)
- Core Concepts for ABAC
- Policy Evaluation Order
- [Unity Catalog User-Defined Functions](/concepts/abac-user-defined-functions-udfs.md)

## Sources

- create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md

# Citations

1. [create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws.md](/references/create-and-manage-row-filter-and-column-mask-policies-databricks-on-aws-d315307d.md)
