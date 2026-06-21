---
title: Manage model lifecycle using the Workspace Model Registry (legacy) | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry
ingestedAt: "2026-06-18T08:11:29.748Z"
---

important

This documentation covers the Workspace Model Registry. If your workspace is enabled for Unity Catalog, do not use the procedures on this page. Instead, see [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/).

For guidance on how to upgrade from the Workspace Model Registry to Unity Catalog, see [Migrate workflows and models to Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/migrate-to-uc).

If your workspace's [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is in Unity Catalog (rather than `hive_metastore`), and you are either running a cluster using Databricks Runtime 13.3 LTS or above or using [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install), models are automatically created in and loaded from the workspace default catalog, with no configuration required. To use the Workspace Model Registry in this case, you must explicitly target it by running `import mlflow; mlflow.set_registry_uri("databricks")` at the start of your workload. A small number of workspaces where both the default catalog was configured to a catalog in Unity Catalog prior to January 2024 and the workspace model registry was used prior to January 2024 are exempt from this behavior and continue to use the Workspace Model Registry by default.

Starting in April 2024, Databricks disabled Workspace Model Registry for workspaces in new accounts where the workspace's [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is in Unity Catalog.

This article describes how to use the Workspace Model Registry as part of your machine learning workflow to manage the full lifecycle of ML models. The Workspace Model Registry is a Databricks-provided, hosted version of the MLflow Model Registry.

The Workspace Model Registry continues to be supported in [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) as in MLflow 2.x. With MLflow 3, the default registry URI is `databricks-uc`, meaning the MLflow Model Registry in Unity Catalog will be used. To use the Workspace Model Registry, you must call `mlflow.set_registry_uri("databricks")`. For more details, see [Model registry](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install#model-registry).

The Workspace Model Registry provides:

*   Chronological model lineage (which MLflow experiment and run produced the model at a given time).
*   [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).
*   Model versioning.
*   Stage transitions (for example, from staging to production or archived).
*   [Webhooks](https://docs.databricks.com/aws/en/mlflow/model-registry-webhooks) so you can automatically trigger actions based on registry events.
*   Email notifications of model events.

You can also create and view model descriptions and leave comments.

This article includes instructions for both the Workspace Model Registry UI and the Workspace Model Registry API.

For an overview of Workspace Model Registry concepts, see [MLflow on Databricks](https://docs.databricks.com/aws/en/mlflow/).

## Create or register a model[​](#create-or-register-a-model "Direct link to Create or register a model")

You can create or register a model using the UI, or [register a model using the API](#register-model-api).

### Create or register a model using the UI[​](#create-or-register-a-model-using-the-ui "Direct link to Create or register a model using the UI")

There are two ways to register a model in the Workspace Model Registry. You can register an existing model that has been logged to MLflow, or you can create and register a new, empty model and then assign a previously logged model to it.

#### Register an existing logged model from a notebook[​](#register-an-existing-logged-model-from-a-notebook "Direct link to register-an-existing-logged-model-from-a-notebook")

1.  In the Workspace, identify the MLflow run containing the model you want to register.
    
    1.  Click the **Experiment** icon ![Experiment icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAVCAYAAACpF6WWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFaADAAQAAAABAAAAFQAAAAAIGxIOAAABUUlEQVQ4EWP8DwQMVAZMVDYPbBxNDGUh5NL04jqGe4+eoChTkpNhmNnbhCKGzCFoKMhAYz0tBgMdDbC+C1duMJy9dA3ZDAw2QUNBOkAGRgT6wDUTMpQmYTpMDP0HzRdMjIzw8ISx8eUZvN4/eeYC2DBREWG4oTD2qfOX4GLoDEZc2XTf4RMMnVPmMPz7948hOtiXgYOdFaz3x49fDEvXbWFgYmJiqMhLYXC0tkA3kwHDUJCXFyxfx7B8/VYMxdgEQBbGhwcwMCIFEQPIpchgzaYd/11CEv9Pmr3o/9+/f5GlUNggud5pc8Fq123ZhSKHYWhoYv7/lr5pKIrwcRq7J/+PTC9GUYKRo8TFhRkePXnOsGL9Fmy+xRB78uwlg7iIEIo4RpjeuHWXoWvqXIbHz16gKMTFkZeWZCjNTWFQV1aEK8EwFC5DAQNvOiXX3KFjKAAbsvOWj3bmtQAAAABJRU5ErkJggg==) in the notebook's right sidebar.
        
        ![Notebook toolbar](https://docs.databricks.com/aws/en/assets/images/notebook-toolbar-70a2fafa48b3a925099e836a4d5fb0ae.png)
        
    2.  In the Experiment Runs sidebar, click the ![External Link](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAXCAYAAAARIY8tAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAGKADAAQAAAABAAAAFwAAAABgZeJ8AAAA8ElEQVRIDWP8DwQMNARMNDQbbDTNLWAh1wfKxdswtN7t9cIQw2pB1LQTDCfvvsNQDBKAGZLnrgqWP3nnLU61IAVYLQAZbq4sxGCuIgw2BBuR76bKMHHXbbyG47QAJAEyHGQILgAyfNLO2wwwn4DY2ABZkYxsOD5HgC0E5QN0oFS09f+EnbfQhcF8kDg+eXRNJPkAFDewYCHocmh4kWQBKOKXZVmgxA0ouLAlWVh8kGQBSBPIElIAyRaQYjhI7dC3AGtOBnkNVARMBDEIAJA6fACrBaCIBCVJXOURuoH4Ip4RlDHQNVCTP/QjedQHBNMDAL0aoP7asXF1AAAAAElFTkSuQmCC) icon next to the date of the run. The MLflow Run page displays. This page shows details of the run including parameters, metrics, tags, and list of artifacts.
        
2.  In the Artifacts section, click the directory named **xxx-model**.
    
    ![Register model](https://docs.databricks.com/aws/en/assets/images/register-model-42b0af55568933728101e0b45428fda2.png)
    
3.  Click the **Register Model** button at the far right.
    
4.  In the dialog, click in the **Model** box and do one of the following:
    
    *   Select **Create New Model** from the drop-down menu. The **Model Name** field appears. Enter a model name, for example `scikit-learn-power-forecasting`.
    *   Select an existing model from the drop-down menu.
    
    ![Create new model](https://docs.databricks.com/aws/en/assets/images/create-model-0fa1d1eabf54cd9b18377029a897b7a0.png)
    
5.  Click **Register**.
    
    *   If you selected **Create New Model**, this registers a model named `scikit-learn-power-forecasting`, copies the model into a secure location managed by the Workspace Model Registry, and creates a new version of the model.
    *   If you selected an existing model, this registers a new version of the selected model.
    
    After a few moments, the **Register Model** button changes to a link to the new registered model version.
    
    ![Select newly created model](https://docs.databricks.com/aws/en/assets/images/registered-model-version-09f93a481aaeaceb1ec8dd0d1c34bd31.png)
    
6.  Click the link to open the new model version in the Workspace Model Registry UI. You can also find the model in the Workspace Model Registry by clicking ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in the sidebar.
    

#### Create a new registered model and assign a logged model to it[​](#create-a-new-registered-model-and-assign-a-logged-model-to-it "Direct link to Create a new registered model and assign a logged model to it")

You can use the Create Model button on the registered models page to create a new, empty model and then assign a logged model to it. Follow these steps:

1.  On the registered models page, click **Create Model**. Enter a name for the model and click **Create**.
    
2.  Follow Steps 1 through 3 in [Register an existing logged model from a notebook](#register-an-existing-logged-model-from-a-notebook).
    
3.  In the Register Model dialog, select the name of the model you created in Step 1 and click **Register**. This registers a model with the name you created, copies the model into a secure location managed by the Workspace Model Registry, and creates a model version: `Version 1`.
    
    After a few moments, the MLflow Run UI replaces the Register Model button with a link to the new registered model version. You can now select the model from the **Model** drop-down list in the Register Model dialog on the **Experiment Runs** page. You can also register new versions of the model by specifying its name in API commands like [Create ModelVersion](https://mlflow.org/docs/latest/rest-api.html#create-modelversion).
    

### Register a model using the API[​](#register-a-model-using-the-api "Direct link to register-a-model-using-the-api")

There are three programmatic ways to register a model in the Workspace Model Registry. All methods copy the model into a secure location managed by the Workspace Model Registry.

*   To log a model and register it with the specified name during an MLflow experiment, use the `mlflow.<model-flavor>.log_model(...)` method. If a registered model with the name doesn't exist, the method registers a new model, creates Version 1, and returns a `ModelVersion` MLflow object. If a registered model with the name exists already, the method creates a new model version and returns the version object.
    
    Python
    
        with mlflow.start_run(run_name=<run-name>) as run:  ...  mlflow.<model-flavor>.log_model(<model-flavor>=<model>,    artifact_path="<model-path>",    registered_model_name="<model-name>"  )
    
*   To register a model with the specified name after all your experiment runs complete and you have decided which model is most suitable to add to the registry, use the `mlflow.register_model()` method. For this method, you need the run ID for the `mlruns:URI` argument. If a registered model with the name doesn't exist, the method registers a new model, creates Version 1, and returns a `ModelVersion` MLflow object. If a registered model with the name exists already, the method creates a new model version and returns the version object.
    
    Python
    
        result=mlflow.register_model("runs:<model-path>", "<model-name>")
    
*   To create a new registered model with the specified name, use the MLflow Client API `create_registered_model()` method. If the model name exists, this method throws an `MLflowException`.
    
    Python
    
        client = MlflowClient()result = client.create_registered_model("<model-name>")
    

You can also register a model with the [Databricks Terraform provider](https://docs.databricks.com/aws/en/dev-tools/terraform/) and [databricks\_mlflow\_model](https://registry.terraform.io/providers/databricks/databricks/latest/docs/resources/mlflow_model).

## Quota limits[​](#quota-limits "Direct link to Quota limits")

Starting May 2024 for all Databricks workspaces, the Workspace Model Registry imposes quota limits on the total number of registered models and model versions per workspace. See [Resource limits](https://docs.databricks.com/aws/en/resources/limits). If you exceed the registry quotas, Databricks recommends that you delete registered models and model versions that you no longer need. Databricks also recommends that you adjust your model registration and retention strategy to stay under the limit. If you require an increase to your workspace limits, reach out to your Databricks account team.

The following notebook illustrates how to inventory and delete your model registry entities.

#### Inventory workspace model registry entities notebook

## View models in the UI[​](#view-models-in-the-ui "Direct link to View models in the UI")

### Registered models page[​](#registered-models-page "Direct link to Registered models page")

The registered models page displays when you click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in the sidebar. This page shows all of the models in the registry.

You can [create a new model](#create-a-new-registered-model-and-assign-a-logged-model-to-it) from this page.

Also from this page, workspace administrators can [set permissions for all models in the Workspace Model Registry](#permissions).

![Registered models](https://docs.databricks.com/aws/en/assets/images/registered-models-c97430c6ce709cd846c596fc421ae25b.png)

### Registered model page[​](#registered-model-page "Direct link to registered-model-page")

To display the registered model page for a model, click a model name in the registered models page. The registered model page shows information about the selected model and a table with information about each version of the model. From this page, you can also:

*   Set up [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).
*   [Automatically generate a notebook to use the model for inference](#use-model-for-inference).
*   [Configure email notifications](#email-notification).
*   [Compare model versions](#compare-model-versions).
*   [Set permissions for the model](#permissions).
*   [Delete a model](#delete-a-model-or-model-version).

![Registered model](https://docs.databricks.com/aws/en/assets/images/registered-model-06d672354a4be8e01a322469985ab787.png)

### Model version page[​](#model-version-page "Direct link to model-version-page")

To view the model version page, do one of the following:

*   Click a version name in the **Latest Version** column on the registered models page.
*   Click a version name in the **Version** column in the registered model page.

This page displays information about a specific version of a registered model and also provides a link to the source run (the version of the notebook that was run to create the model). From this page, you can also:

*   [Automatically generate a notebook to use the model for inference](#use-model-for-inference).
*   [Delete a model](#delete-a-model-or-model-version).

![Model version](https://docs.databricks.com/aws/en/assets/images/model-version-249eba0c289b4ce44186b9386e643ca0.png)

## Control access to models[​](#control-access-to-models "Direct link to control-access-to-models")

You must have at least CAN MANAGE permission to configure permissions on a model. For information on model permission levels, see [MLflow model ACLs](https://docs.databricks.com/aws/en/security/auth/access-control/#models). A model version inherits permissions from its parent model. You cannot set permissions for model versions.

1.  In the sidebar, click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models**.
    
2.  Select a model name.
    
3.  Click **Permissions**. The Permission Settings dialog opens
    
    ![Model permissions button](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA+gAAABHCAYAAACUAW1CAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAD6KADAAQAAAABAAAARwAAAABsyPVOAAAjMUlEQVR4Ae2dB5xU1dmHX2DpvfcOUgQUEGkWsCcqlohGCRZEiVGjUdEYo6L5MGo0qFFQQBFREUGxYcFGsCAlCEhTell6X1w6fOc5eHAYZnZ3dhfYXf6vzs7Mveeec+5z7/x+/N9ybr59zkwmAiIgAiIgAiIgAiIgAiIgAiIgAiJwVAnkP6qja3AREAEREAEREAEREAEREAEREAEREAFPQAJdN4IIiIAIiIAIiIAIiIAIiIAIiIAI5AACEug54CJoCiIgAiIgAiIgAiIgAiIgAiIgAiIgga57QAREQAREQAREQAREQAREQAREQARyAAEJ9BxwETQFERABERABERABERABERABERABEZBA1z0gAiIgAiIgAiIgAiIgAiIgAiIgAjmAgAR6DrgImoIIiIAIiIAIiIAIiIAIiIAIiIAISKDrHhABERABERABERABERABERABERCBHEBAAj0HXARNQQREQAREQAREQAREQAREQAREQAQk0HUPiIAIiIAIiIAIiIAIiIAIiIAIiEAOICCBngMugqYgAiIgAiIgAiIgAiIgAiIgAiIgAhLougdEQAREQAREQAREQAREQAREQAREIAcQSFig79y917bt3ONf+/Zl7QwWrt5qi9b8nLVOsnD0ms3bbcm6Q8ff5c5x797YJ8f5J2Lbd+2xuclbbE+c/uhr0887bf6qlES6VVsREAEREAEREAEREAEREAEREIE8RiAhgZ66Y4/dMmSKXfv8RLth0CS76rlv7eXxi9IUn2nxeuO7pfb25GVxm6Tu2G3v/y/ZdjiRezjs3anJ1v/TeYd0/fgHc63PWzMP2f7mhGXWc+AkY14ZteSNqXbX69Ms1Tk14tnEBevt4dGz4+1Od/vSFavt+1mHnke6B6qBCIiACIiACIiACIiACIiACIhAjiGQkEDfvXevLXQR756d6trDlzW3GzrXt8FfLrRxs9ccOKFNqbtstYtMR9sGFyVev3WH37z9F7F601kN7PrO9Q40JZK8dsv+NmxcvC7VHv1gji3fsM127/k1or1q03bbsm3XgeN27dnr9yOcN2zdeWB7dLuwg/mRBZA/Xz7nXAhbf31P3pBqr01YYovX/hpdJ3I+5KuFNnflwdHwNVu227qUX+ccetmUyvnutPzmxohKNWB8OAVjd2QbHBLMfVfEOYe2sd6TV6+z/wwdZd9OPdSpEKu9tomACIiACIiACIiACIiACIiACOQ8AkmJTqlQUn5rWLWk1alYwupVLmEfTF1h05ZusjObVbZXv15sr7hXPid8W9YqY30ua2ZFChawIeMW2dCvF1m5EoWtbvlitsGJ1yG92tow15b9N55R3174fL59OH2lF8xNqpW0ey5sYk+MmetE7i7rPXya9e3awmq5Y+95Y7rNX7PVELW3nt3QLmhVzd5zUfZR3y3zIvfk+uUN4X/viBn20+oU2+cE+M1nN7Aurav7SPwDo2ba5EUbrFqZok46m9V0fUZbYTen0kUK2ruu39vOO87vnuSi3OtTdlrlUkX8d5wCfd+Zbd/MW2f53Fw6N61kvS9oYkkF8tlbk5bZf8bOszLFC1ntcsX8OPndYDgmHhj1g01bttnMpbxf36meXdG+lu+PuWBE059wEfzdbn+SO6jP75rZ8TVK798Z52/7lsfbtm077KWRYxyXfdaxdfM4LbVZBERABERABERABERABERABEQgpxJIWKDvdQJw5rItLs17j610UV7E7sVtavga6qHjF9vTV7e0ak6U3vTiZBs9ebkhmAf/d6E91e1EL+gfeW+OLVi9PzK92UXBqc1O2b7bXvzvIhtw3UlOjJaywV8stO2u//submo9B022ft1aWa0KxbxgpzZ81K0d7AcnchHbHY6rYNt37bVFrpZ88A0nW8MqJey5sfNtpxPQI1272cu32H0jZ9gpjSrY57PW2Ixlm+wV5xzY4Y7pMXiSVXdzjTbGuLxdLfvqx7XWw2ULlHRifeTEZdbFOQPmuHrypAL57e1Jy+1/izbayzee7KP3vV6aYs1qlrF2Dctbv49/sj6XNLOWdcrYkx/+aOtc5kCRJOeoGL/Q1rgMAea1xEXnbxs21Tq6edGfV/FuIv0/nW9t6pazu7s08WMkr09NV6Az/zM6tLJNKVut/7DRVqFsaWtUb7/wjz43fRcBERABERABERABERABERABEciZBBIS6KSEk+o9eNwCK14oySa4aO99XZraaY0r2vAJS1za9k57z0XUabfRpXBPW7LRCVMXcXeiuU2D8p5Atw61nWh2EWRntMOKuoh1Cxdx7/vOLC9Yu7SqbjWcIF/uUs2JPJcoUsBF5c0mLVxvhZyY7f/ZAtuxe48lb9rm09DppaMT6s1q7o80T3TtCrgDBrh2O107HAnzVm3187modQ2r8UvUvEvL6rYqRjo+6fQtnNhe7ET/+DlrndAu61L7t9q1p9a16Us2+blMmLfeC/Yg8M9rXsWmLNxgZYoVtKqli9hZzSv7c+vWsbZ9N3+d7XaODY7Z6tLwB36xwIn6vT7N/ceVKX6u9ksG/ymNHMtvHcvtu+ycZlWsk4vMZ8RWr9tgE6fNMqLpNapk7JiM9Ks2IiACIiACIiACIiACIiACIiACR4ZAQgKd6Dkp6Y9c3sLqu/T2Hm7BtBQnJLF87r+KTph2aFjBp1m3qlvWqpctatRzU6NNVDq/U9tLnejdEbESutvs08IH9jjJpXdvsC9mrbar3SJ0z17T2kW3i/q+C+TfXyqPoG9crZS1a1CODHFr78YizZ5oehIK3hk6d3+7kgfatXPtGlYp6dPiSU0PFvk5bAvvBZPy2eVta9oItzAcUXgyAZgPDDBS2SNXdCdiT0o6L9LTgyHEyRJgdpx/46qlrG39cn4ubVyfOAK+X7wxNHd1/fWsc5OK9uWcNfZ/LoV+istQuOv8xgf2x/rAInH9Xhxh9WtXt15XXmQFCyZ0WWN1qW0iIAIiIAIiIAIiIAIiIAIiIAJHmEBCi8QxN6LLBZzQpE779vMa2bBvlvjoclsnNne6xc0QvdSoT3HR9QWuBhxxXMy1/aNLAX/S1ZQP+nKBFXLiF/PC1X1c59K+73xtmpUqmuTqsuv66PwGlxZe2EXfN7qF44hA0+/pLlI/d8UWl+5e3Eq7SPVYV7O+z4lf6q6DKKbn01wUeq6LTNd07agDHztjpRfWp7rt1IcjiL9z0ey33Aryv+h6P5/wh3mRNn9a40q2YlOqvfrtYrvS1YozBgu3odGpOR/tatSnub6mOMfCR24uHRtXsKauXnzTz7t8Pf48N4fnP1/goub7F6Tr3KSS/eQWmaMEoKKrZf/EHRNEPmNij7gsgmkuSn+FS7E/yTk5kt0CeelZ8qq11rh+bfvjVRdLnKcHS/tFQAREQAREQAREQAREQAREIIcSSCjUijA/zolvouhYGxcJvuDEavbJjFV+YTYivc+6x5ahNZu4dm1dWnvxwkn2VPdWfgE4wsi3nNPQXnAp3lg1F2EvUjC/lStZyBq59ve7BdSIfp9/YlUvjoliX3daXRvgRC416Kwazyrtt7wy1Yv3rq72HQFerkShgxZ76+EWX2PV+FuH7m/3O9eONueeUMWvws4CcvTH3MuVLOznEvmndsVi3gFAlPxSd+xsV3fewEXgWVmddH3E9Pktq/kU/PuYszuxa1z6+xlN96e1P+QWdnviw7n2jnuMW1tXT17QpeXjYKCuPXnjNl97XrhAAX+eVcsU8c9ir1epuJ8CToH+n8234e4RdNXdQnbpRc85qH2rZv4VeQ76LAIiIAIiIAIiIAIiIAIiIAIikLsI5HPR51/zsTM5d9K+Qz054pW0biLs2AaX3n738Ol+tXXSuwe6x7IVdML3sStPOGQ0jqUvBG2kkR6fzzkHiI5j212knjY4DNIyHlfGAmzR7VggrrBzDGSHEQFnFgVdtD/S4p0LbRifOeEAiGfMPTCM10bbRUAEREAEREAEREAEREAEREAE8g6BbBHoaeFA/n82c5VLLV9ue5xwr+tqxnu5x6qVjxG5Tqsf7RMBERABERABERABERABERABERCBvEzgsAv0SHiI9Vg135Ft9FkEREAEREAEREAEREAEREAEREAEjkUCCdWgZxWQxHlWCep4ERABERABERABERABERABETj6BPbudU+r2rPn6E8kl80gKSnJBa3jlzofUYGey9hpuiIgAiIgAiIgAiIgAiIgAiIgAlEE1q9fb5s2bYraqq/pEQjCvEKFClaqVKmYzSXQY2LRRhEQAREQAREQAREQAREQAREQgWgCGzZssM2bN1uNGjWscOFDn4gV3V7fDyaQmppqycnJVsA91at48f1P8opscfDS45F79FkEREAEREAEREAEREAEREAEREAEfiHAA8CInFerVk3iPJN3RbFixaxixYqGoyOWSaDHoqJtIiACIiACIiACIiACIiACIiAChxCg9rxgwYKHbNeGjBMg82D37t0xD5BAj4lFG0VABERABERABERABERABERABETgyBKQQD+yvDWaCIiACIiACIiACIiACIiACIiACMQkkPAicdQdBAur0IXv0e+JtI0+Nvp76Cu9MTkuVttY26LHiDw21j62Mf727dtt1apV/jP1F8dqigf1J9ROkKIBh4xcGxiSFrNixQrbuXOnr78oWbIkm2UiIAIiIAIiIAIiIAIiIAIicEwTSFig/+tf/7Kvv/7a8ufPb3/961+tXbt2MQFOnz7dHnroIf9svJYtW1qfPn1itsvIRsTwXXfdZVu3brWqVavav//9bytatGjMQ5955hn77LPP/L477rjDOnXq5Of7xBNPGAX5ffv2tbp168Y8dvbs2fbAAw/E3MdGnvPXr18/Ly67devm+xs5cqQ1bdo07jF5eceLL75ocOX8P/zwwwwvFLFlyxa7/PLLbcGCBfbII4/Y9ddfn5cx6dxEQAREQAREQAREQARE4KgQQD/t2rXLypYte1TG16CJE0hYoCO8gwAmahpPoL/66qv28ccf+6hqiF4nPr39R/z88882btw4S0lJ8cvRd+3a1c4444xDulu3bp0NGjTIlixZ4m/E3//+977NypUr/ZyJ1NJHPCMa/Pnnn/s5h6L9yLmzDUcDEWBEJoKd17FqO3bs8Bz44UdySo8HbbkOMKQPmQiIgAiIgAiIgAiIgAiIQPYSWLt2rQ0cONC2bdtm11xzjTVs2DB7B1Bvh4VAwgKddG5Smnn/4osvbNmyZVazZs2DJsfNMHbsWCtRooRfnS6rKeCkTjMm3h/SokeMGBFToH/66af+mXJEyklD59lyGO8czyutNGyyAmiDAL/lllusRYsWBwlPhGWdOnXs+++/9xkEtD+WDZYwyAyHcFxa1+NYZqtzFwEREAEREAEREAEREIGsEFi+fLkRqCTIuHDhwqMi0AnKvfHGG14Xoglr165trVq1OqDTsnJ+kceiEXv37u0dEfSfUVu6dKnP6CWrt1y5chk97LC2S1igh9kgrEg9f++99+zmm28Om/07kXNOtlChQv47bYk0kxJNlPv444+3iy666MAxRGCHDh3qH3jfoUMH6+TS0uNZUlKSffnllz5KzgUORv9vvvnmQYI67EvkPUSCzz77bDv11FNjHoqAj2VEhMeMGWPfffedjw6TYXDWWWdZ586dffMpU6Z4xwUpJnixcCRgpMn/9NNPnsvFF1/st5E1MGTIEN/P+eefbyeccILfHv7MmDHDp5XT1wUXXGBvvfWWTZ061deCX3nllda8eXObOXOmZ0JGAWn9pJJHO1MmTpxoH330kb9ezIdyhC5duvja8DAW72ROjB492jtA6tWrZ1dddVXc2vvk5GR7++23jTlizZo1s0svvfSQsf1O/REBERABERABERABERABEch2AvwbHB2xceNG69ixY7b3n5EOcRJQYnzuued6Uf7DDz94gU7ZdNCKGeknvTYE/5o0aWKlSpVKr+lB+4sUKeI1WFYDygd1msUvmRLoiNjy5csbkfJ33nnHevbs6SPPzAUPzahRo3xUlTaIeAxopI8j3BCbZ555pveksA/het999/kIOanx8QxxDnQEII6BW2+99UBTBOSkSZOsdOnSXjiSypEVSzR1HYdEr1697Ntvvz2Qto1j4oUXXrAePXrYP//5T8+Ld6L0iH9+NDgnuGl//PFH//2cc87xwh3B/uCDD3rHRqwfFGL84Ycf9kL6tdde804BGHNzUQ9+++23+34XLVrkb36yCChNwINVo0YN78igfpx6/pCuDy+Ox5FCOgzzwz744APvhOHHjXcKNvTTuHHjQ0Q6zombbrrJOxxoBwPmNXjwYBswYICdcsopvk/9EQEREAEREAEREAEREAEROHwE+Hf9b37zm8M3QAZ6JrBJUPWpp57ya4itXr3aBxenTZtmJ598steBZEFXqFDBKE+mJJl1wdB7BHYR8QRwyWBGz3AcgV706LvvvuuDkAQC0Yn169f3WpBp0Y5+y5QpYwRAK1as6FP90a4EL9u2bWudXFCYAOVxxx13wFlAgBMtxbj0W6tWLb8o9jfffOPr+Hlv1KiRD2iicSiRJoi5fv16n+F90kknZYBK2k0ylaONSCMyTB0DsBBlwfhOVJYLcd5553nRDUCE2hVXXOGhAzxEVzlu/PjxXtjj9QBULKMPhO1ll13mRSEgSGMPRhQaQMyLaHGoIQ/7E33HscA88frwIpWf/qON82Ju9957r3311Vfe6YCzAUcD54sh0l9//XXvuYILc8OhgM2ZM8cL9+LFi3tnxvz58/12OJLS36BBAx/V9hsj/nCDslAekXZWU8cLhSjHQcEK6Xfeeae/Sfv37+9vdm4+blTEPMaN99hjj3mG1PMz30cffdRH4PFssSgf9eH8MHAUIOJJ++A8n332WX8dKWPgx4Bxg27evNmPyzmQJYHIf+mll6xNmza2ePFiu+eee/xcmbtMBERABERABERABERABETg8BEgEEiGMf8e59/0R9PQCljlypUN3YOeREP++c9/9pqD0um//OUvPhBIwPO6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FLRQRuZHuTOL2cEx2hIW6NEdJPId0UpaNeJtxIgRvkifVGqi7/GEaCL9q60IiIAIiIAIiIAIiIAIiIAIiMDhIXCsC3QCwyzyff/99/uV4gnwUqpN1jECPaMiPS2BnuVF4hK59ES88TyQt0/0mOgyJydxnghFtRUBERABERABERABERABERABEThSBBDiBJZZh4tSa9bXIoObsmUEO9nI0aXHmZ1bwjXomR2I4zgZFg8jDZ0T4hnq8dLIszKOjhUBERABERABERABERABERABEch+AgRXiaQfK4Y4Z8217t27+zLka6+91gecKSFmxXfW4YIJ625l1OAXL0h9RFPcMzphtRMBERABERABERABERABERABEch5BHiUNOtg8QiyY8FYfwwRvmjRIi+qU1JSfKC5Z8+eNmDAgLhCOy02y5Yt833GYnhEI+hpTVL7REAEREAEREAEREAEREAEREAEcjYBFuFGYLJ4Wqznm+fs2Sc2OyLdW7Zs8S+edkUmOAu78UQrFg1nHxH2sEh6RnpnoWysfPnyMZsrgh4TizaKgAiIgAiIgAiIgAiIgAiIgAjEIoBQ5SlPiPS8bAh0VmvnfElh5zsRdSLfPMaap4yxjQh7Rg2nBrXr8VLcFUHPKEm1EwEREAEREAEREAEREAEREAER8KuVH4triSHUebwcUXOi55UqVfLrrJHyn12mCHp2kVQ/IiACIiACIiACIiACIiACIiACeZoAWQNEz0PknPT2eNHwzICQQM8MNR0jAiIgAiIgAiIgAiIgAiIgAiJwTBJAnGenKI+EeESfgx45sD6LgAiIgAiIgAiIgAiIgAiIgAiIQG4jcLjEORwk0HPb3aD5ioAIiIAIiIAIiIAIiIAIiIAI5EkCEuh58rLqpERABERABERABERABERABERABHIbAQn03HbFNF8REAEREAEREAEREAEREAEREIE8SUACPU9eVp2UCIiACIiACIiACIiACIiACIhAbiMggZ7brpjmKwIiIAIiIAIiIAIiIAIiIAIikCcJSKDnycuqkxIBERABERABERABERABERABEchtBCTQc9sV03xFQAREQAREQAREQAREQAREQATyJAEJ9Dx5WXVSIiACIiACIiACIiACIiACIiACuY2ABHpuu2KarwiIgAiIgAiIgAiIgAiIgAiIQJ4kIIGeJy+rTkoEREAEREAEREAEREAEREAERCC3EZBAz21XTPMVAREQAREQAREQAREQAREQARHIkwQyLND37TPjJRMBERABERABERABERABERABERABEch+AkkZ7jKfmftfJgIiIAIiIAIiIAIiIAIiIAIiIAIicBgIZDiCLnF+GOirSxEQAREQAREQAREQAREQAREQARH4hcD/A8fxKvJ+PvIyAAAAAElFTkSuQmCC)
    
4.  In the dialog, select the **Select User, Group or Service Principal…** drop-down and select a user, group, or service principal.
    
    ![Change MLflow model permissions](https://docs.databricks.com/aws/en/assets/images/select-permission-f927290101bdc4d7afda05207b1034f9.png)
    
5.  Select a permission from the permission drop-down.
    
6.  Click **Add** and click **Save**.
    

Workspace admins and users with CAN MANAGE permission at the registry-wide level can set permission levels on all models in the workspace by clicking **Permissions** on the Models page.

## Transition a model stage[​](#transition-a-model-stage "Direct link to transition-a-model-stage")

A model version has one of the following stages: **None**, **Staging**, **Production**, or **Archived**. The **Staging** stage is meant for model testing and validating, while the **Production** stage is for model versions that have completed the testing or review processes and have been deployed to applications for live scoring. An Archived model version is assumed to be inactive, at which point you can consider [deleting it](#delete-a-model-or-model-version). Different versions of a model can be in different stages.

A user with appropriate [permission](#permissions) can transition a model version between stages. If you have permission to transition a model version to a particular stage, you can make the transition directly. If you do not have permission, you can request a stage transition and a user that has permission to transition model versions can [approve, reject, or cancel the request](#str).

You can transition a model stage using the UI or [using the API](#transition-stage-api).

### Transition a model stage using the UI[​](#transition-a-model-stage-using-the-ui "Direct link to Transition a model stage using the UI")

Follow these instructions to transition a model's stage.

1.  To display the list of available model stages and your available options, in a model version page, click the drop down next to **Stage:** and request or select a transition to another stage.
    
    ![Stage transition options](https://docs.databricks.com/aws/en/assets/images/stage-options-6e0af02811649b9cdd785a100359fcbc.png)
    
2.  Enter an optional comment and click **OK**.
    

#### Transition a model version to the Production stage[​](#transition-a-model-version-to-the-production-stage "Direct link to Transition a model version to the Production stage")

After testing and validation, you can transition or request a transition to the Production stage.

Workspace Model Registry allows more than one version of the registered model in each stage. If you want to have only one version in Production, you can transition all versions of the model currently in Production to Archived by checking **Transition existing Production model versions to Archived**.

#### Approve, reject, or cancel a model version stage transition request[​](#approve-reject-or-cancel-a-model-version-stage-transition-request "Direct link to approve-reject-or-cancel-a-model-version-stage-transition-request")

A user without stage transition permission can request a stage transition. The request appears in the **Pending Requests** section in the model version page:

![Transition to production](https://docs.databricks.com/aws/en/assets/images/handle-transition-request-af93986026a2d0e5e9f76c4bd9ab0214.png)

To approve, reject, or cancel a stage transition request, click the **Approve**, **Reject**, or **Cancel** link.

The creator of a transition request can also cancel the request.

#### View model version activities[​](#view-model-version-activities "Direct link to View model version activities")

To view all the transitions requested, approved, pending, and applied to a model version, go to the Activities section. This record of activities provides a lineage of the model's lifecycle for auditing or inspection.

### Transition a model stage using the API[​](#transition-a-model-stage-using-the-api "Direct link to transition-a-model-stage-using-the-api")

Users with appropriate [permissions](#permissions) can transition a model version to a new stage.

To update a model version stage to a new stage, use the MLflow Client API `transition_model_version_stage()` method:

Python

      client = MlflowClient()  client.transition_model_version_stage(    name="<model-name>",    version=<model-version>,    stage="<stage>",    description="<description>"  )

The accepted values for `<stage>` are: `"Staging"|"staging"`, `"Archived"|"archived"`, `"Production"|"production"`, `"None"|"none"`.

## Use model for inference[​](#use-model-for-inference "Direct link to use-model-for-inference")

After a model is registered in the Workspace Model Registry, you can automatically generate a notebook to use the model for batch or streaming inference. Alternatively, you can create an endpoint to use the model for real-time serving with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

In the upper-right corner of the [registered model page](#registered-model-page) or the [model version page](#model-version-page), click ![use model button](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAALMAAAAfCAYAAACsyvxmAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAs6ADAAQAAAABAAAAHwAAAABxsES1AAAMaUlEQVR4Ae1bCXCURRb+5sokk4Tc932QkARC7gCChlNORVZTUIiirOAGQQWV3S1FFwRBLSyJUSh3cRVWpTxwl0V3yVKIIrgkahASkCP3BnIQM7kz577uyRxJJskkDgao/1XN//fff/d7r79+/fq9nhlR9puF+rLSnyGQgMDNjoC4oqLpZh+DoL+AAEdArNPqBSgEBG4JBMS3xCiEQQgIEAKCMQtmcMsgIBjzLTOVwkAEYxZs4JZBwC7GrNdpwT7WSKfVQK/XWXt1Q9cNRW+dbuAx6vV6aDVddhnvQFhbE2BP2db430h1djHm4AA54sLlfcYlkgLpsc5QuFHhJqPMOFd4ejnYpPW4CAU8Pa2PkRmxTNaG+6eG2MRrsEbBAQ4ID+qLtbV+9pZtTcaNVGcXY975UDr25NzeZ1xhQa54a9UUPDo9us+7G73i9RWTsGZ2jE1qvp0zBX9YmGC17SNzR+PESwvxxIJEq++HWvnGignYtXKSTd3sLdsmoSPYyLo7uU4KsXBDq+qgLbcTFHtALJVDKneBSCTiEnUaFTRdbRSyaCCWOEAid6a7dRXVHU30Tg6dVk0fFW8vpfYadRt0ahXxlEDq6EL1MgNvaqfpbCXeKjrDkULqoIBE5mQaqUbVDh3Ti0gsdTTVGwtD0c3Yh/HMSvBFl1qLCes/g0zuxkMuTWeLQRbpKJE58nGKIKI6FbTqdohJL62qjXQk/aU9d4d1730HqdiAF8PKSBxTemBjYmOzJpu1NY5Tr9N14+9MWIm5Xup2JemiIPw6IGIY0dywsIbhptOpIZKQvlInrjPnNYB89p6FOJou6qsmXMVi6iuHhHRj8nj/bsx768JfDuNi3VKGwciWLs6uIry0eCLSor1p6oBLtc1YlnuSEJbxibxvSgB+N2csXBylqG/uxKb9hTj1UzsBK+nDPn/rfBw/dxXjIzwR6u2KmsY2PPXuSWxdOhPhvi7oVGnx7AeF+KaETYQGs1I88cd7Z8BZLoNKo8WB/5bhlU9+4gCzBbb5gSRMHRdIckT4uqSmhzxmZEPRzdh5+28zERPgRhxF+M+W+Zi96Sv4ewJv58yFn5sTdDTZp8uvYeWukxDpnZA9PRIP3x6OfV9ewKrZCXgj/zI++rLSyI7fc2aOhsJBgtW7i5D32CRotVqyExHSo32Yf8Dhoiq88ME59JY9Z9PX3JC3PJiErLFBkElEKK9vxcN5X6OzUw5ffxfsf2wq/nz4HO7PikFZQzty3ixEZJAEO1fMhberI1o7Ndh//DJ2f36JG/RA8sW0GPSSTrz/TBZig92hoS/n2FjX7/0ene2GRdWfLj0GPIQHu4QZtsrLfSgV6aN98ElBDYoqmxEb4I7cFRm8+6IpQdiwKBns+8iDP9TC0UGKvJVTMCbCxSp7LwJ3YWY4XJ0cUfy/FoR402Ssn4lALwVOXGyEXCbG9mUZxE+PpBg3bL0/E+0qHfZ8VYHyhg4snhyNJ++J5bw3Lk3EvNRQMgYRLl5txazxISbvxxoMVTejwt+WNqGDFpWWvOCxnxrJbdIi+v1MeLrI8f7Jahw734CUSG98tD6Le8YgDyd4j3LEE3clokujw+X6DiMr0z3a3xWRfq78OdTbGZPj/JEW5YP8s/Xk8YD5aWFIjfdGb9lsV8zLycSclFDUNXfh39Q+wtcVR56fQwhpuANxcZRx2W7ODigoU8LdQ4oPn5wBLxdHHCmpR0OrCitnjcFjdxtwG0g+8+j/2DANcSEeOFrSQPOt5Avu3ZxJfKwD6WIa7BALv6pnjgtyh7KtC9v2nuBhwap7EhHs6cxVfnxuPN+Opz5ziD9vVshQsG0e1s6JxepdRVaH9XObCnPJ2zE69Nxk+JAhZL9RiNqaFmxcEo/5KYGQOEnx3KJE7rUWvPQN9GQku3ERn2+cguxJkXj9YBkWpIeC8brzBQOv+7LC8PS80SaZw9GNdT54vAqLMwJJLzm27S/GuoVj+CJZve8MCs7Ucf5blydiBoUinj7mkOfTwhpqX2KSP1CBeeNp276BStmF13wUyH9mEiZEe+Ktf5b2kK1wd8DEWD+crWrCAy9/yVkeSQ/BjgdSsWhyKIqqWnld1bUO/OblE6BtA3mrkvgCmbftKOqvNvP3h7fMRvbEcLz1eQV/7k9+W5cGgTS3h4qu4k9/O8vb7nw0FWnh7hhMlwPHe+6MvLMNF7sYMzkeTswLsi3VRGykRGw7ZXTodB3uTvFHwc57cbayER+fKMXuz85SbKuAM3kFFlvuWX8Hb8sujB/zuP1RSbXS9Kq5Q41RTjJuyKzyitIQ/zqRMfu7O6JW2cEN2dihmPreEeeLgECKy8mlFZaS5+ymTwuvmI2Z9q7h6GbkZXkfG+LOF1VBcb2p+mhxHTfmtAgPU92Of102lQcrKNtV3JBZO2U97d9EbFH3pswoim+I/NwcTRhLKdRgNC7U3WTMH52q4obM6tkuwKZu+9Jk9shJIZfCiXZNI/UnPz3SIO+L01eNTbF213e8nJXiy+/96XIAI2jMrbQKpRIxxA5kgJRfGSnWT8GLDa1qbpib9hagujEBdyUHICncG8kR3uQVa/Hkh+d5O3IGUJBRG+kSbfkXaw0ew1hneWcGbElqrfXzbJlUjMbWnue80u41x2JXRtXXzMmUppUM37D+IKEtl9FQdeOdel1cabExHfUU5xqTIKnYIEhn4QSYl7WVVLTT2EJGA2fJtiXGF8jjltSYMa6nEMRIcorNmUOxbF/dyLDpBoca9ifflxYNI5bLGIknn+ouWmyhvGowXYz9bL2bl5itPay0u1TbjoRgN0yLd0d+IXkdylz1GjWyxnjx1j9UtkBCRpq7bDxyvziPd764QBm7FHvXpCNztB8tgBJuPE0UgiyhLY2dZGgpA978YDIu1hs8rBWxNlexxCWK4kzGk52gsNOP2MBR3LDOUuzOKIM8V572AuV/ImTSOFj8yUjborKbbmy3CPdxBkuE21rIICiOvW20wSOfqW7B2KD+dyGDNsO/llwxGBVLml/8oJjPkchBjdyHMigRNxucpYTGVg2CKG5evP0IJGJHfnK0bHoYYoINXteybe/ypTpDvD8jzhN7Ksv46y3LkzGFYvw1+wxhx1B06c3f2rNdEsC3j1XwUGLz4lSe9SdFOmLj0nGYnhgEJXnPkgvXoCODSgzzwmvL05EQJoeDuBUeLg7ooNBC16XFj1VKBHgosOG+eITQLpS3egJPylhW/Evp6LkGSgglyJkfTcmYEkuygnmidez8NWjb1LjS1In4YA9kjXfnur24OKWHSNt0swivevQ2P7xzvJo/5C5PpROaFsSFyTBtbCAaaMHUXTF7R3MP+5WKKSlup2R0XkoIn6PkKCcc3DAdE2L8UNNk9saWElnszhb1X9bcxudk/aJYPD5/HIK8Bl90hyjJ19J2tmJ6DBZM9KO43B+zk0IoiVRjOLpY6tVf+ZdbCnFmE7Fm7xm8TgbMTiSM1NSuxrwd3xof8eaRMqybE4V3107ldSxjf4WOeRjlvPcjDqzNQPZtUfzD6r4vV2JffikrWiV2FmoiOrvU0WmEkegUlRfpNBtbPz5PcaEbVswYwz/sRQUdPT37IXkoolV/PY39q9Pw6oMT+TPTm4csdA7MaDDdmFR999kp72Bx0TNr6HbzRRQr//37K5Q3BODUy4t4K3ba8cie7gSXdrRBielk3DZ42UqPbr0tZbM4aTVhvHv5eNMcsWhh99FyPn8R4W4GRt192QPDPiPKAxOivPHphjv5+2t0ovHoO6fNbc2QG+rYlXgwB/U04fvqkgQ8n53K3zGnsYr1HUQXM6OhlUTpT+WbA6Ch9bXa2tPPGfGBrjhJ3ph5vd4kIg85LdkPZZSslJb1/ZdLUPAoCgmc8V15E9oos7YnMd3GEv8fKpRoIWO2JBElQ4kxXmBxeBktImtkL92kdLoxkU4cyuvbUEXhhSlAtybUznVsnPEkexSd5Z+60Ahtr7zDmjgFHRmmRbrzOauiI7YhEZ2BR4W5obyurY89DEeXgWTb3ZgHEia8ExC4ngjYsK9dT/ECbwEB+yEgGLP9sBQ4jTACgjGP8AQI4u2HgGDM9sNS4DTCCAjGPMITIIi3HwJicff38/ZjKXASEBgZBMShIaNGRrIgVUDAzgiI180Kpd9CWPsax86SBHYCAtcZAVFHR4e+iH4XseNwJSqrmunHJHb9QvA6qy+wFxCg30yRM2YRhoj+dqMngxYwERC46RH4PwEtU5HMzLsfAAAAAElFTkSuQmCC). The Configure model inference dialog appears, which allows you to configure batch, streaming, or real-time inference.

important

Anaconda Inc. updated their [terms of service](https://www.anaconda.com/terms-of-service) for anaconda.org channels. Based on the new terms of service you may require a commercial license if you rely on Anaconda's packaging and distribution. See [Anaconda Commercial Edition FAQ](https://www.anaconda.com/blog/anaconda-commercial-edition-faq) for more information. Your use of any Anaconda channels is governed by their terms of service.

MLflow models logged before [v1.18](https://mlflow.org/news/2021/06/18/1.18.0-release/index.html) (Databricks Runtime 8.3 ML or earlier) were by default logged with the conda `defaults` channel ([https://repo.anaconda.com/pkgs/](https://repo.anaconda.com/pkgs/)) as a dependency. Because of this license change, Databricks has stopped the use of the `defaults` channel for models logged using MLflow v1.18 and above. The default channel logged is now `conda-forge`, which points at the community managed [https://conda-forge.org/](https://conda-forge.org/).

If you logged a model before MLflow v1.18 without excluding the `defaults` channel from the conda environment for the model, that model may have a dependency on the `defaults` channel that you may not have intended. To manually confirm whether a model has this dependency, you can examine `channel` value in the `conda.yaml` file that is packaged with the logged model. For example, a model's `conda.yaml` with a `defaults` channel dependency may look like this:

YAML

    channels:- defaultsdependencies:- python=3.8.8- pip- pip:    - mlflow    - scikit-learn==0.23.2    - cloudpickle==1.6.0      name: mlflow-env

Because Databricks can not determine whether your use of the Anaconda repository to interact with your models is permitted under your relationship with Anaconda, Databricks is not forcing its customers to make any changes. If your use of the Anaconda.com repo through the use of Databricks is permitted under Anaconda's terms, you do not need to take any action.

If you would like to change the channel used in a model's environment, you can re-register the model to the Workspace model registry with a new `conda.yaml`. You can do this by specifying the channel in the `conda_env` parameter of `log_model()`.

For more information on the `log_model()` API, see the MLflow documentation for the model flavor you are working with, for example, [log\_model for scikit-learn](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model).

For more information on `conda.yaml` files, see the [MLflow documentation](https://www.mlflow.org/docs/latest/models.html#additional-logged-files).

![Configure model inference dialog](https://docs.databricks.com/aws/en/assets/images/configure-model-inference-63344ba4db0f7a49e545dfc3ee410b0a.png)

### Configure batch inference[​](#configure-batch-inference "Direct link to Configure batch inference")

When you follow these steps to create a batch inference notebook, the notebook is saved in your user folder under the `Batch-Inference` folder in a folder with the model's name. You can edit the notebook as needed.

1.  Click the **Batch inference** tab.
    
2.  From the **Model version** drop-down, select the model version to use. The first two items in the drop-down are the current Production and Staging version of the model (if they exist). When you select one of these options, the notebook automatically uses the Production or Staging version as of the time it is run. You do not need to update the notebook as you continue to develop the model.
    
3.  Click the **Browse** button next to **Input table**. The **Select input data** dialog appears. If necessary, you can change the cluster in the **Compute** drop-down.
    
    note
    
    For Unity Catalog enabled workspaces, the **Select input data** dialog allows you to select from three levels, `<catalog-name>.<database-name>.<table-name>`.
    
4.  Select the table containing the input data for the model, and click **Select**. The generated notebook automatically imports this data and sends it to the model. You can edit the generated notebook if the data requires any transformations before it is input to the model.
    
5.  Predictions are saved in a folder in the directory `dbfs:/FileStore/batch-inference`. By default, predictions are saved in a folder with the same name as the model. Each run of the generated notebook writes a new file to this directory with the timestamp appended to the name. You can also choose not to include the timestamp and to overwrite the file with subsequent runs of the notebook; instructions are provided in the generated notebook.
    
    You can change the folder where the predictions are saved by typing a new folder name into the **Output table location** field or by clicking the folder icon to browse the directory and select a different folder.
    
    To save predictions to a location in Unity Catalog, you must edit the notebook. For an example notebook that shows how to train a machine-learning model that uses data in Unity Catalog and write the results back to Unity Catalog, see [Machine learning tutorial](https://docs.databricks.com/aws/en/machine-learning/train-model/scikit-learn).
    

### Configure streaming inference using Lakeflow Spark Declarative Pipelines[​](#configure-streaming-inference-using-lakeflow-spark-declarative-pipelines "Direct link to configure-streaming-inference-using-lakeflow-spark-declarative-pipelines")

When you follow these steps to create a streaming inference notebook, the notebook is saved in your user folder under the `DLT-Inference` folder in a folder with the model's name. You can edit the notebook as needed.

1.  Click the **Streaming (Lakeflow Spark Declarative Pipelines)** tab.
    
2.  From the **Model version** drop-down, select the model version to use. The first two items in the drop-down are the current Production and Staging version of the model (if they exist). When you select one of these options, the notebook automatically uses the Production or Staging version as of the time it is run. You do not need to update the notebook as you continue to develop the model.
    
3.  Click the **Browse** button next to **Input table**. The **Select input data** dialog appears. If necessary, you can change the cluster in the **Compute** drop-down.
    
    note
    
    For Unity Catalog enabled workspaces, the **Select input data** dialog allows you to select from three levels, `<catalog-name>.<database-name>.<table-name>`.
    
4.  Select the table containing the input data for the model, and click **Select**. The generated notebook creates a data transform that uses the input table as a source and integrates the MLflow [PySpark inference UDF](https://mlflow.org/docs/latest/models.html#export-a-python-function-model-as-an-apache-spark-udf) to perform model predictions. You can edit the generated notebook if the data requires any additional transformations before or after the model is applied.
    
5.  Provide the output Lakeflow Spark Declarative Pipelines name. The notebook creates a live table with the given name and uses it to store the model predictions. You can modify the generated notebook to customize the target dataset as needed - for example: define a streaming live table as output, add schema information or data quality constraints.
    
6.  You can then either create a new pipeline with this notebook or add it to an existing pipeline as an additional notebook library.
    

### Configure real-time inference[​](#configure-real-time-inference "Direct link to Configure real-time inference")

[Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) exposes your MLflow machine learning models as scalable REST API endpoints. To create a Model Serving endpoint, see [Create custom model serving endpoints](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

### Provide feedback[​](#provide-feedback "Direct link to Provide feedback")

This feature is in preview, and we would love to get your feedback. To provide feedback, click `Provide Feedback` in the Configure model inference dialog.

## Compare model versions[​](#compare-model-versions "Direct link to Compare model versions")

You can compare model versions in the Workspace Model Registry.

1.  On the [registered model page](#registered-model-page), select two or more model versions by clicking in the checkbox to the left of the model version.
2.  Click **Compare**.
3.  The Comparing `<N>` Versions screen appears, showing a table that compares the parameters, schema, and metrics of the selected model versions. At the bottom of the screen, you can select the type of plot (scatter, contour, or parallel coordinates) and the parameters or metrics to plot.

## Control notification preferences[​](#control-notification-preferences "Direct link to control-notification-preferences")

You can configure Workspace Model Registry to notify you by email about activity on registered models and model versions that you specify.

On the registered model page, the **Notify me about** menu shows three options:

![Email notifications menu](https://docs.databricks.com/aws/en/assets/images/email-notifications-menu-6c3b102ee1f8a7b08a4316db5085752d.png)

*   **All new activity**: Send email notifications about all activity on all model versions of this model. If you created the registered model, this setting is the default.
*   **Activity on versions I follow**: Send email notifications only about model versions you follow. With this selection, you receive notifications for all model versions that you follow; you cannot turn off notifications for a specific model version.
*   **Mute notifications**: Do not send email notifications about activity on this registered model.

The following events trigger an email notification:

*   Creation of a new model version
*   Request for a stage transition
*   Stage transition
*   New comments

You are automatically subscribed to model notifications when you do any of the following:

*   Comment on that model version
*   Transition a model version's stage
*   Make a transition request for the model's stage

To see if you are following a model version, look at the Follow Status field on the [model version page](#model-version-page), or at the table of model versions on the [registered model page](#registered-model-page).

### Turn off all email notifications[​](#turn-off-all-email-notifications "Direct link to Turn off all email notifications")

You can turn off email notifications in the Workspace Model Registry Settings tab of the User Settings menu:

1.  Click your username in the upper-right corner of the Databricks workspace, and select **Settings** from the drop-down menu.
2.  In the **Settings** sidebar, select **Notifications**.
3.  Turn off **Model Registry email notifications**.

An account admin can turn off email notifications for the entire organization in the [admin settings page](https://docs.databricks.com/aws/en/admin/admin-concepts#admin-settings).

### Maximum number of emails sent[​](#maximum-number-of-emails-sent "Direct link to Maximum number of emails sent")

Workspace Model Registry limits the number of emails sent to each user per day per activity. For example, if you receive 20 emails in one day about new model versions created for a registered model, Workspace Model Registry sends an email noting that the daily limit has been reached, and no additional emails about that event are sent until the next day.

To increase the limit of the number of emails allowed, contact your Databricks account team.

## Webhooks[​](#webhooks "Direct link to Webhooks")

[Webhooks](https://docs.databricks.com/aws/en/mlflow/model-registry-webhooks) enable you to listen for Workspace Model Registry events so your integrations can automatically trigger actions. You can use webhooks to automate and integrate your machine learning pipeline with existing CI/CD tools and workflows. For example, you can trigger CI builds when a new model version is created or notify your team members through Slack each time a model transition to production is requested.

## Annotate a model or model version[​](#annotate-a-model-or-model-version "Direct link to Annotate a model or model version")

You can provide information about a model or model version by annotating it. For example, you may want to include an overview of the problem or information about the methodology and algorithm used.

### Annotate a model or model version using the UI[​](#annotate-a-model-or-model-version-using-the-ui "Direct link to Annotate a model or model version using the UI")

The Databricks UI provides several ways to annotate models and model versions. You can add text information using a description or comments, and you can add [searchable key-value tags](#search-for-a-model). Descriptions and tags are available for models and model versions; comments are only available for model versions.

*   Descriptions are intended to provide information about the model.
*   Comments provide a way to maintain an ongoing discussion about activities on a model version.
*   Tags let you customize model metadata to make it easier to find specific models.

#### Add or update the description for a model or model version[​](#add-or-update-the-description-for-a-model-or-model-version "Direct link to Add or update the description for a model or model version")

1.  From the [registered model](#registered-model-page) or [model version](#model-version-page) page, click **Edit** next to **Description**. An edit window appears.
    
2.  Enter or edit the description in the edit window.
    
3.  Click **Save** to save your changes or **Cancel** to close the window.
    
    If you entered a description of a model version, the description appears in the **Description** column in the table on the [registered model page](#registered-model-page). The column displays a maximum of 32 characters or one line of text, whichever is shorter.
    

1.  Scroll down the [model version](#model-version-page) page and click the down arrow next to **Activities**.
2.  Type your comment in the edit window and click **Add Comment**.

#### Add tags for a model or model version[​](#add-tags-for-a-model-or-model-version "Direct link to Add tags for a model or model version")

1.  From the [registered model](#registered-model-page) or [model version](#model-version-page) page, click ![Tag icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEsAAAAZCAYAAAB5CNMWAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAS6ADAAQAAAABAAAAGQAAAADG2PsQAAAEHUlEQVRYCe1XWShtbRh+HCc3IpJChnJhvEGGpAxFkQwZM9y5wQU3UhQZilyZpchQhDKXkAxX7ogypIxJIfOcsM5639qrvU/svdfy+x21v9prfcPzvt/6nu+dtpEgNhiaXgz80gtlADEDBrJkGIKBLANZMhiQAf0tA/spaHV1Nbq6urTqGBgYgJeXl1bMdy7+b2SFh4fDyclJOmt5eTl8fHwQExMjzdnb20v9f7Fj9F2lg6urKzIzM1FSUvIuL1TRGBkZvbtGk7rWVYL64lR4be93A3xTUxOqqqq0yX3J2vPzM+rr60FW6ObmhqSkJIyNjWnsdXx8jLKyMgQFBbFl1tbWYnh4GNHR0bi/v2fs09MTyO1DQkJYT0ZGBpaXlzX0KBl86Ibd3d04OjpCc3OzEr2KZOiC+vr6EBcXh/j4eMzNzaGwsBCWlpYIDg7G4+MjcnNzsb6+jsTERFhZWWFiYgIXFxdM1OvrK+9bWlrKJBOWZAcHB5GWlobZ2Vl8ytXJDf9ujY2NgouLC//EDxd2d3f/hnx6TPorKio09LS3twuiJUlzl5eX/A2VlZU8NzQ0xOORkREJc3p6KgQGBvL89fW18Pb2xv2CggIJc3JyIrS0tAgiydKcks67bqhuFpubm0hJSeFbUZ//in5WVhZiY2MhHg5bW1vY3t7mbcj1qG1sbPBbPSlYW1trJAmKcxQPx8fH0dHRgb29PRAmJycHHh4eLK/0oZMsUvzy8gLxxpTuobfc/Pw8xxlyOSKNYg01lXsRaeR6xsbGGjqJDPVWV1cHX19f1NTUIDIyEqGhoejt7VWHKOrrJMvR0RE9PT2IiIhQtIG+QldXV8jOzmYraG1txcLCApaWluDg4AATExNW4+7ujvPzcxBWva2trakP4ezszOQQ+UQYESy6PMc3DaDMgVayvL29MTMzA09PT5lq5cPJ7ailp6cjLCwMtra2HLQPDw8lZX5+ftynAH57e8sWR+42OTkpYW5ubjA1NYWDgwPY2dlxohBjIa+r3FgCy+x8mA1TU1P5NmTqUwwXAz7LUpVvamrKrt/Q0KChz9/fn7OhGKwxPT0trZGbkSVSIyssLi6GmZkZioqKYGNjg9HRUV4LCAjgt+KHkqzwX8i8lw3FMkAQrZmzGa23tbUJYjAX8vLypC0p24lJRxBLG6Gzs1PY398XxEAuZUMCrqyssBzpoB9ly/7+fkmH0s63VfAf3a54EI5L5ubmUqxSYXd2dtiiqNhUhQbCU112dnaGxcVFFZTfDw8PoELXwsJCY17p4J8jS9tB7u7uuDglTHJyMrsaFa5UpObn57OLapP/7NqPIosOS/8q6C/R6uoqB3mysKioKCQkJHyWC53yP44snSf6QoDW0uEL9/2Rqg1kybg2A1kGsmQwIAP6B1GoWkBNFigmAAAAAElFTkSuQmCC) if it is not already open. The tags table appears.
    
    ![tag table](https://docs.databricks.com/aws/en/assets/images/tags-open-2b92892f2d6833c4fac51ed029b0ae39.png)
    
2.  Click in the **Name** and **Value** fields and type the key and value for your tag.
    
3.  Click **Add**.
    
    ![add tag](https://docs.databricks.com/aws/en/assets/images/tag-add-e7a0a94c7df96101259d3f82deb415fc.png)
    

#### Edit or delete tags for a model or model version[​](#edit-or-delete-tags-for-a-model-or-model-version "Direct link to Edit or delete tags for a model or model version")

To edit or delete an existing tag, use the icons in the **Actions** column.

![tag actions](https://docs.databricks.com/aws/en/assets/images/tag-edit-or-delete-2a374d59a14e35d810bf70d2e1369a79.png)

### Annotate a model version using the API[​](#annotate-a-model-version-using-the-api "Direct link to Annotate a model version using the API")

To update a model version description, use the MLflow Client API `update_model_version()` method:

Python

    client = MlflowClient()client.update_model_version(  name="<model-name>",  version=<model-version>,  description="<description>")

To set or update a tag for a registered model or model version, use the MLflow Client API [`set_registered_model_tag()`](https://www.mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient.set_registered_model_tag)) or [`set_model_version_tag()`](https://www.mlflow.org/docs/latest/python_api/mlflow.tracking.html#mlflow.tracking.MlflowClient.set_model_version_tag) method:

Python

    client = MlflowClient()client.set_registered_model_tag()(  name="<model-name>",  key="<key-value>",  tag="<tag-value>")

Python

    client = MlflowClient()client.set_model_version_tag()(  name="<model-name>",  version=<model-version>,  key="<key-value>",  tag="<tag-value>")

## Rename a model (API only)[​](#rename-a-model-api-only "Direct link to Rename a model (API only)")

To rename a registered model, use the MLflow Client API `rename_registered_model()` method:

Python

    client=MlflowClient()client.rename_registered_model("<model-name>", "<new-model-name>")

note

You can rename a registered model only if it has no versions, or all versions are in the None or Archived stage.

## Search for a model[​](#search-for-a-model "Direct link to Search for a model")

You can search for models in the Workspace Model Registry using the UI or the API.

note

When you search for a model, only models for which you have at least CAN READ permissions are returned.

### Search for a model using the UI[​](#search-for-a-model-using-the-ui "Direct link to Search for a model using the UI")

To display registered models, click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in the sidebar.

To search for a specific model, enter text in the search box. You can enter the name of a model or any part of the name:

![Registered models search](https://docs.databricks.com/aws/en/assets/images/registered-models-c97430c6ce709cd846c596fc421ae25b.png)

You can also search on tags. Enter tags in this format: `tags.<key>=<value>`. To search for multiple tags, use the `AND` operator.

![Tag-based search](https://docs.databricks.com/aws/en/assets/images/search-with-tags-c556dd179d35c1e762d355e11b8bc7c7.png)

You can search on both the model name and tags using the [MLflow search syntax](https://www.mlflow.org/docs/latest/search-runs.html#syntax). For example:

![Name and tag-based search](https://docs.databricks.com/aws/en/assets/images/model-search-name-and-tag-4cf926a5ed4b4546d7bbc240b478b697.png)

### Search for a model using the API[​](#search-for-a-model-using-the-api "Direct link to Search for a model using the API")

You can search for registered models in the Workspace Model Registry with the MLflow [search\_registered\_models()](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_registered_models#mlflow.search_registered_models) method.

If you have [set tags](#annotate-a-model-version-using-the-api) on your models, you can also search by those tags with `search_registered_models()`.

Python

    import mlflowfrom pprint import pprintprint(f"Find registered models with a specific tag value")for m in mlflow.search_registered_models(f"tags.`<key-value>`='<tag-value>'"):  pprint(dict(m), indent=4)

You can also search for a specific model name and list its version details using MLflow [search\_model\_versions()](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_model_versions#mlflow.search_model_versions) method:

Python

    import mlflowfrom pprint import pprint[pprint(mv) for mv in mlflow.search_model_versions("name='<model-name>'")]

This outputs:

Console

    {   'creation_timestamp': 1582671933246,    'current_stage': 'Production',    'description': 'A random forest model containing 100 decision trees '                   'trained in scikit-learn',    'last_updated_timestamp': 1582671960712,    'name': 'sk-learn-random-forest-reg-model',    'run_id': 'ae2cc01346de45f79a44a320aab1797b',    'source': './mlruns/0/ae2cc01346de45f79a44a320aab1797b/artifacts/sklearn-model',    'status': 'READY',    'status_message': None,    'user_id': None,    'version': 1 }{   'creation_timestamp': 1582671960628,    'current_stage': 'None',    'description': None,    'last_updated_timestamp': 1582671960628,    'name': 'sk-learn-random-forest-reg-model',    'run_id': 'd994f18d09c64c148e62a785052e6723',    'source': './mlruns/0/d994f18d09c64c148e62a785052e6723/artifacts/sklearn-model',    'status': 'READY',    'status_message': None,    'user_id': None,    'version': 2 }

## Delete a model or model version[​](#delete-a-model-or-model-version "Direct link to Delete a model or model version")

You can delete a model using the UI or the API.

### Delete a model version or model using the UI[​](#delete-a-model-version-or-model-using-the-ui "Direct link to Delete a model version or model using the UI")

warning

You cannot undo this action. You can transition a model version to the Archived stage rather than deleting it from the registry. When you delete a model, all model artifacts stored by the Workspace Model Registry and all the metadata associated with the registered model are deleted.

note

You can only delete models and model versions in the None or Archived stage. If a registered model has versions in the Staging or Production stage, you must transition them to either the None or Archived stage before deleting the model.

To delete a model version:

1.  Click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in the sidebar.
2.  Click a model name.
3.  Click a model version.
4.  Click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) at the upper right corner of the screen and select **Delete** from the drop-down menu.

To delete a model:

1.  Click ![Models Icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAHqADAAQAAAABAAAAHgAAAADKQTcFAAADQ0lEQVRIDe1WWUhUURj+xlS0RYeEBHPcdw1NS8cUKwvbBKOMTMqiogehICJ8CCJ6sagsinoQyiQhLJU0MZWgtMClNMs1KcqyXkJTM9fR6f5H73TvnbkzdzLwoX4427995/znv/+5Kq/YRD3mgWzmAZNB/geec+TPnjiGtsflrNFcjhaoNd5n5ITW8glo384U2NvZsRYeEgQXtRpP6hqMXM35ju1t7aBdGY7MjHSkb09mACkHM0GNaMeWJDZKO1spg3bNK5c8qsbpS1dFKq4uLohcEcq1EESGzYwiBYULETAfKt6WwqZ2dkJ9U4sByNvDnRcbxtaubjS3dsDXU4P46CiU3rphkNHmTZFKWEAoKRYtdDSESeiANx4eGWEgza3taG7r5Fo7fnI8ni6cOonUbZuh1+tRUFJmFDFeT3Rinikd6cSVNc8YYOvbbqlYtL73sJIBt3R0yYKSgQiYwkLhlZ5UGxWBCZ0OHz59EYGYWni6uzF2T695XVFWUyLdKS7lQjeKyUkdBoaG2HroxzASYlYh/8o55F8+j4To1aYwGc/LfTkbP362ApgsCDxsYzKKK6qgdnJC3/cBaFN2Iyc3D4MKNuCpmQHu6f3KNiDXiU4sVKqqec6Wm9bGY3RsDNduFyBWwQb4E/f09grdGc1FWS2VNlWUYKnaGVszjqDz3XuD2NHBAYfTUnFozy44L1nM+LUNL7nrmcT6NTFQqVS4X16JrOyLBhvpxGzJ9ObuKywoAN/6+tHw6rXBVsclWmPLG+QXPcD4+ARCAvwQ6OMNHw8NAyXg0EB/2XJJjmRDTUJhuGktpd9XkIYJ7rRESsol6ZkFflrfiP6BQQT7+yLYz5f0/xqZBSaU6tkkS0qIMwKluz56YC/qSgvZa0QKVAP4OiBXLknPbHKRwjptNPJysjE9Pc1l9zjIWfb1XNnk0kZGkBnTkz4wTDDbiSqXUMDPE+O0bGpjY8PqOFW2DfGxcHNdxviUzTfvFqG28QVvomi0CMw/kfz7SmGkT+xPAfldWQTmFYXj1NQ09h/PErKsnlsENvVwmEsapTswW0DICf0v0X+Tn5cnezgKyyrMPndKgS1mtVJH1upZ/I6tdahU/98D/gXOKT9CrMPb5gAAAABJRU5ErkJggg==) **Models** in the sidebar.
2.  Click a model name.
3.  Click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) at the upper right corner of the screen and select **Delete** from the drop-down menu.

### Delete a model version or model using the API[​](#delete-a-model-version-or-model-using-the-api "Direct link to Delete a model version or model using the API")

warning

You cannot undo this action. You can transition a model version to the Archived stage rather than deleting it from the registry. When you delete a model, all model artifacts stored by the Workspace Model Registry and all the metadata associated with the registered model are deleted.

note

You can only delete models and model versions in the None or Archived stage. If a registered model has versions in the Staging or Production stage, you must transition them to either the None or Archived stage before deleting the model.

#### Delete a model version[​](#delete-a-model-version "Direct link to Delete a model version")

To delete a model version, use the MLflow Client API `delete_model_version()` method:

Python

    # Delete versions 1,2, and 3 of the modelclient = MlflowClient()versions=[1, 2, 3]for version in versions:  client.delete_model_version(name="<model-name>", version=version)

#### Delete a model[​](#delete-a-model "Direct link to Delete a model")

To delete a model, use the MLflow Client API `delete_registered_model()` method:

Python

    client = MlflowClient()client.delete_registered_model(name="<model-name>")

Databricks recommends using [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) to share models across workspaces. Unity Catalog provides out-of-the-box support for cross-workspace model access, governance, and audit logging.

However, if using the workspace model registry, you can also [share models across multiple workspaces](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/multiple-workspaces) with some setup. For example, you can develop and log a model in your own workspace and then access it from another workspace using a remote Workspace model registry. This is useful when multiple teams share access to models. You can create multiple workspaces and use and manage models across these environments.

## Copy MLflow objects between workspaces[​](#copy-mlflow-objects-between-workspaces "Direct link to Copy MLflow objects between workspaces")

To import or export MLflow objects to or from your Databricks workspace, you can use the community-driven open source project [MLflow Export-Import](https://github.com/mlflow/mlflow-export-import#why-use-mlflow-export-import) to migrate MLflow experiments, models, and runs between workspaces.

With these tools, you can:

*   Share and collaborate with other data scientists in the same or another tracking server. For example, you can clone an experiment from another user into your workspace.
*   Copy a model from one workspace to another, such as from a development to a production workspace.
*   Copy MLflow experiments and runs from your local tracking server to your Databricks workspace.
*   Back up mission critical experiments and models to another Databricks workspace.

## Example[​](#example "Direct link to Example")

This example illustrates how to use the Workspace Model Registry to build a machine learning application.

[Workspace Model Registry example](https://docs.databricks.com/aws/en/mlflow/workspace-model-registry-example)
