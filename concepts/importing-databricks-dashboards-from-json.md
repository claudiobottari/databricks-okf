---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7d40ca69e99f4f621805041bb5652a47af51d593bd2c9c77a707a0b62dc80190
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - importing-databricks-dashboards-from-json
    - IDDFJ
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Importing Databricks Dashboards from JSON
description: The ability to import Databricks dashboards from a JSON file definition, enabling sharing and reuse of dashboard templates like the MLflow system tables dashboard.
tags:
  - databricks
  - dashboards
  - import-export
timestamp: "2026-06-19T14:10:24.494Z"
---

# Importing Databricks Dashboards from JSON

**Importing Databricks Dashboards from JSON** refers to the process of loading a pre-built dashboard into a Databricks workspace using a JSON file definition. This method allows users to quickly create visualizations of [MLflow](/concepts/mlflow.md) metadata stored in system tables without building the dashboard from scratch.

## Overview

Databricks dashboards can be exported as JSON files and then imported into another workspace. This is particularly useful for sharing dashboard templates that visualize [MLflow System Tables](/concepts/mlflow-system-tables.md) data, such as run details, experiment metrics, or system metrics like GPU utilization. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Importing a Dashboard

To import a dashboard from a JSON file:

1. Navigate to the **Dashboard** panel from the left navigation menu in your Databricks workspace.
2. Use the [import functionality](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import) to upload the JSON file. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Once imported, the dashboard becomes available in your workspace and can be used immediately with your own data.

## Example: [MLflow Run](/concepts/mlflow-run.md) Details Dashboard

Databricks provides an [example dashboard](https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json) as a downloadable JSON file. This dashboard contains a skeleton structure that replicates the run details page from the [MLflow UI](/concepts/mlflow.md). It displays:

- Run details (for a given experiment ID and run ID)
- Tags and parameters
- A metric graph

Users can obtain the experiment ID and run ID from the MLflow UI or directly from the URL: `https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`. After importing the dashboard, input boxes at the top allow filtering for the relevant run and experiment within your workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Example: GPU Utilization Monitoring Dashboard

The fourth tab of the example dashboard provides summary statistics across all experiments that contain a specified metric within a given time window. This is useful for monitoring [system metrics](/concepts/mlflow-system-metrics.md) recorded by MLflow, such as CPU, memory, or GPU utilization, across the entire workspace. For example, you can identify experiments with an average GPU utilization of less than 10% that may require investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Customization

After importing a JSON dashboard, you can explore the underlying queries and modify the plots to meet your specific needs. The dashboard structure is fully editable within the Databricks dashboard editor. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Benefits

- **Efficiency**: Avoids time-consuming iteration required when using the MLflow UI or REST APIs for analyzing experiment data across an entire workspace.
- **Reusability**: Share dashboard templates as JSON files across teams or workspaces.
- **Flexibility**: Customize queries and visualizations after importing.

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) – The data source for these dashboards
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit for runs and metrics
- [System Metrics](/concepts/mlflow-system-metrics.md) – Performance data recorded by MLflow (CPU, GPU, memory)
- [Dashboard Import/Export](/concepts/databricks-dashboard-importexport.md) – The underlying mechanism for sharing dashboard definitions

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
