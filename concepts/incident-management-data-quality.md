---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fcc72c62cc845b83e3cd22db7b147d49d147c30bafa2b3e14f8383c9b2dc6025
  pageDirectory: concepts
  sources:
    - anomaly-detection-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - incident-management-data-quality
    - IM(Q
  citations:
    - file: anomaly-detection-databricks-on-aws.md
title: Incident Management (Data Quality)
description: Workflow for handling detected data quality incidents including assigning ownership, marking false positives, and reviewing recently auto-resolved incidents.
tags:
  - data-quality
  - workflow
  - incident-response
timestamp: "2026-06-18T14:25:42.146Z"
---

# Incident Management (Data Quality)

**Incident Management (Data Quality)** refers to the process of identifying, reviewing, and resolving data quality issues detected by monitoring systems such as [Anomaly Detection](/concepts/anomaly-detection.md). In the context of [Unity Catalog](/concepts/unity-catalog.md) and [Data Quality Monitoring](/concepts/data-quality-monitoring.md), incidents represent tables that have been flagged as unhealthy due to failures in [freshness](/concepts/freshness-data-quality.md) or [completeness](/concepts/data-completeness.md) checks, and the workflow for managing these incidents involves reviewing detected anomalies, assigning ownership for investigation, dismissing false positives, and monitoring self-healing resolutions. ^[anomaly-detection-databricks-on-aws.md]

## Overview

When [Anomaly Detection](/concepts/anomaly-detection.md) is enabled on a schema, Databricks automatically evaluates each table's [freshness](/concepts/freshness-data-quality.md) (how recently it has been updated) and [completeness](/concepts/data-completeness.md) (the expected number of rows written in the last 24 hours). Tables that fail these checks are marked as **Unhealthy** and appear as incidents in the [Data Quality Monitoring](/concepts/data-quality-monitoring.md) results UI. ^[anomaly-detection-databricks-on-aws.md]

The incident management workflow provides two primary actions for responding to unhealthy tables: **Assign to me** (to claim ownership for investigation) and **Not an issue** (to mark a detected issue as a false positive and dismiss the incident). ^[anomaly-detection-databricks-on-aws.md]

## Viewing Incidents

Incidents can be viewed in several ways:

- From the **Data Quality Monitoring** results UI, accessible after enabling anomaly detection on a schema. Users with **MANAGE** or **SELECT** privileges on a catalog can view incidents at the catalog level by selecting **All Schemas** from the Schema drop-down menu. For a specific schema, users must also have **MANAGE** or **SELECT** privileges on that schema. ^[anomaly-detection-databricks-on-aws.md]
- From the **Catalog Explorer** Table Details page, by visiting the **Quality** tab on the table page. This view shows summaries from each quality check with graphs of predicted and observed values at each evaluation timestamp over the last week. ^[anomaly-detection-databricks-on-aws.md]
- Through **health indicators** that appear on schema and table overview pages in Catalog Explorer. Users need the **SELECT** or **BROWSE** permission to view these status indicators. ^[anomaly-detection-databricks-on-aws.md]

The results UI includes a summary section at the top displaying overall data quality for the selected scope, including the percentage of healthy tables and the percentage of schemas/tables currently monitored. Below this section is a table listing incidents across all monitored tables. Users can filter using buttons for **Unhealthy**, **Healthy**, or **Error** tables. ^[anomaly-detection-databricks-on-aws.md]

## Managing Unhealthy Table Incidents

From the **Unhealthy** tab in the results UI, the **Results** column provides a **Review** link to open incident details for the table. Two actions are available:
- **Assign to me**: Claims ownership of the incident to indicate it is actively being investigated. The table remains in **Unhealthy** status. The assignment persists for **7 days**. ^[anomaly-detection-databricks-on-aws.md]
- **Not an issue**: Marks the incident as a false positive and dismisses it. The table's status changes from **Unhealthy** to **Healthy**, and the **Resolution** column in the [Recently Resolved Incidents](#recently-resolved-incidents) section displays **Not an issue**. The dismissal persists for **7 days**. ^[anomaly-detection-databricks-on-aws.md]

## Recently Resolved Incidents

The **Recently Resolved Incidents** section of the data quality monitoring dashboard shows tables that were previously unhealthy but have since recovered on their own. A table appears in this section when its status changes from **Unhealthy** to **Healthy** automatically, without manual intervention. ^[anomaly-detection-databricks-on-aws.md]

Monitoring recently auto-resolved incidents helps identify self-healing data quality issues. Typically, these issues are transient problems such as upstream delays or staleness windows that resolve after fresh data arrives. Reviewing auto-resolved incidents helps distinguish flaky issues from persistent problems and ensures that tables remain healthy over time. ^[anomaly-detection-databricks-on-aws.md]

The following table describes the columns in this section: [table omitted for brevity, refer to the source document for column details] ^[anomaly-detection-databricks-on-aws.md]

## Table Quality Details

When a table fails quality checks, the **Table Quality Details** UI displays any upstream jobs that were identified as the root cause of the anomaly, along with trend visualizations. ^[anomaly-detection-databricks-on-aws.md]

## Setting Up Alerts

To configure a Databricks SQL alert on the output results table, see [Alerts for anomaly detection](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-quality-monitoring/anomaly-detection/alerts). ^[anomaly-detection-databricks-on-aws.md]

## Limitations

- Anomaly detection does not support views or foreign tables. ^[anomaly-detection-databricks-on-aws.md]
- The determination of completeness does not take into account metrics such as the fraction of nulls, zero values, or NaN. ^[anomaly-detection-databricks-on-aws.md]

## Related Concepts

- [Anomaly Detection](/concepts/anomaly-detection.md) — The monitoring system that detects data quality issues and generates incidents
- [Freshness](/concepts/freshness-data-quality.md) — How recently a table has been updated
- [Completeness](/concepts/data-completeness.md) — Expected number of rows written to a table
- [Data Quality Monitoring](/concepts/data-quality-monitoring.md) — The overall framework for tracking data health
- [Anomaly Detection Results](/concepts/anomaly-detection-result-schema.md) — The logged output system table for incident data
- Anomaly Detection Health Indicators — Visual status indicators in Catalog Explorer
- [Data Quality Monitoring Dashboard](/concepts/data-quality-monitoring-ui-beta.md) — Legacy dashboard for reviewing quality results

## Sources

- anomaly-detection-databricks-on-aws.md

# Citations

1. [anomaly-detection-databricks-on-aws.md](/references/anomaly-detection-databricks-on-aws-a589cd11.md)
