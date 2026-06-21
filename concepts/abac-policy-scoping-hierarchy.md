---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a52a8a290667c79065afc7cfcfec66573d880a70ffdf46722a548a00a31b725d
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-scoping-hierarchy
    - APSH
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Policy Scoping Hierarchy
description: Principle of attaching ABAC policies at the highest applicable scope (catalog or schema level) rather than table level to maximize reusability
tags:
  - abac
  - policy-design
  - unity-catalog
  - access-control
timestamp: "2026-06-19T14:09:04.036Z"
---

# ABAC Policy Scoping Hierarchy

The **ABAC Policy Scoping Hierarchy** defines the levels at which an attribute-based access control (ABAC) policy can be attached within [Unity Catalog]: **catalog**, **schema**, and **table**. Higher scopes (catalog, schema) apply broadly, while lower scopes (table) apply to a single object. Understanding this hierarchy is essential for designing efficient, maintainable governance policies.

## Policy Scopes

ABAC policies can be created at three scopes:

| Scope | Evaluation Scope | Use case |
|-------|------------------|----------|
| **Catalog** | All tables in the catalog | Broad policies such as masking PII across an entire catalog or regional row filtering. |
| **Schema** | All tables in the schema | Department‑ or domain‑level policies that apply to a set of related tables. |
| **Table** | A single table | Exception‑only; rarely needed because higher‑scope policies already cover most tables. |

Catalog‑scoped policies evaluate against all tables in the catalog, and schema‑scoped policies evaluate against all tables in the schema. When new tables are added to a catalog or schema, existing policies automatically apply to them as long as the tables’ tags match the policy’s conditions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practice: Attach at the Highest Applicable Scope

ABAC is designed to **reduce** the number of access control rules. The recommended practice is to attach policies at the catalog or schema level whenever possible. Table‑level policies should be the exception, used only when a specific table requires a rule that cannot be expressed at a higher scope. ^[best-practices-for-abac-policies-databricks-on-aws.md]

This approach prevents **policy sprawl** — a situation where too many tags and policies make the system hard to manage and audit. Instead of creating separate policies for every edge case, start with a small number of broad policies (e.g., PII masking across a catalog, regional row filtering at the schema level) and consolidate overlapping ones. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Dynamic Evaluation at Query Time

ABAC policies evaluate dynamically based on the user’s identity, group memberships, and the tags on the data object at the time of query. Unlike static row filters or column masks that are visible directly on a table definition, ABAC policies are applied transparently. To understand which policies apply to a particular table, use the [`SHOW EFFECTIVE POLICIES`](https://docs.databricks.com/aws/en/sql/language-manual/sql-ref-syntax-aux-show-policies) command. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Relationship to Direct Grants

A user’s effective privileges on a data object are the union of direct grants and ABAC GRANT policies (where supported). When auditing access, both surfaces must be checked — auditing only direct grants or only ABAC policies can hide unintended permissions. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC](/concepts/abac-attribute-based-access-control.md) — The attribute‑based access control paradigm
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that hosts ABAC policies
- [Row Filters and Column Masks](/concepts/row-filters-and-column-masks.md) — Alternative table‑level access controls
- Tag Governance — Best practices for standardizing tags used in ABAC conditions
- [ABAC GRANT Policies](/concepts/abac-grant-policies.md) — Beta feature that grants privileges based on attributes

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
