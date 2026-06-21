---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a8c962bfd1c09109a44b916c378f9b39f01f91e4b847283ca35da76d2882154d
  pageDirectory: concepts
  sources:
    - describe-history-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - delta-table-provenance
    - DTP
  citations:
    - file: describe-history-databricks-on-aws.md
title: Delta Table Provenance
description: Metadata captured for every write operation on a Delta table, including operation type, user, and timestamp.
tags:
  - delta-lake
  - metadata
  - audit
timestamp: "2026-06-19T18:30:52.469Z"
---

```markdown
---
title: Delta Table Provenance
summary: Provenance metadata tracked per write operation on Delta tables, including operation type, user identity, and other details.
sources:
  - describe-history-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:12:25.098Z"
updatedAt: "2026-06-19T10:12:25.098Z"
tags:
  - delta-lake
  - governance
  - auditing
aliases:
  - delta-table-provenance
  - DTP
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Delta Table Provenance

**Delta Table Provenance** refers to the historical metadata automatically captured by [[Delta Lake]] for every write operation performed on a Delta table. This provenance information includes details such as the operation type, the user who performed it, and the timestamp. In Databricks, the `DESCRIBE HISTORY` SQL command is used to retrieve this history. ^[describe-history-databricks-on-aws.md]

## Syntax

```sql
DESCRIBE HISTORY table_name
```

^[describe-history-databricks-on-aws.md]

## Parameters

- **table_name**: The name of an existing Delta table. The name must not include a temporal specification or options specification. ^[describe-history-databricks-on-aws.md]

## Details

`DESCRIBE HISTORY` returns one row for each write to the table, including fields such as the operation (e.g., `WRITE`, `MERGE`, `DELETE`, `UPDATE`), the user, the timestamp, and other provenance metadata. Table history is retained for **30 days** by default. ^[describe-history-databricks-on-aws.md]

For more detailed guidance on working with table history, see Work with table history. Related commands include the `table_changes` function, which can be used to read the change data feed. ^[describe-history-databricks-on-aws.md]

## Related Concepts

- Work with table history
- table_changes function
- [[Delta Lake]]
- DESCRIBE DETAIL (for table metadata)

## Sources

- describe-history-databricks-on-aws.md
```

# Citations

1. [describe-history-databricks-on-aws.md](/references/describe-history-databricks-on-aws-c4aeec74.md)
