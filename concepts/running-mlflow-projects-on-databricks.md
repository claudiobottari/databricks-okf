---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6adcd68de5f92bc4b09ce77d5b40aaed30ac3b4dad35a316446e825fafa2748f
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - running-mlflow-projects-on-databricks
    - RMPOD
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: Running MLflow Projects on Databricks
description: The process of executing MLflow Projects remotely on Databricks clusters using the MLflow CLI with 'mlflow run <uri> -b databricks --backend-config <cluster-spec>' and Databricks CLI authentication.
tags:
  - databricks
  - mlflow
  - CLI
timestamp: "2026-06-19T20:17:22.032Z"
---

# Running MLflow Projects on Databricks

**MLflow Projects** provide a standard format for packaging data science code in a reusable and reproducible way. The Projects component includes an API and command‑line tools for running projects, and it integrates with the Tracking component to automatically record parameters and the git commit of the source code for reproducibility.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

> ⚠️ **Deprecation notice**: MLflow Projects is no longer supported. The products, services, and technologies mentioned in this content have been retired. This page is provided for historical reference only.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

MLflow Project execution is not supported on Databricks Free Edition.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## MLflow Project Format

Any local directory or Git repository can be treated as an MLflow Project. The following conventions define a project:^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

- The project’s name is the name of the directory.
- The software environment is specified in `python_env.yaml`, if present. If no `python_env.yaml` file is present, MLflow uses a virtualenv environment containing only Python (specifically, the latest Python available to virtualenv) when running the project.
- Any `.py` or `.sh` file in the project can be an entry point with no parameters explicitly declared. When you run such a command with a set of parameters, MLflow passes each parameter on the command line using `--key <value>` syntax.

You can specify more options by adding an `MLproject` file, a YAML text file. An example `MLproject` file looks like this:

```yaml
name: My Project
python_env: python_env.yaml
entry_points:
  main:
    parameters:
      data_file: path
      regularization: { type: float, default: 0.1 }
    command: 'python train.py -r {regularization} {data_file}'
  validate:
    parameters:
      data_file: path
    command: 'python validate.py {data_file}'
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

For Databricks Runtime 13.0 ML and above, MLflow Projects cannot successfully run within a Databricks job type cluster. In order to migrate existing MLflow Projects to Databricks Runtime 13.0 ML and above, see the [MLflow Databricks Spark job project format](/concepts/databricks-spark-job-project-format.md) described below.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## MLflow Databricks Spark Job Project Format

The **MLflow Databricks Spark job project** is a type of MLflow Project introduced in MLflow 2.14. This project type supports running MLflow Projects from within a Spark Jobs cluster and can only be run using the `databricks` backend.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

Databricks Spark job projects must set either `databricks_spark_job.python_file` or `entry_points`. Not specifying either or specifying both settings raises an exception.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Example using `databricks_spark_job.python_file`

This setting uses a hardcoded path for the Python run file and its arguments.

```yaml
name: My Databricks Spark job project 1
databricks_spark_job:
  python_file: 'train.py'
  parameters: ['param1', 'param2']
  python_libraries:
    - mlflow==2.4.1
    - scikit-learn
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Example using `entry_points`

```yaml
name: My Databricks Spark job project 2
databricks_spark_job:
  python_libraries:
    - mlflow==2.4.1
    - scikit-learn
entry_points:
  main:
    parameters:
      model_name: { type: string, default: model }
      script_name: { type: string, default: train.py }
    command: 'python {script_name} {model_name}'
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

The `entry_points` setting lets you pass in parameters via the command line, for example:

```bash
[[mlflow-run|MLflow Run]] . -b databricks --backend-config cluster-spec.json \
  -P script_name=train.py -P model_name=model123 \
  --experiment-id <experiment-id>
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Limitations for Databricks Spark Job Projects

- The project type does not support `docker_env`, `python_env`, or `conda_env` sections in the `MLproject` file.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- Dependencies must be specified in the `python_libraries` field of the `databricks_spark_job` section. Versions of Python cannot be customized.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- The running environment must use the main Spark driver runtime environment to run in jobs clusters that use Databricks Runtime 13.0 or above. All Python dependencies defined as required must be installed as Databricks cluster dependencies (this differs from previous project run behaviors where libraries needed to be installed in a separate environment).^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Run an MLflow Project

To run an MLflow project on a Databricks cluster in the default workspace, use the command:

```bash
[[mlflow-run|MLflow Run]] <uri> -b databricks --backend-config <json-new-cluster-spec>
```

where `<uri>` is a Git repository URI or folder containing an MLflow project, and `<json-new-cluster-spec>` is a JSON document containing a `new_cluster` structure (see the Databricks Jobs API). The Git URI should be of the form `https://github.com/<repo>#<project-folder>`.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

An example cluster specification:

```json
{
  "spark_version": "7.3.x-scala2.12",
  "num_workers": 1,
  "node_type_id": "i3.xlarge"
}
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

If you need to install libraries on the worker, use the cluster specification format. [Python Wheel Files](/concepts/python-wheel-files.md) must be uploaded to DBFS and specified as `pypi` dependencies. For example:

```json
{
  "new_cluster": {
    "spark_version": "7.3.x-scala2.12",
    "num_workers": 1,
    "node_type_id": "i3.xlarge"
  },
  "libraries": [
    { "pypi": { "package": "tensorflow" } },
    { "pypi": { "package": "/dbfs/path_to_my_lib.whl" } }
  ]
}
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Important Restrictions

- `.egg` and `.jar` dependencies are not supported for MLflow projects.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- Execution for MLflow projects with Docker environments is not supported.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- You **must** use a new cluster specification when running an MLflow Project on Databricks. Running Projects against existing clusters is not supported.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Using SparkR

To use SparkR in an MLflow Project run, your project code must first install and import SparkR as follows:

```r
if (file.exists("/databricks/spark/R/pkg")) {
    install.packages("/databricks/spark/R/pkg", repos = NULL)
} else {
    install.packages("SparkR")
}
library(SparkR)
```

Your project can then initialize a SparkR session and use SparkR as normal.^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Example: Running the MLflow Tutorial Project

This example demonstrates creating an experiment, running the MLflow tutorial project on a Databricks cluster, viewing the job run output, and viewing the run in the experiment.

### Requirements

1. Install MLflow using `pip install mlflow`.
2. Install and configure the Databricks CLI. The Databricks CLI authentication mechanism is required to run jobs on a Databricks cluster.

### Step 1: Create an Experiment

1. In the workspace, select **Create > MLflow Experiment**.
2. In the Name field, enter `Tutorial`.
3. Click **Create**. Note the Experiment ID (for example, `14622565`).

### Step 2: Run the MLflow Tutorial Project

1. Set the `MLFLOW_TRACKING_URI` environment variable to the Databricks workspace:

   ```bash
   export MLFLOW_TRACKING_URI=databricks
   ```

2. Run the MLflow tutorial project (training a wine model). Replace `<experiment-id>` with your Experiment ID:

   ```bash
   [[mlflow-run|MLflow Run]] https://github.com/mlflow/mlflow#examples/sklearn_elasticnet_wine -b databricks --backend-config cluster-spec.json --experiment-id <experiment-id>
   ```

   The output displays a URL for the run status, e.g., `https://<databricks-instance>#job/<job-id>/run/1`.

### Step 3: View the Databricks Job Run

Open the URL from the previous step in a browser to view the job run output.

### Step 4: View the Experiment and [MLflow Run](/concepts/mlflow-run.md) Details

Navigate to the experiment in your workspace, click the experiment, and then click a link in the Date column to display run details. You can view logs from your run by clicking the **Logs** link in the Job Output field.

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Resources

For example MLflow projects, see the MLflow App Library (a repository of ready-to-run projects aimed at making it easy to include ML functionality into your code).^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Related Concepts

- [MLflow](/concepts/mlflow.md) — Overview of the MLflow platform.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizing runs and tracking results.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The underlying job execution system for remote runs.
- Databricks CLI — Required for authentication when running projects.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Automatic recording of parameters and metrics.
- DBFS — Databricks File System for storing project archives and library wheels.

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
