---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cd85cbbd8e562b9d07ada8e68e9e72638de3e13d70c6eb2c3df9b650b2c16523
  pageDirectory: concepts
  sources:
    - choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
  confidence: 0.9
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - notebook-experiment-in-databricks-mlflow
    - NEIDM
  citations:
    - file: choose-where-your-mlflow-data-is-stored-databricks-on-aws.md
title: Notebook experiment in Databricks MLflow
description: The default experiment for MLflow runs when no experiment is explicitly set, where runs are automatically logged to the notebook's associated experiment.
tags:
  - mlflow
  - experiments
  - databricks
timestamp: "2026-06-18T10:56:08.224Z"
---

# Notebook experiment in Databricks MLflow

**Notebook experiment** is the default destination for MLflow runs when no explicit experiment is set in a Databricks workspace. When you run MLflow code in a notebook without calling `mlflow.set_experiment()` or providing an experiment name to `mlflow.start_run()`, the runs are automatically logged to the notebook experiment associated with that specific notebook.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## How notebook experiments work

Each Databricks notebook has its own associated experiment by default. This experiment is created automatically and is visible in the notebook's experiment tracking UI within the workspace. The notebook experiment stores all MLflow runs, parameters, metrics, artifacts, and models logged during the execution of that notebook.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Default behavior

By default, all MLflow runs are logged to the workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the notebook experiment. This means that if you open a Databricks notebook and run MLflow tracking code without any experiment configuration, the runs will appear under that notebook's experiment.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Overriding the notebook experiment

You can control where runs are logged by setting the active experiment using several methods:

- `mlflow.set_experiment()` — Sets a specific experiment for all subsequent runs in the execution
- `mlflow.start_run()` — Can specify an experiment when starting a run
- Environment variables — Configure the experiment at the environment level

For example, to log to a shared experiment instead of the notebook experiment:

```python
import mlflow

mlflow.set_experiment("/Shared/my-experiment")
```

^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Relationship to the tracking server

The notebook experiment exists within the [Databricks-hosted MLflow tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md), which is the managed MLflow tracking server provided by default in every Databricks workspace. This tracking server stores all experiment data in your workspace, including notebook experiments, and requires no additional setup or configuration. The Databricks-hosted tracking server integrates seamlessly with Databricks notebooks and clusters.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Use cases

Notebook experiments are ideal for:

- **Rapid prototyping** — Quick experimentation where you don't want to create a separate named experiment
- **Personal exploration** — Individual data scientists exploring data and models without needing shared experiment visibility
- **Ad-hoc analysis** — One-off analyses that don't require long-term organization in a shared experiment hierarchy

## Best practices

For production and team workflows, it is generally recommended to set an explicit experiment path rather than relying on the default notebook experiment. Using named experiments like `/Shared/my-experiment` provides better organization, discoverability, and sharing across team members. Notebook experiments are best suited for personal or exploratory work where the experiment is tied to a specific notebook session.^[choose-where-your-mlflow-data-is-stored-databricks-on-aws.md]

## Related concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — The core logging component of MLflow
- [Databricks-hosted MLflow tracking server](/concepts/databricks-hosted-mlflow-tracking-server.md) — The managed tracking server that stores notebook experiments
- [Active MLflow run management](/concepts/active-mlflow-run-management.md) — Best practices for managing run lifecycles
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Named experiments for organizing runs
- Databricks Notebooks — The environment that creates notebook experiments

## Sources

- choose-where-your-mlflow-data-is-stored-databricks-on-aws.md

# Citations

1. [choose-where-your-mlflow-data-is-stored-databricks-on-aws.md](/references/choose-where-your-mlflow-data-is-stored-databricks-on-aws-1fe2cb47.md)
