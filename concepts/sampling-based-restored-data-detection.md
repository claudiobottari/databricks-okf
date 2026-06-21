---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 07a2d97b26f5f035f1ddd0e83a418fd8e9ddda8f3f69728d2bf2c2ebb3907bc5
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.94
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sampling-based-restored-data-detection
    - SRDD
    - RDD
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Sampling-based restored data detection
description: Databricks samples files presumed archived to detect whether they have been restored; if sampling indicates restoration, it assumes all files are available.
tags:
  - databricks
  - delta-lake
  - archival
  - optimization
timestamp: "2026-06-19T22:07:46.083Z"
---

---
title: Sampling-based restored data detection
summary: The mechanism by which Databricks samples older files to determine whether archived data has been restored from cold storage tiers before planning a scan.
sources:
  - archival-support-in-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:47:29.305Z"
updatedAt: "2026-06-18T10:47:29.305Z"
tags:
  - archival
  - delta-lake
  - databricks
  - query-optimization
aliases:
  - sampling-based-restored-data-detection
  - SRDD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Sampling-based restored data detection

**Sampling-based restored data detection** is a mechanism used by [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) to determine whether files that are presumed to be archived have been restored to a fast-retrieval storage tier. It avoids directly accessing archived objects and allows queries to proceed when restored files are present. ^[archival-support-in-databricks-databricks-on-aws.md]

## How sampling works

When Databricks prepares a scan over a [Delta table](/concepts/delta-lake-table.md) with archival support enabled, it samples files older than the specified `delta.timeUntilArchived` retention period that are required by the query. The sampling checks whether those files have been restored from archival storage. If the results indicate that the sampled files—presumed to be archived—have been restored, Databricks assumes that *all* files needed for the query have been restored, and the query processes normally. In that case, the results include data from the files that were previously marked for archival. ^[archival-support-in-databricks-databricks-on-aws.md]

## Behavior without lifecycle policies

If archival support is enabled (by setting `delta.timeUntilArchived`) but no lifecycle policies are configured on the underlying cloud object storage, the sampling logic still applies. Queries succeed, and the results include data from the files that are marked for archival under the property. ^[archival-support-in-databricks-databricks-on-aws.md]

## Limitations

Sampling-based detection does **not** apply to all queries. In particular, `LIMIT` queries on tables with archival support enabled do **not** trigger sampling for restored data. If the table’s data has been restored, most queries succeed when querying restored data, but a `LIMIT` query returns the error `DELTA_ARCHIVED_FILES_IN_LIMIT`. This is because `LIMIT` cannot guarantee that enough unarchived rows exist to satisfy the requested count without scanning archived files. If you encounter the error “Not enough files to satisfy LIMIT”, your table does not have enough unarchived rows; lower the `LIMIT` clause to find enough unarchived rows. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The feature that uses sampling for restored data detection.
- [Delta Lake](/concepts/delta-lake.md) — The storage format to which archival support applies.
- [Delta transaction log](/concepts/delta-transaction-log.md) — Must not be archived; if it is, the table becomes inaccessible.
- Lifecycle management transition rule — The cloud policy that determines when files are archived; changes require updating `delta.timeUntilArchived`.
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) — A command that returns URIs for archived files that must be restored to complete a query.
- Restore archived files — The process of restoring files to a fast-retrieval tier using cloud provider APIs.
- LIMIT clause — SQL clause that is not compatible with sampling-based detection.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
