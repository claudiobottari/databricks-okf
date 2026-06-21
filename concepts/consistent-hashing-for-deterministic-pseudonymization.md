---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b30d338e51dd5b26702dfd8c532e117763f04de9f2a92034f49f407f658079a5
  pageDirectory: concepts
  sources:
    - common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - consistent-hashing-for-deterministic-pseudonymization
    - CHFDP
    - Consistent Hashing for Pseudonymization
  citations:
    - file: common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md
title: Consistent hashing for deterministic pseudonymization
description: Replacing sensitive data with a deterministic hash that is consistent across tables using DETERMINISTIC UDFs, with a version parameter to support key rotation without breaking historical data.
tags:
  - data-governance
  - pseudonymization
  - hashing
  - abac
  - privacy
timestamp: "2026-06-19T17:47:09.012Z"
---

# Consistent Hashing for Deterministic Pseudonymization

**Consistent hashing for deterministic pseudonymization** (also called deterministic pseudonymization) is a data masking technique that replaces sensitive values with a hashed representation that remains consistent across different tables and queries. It is commonly implemented as a column mask function in an ABAC policy. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Overview

Consistent hashing replaces sensitive data with a hashed value that is the same across multiple tables. Because the function is marked `DETERMINISTIC`, the engine always returns the same result for the same input, which enables query optimizations such as predicate pushdown and result caching. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Key Concepts

### Deterministic Property

Marking a masking function as `DETERMINISTIC` tells the query engine that the function produces the same output for the same input. This allows the engine to optimize execution by reusing computed results and safely pushing predicates through the mask. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md] See [Use deterministic, error-safe expressions](/concepts/deterministic-and-error-safe-expressions-in-policy-udfs.md) for more details. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

### Version Parameter for Key Rotation

The function accepts a `version` parameter to support key rotation. By incrementing the version number (typically passed via the policy’s `USING COLUMNS` clause), the administrator generates new hashes without breaking historical data that was produced with the previous version. The version number is concatenated with the original value before hashing, ensuring that the same input with a different version yields a different hash. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Example Implementation

The following SQL function uses SHA‑256 to produce a consistent hash of a string value:

```sql
CREATE FUNCTION pseudonymize(val STRING, version INT) RETURNS STRING
DETERMINISTIC
  RETURN SHA2(CONCAT(val, CAST(version AS STRING)), 256);
```

The function concatenates the original value with the version number and then applies SHA‑256. In a [column mask policy](/concepts/column-mask-policies.md), you would call this function with a fixed version to generate a deterministic pseudonym for each input value. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Benefits

- **Cross‑table consistency**: The hash of a given value (e.g., a user ID or email) is the same in every table where the mask is applied, enabling joins on pseudonymized columns. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]
- **Reversible rotation**: By storing the version number as part of the policy, you can invalidate old hashes and generate new ones without touching historical data – the old version remains usable for lookups that match the previous hash. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]
- **Performance**: The `DETERMINISTIC` flag allows the engine to avoid redundant computations and to optimize query plans. ^[common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md]

## Related Concepts

- ai_mask Function|Masking function – The SQL UDF that implements the pseudonymization logic.
- [Column mask policy](/concepts/column-mask-policies.md) – The ABAC policy that applies the masking function to specific columns.
- [ABAC for row filtering and column masking](/concepts/row-filters-and-column-masks.md) – General patterns for implementing ABAC in Unity Catalog.
- SHA-256 – The cryptographic hash function used in the example.
- Key rotation – The practice of periodically changing cryptographic secrets; the version parameter supports this.

## Sources

- common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md

# Citations

1. [common-patterns-for-row-filtering-and-column-masking-databricks-on-aws.md](/references/common-patterns-for-row-filtering-and-column-masking-databricks-on-aws-f18db1c1.md)
