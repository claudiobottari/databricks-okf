---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 15034923dfdcbc7ff6e2829f563665ec33c221ab113353fd0371d6d483d00c17
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - profile-refresh-scheduling
    - PRS
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Profile Refresh Scheduling
description: Configuration for automated scheduled refreshes or manual refresh of data profiles, including frequency and time settings, with support for incremental processing via change data feed.
tags:
  - scheduling
  - data-quality
  - automation
timestamp: "2026-06-18T14:48:06.711Z"
---

Here is the wiki page for "Profile Refresh Scheduling".

---

## Profile Refresh Scheduling

**Profile Refresh Scheduling** controls how often a [data profile](create-a-profile-using-the-databricks-ui-databricks-on-aws.md) is updated within [Databricks](create-a-profile-using-the-databricks-ui-databricks-on-aws.md) [Unity Catalog](create-a-profile-using-the-databricks-ui-databricks-on-aws.md) [monitoring](create-a-profile-using-the-databricks-ui-databricks-on-aws.md). You can set a profile to refresh automatically on a schedule or trigger updates manually. The scheduling choice affects how fresh the profile metrics are and how soon a profile detects drift or anomalies after data changes.

## Scheduling Options

A profile's refresh schedule is configured in the **Advanced options** section of the **Data Quality Monitoring** dialog. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md] You have two options:

- **Refresh on schedule** – The profile runs automatically at a chosen frequency and time. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Refresh manually** – The profile does not run automatically; you must trigger a refresh later from the **Quality** tab. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Initial Data Window

When you first create a `TimeSeries` or `Inference` profile, the initial refresh analyzes only data from the 30 days preceding its creation. After that, all new data is processed on subsequent refreshes. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Manual Refresh

Selecting **Refresh manually** defers scheduling to you. You can later trigger a profile update from the **Quality** tab. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

To refresh the profile manually after it is created, click **View refresh history** to open a dialog showing past runs, then click **Refresh metrics**. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Best Practice: Enable Change Data Feed

For `TimeSeries` and `Inference` profiles, enabling change data feed (CDF) on the source table is a best practice. When CDF is enabled, only newly appended data is processed rather than the full table on every refresh. This makes execution more efficient and reduces costs as you scale profiling across many tables. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- Create a profile using the Databricks UI – The primary interface for setting up profiles.
- Monitor metric tables – The tables created by profiles that store refresh results.
- Profile Types – `TimeSeries`, `Inference`, and other profile categories.
- [Change Data Feed](/concepts/delta-change-data-feed-cdf.md) – Enables efficient incremental refresh processing.

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
