---
title: Use custom Python libraries with Model Serving | Databricks on AWS
source: https://docs.databricks.com/aws/en/machine-learning/model-serving/private-libraries-model-serving
ingestedAt: "2026-06-18T08:12:21.515Z"
---

In this article, you learn how to include custom libraries or libraries from a private mirror server when you log your model, so that you can use them with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/) model deployments. You should complete the steps detailed in this guide after you have a trained ML model ready to deploy but before you create a Databricks [Model Serving endpoint](https://docs.databricks.com/aws/en/machine-learning/model-serving/create-manage-serving-endpoints).

Model development often requires the use of custom Python libraries that contain functions for pre- or post-processing, custom model definitions, and other shared utilities. In addition, many enterprise security teams encourage the use of private PyPi mirrors, such as Nexus or Artifactory, to reduce the risk of [supply-chain attacks](https://wikipedia.org/wiki/Supply_chain_attack). Databricks offers [native support](https://docs.databricks.com/aws/en/libraries/) for installation of custom libraries and libraries from a private mirror in the Databricks workspace.

## Requirements[​](#requirements "Direct link to Requirements")

*   MLflow 1.29 or higher

*   Restrict outbound network access from Model Serving endpoints by configuring network policies. See [Validate with model serving](https://docs.databricks.com/aws/en/security/network/serverless-network-security/manage-network-policies#model-serving).

## Option 1: Use a private package repository[​](#option-1-use-a-private-package-repository "Direct link to Option 1: Use a private package repository")

Use Option 1 if your organization uses a private PyPI mirror (such as Nexus or Artifactory). Workspace admins can configure it as the default package repository for the workspace. Model Serving automatically uses this workspace-level configuration when building your model environment.

To set up a private package repository, see [Configure default Python package repositories](https://docs.databricks.com/aws/en/admin/workspace-settings/default-python-packages).

Once configured, proceed to [Serve your model](#serve-your-model).

## Option 2: Package custom libraries as wheel files[​](#option-2-package-custom-libraries-as-wheel-files "Direct link to Option 2: Package custom libraries as wheel files")

Use Option 2 if a private PyPI mirror is not accessible, or if you have custom libraries that are not available in any package repository. You can package them as Python wheel files and include them when logging your model.

### Step 1: Upload your dependency file[​](#step-1-upload-your-dependency-file "Direct link to Step 1: Upload your dependency file")

Databricks recommends that you upload your dependency file to Unity Catalog [volumes](https://docs.databricks.com/aws/en/volumes/). Alternatively, you can upload it to [Databricks File System (DBFS)](https://docs.databricks.com/aws/en/dbfs/) using the Databricks UI.

To ensure your library is available to your notebook, you need to install it using `%pip`. Using `%pip` installs the library in the current notebook and downloads the dependency to the cluster.

### Step 2: Log the model with a custom library[​](#step-2-log-the-model-with-a-custom-library "Direct link to Step 2: Log the model with a custom library")

After you install the library and upload the Python wheel file to either Unity Catalog volumes or DBFS, include the following code in your script. In the `extra_pip_requirements` specify the path of your dependency file.

Python

    mlflow.sklearn.log_model(model, "sklearn-model", extra_pip_requirements=["/volumes/path/to/dependency.whl"])

For DBFS, use the following:

Python

    mlflow.sklearn.log_model(model, "sklearn-model", extra_pip_requirements=["/dbfs/path/to/dependency.whl"])

If you have a custom library, you must specify all custom Python libraries associated with your model when you configure logging. You can do so with the `extra_pip_requirements` or `conda_env` parameters in [log\_model()](https://www.mlflow.org/docs/latest/python_api/mlflow.sklearn.html#mlflow.sklearn.log_model).

important

If using DBFS, be sure to include a forward slash, `/`, before your `dbfs` path when logging `extra_pip_requirements`. Learn more about DBFS paths in [Work with files on Databricks](https://docs.databricks.com/aws/en/files/).

Python

    from mlflow.utils.environment import _mlflow_conda_envmlflow.pyfunc.log_model(    name="model",    python_model=MyModel(),    extra_pip_requirements=["/volumes/path/to/dependency.whl"],)

If your custom library is stored somewhere other than a volume or DBFS, you can specify its location using the `code_paths` parameter, and pass `"code/<wheel-file-name>.whl"` in the `extra_pip_requirements` parameter.

Python

    mlflow.pyfunc.log_model(    name="model",    python_model=MyModel(),    code_paths=["/path/to/dependency.whl"], # This will be logged as `code/dependency.whl`    extra_pip_requirements=["code/dependency.whl"],)

### Step 3: Update MLflow model with Python wheel files[​](#step-3-update-mlflow-model-with-python-wheel-files "Direct link to Step 3: Update MLflow model with Python wheel files")

MLflow provides the [add\_libraries\_to\_model()](https://mlflow.org/docs/latest/python_api/mlflow.models.html#mlflow.models.add_libraries_to_model) utility to log your model with all of its dependencies pre-packaged as Python wheel files. This packages your custom libraries alongside the model in addition to _all_ other libraries that are specified as dependencies of your model. This guarantees that the libraries used by your model are exactly the ones accessible from your training environment.

In the following example, `model_uri` references the Unity Catalog model registry using the syntax `models:/<uc-model>/<model-version>`. To reference the workspace model registry (legacy) use, `models:/<model-name>/<model-version>`.

When you use the model registry URI, this utility generates a new version under your existing registered model.

Python

    import mlflow.models.utilsmlflow.models.utils.add_libraries_to_model(<model-uri>)

## Serve your model[​](#serve-your-model "Direct link to Serve your model")

When a new model version with the packages included is available in the model registry, you can add this model version to an endpoint with [Model Serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/).

## Troubleshoot package installation[​](#troubleshoot-package-installation "Direct link to Troubleshoot package installation")

If your model deployment fails during the build phase, you can review the build logs to identify package installation issues.

1.  Go to the **Serving** page in your Databricks workspace.
2.  Click your endpoint name to open the endpoint details.
3.  Click the **Logs** tab.
4.  Select the failed version from the drop-down menu.
5.  Click **Build logs**.

Review the error messages to identify the issue.

After resolving the issue, create a new deployment or update your endpoint to trigger a new build.

### Troubleshoot private package repository[​](#troubleshoot-private-package-repository "Direct link to Troubleshoot private package repository")

If you are using a private package repository, common issues include:

*   **Missing packages**: The package is not available in your configured repository. Add the required package to your private repository.
*   **Connection issues**: Model Serving can't reach your package repository. Verify network connectivity and firewall rules.
*   **Authentication failures**: The credentials configured for your repository are not valid or expired. Update the secrets in your workspace configuration.

Serverless notebooks use the same default package repository configured for your workspace. You can use a notebook to test connectivity, authentication, and package availability by installing the requirements from your model's `requirements.txt` file before deploying to Model Serving.

Python

    import mlflowimport subprocessimport sys# Step 1: Set your model detailscatalog = "<your_catalog>"schema = "<your_schema>"model_name = "<your_model>"version = <your_version># Step 2: Download the model's requirements.txtfull_model_name = f"{catalog}.{schema}.{model_name}"requirements_uri = f"models:/{full_model_name}/{version}/requirements.txt"print(f"Downloading artifacts from: {requirements_uri}")local_path = mlflow.artifacts.download_artifacts(requirements_uri)# Step 3: Print the requirementswith open(local_path, "r") as f:    print(f.read())# Step 4: Install the requirements using the workspace's default package repositoryprint(f"Installing requirements from {local_path}...")subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", local_path])print("Installation complete!")
