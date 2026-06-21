---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6bd2bf0cda98018b7f8ad2c9eb86930aeec0e0c9c6e28101d445af5acf5cb6b5
  pageDirectory: concepts
  sources:
    - core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - separation-of-duties-for-abac
    - SODFA
  citations:
    - file: core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md
title: Separation of Duties for ABAC
description: "The organizational model distributing ABAC responsibilities across specialized roles: tag taxonomy creators, data stewards (tagging), governance admins (policy creation), data creators, and data consumers."
tags:
  - governance
  - roles
  - unity-catalog
timestamp: "2026-06-19T14:27:49.105Z"
---

## Separation of Duties for ABAC

**Separation of duties for ABAC** refers to the practice of distributing the responsibilities required to set up [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) across different teams or roles. By dividing tasks — such as tag taxonomy creation, data classification, policy writing, object creation, and data access — organizations can enforce least privilege and reduce the risk that a single user can both classify data and set access rules. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

The following steps describe the recommended separation when implementing ABAC with [Unity Catalog](/concepts/unity-catalog.md). Each step lists the required permissions and the typical role that performs it.

### 1. Create the tag taxonomy

Define the governed tag keys and their allowed values before anyone applies tags or writes policies. For example, create a `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) or a `pii` tag with values like `ssn`, `email`, and `phone_number`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Required permissions:* Account admin, or a user with `CREATE` permission for tags at the account level.

*Typical role:* Central governance or security team.

### 2. Tag data assets

A data steward, data creator, or AI classification system applies governed tags to Unity Catalog securable objects (catalogs, schemas, tables, columns, models, volumes). For example, tag columns that contain personally identifiable information with `pii : ssn`, or tag a model with `lifecycle : production`. Correct tagging is the essential first step for ABAC policies to apply. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Required permissions:* `ASSIGN` on the tag, and `APPLY TAG` on the object.

*Typical role:* Data steward or data creator.

> **Warning:** Tagging is a security boundary. If a user can change tags on a data asset, they can change which policies apply to it. Organizations should control who can apply tags and audit tag changes. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

### 3. Create a policy

A governance admin creates a policy at a scope, such as a catalog or schema. The policy specifies who it applies to, what conditions it evaluates, and the action to apply (row filter, column mask, or privilege grant). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Required permissions:* `MANAGE` permission or object ownership on the securable object where the policy is attached. For row filter and column mask policies, also `EXECUTE` privilege on the UDF.

*Typical role:* Governance admin.

### 4. Create data objects

Data creators create securable objects (tables, models, volumes) within the scopes to which they were granted access. New objects inherit tags from parent catalogs and schemas. Data creators also have `APPLY TAG` automatically on objects they create, so they can apply additional tags or rely on automatic data classification. Data creators do not need to configure access controls if policies are set at higher levels (recommended). ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Required permissions:* `CREATE TABLE` or other relevant creation privileges on the parent object.

*Typical role:* Data engineer or data creator.

### 5. Access governed objects

When a user attempts to access a securable object within a policy’s scope, Unity Catalog evaluates applicable policies automatically. For [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md), the user sees filtered or masked data if the table or columns match the policy’s conditions and the user is not exempt. For [GRANT policies](/concepts/grant-policies-beta.md) (Beta), the user gains the granted privilege if the conditions match and the user is in `TO` and not in `EXCEPT`. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Required permissions:* For row filter and column mask policies, users must be granted permissions on the table (e.g., `SELECT`) through a direct object grant. These policies filter records or mask columns for tables the user can already access — they do not grant permissions on their own. GRANT policies grant the privilege themselves and union with any direct grants on the same securable. ^[core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md]

*Typical role:* Data consumer.

### Benefits of this separation

Distributing ABAC setup across specialized groups delivers several advantages:

- **Reduced risk of privilege escalation:** No single user can both tag data and write policies that affect that data.
- **Clear accountability:** Each team owns a well-defined step (taxonomy, tagging, policy creation, data creation, data consumption).
- **Auditability:** Permissions and actions are scoped to specific roles, making it easier to review who changed what.
- **Scalability:** Policies can be created by a central governance team while data creators continue to tag and create objects independently within governed boundaries.

These principles align with Unity Catalog best practices for enterprise governance.

## Related Concepts

- [Governed Tags](/concepts/governed-tags.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [GRANT policies](/concepts/grant-policies-beta.md)
- [UDFs in Unity Catalog](/concepts/python-udfs-in-unity-catalog.md)
- Unity Catalog permissions and privileges
- Best practices for ABAC policies

## Sources

- core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md

# Citations

1. [core-concepts-for-attribute-based-access-control-abac-databricks-on-aws.md](/references/core-concepts-for-attribute-based-access-control-abac-databricks-on-aws-ca4d8af7.md)
