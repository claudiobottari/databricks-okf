---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fd8a501fc20ec3f526f7cd9cf1d0f0cdc8aea0bb4ad61bafc0dbe75383f1470f
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - recently-resolved-incidents
    - RRI
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Recently Resolved Incidents
description: A section in the Databricks data quality monitoring dashboard showing tables that auto-recovered from unhealthy to healthy status, helping distinguish transient issues from persistent problems.
tags:
  - data-quality
  - incidents
  - monitoring
timestamp: "2026-06-19T17:33:36.784Z"
---

Here is the updated wiki page for **Recently Resolved Incidents**, rewritten based solely on the provided source material and structured for clarity.

---

# Recently Resolved Incidents

**Recently Resolved Incidents** is a section of the [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) that lists tables previously marked as **Unhealthy** but have since returned to a **Healthy** status automatically, without any manual user intervention. It provides visibility into self-healing data quality events across a monitored schema or catalog. ^[anomaly-detection-databricks-on-aws.md]

## Overview

When [Anomaly Detection](/concepts/anomaly-detection.md) determines that a table has recovered from a freshness or completeness violation, the table appears in the **Recently Resolved Incidents** section. The transition occurs automatically when the underlying metrics — such as commit timeliness or row count — return to within the expected range. This contrasts with manual dismissals, where a user marks an incident as **Not an issue**, which also moves the table to this section but with a different *Resolution* value. ^[anomaly-detection-databricks-on-aws.md]

## Why monitor recently resolved incidents

Reviewing auto-resolved incidents helps identify transient data quality issues — for example, upstream pipeline delays or short staleness windows that resolve once fresh data arrives. By distinguishing flaky problems from persistent ones, teams can decide whether to investigate further or accept the temporary deviation as normal behaviour. ^[anomaly-detection-databricks-on-aws.md]

## Resolution column

The **Resolution** column in this section indicates how the incident was resolved:

- **Not an issue** – The incident was manually dismissed by a user via the **Not an issue** action in the unhealthy table view. The dismissal persists for 7 days. ^[anomaly-detection-databricks-on-aws.md]
- (Auto-resolved incidents show a different default value, such as the date of recovery; the exact label is determined by the system.)

## Related concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) – The background job that monitors table freshness and completeness.
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) – The overarching feature that includes anomaly detection and the results UI.
- [Health Indicators](/concepts/health-indicators-databricks.md) – Visual status icons shown in Catalog Explorer for each table.
- Unhealthy Table Incidents – The view where users can assign or dismiss incidents.
- [Data Quality Monitoring UI](/concepts/data-quality-monitoring-ui.md) – The dashboard for reviewing quality results across schemas.

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
