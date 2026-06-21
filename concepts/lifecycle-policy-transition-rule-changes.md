---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c5422df735be97242d6d5fa50745c015a83451e21c638397fa255ffe9375ec1
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lifecycle-policy-transition-rule-changes
    - LPTRC
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Lifecycle Policy Transition Rule Changes
description: Procedures and risks associated with changing the cloud lifecycle management transition rule interval and keeping the delta.timeUntilArchived property in sync.
tags:
  - archival
  - lifecycle-management
  - configuration
  - cloud-storage
timestamp: "2026-06-19T09:02:21.373Z"
---

Here is the wiki page for "Lifecycle Policy Transition Rule Changes".

---

## Lifecycle Policy Transition Rule Changes

**Lifecycle Policy Transition Rule Changes** refer to the process of modifying the time-based rules that govern how cloud object storage (such as AWS S3) moves data to archive tiers, and the required steps to synchronize those changes with [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) for [Delta tables](/concepts/delta-lake-table.md). When you alter the lifecycle management transition rule in your cloud storage, you must also update the corresponding `delta.timeUntilArchived` table property to maintain consistency and avoid errors. ^[archival-support-in-databricks-databricks-on-aws.md]

### Shortening the Transition Interval

If you change the lifecycle policy to shorten the time before files are archived (i.e., less time since file creation), archival support for the Delta table continues functioning normally after the table property is updated. ^[archival-support-in-databricks-databricks-on-aws.md]

### Extending the Transition Interval

If you change the lifecycle policy to extend the time before files are archived (i.e., add more time before archival is triggered), updating the `delta.timeUntilArchived` property to the new value can lead to errors. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means that files previously eligible for archival but now not considered eligible for archival are still archived. ^[archival-support-in-databricks-databricks-on-aws.md]

**Important:** To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

#### Example Scenario: Extending from 60 to 90 Days

Consider a scenario in which the time interval for archival is changed from 60 days to 90 days:

1. All records between 60 and 90 days old are archived when the policy changes.
2. For 30 days, no new files are archived (the oldest non-archived files are 60 days old when the policy is extended).
3. After 30 days, the lifecycle policy correctly describes all archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

The `delta.timeUntilArchived` setting tracks the set time interval against the file creation time recorded by the Delta transaction log. It does not have explicit knowledge of the underlying policy. During the lag period between the old archival threshold and the new archival threshold, you can take one of the following approaches to avoid querying archived files: ^[archival-support-in-databricks-databricks-on-aws.md]

#### Approach 1: Keep the Old Setting Temporarily

You can leave the setting `delta.timeUntilArchived` with the old threshold until enough time has passed for all files to be archived. Following the example above, each day for the first 30 days, another day's worth of data would be considered archived by Databricks but still needs to be archived by the cloud provider. This does not result in an error but ignores some data files that could be queried. After 30 days, update the `delta.timeUntilArchived` to `90 days`. ^[archival-support-in-databricks-databricks-on-aws.md]

#### Approach 2: Daily Incremental Updates

You can update the setting `delta.timeUntilArchived` each day to reflect the current interval during the lag period. While the cloud policy is set to 90 days, the actual age of archived data changes in real-time. For example, after 7 days, setting `delta.timeUntilArchived` to `67 days` accurately reflects the age of all archived data files. This approach is only necessary if you must access all data in hot tiers. ^[archival-support-in-databricks-databricks-on-aws.md]

**Note:** Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived. ^[archival-support-in-databricks-databricks-on-aws.md]

### Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The feature that enables Databricks to work with archived cloud storage.
- [Delta timeUntilArchived](/concepts/deltatimeuntilarchived.md) — The table property that sets the archival time threshold.
- [Show archived files](/concepts/show-archived-files-syntax.md) — The command to identify archived files.
- Restore archived files — The process to restore files from archive for queries.

### Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
