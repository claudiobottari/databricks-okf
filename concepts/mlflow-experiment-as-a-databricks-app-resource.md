---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 41fd6437dabc6474136d01b93f622d0259e3d69e8106624e9fb561ea665b5039
  pageDirectory: concepts
  sources:
    - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-experiment-as-a-databricks-app-resource
    - MEAADAR
  citations:
    - file: add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
title: MLflow Experiment as a Databricks App Resource
description: The ability to add an MLflow experiment as a resource within a Databricks App, enabling experiment tracking for AI applications directly from the app.
tags:
  - databricks
  - mlflow
  - app-resources
timestamp: "2026-06-19T08:51:41.156Z"
---

---

title: MLflow Experiment as a Databricks App Resource
summary: How to add an MLflow experiment as a first-class resource in a Databricks App, enabling the app to log runs, track parameters, metrics, and artifacts via the MLflow Tracking API.
sources:
  - add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:39:17.910Z"
updatedAt: "2026-06-18T10:39:17.910Z"
tags:
  - databricks
  - mlflow
  - app-resources
aliases:
  - mlflow-experiment-as-a-databricks-app-resource
  - MEAADAR
confidence: 1
provenanceState: extracted
inferredParagraphs: 1
---

# MLflow Experiment as a Databricks App Resource

When you develop AI applications, agents, LLMs, or machine learning models on Databricks, you can add an [MLflow Experiment](/concepts/mlflow-experiment.md) as a resource to a Databricks App. This integration enables the app to use MLflow’s experiment tracking capabilities — logging runs, parameters, metrics, and artifacts — directly from within the application runtime. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Capabilities

An app that has an MLflow experiment resource attached can:

- Debug agents and LLM applications with [[MLflow Trace|MLflow Traces]].
- Evaluate agent and LLM application quality using automated scorers.
- Manage and version [Prompt Templates](/concepts/prompt-templates-with-variables.md) for LLM applications.
- Log ML model training runs with parameters, metrics, and artifacts.
- Retrieve experiment data, metadata, and run history via the [MLflow Tracking API](/concepts/mlflow-tracking.md).

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Adding an MLflow Experiment Resource

Before you add the resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs). ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

1. On the **App resources** section when you create or edit an app, click **+ Add resource** > **MLflow experiment**.
2. Choose an MLflow experiment from the list of available experiments in your workspace.
3. Select the appropriate permission level for your app:
   - **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
   - **Can edit:** Grants the app permission to modify experiment settings and metadata.
   - **Can manage:** Grants the app full administrative access to the experiment.
4. (Optional) Specify a custom resource key, which is how you reference the experiment in your app configuration. The default key is `experiment`.

When you add the resource, Databricks grants your app’s Service Principal the specified permissions on the selected experiment. Access is scoped to that experiment only — the app cannot access other experiments unless you add them as separate resources. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Environment Variables

When you deploy the app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables. You reference these using the `valueFrom` field in your `app.yaml` configuration.

**Example configuration:**

```yaml
env:
  - name: MLFLOW_EXPERIMENT_ID
    valueFrom: experiment # Use your custom resource key if different
```

**Using the experiment ID in your application:**

```python
import os
import mlflow

experiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")
mlflow.set_experiment(experiment_id=experiment_id)

with mlflow.start_run():
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_artifact("model.pkl")
```

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Removing the Resource

When you remove an MLflow experiment resource from an app, the app’s service principal loses its permissions to that experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions. ^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Best Practices

- Organize experiments logically by project or model type to improve discoverability.
- Use consistent naming conventions for runs and parameters across your organization.
- Consider experiment retention policies and storage management for long-running projects.

^[add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md]

## Related Concepts

- Databricks Apps — The platform for deploying AI applications
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The structured unit of MLflow tracking
- [MLflow Tracking API](/concepts/mlflow-tracking.md) — Programmatic interface for logging and querying experiment data
- [[MLflow Trace|MLflow Traces]] — Execution traces for agents and LLMs
- Service Principal — Identity used by the app to access resources
- Environment Variables in Databricks Apps — How to access resource-bound environment variables

## Sources

- add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md

# Citations

1. [add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws.md](/references/add-an-mlflow-experiment-resource-to-a-databricks-app-databricks-on-aws-2dc6c6e2.md)
