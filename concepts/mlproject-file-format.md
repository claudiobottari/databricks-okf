---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c4792f0a220493e160b48ec24129a9fcbc7eef1dc6810189415c6376f34a03c
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlproject-file-format
    - MFF
    - MLproject
    - MLproject File
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: MLproject File Format
description: A YAML-based configuration file that defines an MLflow Project's name, software environment, entry points, and parameters for more explicit project specification.
tags:
  - mlflow
  - configuration
  - YAML
timestamp: "2026-06-19T20:17:25.802Z"
---

# MLproject File Format

The **MLproject file format** is a YAML-based specification used by [MLflow Projects](/concepts/mlflow-projects.md) to define reusable and reproducible data science workflows. An MLproject file describes a project's name, its software environment, and its executable entry points, enabling both local and remote execution on platforms such as Databricks.

---

## Overview

An MLflow Project is a packaging convention that allows any local directory or Git repository to be treated as a runnable project. While the directory name and the presence of `.py` or `.sh` files establish a minimal project, richer metadata is supplied through an `MLproject` file (in YAML syntax). This extended format lets you declare explicit parameters, dependencies, and the runtime environment. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## MLproject File Structure

The canonical MLproject file contains the following top-level keys:

- **`name`** (required): The human-readable project name.
- **`python_env`**: Path to a `python_env.yaml` file that describes the Python environment. If omitted, MLflow defaults to a virtualenv containing only the latest Python version available. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- **`entry_points`** (optional): A map of named commands, each with its own parameter declarations and a `command` string that invokes a script with placeholders.

### Example

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

---

## Parameter Syntax

Parameters inside an entry point are declared using the following format:

```yaml
param_name: <type> [default: <value>]
```

Valid types include `string`, `float`, `path`, and `int`. When a parameter is given a `default`, the value is optional at run time. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

The `command` field uses curly-brace placeholders `{param_name}` that MLflow substitutes with the actual values provided via the `-P` flag (e.g., `-P script_name=train.py`). ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Databricks Spark Job Project Format

Starting in MLflow 2.14, a specialized variant of the MLproject format was introduced for running projects inside Databricks Runtime|Databricks Spark Jobs clusters. This variant uses the `databricks_spark_job` key instead of `entry_points` (or in addition to it) and has distinct constraints. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Structure

```yaml
name: My Databricks Spark job project 1
databricks_spark_job:
  python_file: 'train.py'
  parameters: ['param1', 'param2']
  python_libraries:
    - mlflow==2.4.1
    - scikit-learn
```

Alternatively, `entry_points` can be used for command-line parameterization:

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
    command: 'python {script_name} {model_name}'
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Limitations

- The `docker_env`, `python_env`, and `conda_env` sections are **not supported** for Spark job projects. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- Dependencies must be listed in the `python_libraries` field; Python version customization is not available. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- The runtime environment for projects running on Databricks Runtime 13.0 ML and above must use the main Spark driver environment. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Execution

The MLflow CLI (`mlflow run`) is used to execute projects. The typical invocation pattern is:

```bash
[[mlflow-run|MLflow Run]] <uri> -b databricks --backend-config <json-new-cluster-spec>
```

`<uri>` can be a local path or a Git URL (e.g., `https://github.com/<repo>#<project-folder>`). For Databricks execution, a JSON cluster specification is required; existing clusters are not supported. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

A sample cluster specification:

```json
{
  "spark_version": "7.3.x-scala2.12",
  "num_workers": 1,
  "node_type_id": "i3.xlarge"
}
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

---

## Related Concepts

- [MLflow Projects](/concepts/mlflow-projects.md) — The packaging system enabled by the MLproject format.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — Integration that automatically records parameters, metrics, and code from project runs.
- python_env.yaml — The environment descriptor referenced by the `python_env` field.
- Databricks CLI — Authentication mechanism required for running projects on Databricks.
- [MLflow Databricks Spark job project format](/concepts/databricks-spark-job-project-format.md) — The specialized variant for Spark job execution.

---

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
