---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a725b23a902bc234745b2fecc1b429a87f9c08e894c237709ec1d020c2da774
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-alert-notification-templates
    - CANT
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Custom Alert Notification Templates
description: The ability to customize email notification templates for anomaly detection alerts in Databricks SQL using HTML, allowing detailed table-level information to be included in alert emails.
tags:
  - databricks
  - notifications
  - email-templates
  - customization
timestamp: "2026-06-19T08:57:39.969Z"
---

# Custom Alert Notification Templates

**Custom Alert Notification Templates** allow you to control the format and content of email notifications sent by Databricks SQL alerts. When an alert triggers—for example, when anomaly detection identifies unhealthy tables—you can override the default email body with a custom HTML template that includes dynamic placeholders for query result values. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## How to Create a Custom Template

Custom templates are configured during alert creation using the **Advanced** tab in the Databricks SQL alert editor.

1. Create or edit an alert in the **Alerts** sidebar.
2. In the alert editor, open the **Advanced** tab.
3. Check **Customize template** to enable the template editor.
4. Enter your HTML template, using the placeholders described below.
5. Save the alert. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Template Placeholders

The template can reference any column returned by the alert's SQL query. Rows from the query are iterated using the `{{#QUERY_RESULT_ROWS}}` ... `{{/QUERY_RESULT_ROWS}}` block. Within that block, individual column values are inserted with `{{column_name}}`.

The source example uses an anomaly-detection alert whose query returns columns such as `full_table_name`, `commit_expected`, `commit_actual`, `completeness_expected`, `completeness_actual`, and `impacted_queries`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Example Template

The following template, provided in the Databricks documentation, generates a table listing unhealthy tables along with their staleness and row volume metrics:

```html
<h4>The following tables are failing quality checks in the last hour</h4>
<table>
  <tr>
    <td>
      <table>
        <tr>
          <th>Table</th>
          <th>Expected Staleness</th>
          <th>Actual Staleness</th>
          <th>Expected Row Volume</th>
          <th>Actual Row Volume</th>
          <th>Impact (queries)</th>
        </tr>
        {{#QUERY_RESULT_ROWS}}
        <tr>
          <td>{{full_table_name}}</td>
          <td>{{commit_expected}}</td>
          <td>{{commit_actual}}</td>
          <td>{{completeness_expected}}</td>
          <td>{{completeness_actual}}</td>
          <td>{{impacted_queries}}</td>
        </tr>
        {{/QUERY_RESULT_ROWS}}
      </table>
    </td>
  </tr>
</table>
```

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- Alerts for Anomaly Detection — The monitoring alerts that use these templates
- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The general alerting framework supporting custom templates
- [Anomaly Detection](/concepts/anomaly-detection.md) — The data quality feature that generates the underlying health status
- System Tables — The `system.data_quality_monitoring.table_results` table often queried in the alert

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
