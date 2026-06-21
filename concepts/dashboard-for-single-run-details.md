---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 84b2573257f11fcec22cc32c53de3ea7dd83b8e085d3c4f5644e24d2c9e73cac
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-for-single-run-details
    - DFSRD
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Dashboard for Single Run Details
description: A pre-built dashboard pattern that replicates the MLflow run details page, allowing filtering by experiment ID, run ID, and metric name to display tags, parameters, and metric graphs.
tags:
  - mlflow
  - dashboards
  - experiment-tracking
timestamp: "2026-06-19T09:10:32.079Z"
---

# Dashboard for Single Run Details

**Dashboard for Single Run Details** is a pre-built Databricks dashboard that replicates the functionality of the [MLflow Run](/concepts/mlflow-run.md) details page using data from system tables. It provides a structured, query‑based view of a single [MLflow Run](/concepts/mlflow-run.md) without requiring iterative API calls or navigating the MLflow UI. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

The dashboard draws on MLflow metadata stored in [MLflow System Tables](/concepts/mlflow-system-tables.md) to display run‑level information for a given experiment and run. For a specified experiment ID, run ID, and metric name, the dashboard shows run details, tags, parameters, and a metric graph – mirroring what appears on the run details page in the MLflow UI. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

This approach is more efficient than using the MLflow UI or REST APIs directly because the dashboard queries the system tables, which contain metadata for all runs across the workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Getting Started

To use the dashboard, download the example dashboard JSON file from the Databricks documentation asset and [import it into your workspace|Dashboards – Import & Export](/concepts/databricks-dashboard-importexport.md). The JSON is also available from a [Gist](https://gist.github.com/ian-ack-db/684a83040a557f92f1668449c0df75df). ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

The experiment ID and run ID can be obtained from the run details page – they appear in both the UI and the URL:

```
https://<workspace>.databricks.com/ml/experiments/<experiment_id>/runs/<run_id>
```

After importing, use the input boxes at the top of the dashboard to filter for the desired run and experiment. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Customization

The dashboard ships with a skeleton of data that can be extended. Users are encouraged to explore the underlying queries and change the plots to meet their specific needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- [MLflow System Tables](/concepts/mlflow-system-tables.md) — The source of metadata for the dashboard queries.
- [MLflow experiments](/concepts/mlflow-experiment.md) and [MLflow runs](/concepts/mlflow-run.md) — The organizational units for tracking.
- [Build dashboards with MLflow metadata in system tables](/concepts/mlflow-dashboards-from-system-tables.md) — The broader topic that includes additional dashboards (e.g., average GPU utilization across experiments).
- [MLflow UI run details page](/concepts/mlflow-dashboard-for-run-details.md) — The conventional way to view run details, which this dashboard replicates.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
