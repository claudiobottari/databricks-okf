---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 963ac846f03ac955df64e35e48b38add3033911e37b45cf56b8fcbdaeffd90e8
  pageDirectory: concepts
  sources:
    - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - version_mismatch
    - VERSION_MISMATCH
  citations:
    - file: delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
title: VERSION_MISMATCH
description: Sub-error indicating the managed and external DeltaLog versions do not match, often due to a concurrent UNSET MANAGED command
tags:
  - databricks
  - error-message
  - concurrency
timestamp: "2026-06-19T18:22:07.719Z"
---

```markdown
---
title: VERSION_MISMATCH
summary: A cause of DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED indicating a version conflict between the managed and external Delta logs, often due to a concurrent UNSET MANAGED operation.
sources:
  - delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T11:49:39.865Z"
updatedAt: "2026-06-19T15:01:25.284Z"
tags:
  - error-message
  - databricks
  - concurrency
  - version-conflict
aliases:
  - version_mismatch
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# VERSION_MISMATCH

**VERSION_MISMATCH** is a sub-condition of the DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class (SQLSTATE 42809). It is raised by `ALTER TABLE ... UNSET MANAGED` when the versions of the managed DeltaLog and the external DeltaLog do not match. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Error Message

The error message includes the actual and expected version numbers:

```
The versions of the managed DeltaLog (<managedDeltaLogVersion>) and external DeltaLog (<externalDeltaLogVersion>) do not match.
```

^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Cause

This error occurs when a concurrent `ALTER TABLE ... UNSET MANAGED` command has already successfully rolled back the table from a managed to an external state. Because the metadata versions of the table's DeltaLog have advanced, the second command sees a version mismatch. ^[delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md]

## Related Concepts

- DELTA_ALTER_TABLE_UNSET_MANAGED_FAILED error class — The parent error class containing this condition.
- [[ALTER TABLE UNSET MANAGED command|ALTER TABLE UNSET MANAGED]] — The SQL command that triggers this error.
- External Table — The target table type after a successful rollback.
- [[Unity Catalog Managed Tables|Managed Table]] — The source table type before rollback.
- DeltaLog — The transaction log that stores table metadata versions.

## Sources

- delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md
```

# Citations

1. [delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws.md](/references/delta_alter_table_unset_managed_failed-error-condition-databricks-on-aws-a24f2e75.md)
