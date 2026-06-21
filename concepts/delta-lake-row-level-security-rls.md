---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 633d24cb3d0c35252662f302db55d05db4bc6c17fa1e80316589efa5508b1858
  pageDirectory: concepts
  sources:
    - delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-row-level-security-rls
    - DLRS(
  citations:
    - file: delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md
title: Delta Lake Row-Level Security (RLS)
description: A Delta table security feature that restricts row access; incompatible with external metadata sources in Databricks.
tags:
  - delta-lake
  - security
  - data-governance
timestamp: "2026-06-18T11:53:16.822Z"
---

# Delta Lake Row-Level Security (RLS)

**Delta Lake Row-Level Security (RLS)** is a feature that uses row filter policies to restrict which rows of a Delta table are visible to a user at query time. RLS policies are implemented as [Row Filter Policies](/concepts/row-filter-policies.md) in [Unity Catalog](/concepts/unity-catalog.md) and are a type of [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) policy that filters data based on conditions evaluated at runtime. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Overview

RLS policies in Delta Lake filter data at the row level by applying user-defined functions (UDFs) that evaluate against the current user's identity or attributes. When a user queries a table with an RLS policy in place, only rows that match the policy's condition are returned. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## RLS and External Metadata

External Metadata does not support sources that have Row-level Security (RLS) policies applied. Specifically, the error condition `DELTA_EXTERNAL_METADATA_UNSUPPORTED_SOURCE` with subtype `ROW_FILTER` is raised when an unsupported table type has RLS policies enabled. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

### ROW_FILTER Error Condition

The `ROW_FILTER` error occurs under the following condition: ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

| Error Subtype | Description |
|---------------|-------------|
| `ROW_FILTER` | `<tableType>` with Row-level Security (RLS) policies. |

This error indicates that External Metadata cannot process a Delta table that has RLS policies applied, as External Metadata does not support this security feature.

## Limitations

- External Metadata sources do not support Delta tables with RLS policies. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- RLS policies are implemented through row filter policies, which require user-defined functions (UDFs) registered in Unity Catalog to implement the filter logic. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]
- Both [Row Filter Policies](/concepts/row-filter-policies.md) and [Column Mask Policies](/concepts/column-mask-policies.md) are not supported in External Metadata scenarios. ^[delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md]

## Related Concepts

- [Row Filter Policies](/concepts/row-filter-policies.md) — ABAC policies that restrict data rows based on conditions
- [Column Mask Policies](/concepts/column-mask-policies.md) — ABAC policies that mask sensitive columns
- [Attribute-Based Access Control (ABAC)](/concepts/attribute-based-access-control-abac.md) — The access control model for Unity Catalog
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer that provides ABAC policy capabilities
- [Delta Lake](/concepts/delta-lake.md) — The storage format where RLS policies are applied
- [External Metadata](/concepts/external-metadata-api.md) — A feature that does not support Delta tables with RLS
- [ABAC Policy Audit Logging](/concepts/abac-policy-audit-logging.md) — Monitoring and tracking of ABAC policy operations
- User-Defined Functions (UDFs) — Functions used to implement row filter logic in RLS policies

## Sources

- delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md

# Citations

1. [delta_external_metadata_unsupported_source-error-condition-databricks-on-aws.md](/references/delta_external_metadata_unsupported_source-error-condition-databricks-on-aws-478fcc27.md)
