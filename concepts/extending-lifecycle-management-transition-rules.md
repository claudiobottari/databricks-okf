---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3670c679592dd926b2e092b04ea7b75f36bb3fab5341e58e69264d1b76525fd5
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - extending-lifecycle-management-transition-rules
    - ELMTR
    - Lifecycle Management Transition Rule
    - Lifecycle management transition rule
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Extending lifecycle management transition rules
description: "A risk scenario: extending the cloud archival interval without caution may cause errors because cloud providers do not auto-restore already-archived files."
tags:
  - databricks
  - delta-lake
  - archival
  - lifecycle
timestamp: "2026-06-19T22:07:50.722Z"
---

# Extending Lifecycle Management Transition Rules

**Extending lifecycle management transition rules** refers to increasing the time interval before files are moved to archival storage in a cloud object store (e.g., changing from 60 days to 90 days). When you extend the rule, you must also update the corresponding Delta table property `delta.timeUntilArchived` to match the new interval. However, because cloud providers do not automatically restore files from archived storage when a retention policy is changed, files that were already archived under the old rule remain archived—even though they are now younger than the new archival threshold. This mismatch can lead to query errors unless handled carefully. ^[archival-support-in-databricks-databricks-on-aws.md]

## The Core Problem

When the archival interval is extended, files that were eligible for archival under the previous rule have already been moved to an archival storage tier. Once the rule is extended, those files are no longer considered eligible for archival by the policy, but they are still physically archived. Databricks determines whether a file is archived based on its creation time relative to the `delta.timeUntilArchived` setting. If you update that setting to the new interval immediately, Databricks will treat the already-archived files as unarchived and attempt to read them, resulting in errors because the files remain in cold storage. ^[archival-support-in-databricks-databricks-on-aws.md]

The source warns: **never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data.** ^[archival-support-in-databricks-databricks-on-aws.md]

## Example Scenario

Consider a table with a life‑cycle policy that originally archived files older than 60 days. The policy is then extended to 90 days. At the moment the change is made:

- All files between 60 and 90 days old are already archived.
- For the next 30 days, no new files reach the 90‑day threshold, so no new archiving occurs.
- After 30 days, the policy correctly describes the archived data (files older than 90 days), but the files that were archived during the interval between 60 and 90 days remain inaccessible unless restored.

If you simply set `delta.timeUntilArchived` to `90 days` immediately after the policy change, Databricks would treat files with creation times between 60 and 90 days as unarchived, but those files are still in archive storage—queries that need them will fail. ^[archival-support-in-databricks-databricks-on-aws.md]

## Approaches to Avoid Errors

During the lag period between the old archival threshold and the new threshold, you can choose one of the following approaches:

### Approach 1: Keep the Old Threshold Until the New One Is Fully Effective

Leave `delta.timeUntilArchived` at the old value (e.g., 60 days) until enough time has passed for all files that were archived under the old rule to now be correctly covered by the new rule. In the example above, you would keep the setting at 60 days for the first 30 days. During this period, Databricks treats files older than 60 days as archived. Some of those files have actually been archived (the ones between 60 and 90 days), but some have not yet been archived (they are still waiting to reach the new 90‑day threshold). This means you may ignore some data files that could be queried, but you avoid errors. After 30 days, when the oldest unarchived files are exactly 90 days old, you can safely update `delta.timeUntilArchived` to `90 days`. ^[archival-support-in-databricks-databricks-on-aws.md]

### Approach 2: Incrementally Update the Threshold Each Day

If you need to access all data in the hot tier without ignoring any files, you can update `delta.timeUntilArchived` each day to reflect the current interval during the lag period. For example, 7 days after the policy change, the actual age of all archived data is 67 days (the original 60‑day threshold plus the 7 days since the change). Setting `delta.timeUntilArchived` to `67 days` accurately reflects which files are archived. This approach requires daily adjustments until the new threshold is reached. ^[archival-support-in-databricks-databricks-on-aws.md]

## Important Notes

- Updating the `delta.timeUntilArchived` property changes only which files Databricks treats as archived; it does not change which files are actually archived in the cloud storage. The underlying cloud lifecycle policy is independent of the table property. ^[archival-support-in-databricks-databricks-on-aws.md]
- The scenario described above assumes a fixed lifecycle policy extension. If the policy is shortened (less time before archival), updating the property to match the new interval works normally because no files are unexpectedly unarchived from Databricks’ perspective. ^[archival-support-in-databricks-databricks-on-aws.md]
- Extending the lifecycle management transition rule **without following one of the recommended approaches** is listed as a limitation that results in unexpected behavior. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) – The overall feature for using cloud‑based life‑cycle policies on Delta tables.
- [delta.timeUntilArchived](/concepts/deltatimeuntilarchived.md) – The table property that controls how old a file must be before Databricks considers it archived.
- Lifecycle management transition rule – The cloud object‑store rule that defines when files transition to archival storage.
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) – Syntax to identify which files must be restored.
- Restore archived files – Process for making archived files available again.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
