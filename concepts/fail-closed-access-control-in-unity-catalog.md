---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c22b2cfab0feb6d4e0654016edc062e95716b4afb56da987fd408000c31c0b41
  pageDirectory: concepts
  sources:
    - use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - fail-closed-access-control-in-unity-catalog
    - FACIUC
  citations:
    - file: use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md
title: Fail-Closed Access Control in Unity Catalog
description: A security design principle where users not found in an access mapping table, or whose access has expired, see no rows by default rather than all rows.
tags:
  - data-governance
  - security
  - access-control
timestamp: "2026-06-19T23:22:22.179Z"
---

# Fail-Closed Access Control in [Unity Catalog](/concepts/unity-catalog.md)

**Fail-Closed Access Control** in [Unity Catalog](/concepts/unity-catalog.md) is a security principle where access is denied by default if a row filter or column mask policy cannot determine that a user should have access. In Unity Catalog’s [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policies, this means that if a user does not have a matching entry in a mapping table, or if their access entry has expired, the policy returns no rows (for row filters) or fully redacts values (for column masks). This design prevents accidental data exposure when a user’s authorization cannot be positively confirmed. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## How Fail-Closed Works with Row Filters

A row filter policy is implemented as a user-defined function (UDF) that returns a boolean value. In a typical mapping-table implementation, the UDF evaluates whether the current user exists in the mapping table with a matching region and department, and whether their `expires_on` date has not yet passed. If the `EXISTS` query returns no rows, the UDF returns `FALSE`, and the entire row is excluded from the query result. This behavior is explicitly described as **fail-closed design**: “Users not in the mapping table, or whose access has expired, see no rows (fail-closed design).” ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## How Fail-Closed Works with Column Masks

[Column Mask Policies](/concepts/column-mask-policies.md) function similarly. If a user does not have a clearance level recorded in the mapping table (or if the highest clearance across all their entries is absent), the mask UDF returns a fully redacted value (for example, `***REDACTED***`). This ensures that sensitive data is never visible unless the policy can positively authorize the user. The same fail-closed principle applies even when conditional masking is used: if the order priority is `confidential`, the PII is always fully redacted regardless of clearance, as a further fail-closed safeguard. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Role of Access Expiration

The mapping table often includes an `expires_on` column. The row filter checks `expires_on >= current_date()`. When the expiration date is in the past, the lookup fails and the user is denied access. This automatic fail‑closed behavior allows time‑limited access to be revoked without manual intervention: expired entries are silently ignored, and the user sees no rows. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Contrast with Fail-Open

While the source material does not explicitly use the term “fail‑open,” the fail‑closed design ensures that a missing or expired mapping entry results in denial, rather than granting access by default. This is a deliberate choice to prevent data leakage when the mapping table does not contain an entry for the current user. ^[use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md]

## Related Concepts

- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that supports ABAC policies and fail‑closed evaluation.
- [Row Filter Policy](/concepts/abac-row-filter-policy.md) – A policy that includes or excludes rows based on a UDF returning TRUE or FALSE.
- [Column Mask Policy](/concepts/column-mask-policies.md) – A policy that transforms column values, with redaction as the fallback.
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) – The permission model underlying mapping-table lookups.
- Mapping Table – A lookup table that drives dynamic row and column access without per-group policy changes.
- [Policy Evaluation in Unity Catalog](/concepts/effective-policy-evaluation-in-unity-catalog.md) – The broader rules governing how policies are combined and how fail‑closed applies.

## Sources

- use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md

# Citations

1. [use-mapping-tables-for-dynamic-access-control-databricks-on-aws.md](/references/use-mapping-tables-for-dynamic-access-control-databricks-on-aws-cfb1e1c1.md)
