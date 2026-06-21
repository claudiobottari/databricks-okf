---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b9988e03c5184574891b35ac208a7409f67f04f5b89e9a24281a676803231685
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lifecycle-policy-extension-problem
    - LPEP
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Lifecycle Policy Extension Problem
description: The risk and complications that arise when extending the cloud lifecycle management transition rule to a longer interval, due to the mismatch between the table property and actual archival state during the lag period.
tags:
  - databricks
  - archival
  - lifecycle-management
  - risk
timestamp: "2026-06-19T14:03:13.999Z"
---

# Lifecycle Policy Extension Problem

The **Lifecycle Policy Extension Problem** occurs when a cloud storage lifecycle management transition rule's archival interval is extended (lengthened) without correspondingly updating the `delta.timeUntilArchived` table property, leading to potential query failures on [Delta Lake](/concepts/delta-lake.md) tables with [Archival Support in Databricks](/concepts/archival-support-in-databricks.md).

## Cause

When the time interval before archival is extended — for example, changing from 60 days to 90 days — cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means that files previously eligible for archival (under the old shorter interval) remain archived even though they are no longer considered eligible under the new longer interval. ^[archival-support-in-databricks-databricks-on-aws.md]

## Risk

If the property `delta.timeUntilArchived` is updated to the new, longer value immediately after changing the cloud lifecycle policy, Databricks will assume those files are available in hot storage when they are in fact still archived. This mismatch can lead to query failures because Databricks attempts to read files that remain in archival storage. ^[archival-support-in-databricks-databricks-on-aws.md]

## Prevention

To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md]

## Mitigation Strategies

During the lag period between the old archival threshold and the new archival threshold, two approaches are available: ^[archival-support-in-databricks-databricks-on-aws.md]

### Option 1: Maintain the Old Threshold Temporarily

Leave the setting `delta.timeUntilArchived` with the old threshold until enough time has passed for all files to be archived under the new policy. ^[archival-support-in-databricks-databricks-on-aws.md]

For example, if the archival interval changes from 60 days to 90 days:
- For the first 30 days, leave `delta.timeUntilArchived` at `60 days`. Each day during this period, another day's worth of data would be considered archived by Databricks but still needs to be archived by the cloud provider. This does not result in an error but ignores some data files that could be queried.
- After 30 days, update `delta.timeUntilArchived` to `90 days`. ^[archival-support-in-databricks-databricks-on-aws.md]

### Option 2: Daily Incremental Updates

Update the setting `delta.timeUntilArchived` each day to reflect the current actual age of archived data during the lag period. ^[archival-support-in-databricks-databricks-on-aws.md]

For example, while the cloud policy is set to 90 days, the actual age of archived data changes in real-time. After 7 days from the policy change, setting `delta.timeUntilArchived` to `67 days` accurately reflects the age of all archived data files. This approach is only necessary if you must access all data in hot tiers. ^[archival-support-in-databricks-databricks-on-aws.md]

## Important Note

Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived. The table property and the cloud lifecycle policy are separate settings — changes to one do not affect the other. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The feature enabling cloud-based lifecycle policies on Delta tables
- [Delta Lake](/concepts/delta-lake.md) — The underlying storage format for archival support
- [Lifecycle Management Transition Rule](/concepts/extending-lifecycle-management-transition-rules.md) — The cloud storage policy that governs file archival
- [delta.timeUntilArchived](/concepts/deltatimeuntilarchived.md) — The table property that tells Databricks to ignore files older than the specified period

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
