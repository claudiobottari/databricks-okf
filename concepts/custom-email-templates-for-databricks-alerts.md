---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbe1819ad6b0fa5c6e48114c65482d86a5c0087b0bae94abad59ccad2a8d273f
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-email-templates-for-databricks-alerts
    - CETFDA
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Custom Email Templates for Databricks Alerts
description: The ability to customize email notification templates for anomaly detection alerts using HTML and query result placeholders.
tags:
  - databricks
  - notifications
  - email-templates
  - alerting
timestamp: "2026-06-19T13:59:20.343Z"
---

# Custom Email Templates for Databricks Alerts

Databricks alerts for anomaly detection can send email notifications with a customizable HTML body. Custom email templates allow you to format the alert message to include specific metrics from the query result, such as table names, expected vs. actual staleness, row counts, and query impact. This feature is available only for alerts created using Databricks SQL (not for alerts created via the Data Quality Monitoring UI).^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Enabling the Custom Template

When creating or editing an alert from the Databricks SQL alert editor, open the **Advanced** tab on the right side of the screen and check **Customize template**. This opens the template editor where you can enter your own HTML.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Template Syntax

The custom email template uses the [Handlebars](https://handlebarsjs.com/)-like template syntax supported by Databricks SQL alerts. The main iteration construct is `{{#QUERY_RESULT_ROWS}}...{{/QUERY_RESULT_ROWS}}`, which loops over each row returned by the alert's query. Inside the loop, you can reference any column name from the query result as a placeholder using double curly braces, e.g., `{{full_table_name}}`.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Example Template

The following example is provided in the Databricks documentation for anomaly detection alerts. It displays a table listing tables that failed quality checks in the last hour, along with expected and actual staleness, row volume, and query impact:

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

This template expects the alert query to return columns named `full_table_name`, `commit_expected`, `commit_actual`, `completeness_expected`, `completeness_actual`, and `impacted_queries`. The query in the documentation uses the system table `system.data_quality_monitoring.table_results` and defines these columns via aliases.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Custom Template Placeholders

Any column name from the alert query's result set can be used as a placeholder. Common columns used in anomaly detection alerts include:

| Placeholder | Description |
|---|---|
| `full_table_name` | Fully qualified table name (`catalog.schema.table`) |
| `commit_expected` | Expected staleness (predicted commit freshness) |
| `commit_actual` | Actual staleness (last observed commit freshness) |
| `completeness_expected` | Expected daily row count |
| `completeness_actual` | Actual daily row count |
| `impacted_queries` | Number of queries affected by the unhealthy table |

^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Important Notes

- The custom template feature is optional; by default, alerts use a standard email format.
- The template is rendered with the complete result set of the alert query. If the query returns no rows, the alert is not triggered and no email is sent.
- For more information about advanced settings and template syntax, see the Create an Alert documentation in Databricks SQL.^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Databricks SQL Alerts](/concepts/databricks-sql-alerts.md) — The alerting system that supports custom email templates
- [Anomaly Detection](/concepts/anomaly-detection.md) — The data quality monitoring feature that triggers these alerts
- System Tables — The `system.data_quality_monitoring` tables that provide anomaly detection results

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
