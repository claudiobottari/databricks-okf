---
title: Run MLflow Projects on Databricks | Databricks on AWS
source: https://docs.databricks.com/aws/en/archive/mlflow/projects
ingestedAt: "2026-06-18T08:03:11.433Z"
---

note

MLflow Projects is no longer supported.

This documentation has been retired and might not be updated. The products, services, or technologies mentioned in this content are no longer supported.

An [MLflow Project](https://mlflow.org/docs/latest/projects.html#) is a format for packaging data science code in a reusable and reproducible way. The MLflow Projects component includes an API and command-line tools for running projects, which also integrate with the Tracking component to automatically record the parameters and git commit of your source code for reproducibility.

This article describes the format of an MLflow Project and how to run an MLflow project remotely on Databricks clusters using the MLflow CLI, which makes it easy to vertically scale your data science code.

MLflow Project execution is not supported on Databricks Free Edition.

## MLflow project format[​](#mlflow-project-format "Direct link to MLflow project format")

Any local directory or Git repository can be treated as an MLflow project. The following conventions define a project:

*   The project's name is the name of the directory.
*   The software environment is specified in `python_env.yaml`, if present. If no `python_env.yaml` file is present, MLflow uses a virtualenv environment containing only Python (specifically, the latest Python available to virtualenv) when running the project.
*   Any `.py` or `.sh` file in the project can be an entry point, with no parameters explicitly declared. When you run such a command with a set of parameters, MLflow passes each parameter on the command line using `--key <value>` syntax.

You specify more options by adding an MLproject file, which is a text file in YAML syntax. An example MLproject file looks like this:

YAML

    name: My Projectpython_env: python_env.yamlentry_points:  main:    parameters:      data_file: path      regularization: { type: float, default: 0.1 }    command: 'python train.py -r {regularization} {data_file}'  validate:    parameters:      data_file: path    command: 'python validate.py {data_file}'

For Databricks Runtime 13.0 ML and above, MLflow Projects cannot successfully run within a Databricks job type cluster. In order to migrate existing MLflow Projects to Databricks Runtime 13.0 ML and above, see [MLflow Databricks Spark job project format](#spark-project-format).

## MLflow Databricks Spark job project format[​](#mlflow-databricks-spark-job-project-format "Direct link to mlflow-databricks-spark-job-project-format")

MLflow Databricks Spark job project is a type of MLflow Project introduced in MLflow 2.14. This project type supports running MLflow Projects from within a Spark Jobs cluster and can only be run using the `databricks` backend.

Databricks Spark job projects must set either `databricks_spark_job.python_file` or `entry_points`. Not specifying either or specifying both settings raises an exception.

The following is an example of an `MLproject` file that uses the `databricks_spark_job.python_file` setting. This setting involves using a hardcoded path for the Python run file and its arguments.

YAML

    name: My Databricks Spark job project 1databricks_spark_job:  python_file: 'train.py' # the file which is the entry point file to execute  parameters: ['param1', 'param2'] # a list of parameter strings  python_libraries: # dependencies required by this project    - mlflow==2.4.1 # MLflow dependency is required    - scikit-learn

The following is an example of an `MLproject` file that uses the `entry_points` setting:

YAML

    name: My Databricks Spark job project 2databricks_spark_job:  python_libraries: # dependencies to be installed as databricks cluster libraries    - mlflow==2.4.1    - scikit-learnentry_points:  main:    parameters:      model_name: { type: string, default: model }      script_name: { type: string, default: train.py }    command: 'python {script_name} {model_name}'

The `entry_points` setting lets you pass in parameters that are using command line params, like:

    mlflow run . -b databricks --backend-config cluster-spec.json \ -P script_name=train.py -P model_name=model123 \ --experiment-id <experiment-id>

The following limitations apply for Databricks Spark job projects:

*   This project type does not support specifying the following sections in the `MLproject` file: `docker_env`, `python_env`, or `conda_env`.
*   Dependencies for your project must be specified in the `python_libraries` field of the `databricks_spark_job` section. Versions of Python cannot be customized with this project type.
*   The running environment must use the main Spark driver runtime environment to run in jobs clusters that use Databricks Runtime 13.0 or above.
    *   Likewise, all Python dependencies that are defined as required for the project must be installed as Databricks cluster dependencies. This behavior is different from previous project run behaviors where libraries needed to be installed in a separate environment.

## Run an MLflow project[​](#run-an-mlflow-project "Direct link to Run an MLflow project")

To run an MLflow project on a Databricks cluster in the default workspace, use the command:

Bash

    mlflow run <uri> -b databricks --backend-config <json-new-cluster-spec>

where `<uri>` is a Git repository URI or folder containing an MLflow project and `<json-new-cluster-spec>` is a JSON document containing a [new\_cluster structure](https://docs.databricks.com/api/workspace/jobs). The Git URI should be of the form: `https://github.com/<repo>#<project-folder>`.

An example cluster specification is:

JSON

    {  "spark_version": "7.3.x-scala2.12",  "num_workers": 1,  "node_type_id": "i3.xlarge"}

If you need to install libraries on the worker, use the “cluster specification” format. Note that Python wheel files must be uploaded to DBFS and specified as `pypi` dependencies. For example:

JSON

    {  "new_cluster": {    "spark_version": "7.3.x-scala2.12",    "num_workers": 1,    "node_type_id": "i3.xlarge"  },  "libraries": [    {      "pypi": {        "package": "tensorflow"      }    },    {      "pypi": {        "package": "/dbfs/path_to_my_lib.whl"      }    }  ]}

important

*   `.egg` and `.jar` dependencies are not supported for MLflow projects.
*   Execution for MLflow projects with Docker environments is not supported.
*   You must use a new cluster specification when running an MLflow Project on Databricks. Running Projects against existing clusters is not supported.

### Using SparkR[​](#using-sparkr "Direct link to Using SparkR")

In order to use SparkR in an MLflow Project run, your project code must first install and import SparkR as follows:

R

    if (file.exists("/databricks/spark/R/pkg")) {    install.packages("/databricks/spark/R/pkg", repos = NULL)} else {    install.packages("SparkR")}library(SparkR)

Your project can then initialize a SparkR session and use SparkR as normal:

## Example[​](#example "Direct link to example")

This example shows how to create an experiment, run the MLflow tutorial project on a Databricks cluster, view the job run output, and view the run in the experiment.

### Requirements[​](#requirements "Direct link to Requirements")

1.  Install MLflow using `pip install mlflow`.
2.  Install and configure the [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/). The Databricks CLI authentication mechanism is required to run jobs on a Databricks cluster.

### Step 1: Create an experiment[​](#step-1-create-an-experiment "Direct link to Step 1: Create an experiment")

1.  In the workspace, select **Create > MLflow Experiment**.
    
2.  In the Name field, enter `Tutorial`.
    
3.  Click **Create**. Note the Experiment ID. In this example, it is `14622565`.
    
    ![Experiment ID](https://docs.databricks.com/aws/en/assets/images/mlflow-experiment-id-cd69957fcec99886423dd14ce1afd2ba.png)
    

### Step 2: Run the MLflow tutorial project[​](#step-2-run-the-mlflow-tutorial-project "Direct link to Step 2: Run the MLflow tutorial project")

The following steps set up the `MLFLOW_TRACKING_URI` environment variable and run the project, recording the training parameters, metrics, and the trained model to the experiment noted in the preceding step:

1.  Set the `MLFLOW_TRACKING_URI` environment variable to the Databricks workspace.
    
    Bash
    
        export MLFLOW_TRACKING_URI=databricks
    
2.  Run the MLflow tutorial project, training a [wine model](https://github.com/mlflow/mlflow/tree/master/examples/sklearn_elasticnet_wine). Replace `<experiment-id>` with the Experiment ID you noted in the preceding step.
    
    Bash
    
        mlflow run https://github.com/mlflow/mlflow#examples/sklearn_elasticnet_wine -b databricks --backend-config cluster-spec.json --experiment-id <experiment-id>
    
    Console
    
        === Fetching project from https://github.com/mlflow/mlflow#examples/sklearn_elasticnet_wine into /var/folders/kc/l20y4txd5w3_xrdhw6cnz1080000gp/T/tmpbct_5g8u ====== Uploading project to DBFS path /dbfs/mlflow-experiments/<experiment-id>/projects-code/16e66ccbff0a4e22278e4d73ec733e2c9a33efbd1e6f70e3c7b47b8b5f1e4fa3.tar.gz ====== Finished uploading project to /dbfs/mlflow-experiments/<experiment-id>/projects-code/16e66ccbff0a4e22278e4d73ec733e2c9a33efbd1e6f70e3c7b47b8b5f1e4fa3.tar.gz ====== Running entry point main of project https://github.com/mlflow/mlflow#examples/sklearn_elasticnet_wine on Databricks ====== Launched MLflow run as Databricks job run with ID 8651121. Getting run status page URL... ====== Check the run's status at https://<databricks-instance>#job/<job-id>/run/1 ===
    
3.  Copy the URL `https://<databricks-instance>#job/<job-id>/run/1` in the last line of the MLflow run output.
    

### Step 3: View the Databricks job run[​](#step-3-view-the-databricks-job-run "Direct link to step-3-view-the-databricks-job-run")

1.  Open the URL you copied in the preceding step in a browser to view the Databricks job run output:
    
    ![Job run output](https://docs.databricks.com/aws/en/assets/images/mlflow-job-run-ecf7d8972c563741e92a73c403a56142.png)
    

### Step 4: View the experiment and MLflow run details[​](#step-4-view-the-experiment-and-mlflow-run-details "Direct link to Step 4: View the experiment and MLflow run details")

1.  Navigate to the experiment in your Databricks workspace.
    
    ![Go to experiment](https://docs.databricks.com/aws/en/assets/images/mlflow-workspace-experiment-31772661bd6b81094fd90d6c248df115.png)
    
2.  Click the experiment.
    
    ![View experiment](https://docs.databricks.com/aws/en/assets/images/mlflow-experiment-65933a52d14d28699e2b363869406923.png)
    
3.  To display run details, click a link in the Date column.
    
    ![Run details](https://docs.databricks.com/aws/en/assets/images/mlflow-run-remote-a4c49d057a028dfebbb8296846457dcd.png)
    

You can view logs from your run by clicking the **Logs** link in the Job Output field.

## Resources[​](#resources "Direct link to Resources")

For some example MLflow projects, see the [MLflow App Library](https://github.com/mlflow/mlflow-apps), which contains a repository of ready-to-run projects aimed at making it easy to include ML functionality into your code.
