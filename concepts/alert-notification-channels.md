---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cebf1695108cfb0812944fb23c5b9d685bbd16504076c932b598eb4741b32ee9
  pageDirectory: concepts
  sources:
    - profile-alerts-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-notification-channels
    - ANC
  citations:
    - file: profile-alerts-databricks-on-aws.md
title: Alert Notification Channels
description: Supported destinations for profile alert notifications including email, webhook, Slack, and PagerDuty.
tags:
  - databricks
  - alerting
  - notifications
timestamp: "2026-06-19T19:57:50.505Z"
---

# Alert Notification Channels

**Alert Notification Channels** are the delivery mechanisms used by [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) to send notifications when a monitoring condition is triggered. When creating alerts based on [Profile Metrics Table](/concepts/profile-metrics-table.md) or [Drift Metrics Table](/concepts/drift-metrics-table.md) queries, you can configure one or more notification channels to receive alerts.

## Default Notification Channel

By default, when you create a Databricks SQL alert, email notification is sent automatically. This means you will receive alert notifications via email without any additional configuration.^[profile-alerts-databricks-on-aws.md]

## Additional Notification Channels

Beyond the default email notification, you can configure additional notification channels for profile alerts. These include:

- **Webhooks**: You can set up a webhook to send alert notifications to a custom endpoint. This enables integration with other monitoring or incident management systems.^[profile-alerts-databricks-on-aws.md]
- **Slack**: Notifications can be sent directly to Slack channels, allowing team members to receive alerts in their collaboration workspace.^[profile-alerts-databricks-on-aws.md]
- **PagerDuty**: For critical alerts that require immediate attention, you can configure PagerDuty integration to trigger incident response workflows.^[profile-alerts-databricks-on-aws.md]

## Configuration

Alert notification channels are configured as part of creating a [Databricks SQL Alert](/concepts/databricks-sql-alerts.md). The general workflow is:

1. Create a Databricks SQL Query on the profile metrics table or drift metrics table.
2. Create a Databricks SQL alert for this query.
3. Configure the alert to evaluate at a desired frequency.
4. Set up the notification channels to determine how you receive notifications when the alert is triggered.^[profile-alerts-databricks-on-aws.md]

If the query uses parameters, the alert is based on the default values for those parameters. You should confirm that the default values reflect the intent of the alert.^[profile-alerts-databricks-on-aws.md]

## Common Alert Use Cases

Profile alerts that utilize notification channels are commonly used for:

- Receiving notifications when a statistic moves out of a certain range, such as when the fraction of missing values exceeds a threshold.^[profile-alerts-databricks-on-aws.md]
- Being notified of changes in data distribution, tracked through drift metrics.^[profile-alerts-databricks-on-aws.md]
- Receiving alerts when data has drifted compared to a baseline table, which for [Inference Log Analysis](/concepts/inferencelog-analysis.md) may indicate that a model should be retrained.^[profile-alerts-databricks-on-aws.md]

## Related Concepts

- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md)
- Databricks SQL Queries
- [Profile Metrics Table](/concepts/profile-metrics-table.md)
- [Drift Metrics Table](/concepts/drift-metrics-table.md)
- [Data Profiling](/concepts/data-profiling.md)
- [Inference Log Analysis](/concepts/inferencelog-analysis.md)

## Sources

- profile-alerts-databricks-on-aws.md

# Citations

1. [profile-alerts-databricks-on-aws.md](/references/profile-alerts-databricks-on-aws-08d2e777.md)
