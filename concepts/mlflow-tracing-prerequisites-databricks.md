---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5b7303bb8800306aef8aae7af8951c2f204bb91b67bf218e5ae0daa6585076c
  pageDirectory: concepts
  sources:
    - attach-custom-tags-and-metadata-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-prerequisites-databricks
    - MTP(
  citations:
    - file: attach-custom-tags-and-metadata-databricks-on-aws.md
      start: 11
      end: 16
title: MLflow Tracing Prerequisites (Databricks)
description: "Required software setup for MLflow tracing on Databricks: mlflow[databricks]>=3.1.0, openai, and databricks-connect>=16.1, plus creating an MLflow experiment."
tags:
  - mlflow
  - databricks
  - setup
timestamp: "2026-06-18T10:48:50.366Z"
---

# [MLflow Tracing](/concepts/mlflow-tracing.md) Prerequisites (Databricks)

Before you can use [MLflow Tracing](/concepts/mlflow-tracing.md) on Databricks, you must satisfy the following prerequisites:

1. **Install MLflow and required packages**  
   You need `mlflow[databricks]` version 3.1.0 or newer, along with the `openai` and `databricks-connect` (version 16.1 or later) packages. This is typically done with pip:

   ```bash
   pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"
   ```

   ^[attach-custom-tags-and-metadata-databricks-on-aws.md:11-16]

2. **Create an MLflow experiment**  
   Follow the [setup your environment quickstart](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment) to create an [MLflow Experiment](/concepts/mlflow-experiment.md) that traces will be logged to. ^[attach-custom-tags-and-metadata-databricks-on-aws.md:11-16]

These steps apply whether you use automatic tracing, the fluent API, or the decorator-based approach (`@mlflow.trace`). The `databricks-connect` dependency is required for connectivity to a Databricks workspace when running traces outside the workspace (e.g., from a local development environment).

For additional context, see MLflow Tracing Overview and [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) for compatible runtime versions.

## Sources

- attach-custom-tags-and-metadata-databricks-on-aws.md

# Citations

1. [attach-custom-tags-and-metadata-databricks-on-aws.md:11-16](/references/attach-custom-tags-and-metadata-databricks-on-aws-e81e9298.md)
