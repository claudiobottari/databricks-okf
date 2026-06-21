---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 223341392fd8cebd207e92f1bad27efad75aa45d97246d4cfa394c849b38162f
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - access-expiration-via-mapping-tables
    - AEVMT
    - Access Expiration
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Access Expiration via Mapping Tables
description: Using an expires_on date column in a mapping table to automatically revoke access without manual intervention, useful for contractors and time-limited data sharing.
tags:
  - data-governance
  - access-control
  - expiration
timestamp: "2026-06-19T23:22:02.494Z"
---

# Access Expiration via Mapping Tables

**Access Expiration via Mapping Tables** is a pattern for implementing time-limited data access in [Unity Catalog](/concepts/unity-catalog.md) by including an expiry date column in a mapping table. When a row filter UDF checks the expiry date against the current date, expired entries are silently ignored and access is automatically revoked without any manual intervention.

## Overview

Mapping tables used for Dynamic Access Control can include an `expires_on` column that sets an expiration date for each access entry. The row filter UDF checks `expires_on >= current_date()` at query time, so entries with a past date stop matching and the user loses access. This eliminates the need to manually revoke access by updating policies, UDFs, or group memberships. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Implementation

### Schema Design

The mapping table must include a date column for expiration. In the following example, the `user_access` table contains an `expires_on` column of type `DATE`:

```sql
CREATE OR REPLACE TABLE catalog.schema.user_access (
  user_email STRING,
  region STRING,
  department STRING,
  pii_access STRING,
  expires_on DATE
);
```

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

### Row Filter UDF with Expiration Check

The row filter UDF must include an expiration check as part of its `WHERE` clause. The UDF returns `TRUE` only if a matching entry exists *and* the entry has not expired:

```sql
CREATE OR REPLACE FUNCTION catalog.schema.access_filter(
  region_val STRING,
  dept_val STRING
) RETURNS BOOLEAN
RETURN EXISTS (
  SELECT 1 FROM catalog.schema.user_access
  WHERE user_email = current_user()
    AND region = region_val
    AND department = dept_val
    AND expires_on >= current_date()
);
```

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

Because the row filter follows a Fail-Closed Policy Evaluation|fail-closed design, users whose access has expired see no rows at all — they are not shown an error or warning. The expiration is transparent to the end user. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Use Cases

Access expiration via mapping tables is useful for:

- **Contractors and temporary workers**: set an expiration date matching the contract end date, after which access automatically terminates.
- **Time-limited data sharing agreements**: grant access for a fixed duration without requiring manual revocation.
- **Time-limited projects**: grant access only for the duration of a project, after which the entry expires.

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Example: Expiring Access

To expire a user's access, update the `expires_on` column to a past date. The following example sets the expiration to yesterday, which immediately revokes access:

```sql
UPDATE catalog.schema.user_access
SET expires_on = current_date() - INTERVAL 1 DAY
WHERE user_email = current_user();
```

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

After this update, queries against the protected table return no rows because the row filter UDF checks `expires_on >= current_date()` and the condition fails.

To restore access, set a future expiration date:

```sql
UPDATE catalog.schema.user_access
SET expires_on = '2099-12-31'
WHERE user_email = current_user();
```

^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Design Considerations

The `expires_on` check is performed at query time, so there is no background job or scheduler required to revoke access. The expiration is enforced immediately when the date passes. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

Keep mapping tables small and simple. Each query against a protected table runs the row filter UDF, which in turn queries the mapping table. Large mapping tables and complex UDF logic can impact query performance. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Related Concepts

- [Mapping Tables for Access Control](/concepts/mapping-tables-for-access-control.md) — The general pattern of using lookup tables for dynamic access control
- [Row Filter UDF](/concepts/row-filter-and-column-mask-udfs.md) — The function that evaluates mapping table entries, including expiration checks
- [Column Mask UDF](/concepts/row-filter-and-column-mask-udfs.md) — Column-level masking policies that can be combined with expiration-based row filters
- Fail-Closed Policy Evaluation — The security model where expired users see no rows instead of an error

## Sources

- use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
