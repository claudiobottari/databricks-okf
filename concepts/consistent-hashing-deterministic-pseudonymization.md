---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6d1fbfd22dcdfcf89f8650232229c40d2fe0870ca9eafb82a58239753dcd3677
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consistent-hashing-deterministic-pseudonymization
    - CH(P
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Consistent hashing (deterministic pseudonymization)
description: Replacing sensitive data with a deterministic hash (e.g., SHA2) via a DETERMINISTIC UDF so the same input always produces the same pseudonym across tables, with a version parameter to support key rotation.
tags:
  - abac
  - pseudonymization
  - hashing
  - data-masking
  - deterministic
timestamp: "2026-06-19T09:18:29.933Z"
---

# Consistent hashing (deterministic pseudonymization)

**Consistent hashing (deterministic pseudonymization)** is a data masking pattern that replaces sensitive data with a hashed value that is the same across multiple tables. This approach enables joins and aggregations on pseudonymized columns while protecting underlying sensitive data.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Deterministic behavior

Marking the hashing function as `DETERMINISTIC` tells the query engine that the function always returns the same result for the same input, which helps the engine optimize query performance. Deterministic functions are recommended for [ABAC](/concepts/abac-attribute-based-access-control.md) column mask and row filter policies wherever possible.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Versioning for key rotation

The pattern uses a `version` parameter to support key rotation. The version number can be incremented through the policy's `USING COLUMNS` clause to generate new hashes without breaking historical data that used the previous version. The function concatenates the original value with the version number before hashing, so the same input with the same version always produces the same hash.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example function

The following SQL function implements consistent hashing using SHA2 with a 256-bit digest:^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

```sql
CREATE FUNCTION pseudonymize(val STRING, version INT) RETURNS STRING
DETERMINISTIC
  RETURN SHA2(CONCAT(val, CAST(version AS STRING)), 256);
```

A [column mask policy](/concepts/column-mask-policies.md) can invoke this function as its masking UDF, passing the current version via `USING COLUMNS`. When the version is incremented, the policy's `USING COLUMNS` clause is updated to the new number; rows already stored retain their old hash, and new queries produce a hash with the new version.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Usage in ABAC policies

This pattern is commonly used in [ABAC Column Mask Policies](/concepts/abac-column-mask-policies.md) to pseudonymize columns such as email addresses, user IDs, or account numbers. Because the hash is consistent across tables, analysts can still join on the pseudonymized column without seeing the original value. The `version` parameter provides a managed rotation mechanism that avoids rewriting all historical data on every key change.^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related concepts

- [ABAC (Attribute-Based Access Control)](/concepts/abac-attribute-based-access-control.md) — The access control model within which row filter and column mask policies operate.
- [Column mask policy](/concepts/column-mask-policies.md) — An ABAC policy that applies a masking UDF to a column.
- DETERMINISTIC function — Function property enabling query optimizations.
- SHA2 — The hash function used in the example (SHA-256).

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
