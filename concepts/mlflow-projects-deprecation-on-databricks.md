---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e660efbd02ebfef489ac3ae02be94fa4c4a5f81fb12b947d9eaf46d08b419a5e
  pageDirectory: concepts
  sources:
    - run-mlflow-projects-on-databricks-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-projects-deprecation-on-databricks
    - MPDOD
  citations:
    - file: run-mlflow-projects-on-databricks-databricks-on-aws.md
title: MLflow Projects Deprecation on Databricks
description: MLflow Projects is no longer supported on Databricks; documentation is retired and users must migrate to alternative approaches, especially for Databricks Runtime 13.0 ML and above.
tags:
  - databricks
  - mlflow
  - deprecation
timestamp: "2026-06-19T20:17:22.222Z"
---

# MLflow Projects Deprecation on Databricks

**MLflow Projects**—the format for packaging data science code in reusable, reproducible ways—is no longer supported on Databricks. The feature’s documentation has been retired and will not be updated. The products, services, and technologies described in that documentation are no longer supported in the Databricks ecosystem. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Background

An [MLflow Project](/concepts/mlflow-projects.md) is a convention for structuring code with a `MLproject` file, a `python_env.yaml` (or `conda_env`), and entry points. Users previously ran projects on Databricks clusters using the `mlflow run` command with the `databricks` backend and a JSON cluster specification. However, this capability has been deprecated, and the related documentation is archived. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Affected Features

The deprecation applies to all MLflow Project execution on Databricks, including:

- Running projects via `mlflow run -b databricks` against new clusters.
- The [Databricks Spark Job Project Format](/concepts/databricks-spark-job-project-format.md) introduced in MLflow 2.14, which was meant to support running projects from Spark Jobs clusters on Databricks Runtime 13.0 ML and above.

Even though the Spark job format was presented as a migration path for Databricks Runtime 13.0+, the top-level deprecation notice indicates that the entire MLflow Projects functionality is now unsupported. Users should not rely on any form of MLflow Projects on Databricks going forward. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Migration Considerations

The deprecated documentation provided an alternative for Databricks Runtime 13.0 ML and above: the Databricks Spark job project format. That format required setting `databricks_spark_job.python_file` or `entry_points` in the `MLproject` file and did not support `docker_env`, `python_env`, or `conda_env`. Dependencies had to be declared in `python_libraries` and installed as cluster libraries. However, because the entire Projects feature is deprecated, this format is also unsupported, and users should seek other ways to package and run reusable code on Databricks, such as Notebooks, [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md), or MLflow Models with custom inference wrappers.

## Additional Restrictions

Even before the deprecation, MLflow Project execution was not supported on Databricks Free Edition. Additionally, running projects against existing clusters was never supported—only new cluster specifications could be used. ^[run-mlflow-projects-on-databricks-databricks-on-aws.md]

## Related Concepts

- [MLflow Projects](/concepts/mlflow-projects.md)  
- [Databricks Spark Job Project Format](/concepts/databricks-spark-job-project-format.md)  
- [MLflow Tracking](/concepts/mlflow-tracking.md)  
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md)  
- MLflow Models  
- Databricks Runtime

## Sources

- run-mlflow-projects-on-databricks-databricks-on-aws.md

# Citations

1. [run-mlflow-projects-on-databricks-databricks-on-aws.md](/references/run-mlflow-projects-on-databricks-databricks-on-aws-26c903d7.md)
