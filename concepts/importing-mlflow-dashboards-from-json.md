---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 242404267f8245c4893addb7abc160344dae305ac5433b5216e7d453f29e2c1c
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - importing-mlflow-dashboards-from-json
    - IMDFJ
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Importing MLflow Dashboards from JSON
description: The workflow of downloading a pre-built dashboard JSON file and importing it into a Databricks workspace to quickly visualize MLflow system table data.
tags:
  - databricks
  - dashboards
  - import-export
timestamp: "2026-06-19T09:10:27.800Z"
---

## Importing MLflow Dashboards from JSON

**Importing MLflow Dashboards from JSON** refers to the process of creating a Databricks dashboard pre-populated with queries and visualizations by uploading a `.lvdash` JSON file. These dashboards use data from [MLflow System Tables](/concepts/mlflow-system-tables.md) to analyze experiments, runs, and metrics across an entire workspace, providing a scalable alternative to the MLflow UI for monitoring and debugging. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Why Use a Dashboard Instead of the MLflow UI?

The MLflow UI and REST APIs can require extensive, time-consuming iteration when inspecting runs across many experiments. A dashboard built on system tables consolidates that information into parameterised, reusable views that can be shared with a team. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Obtaining the Example Dashboard

A reference dashboard is available as a JSON file. You can download it from the Databricks documentation:
`https://docs.databricks.com/aws/en/assets/files/mlflow_system_tables_dashboard.lvdash-c47a9bd31724e4ee62a78acffc600d0b.json` ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Alternatively, you can copy the definition from a [GitHub Gist](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df) linked in the documentation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Importing the Dashboard

1. Save the downloaded `.lvdash` JSON file locally.
2. In your Databricks workspace, navigate to the **Dashboards** panel from the left navigation menu.
3. Use the [import function](https://docs.databricks.com/aws/en/dashboards/automate/import-export#import) to upload the JSON file. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

After import, the dashboard appears in your workspace and is ready to be configured.

### Dashboard Contents and Usage

The imported dashboard contains several tabs:

- **Run Details Tab** – Displays a skeleton of data replicating the run details page in the MLflow UI. For a given experiment ID, run ID, and metric name, it shows run details, tags, parameters, and a metric graph. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]
- **GPU Utilization Monitoring Tab** (fourth tab) – Accepts a metric name and a time window, then returns summary statistics across all experiments that recorded that metric. Particularly useful for monitoring [system metrics](/concepts/mlflow-system-metrics.md) such as average GPU utilization across the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

You can obtain the **experiment ID** and **run ID** from the MLflow UI: they appear in the run details page and in the URL (`https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>`) as shown in the documentation screenshot. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Use the input boxes at the top of the dashboard to filter for the relevant run and experiment. The dashboard queries are fully customisable – you can explore and modify the underlying queries and plots to meet your specific needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Example: Detecting Low GPU Utilization

The GPU utilization tab can reveal experiments with very low GPU usage. In the provided example, several experiments showed an average GPU utilization of less than 10%, helping teams identify inefficient resource allocation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) – The source tables that back the dashboard queries.
- [System metrics](/concepts/mlflow-system-metrics.md) – CPU, memory, and GPU metrics tracked by MLflow.
- Dashboards on Databricks – General dashboard creation and import/export.
- MLflow experiments and runs – The entities queried by the dashboard.
- GPU utilization monitoring – Specific use case shown in the example tab.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
