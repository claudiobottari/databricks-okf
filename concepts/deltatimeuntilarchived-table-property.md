---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 08ca946a5322f5fcf41b3020a92e1c1a2a93336ce2cb8fceed26065c8ab29575
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - deltatimeuntilarchived-table-property
    - DTP
    - delta.timeUntilArchived Property
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 24
      end: 27
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 89
      end: 91
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 91
      end: 92
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 52
      end: 54
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 42
      end: 47
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 72
      end: 73
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 99
      end: 101
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 105
      end: 109
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 115
      end: 124
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 85
      end: 86
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 95
      end: 96
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 93
      end: 93
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 94
      end: 94
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 64
      end: 65
title: delta.timeUntilArchived table property
description: A Delta table property that specifies the archival threshold, telling Databricks to ignore files older than a given duration.
tags:
  - databricks
  - delta-lake
  - archival
  - configuration
timestamp: "2026-06-19T22:07:33.547Z"
---

# `delta.timeUntilArchived` Table Property

The `delta.timeUntilArchived` table property is a Delta Lake configuration setting on Databricks that specifies the archival interval for data files. When set, it tells Databricks to ignore files older than the specified period, assuming they have been moved to an archival storage tier by the cloud's lifecycle management policy. This property is the key enabler of [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) and must be manually kept in sync with the underlying cloud lifecycle transition rule. ^[archival-support-in-databricks-databricks-on-aws.md]

## Requirements

- Requires Databricks Runtime 13.3 LTS or above (Public Preview).
- Only compatible with Delta tables.
- The cloud lifecycle policy must archive data files to S3 Glacier Deep Archive or Glacier Flexible Retrieval. Amazon S3 Glacier Instant Retrieval does not require setting this property, but queries may retrieve all scanned files. ^[archival-support-in-databricks-databricks-on-aws.md:24-27]
- The Delta transaction log (`_delta_log/` directory) must **never** be archived; archiving it makes the table entirely inaccessible. ^[archival-support-in-databricks-databricks-on-aws.md:89-91]
- Lifecycle policies based on access time or tags are not supported — only file creation time policies are compatible. ^[archival-support-in-databricks-databricks-on-aws.md:91-92]

## Setting `delta.timeUntilArchived`

Use the `ALTER TABLE` SQL command to set the property:

```sql
ALTER TABLE <table_name> SET TBLPROPERTIES(delta.timeUntilArchived = 'X days');
```

Where `X` is the number of days after file creation that the cloud lifecycle policy archives files. Setting this property does **not** create or alter the cloud lifecycle policy; it only tells Databricks which files to treat as archived. ^[archival-support-in-databricks-databricks-on-aws.md:52-54]

## How It Affects Queries

When `delta.timeUntilArchived` is set, Databricks avoids reading files older than the specified period unless a query can be answered without them. Queries that require data from archived files fail early with an informative error message. Queries that can be satisfied by metadata only, or by files that are not archived, succeed normally. ^[archival-support-in-databricks-databricks-on-aws.md:42-47]

To identify which archived files must be restored to complete a given query, use `SHOW ARCHIVED FILES`. See [Show archived files (Delta Lake)](/concepts/show-archived-files-syntax.md). ^[archival-support-in-databricks-databricks-on-aws.md:72-73]

## Interaction with Lifecycle Policies

The value of `delta.timeUntilArchived` must be kept consistent with the actual cloud lifecycle management transition rule. If you shorten the archival interval (e.g., from 90 days to 60 days), update the property to the same value. ^[archival-support-in-databricks-databricks-on-aws.md:99-101]

If you extend the interval (e.g., from 60 days to 90 days), caution is required. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means files previously archived may still be in cold storage even though the new policy would not archive them yet. To avoid errors, never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md:105-109]

During the lag period between the old archival threshold and the new archival threshold, you can either:
1. Leave `delta.timeUntilArchived` at the old threshold until enough time has passed for all files to be archived at the new threshold, then update it.
2. Update the setting daily to reflect the current actual age of archived data during the lag period. ^[archival-support-in-databricks-databricks-on-aws.md:115-124]

## Limitations

- `MERGE`, `UPDATE`, or `DELETE` operations fail if they impact data in archived files. You must restore data first using `SHOW ARCHIVED FILES` to identify files to restore. ^[archival-support-in-databricks-databricks-on-aws.md:85-86]
- `LIMIT` queries on tables with this property set do not trigger sampling for restored data; if archived files exist, the query may return a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. ^[archival-support-in-databricks-databricks-on-aws.md:95-96]
- `DROP COLUMN` cannot be used on a table with archived files. ^[archival-support-in-databricks-databricks-on-aws.md:93]
- `REORG TABLE APPLY PURGE` makes a best-effort attempt but only works on files that are not archived. ^[archival-support-in-databricks-databricks-on-aws.md:94]
- The property only supports lifecycle policies based on file creation time, not access time or tags. ^[archival-support-in-databricks-databricks-on-aws.md:91-92]
- Archival support relies entirely on compatible Databricks compute environments and only works for Delta tables. It does not change behavior for OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below. ^[archival-support-in-databricks-databricks-on-aws.md:64-65]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md)
- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md)
- [Show archived files (Delta Lake)](/concepts/show-archived-files-syntax.md)
- Cloud lifecycle policies
- S3 Glacier storage classes

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
2. [archival-support-in-databricks-databricks-on-aws.md:24-27](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
3. [archival-support-in-databricks-databricks-on-aws.md:89-91](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
4. [archival-support-in-databricks-databricks-on-aws.md:91-92](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
5. [archival-support-in-databricks-databricks-on-aws.md:52-54](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
6. [archival-support-in-databricks-databricks-on-aws.md:42-47](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
7. [archival-support-in-databricks-databricks-on-aws.md:72-73](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
8. [archival-support-in-databricks-databricks-on-aws.md:99-101](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
9. [archival-support-in-databricks-databricks-on-aws.md:105-109](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
10. [archival-support-in-databricks-databricks-on-aws.md:115-124](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
11. [archival-support-in-databricks-databricks-on-aws.md:85-86](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
12. [archival-support-in-databricks-databricks-on-aws.md:95-96](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
13. [archival-support-in-databricks-databricks-on-aws.md:93-93](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
14. [archival-support-in-databricks-databricks-on-aws.md:94-94](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
15. [archival-support-in-databricks-databricks-on-aws.md:64-65](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
