---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4417abffa849ca606d4eaa4587ad5acffe8413b56a0d712a02b9986fc8603860
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-project-environment-specification
    - MPES
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: MLflow Project Environment Specification
description: The software environment for an MLflow Project is defined via python_env.yaml for virtualenv, conda_env for Conda, or docker_env for Docker; if absent, a minimal Python virtualenv is used.
tags:
  - mlflow
  - environment
  - reproducibility
timestamp: "2026-06-19T20:17:05.729Z"
---

# MLflow Project Environment Specification

The **MLflow Project Environment Specification** defines the software environment in which an [MLflow Project](/concepts/mlflow-projects.md) runs. It is one of the key components of the MLflow Projects format, alongside the project name and entry points. The environment specification ensures reproducibility by explicitly declaring the dependencies required to execute the project's code. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Environment Specification Methods

MLflow supports several methods for specifying the project environment, which are defined in the [MLproject](/concepts/mlproject-file-format.md) file or through convention-based defaults.

### `python_env.yaml` (Recommended)

The `python_env.yaml` file is the primary method for specifying a Python virtual environment for an MLflow Project. When this file is present in the project directory, MLflow uses it to create a virtualenv environment with the specified dependencies. An example MLproject file referencing this environment looks like:

```yaml
name: My Project
python_env: python_env.yaml
entry_points:
  main:
    parameters:
      data_file: path
      regularization: { type: float, default: 0.1 }
    command: 'python train.py -r {regularization} {data_file}'
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Default Environment (No Specification File)

If no `python_env.yaml` file is present, MLflow uses a virtualenv environment containing only Python (specifically, the latest Python version available to virtualenv) when running the project. This minimal environment may not include necessary dependencies and is best suited for projects with no external library requirements. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Databricks Spark Job Project Environment

For MLflow Databricks Spark Job Projects, a different environment specification applies. This project type, introduced in MLflow 2.14, does not support `docker_env`, `python_env`, or `conda_env` in the `MLproject` file. Instead, dependencies must be specified in the `python_libraries` field of the `databricks_spark_job` section:

```yaml
name: My Databricks Spark job project
databricks_spark_job:
  python_file: 'train.py'
  parameters: ['param1', 'param2']
  python_libraries:
    - mlflow==2.4.1
    - scikit-learn
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

Key constraints for Spark job project environments include:

- Dependencies are installed as Databricks cluster libraries.
- The running environment uses the main Spark driver runtime environment (Databricks Runtime 13.0 or above).
- Python version cannot be customized.
- All Python dependencies defined must be installed as Databricks cluster dependencies, rather than in a separate environment. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Unsupported Environment Types

Certain environment specification types are not supported when running MLflow Projects on Databricks:

- **Docker environments** (`docker_env`) are not supported for execution.
- **Conda environments** (`conda_env`) are not supported for Databricks Spark job projects. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Running Projects with Environment Specifications

When running an MLflow Project on a Databricks cluster, libraries can be installed on workers using the cluster specification JSON format. For example, [Python Wheel Files](/concepts/python-wheel-files.md) must be uploaded to DBFS and specified as `pypi` dependencies:

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

Note that `.egg` and `.jar` dependencies are not supported for MLflow Projects. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Project](/concepts/mlflow-projects.md)
- [MLproject File](/concepts/mlproject-file-format.md)
- Databricks Cluster Libraries
- DBFS
- [MLflow Databricks Spark Job Project](/concepts/databricks-spark-job-project-format.md)
- Virtual Environment

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
