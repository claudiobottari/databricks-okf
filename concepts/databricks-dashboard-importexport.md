---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fe5ba8bc89fa88d03e3b4e142617b2e71186555e68c64c4b1c99b81e86ef8af9
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-dashboard-importexport
    - DDI
    - Dashboard Import/Export
    - Databricks dashboard
    - import it into your workspace|Dashboards – Import & Export
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Databricks Dashboard Import/Export
description: The ability to import and export Databricks dashboards as JSON files, enabling sharing and reproduction of dashboard definitions across workspaces.
tags:
  - databricks
  - dashboards
  - import-export
timestamp: "2026-06-18T14:33:52.664Z"
---

---
title: Databricks Dashboard Import/Export
summary: The mechanism to import and export Databricks dashboards as JSON files, enabling sharing and reuse of dashboard definitions including pre-built MLflow dashboards.
sources:
  - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:54:06.290Z"
updatedAt: "2026-06-18T10:54:06.290Z"
tags:
  - databricks
  - dashboards
  - import-export
aliases:
  - databricks-dashboard-importexport
  - DDI
confidence: 0.85
provenanceState: inferred
inferredParagraphs: 1
---

# Databricks Dashboard Import/Export

**Databricks Dashboard Import/Export** is a feature that allows users to transfer dashboard definitions between workspaces using JSON file representations. This capability is particularly useful for sharing pre-built dashboards, such as those designed to visualize [MLflow metadata in system tables](/concepts/mlflow-system-tables.md), across environments or with other teams.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Importing a Dashboard

To import a dashboard, obtain a JSON file containing the dashboard definition (for example, the [MLflow System Tables Dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) sample file).^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Navigate to the **Dashboard** panel from the left navigation menu in your Databricks workspace. Use the **Import** option to load the JSON file into your workspace. After importing, the dashboard becomes available for querying and visualization against your own workspace data.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Exported Dashboard Format

The exported dashboard is a JSON file that contains a skeleton of query definitions and visual layout data. In the context of MLflow system tables, the dashboard includes input boxes for filtering by experiment ID, run ID, and metric name. These inputs allow users to plot run details, tags, parameters, and metrics for a specific run within their workspace.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

When importing, you can obtain the experiment ID and run ID from the run details page in the MLflow UI. The URL format for a specific run is: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Use Cases

### Single Run Details Dashboard

The example dashboard for MLflow system tables includes pre-built queries that display run details, tags, parameters, and a metric graph for a given experiment ID, run ID, and metric name. Users can modify the queries and change the plots to suit their needs.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### GPU Utilization Monitoring

On the fourth tab of the example dashboard, users can input a metric name to get summary statistics across all experiments with that metric within a given time window. This is useful for monitoring [system metrics](/concepts/mlflow-system-metrics.md) recorded by MLflow, such as CPU, memory, or GPU utilization across the workspace.^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Considerations

- Imported dashboards can be explored and adapted by modifying the underlying queries.
- The feature supports sharing dashboard templates that can work across different workspaces, as long as the relevant MLflow data exists in the target workspace's [system tables](/concepts/mlflow-system-tables.md).^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- System tables — The underlying data source for MLflow dashboard queries
- [MLflow metadata in system tables](/concepts/mlflow-system-tables.md) — The metadata structure that makes these dashboards possible
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The experiment tracking framework that generates the data visualized in these dashboards
- Dashboards — Databricks visualization tool that supports import/export functionality

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
