---
title: Manage model lifecycle in Unity Catalog | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/
ingestedAt: "2026-06-18T08:11:21.931Z"
---

This article describes how to use Models in Unity Catalog as part of your machine learning workflow to manage the full lifecycle of ML models. Databricks provides a hosted version of MLflow Model Registry in [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/). Models in Unity Catalog extends the benefits of Unity Catalog to ML models, including centralized access control, auditing, lineage, and model discovery across workspaces. Models in Unity Catalog is compatible with the open-source MLflow Python client.

For an overview of Model Registry concepts, see [MLflow on Databricks](https://docs.databricks.com/aws/en/mlflow/).

[MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) makes significant enhancements to the MLflow Model Registry in Unity Catalog, allowing your models to directly capture data like parameters and metrics and make them available across all workspaces and experiments. The default registry URI in MLflow 3 is `databricks-uc`, meaning the MLflow Model Registry in Unity Catalog will be used. For more details, see [Get started with MLflow 3 for models](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install) and [Model Registry improvements with MLflow 3](https://docs.databricks.com/aws/en/mlflow/model-registry-3).

## Requirements[​](#requirements "Direct link to Requirements")

*   Unity Catalog must be enabled in your workspace. See [Get started using Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/get-started) to create a Unity Catalog Metastore, enable it in a workspace, and create a catalog. If Unity Catalog is not enabled, use the [workspace model registry](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/workspace-model-registry).
    
*   You must use a compute resource that has access to Unity Catalog. For ML workloads, this means that the compute's access mode must be **Dedicated** (formerly single user). For more information, see [Access modes](https://docs.databricks.com/aws/en/compute/configure#access-mode). With Databricks Runtime 15.4 LTS ML and above, you can also use [dedicated group access mode](https://docs.databricks.com/aws/en/compute/group-access).
    
*   To create new registered models, you need the following privileges:
    
    *   `USE SCHEMA` and `USE CATALOG` privileges on the schema and its enclosing catalog.
    *   `CREATE MODEL` or `CREATE FUNCTION` privilege on the schema. To grant privileges, use the Catalog Explorer UI or the [SQL GRANT command](https://docs.databricks.com/aws/en/sql/language-manual/security-grant):
    
    SQL
    
        GRANT CREATE MODEL ON SCHEMA <schema-name> TO <principal>
    
*   If you are using [Databricks on AWS GovCloud](https://docs.databricks.com/aws/en/security/privacy/gov-cloud), you must set the environment variable `MLFLOW_USE_DATABRICKS_SDK_MODEL_ARTIFACTS_REPO_FOR_UC` to `True`. Include a cell in your notebook with the following code:
    
    Python
    
        import osos.environ['MLFLOW_USE_DATABRICKS_SDK_MODEL_ARTIFACTS_REPO_FOR_UC'] = 'True'
    
    This setting might also be useful in other cases if you run into authorization issues when trying to register a model. This approach cannot be used for models shared with OpenSharing that use default storage.
    

note

Your workspace must be attached to a Unity Catalog metastore that supports privilege inheritance. This is true for all metastores created after August 25, 2022. If running on an older metastore, [follow docs](https://docs.databricks.com/aws/en/archive/unity-catalog/upgrade-privilege-model) to upgrade.

## Install and configure MLflow client for Unity Catalog[​](#install-and-configure-mlflow-client-for-unity-catalog "Direct link to install-and-configure-mlflow-client-for-unity-catalog")

This section includes instructions for installing and configuring the MLflow client for Unity Catalog.

### Install MLflow Python client[​](#install-mlflow-python-client "Direct link to Install MLflow Python client")

Support for models in Unity Catalog is included in Databricks Runtime 13.2 ML and above.

You can also use models in Unity Catalog on Databricks Runtime 11.3 LTS and above by installing the latest version of the MLflow Python client in your notebook, using the following code.

    %pip install --upgrade "mlflow-skinny[databricks]"dbutils.library.restartPython()

### Configure MLflow client to access models in Unity Catalog[​](#configure-mlflow-client-to-access-models-in-unity-catalog "Direct link to configure-mlflow-client-to-access-models-in-unity-catalog")

If your workspace's [default catalog](https://docs.databricks.com/aws/en/catalogs/default) is in Unity Catalog (rather than `hive_metastore`), and you are either running a cluster using Databricks Runtime 13.3 LTS or above or using [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install), models are automatically created in and loaded from the default catalog. You do not have to perform this step.

For other workspaces, the MLflow Python client creates models in the Databricks workspace model registry. To upgrade to models in Unity Catalog, use the following code in your notebooks to configure the MLflow client:

Python

    import mlflowmlflow.set_registry_uri("databricks-uc")

For a small number of workspaces where both the default catalog was configured to a catalog in Unity Catalog prior to January 2024 and the workspace model registry was used prior to January 2024, you must manually set the default catalog to Unity Catalog using the command shown above.

## Train and register Unity Catalog\-compatible models[​](#train-and-register-unity-catalog-compatible-models "Direct link to train-and-register-unity-catalog-compatible-models")

**Permissions required**:

*   To create a new registered model, you need the `CREATE MODEL` and `USE SCHEMA` privileges on the enclosing schema, and `USE CATALOG` privilege on the enclosing catalog.
*   To create new model versions under a registered model, you must be the owner of the registered model, or have the [`CREATE MODEL VERSION`](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#create-model-version) privilege on it plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

If you run into authorization issues when trying to register a model, try setting the environment variable `MLFLOW_USE_DATABRICKS_SDK_MODEL_ARTIFACTS_REPO_FOR_UC` to `True`. This approach cannot be used for models shared with OpenSharing that use default storage. See [Requirements](#requirements).

If you are using [Databricks on AWS GovCloud](https://docs.databricks.com/aws/en/security/privacy/gov-cloud), you must set the environment variable `MLFLOW_USE_DATABRICKS_SDK_MODEL_ARTIFACTS_REPO_FOR_UC` to `True`. See [Requirements](#requirements).

New ML model versions in UC must have a [model signature](https://mlflow.org/docs/latest/ml/model/signatures/). If you're not already logging MLflow models with signatures in your model training workloads, you can either:

*   Use [Databricks autologging](https://docs.databricks.com/aws/en/mlflow/databricks-autologging), which automatically logs models with signatures for many popular ML frameworks. See supported frameworks in the [MLflow docs](https://mlflow.org/docs/latest/ml/tracking/autolog/).
*   With MLflow 2.5.0 and above, you can specify an input example in your `mlflow.<flavor>.log_model` call, and the model signature is automatically inferred. For further information, refer to [the MLflow documentation](https://mlflow.org/docs/latest/ml/model/#model-signatures-and-input-examples).

Then, pass the three-level name of the model to MLflow APIs, in the form `<catalog>.<schema>.<model>`.

Model versions that do not have signatures have certain limitations. For a list of these limitations, and to add or update a signature for an existing model version, see [Add or update a signature for an existing model version](#add-signature).

The examples in this section create and access models in the `ml_team` schema under the `prod` catalog.

The model training examples in this section create a new model version and register it in the `prod` catalog. Using the `prod` catalog doesn't necessarily mean that the model version serves production traffic. The model version's enclosing catalog, schema, and registered model reflect its environment (`prod`) and associated governance rules (for example, privileges can be set up so that only admins can delete from the `prod` catalog), but not its deployment status. To manage the deployment status, use [model aliases](#uc-model-aliases).

### Register a model to Unity Catalog using autologging[​](#register-a-model-to-unity-catalog-using-autologging "Direct link to register-a-model-to-unity-catalog-using-autologging")

To register a model, use MLflow Client API `register_model()` method. See [mlflow.register\_model](https://mlflow.org/docs/latest/python_api/mlflow.html?highlight=register_model#mlflow.register_model).

*   MLflow 3
*   MLflow 2.x

Python

    from sklearn import datasetsfrom sklearn.ensemble import RandomForestClassifier# Train a sklearn model on the iris datasetX, y = datasets.load_iris(return_X_y=True, as_frame=True)clf = RandomForestClassifier(max_depth=7)clf.fit(X, y)# Note that the UC model name follows the pattern# <catalog_name>.<schema_name>.<model_name>, corresponding to# the catalog, schema, and registered model name# in Unity Catalog under which to create the version# The registered model will be created if it doesn't already exist,# and the model version will contain all parameters and metrics# logged with the corresponding MLflow Logged Model.logged_model = mlflow.last_logged_model()mlflow.register_model(logged_model.model_uri, "prod.ml_team.iris_model")

### Register a model using the API[​](#register-a-model-using-the-api "Direct link to Register a model using the API")

*   MLflow 3
*   MLflow 2.x

Python

    mlflow.register_model(  "models:/<model_id>", "prod.ml_team.iris_model")

### Register a model to Unity Catalog with automatically inferred signature[​](#register-a-model-to-unity-catalog-with-automatically-inferred-signature "Direct link to register-a-model-to-unity-catalog-with-automatically-inferred-signature")

Support for automatically inferred signatures is available in MLflow version 2.5.0 and above, and is supported in Databricks Runtime 11.3 LTS ML and above. To use automatically inferred signatures, use the following code to install the latest MLflow Python client in your notebook:

    %pip install --upgrade "mlflow-skinny[databricks]"dbutils.library.restartPython()

The following code shows an example of an automatically inferred signature. Note that using `registered_model_name` in the `log_model()` call registers the model to Unity Catalog, so you must provide the full three-level name of the model in the format `<catalog>.<schema>.<model>`.

*   MLflow 3
*   MLflow 2.x

Python

    from sklearn import datasetsfrom sklearn.ensemble import RandomForestClassifierwith mlflow.start_run():    # Train a sklearn model on the iris dataset    X, y = datasets.load_iris(return_X_y=True, as_frame=True)    clf = RandomForestClassifier(max_depth=7)    clf.fit(X, y)    # Take the first row of the training dataset as the model input example.    input_example = X.iloc[[0]]    # Log the model and register it as a new version in UC.    mlflow.sklearn.log_model(        sk_model=clf,        name="model",        # The signature is automatically inferred from the input example and its predicted output.        input_example=input_example,        # Use three-level name to register model in Unity Catalog.        registered_model_name="prod.ml_team.iris_model",    )

### Register a model using the UI[​](#register-a-model-using-the-ui "Direct link to Register a model using the UI")

Follow these steps:

1.  From the experiment run page, click **Register model** in the upper-right corner of the UI.
    
2.  In the dialog, select **Unity Catalog**, and select a destination model from the drop down list.
    
    ![Register model version dialog with dropdown menu](https://docs.databricks.com/aws/en/assets/images/uc-register-model-dialog-dbc7806e79613776eb84159fa6c394e2.png)
    
3.  Click **Register**.
    
    ![Register model version dialog with button](https://docs.databricks.com/aws/en/assets/images/uc-register-model-button-e6b3b94bde6506bda3be82836db5e019.png)
    

Registering a model can take time. To monitor progress, navigate to the destination model in Unity Catalog and refresh periodically.

### Add or update a signature for an existing model version[​](#-add-or-update-a-signature-for-an-existing-model-version "Direct link to -add-or-update-a-signature-for-an-existing-model-version")

Model versions that do not have signatures have the following limitations:

*   If a signature is provided, model inputs are checked at inference and an error is reported if the inputs do not match the signature. Without a signature, there is no automatic input enforcement, and models need to be able to handle unexpected inputs.
*   Using a model version with [AI functions](https://docs.databricks.com/aws/en/large-language-models/ai-functions) requires providing a schema in the function call.
*   Using a model version with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) does not auto-generate input examples.

To add or update a model version signature, see the [MLflow documentation](https://mlflow.org/docs/latest/ml/model/signatures/).

## Use model aliases[​](#use-model-aliases "Direct link to use-model-aliases")

Model aliases allow you to assign a mutable, named reference to a particular version of a registered model. You can use aliases to indicate the deployment status of a model version. For example, you could allocate a “Champion” alias to the model version currently in production and target this alias in workloads that use the production model. You can then update the production model by reassigning the “Champion” alias to a different model version.

### Set and delete aliases on models[​](#set-and-delete-aliases-on-models "Direct link to Set and delete aliases on models")

**Permissions required**: Owner of the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

You can set, update, and remove aliases for models in Unity Catalog using Catalog Explorer. See [View and manage models in the UI](#ui).

To set, update, and delete aliases using the MLflow Client API, see the examples below:

Python

    from mlflow import MlflowClientclient = MlflowClient()# create "Champion" alias for version 1 of model "prod.ml_team.iris_model"client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 1)# reassign the "Champion" alias to version 2client.set_registered_model_alias("prod.ml_team.iris_model", "Champion", 2)# get a model version by aliasclient.get_model_version_by_alias("prod.ml_team.iris_model", "Champion")# delete the aliasclient.delete_registered_model_alias("prod.ml_team.iris_model", "Champion")

For more details on alias client APIs, see the [MLflow API documentation](https://mlflow.org/docs/latest/python_api/mlflow.client.html).

### Load model version by alias for inference workloads[​](#load-model-version-by-alias-for-inference-workloads "Direct link to load-model-version-by-alias-for-inference-workloads")

**Permissions required**: `EXECUTE` privilege on the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

Batch inference workloads can reference a model version by alias. The snippet below loads and applies the “Champion” model version for batch inference. If the “Champion” version is updated to reference a new model version, the batch inference workload automatically picks it up on its next execution. This allows you to decouple model deployments from your batch inference workloads.

Python

    import mlflow.pyfuncmodel_version_uri = "models:/prod.ml_team.iris_model@Champion"champion_version = mlflow.pyfunc.load_model(model_version_uri)champion_version.predict(test_x)

Model serving endpoints can also reference a model version by alias. You can write deployment workflows to get a model version by alias and update a model serving endpoint to serve that version, using the [model serving REST API](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints#endpoint-config). For example:

Python

    import mlflowimport requestsclient = mlflow.tracking.MlflowClient()champion_version = client.get_model_version_by_alias("prod.ml_team.iris_model", "Champion")# Invoke the model serving REST API to update endpoint to serve the current "Champion" versionmodel_name = champion_version.namemodel_version = champion_version.versionrequests.request(...)

### Load model version by version number for inference workloads[​](#load-model-version-by-version-number-for-inference-workloads "Direct link to Load model version by version number for inference workloads")

You can also load model versions by version number:

Python

    import mlflow.pyfunc# Load version 1 of the model "prod.ml_team.iris_model"model_version_uri = "models:/prod.ml_team.iris_model/1"first_version = mlflow.pyfunc.load_model(model_version_uri)first_version.predict(test_x)

As long as you have the appropriate privileges, you can access models in Unity Catalog from any workspace that is attached to the metastore containing the model. For example, you can access models from the `prod` catalog in a dev workspace, to facilitate comparing newly-developed models to the production baseline.

To collaborate with other users (share write privileges) on a registered model you created, you must grant ownership of the model to a group containing yourself and the users you'd like to collaborate with. Collaborators must also have the `USE CATALOG` and `USE SCHEMA` privileges on the catalog and schema containing the model. See [Unity Catalog privileges reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference) for details.

To share models with users in other regions or accounts, use the OpenSharing [Databricks-to-Databricks sharing flow](https://docs.databricks.com/aws/en/delta-sharing/#delta-sharing). See [Add models to a share](https://docs.databricks.com/aws/en/delta-sharing/create-share#models) (for providers) and [Get access in the Databricks-to-Databricks model](https://docs.databricks.com/aws/en/delta-sharing/recipient#get-access-db-to-db) (for recipients). As a recipient, after you create a catalog from a share, you access models in that shared catalog the same way as any other model in Unity Catalog.

## Track the data lineage of a model in Unity Catalog[​](#track-the-data-lineage-of-a-model-in-unity-catalog "Direct link to track-the-data-lineage-of-a-model-in-unity-catalog")

note

Support for table to model lineage in Unity Catalog is available in MLflow 2.11.0 and above.

When you train a model on a table in Unity Catalog, you can track the lineage of the model to the upstream dataset(s) it was trained and evaluated on. To do this, use [mlflow.log\_input](https://mlflow.org/docs/latest/python_api/mlflow.html?highlight=log_input#mlflow.log_input). This saves the input table information with the MLflow run that generated the model. Data lineage is also automatically captured for models logged using feature store APIs. See [Feature governance and lineage](https://docs.databricks.com/aws/en/machine-learning/feature-store/lineage).

When you register the model to Unity Catalog, lineage information is automatically saved and is visible in the **Lineage** tab on the model version page in Catalog Explorer. See [View model version information and model lineage](#view-model-version-information).

The following code shows an example.

*   MLflow 3
*   MLflow 2.x

Python

    import mlflowimport pandas as pdimport pyspark.pandas as psfrom sklearn.datasets import load_irisfrom sklearn.ensemble import RandomForestRegressor# Write a table to Unity Catalogiris = load_iris()iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)iris_df.rename(  columns = {    'sepal length (cm)':'sepal_length',    'sepal width (cm)':'sepal_width',    'petal length (cm)':'petal_length',    'petal width (cm)':'petal_width'},  inplace = True)iris_df['species'] = iris.targetps.from_pandas(iris_df).to_table("prod.ml_team.iris", mode="overwrite")# Load a Unity Catalog table, train a model, and log the input tabledataset = mlflow.data.load_delta(table_name="prod.ml_team.iris", version="0")pd_df = dataset.df.toPandas()X = pd_df.drop("species", axis=1)y = pd_df["species"]with mlflow.start_run():    clf = RandomForestRegressor(n_estimators=100)    clf.fit(X, y)    mlflow.log_input(dataset, "training")    # Take the first row of the training dataset as the model input example.    input_example = X.iloc[[0]]    # Log the model and register it as a new version in UC.    mlflow.sklearn.log_model(        sk_model=clf,        name="model",        # The signature is automatically inferred from the input example and its predicted output.        input_example=input_example,        # Use three-level name to register model in Unity Catalog.        registered_model_name="prod.ml_team.iris_classifier",    )

## Control access to models[​](#control-access-to-models "Direct link to Control access to models")

In Unity Catalog, registered models are a subtype of the `FUNCTION` securable object. To grant access to a model registered in Unity Catalog, you use `GRANT ON FUNCTION`. You can also use Catalog Explorer to set model ownership and permissions. For details, see [Manage privileges in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/) and [Unity Catalog securable objects reference](https://docs.databricks.com/aws/en/data-governance/unity-catalog/securable-objects).

You can configure model permissions programmatically using the [Grants REST API](https://docs.databricks.com/api/workspace/grants). When you configure model permissions, set `securable_type` to `"FUNCTION"` in REST API requests. For example, use `PATCH /api/2.1/unity-catalog/permissions/function/{full_name}` to update registered model permissions.

## View and manage models in the UI[​](#view-and-manage-models-in-the-ui "Direct link to view-and-manage-models-in-the-ui")

**Permissions required**: To view a registered model and its model versions in the UI, you need `EXECUTE` privilege on the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model

You can view and manage registered models and model versions in Unity Catalog using Catalog Explorer.

### View model information[​](#view-model-information "Direct link to View model information")

To view models in Catalog Explorer:

1.  Click ![Data icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjY0NTc2IDAuMzY4NDUzQzguNTEwODIgMC4xNDAwOTkgOC4yNjUzIDAgOC4wMDAwNiAwQzcuNzM0ODIgMCA3LjQ4OTMgMC4xNDAwOTkgNy4zNTQzNyAwLjM2ODQ1M0w0LjEwNDM3IDUuODY4NDVDMy45NjczNiA2LjEwMDMgMy45NjUxOCA2LjM4NzgxIDQuMDk4NjUgNi42MjE3MUM0LjIzMjEzIDYuODU1NjEgNC40ODA3NiA3IDQuNzUwMDYgN0gxMS4yNTAxQzExLjUxOTQgNyAxMS43NjggNi44NTU2MSAxMS45MDE1IDYuNjIxNzFDMTIuMDM0OSA2LjM4NzgxIDEyLjAzMjggNi4xMDAzIDExLjg5NTggNS44Njg0NUw4LjY0NTc2IDAuMzY4NDUzWk04LjAwMDA2IDIuMjI0MjZMOS45MzU3MiA1LjVINi4wNjQ0TDguMDAwMDYgMi4yMjQyNloiIGZpbGw9IiM2RjZGNkYiLz4KPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik04LjUgOS4yNUM4LjUgOC44MzU3OSA4LjgzNTc5IDguNSA5LjI1IDguNUgxNC4yNUMxNC42NjQyIDguNSAxNSA4LjgzNTc5IDE1IDkuMjVWMTQuMjVDMTUgMTQuNjY0MiAxNC42NjQyIDE1IDE0LjI1IDE1SDkuMjVDOC44MzU3OSAxNSA4LjUgMTQuNjY0MiA4LjUgMTQuMjVWOS4yNVpNMTAgMTBWMTMuNUgxMy41VjEwSDEwWiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTEgMTEuNzVDMSA5Ljk1NTA3IDIuNDU1MDcgOC41IDQuMjUgOC41QzYuMDQ0OTMgOC41IDcuNSA5Ljk1NTA3IDcuNSAxMS43NUM3LjUgMTMuNTQ0OSA2LjA0NDkzIDE1IDQuMjUgMTVDMi40NTUwNyAxNSAxIDEzLjU0NDkgMSAxMS43NVpNNC4yNSAxMEMzLjI4MzUgMTAgMi41IDEwLjc4MzUgMi41IDExLjc1QzIuNSAxMi43MTY1IDMuMjgzNSAxMy41IDQuMjUgMTMuNUM1LjIxNjUgMTMuNSA2IDEyLjcxNjUgNiAxMS43NUM2IDEwLjc4MzUgNS4yMTY1IDEwIDQuMjUgMTBaIiBmaWxsPSIjNkY2RjZGIi8+Cjwvc3ZnPgo=) **Catalog** in the sidebar.
    
2.  Select a compute resource from the drop-down list at the top right.
    
3.  In the Catalog Explorer tree at the left, open a catalog and select a schema.
    
4.  If the schema contains any models, they appear in the tree under **Models**, as shown.
    
    ![Section of catalog explorer tree showing models.](https://docs.databricks.com/aws/en/assets/images/models-in-catalog-explorer-tree-056e9d58ef849fada32a472c625cdfd7.png)
    
5.  Click a model to see more information. The model details page shows a list of model versions with additional information.
    
    ![model details page](https://docs.databricks.com/aws/en/assets/images/registered-model-714531f328fbab75b0a5d6b47210ce42.png)
    

### Set model aliases[​](#set-model-aliases "Direct link to Set model aliases")

To set a model alias using the UI:

1.  On the model details page, hover over the row for the model version to which you want to add an alias. The **Add alias** button appears.
2.  Click **Add alias**.
3.  Enter an alias or select one from the drop-down menu. You can add multiple aliases in the dialog.
4.  Click **Save aliases**.

![How to add an alias to a model version from the model details page.](https://docs.databricks.com/aws/en/assets/images/add-alias-7ca26ae0fd8c025c03f52639ee5fe082.gif)

To remove an alias:

1.  Hover over the row for the model version and click the pencil icon next to the alias.
2.  In the dialog, click the `X` next to the alias that you want to remove.
3.  Click **Save aliases**.

![How to remove an alias from a model version on the model details page.](https://docs.databricks.com/aws/en/assets/images/remove-alias-1fa338cf1b8fdc7aba2657d73deb4fab.gif)

### View model version information and model lineage[​](#view-model-version-information-and-model-lineage "Direct link to view-model-version-information-and-model-lineage")

To view more information about a model version, click its name in the list of models. The model version page appears. This page includes a link to the MLflow source run that created the version. In [MLflow 3](https://docs.databricks.com/aws/en/mlflow/mlflow-3-install), you can also view all parameters and metrics logged with the corresponding MLflow Logged Model.

*   MLflow 3
*   MLflow 2.x

![MLflow 3 model version page](https://docs.databricks.com/aws/en/assets/images/mlflow3-model-version-page-3bef0948f25abb51b63eb489ea55e01f.png)

From this page, you can view the lineage of the model as follows:

1.  Select the **Lineage** tab. The left sidebar shows components that were logged with the model.
    
    ![Lineage tab on model page in Catalog Explorer](https://docs.databricks.com/aws/en/assets/images/model-page-lineage-tab-eafe657793dcb514dbf415f927341250.png)
    
2.  Click **See lineage graph**. The lineage graph appears. For details about exploring the lineage graph, see [Capture and explore lineage](https://docs.databricks.com/aws/en/data-governance/unity-catalog/data-lineage).
    
    ![lineage screen](https://docs.databricks.com/aws/en/assets/images/lineage-graph-8b47d8dfa55669140117a1eeff33d241.png)
    
3.  To close the lineage graph, click ![close button for lineage graph](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAFqADAAQAAAABAAAAFgAAAAAcITNaAAABlElEQVQ4Ed3Tva4BURAH8P9u9h2UEo0Gsa/gCRRbidBJPI+PfhVapUZFdGhktxCF6BDis8Q1k3s21o5djeLeU1hzzpxfxuzQ7o+FLyz9CyaT/wQ+Ho/o9Xr4pP3n81nMFVsxGo3Q7XbR6XRCcUKbzSbD6/Xa97oMX/Qb5HI5UNWDwQC32w2WZQXSCK3X6zgcDqhWq4jFYr4cEaaMfD7PiYQbhuHFtHm5XBjd7/eMxuNxzn3+eAtT0jOuYkLp5xNaqVQgoZQbCitM0zT0+33u93w+x3a7ZTSRSFCKuLRP/3ntdhvj8ZgRqjSZTIqg2hSnQh2q52azwWw2UyGGwyGu16sXS18iYUIbjQa/sHK5DNM04TgObNsOxUPhVzSTyaBQKCCdTns4jaO03sK73Y4rpXmlSlOpFN/XdR2lUsnDW60Wz/orLsKE1mo1EFosFj1UXX7Gp9MpJFyEJ5MJTqcTo9lsVnm+p8KpPa7rYrVa+c5pNgPr0bf7YrEI7Esbj+m4L5fLwNHHc+wvJzoSWxF9LTrj78E/Ap8lauZ1EcwAAAAASUVORK5CYII=) in the upper-right corner.
    

## Rename a model[​](#rename-a-model "Direct link to Rename a model")

**Permissions required**: Owner of the registered model, `CREATE MODEL` privilege on the schema containing the registered model, and `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

To rename a registered model, use the MLflow Client API `rename_registered_model()` method, where `<full-model-name>` is the full 3-level name of the model and `<new-model-name>` is the model name without the catalog or schema.

Python

    client=MlflowClient()client.rename_registered_model("<full-model-name>", "<new-model-name>")

For example, the following code changes the name of the model `hello_world` to `hello`.

Python

    client=MlflowClient()client.rename_registered_model("docs.models.hello_world", "hello")

## Copy a model version[​](#copy-a-model-version "Direct link to Copy a model version")

You can copy a model version from one model to another in Unity Catalog.

### Copy a model version using the UI[​](#copy-a-model-version-using-the-ui "Direct link to Copy a model version using the UI")

Follow these steps:

1.  From the model version page, click **Copy this version** in the upper-right corner of the UI.
    
2.  Select a destination model from the drop down list and click **Copy**.
    
    ![Copy model version dialog](https://docs.databricks.com/aws/en/assets/images/uc-copy-model-dialog-6ae0befbf4db7d7802b214a9a68fbd8f.png)
    

Copying a model can take time. To monitor progress, navigate to the destination model in Unity Catalog and refresh periodically.

### Copy a model version using the API[​](#copy-a-model-version-using-the-api "Direct link to Copy a model version using the API")

To copy a model version, use the MLflow's [copy\_model\_version()](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.copy_model_version) Python API:

Python

    client = MlflowClient()client.copy_model_version(  "models:/<source-model-name>/<source-model-version>",  "<destination-model-name>",)

## Delete a model or model version[​](#delete-a-model-or-model-version "Direct link to Delete a model or model version")

**Permissions required**: Owner of the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

You can delete a registered model or a model version within a registered model using the UI or the API.

warning

You cannot undo this action. When you delete a model, all model artifacts stored by Unity Catalog and all the metadata associated with the registered model are deleted.

### Delete a model version or model using the UI[​](#delete-a-model-version-or-model-using-the-ui "Direct link to Delete a model version or model using the UI")

To delete a model or model version in Unity Catalog, follow these steps.

1.  In Catalog Explorer, on the model page or model version page, click the kebab menu ![Kebab menu icon.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMUM3LjAzMzUgMSA2LjI1IDEuNzgzNSA2LjI1IDIuNzVDNi4yNSAzLjcxNjUgNy4wMzM1IDQuNSA4IDQuNUM4Ljk2NjUgNC41IDkuNzUgMy43MTY1IDkuNzUgMi43NUM5Ljc1IDEuNzgzNSA4Ljk2NjUgMSA4IDFaIiBmaWxsPSIjNkY2RjZGIi8+CjxwYXRoIGQ9Ik04IDYuMjVDNy4wMzM1IDYuMjUgNi4yNSA3LjAzMzUgNi4yNSA4QzYuMjUgOC45NjY1IDcuMDMzNSA5Ljc1IDggOS43NUM4Ljk2NjUgOS43NSA5Ljc1IDguOTY2NSA5Ljc1IDhDOS43NSA3LjAzMzUgOC45NjY1IDYuMjUgOCA2LjI1WiIgZmlsbD0iIzZGNkY2RiIvPgo8cGF0aCBkPSJNOCAxMS41QzcuMDMzNSAxMS41IDYuMjUgMTIuMjgzNSA2LjI1IDEzLjI1QzYuMjUgMTQuMjE2NSA3LjAzMzUgMTUgOCAxNUM4Ljk2NjUgMTUgOS43NSAxNC4yMTY1IDkuNzUgMTMuMjVDOS43NSAxMi4yODM1IDguOTY2NSAxMS41IDggMTEuNVoiIGZpbGw9IiM2RjZGNkYiLz4KPC9zdmc+Cg==) in the upper-right corner.
    
    From the model page:
    
    ![model page kebab menu with delete](https://docs.databricks.com/aws/en/assets/images/uc-delete-model-dialog-20773050c836e40e42b1faea36645e0c.png)
    
    From the model version page:
    
    ![model version page kebab menu with delete](https://docs.databricks.com/aws/en/assets/images/uc-delete-model-version-dialog-b4888f254f756676d9eb2987e83d4562.png)
    
2.  Select **Delete**.
    
3.  A confirmation dialog appears. Click **Delete** to confirm.
    

### Delete a model version or model using the API[​](#delete-a-model-version-or-model-using-the-api "Direct link to Delete a model version or model using the API")

To delete a model version, use the MLflow Client API `delete_model_version()` method:

Python

    # Delete versions 1,2, and 3 of the modelclient = MlflowClient()versions=[1, 2, 3]for version in versions:  client.delete_model_version(name="<model-name>", version=version)

To delete a model, use the MLflow Client API `delete_registered_model()` method:

Python

    client = MlflowClient()client.delete_registered_model(name="<model-name>")

[Tags](https://docs.databricks.com/aws/en/database-objects/tags) are key-value pairs that you associate with registered models and model versions, allowing you to label and categorize them by function or status. For example, you could apply a tag with key `"task"` and value `"question-answering"` (displayed in the UI as `task:question-answering`) to registered models intended for question answering tasks. At the model version level, you could tag versions undergoing pre-deployment validation with `validation_status:pending` and those cleared for deployment with `validation_status:approved`.

**Permissions required**: Owner of or have `APPLY TAG` privilege on the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

See [Apply tags to Unity Catalog securable objects](https://docs.databricks.com/aws/en/database-objects/tags) to learn how to set and delete tags using the UI.

To set and delete tags using the MLflow Client API, see the examples below:

Python

    from mlflow import MlflowClientclient = MlflowClient()# Set registered model tagclient.set_registered_model_tag("prod.ml_team.iris_model", "task", "classification")# Delete registered model tagclient.delete_registered_model_tag("prod.ml_team.iris_model", "task")# Set model version tagclient.set_model_version_tag("prod.ml_team.iris_model", "1", "validation_status", "approved")# Delete model version tagclient.delete_model_version_tag("prod.ml_team.iris_model", "1", "validation_status")

Both registered model and model version tags must meet the [platform-wide constraints](https://docs.databricks.com/aws/en/database-objects/tags#constraint).

For more details on tag client APIs, see the [MLflow API documentation](https://mlflow.org/docs/latest/python_api/mlflow.client.html).

**Permissions required**: Owner of the registered model, plus `USE SCHEMA` and `USE CATALOG` privileges on the schema and catalog containing the model.

You can include a text description for any model or model version in Unity Catalog. For example, you can provide an overview of the problem or information about the methodology and algorithm used.

For models, you also have the option of using AI-generated comments. See [Add AI-generated comments to Unity Catalog objects](https://docs.databricks.com/aws/en/comments/ai-comments).

### Add a description to a model using the UI[​](#add-a-description-to-a-model-using-the-ui "Direct link to Add a description to a model using the UI")

To add a description for a model, you can use AI-generated comments, or you can enter your own comments. You can edit AI-generated comments as necessary.

*   To add automatically generated comments, click the **AI generate** button.
*   To add your own comments, click **Add**. Enter your comments in the dialog, and click **Save**.

![uc model description buttons](https://docs.databricks.com/aws/en/assets/images/uc-model-description-0fa4b7737238e0288a05ec2931920232.png)

### Add a description to a model version using the UI[​](#add-a-description-to-a-model-version-using-the-ui "Direct link to Add a description to a model version using the UI")

To add a description to a model version in Unity Catalog, follow these steps:

1.  On the model version page, click the pencil icon under **Description**.
    
    ![pencil icon to add comments to a model version](https://docs.databricks.com/aws/en/assets/images/uc-model-version-description-8065499e536ef509770fe88173c84556.png)
    
2.  Enter your comments in the dialog, and click **Save**.
    

### Add a description to a model or model version using the API[​](#add-a-description-to-a-model-or-model-version-using-the-api "Direct link to Add a description to a model or model version using the API")

To update a registered model description, use the MLflow Client API `update_registered_model()` method:

Python

    client = MlflowClient()client.update_registered_model(  name="<model-name>",  description="<description>")

To update a model version description, use the MLflow Client API `update_model_version()` method:

Python

    client = MlflowClient()client.update_model_version(  name="<model-name>",  version=<model-version>,  description="<description>")

## List and search models[​](#list-and-search-models "Direct link to List and search models")

To get a list of registered models in Unity Catalog, use MLflow's [search\_registered\_models()](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_registered_models#mlflow.search_registered_models) Python API:

Python

    mlflow.search_registered_models()

To search for a specific model name and get information about that model's versions, use `search_model_versions()`:

Python

    from pprint import pprint[pprint(mv) for mv in mlflow.search_model_versions("name='<model-name>'")]

note

Not all search API fields and operators are supported for models in Unity Catalog. See [Limitations](#limitations) for details.

## Download model files (advanced use case)[​](#download-model-files-advanced-use-case "Direct link to Download model files (advanced use case)")

In most cases, to load models, you should use MLflow APIs like `mlflow.pyfunc.load_model` or `mlflow.<flavor>.load_model` (for example, `mlflow.transformers.load_model` for HuggingFace models).

In some cases you may need to download model files to debug model behavior or model loading issues. You can download model files using `mlflow.artifacts.download_artifacts`, as follows:

Python

    import mlflowmlflow.set_registry_uri("databricks-uc")model_uri = f"models:/{model_name}/{version}" # reference model by version or aliasdestination_path = "/local_disk0/model"mlflow.artifacts.download_artifacts(artifact_uri=model_uri, dst_path=destination_path)

Databricks recommends that you deploy ML pipelines as code. This eliminates the need to promote models across environments, as all production models can be produced through automated training workflows in a production environment.

However, in some cases, it may be too expensive to retrain models across environments. Instead, you can copy model versions across registered models in Unity Catalog to promote them across environments.

You need the following privileges to execute the example code below:

*   `USE CATALOG` on the `staging` and `prod` catalogs.
*   `USE SCHEMA` on the `staging.ml_team` and `prod.ml_team` schemas.
*   `EXECUTE` on `staging.ml_team.fraud_detection`.

In addition, you need either ownership of the destination model `prod.ml_team.fraud_detection` or the [`CREATE MODEL VERSION`](https://docs.databricks.com/aws/en/data-governance/unity-catalog/access-control/privileges-reference#create-model-version) privilege on it.

The following code snippet uses the `copy_model_version` [MLflow Client API](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.copy_model_version), available in MLflow version 2.8.0 and above.

Python

    import mlflowmlflow.set_registry_uri("databricks-uc")client = mlflow.tracking.MlflowClient()src_model_name = "staging.ml_team.fraud_detection"src_model_version = "1"src_model_uri = f"models:/{src_model_name}/{src_model_version}"dst_model_name = "prod.ml_team.fraud_detection"copied_model_version = client.copy_model_version(src_model_uri, dst_model_name)

After the model version is in the production environment, you can perform any necessary pre-deployment validation. Then, you can mark the model version for deployment [using aliases](#uc-model-aliases).

Python

    client = mlflow.tracking.MlflowClient()client.set_registered_model_alias(name="prod.ml_team.fraud_detection", alias="Champion", version=copied_model_version.version)

In the example above, only users who can read from the `staging.ml_team.fraud_detection` registered model and write to the `prod.ml_team.fraud_detection` registered model can promote staging models to the production environment. The same users can also use aliases to manage which model versions are deployed within the production environment. You don't need to configure any other rules or policies to govern model promotion and deployment.

You can customize this flow to promote the model version across multiple environments that match your setup, such as `dev`, `qa`, and `prod`. Access control is enforced as configured in each environment.

## Example notebook[​](#example-notebook "Direct link to example-notebook")

This example notebook illustrates how to use Models in Unity Catalog APIs to manage models in Unity Catalog, including registering models and model versions, adding descriptions, loading and deploying models, using model aliases, and deleting models and model versions.

*   MLflow 3
*   MLflow 2.x

#### Models in Unity Catalog example notebook for MLflow 3

## Limitations[​](#limitations "Direct link to limitations")

*   Stages are not supported for models in Unity Catalog. Databricks recommends using the three-level namespace in Unity Catalog to express the environment a model is in, and using aliases to promote models for deployment. See [Promote a model across environments](#promote) for details.
*   Webhooks are not supported for models in Unity Catalog. See suggested alternatives in [the upgrade guide](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/upgrade-workflows#manual-approval).
*   Some search API fields and operators are not supported for models in Unity Catalog. This can be mitigated by calling the search APIs using supported filters and scanning the results. Following are some examples:
    *   The `order_by` parameter is not supported in the [search\_model\_versions](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_model_versions#mlflow.search_model_versions) or [search\_registered\_models](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_registered_models#mlflow.search_registered_models) client APIs.
    *   Tag-based filters (`tags.mykey = 'myvalue'`) are not supported for `search_model_versions` or `search_registered_models`.
    *   Operators other than exact equality (for example, `LIKE`, `ILIKE`, `!=`) are not supported for `search_model_versions` or `search_registered_models`.
    *   Searching registered models by name (for example, `search_registered_models(filter_string="name='main.default.mymodel'")` is not supported. To fetch a particular registered model by name, use [get\_registered\_model](https://mlflow.org/docs/latest/python_api/mlflow.client.html#mlflow.client.MlflowClient.get_registered_model).
*   Email notifications and comment discussion threads on registered models and model versions are not supported in Unity Catalog.
*   The activity log is not supported for models in Unity Catalog. To track activity on models in Unity Catalog, use [audit logs](https://docs.databricks.com/aws/en/admin/account-settings/audit-logs#uc).
*   `search_registered_models` might return stale results for models shared through OpenSharing. To ensure the most recent results, use the Databricks CLI or [SDK](https://databricks-sdk-py.readthedocs.io/en/latest/workspace/catalog/registered_models.html#databricks.sdk.service.catalog.RegisteredModelsAPI.list) to list the models in a schema.
