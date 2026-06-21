---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7b2ad33654b7282e6bcb493a548a5e8deec7e687e05c2768ce274dab100d69e5
  pageDirectory: concepts
  sources:
    - row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - troubleshooting-abac-policy-conflicts
    - TAPC
  citations:
    - file: row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md
title: Troubleshooting ABAC Policy Conflicts
description: Diagnostic approach using SHOW EFFECTIVE POLICIES and INFORMATION_SCHEMA views to identify conflicts, with resolution strategies including refining conditions, adjusting principals, and restructuring policies.
tags:
  - abac
  - troubleshooting
  - conflict-resolution
  - diagnostics
timestamp: "2026-06-19T20:16:40.183Z"
---

# Troubleshooting ABAC Policy Conflicts

**Troubleshooting ABAC Policy Conflicts** refers to the process of diagnosing and resolving situations where multiple Attribute-Based Access Control (ABAC) policies produce conflicting row filters or column masks for the same user and table at query time. When Databricks detects such conflicts during policy evaluation, it blocks access and returns specific error codes until the conflict is resolved. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Overview of Conflict Detection

ABAC policy evaluation follows a [fail-closed design](/concepts/fail-closed-design-for-abac-policies.md): Databricks defaults to denying access if it cannot safely enforce all applicable policies. For a given table and user, only one distinct row filter can be resolved at query time, and only one distinct column mask per column can be applied for a given column and user. This prevents ambiguous query results. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

If multiple distinct filters or masks would apply to the same user and table (or column), Databricks blocks access and returns an error. Examples of conflicting scenarios include:

- A table-level row filter or column mask (manually applied) conflicts with an ABAC-defined filter or mask on the same target.
- A row filter’s `USING COLUMNS` clause references a `MATCH COLUMNS` alias that matches multiple columns, making it impossible to determine which column value to pass to the UDF.
- A column masked by one policy is referenced in the `USING COLUMNS` clause of another policy.

Multiple ABAC policies can coexist for the same table or column only if they resolve to the same effective filter or mask—for example, policies referencing the same UDF with identical arguments. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Error Messages

When a conflict is detected, Databricks throws one of the following errors:

- `INVALID_PARAMETER_VALUE.UC_ABAC_MULTIPLE_ROW_FILTERS` — for row filter conflicts
- `COLUMN_MASKS_FEATURE_NOT_SUPPORTED.MULTIPLE_MASKS` — for column mask conflicts

Access to the affected table is blocked until the conflict is resolved. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Diagnosing Conflicts

To identify the source of a policy conflict, use the following diagnostic tools:

1. **`SHOW EFFECTIVE POLICIES`** — Displays all ABAC policies that apply to the target table for the current user.^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
2. **`INFORMATION_SCHEMA.ROW_FILTERS`** and **`INFORMATION_SCHEMA.COLUMN_MASKS`** — Reveals any table-level row filters or column masks manually applied to the table that may conflict with ABAC policies.^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]
3. **Check overlapping policy conditions** — Review which policies overlap in their `TO`/`EXCEPT` principal lists and `WHEN`/`MATCH COLUMNS` conditions to identify where multiple policies apply to the same user and table. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Resolution Strategies

Resolve policy conflicts by applying one or more of the following approaches:

### Refining Policy Conditions

Update `WHEN` or `MATCH COLUMNS` clauses to be more specific, ensuring distinct policies target different tables or columns rather than overlapping scopes. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Adjusting Governed Tags

Review [governed tag](/concepts/governed-tags.md) assignments on columns or tables that may cause unintended policy matches. Remove or update tags that trigger multiple applicable policies for the same user. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Adjusting Principals

Update `TO`/`EXCEPT` clauses so each user falls within the scope of at most one policy per table (for row filters) or per column (for column masks). This is the most direct way to eliminate overlap. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

### Restructuring Policies

Consolidate overlapping policies into a single, unified policy, or split broad policies into separate, explicitly targeted ones that do not share the same user or table scope. ^[row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md]

## Related Concepts

- [ABAC policy evaluation](/concepts/dynamic-abac-policy-evaluation.md) — The two-stage process (Unity Catalog + Databricks Runtime) that determines effective filters and masks
- [Fail-closed design](/concepts/fail-closed-design-for-abac-policies.md) — Security model that denies access when enforcement cannot be verified
- [Row Filter and Column Mask Policies](/concepts/row-filter-and-column-mask-policies.md) — The UDF-based mechanisms that enforce ABAC at query time
- [Governed Tags](/concepts/governed-tags.md) — Tag-based dependencies that can trigger policy conflicts
- INVALID_PARAMETER_VALUE — Error class for row filter conflicts
- COLUMN_MASKS_FEATURE_NOT_SUPPORTED — Error class for column mask conflicts
- [SHOW EFFECTIVE POLICIES](/concepts/show-effective-policies.md) — Diagnostic command for viewing applicable policies
- INFORMATION_SCHEMA — System catalog tables for identifying manually applied filters

## Sources

- row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md

# Citations

1. [row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws.md](/references/row-filter-and-column-mask-policy-evaluation-and-runtime-behavior-databricks-on-aws-2d8da254.md)
