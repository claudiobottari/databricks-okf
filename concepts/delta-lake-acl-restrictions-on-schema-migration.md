---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb54a3cd872eb26c65238df2ecfe1f2b49a0edc46de05addde786443360a0729
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-lake-acl-restrictions-on-schema-migration
    - DLAROSM
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Delta Lake ACL Restrictions on Schema Migration
description: When Table ACLs are enabled on a cluster, automatic schema migration via DataFrameWriter options is blocked; users must use ALTER TABLE instead.
tags:
  - delta-lake
  - access-control
  - security
timestamp: "2026-06-19T18:26:32.368Z"
---

# Delta Lake ACL Restrictions on Schema Migration

**Delta Lake ACL Restrictions on Schema Migration** refers to a specific error condition that occurs when attempting to automatically migrate a Delta table's schema in a cluster where Table Access Control Lists (ACLs) are enabled. This restriction prevents automatic schema changes and requires manual intervention through explicit `ALTER TABLE` commands.

## Error Condition

When writing to a Delta table in a cluster with Table ACLs enabled, the `DELTA_METADATA_MISMATCH` error class is raised with the `ACL_ENABLED` sub-type. The error indicates that automatic schema migration is blocked due to security policies enforced by the ACL system. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Error Identifier

- **SQLSTATE**: 42KDG ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **Error Class**: `DELTA_METADATA_MISMATCH` ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- **Sub-type**: `ACL_ENABLED` ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Error Message

> Table ACLs are enabled in this cluster, so automatic schema migration is not allowed. Please use the `ALTER TABLE` command for changing the schema.

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

The restriction is triggered when [Delta Lake](/concepts/delta-lake.md) detects that Table ACLs are enabled on the cluster where the write operation is being performed. The ACL framework enforces fine-grained access control on metadata operations, including schema changes. To maintain security integrity, automatic schema migration is disabled in this context. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

Instead of relying on automatic schema migration via DataFrameWriter options (such as `mergeSchema` or `overwriteSchema`), users must explicitly modify the table schema using the ALTER TABLE SQL command. This ensures that all schema changes are subject to the appropriate ACL permissions and auditing. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Example

```sql
ALTER TABLE table_name ADD COLUMNS (new_column data_type);
```

This approach respects the ACL permissions configured for the table and cluster. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Error Sub-types

The `DELTA_METADATA_MISMATCH` error class includes several other sub-types for different schema migration scenarios: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

- `ENABLE_LIQUID` — Requires `overwriteSchema` option when enabling clustering on existing tables ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- `OVERWRITE_REQUIRED` — Requires `overwriteSchema` option for schema or partitioning changes ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- `PARTITIONING_MISMATCH` — Partition columns don't match table specification ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]
- `SCHEMA_MISMATCH` — General schema mismatch detected when writing to Delta tables ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The underlying storage layer and transactional metadata system
- Table ACLs in Databricks — Access control policies governing table operations
- ALTER TABLE — SQL command for explicit schema modification
- Schema Evolution in Delta Lake — Strategies for managing schema changes over time
- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH — The broader error class for metadata conflicts

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
