---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c2fecc25d58b200a238f0a12f928f0078234caf63575ef0f1c84365260a2cf57
  pageDirectory: concepts
  sources:
    - delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deletion-vector-constraints-for-iceberg-compat
    - DVCFIC
  citations:
    - file: delta_iceberg_compat_violation-error-condition-databricks-on-aws.md
title: Deletion Vector constraints for Iceberg compat
description: IcebergCompatV requires that Deletion Vectors be either disabled or fully purged from a Delta table before Uniform Iceberg compatibility can be enabled.
tags:
  - delta-lake
  - iceberg-compatibility
  - deletion-vectors
timestamp: "2026-06-19T10:06:20.021Z"
---

## Deletion Vector constraints for Iceberg compat

**Deletion Vector constraints for Iceberg compat** refer to the requirement that [Deletion Vectors](/concepts/deletion-vectors.md) must be fully disabled and purged from a table before the table can have IcebergCompat (IcebergCompatV7 version) enabled. Enabling IcebergCompat while Deletion Vectors are present causes a `DELTA_ICEBERG_COMPAT_VIOLATION` error with one of two sub‑error codes, depending on the state of the Deletion Vectors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Error sub‑conditions

| Error code | Meaning | Recommended action |
|------------|---------|-------------------|
| `DELETION_VECTORS_NOT_PURGED` | Deletion Vectors exist on the table but have not been fully purged. | Run `REORG TABLE APPLY (PURGE)` to remove the remaining Deletion Vectors. |
| `DELETION_VECTORS_SHOULD_BE_DISABLED` | The Deletion Vectors feature is still enabled on the table. | Disable Deletion Vectors first, then run `REORG TABLE APPLY (PURGE)` to purge any existing Deletion Vectors. |

Both errors require the same end state: Deletion Vectors must be both **disabled** (feature toggled off) and **purged** (all existing vector files removed). The error message identifies which step is still outstanding. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Resolution steps

1. **Disable the Deletion Vectors feature** if it is currently enabled (use the appropriate `ALTER TABLE` command).  
2. **Purge any remaining Deletion Vectors** by executing:  
   `REORG TABLE APPLY (PURGE)`  

After these steps, the table will no longer have Deletion Vectors and the IcebergCompat version can be enabled without encountering the `DELETION_VECTORS_SHOULD_BE_DISABLED` or `DELETION_VECTORS_NOT_PURGED` errors. ^[delta_iceberg_compat_violation-error-condition-databricks-on-aws.md]

### Related concepts

- [IcebergCompat (Uniform Apache Iceberg)](/concepts/uniform-apache-iceberg-format.md)
- [Deletion Vectors](/concepts/deletion-vectors.md)
- [REORG TABLE command](/concepts/reorg-table-command.md)
- Delta table features
- DELTA_ICEBERG_COMPAT_VIOLATION error class

### Sources

- delta_iceberg_compat_violation-error-condition-databricks-on-aws.md

# Citations

1. [delta_iceberg_compat_violation-error-condition-databricks-on-aws.md](/references/delta_iceberg_compat_violation-error-condition-databricks-on-aws-206a4feb.md)
