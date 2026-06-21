---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 35f10ed53e2e8d2bc0ab6c9088318341058a9833a08ef2a4ed3eefb6a139fedc
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - delta-transaction-log-archival-prohibition
    - DTLAP
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Delta transaction log archival prohibition
description: The Delta transaction log (_delta_log/) must never be archived by cloud lifecycle policies, or the table becomes entirely inaccessible.
tags:
  - databricks
  - delta-lake
  - archival
  - transaction-log
timestamp: "2026-06-19T22:07:49.195Z"
---

# Delta Transaction Log Archival Prohibition

The **Delta transaction log archival prohibition** is a hard constraint that applies to any [Delta Lake](/concepts/delta-lake.md) table for which [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) has been configured on cloud object storage. Under this rule, no file within the `_delta_log/` directory may be moved to an archived storage tier. If any transaction log file is archived, the table becomes entirely inaccessible and all queries against the table fail. ^[archival-support-in-databricks-databricks-on-aws.md]

## Why the Log Must Not Be Archived

Databricks archival support enables the use of cloud-based lifecycle policies on object storage containing Delta tables. When a table has archival support enabled, Databricks can ignore data files older than the configured `delta.timeUntilArchived` period. However, this optimization depends on the transaction log remaining fully readable. The Delta transaction log contains the metadata, commit history, and statistics that Databricks uses to plan and execute queries. If any log file is moved to an archived tier, Databricks cannot read the table's metadata and the table becomes completely inaccessible — not just for queries that touch old data, but for any query whatsoever. ^[archival-support-in-databricks-databricks-on-aws.md]

## Consequences of Violation

If a cloud lifecycle policy moves files from the `_delta_log/` directory to an archival storage tier such as S3 Glacier Deep Archive or Glacier Flexible Retrieval:

- The table becomes entirely inaccessible.
- All queries against the table fail.
- No workaround exists to restore access without first returning the archived transaction log files to a fast-retrieval storage tier.

This is fundamentally different from the behavior for archived data files, which only cause failures for queries that must scan those files. Archived log files cause a total table outage. ^[archival-support-in-databricks-databricks-on-aws.md]

## Prevention

### Cloud Lifecycle Policy Exclusion

You must configure your cloud lifecycle policy so that the `_delta_log/` path prefix is explicitly excluded from archival. This is a configuration on the cloud provider side, not a Databricks setting. For S3, this means adding an exclusion filter in the lifecycle rule for the `_delta_log/` prefix. See AWS documentation on [S3 Lifecycle configuration examples](https://docs.aws.amazon.com/AmazonS3/latest/userguide/lifecycle-configuration-examples.html). ^[archival-support-in-databricks-databricks-on-aws.md]

### Verification

After setting up lifecycle policies, verify that the Delta transaction log directory is accessible by running a simple query against the table. If the query succeeds, the log is not archived.

## Related Restrictions

The archival prohibition on the transaction log is one of several limitations that apply to Delta tables with archival support enabled:

- Archival support applies only to data files, not transaction log files.
- No support exists for lifecycle policies that are not based on file creation time, including access-time-based policies and tag-based policies.
- Extending the lifecycle management transition rule (making the interval longer) can lead to errors because cloud providers do not automatically restore previously archived files. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The broader feature that enables ignoring archived data files
- [Delta transaction log](/concepts/delta-transaction-log.md) — The metadata directory that must remain accessible
- [delta.timeUntilArchived](/concepts/deltatimeuntilarchived.md) — The table property that controls which files Databricks treats as archived
- S3 lifecycle policies — Cloud-native mechanisms for transitioning objects to archival tiers
- Delta Lake table storage — The overall structure of data and log files in a Delta table

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
