---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0ee2f4d8eb7c3f67792fe8da91949892c6b643eeb03ae901a02c551a3128f156
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - downstream-impact-tracking-in-data-quality
    - DITIDQ
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Downstream Impact Tracking in Data Quality
description: A metric (num_queries_on_affected_tables) that measures how many queries are affected by unhealthy tables, used to prioritize alerting based on business impact.
tags:
  - data-quality
  - metrics
  - impact-analysis
timestamp: "2026-06-18T10:44:59.496Z"
---

---
title: Downstream Impact Tracking in Data Quality
summary: A feature of Data Quality Monitoring that measures how many queries are affected by unhealthy tables, enabling prioritization of data quality issues based on their downstream impact.
sources:
  - alerts-for-anomaly-detection-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:00:00.000Z"
updatedAt: "2026-06-18T12:00:00.000Z"
tags:
  - data-quality
  - anomaly-detection
  - downstream-impact
aliases:
  - downstream-impact-tracking
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Downstream Impact Tracking in Data Quality

**Downstream impact tracking** is a feature of [Data Quality Monitoring](/concepts/data-quality-monitoring.md) that quantifies the business effect of a data quality issue by counting the number of queries that depend on an unhealthy table. This metric is available in the anomaly detection output system table and can be used to prioritize alerts and investigations.

## How It Works

When [Anomaly Detection](/concepts/anomaly-detection.md) runs for a monitored table, it captures a `downstream_impact` field that contains `num_queries_on_affected_tables` — the number of downstream queries that reference the table and are therefore potentially affected by its quality degradation. The system tracks this value at each evaluation time so you can see how the impact changes over time. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

The metric is accessible through the system table `system.data_quality_monitoring.table_results`, which stores per-evaluation records for each monitored table. The field is stored as a nested struct inside the `downstream_impact` column. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Using Downstream Impact in Alerts

You can configure Alerts to trigger only when the downstream impact exceeds a configurable threshold. This prevents alert fatigue by ignoring isolated quality issues that affect no active queries.

In the recommended alert SQL, the downstream impact is extracted and compared against a parameter:

```sql
WITH rounded_data AS (
  SELECT
    DATE_TRUNC('HOUR', event_time) AS evaluated_at,
    CONCAT(catalog_name, '.', schema_name, '.', table_name) AS full_table_name,
    status,
    MAX(downstream_impact.num_queries_on_affected_tables) AS impacted_queries,
    ...
  FROM system.data_quality_monitoring.table_results
  GROUP BY ALL
)
SELECT ...
WHERE
  evaluated_at >= current_timestamp() - INTERVAL 6 HOURS
  AND impacted_queries > :min_tables_affected
  AND status = 'Unhealthy';
```

The query uses `MAX(downstream_impact.num_queries_on_affected_tables)` to capture the highest impact within the evaluation window, and the alert condition `impacted_queries > :min_tables_affected` ensures that only issues affecting at least a certain number of queries fire a notification. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

### Custom Email Template

The downstream impact can be included in alert email notifications by referencing the `{{impacted_queries}}` placeholder. For example:

```html
<table>
  <tr>
    <th>Impact (queries)</th>
  </tr>
  {{#QUERY_RESULT_ROWS}}
  <tr>
    <td>{{impacted_queries}}</td>
  </tr>
  {{/QUERY_RESULT_ROWS}}
</table>
```

This allows data engineers to see at a glance which tables have the largest blast radius. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Best Practices

- Set the threshold `:min_tables_affected` to a value that reflects your team's tolerance for undetected issues. A higher threshold reduces noise but may miss early warnings.
- Combine downstream impact with other metrics such as staleness and row completeness to get a full picture of the issue's severity.
- Use the metric to triage alerts: fix tables with the highest `impacted_queries` first.

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The overall framework for monitoring table health
- [Anomaly Detection](/concepts/anomaly-detection.md) — The process of detecting quality regressions
- System Tables — Where the downstream impact data is stored
- Alerts — How to notify teams when quality issues arise

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
