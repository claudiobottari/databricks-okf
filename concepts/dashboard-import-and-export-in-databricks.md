---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1ff95b7f4709046a526aea8aede68fbc74a6db07b144843ae7f5352fd03884d8
  pageDirectory: concepts
  sources:
    - build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dashboard-import-and-export-in-databricks
    - Export in Databricks and Dashboard Import
    - DIAEID
  citations:
    - file: build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md
title: Dashboard Import and Export in Databricks
description: Ability to export dashboards as JSON files and import them into a Databricks workspace for reuse and customization
tags:
  - databricks
  - dashboards
  - import-export
timestamp: "2026-06-19T17:41:44.832Z"
---

# Dashboard Import and Export in Databricks

**Dashboard Import and Export in Databricks** refers to the ability to move dashboard definitions between workspaces or store them as JSON files for version control, sharing, and backup. This functionality is essential for replicating analyses across environments or collaborating on dashboard designs.

## Overview

Dashboards in Databricks can be exported as JSON files and subsequently imported into the same or a different workspace. The JSON file contains the dashboard’s queries, layout, filters, and all other metadata needed to recreate the dashboard. This capability enables teams to reuse dashboard templates, such as those built to analyze MLflow experiment metadata stored in system tables. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Importing a Dashboard

To import a dashboard, you first obtain its JSON definition (for example, by downloading an example dashboard file) and then use the import feature in the Databricks workspace.

### Steps

1. **Obtain the JSON file** – Download a predefined dashboard definition from a trusted source. The Databricks documentation provides an example dashboard for visualizing MLflow metadata as a JSON file. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

2. **Navigate to the Dashboards panel** – From the left navigation menu, open the **Dashboards** section.

3. **Import the dashboard** – Use the workspace import option (available from the Dashboards UI or via the REST API) to upload the JSON file. The dashboard will be recreated in your workspace. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

4. **Adjust inputs** – After import, you can interact with any defined input boxes (e.g., experiment ID, run ID, metric name) to filter the data shown. The dashboard will query your workspace’s system tables using the provided filters. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Exporting a Dashboard

While the source material does not describe the export procedure in detail, the ability to import a dashboard from a JSON file implies that dashboards can be exported to a JSON format as well. Exported JSON files can be stored in version control repositories, shared with colleagues, or transferred between workspaces. For specific instructions on exporting dashboards, refer to the official Databricks documentation on dashboard automation. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Use Cases

- **Collaboration** – Teams can share a common dashboard definition by exporting it from one workspace and importing it into others.
- **Version control** – Dashboard JSON definitions can be tracked in Git, enabling rollback and review of changes over time.
- **Template reuse** – Example dashboards (such as the one provided for [MLflow Run](/concepts/mlflow-run.md) details and GPU utilization monitoring) can be imported as starting points and then customized to meet specific needs. ^[build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md]

## Related Concepts

- Dashboards – The main visualization tool in Databricks.
- [MLflow System Tables](/concepts/mlflow-system-tables.md) – System tables that store MLflow experiment and run metadata.
- Dashboard JSON format – The structure of exported/imported dashboard files.
- Import/Export API – REST endpoints for programmatic dashboard import and export.
- Customizing dashboards with filters – Using input boxes to dynamically filter dashboard data.

## Sources

- build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md

# Citations

1. [build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws.md](/references/build-dashboards-with-mlflow-metadata-in-system-tables-databricks-on-aws-bdd77682.md)
