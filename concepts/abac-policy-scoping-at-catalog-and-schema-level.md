---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 043e6aaeb6ac67642e678c530ea6ae1f959dc160dbc03a2eb22c9420617e99e9
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - abac-policy-scoping-at-catalog-and-schema-level
    - Schema Level and ABAC Policy Scoping at Catalog
    - APSACASL
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: ABAC Policy Scoping at Catalog and Schema Level
description: Attaching ABAC policies at the highest applicable scope (catalog or schema) rather than table level for simpler management.
tags:
  - attribute-based-access-control
  - policy-design
timestamp: "2026-06-19T17:40:33.925Z"
---

# ABAC Policy Scoping at [Catalog and Schema](/concepts/catalog-and-schema.md) Level

**ABAC policy scoping at [Catalog and Schema](/concepts/catalog-and-schema.md) level** is a best practice for defining [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies in [Unity Catalog](/concepts/unity-catalog.md) on Databricks. Policies attached at the catalog or schema scope evaluate against all tables within that scope, reducing the number of individual access control rules needed while maintaining fine-grained authorization through tags.

## Overview

ABAC policies use tags (key-value attributes) on data objects and users to determine access at query time. When you attach a policy at the catalog or schema level, it applies to every table in that catalog or schema. This design supports dynamic evaluation: as new tables are added or existing tables are tagged, the same policy automatically governs them without requiring additional rule creation.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Catalog-Level Policies

A catalog-scoped ABAC policy evaluates all tables in the catalog against the conditions defined in the policy. For example, a policy that masks columns tagged with `sensitivity: confidential` would apply to any table in the catalog that has that tag, regardless of the table’s schema.^[best-practices-for-abac-policies-databricks-on-aws.md]

This scope is ideal for broad governance rules that should span an entire domain, such as applying row filtering based on [Regional Tags](/concepts/regional-tags.md) across all tables in a sales catalog.

## Schema-Level Policies

Schema-scoped policies evaluate only within a single schema. They are useful when different schemas within the same catalog require distinct access rules. For instance, a schema containing personally identifiable information (PII) might have a stricter masking policy than a schema holding aggregated reports.^[best-practices-for-abac-policies-databricks-on-aws.md]

When new tables are added to the schema, existing policies automatically apply as long as the table’s tags match the policy’s conditions.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Why Prefer Higher Scopes

Databricks recommends attaching policies at the catalog or schema level whenever possible. Table-level policies are rare and should be the exception. Catalog- and schema-level policies scale naturally: you define the rule once, and it governs all current and future objects in that scope. This reduces administrative overhead, simplifies auditing, and prevents policy sprawl.^[best-practices-for-abac-policies-databricks-on-aws.md]

Higher‑scope policies also make it easier to enforce consistent governance standards across an entire data domain, because every table in the catalog or schema is covered unless explicitly excluded.

## Best Practices for Scoping

- **Standardize tags first.** Before attaching policies, establish a consistent tagging taxonomy (e.g., a `sensitivity` tag with controlled values). Policies are only effective when the tags they reference are correctly and reliably applied.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Set fallback rules for unclassified data.** Use a default restrictive tag (e.g., `classification: unverified`) and a policy that blocks or restricts access to objects with that tag until a data steward reviews them.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Audit direct grants and ABAC GRANT policies together.** A user’s effective privileges are the union of direct grants and ABAC GRANT policies (Beta). Checking only one surface may miss unintended permissions.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Prefer `TO`/`EXCEPT` for principal targeting.** In row filter and column mask policies, use the policy’s `TO` and `EXCEPT` clauses to define which users the policy applies to, rather than embedding complex conditional logic in the UDF.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Plan for dynamic evaluation.** Because ABAC policies are evaluated at query time based on the user’s identity and current tags, data consumers may not immediately see which rules apply. Use `SHOW EFFECTIVE POLICIES` to inspect what applies to a specific table, and document the tagging taxonomy so teams understand the governance model.^[best-practices-for-abac-policies-databricks-on-aws.md]
- **Avoid policy sprawl.** Start with a small number of broad policies (e.g., PII masking across a catalog, regional row filtering). Creating separate policies for every edge case leads to a system that is hard to manage and audit, and can slow performance.^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The foundational access control model.
- [Row Filters](/concepts/row-filter-policies.md) and Column Masks – Mechanisms used inside ABAC policies to restrict or transform data.
- [ABAC GRANT Policies (Beta)](/concepts/abac-grant-policies.md) – Policies that grant privileges based on tags, complementing direct grants.
- Tag Governance – Best practices for managing tags to ensure ABAC policies work correctly.
- Performance Considerations – How large numbers of policies and complex conditions affect authorization speed.
- [Unity Catalog](/concepts/unity-catalog.md) – The data governance platform that hosts ABAC policies.

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
