---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a3498348f3972b35fb9ae9d469679314d47753e5b90220228521613e5c964810
  pageDirectory: concepts
  sources:
    - restore-databricks-on-aws.md
    - tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
    - what-is-delta-lake-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - delta-lake-time-travel
    - DLTT
    - Delta Time Travel
    - Delta time travel
    - TIME TRAVEL
    - Time Travel
    - Time Travel Queries
    - Time travel
    - Time travel queries
    - time travel
    - time travel queries
  citations:
    - file: tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
    - file: what-is-delta-lake-in-databricks-databricks-on-aws.md
    - file: restore-databricks-on-aws.md
title: Delta Lake Time Travel
description: Ability to query, restore, or access previous versions of a Delta table using timestamps or version numbers
tags:
  - delta-lake
  - time-travel
  - versioning
timestamp: "2026-06-19T20:14:23.720Z"
---

## Delta Lake Time Travel

**Delta Lake Time Travel** is a feature that allows users to query, inspect, or restore a [Delta Lake Table](/concepts/delta-lake-table.md) to any previous version. Each write operation on a Delta table creates a new, immutable version, and the transaction log records provenance information for every version. Time travel leverages this version history to provide point-in-time access to the data without requiring separate backups. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md, what-is-delta-lake-in-databricks-databricks-on-aws.md]

### How Time Travel Works

Delta Lake assigns an integer version number to every write (including operations like `INSERT`, `UPDATE`, `DELETE`, `MERGE`, and `OPTIMIZE`). The transaction log also stores a timestamp for each version. Time travel can target a table state using either a **version number** or a **timestamp**. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

For timestamps, only date or timestamp strings are accepted. For example, strings must be formatted as `"2026-01-05T22:43:15.000+00:00"` or `"2026-01-05 22:43:15"`. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

### Querying Previous Versions

To query an older snapshot of a [Delta Lake Table](/concepts/delta-lake-table.md), you can use the DataFrameReader options `versionAsOf` or `timestampAsOf` in Python (or equivalent Scala/DataFrame APIs). The following Python example queries version `0` and a specific timestamp of the `workspace.default.people_10k` table: ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

```python
# Query using the version number.
df = spark.read.option('versionAsOf', 0).table("workspace.default.people_10k")

# Query using the timestamp.
df = spark.read.option('timestampAsOf', '2026-01-05T23:09:47.000+00:00').table("workspace.default.people_10k")
```

You can also use the `DeltaTable.history()` method (or the `DESCRIBE HISTORY` SQL statement) to retrieve version numbers and timestamps for each write to the table. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

```python
deltaTable = DeltaTable.forName(spark, "workspace.default.people_10k")
deltaHistory = deltaTable.history()

# Query using the version number.
display(deltaHistory.where("version == 0"))

# Query using the timestamp.
display(deltaHistory.where("timestamp == '2026-01-05T23:09:47.000+00:00'"))
```

### Restoring a Table to a Previous Version

The `RESTORE TABLE` SQL command permanently reverts a [Delta Lake Table](/concepts/delta-lake-table.md) to a specific version or timestamp. After a restore, the table’s current state is replaced by the targeted historical state. The command returns statistics such as the number of files removed and restored. ^[restore-databricks-on-aws.md]

```sql
-- Restore the employee table to a specific timestamp
RESTORE TABLE employee TO TIMESTAMP AS OF '2022-08-02 00:00:00';

-- Restore the employee table to a specific version number
RESTORE TABLE employee TO VERSION AS OF 1;

-- Restore the employee table to the state it was in an hour ago
RESTORE TABLE employee TO TIMESTAMP AS OF current_timestamp() - INTERVAL '1' HOUR;
```

### Limitations and Retention

Time travel is only available for versions whose underlying data files still exist in storage. The `VACUUM` operation physically removes old data files that are no longer referenced by the latest table version. Running `VACUUM` permanently deletes the data for those historical versions, making time travel to any version older than the retention threshold impossible. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

> **Important**: Deletion removes the data from the latest version but does not remove it from physical storage until old versions are explicitly vacuumed. ^[tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md]

### Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Table History|DESCRIBE HISTORY](/concepts/describe-history.md)
- Vacuum|VACUUM
- RESTORE|RESTORE TABLE
- [ACID Transactions](/concepts/delta-acid-transactions.md)

### Sources

- restore-databricks-on-aws.md
- tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md
- what-is-delta-lake-in-databricks-databricks-on-aws.md

# Citations

1. [tutorial-create-and-manage-delta-lake-tables-databricks-on-aws.md](/references/tutorial-create-and-manage-delta-lake-tables-databricks-on-aws-481179d7.md)
2. [what-is-delta-lake-in-databricks-databricks-on-aws.md](/references/what-is-delta-lake-in-databricks-databricks-on-aws-49c98a82.md)
3. [restore-databricks-on-aws.md](/references/restore-databricks-on-aws-b92cad28.md)
