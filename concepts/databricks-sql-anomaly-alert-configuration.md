---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c06781e4dc1e96d83f5e54210e4f44b0939d8a96da7c4c9d9ada9786d9c539fd
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-sql-anomaly-alert-configuration
    - DSAAC
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Databricks SQL Anomaly Alert Configuration
description: An approach to configure anomaly detection alerts by querying the system.data_quality_monitoring.table_results system table with custom SQL, supporting advanced filtering and custom notification templates.
tags:
  - sql
  - alerting
  - data-quality
timestamp: "2026-06-18T14:24:14.765Z"
---

Here is the wiki page for "Databricks SQL Anomaly Alert Configuration".

---

## Databricks SQL Anomaly Alert Configuration

**Databricks SQL Anomaly Alert Configuration** refers to the process of creating a Databricks SQL alert that queries the [Anomaly Detection](/concepts/anomaly-detection.md) output system table to notify users when a data quality issue is detected. This approach supports advanced filtering and custom notification templates, offering more flexibility than the UI-based alert creation in the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Overview

While alerts can be created from the Data Quality Monitoring UI, the Databricks SQL method allows for sophisticated conditions and personalized email notifications. By querying the `system.data_quality_monitoring.table_results` system table, you can trigger alerts based on specific metrics such as table staleness (freshness), row count drops (completeness), or the downstream impact of the quality issue. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Prerequisites

By default, only account admins can access the `system.data_quality_monitoring.table_results` system table. Other users who need to configure these alerts must be granted appropriate access by an admin. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

For legacy beta jobs, the table name in the query should be `<catalog>.<schema>._quality_monitoring_summary` instead of `system.data_quality_monitoring.table_results`. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Creating the Alert

1. In your Databricks workspace, click **Alerts** in the sidebar and click **Create alert**.
2. Enter the following SQL query into the query editor:

```sql
WITH rounded_data AS (
  SELECT
    DATE_TRUNC('HOUR', event_time) AS evaluated_at,
    CONCAT(catalog_name, '.', schema_name, '.', table_name) AS full_table_name,
    status,
    MAX(downstream_impact.num_queries_on_affected_tables) AS impacted_queries,
    MAX(freshness.commit_freshness.predicted_value) AS commit_expected,
    MAX(freshness.commit_freshness.last_value) AS commit_actual,
    MAX(completeness.daily_row_count.min_predicted_value) AS completeness_expected,
    MAX(completeness.daily_row_count.last_value) AS completeness_actual
  FROM system.data_quality_monitoring.table_results
  GROUP BY ALL
)
SELECT
  evaluated_at,
  full_table_name,
  status,
  commit_expected,
  commit_actual,
  completeness_expected,
  completeness_actual,
  impacted_queries
FROM rounded_data
WHERE
  evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
  -- enter the minimum number of table violations before the alert is triggered
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

^[alerts-for-anomaly-detection-databricks-on-aws.md]

3. Run the query to verify it returns the expected results.
4. Using the alert editor on the right side of the screen, configure the trigger condition. For general guidance on setting alert conditions, see Create an alert.
5. (Optional) To customize the email notification template, open the **Advanced** tab on the right side of the screen, and check **Customize template** to open the template editor. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

#### Example Custom Email Template

The following HTML template can be used to format the alert email with a table showing each affected table's staleness, row volume, and downstream impact:

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

For more information about custom templates, see [Advanced settings for alerts](/concepts/anomaly-detection-alert.md). ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Query Details

The provided SQL query performs the following operations:

- **Time Aggregation:** Truncates `event_time` to the hour to group results.
- **Metrics:** Extracts the predicted and actual values for table freshness (`commit_freshness`) and row count completeness (`daily_row_count`), as well as the number of downstream queries impacted.
- **Filtering:** Selects only records from the last 6 hours that are marked as `Unhealthy`.
- **Parameterized Threshold:** Uses a SQL parameter `:min_tables_affected` to set the minimum number of table violations before the alert is triggered. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The underlying data quality monitoring system
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) — An alternative UI-based method for creating alerts
- Create an alert — General documentation for Databricks SQL alerts
- [Advanced settings for alerts](/concepts/anomaly-detection-alert.md) — Customizing alert behavior and templates
- [Unity Catalog](/concepts/unity-catalog.md) — The governance layer hosting the system tables
- [Freshness Metric](/concepts/freshness-data-quality.md) — Detecting stale tables
- [Completeness Metric](/concepts/completeness-data-quality.md) — Detecting unexpected drops in row count

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
