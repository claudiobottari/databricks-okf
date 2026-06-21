---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc562d1a653217565bcf39b2ce49503b68cff1a0e8e4581f11c92aaee22019be
  pageDirectory: concepts
  sources:
    - archival-support-in-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - lifecycle-policy-extension-risks-with-delta-lake-archival
    - LPERWDLA
  citations:
    - file: archival-support-in-databricks-databricks-on-aws.md
title: Lifecycle policy extension risks with Delta Lake archival
description: Extending the archival interval in cloud lifecycle policies can lead to errors because previously archived files are not automatically restored.
tags:
  - delta-lake
  - archival
  - lifecycle-management
  - risks
timestamp: "2026-06-19T17:35:04.609Z"
---

# Lifecycle Policy Extension Risks with Delta Lake Archival

The **lifecycle policy extension risk** arises when a cloud object‑storage lifecycle management transition rule is changed to a *longer* time interval before archival, while the Delta table’s `delta.timeUntilArchived` property is updated accordingly. Because cloud providers do not automatically restore already‑archived files when a retention policy is relaxed, the table can enter an inconsistent state where archived data files are still treated as unavailable, leading to query failures or missing data. ^[archival-support-in-databricks-databricks-on-aws.md]

## How Extension Creates Risk

Archival support in Databricks relies on the table property `delta.timeUntilArchived` to tell the query engine which files to ignore because they are older than the specified period. This property must match the actual archival threshold applied by the cloud provider’s lifecycle policy. When the lifecycle policy is extended (e.g., from 60 days to 90 days), files that were already archived by the old policy remain in the archival tier. The cloud does not retroactively move them back to a hot storage tier. ^[archival-support-in-databricks-databricks-on-aws.md]

If a user updates `delta.timeUntilArchived` to the new, longer interval (e.g., 90 days), Databricks will assume that files between 60 and 90 days old are still available in hot storage. In reality, those files are archived. Queries that need to scan this data will either fail or, if archival support prevents scanning, produce incorrect results because the engine believes those files are not archived. ^[archival-support-in-databricks-databricks-on-aws.md]

> **Important:** Never set `delta.timeUntilArchived` to a value greater than the actual age of the most recently archived data. Doing so risks query errors. ^[archival-support-in-databricks-databricks-on-aws.md]

## Example Scenario

Consider a table with a lifecycle policy that originally archived objects older than 60 days. After the policy has been in place for some time, all data files older than 60 days are in archival storage. The operator then changes the policy to archive objects after 90 days.

| Day | Event |
|-----|-------|
| 0   | Policy changed from 60 → 90 days |
| 0–30 | Files aged 60–90 days were already archived; new files (age <60 days) remain in hot storage. |
| 30  | No new files archived for 30 days; the oldest hot files are now 60 days old (still within the 90‑day window). |
| 90  | All files now match the policy; the oldest archived file is now 90 days old. |

If `delta.timeUntilArchived` is set to `90 days` immediately on day 0, any query that needs files aged 60–90 days will fail because those files are archived but the engine treats them as hot. The setting must be adjusted carefully during this 30‑day lag period. ^[archival-support-in-databricks-databricks-on-aws.md]

## Mitigation Approaches

Two strategies can avoid query errors during the transition period:

1. **Keep the old `delta.timeUntilArchived` value until enough time has passed for all previously archived files to be covered by the new policy.**  
   *Example:* Leave the property at `60 days` for the first 30 days. During that period, files aged 60–90 days are considered archived (and ignored), even though some of those files are still in hot storage. This is safe but means a portion of accessible data is not queried. After 30 days, update the property to `90 days`. ^[archival-support-in-databricks-databricks-on-aws.md]

2. **Update `delta.timeUntilArchived` daily to reflect the actual age of the oldest archived data.**  
   *Example:* On day 7 after extending the policy to 90 days, set the property to `67 days` (60 original + 7 days). This gradually increases each day until it reaches 90 days. This approach is more precise but requires daily maintenance. It is only necessary if all hot‑tier data must be accessible during the lag period. ^[archival-support-in-databricks-databricks-on-aws.md]

Note that changing `delta.timeUntilArchived` does **not** alter which files the cloud provider archives; it only changes which files Databricks treats as if they were archived. ^[archival-support-in-databricks-databricks-on-aws.md]

## Related Concepts

- [Archival Support in Delta Lake](/concepts/archival-support-for-delta-tables.md) — Overview of enabling cloud‑based lifecycle policies on Delta tables.
- [delta.timeUntilArchived Property](/concepts/deltatimeuntilarchived-table-property.md) — The table property that defines the archival threshold.
- Lifecycle Management Policy — Cloud provider policies (e.g., S3 Lifecycle) that move objects to cheaper storage tiers.
- [SHOW ARCHIVED FILES](/concepts/show-archived-files-syntax.md) — Syntax to list files that must be restored.
- [Delta transaction log](/concepts/delta-transaction-log.md) — Archiving the `_delta_log/` directory makes the table entirely inaccessible; must be excluded from lifecycle policies.

## Sources

- archival-support-in-databricks-databricks-on-aws.md

# Citations

1. [archival-support-in-databricks-databricks-on-aws.md](/references/archival-support-in-databricks-databricks-on-aws-d64d2061.md)
