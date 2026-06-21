---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 30b8835253c3c62cdf784f0ae95e91a67d3afaa26a8a2bdca2fb9a852c279558
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mapping-table-pattern-for-access-control
    - MTPFAC
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Mapping Table Pattern for Access Control
description: A single lookup table that drives both row-level filtering and column-level masking, replacing complex group-based approaches with row updates for access changes.
tags:
  - data-governance
  - access-control
timestamp: "2026-06-19T23:22:05.856Z"
---

# Mapping Table Pattern for Access Control

The **Mapping Table Pattern for Access Control** is a database design approach that uses a single lookup table to dynamically manage [Row Filters](/concepts/row-filter-policies.md) and [Column Masks (Databricks)](/concepts/column-masks-in-delta-lake.md) in [Unity Catalog](/concepts/unity-catalog.md). Instead of creating a separate group for every combination of access dimensions (such as region, department, and clearance level), a single mapping table stores one row per user with columns representing each access dimension. Access changes require only a row update — no new groups, policy rewrites, or UDF modifications are needed. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Benefits Over Group-Based Approaches

With a group-based approach, every combination of access dimensions requires a dedicated group. For example, four regions and four departments create 16 groups. Adding PII clearance tiers (full, masked, none) triples that count to 48 groups. Each new region, department, or clearance level requires additional groups and policy updates. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

The mapping table approach replaces this combinatorial explosion with a single lookup table: one row per user, one column per access dimension. To change a user's access, you update a row in the table. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Architecture

The pattern involves four components working together:

1. **Mapping table**: Stores user identities, allowed regions, departments, PII clearance levels, and optional expiration dates. One row represents one access assignment for one user. Users needing multiple region-department combinations have multiple rows. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

2. **Row filter UDF**: A function that receives a row's attribute values (passed by the policy via tag matching), looks up the current user in the mapping table, and returns `TRUE` only if a matching, non-expired entry exists. Users not in the mapping table, or whose access has expired, see no rows (fail-closed design). ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

3. **Column mask UDF**: A function that controls how sensitive columns are displayed. It takes the column value and optional context parameters, then applies masking logic based on the user's clearance level from the mapping table. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

4. **[Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies**: Row filter and [Column Mask Policies](/concepts/column-mask-policies.md) that use `MATCH COLUMNS` with [Governed Tags](/concepts/governed-tags.md) to automatically discover which columns to pass to the UDFs. Tags such as `region`, `department`, and `pii` tell the policies which columns to protect and how to identify them. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Performance Considerations

Keep mapping tables small and simple. Each query against a protected table runs the [Row Filter and Column Mask UDFs](/concepts/row-filter-and-column-mask-udfs.md), which in turn query the mapping table. Large mapping tables and complex UDF logic can impact query performance. Use narrow schemas and keep UDF logic to a single lookup where possible. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Common Patterns

### Conditional Masking

The mask UDF can check a row-level attribute (such as `order_priority`) to decide how to mask PII. For example, orders marked `confidential` have their PII fully redacted regardless of the user's clearance level. This is implemented by tagging the row attribute column (e.g., with a `priority` tag) and passing its value to the mask UDF via `MATCH COLUMNS`. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Access Expiration

The mapping table can include an `expires_on` date column. The row filter UDF checks `expires_on >= current_date()`, so expired entries are silently ignored and access is automatically revoked with no manual intervention. This is useful for contractors, temporary data sharing agreements, or time-limited projects. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Multi-Region Access

Users needing access to multiple region-department combinations simply have multiple rows in the mapping table. No new groups or policies are required. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Example Schema

```sql
CREATE OR REPLACE TABLE user_access (
  user_email STRING,
  region STRING,
  department STRING,
  pii_access STRING,   -- 'full', 'masked', or 'none'
  expires_on DATE
);
```

The `pii_access` column controls how PII columns appear:
- `full` — see the actual value (for standard-priority rows)
- `masked` — see a partial value such as `A***` or `o***@acme.com`
- `none` — see `***REDACTED***`

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Requirements

- Databricks Runtime 16.4 or above, or serverless compute
- Account admin or workspace admin permissions (to create [Governed Tags](/concepts/governed-tags.md))
- `MANAGE` permission on the target catalog or schema
- `EXECUTE` on the UDFs

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Security Considerations

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values, or descriptors that contain personal or sensitive information. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Related Concepts

- [Row Filters](/concepts/row-filter-policies.md) — Policies that restrict which rows a user can see
- [Column Masks (Databricks)](/concepts/column-masks-in-delta-lake.md) — Policies that obfuscate column values at query time
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model underlying tag-based policies
- [Unity Catalog](/concepts/unity-catalog.md) — The data governance platform that enforces these policies
- [Policy Evaluation](/concepts/dynamic-abac-policy-evaluation.md) — How Databricks evaluates multiple policies on the same table

## Sources

- use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
