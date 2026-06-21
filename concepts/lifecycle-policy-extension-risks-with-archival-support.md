---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1db7823c5853ef02a8a8c49b24efa280c6786be9fcd962db79b8796e0834606f
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lifecycle-policy-extension-risks-with-archival-support
    - LPERWAS
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 101
      end: 104
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 105
      end: 113
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 114
      end: 122
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 115
      end: 117
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 118
      end: 121
    - file: archival-support-in-databricks-databricks-on-aws.md
      start: 123
      end: 125
title: Lifecycle policy extension risks with archival support
description: Extending the cloud lifecycle management transition rule (e.g., from 60 to 90 days) can cause errors because previously archived files are not automatically restored; delta.timeUntilArchived must never exceed the actual age of the most recently archived data.
tags:
  - databricks
  - delta-lake
  - lifecycle-management
  - risk
timestamp: "2026-06-18T10:47:49.425Z"
---

---
title: Lifecycle policy extension risks with archival support
summary: Risks and best practices when extending the archival retention interval in cloud lifecycle policies that affect Delta tables
sources:
  - archival-support-in-databricks-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:35:53.100Z"
updatedAt: "2026-06-18T10:35:53.100Z"
tags:
  - databricks
  - delta-lake
  - archival
  - lifecycle-policies
aliases:
  - lifecycle-policy-extension-risks
  - LPEX
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 1
---

# Lifecycle policy extension risks with archival support

**Lifecycle policy extension risks** with archival support occur when the time interval in a cloud object storage lifecycle management transition rule is extended — for example, from 60 days before archival to 90 days — and the corresponding Delta table property `delta.timeUntilArchived` is also updated to match. Cloud providers do not automatically restore files from archived storage when data retention policies are changed. This means that files that were previously eligible for archival and were actually archived remain in the archived storage tier, even though the new policy would not consider files of that age eligible for archival. ^[archival-support-in-databricks-databricks-on-aws.md#L101-L104]

## The core warning

> **Important**: To avoid errors, never set the property `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. ^[archival-support-in-databricks-databricks-on-aws.md#L101-L104]

## Example scenario

Consider a scenario where the cloud lifecycle policy originally archived files at 60 days old, and the policy is extended to 90 days: ^[archival-support-in-databricks-databricks-on-aws.md#L105-L113]

1. All records between 60 and 90 days old are already archived when the policy changes.
2. For the next 30 days, no new files are archived (the oldest non-archived files are 60 days old when the policy is extended).
3. After 30 days, the lifecycle policy correctly describes all archived data — but files that are 60 to 90 days old remain archived during that 30-day lag period.

During this lag period, `delta.timeUntilArchived` set to 90 days would cause Databricks to consider files aged 60–90 days as non-archived, but they are in fact still stored in an archival tier. This can lead to queries that attempt to scan those files and fail. ^[archival-support-in-databricks-databricks-on-aws.md#L105-L113]

## Workarounds

During the lag period between the old archival threshold and the new archival threshold, you can take one of two approaches to avoid querying archived files: ^[archival-support-in-databricks-databricks-on-aws.md#L114-L122]

### Approach 1: Keep the old threshold

Leave the setting `delta.timeUntilArchived` at the old threshold until enough time has passed for all files to be archived under the new policy. ^[archival-support-in-databricks-databricks-on-aws.md#L115-L117]

- Following the example: each day for the first 30 days, another day's worth of data would be considered archived by Databricks but still needs to be archived by the cloud provider. This does not result in an error, but ignores some data files that could be queried.
- After 30 days, update `delta.timeUntilArchived` to `90 days`.

### Approach 2: Incremental updates

Update the setting `delta.timeUntilArchived` each day to reflect the current interval during the lag period. ^[archival-support-in-databricks-databricks-on-aws.md#L118-L121]

- While the cloud policy is set to 90 days, the actual age of archived data changes in real-time. For example, after 7 days, setting `delta.timeUntilArchived` to `67 days` accurately reflects the age of all archived data files.
- This approach is only necessary if you must access all data in hot tiers.

> **Note**: Updating the value for `delta.timeUntilArchived` does not change which data is archived. It only changes which data Databricks treats as if it were archived. ^[archival-support-in-databricks-databricks-on-aws.md#L123-L125]

## Related concepts

- [Archival Support in Databricks](/concepts/archival-support-in-databricks.md) — The broader feature for using cloud lifecycle policies with Delta tables
- [Delta timeUntilArchived](/concepts/deltatimeuntilarchived.md) — The table property that controls archival behavior
- Cloud lifecycle policies — The underlying object storage policies that trigger archival
- [Delta Lake](/concepts/delta-lake.md) — The storage format that archival support optimizes

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md:101-104](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
2. [archival-support-in-databricks-databricks-on-aws.md:105-113](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
3. [archival-support-in-databricks-databricks-on-aws.md:114-122](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
4. [archival-support-in-databricks-databricks-on-aws.md:115-117](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
5. [archival-support-in-databricks-databricks-on-aws.md:118-121](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
6. [archival-support-in-databricks-databricks-on-aws.md:123-125](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
