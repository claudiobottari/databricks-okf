---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37ceff266bb180796bd52136099fb8ee17c046a1bd707e9b3d41ecc272a3d927
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-spark-job-project-format
    - DSJPF
    - Databricks Spark Job Project
    - MLflow Databricks Spark job project format
    - MLflow Databricks Spark Job Project
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: Databricks Spark Job Project Format
description: A specialized MLflow Project type for Databricks Spark Jobs clusters (Runtime 13.0+), using databricks_spark_job section with python_file or entry_points settings and python_libraries dependencies.
tags:
  - databricks
  - mlflow
  - spark
timestamp: "2026-06-19T20:17:09.399Z"
---

# Databricks Spark Job Project Format

The **Databricks Spark Job Project Format** is a type of [MLflow Project](/concepts/mlflow-projects.md) introduced in MLflow 2.14. It enables running MLflow Projects from within a Spark Jobs cluster on Databricks. Unlike standard MLflow Projects, which are run on a separate cluster, this format is designed to execute directly in the same environment as the Spark job and can only be used with the `databricks` backend. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Format specification

A Databricks Spark Job Project is defined by an `MLproject` file in YAML syntax. The file must contain a `databricks_spark_job` section with one of two mutually exclusive settings: `python_file` or `entry_points`. Specifying both or neither raises an exception. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

### Using `databricks_spark_job.python_file`

This setting uses a hardcoded path for the Python run file and its arguments. Dependencies are listed in the `python_libraries` field within the same section. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

```yaml
name: My Databricks Spark job project 1
databricks_spark_job:
  python_file: 'train.py'
  parameters: ['param1', 'param2']
  python_libraries:
    - mlflow==2.4.1
    - scikit-learn
```

### Using `entry_points`

This setting defines parameterized entry points, similar to a standard MLflow Project. Parameters are passed via the `mlflow run` command line. The `databricks_spark_job.python_libraries` section is still used for dependencies. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

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

Example invocation:

```bash
[[mlflow-run|MLflow Run]] . -b databricks --backend-config cluster-spec.json \
  -P script_name=train.py -P model_name=model123 \
  --experiment-id <experiment-id>
```

## Limitations

- The `MLproject` file cannot include `docker_env`, `python_env`, or `conda_env` sections. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- Dependencies must be specified in the `databricks_spark_job.python_libraries` field and are installed as Databricks cluster libraries. Python version customization is not supported. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]
- The running environment uses the main Spark driver runtime; this differs from earlier project run behaviors that used separate environments. The project type is intended for Databricks Runtime 13.0 ML or above and serves as a migration path for standard MLflow Projects that no longer work on job clusters in those runtimes. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Example usage

The following steps outline how to create and run a Databricks Spark Job Project:

1. Create an MLflow experiment in the Databricks workspace.
2. Write an `MLproject` file using one of the formats above.
3. Set `MLFLOW_TRACKING_URI=databricks`.
4. Run the project with `mlflow run` using `-b databricks` and a valid backend cluster specification JSON file.
5. Monitor the job run in the Databricks Jobs UI and view run details in the experiment.

(See the source documentation for a complete walkthrough with a wine-quality training example.) ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Related concepts

- [MLflow Project](/concepts/mlflow-projects.md) – General format for packaging data science code.
- [MLflow](/concepts/mlflow.md) – The open-source platform for ML lifecycle management.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) – The execution environment for Spark jobs.
- [Databricks Runtime ML](/concepts/databricks-runtime-ml.md) – The runtime version required for this project format.

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
