---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: abcc090a5b4bfd1f331774aeccdb8a97f46a83761a55d41bb316bbee594ffbcb
  pageDirectory: concepts
  sources:
    - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - cross-workspace-model-performance
    - CMP
  citations:
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
title: Cross-Workspace Model Performance
description: Capability to view model performance metrics across all MLflow experiments and workspaces on a single page within the model registry UI.
tags:
  - machine-learning
  - mlflow
  - model-registry
  - collaboration
timestamp: "2026-06-19T19:43:27.077Z"
---

## Cross-Workspace Model Performance

**Cross-Workspace Model Performance** refers to the ability in MLflow 3 to view model performance metrics and parameters across multiple MLflow experiments and workspaces on a single page in the Unity Catalog model registry. This feature eliminates the need to navigate between different experiments or workspaces to compare model behavior, streamlining analysis for teams that manage models across organizational boundaries. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### How It Works

When you register a `LoggedModel` to the [Unity Catalog](/concepts/unity-catalog.md) model registry, all of its metrics and parameters become available in the model registry UI and through the API. The model version page in Catalog Explorer displays these metrics and parameters, enabling you to see performance data from any experiment or workspace that has registered models to the same Unity Catalog schema. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Traces Across Workspaces

The **Traces** panel on the model version page shows traces associated with the model ID from both development and evaluation runs (including `mlflow.evaluate()` calls) alongside traces from online serving in endpoints. This unified view allows you to inspect inference behavior from multiple stages of the model lifecycle—training, evaluation, and production—without switching between workspaces. You can filter traces using the search box and click on a trace to see its full set of spans. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

### Benefits

- **Centralized comparison:** Compare performance metrics from different experiments or workspaces in one location, reducing context switching.
- **Unified trace visibility:** Access traces from development, evaluation, and production serving in a single panel.
- **Parameter transparency:** View model parameters alongside metrics for a complete picture of each model version.

### Prerequisites

- The feature requires MLflow 3 and a [Unity Catalog](/concepts/unity-catalog.md) enabled workspace.
- Models must be registered as `LoggedModel` objects to the Unity Catalog model registry.

### Related Concepts

- [Model Registry](/concepts/mlflow-model-registry.md) – The centralized repository for model versions.
- [MLflow LoggedModels](/concepts/mlflow-loggedmodel.md) – The object format that carries metrics and parameters into the registry.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – Organizational units for runs that now contribute to cross-workspace views.
- [Traces and Spans](/concepts/trace-spans.md) – Observability data displayed in the Traces panel.
- [Unity Catalog](/concepts/unity-catalog.md) – The [Metastore](/concepts/metastore.md) that enables cross-workspace model governance.

### Sources

- model-registry-improvements-with-mlflow-3-databricks-on-aws.md

# Citations

1. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
