---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 83e0f09402fca7e6636de3d671601d670312d980ae5e41ab7ef09d8a12a7f1ea
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-projects
    - MLflow Project
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: MLflow Projects
description: A format for packaging data science code in a reusable and reproducible way, including API and CLI tools for running projects with automatic parameter and git commit tracking.
tags:
  - machine-learning
  - mlflow
  - reproducibility
timestamp: "2026-06-19T20:16:58.440Z"
---

# MLflow Projects

**MLflow Projects** is a component of the [MLflow](/concepts/mlflow.md) ecosystem that provides a format for packaging data science code in a reusable and reproducible way. It includes an API and command-line tools for running projects, which integrate with the [MLflow Tracking](/concepts/mlflow-tracking.md) component to automatically record parameters and git commit information for reproducibility. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

> **Note:** MLflow Projects is no longer supported. The documentation has been retired and might not be updated. The products, services, or technologies mentioned in this content are no longer supported. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Project Format

Any local directory or Git repository can be treated as an MLflow project. The following conventions define a project:

- The project's name is the name of the directory.
- The software environment is specified in `python_env.yaml`, if present. If no `python_env.yaml` file is present, MLflow uses a virtualenv environment containing only Python (specifically, the latest Python available to virtualenv) when running the project.
- Any `.py` or `.sh` file in the project can be an entry point, with no parameters explicitly declared. When you run such a command with a set of parameters, MLflow passes each parameter on the command line using `--key <value>` syntax.

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

You specify more options by adding an `MLproject` file, which is a text file in YAML syntax. An example `MLproject` file looks like this:

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

For Databricks Runtime 13.0 ML and above, MLflow Projects cannot successfully run within a Databricks job type cluster. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Databricks Spark Job Project Format

MLflow Databricks Spark job project is a type of MLflow Project introduced in MLflow 2.14. This project type supports running MLflow Projects from within a Spark Jobs cluster and can only be run using the `databricks` backend. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

Databricks Spark job projects must set either `databricks_spark_job.python_file` or `entry_points`. Not specifying either or specifying both settings raises an exception. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

The following is an example of an `MLproject` file that uses the `databricks_spark_job.python_file` setting:

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

The following is an example of an `MLproject` file that uses the `entry_points` setting:

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

The `entry_points` setting lets you pass in parameters using command line params, like:

```bash
[[mlflow-run|MLflow Run]] . -b databricks --backend-config cluster-spec.json \
 -P script_name=train.py -P model_name=model123 \
 --experiment-id <experiment-id>
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Limitations for Databricks Spark Job Projects

- This project type does not support specifying the following sections in the `MLproject` file: `docker_env`, `python_env`, or `conda_env`.
- Dependencies for your project must be specified in the `python_libraries` field of the `databricks_spark_job` section. Versions of Python cannot be customized with this project type.
- The running environment must use the main Spark driver runtime environment to run in jobs clusters that use Databricks Runtime 13.0 or above.
- All Python dependencies that are defined as required for the project must be installed as Databricks cluster dependencies. This behavior is different from previous project run behaviors where libraries needed to be installed in a separate environment.

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Running an MLflow Project

To run an MLflow project on a Databricks cluster in the default workspace, use the command:

```bash
[[mlflow-run|MLflow Run]] <uri> -b databricks --backend-config <json-new-cluster-spec>
```

where `<uri>` is a Git repository URI or folder containing an MLflow project and `<json-new-cluster-spec>` is a JSON document containing a [new_cluster structure](https://docs.databricks.com/api/workspace/jobs). The Git URI should be of the form: `https://github.com/<repo>#<project-folder>`. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

An example cluster specification is:

```json
{
  "spark_version": "7.3.x-scala2.12",
  "num_workers": 1,
  "node_type_id": "i3.xlarge"
}
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

If you need to install libraries on the worker, use the "cluster specification" format. [Python Wheel Files](/concepts/python-wheel-files.md) must be uploaded to DBFS and specified as `pypi` dependencies. For example:

```json
{
  "new_cluster": {
    "spark_version": "7.3.x-scala2.12",
    "num_workers": 1,
    "node_type_id": "i3.xlarge"
  },
  "libraries": [
    {
      "pypi": {
        "package": "tensorflow"
      }
    },
    {
      "pypi": {
        "package": "/dbfs/path_to_my_lib.whl"
      }
    }
  ]
}
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Important Notes

- `.egg` and `.jar` dependencies are not supported for MLflow projects.
- Execution for MLflow projects with Docker environments is not supported.
- You must use a new cluster specification when running an MLflow Project on Databricks. Running Projects against existing clusters is not supported.
- MLflow Project execution is not supported on Databricks Free Edition.

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Using SparkR

In order to use SparkR in an MLflow Project run, your project code must first install and import SparkR as follows:

```r
if (file.exists("/databricks/spark/R/pkg")) {
    install.packages("/databricks/spark/R/pkg", repos = NULL)
} else {
    install.packages("SparkR")
}
library(SparkR)
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md) — Records parameters, metrics, and artifacts from MLflow Project runs
- [MLflow Experiments](/concepts/mlflow-experiment.md) — Organizational unit for grouping related MLflow runs
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The execution environment for running MLflow Projects on Databricks
- Databricks CLI — Required authentication mechanism for running projects on Databricks clusters
- MLflow Models — Format for packaging machine learning models

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
