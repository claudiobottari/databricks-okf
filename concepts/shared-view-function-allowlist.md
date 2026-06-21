---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: de8d8fbc73b2166f5813c6b390de4a8935b0654efb4d8e7d3c580bfafa7e1e73
  pageDirectory: concepts
  sources:
    - functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - shared-view-function-allowlist
    - SVFA
  citations:
    - file: functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md
title: Shared View Function Allowlist
description: The security mechanism that restricts Databricks-to-Databricks shared views to only a specific subset of built-in SQL functions and operators, preventing potentially dangerous operations on shared data.
tags:
  - delta-sharing
  - security
  - sql-functions
timestamp: "2026-06-19T10:42:01.610Z"
---

# Shared View Function Allowlist

**Shared View Function Allowlist** refers to the restricted set of built-in SQL functions and operators that Databricks permits in Databricks-to-Databricks view sharing. This allowlist is enforced to protect data security when materialized views are shared across workspaces using Delta Sharing.

## Overview

When a provider shares a view using Databricks-to-Databricks view sharing, the recipient sees only the result of the view query, not the underlying tables. To prevent potential data leakage or injection through arbitrary SQL execution, Databricks limits the functions and operators allowed in shared view definitions to a curated allowlist. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

All functions outside this allowlist are blocked from the view definition. This ensures that the shared view is deterministic and safe for the recipient to query.

## Allowlist Scope

The allowlist covers a subset of all Databricks built-in functions and operators. It includes common mathematical, string, date/time, aggregation, array, map, H3 geospatial, and type conversion functions, as well as operators like arithmetic, comparison, and logical operators. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

The complete list is maintained in the Databricks documentation and is the authoritative reference. Representative examples include:

- **Arithmetic operators**: `+`, `-`, `*`, `/`, `%`
- **Comparison operators**: `=`, `<`, `>`, `<=`, `>=`, `<>`, `BETWEEN`, `IN`
- **String functions**: `SUBSTR`, `CONCAT`, `REPLACE`, `TRIM`, `LOWER`, `UPPER`, `REGEXP_REPLACE`
- **Date/time functions**: `CURRENT_DATE`, `CURRENT_TIMESTAMP`, `DATEADD`, `DATEDIFF`, `YEAR`, `MONTH`, `DAY`
- **Aggregate functions**: `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `COLLECT_LIST`, `COLLECT_SET`
- **Array and map functions**: `ARRAY`, `ARRAY_CONTAINS`, `ARRAY_DISTINCT`, `MAP`, `MAP_KEYS`, `TRANSFORM`
- **Type conversion functions**: `CAST`, `STRING`, `INT`, `BIGINT`, `DATE`, `TIMESTAMP`, `TO_DATE`, `TO_NUMBER`
- **Encryption/hash functions**: `MD5`, `SHA1`, `SHA2`, `AES_ENCRYPT`, `AES_DECRYPT`
- **Conditional functions**: `IF`, `COALESCE`, `NULLIF`, `CASE` (implicit through `WHEN`)
- **Window functions**: `RANK`, `DENSE_RANK`, `ROW_NUMBER`, `LAG`, `LEAD`, `NTILE`
- **H3 geospatial functions**: `H3_LONGLATASH3`, `H3_DISTANCE`, `H3_KRING`, `H3_TOCHILDREN`, etc.

## Security Rationale

By restricting the function set, the allowlist reduces the attack surface for malicious or accidental data exposure through shared views. It prevents the use of potentially dangerous functions such as file I/O, external network access, or arbitrary UDFs that might otherwise be executed in the recipient’s cluster. ^[functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md]

## Related Concepts

- [Databricks-to-Databricks View Sharing](/concepts/databricks-to-databricks-view-sharing.md) – The infrastructure that enables sharing views across workspaces.
- [Delta Sharing](/concepts/delta-sharing.md) – The open protocol underlying view sharing.
- View Security in Databricks – Broader security considerations for shared views.
- Built-in Functions in Databricks SQL – The full set of functions from which the allowlist is drawn.

## Sources

- functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md

# Citations

1. [functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws.md](/references/functions-supported-in-databricks-to-databricks-view-sharing-databricks-on-aws-c0b6a2ae.md)
