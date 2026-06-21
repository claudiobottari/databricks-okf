---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7c6c50f86b0b631eb264c3b259552bb215b74bb945c5b9a398e7dab3718b3db8
  pageDirectory: concepts
  sources:
    - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - loggedmodel
    - Logged Model
    - log_model
    - log_model()
    - logged model
  citations:
    - file: model-registry-improvements-with-mlflow-3-databricks-on-aws.md
title: LoggedModel
description: MLflow abstraction that packages model artifacts together with metrics, parameters, and lineage; when registered to Unity Catalog, all metadata becomes queryable in the UI and API.
tags:
  - machine-learning
  - mlflow
  - experiment-tracking
timestamp: "2026-06-19T19:43:30.343Z"
---

```markdown
---
title: LoggedModel
summary: A new MLflow 3 concept establishing a logged model as a dedicated first-class object that, when registered to the Unity Catalog model registry, makes all its metrics, parameters, and traces available in the registry UI and API.
sources:
  - model-registry-improvements-with-mlflow-3-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:45:11.221Z"
updatedAt: "2026-06-19T10:45:11.221Z"
tags:
  - mlflow
  - model-management
  - databricks
aliases:
  - loggedmodel
confidence: 0.7
provenanceState: extracted
inferredParagraphs: 0
---

# LoggedModel

**LoggedModel** is a first-class entity introduced in [[MLflow 3 for Models]] that represents a model produced by a training run. When a `LoggedModel` is registered to the Unity Catalog model registry, all of its metrics and parameters are exposed in the model registry UI and available through the API. This provides a single view of model performance data across all MLflow experiments and workspaces. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Traces Integration

The **Traces** panel on the model version page in Unity Catalog displays traces associated with the Model ID from development runs, evaluation runs (`mlflow.evaluate()`), and online serving from endpoints. Users can filter traces using the search box and click on a trace to view its full set of spans. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Relationship with the Model Registry

When a `LoggedModel` is promoted to a Model Version in Unity Catalog, all accumulated metrics and parameters become visible on the model version page. This enables cross‑workspace and cross‑experiment observability of model performance. Additionally, the Traces tab provides end‑to‑end trace visibility from development through production. ^[model-registry-improvements-with-mlflow-3-databricks-on-aws.md]

## Related Concepts

- [[Unity Catalog Model Registry]]
- [[MLflow 3 for Models]]
- Model Version
- mlflow.evaluate()
- [[Trace Tags in MLflow|Traces in MLflow]]
- [[Serving Endpoint ACLs|Serving endpoints]]

## Sources

- model-registry-improvements-with-mlflow-3-databricks-on-aws.md
```

# Citations

1. [model-registry-improvements-with-mlflow-3-databricks-on-aws.md](/references/model-registry-improvements-with-mlflow-3-databricks-on-aws-260d0089.md)
