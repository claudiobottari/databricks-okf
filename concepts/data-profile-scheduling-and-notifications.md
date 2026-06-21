---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b784896444b9162c8552a16c555c8c59cb66d1e5e866178cb40caa503adc2b5d
  pageDirectory: concepts
  sources:
    - create-a-profile-using-the-databricks-ui-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - data-profile-scheduling-and-notifications
    - Notifications and Data Profile Scheduling
    - DPSAN
  citations:
    - file: create-a-profile-using-the-databricks-ui-databricks-on-aws.md
title: Data Profile Scheduling and Notifications
description: Options to run data profiling on a recurring schedule and configure email notifications for profile events, supporting up to 5 emails per event type.
tags:
  - scheduling
  - notifications
  - data-profiling
timestamp: "2026-06-19T09:28:35.658Z"
---

# Data Profile Scheduling and Notifications

**Data Profile Scheduling and Notifications** refers to the configuration options available in the Databricks UI for automating the refresh of [data profiles](/concepts/data-profile-databricks.md) and for alerting users when a refresh fails or times out. These settings are part of the **Advanced options** in the Data Quality Monitoring dialog when creating or editing a profile for a table in Unity Catalog. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Scheduling

You can control how often a data profile recalculates its metrics:

- **Refresh on schedule** – Select a frequency (e.g., daily, weekly) and a specific time for the profile to run automatically. The UI provides a drop‑down menu for the frequency and a time picker for the hour. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]
- **Refresh manually** – Choose this option if you do not want the profile to run automatically. You can trigger an on‑demand refresh later from the **Quality** tab by clicking **View refresh history** and then **Refresh metrics**. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

When a scheduled profile is first created (for `TimeSeries` or `Inference` profile types), it analyzes only data from the 30 days prior to creation. After that, all new data is processed on each subsequent refresh. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Notifications

Email notifications can be configured to alert you when a profile refresh fails or times out. In the **Notifications** section of the Advanced options, you can enter one or more email addresses and select the events for which you want to receive alerts. Up to 5 email addresses are supported per notification event type. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Editing Schedule and Notifications After Creation

After a profile is created, you can modify its scheduling and notification settings by clicking **Configure** on the **Quality** tab of the table in Catalog Explorer, then clicking **Configure** in the **Data profiling** section. The same **Advanced options** dialog appears, allowing you to change the schedule and notification recipients. ^[create-a-profile-using-the-databricks-ui-databricks-on-aws.md]

## Related Concepts

- Create a Data Profile Using the UI – Step‑by‑step guide for enabling profiling on a table.
- Manual Refresh via API – Triggering an immediate, on‑demand profile refresh programmatically.
- Profile Types – TimeSeries, Inference, and Snapshot profiles that can be scheduled.
- [Metric Tables](/concepts/profile-metric-tables.md) – The output tables where profile results are stored.
- Viewing Profile Settings – Reviewing the current configuration, including schedule and notifications.

## Sources

- create-a-profile-using-the-databricks-ui-databricks-on-aws.md

# Citations

1. [create-a-profile-using-the-databricks-ui-databricks-on-aws.md](/references/create-a-profile-using-the-databricks-ui-databricks-on-aws-d97351d2.md)
