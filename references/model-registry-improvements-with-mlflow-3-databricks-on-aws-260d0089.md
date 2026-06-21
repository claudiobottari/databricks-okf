---
title: Model Registry improvements with MLflow 3 | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow/model-registry-3
ingestedAt: "2026-06-18T08:14:09.728Z"
---

This page describes improvements to the Model Registry in MLflow 3.

In MLflow 3, the Unity Catalog model registry has been enhanced to make it easier to find model parameters and performance data. When you register a `LoggedModel` to the Unity Catalog model registry, all of its metrics and parameters are available in the model registry UI and from the API. You can see model performance metrics across all MLflow experiments and workspaces on a single page. For more information about `LoggedModel`, see [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).

![model version page in catalog explorer](https://docs.databricks.com/aws/en/assets/images/mlflow3-model-version-page-3bef0948f25abb51b63eb489ea55e01f.png)

From the **Traces** panel, you can see traces associated with the Model ID from development and evaluation (`mlflow.evaluate()` runs) alongside traces from online serving in endpoints. You can use the search box to filter traces, as well as click on a trace to see the full set of spans.

![Traces tab of model version page in Unity Catalog showing details of multiple traces.](https://docs.databricks.com/aws/en/assets/images/uc-model-version-traces-17c4c2dddd4046d20799269aa7a19e6a.png)

## Next steps[​](#next-steps "Direct link to Next steps")

To learn more about other new features of MLflow 3, see the following articles:

*   [Track and compare models using MLflow Logged Models](https://docs.databricks.com/aws/en/mlflow/logged-model).
*   [MLflow 3 deployment jobs](https://docs.databricks.com/aws/en/mlflow/deployment-job).
