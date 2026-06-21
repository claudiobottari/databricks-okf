---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: adaee5f217ab375832eb98954eafa11fe8732e266a0eb21fae56243e39ac2f5b
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - acl_enabled-sub-error
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: ACL_ENABLED sub-error
description: A DELTA_METADATA_MISMATCH sub-error that occurs when table ACLs are enabled, preventing automatic schema migration
tags:
  - databricks
  - delta-lake
  - access-control
  - error-messages
timestamp: "2026-06-19T15:06:27.410Z"
---

# ACL_ENABLED Sub-error

**ACL_ENABLED** is a sub-error of the DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH error class that occurs when a write operation attempts an automatic schema migration on a Delta table, but the cluster has Table Access Control Lists (ACLs) enabled.

## Error Message

```
DELTA_METADATA_MISMATCH.ACL_ENABLED: Table ACLs are enabled in this cluster, so automatic schema migration is not allowed. Please use the `ALTER TABLE` command for changing the schema.
```

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

When a cluster has Table ACLs turned on, Databricks does not permit automatic schema changes (such as adding or removing columns) during a write operation. This restriction exists because ACLs require explicit, auditable schema modifications to maintain governance and security. Instead, the user must manually apply schema changes using the ALTER TABLE statement before attempting the write. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Resolution

To resolve this error, use an `ALTER TABLE` command to modify the [Delta table](/concepts/delta-lake-table.md) schema to match the data being written. For example, to add a new column:

```sql
ALTER TABLE table_name ADD COLUMNS (new_column <data_type>);
```

After the schema is updated, the write operation (e.g., `INSERT`, `MERGE`, or DataFrame write) can proceed without triggering the metadata mismatch. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH – The parent error class for table metadata conflicts.
- [Schema migration](/concepts/delta-lake-schema-migration.md) in Delta Lake – Automatic or manual adjustments to table schema.
- Table ACLs – Access control lists governing permissions on Delta tables.
- ALTER TABLE – SQL command used for explicit schema changes.
- [Delta Lake](/concepts/delta-lake.md) – The underlying storage format and protocol.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
