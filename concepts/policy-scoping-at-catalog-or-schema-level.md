---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94d82b2c4e62e603973a14c553c6fbdd4bd1ed51c61177ba8f071411b22d8b42
  pageDirectory: concepts
  sources:
    - best-practices-for-abac-policies-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - policy-scoping-at-catalog-or-schema-level
    - Schema Level or Policy Scoping at Catalog
    - PSACOSL
    - Schema-Level Policies
    - abac-policy-scoping-at-catalog-and-schema-level
    - Schema Level and ABAC Policy Scoping at Catalog
    - APSACASL
    - abac-policy-scoping-catalog-vs-schema-vs-table
    - APS(VSVT
  citations:
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Policy Scoping at Catalog or Schema Level
description: Attaching ABAC policies at the highest applicable scope (catalog or schema) rather than at the table level
tags:
  - data-governance
  - abac
  - policy-design
  - unity-catalog
timestamp: "2026-06-19T22:13:06.090Z"
---

```markdown
# Policy Scoping at Catalog or Schema Level

**Policy Scoping at Catalog or Schema Level** is a recommended approach for defining [[ABAC (Attribute-Based Access Control)]] policies within [[Unity Catalog]] on Databricks. Instead of attaching policies directly to individual tables, administrators attach them at the catalog or schema level, allowing a single policy to govern all tables in that scope.

## Motivation

Attaching policies at the catalog or schema level reduces the number of access control rules and simplifies governance. Table-level policies are rare and should be the exception. Catalog-scoped policies evaluate against all tables in the catalog, and schema-scoped policies evaluate against all tables in the schema. When new tables are created, existing policies automatically apply as long as the table's tags match the policy's conditions. This eliminates the need to manually attach a policy to each new table. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## How It Works

ABAC policies use tags (key-value pairs) on data objects to determine which rules apply. A policy defined at the catalog level is evaluated at query time against every table in that catalog. The policy's conditions reference the tags present on the table. If a table has tags that satisfy the condition, the policy applies. Similarly, a schema-scoped policy applies to all tables within that schema. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Policies are dynamic: they evaluate based on the user's identity, group memberships, and the tags on the data object. Because the scope is broad, adding a new table with the correct tags automatically inherits the relevant policies without further configuration. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Best Practices

### Standardize attributes and naming

Establish a consistent tagging taxonomy before creating policies. Use a small, well-defined set of tag keys and allowed values. For example, use a single `sensitivity` tag with controlled values (`public`, `internal`, `confidential`, `restricted`) rather than multiple overlapping tags. Tagging is a security boundary in ABAC – if a user can change tags on an asset, they can change which policies apply. Restrict tag creation and modification to authorized data stewards or governance admins, and audit tag changes regularly using the audit log system table. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Define policies at the highest applicable scope

Attach policies at the catalog or schema level when possible. This ensures that all tables in the catalog or schema are governed by a consistent set of rules. Avoid creating separate policies for individual tables except in rare cases where a specific table requires unique treatment. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Avoid policy sprawl

ABAC is designed to reduce the number of access control rules, not increase them. Start with a small number of broad policies – for example, PII masking across a catalog or regional row filtering. Avoid creating a separate policy for every edge case. Large numbers of policies and complex conditions can slow authorization checks. Review policies periodically and consolidate overlapping ones. ^[best-practices-for-abac-policies-databricks-on-aws.md]

### Set fallback rules for unclassified data

Don't assume that all objects are correctly tagged. Use automation to enforce tagging standards and implement fallback mechanisms. For example, apply a default restrictive tag like `classification : unverified` to new objects until a data steward reviews them, and create a policy that restricts access to objects with that default tag. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [[Attribute-Based Access Control (ABAC)]]
- [[Unity Catalog]]
- Data Governance
- [[Row Filters and Column Masks]]
- [[Dynamic ABAC Policy Evaluation|Tag-based policy evaluation]]
- Dynamic policy evaluation

## Sources

- best-practices-for-abac-policies-databricks-on-aws.md
```

# Citations

1. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
