---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0df400ff71a2b271bff4f5dfe546c4704ef2969eebd5b16b53978df4695d6c55
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - tag-based-access-gating
    - TAG
    - tag
    - Tags
    - tag-based-access-gating-unverified-classification-pattern
    - TAG(CP
    - tag-based-access-gating-workflow
    - TAGW
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
    - file: best-practices-for-abac-policies-databricks-on-aws.md
title: Tag-based access gating
description: A governance pattern that blocks access to untagged or unclassified data using a default restrictive tag, then applies masking policies once classification tags are applied.
tags:
  - abac
  - data-classification
  - tag-based
  - unity-catalog
  - data-governance
timestamp: "2026-06-18T14:39:58.863Z"
---

# Tag-based Access Gating

**Tag-based access gating** refers to the practice of using metadata tags — key-value pairs applied to [Unity Catalog](/concepts/unity-catalog.md) securable objects — to dynamically control data access through [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) policies. By evaluating tags at query time, administrators can implement row filters, column masks, and [ABAC GRANT Policies](/concepts/abac-grant-policy.md) that react automatically to changes in data classification or governance requirements, without hand‑editing individual grants. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md, best-practices-for-abac-policies-databricks-on-aws.md]

## Core Mechanisms

Databricks supports three primary ABAC policy types that use tags for access gating:

### Row Filter Policies
Row filter policies attach a [Row Filter UDF](/concepts/row-filter-and-column-mask-udfs.md) to tables or views. The UDF returns a Boolean expression that the query engine applies as an additional `WHERE` clause. Tags are evaluated via conditions such as `WHEN has_tag_value('classification', 'unverified')` to decide whether a row filter should be active. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Column Mask Policies
Column mask policies attach a [Column Mask UDF](/concepts/row-filter-and-column-mask-udfs.md) to specific columns. The mask function transforms the visible data based on the caller’s identity or other context. Tags can be checked in the `WHEN` clause and in the `MATCH COLUMNS` clause (e.g., `MATCH COLUMNS (has_tag_value('pii', 'name'))`) to determine which columns are masked and under what conditions. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### ABAC GRANT Policies (Beta)
ABAC GRANT policies dynamically grant privileges to securable objects (currently only models) whose [Governed Tags](/concepts/governed-tags.md) match a condition. They work alongside direct grants; the effective privileges on an object are the union of all applicable GRANT policy rules *and* all direct grants. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Common Patterns

The following patterns are drawn from Databricks’ recommended implementation strategies.

### Prevent Access Until Tagged
A common governance workflow is to block access to unclassified data and then automatically apply protections after tagging:

1. Apply a default tag, such as `classification : unverified`, to all new objects (e.g., at the catalog or schema level).
2. Create a row filter policy that blocks **all** non‑admin queries when that tag is present:  
   `WHEN has_tag_value('classification', 'unverified')` → block access.
3. Create a column mask policy that masks sensitive columns on tables where the `unverified` tag is no longer present.  
   When a data steward updates the tag to a verified classification, the blocking policy drops and the masking policy takes effect automatically. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Partial Reveal with String Functions
Instead of expensive regex‑based masking, use built‑in string functions to reveal only part of a sensitive value. For example, to show the last N digits of an SSN:

```sql
CREATE FUNCTION mask_ssn(ssn STRING, show_last INT) RETURNS STRING
  DETERMINISTIC
  RETURN CONCAT('***-**-', RIGHT(ssn, show_last));
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Consistent Hashing (Deterministic Pseudonymization)
Replace sensitive values with a deterministic hash so the same input always yields the same pseudonym across tables. A `version` parameter supports key rotation:

```sql
CREATE FUNCTION pseudonymize(val STRING, version INT) RETURNS STRING
  DETERMINISTIC
  RETURN SHA2(CONCAT(val, CAST(version AS STRING)), 256);
```

^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Row Filtering with Column‑Only Predicates
Filter rows using simple Boolean logic over table columns to enable [predicate pushdown](/concepts/selective-caching-with-predicate-pushdown.md). The UDF accepts column values and a constant list of allowed values, avoiding subqueries in the filter condition:

```sql
CREATE FUNCTION filter_by_region(region STRING, allowed STRING)
  RETURNS BOOLEAN
  DETERMINISTIC
  RETURN array_contains(split(allowed, ','), lower(region));
```

The policy passes the allowed regions via `USING COLUMNS (rgn, 'emea,apac')`. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Lookup Tables for Fine‑Grained Rules
When access rules differ per user and cannot be expressed purely through the policy's `TO`/`EXCEPT` clauses, check a small lookup table inside the UDF. Keep the lookup table small so the optimizer uses a broadcast hash join. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Auditing Tag-Based Access

Because effective privileges are the union of ABAC GRANT policies and direct grants, audit both surfaces together:

- Use `SHOW EFFECTIVE POLICIES` to see which ABAC policies apply to an object, including inherited ones.
- Use `SHOW GRANTS` and the effective permissions API to enumerate direct grants. ^[best-practices-for-abac-policies-databricks-on-aws.md]

Always use groups in the `TO` and `EXCEPT` clauses of ABAC policies to simplify future audits — adding or removing users from a group updates the policy’s effect without editing the policy itself. ^[best-practices-for-abac-policies-databricks-on-aws.md]

## Related Concepts

- [ABAC GRANT Policies](/concepts/abac-grant-policy.md)
- [Row Filter Policies](/concepts/row-filter-policies.md)
- [Column Mask Policies](/concepts/column-mask-policies.md)
- [Governed Tags](/concepts/governed-tags.md)
- [Unity Catalog Privileges](/concepts/unity-catalog-privilege-management.md)
- [Predicate Pushdown](/concepts/selective-caching-with-predicate-pushdown.md)
- Deterministic Functions in ABAC
- Broadcast Hash Join

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
- best-practices-for-abac-policies-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
2. [best-practices-for-abac-policies-databricks-on-aws.md](/references/best-practices-for-abac-policies-databricks-on-aws-716fb4af.md)
