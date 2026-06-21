---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 21b43d3774c0701c264844b0176453c404babdfd2ab0316c3d272e20815239be
  pageDirectory: concepts
  sources:
    - alerts-for-anomaly-detection-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - alert-rule-scope
    - ARS
  citations:
    - file: alerts-for-anomaly-detection-databricks-on-aws.md
title: Alert Rule Scope
description: Alert rules in Databricks are scoped to either a specific schema or an entire catalog; when a monitored table within the scope becomes unhealthy, notifications are sent to designated recipients.
tags:
  - data-quality
  - alerting
  - authorization
  - databricks
timestamp: "2026-06-19T17:31:57.713Z"
---

# Alert Rule Scope

**Alert Rule Scope** determines which monitored tables a data quality alert rule covers. In the Databricks Data Quality Monitoring UI, each alert rule is defined to monitor either a specific schema or an entire catalog. The scope controls the set of unhealthy tables that trigger email notifications to the rule’s recipients. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Defining the Scope

When creating an alert rule in the Data Quality Monitoring UI, you specify its scope in two steps:

1. **Catalog** – Select the catalog that the rule will monitor.
2. **Schema** – Choose one of the following:
   - A specific schema within the selected catalog.
   - **All Schemas**, which creates a catalog‑level rule that covers every schema in the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

The scope is immutable after creation through the UI, though you can edit an existing alert rule to change its [Catalog and Schema](/concepts/catalog-and-schema.md) selection. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Permissions by Scope

The [Unity Catalog](/concepts/unity-catalog.md) privilege required to create or manage an alert rule depends directly on its scope:

- **Schema-level alert** – The user must have the `MANAGE` privilege on the schema.
- **Catalog-level alert** – The user must have the `MANAGE` privilege on the catalog.

^[alerts-for-anomaly-detection-databricks-on-aws.md]

This design ensures that only users with sufficient authority on the underlying securable objects can define monitoring rules that affect the schema or catalog. ^[alerts-for-anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – Overview of the monitoring system that powers anomaly detection.
- [Anomaly Detection](/concepts/anomaly-detection.md) – The underlying analysis that determines when a table is unhealthy.
- [Catalog Explorer](/concepts/catalog-explorer.md) – UI surface where alert rules are created and managed.
- [Unity Catalog](/concepts/unity-catalog.md) – The permission model that governs alert rule scope.
- [Data Quality Monitoring Alerts](/concepts/data-quality-monitoring-alerts.md) – Full guide on creating alerts (including Databricks SQL approach).

## Sources

- alerts-for-anomaly-detection-databricks-on-aws.md

# Citations

1. [alerts-for-anomaly-detection-databricks-on-aws.md](/references/alerts-for-anomaly-detection-databricks-on-aws-037caaff.md)
