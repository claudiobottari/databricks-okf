---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ebb3dd47d69852f6c794315ebf5b35bd6c2649dc1b588e63784f09bfd8784d76
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-system-metrics-monitoring
    - MSMM
    - System Metrics Logging
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: MLflow System Metrics Monitoring
description: Recording and analyzing system-level metrics such as CPU, memory, and GPU utilization across MLflow experiments to detect inefficiencies
tags:
  - mlflow
  - system-metrics
  - monitoring
  - optimization
timestamp: "2026-06-19T17:41:40.774Z"
---

```markdown
---
title: MLflow System Metrics Monitoring
summary: Using MLflow's system metrics recording (CPU, memory, GPU utilization) and Databricks dashboards to monitor resource efficiency across experiments.
sources:
  - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T14:34:01.677Z"
updatedAt: "2026-06-18T14:34:01.677Z"
tags:
  - mlflow
  - monitoring
  - gpu
  - resource-utilization
aliases:
  - mlflow-system-metrics-monitoring
  - MSMM
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# MLflow System Metrics Monitoring

**MLflow System Metrics Monitoring** refers to the practice of collecting and analyzing infrastructure-level performance data — such as CPU, memory, and GPU utilization — alongside MLflow experiment runs. By storing these metrics in [[MLflow System Tables|system tables]], teams can build dashboards that provide workspace-wide visibility into resource efficiency, helping identify underutilized compute and optimize deep learning workloads. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Overview

MLflow automatically records system metrics for each run when enabled. These metrics capture the resource consumption of the training or inference processes, including CPU usage, memory footprint, and GPU utilization. The data is stored in the MLflow system tables, which are workspace-level tables that can be queried with standard SQL. Because system tables aggregate information across all experiments in a workspace, they allow practitioners to monitor resource efficiency at scale rather than inspecting individual runs through the MLflow UI. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Monitoring with Dashboards

Building dashboards on top of MLflow system tables enables efficient analysis of system metrics across experiments. A dashboard designed for single run details can include a tab that accepts a metric name (e.g., `gpu_utilization`) and displays summary statistics — such as average, minimum, and maximum values — across all experiments within a given time window. This approach avoids the "extensive, time-consuming iteration" that would be required if using the MLflow UI or REST APIs directly. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

### Example: Average GPU Utilization

One practical use case is monitoring average GPU utilization across the workspace. The example dashboard (available as a JSON import) includes a tab for this purpose. By entering a metric like `gpu_utilization`, users can see a chart showing average GPU utilization per experiment. The source document shows a screenshot where several experiments exhibit an average GPU utilization of less than 10%, flagging potential inefficiencies that may warrant investigation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

Similar monitoring can be applied to CPU and memory utilization, helping teams identify underutilized resources and optimize instance selection or parallelism strategies.

## Related Concepts

- System Tables — Workspace-level database tables that store MLflow metadata for analytics.
- [[MLflow Experiment|MLflow Experiments]] — Logical grouping of runs; system metrics are scoped within experiments.
- [[GPU Utilization Monitoring Dashboard|GPU Utilization Monitoring]] — Specific use case of system metrics to detect underutilized GPUs.
- [[MLflow Dashboarding on Databricks|Dashboarding on Databricks]] — Building custom visualizations using lakeview dashboards.
- Deep Learning Optimization — Broader practice that includes resource efficiency analysis.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
```

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
