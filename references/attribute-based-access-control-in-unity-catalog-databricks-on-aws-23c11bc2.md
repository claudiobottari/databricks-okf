---
title: Attribute-based access control in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/
ingestedAt: "2026-06-18T08:03:14.260Z"
---

Attribute-based access control (ABAC) is an access control model in Unity Catalog where access is determined by evaluating **attributes** associated with [securable objects](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects). These attributes, represented through [governed tags](https://docs.databricks.com/aws/en/admin/governed-tags/), are used in **policy** conditions to identify which data a policy should protect.

[Policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#policies) are attached at a level in the Unity Catalog hierarchy, such as a catalog, schema, or table, and are evaluated dynamically. When a securable object has the attributes targeted by a policy, that policy takes effect automatically, so a single policy can enforce consistent access rules across an entire catalog or schema.

ABAC supports row and column-level security through [row filter policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#policy-types) and [column mask policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/core-concepts#policy-types) on tables, materialized views, and streaming tables. ABAC also supports dynamic privilege grants through [GRANT policies](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/grant-policies) (Beta), currently scoped to `EXECUTE` on models.

The following topics help you get started with ABAC in Unity Catalog.
