---
title: Profile alerts | Databricks on AWS
source: https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/data-profiling/monitor-alerts
ingestedAt: "2026-06-18T08:04:21.703Z"
---

This page describes how to create a Databricks SQL alert based on a metric from a profile metrics table. Some common uses for profile alerts include:

*   Get notified when a statistic moves out of a certain range. For example, you want to receive a notification when the fraction of missing values exceeds a certain level.
*   Get notified of a change in the data. The drift metrics table stores statistics that track changes in the data distribution.
*   Get notified if data has drifted in comparison to the baseline table. You can set up an alert to investigate the data changes or, for `InferenceLog` analysis, to indicate that the model should be retrained.

Profile alerts are created and used the same way as other Databricks SQL alerts. You create a [Databricks SQL query](https://docs.databricks.com/aws/en/sql/user/queries/) on the profile metrics table or drift metrics table. You then create a Databricks SQL alert for this query. You can configure the alert to evaluate the query at a desired frequency, and send a notification if the alert is triggered. By default, email notification is sent. You can also set up a webhook or send notifications to other applications such as Slack or Pagerduty.

If the query uses parameters, the alert is based on the default values for those parameters. You should confirm that the default values reflect the intent of the alert.

For details, see [Databricks SQL alerts](https://docs.databricks.com/aws/en/sql/user/alerts/).
