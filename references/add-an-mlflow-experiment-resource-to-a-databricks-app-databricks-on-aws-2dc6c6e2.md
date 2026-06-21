---
title: Add an MLflow experiment resource to a Databricks app | Databricks on AWS
source: https://docs.databricks.com/aws/en/dev-tools/databricks-apps/mlflow
ingestedAt: "2026-06-18T08:06:05.903Z"
---

Add [MLflow experiments](https://docs.databricks.com/aws/en/mlflow/experiments) as Databricks Apps resources to enable experiment tracking for your AI applications, agents, LLMs, and ML models. MLflow experiments provide a structured way to organize and log runs, track parameters, metrics, and artifacts throughout the AI application development lifecycle.

When you add an MLflow experiment as a resource, your app can:

*   Debug agents and LLM applications with execution traces
*   Evaluate agent and LLM application quality with scorers
*   Manage and version prompt templates for LLM applications
*   Log ML model training runs with parameters, metrics, and artifacts
*   Retrieve experiment data, metadata, and run history

## Add an MLflow experiment resource[​](#add-an-mlflow-experiment-resource "Direct link to add-an-mlflow-experiment-resource")

Before you add an MLflow experiment as a resource, review the [app resource prerequisites](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/resources#resources-prereqs).

1.  In the **App resources** section when you create or edit an app, click **\+ Add resource** > **MLflow experiment**.
2.  Choose an MLflow experiment from the list of available experiments in your workspace.
3.  Select the appropriate permission level for your app:
    *   **Can read:** Grants the app permission to view experiment metadata, runs, parameters, and metrics. Use for apps that display experiment results.
    *   **Can edit:** Grants the app permission to modify experiment settings and metadata.
    *   **Can manage:** Grants the app full administrative access to the experiment.
4.  (Optional) Specify a custom resource key, which is how you reference the experiment in your app configuration. The default key is `experiment`.

When you add an MLflow experiment resource:

*   Databricks grants your app's [service principal](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/auth#app-authorization) the specified permissions on the selected experiment.
*   The app can log training runs and access experiment data through the MLflow Tracking API.
*   Access is scoped to the selected experiment only. Your app can't access other experiments unless you add them as separate resources.

## Environment variables[​](#environment-variables "Direct link to environment-variables")

When you deploy an app with an MLflow experiment resource, Databricks exposes the experiment ID through environment variables that you can reference using the `valueFrom` field in your `app.yaml` configuration.

**Example configuration:**

YAML

    env:  - name: MLFLOW_EXPERIMENT_ID    valueFrom: experiment # Use your custom resource key if different

**Using the experiment ID in your application:**

Python

    import osimport mlflow# Access the experiment using the injected environment variableexperiment_id = os.getenv("MLFLOW_EXPERIMENT_ID")# Set the experiment for trackingmlflow.set_experiment(experiment_id=experiment_id)# Log parameters and metricswith mlflow.start_run():    mlflow.log_param("learning_rate", 0.01)    mlflow.log_metric("accuracy", 0.95)    mlflow.log_artifact("model.pkl")

For more information, see [Access environment variables from resources](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/environment-variables#access-resources).

## Remove an MLflow Experiment resource[​](#remove-an-mlflow-experiment-resource "Direct link to remove-an-mlflow-experiment-resource")

When you remove an MLflow Experiment resource from an app, the app's service principal loses access to the experiment. The experiment itself remains unchanged and continues to be available for other users and applications that have appropriate permissions.

## Best practices[​](#best-practices "Direct link to best-practices")

Follow these best practices when you work with MLflow experiment resources:

*   Organize experiments logically by project or model type to improve discoverability.
*   Use consistent naming conventions for runs and parameters across your organization.
*   Consider experiment retention policies and storage management for long-running projects.
