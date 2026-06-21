---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 53c09ee4b48283438660b924cd4c405bd8e1d520953dba550d4b8fed692407ae
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - table-acls-blocking-delta-schema-evolution
    - TABDSE
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: Table ACLs Blocking Delta Schema Evolution
description: A restriction where enabling Table ACLs on a cluster disables automatic schema migration for Delta tables, requiring explicit ALTER TABLE commands.
tags:
  - delta-lake
  - security
  - access-control
  - schema-evolution
timestamp: "2026-06-19T10:07:44.378Z"
---

# Table ACLs Blocking Delta Schema Evolution

**Table ACLs Blocking Delta Schema Evolution** is an error condition that occurs when attempting to write data with a different schema to a Delta table while table-level access control lists (ACLs) are enabled on the cluster. The Delta engine blocks automatic schema migration in this case, requiring manual schema changes instead.

## Error Condition

This error manifests as a `DELTA_METADATA_MISMATCH` with the subtype `ACL_ENABLED`. The full error message is: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

```
Table ACLs are enabled in this cluster, so automatic schema migration is not allowed. Please use the `ALTER TABLE` command for changing the schema.
```

## Cause

When a cluster has table ACLs enabled, Delta's automatic schema evolution — which would normally add new columns or change column types when writing data with a different schema — is disabled for security reasons. This prevents potential data exposure or schema manipulation that could bypass ACL protections. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

Without table ACLs, users can set `mergeSchema` to `true` (for DataFrame writers) or enable `spark.databricks.delta.schema.autoMerge.enabled` (for other operations) to allow automatic schema migration. However, these options are insufficient when table ACLs are active on the cluster. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

Use explicit `ALTER TABLE` commands to manually evolve the table schema before writing new data. This approach ensures that schema changes are intentional and can be audited, maintaining the security guarantees provided by table ACLs. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

### Example

Instead of relying on automatic schema merge:

```python
# This will fail with ACL_ENABLED error when table ACLs are active
df.write \
  .mode("append") \
  .option("mergeSchema", "true") \
  .saveAsTable("my_table")
```

First, manually add the new columns:

```sql
ALTER TABLE my_table ADD COLUMNS (new_column STRING);
```

Then write the data without the schema merge option:

```python
df.write.mode("append").saveAsTable("my_table")
```

## Related Error Conditions

The `DELTA_METADATA_MISMATCH` error class includes several other subtypes: ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

- `ENABLE_LIQUID` — Occurs when trying to enable clustering on an existing table; requires overwrite mode with `overwriteSchema` set to `true`.
- `OVERWRITE_REQUIRED` — Occurs when schema or partitioning changes need explicit overwrite mode.
- `PARTITIONING_MISMATCH` — Occurs when the partition columns in the data do not match the table's partition columns.
- `SCHEMA_MISMATCH` — A general schema mismatch detected when writing to the Delta table.

## Related Concepts

- Delta Table Schema Evolution — Automatic schema migration capabilities in Delta Lake
- Table ACLs — Access control lists for Databricks tables
- ALTER TABLE Command — SQL command for manual schema changes
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage layer for Delta tables
- DELTA_METADATA_MISMATCH Error Class — The parent error class for schema-related write errors

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
