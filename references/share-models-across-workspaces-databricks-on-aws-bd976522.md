---
title: Share models across workspaces | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/multiple-workspaces
ingestedAt: "2026-06-18T08:11:26.499Z"
---

important

Databricks recommends using [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) to share models across workspaces. The approach in this article is deprecated.

Databricks supports sharing models across multiple workspaces. For example, you can develop and log a model in a development workspace, and then access and compare it against models in a separate production workspace. This is useful when multiple teams share access to models or when your organization has multiple workspaces to handle the different stages of development. For cross-workspace model development and deployment, Databricks recommends the [deploy code](https://docs.databricks.com/aws/en/machine-learning/mlops/deployment-patterns#deploy-code) approach, where the model training code is deployed to multiple environments.

In multi-workspace situations, you can access models across Databricks workspaces by using a remote model registry. For example, data scientists could access the production model registry with read-only access to compare their in-development models against the current production models. An example multi-workspace set-up is shown below.

![Multiple workspaces](https://docs.databricks.com/aws/en/assets/images/multiworkspace-deda514f1a87b5b8093afb54fe652ae7.png)

Access to a remote registry is controlled by tokens. Each user or script that needs access [creates a personal access token](https://docs.databricks.com/api/workspace/tokenmanagement) in the remote registry and [copies that token into the secret manager](https://docs.databricks.com/api/workspace/secrets) of their local workspace. Each API request sent to the remote registry workspace must include the access token; MLflow provides a simple mechanism to specify the secrets to be used when performing model registry operations.

note

As a security best practice when you authenticate with automated tools, systems, scripts, and apps, Databricks recommends that you use [OAuth tokens](https://docs.databricks.com/aws/en/dev-tools/auth/oauth-m2m).

If you use personal access token authentication, Databricks recommends using personal access tokens belonging to [service principals](https://docs.databricks.com/aws/en/admin/users-groups/service-principals) instead of workspace users. To create tokens for service principals, see [Manage tokens for a service principal](https://docs.databricks.com/aws/en/admin/users-groups/manage-service-principals#tokens).

All [client](https://www.mlflow.org/docs/latest/python_api/mlflow.tracking.html) and [fluent](https://www.mlflow.org/docs/latest/python_api/mlflow.html) API methods for model registry are supported for remote workspaces.

## Requirements[​](#requirements "Direct link to Requirements")

Using a model registry across workspaces requires the MLflow Python client, release 1.11.0 or above.

note

This workflow is implemented from logic in the MLflow client. Ensure that the environment running the client has access to make network requests against the Databricks workspace containing the remote model registry. A common restriction put on the registry workspace is an IP allow list, which can disallow connections from MLflow clients running in a cluster in another workspace.

## Set up the API token for a remote registry[​](#set-up-the-api-token-for-a-remote-registry "Direct link to Set up the API token for a remote registry")

1.  In the model registry workspace, [create an access token](https://docs.databricks.com/api/workspace/tokenmanagement).
2.  In the local workspace, create secrets to store the access token and the remote workspace information:
    1.  Create a secret scope: `databricks secrets create-scope <scope>`.
    2.  Pick a unique name for the target workspace, shown here as `<prefix>`. Then create three secrets:
        *   `databricks secrets put-secret <scope> <prefix>-host` : Enter the hostname of the model registry workspace. For example, `https://cust-success.cloud.databricks.com/`.
        *   `databricks secrets put-secret <scope> <prefix>-token` : Enter the access token from the model registry workspace.
        *   `databricks secrets put-secret <scope> <prefix>-workspace-id` : Enter the workspace ID for the model registry workspace which can be [found in the URL](https://docs.databricks.com/aws/en/workspace/workspace-details#workspace-instance-names-urls-and-ids) of any page.

## Specify a remote registry[​](#specify-a-remote-registry "Direct link to Specify a remote registry")

Based on the secret scope and name prefix you created for the remote registry workspace, you can construct a registry URI of the form:

Python

    registry_uri = f'databricks://<scope>:<prefix>'

You can use the URI to specify a remote registry for [fluent API methods](https://www.mlflow.org/docs/latest/python_api/mlflow.html) by first calling:

Python

    mlflow.set_registry_uri(registry_uri)

Or, you can specify it explicitly when you instantiate an `MlflowClient`:

Python

    client = MlflowClient(registry_uri=registry_uri)

The following workflows show examples of both approaches.

## Register a model in the remote registry[​](#register-a-model-in-the-remote-registry "Direct link to Register a model in the remote registry")

One way to register a model is to use the `mlflow.register_model` API:

Python

    mlflow.set_registry_uri(registry_uri)mlflow.register_model(model_uri=f'runs:/<run-id>/<artifact-path>', name=model_name)

Examples for other model registration methods can be found in the notebook at the end of this page.

note

Registering a model in a remote workspace creates a temporary copy of the model artifacts in DBFS in the remote workspace. You may want to delete this copy once the model version is in `READY` status. The temporary files can be found under the `/dbfs/databricks/mlflow/tmp-external-source/<run-id>` folder.

You can also specify a `tracking_uri` to point to a MLflow Tracking service in another workspace in a similar manner to `registry_uri`. This means you can take a run on a remote workspace and register its model in the current or another remote workspace.

## Use a model from the remote registry[​](#use-a-model-from-the-remote-registry "Direct link to Use a model from the remote registry")

You can load and use a model version in a remote registry with `mlflow.<flavor>.load_model` methods by first setting the registry URI:

Python

    mlflow.set_registry_uri(registry_uri)model = mlflow.pyfunc.load_model(f'models:/<model-name>/Staging')model.predict(...)

Or, you can explicitly specify the remote registry in the `models:/` URI:

Python

    model = mlflow.pyfunc.load_model(f'models://<scope>:<prefix>@databricks/<model-name>/Staging')model.predict(...)

Other helper methods for accessing the model files are also supported, such as:

Python

    client.get_latest_versions(model_name)client.get_model_version_download_uri(model_name, version)

## Manage a model in the remote registry[​](#manage-a-model-in-the-remote-registry "Direct link to Manage a model in the remote registry")

You can perform any action on models in the remote registry as long as you have the required permissions. For example, if you have CAN MANAGE permissions on a model, you can transition a model version stage or delete the model using `MlflowClient` methods:

Python

    client = MlflowClient(tracking_uri=None, registry_uri=registry_uri)client.transition_model_version_stage(model_name, version, 'Archived')client.delete_registered_model(model_name)

## Notebook example: Remote model registry[​](#notebook-example-remote-model-registry "Direct link to Notebook example: Remote model registry")

The following notebook is applicable for workspaces that are not enabled for Unity Catalog. It shows how to log models to the MLflow tracking server from the current workspace, and register the models into Model Registry in a different workspace. Databricks recommends using [Models in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/) to share models across workspaces.

#### Remote Model Registry example notebook
