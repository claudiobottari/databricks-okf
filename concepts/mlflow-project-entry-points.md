---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c12a49a99932c08c045b08f0d521c8076da16123cb2ad6a481d4e160c84e1fe
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-project-entry-points
    - MPEP
    - Entry points
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: MLflow Project Entry Points
description: Executable commands within an MLflow Project defined in the MLproject file, with optional parameters declared with types and defaults, and commanded via 'command' field in YAML.
tags:
  - mlflow
  - configuration
  - CLI
timestamp: "2026-06-19T20:17:16.858Z"
---

# MLflow Project Entry Points

**MLflow Project Entry Points** define the executable commands within an [MLflow Project](/concepts/mlflow-projects.md). Each entry point specifies a command to run, along with declared parameters that can be overridden when the project is executed. Entry points are the primary mechanism for interacting with a packaged project, enabling reproducible runs with custom inputs. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Overview

An MLflow Project can have one or more entry points. Entry points are explicitly declared in an [`MLproject` file](/concepts/mlproject-file) (a YAML text file) under the `entry_points` section. If no `MLproject` file exists, any `.py` or `.sh` file in the project directory is treated as a default entry point, with parameters passed automatically via `--key <value>` syntax on the command line. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Defining Entry Points

Entry points are defined in the `MLproject` file using YAML. Each entry point has a name, an optional `parameters` map, and a `command` string. The command string can reference parameter values using curly-brace substitution (e.g., `{regularization}`). ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

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

## Entry Point Parameters

Each parameter in an entry point can be declared with a **type** and an optional **default** value. The type restricts the expected value (e.g., `float`, `path`, `string`). When a parameter has a default value, it may be omitted at runtime; otherwise it is required. Parameters are substituted into the command string at the positions indicated by the `{parameter_name}` placeholders. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

When running the project via the MLflow CLI, parameters are passed using the `-P` flag:

```bash
[[mlflow-run|MLflow Run]] . -P regularization=0.2 -P data_file=/path/to/data
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Databricks Spark Job Project Format

For Databricks Spark job projects (a type of MLflow Project introduced in MLflow 2.14), entry points can also be defined but with some restrictions. The `MLproject` file must set either `databricks_spark_job.python_file` or `entry_points`, but not both. When using `entry_points`, parameters are passed via command line arguments just like standard projects. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

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

This project type does **not** support `docker_env`, `python_env`, or `conda_env` sections. Dependencies must be listed in `python_libraries` within the `databricks_spark_job` section. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Running Entry Points

Entry points are run using the `mlflow run` CLI command. The project is identified by a URI (local directory or Git repository), and the entry point name can be specified with the `--entry-point` flag (defaults to `main` if not given). Parameters are provided with `-P` flags. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

```bash
[[mlflow-run|MLflow Run]] https://github.com/example/project#example -b databricks \
  --backend-config cluster-spec.json --experiment-id 123 \
  -P data_file=/dbfs/data.csv -P regularization=0.01
```

^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

The MLflow Tracking component automatically records the entry point parameters, git commit, and run results for reproducibility.

## Related Concepts

- [MLproject File](/concepts/mlproject-file-format.md) – YAML file that declares the project name, environment, and entry points.
- [MLflow Projects](/concepts/mlflow-projects.md) – The packaging format for reusable data science code.
- MLflow CLI – Command-line interface for running projects and tracking experiments.
- [Parameter Substitution](/concepts/prompt-templates-with-variable-substitution.md) – Mechanism for injecting values into the command string.
- Databricks Spark Job Project – A variant of MLflow Project designed for Databricks job clusters.

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
