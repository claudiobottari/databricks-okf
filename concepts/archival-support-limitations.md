---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 59241a690b4e28263f8583c53acecf4cd6e623535917706fd3bffeb8c42acd25
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - archival-support-limitations
    - ASL
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Archival support limitations
description: The documented restrictions on Delta Lake archival support including inapplicability to transaction logs, exclusion of non-creation-time-based policies, and unsupported operations on archived data.
tags:
  - delta-lake
  - archival
  - limitations
timestamp: "2026-06-18T14:27:00.010Z"
---

# Archival Support Limitations

**Archival support limitations** refers to the constraints and behaviors of Databricks' archival support feature for [Delta Lake](/concepts/delta-lake.md) tables when using cloud-based lifecycle policies on object storage. This feature is in Public Preview for Databricks Runtime 13.3 LTS and above.

## Transaction Log Requirements

Archival support applies only to data files. If any files in the Delta transaction log (`_delta_log/` directory) are moved to an archived storage tier, the table becomes entirely inaccessible and all queries against the table fail. You must configure your cloud lifecycle policy so that the `_delta_log/` path is not included in archival. ^[archival-support-in-databricks-databricks-on-aws.md]

## Lifecycle Policy Constraints

No support exists for lifecycle management policies that are not based on file creation time. This includes access-time-based policies and tag-based policies. ^[archival-support-in-databricks-databricks-on-aws.md]

Extending the lifecycle management transition rule (making files archive later) results in unexpected behavior. Cloud providers do not automatically restore files from archived storage when data retention policies are changed, so files previously archived but now not considered eligible for archival remain archived. ^[archival-support-in-databricks-databricks-on-aws.md]

## LIMIT Query Restrictions

`LIMIT` queries on tables with archival support enabled do not trigger sampling for restored data. If a table's data is restored, most queries succeed when querying restored data, but a `LIMIT` query returns a `DELTA_ARCHIVED_FILES_IN_LIMIT` error. ^[archival-support-in-databricks-databricks-on-aws.md]

If you get the error "Not enough files to satisfy LIMIT", your table does not have enough data rows in unarchived files to satisfy the number of records specified by `LIMIT`. Lower the `LIMIT` clause to find enough unarchived rows to meet the specified `LIMIT`. ^[archival-support-in-databricks-databricks-on-aws.md]

## DDL and Maintenance Operations

You cannot use `DROP COLUMN` on a table with archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

`REORG TABLE APPLY PURGE` makes a best-effort attempt, but only works on deletion vector files and referenced data files that are not archived. `PURGE` cannot delete archived deletion vector files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Extending the Lifecycle Rule

If the time interval before archival is extended (to add more time before archival is triggered), updating the property `delta.timeUntilArchived` to the new value can lead to errors. To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

During the lag period between the old archival threshold and the new archival threshold, you can take one of the following approaches to avoid querying archived files: ^[archival-support-in-databricks-databricks-on-aws.md]

- Leave the setting `delta.timeUntilArchived` with the old threshold until enough time has passed for all files to be archived. This ignores some data files that could be queried but does not result in an error.
- Update the setting `delta.timeUntilArchived` each day to reflect the current interval during the lag period.

Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived. ^[archival-support-in-databricks-databricks-on-aws.md]

## Compute Environment Constraints

Archival support relies entirely on compatible Databricks compute environments and only works for Delta tables. Configuring archival support does not change behavior, compatibility, or support in OSS Delta Lake clients or Databricks Runtime 12.2 LTS and below. ^[archival-support-in-databricks-databricks-on-aws.md]

## S3 Intelligent-Tiering Incompatibility

Amazon S3 Intelligent-Tiering optional asynchronous archive access tiers is not compatible with archival support in Databricks because it archives based on access time rather than file creation time. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Delta Lake](/concepts/delta-lake.md) — The storage layer that archival support operates on
- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The feature overview and setup
- [Delta transaction log](/concepts/delta-transaction-log.md) — The critical log directory that must not be archived
- Lifecycle Management Policies — Cloud-based rules for transitioning data to archival tiers

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
