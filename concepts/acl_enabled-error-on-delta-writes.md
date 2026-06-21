---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2eefea186b65b8cd53cb1c98d543e3715be2eccbec5ffb0a328e149197253804
  pageDirectory: concepts
  sources:
    - delta_metadata_mismatch-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - acl_enabled-error-on-delta-writes
    - AEODW
  citations:
    - file: delta_metadata_mismatch-error-condition-databricks-on-aws.md
title: ACL_ENABLED Error on Delta Writes
description: A DELTA_METADATA_MISMATCH sub-error that occurs when Table ACLs are enabled on a cluster, preventing automatic schema migration and requiring ALTER TABLE commands instead.
tags:
  - delta-lake
  - acl
  - security
  - error-handling
timestamp: "2026-06-18T15:21:38.421Z"
---

```yaml
---
title: ACL_ENABLED Error on Delta Writes
summary: A sub-error of DELTA_METADATA_MISMATCH that occurs when trying to automatically migrate the schema of a Delta table on a cluster where table ACLs are enabled.
sources:
  - delta_metadata_mismatch-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T08:07:27.979Z"
updatedAt: "2026-06-18T08:07:27.979Z"
tags:
  - error
  - delta
  - acl
  - schema-migration
aliases:
  - acl-enabled-error-on-delta-writes
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# ACL_ENABLED Error on Delta Writes

The **ACL_ENABLED Error on Delta Writes** is a sub‑error of the `DELTA_METADATA_MISMATCH` error condition (SQLSTATE: 42KDG) that occurs when a write operation attempts to automatically migrate the schema of a [[Delta Lake]] table, but the cluster has table ACLs (access control lists) enabled. Automatic schema migration is blocked in this configuration to enforce security policies. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Error Message

When the error is raised, Databricks returns the following explanation:

> Table ACLs are enabled in this cluster, so automatic schema migration is not allowed. Please use the `ALTER TABLE` command for changing the schema.

^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Cause

The error is triggered when a DataFrame write operation (e.g., `df.write.mode("append").saveAsTable(...)`) would require a schema evolution—such as adding new columns—but the cluster is running with table ACLs enabled. Databricks disables automatic schema migration under table ACLs to prevent unintended or unauthorized schema changes that could affect column‑level permissions. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Solution

To resolve the error, use the `ALTER TABLE` command to explicitly modify the table’s schema before writing. For example, to add a new column:

```sql
ALTER TABLE <table_name> ADD COLUMNS (<new_column> <data_type>);
```

After the schema is updated via `ALTER TABLE`, the write operation will succeed because the schema already matches. ^[delta_metadata_mismatch-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_METADATA_MISMATCH Error Class|DELTA_METADATA_MISMATCH — The parent error class containing other sub‑errors such as `SCHEMA_MISMATCH`, `PARTITIONING_MISMATCH`, and `ENABLE_LIQUID`.
- Schema evolution in Delta Lake — Best practices for evolving table schemas safely.
- Table ACLs — How access control lists interact with schema changes in Databricks.
- [[overwriteSchema Option|Overwrite schema option]] — Alternative approach using `.option("overwriteSchema", "true")` for scenarios without ACL restrictions.

## Sources

- delta_metadata_mismatch-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_metadata_mismatch-error-condition-databricks-on-aws.md](/references/delta_metadata_mismatch-error-condition-databricks-on-aws-7ce7a126.md)
