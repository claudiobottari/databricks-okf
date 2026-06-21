---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c3c18e03edb09158e7881418ce6be6e66bf57e222fadcc48e2f1fb0824b82ee
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-dimensional-access-control-with-single-lookup-table
    - MACWSLT
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Multi-Dimensional Access Control with Single Lookup Table
description: Replacing N groups per access dimension with a single table where each row represents a user's permissions across multiple dimensions (region, department, clearance level), eliminating combinatorial group explosion.
tags:
  - data-governance
  - access-control
  - scalability
timestamp: "2026-06-19T23:22:56.619Z"
---

# Multi-Dimensional Access Control with Single Lookup Table

**Multi-Dimensional Access Control with Single Lookup Table** is a dynamic access control pattern on Databricks that uses a single mapping table to drive both row-level filtering and column-level masking, replacing the need to manage large numbers of groups or rewrite policies for each access dimension change. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Overview

In traditional group-based access control, an organization with four regions and four departments requires 16 groups to cover every region-department combination. Adding PII clearance tiers (full, masked, or none) triples that count, and each new region or department requires creating new groups and updating policies. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

The mapping table approach replaces this with a single lookup table containing one row per user, one column per access dimension. To change a user's access, you update a row — no policy or group changes are needed. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Prerequisites

The mapping table pattern requires:
- Databricks Runtime 16.4 or above, or serverless compute
- Account admin or workspace admin permissions (to create [Governed Tags](/concepts/governed-tags.md))
- `MANAGE` permission on the target catalog or schema
- `EXECUTE` on the UDFs
- A SQL notebook or query editor

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Mapping Table Structure

The mapping table (typically named `user_access`) contains one row per user and one column per access dimension:

| Column | Purpose |
|--------|---------|
| `user_email` | Identifies the user |
| `region` | The user's allowed region |
| `department` | The user's allowed department |
| `pii_access` | Controls PII display level (`full`, `masked`, or `none`) |
| `expires_on` | Sets an expiration date for automatic access revocation |

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

Keep mapping tables small and simple. Each query against a protected table runs the [Row Filter and Column Mask UDFs](/concepts/row-filter-and-column-mask-udfs.md), which in turn query the mapping table. Large mapping tables and complex UDF logic can impact query performance. Use narrow schemas and keep UDF logic to a single lookup where possible. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Governance Tags

The mapping table pattern relies on [Governed Tags](/concepts/governed-tags.md) (created in the [Catalog Explorer](/concepts/catalog-explorer.md) UI under **Catalog** > **Govern** > **Governed Tags**) to enable automatic policy matching:

- `region` and `department` tags tell the row filter policy which columns to pass to the filter UDF
- `pii` tag tells [Column Mask Policies](/concepts/column-mask-policies.md) which columns to mask and what PII type they contain
- `priority` tag lets [Column Mask Policies](/concepts/column-mask-policies.md) pass the `order_priority` value to the mask UDF for conditional masking

Tag data is stored as plain text and may be replicated globally. Do not use tag names, values, or descriptors that could compromise the security of your resources. For example, do not use tag names, values or descriptors that contain personal or sensitive information. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Row Filter UDF

The row filter UDF receives a row's `sales_region` and `dept` values (passed in by the policy via tag matching), looks up the current user in the mapping table, and returns `TRUE` only if a matching entry exists and has not expired. Users not in the mapping table, or whose access has expired, see no rows (fail-closed design). ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Column Mask UDF

The column mask UDF controls how PII columns are displayed with two layers:

- **Layer 1 (conditional masking):** If `order_priority` is `confidential`, PII is always fully redacted regardless of the user's clearance level
- **Layer 2 (user clearance):** For standard rows, the UDF checks the mapping table for the user's `pii_access` level and applies the corresponding mask

If a user has multiple mapping table entries (multi-region access), the highest clearance across all rows applies. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Dynamic Access Operations

The key benefit of the mapping table approach is that access changes are made by updating rows in the table — no policy, UDF, or group member updates are needed:

### Reassignment
Change a user's department by updating the `department` column in the mapping table.

### Clearance Upgrade
Change a user's `pii_access` from `masked` to `full` to see actual PII values on standard-priority rows.

### Multi-Region Access
Insert additional rows to grant access to multiple regions without creating new groups or policies.

### Access Expiration
Set `expires_on` to a past date. The row filter UDF checks `expires_on >= current_date()`, so expired entries are silently ignored and access is automatically revoked with no manual intervention. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Related Concepts

- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md)
- [Row-Level Security](/concepts/row-level-security-rls-policies.md)
- Column-Level Security
- [Dynamic Data Masking](/concepts/conditional-column-masking.md)
- [Conditional Masking](/concepts/conditional-column-masking.md)
- Fail-Closed Design
- Managed Governance Tags

## Sources

- Use mapping tables for dynamic access control | [Databricks on AWS](/concepts/databricks-on-aws.md)

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
