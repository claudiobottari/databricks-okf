---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b540300355ef5f796eec2d2c8e05618f0c6686c4a8ccde573d5e0e49c591c57a
  pageDirectory: concepts
  sources:
    - open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-notebook-integration-for-mlflow
    - DNIFM
  citations:
    - file: open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md
title: Databricks notebook integration for MLflow
description: Databricks notebooks automatically connect to the MLflow server, support notebook and workspace experiments, enable autologging for MLflow tracking, and provide an inline tracing UI for GenAI interactive analysis.
tags:
  - notebooks
  - mlflow
  - development
timestamp: "2026-06-19T19:50:01.916Z"
---

# Databricks notebook integration for MLflow

**Databricks notebook integration for MLflow** refers to the built-in connectivity between Databricks notebooks and the managed MLflow server, enabling seamless experiment tracking, model logging, and interactive debugging without manual configuration.^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Features

### Automatic connection to the MLflow server
Databricks notebooks are automatically connected to the managed MLflow server when they are opened in a workspace. Users do not need to explicitly set an MLflow tracking URI or configure authentication — the connection is established for every notebook session.^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Notebook and workspace experiments
Notebooks can log runs to either a [notebook experiment](/concepts/notebook-experiment-in-databricks.md) (scoped to the notebook itself) or a workspace experiment (shared across multiple notebooks and users). This flexibility allows both ad‑hoc exploration and collaborative project tracking.^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Autologging support
Databricks notebooks support [autologging for MLflow tracking](/concepts/mlflow-trace-and-autologging.md), which automatically captures model parameters, metrics, and artifacts without requiring explicit `mlflow.log_param` or `mlflow.log_metric` calls.^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

### Inline tracing UI for GenAI
For Generative AI (GenAI) workflows, notebooks can display an inline tracing UI directly within the notebook environment. This allows interactive analysis of [[MLflow Trace|MLflow Traces]] — such as LLM calls, retrieval, and agent steps — without leaving the notebook.^[open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md]

## Related concepts

- Open source vs. managed MLflow on Databricks
- [MLflow experiments](/concepts/mlflow-experiment.md)
- [Data profiling on Databricks](/concepts/data-profiling-in-databricks.md)
- [MLflow 3 for GenAI](/concepts/mlflow-3-for-genai.md)

## Sources

- open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md

# Citations

1. [open-source-vs-managed-mlflow-on-databricks-databricks-on-aws.md](/references/open-source-vs-managed-mlflow-on-databricks-databricks-on-aws-ce848b0f.md)
