---
title: Choose where your MLflow data is stored | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/tracking-server-configuration
ingestedAt: "2026-06-18T08:14:19.010Z"
---

MLflow tracking servers store and manage your experiment data, runs, and models. Configure your tracking servers to control where your MLflow data is stored and how to access experiments across different environments.

## Databricks-hosted tracking server[​](#databricks-hosted-tracking-server "Direct link to Databricks-hosted tracking server")

By default, Databricks provides a managed MLflow tracking server that:

*   Requires no additional setup or configuration
*   Stores experiment data in your workspace
*   Integrates seamlessly with Databricks notebooks and clusters

## Set the active experiment[​](#set-the-active-experiment "Direct link to Set the active experiment")

By default all MLflow runs are logged to workspace's tracking server using the active experiment. If no experiment is explicitly set, runs are logged to the [notebook experiment](https://docs.databricks.com/aws/en/mlflow/experiments#mlflow-notebook-experiments).

Control where runs are logged in Databricks by setting the active experiment:

*   Mlflow.set\_experiment()
*   Mlflow.start\_run()
*   Environment variables

Set an experiment for all subsequent runs in the execution.

Python

    import mlflowmlflow.set_experiment("/Shared/my-experiment")

## Set up tracking to a remote MLflow tracking server[​](#set-up-tracking-to-a-remote-mlflow-tracking-server "Direct link to Set up tracking to a remote MLflow tracking server")

You may need to set up a connection to a remote MLflow tracking server. This could be because you are developing locally and want to track against the Databricks hosted server, or you want to track to a different MLflow tracking server. For example, one that's in a different workspace.

Common scenarios for remote tracking:

### Set up the tracking URI and experiment[​](#set-up-the-tracking-uri-and-experiment "Direct link to Set up the tracking URI and experiment")

To log experiments to a remote tracking server, configure both the tracking URI and experiment path:

Python

    import mlflow# Set the tracking URI to the remote servermlflow.set_tracking_uri("databricks://remote-workspace-url")# Set the experiment path in the remote servermlflow.set_experiment("/Shared/centralized-experiments/my-project")# All subsequent runs will be logged to the remote serverwith mlflow.start_run():    mlflow.log_param("model_type", "random_forest")    mlflow.log_metric("accuracy", 0.95)

### Authentication methods[​](#authentication-methods "Direct link to Authentication methods")

Remote tracking server connections require proper authentication. Choose between Personal Access Tokens (PAT) or OAuth using service principals.

*   PAT
*   OAuth (service principal)

Use PATs for simple token-based authentication.

**Pros:** Simple setup, good for development

**Cons:** User-specific, requires manual token management

Python

    import os# Set authentication tokenos.environ["DATABRICKS_TOKEN"] = "your-personal-access-token"# Configure remote trackingmlflow.set_tracking_uri("databricks://remote-workspace-url")mlflow.set_experiment("/Shared/remote-experiment")
