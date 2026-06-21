---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8420639915b5a7594c22f56bd078de703991c9cfcaeb45d7a14372e8a78bab48
  pageDirectory: concepts
  sources:
    - open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - open-source-mlflow-data-portability
    - OSMDP
  citations:
    - file: open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
title: Open source MLflow data portability
description: The core MLflow data model, API, and SDK are fully open source, ensuring users can export and use their MLflow data anywhere despite using the managed Databricks platform.
tags:
  - mlflow
  - open-source
  - portability
timestamp: "2026-06-19T19:49:52.204Z"
---

# Open Source MLflow Data Portability

**Open source MLflow data portability** refers to the ability to freely export and reuse machine learning (ML) metadata, model artifacts, and experiment tracking data generated using [MLflow](/concepts/mlflow.md) because the core data model, API, and SDK are published under an open-source license. This portability ensures that users are not locked into any single provider, including Databricks, and can migrate workloads across environments. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Foundation in Open Source

Open source MLflow provides the core data model, API, and SDK, which means both the data and the code that processes it are always portable. The documentation explicitly notes: "Your data and workloads are always portable." ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

The principle is reinforced by the statement: "Your data is always yours – The core data model and APIs are completely open source. You can export and use your MLflow data anywhere." ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Relationship with Managed MLflow on Databricks

[Managed MLflow](/concepts/databricks-managed-mlflow.md) on Databricks builds on the same open-source foundation. The Databricks-managed service adds enterprise-grade governance, fully managed hosting, and platform integrations, but does not alter the underlying portable data model. The documentation emphasizes that managed MLflow "uses the same APIs" and that the core data model remains open source, enabling users to export their data and use it elsewhere. ^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Implications for Users

- **Vendor independence**: Because the data is stored in an open format and the APIs are standard, users can move between any infrastructure that supports MLflow, including self-hosted open-source servers, Databricks, or other third-party platforms.
- **Workload portability**: Not only the metadata but also the workloads (e.g., training runs, evaluations) can be replayed or reproduced in different environments using the same SDK and APIs.
- **No data lock-in**: Even when using managed MLflow on Databricks, users retain full control over their ML data and can export it at any time.

## Related Concepts

- [MLflow](/concepts/mlflow.md) – The open-source platform for managing the ML lifecycle.
- [Managed MLflow](/concepts/databricks-managed-mlflow.md) – Databricks’ hosted version of MLflow.
- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md) – The latest generation of MLflow, focused on generative AI.
- [Unity Catalog](/concepts/unity-catalog.md) – Databricks’ governance layer, which adds metadata management on top of MLflow.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational units for tracking runs.
- [MLflow Tracking](/concepts/mlflow-tracking.md) – The component responsible for logging parameters, metrics, and artifacts.

## Sources

- open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md](/references/open-source-vs-managed-mlflow-on-databricks-databricks-on-aws-ce848b0f.md)
