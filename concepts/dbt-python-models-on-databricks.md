---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a4884792f02ff5b0a8715b9c6def77d6c1dc9f2362bd121aadaa25209f4ddbf
  pageDirectory: concepts
  sources:
    - use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbt-python-models-on-databricks
    - DPMOD
    - Python Models in dbt
    - dbt Python models
  citations:
    - file: use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
title: dbt Python Models on Databricks
description: Running dbt Python models (beta, requires dbt >= 1.3) as part of a Databricks job, noting that SQL warehouses are not supported for Python models and all-purpose compute must be used.
tags:
  - dbt
  - python-models
  - databricks
timestamp: "2026-06-19T23:21:25.148Z"
---

# dbt Python Models on Databricks

**dbt Python Models on Databricks** refers to the ability to define data transformations using Python code within dbt projects, executed on the Databricks platform. This feature enables data practitioners to implement complex transformations that are difficult or impractical to express using SQL alone, leveraging the Python ecosystem's libraries and tools. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Overview

dbt Python models are a feature introduced in dbt 1.3 or greater that allows you to write data transformations in Python instead of SQL. These models are supported on specific data warehouses, including Databricks. Python models are particularly useful for transformations that require advanced statistical methods, machine learning inference, or complex data manipulation that would be cumbersome in SQL. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Running Python Models in Databricks Jobs

You can run dbt Python models as part of a Databricks Job workflow. The dbt task in a job can execute Python models alongside traditional SQL models, allowing you to create comprehensive data pipelines that combine both approaches. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Workflow Integration

A Databricks job can include a dbt task that runs Python models as part of a larger workflow. For example, your workflow might ingest data with Auto Loader, transform the data using dbt (including Python models), and analyze the results with a notebook task. This integration allows you to benefit from [Lakeflow Jobs](/concepts/lakeflow-jobs.md) features such as scheduling, monitoring, and automatic artifact archiving. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Important Limitations

### SQL Warehouse Restriction

You **cannot** run Python models in a dbt task using a SQL Warehouse. Python models require a different execution environment than SQL models. When configuring a dbt task that includes Python models, you must select a compute option other than a SQL warehouse. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

### Compute Requirements

To run dbt Python models, you need to use either:
- All-Purpose Compute (interactive clusters)
- Job Compute (job clusters)

The dbt task must be configured to use one of these compute types rather than a SQL warehouse. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Configuration

When setting up a dbt task that includes Python models, you must configure the compute appropriately. In the task configuration:

1. Set **SQL warehouse** to **None (Manual)**.
2. Configure the **dbt CLI compute** to use an appropriate cluster.
3. Ensure the cluster has the necessary Python dependencies installed for your Python models.

^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Best Practices

- Use Python models for transformations that are genuinely difficult to implement in SQL, such as those requiring iterative algorithms, external library calls, or complex statistical computations.
- Keep SQL models for standard data transformations that are more performant and easier to maintain in SQL.
- Test Python models thoroughly, as debugging Python transformations in a distributed environment can be more complex than SQL.
- Consider the performance implications of Python models, as they may not benefit from the same optimizations as SQL models on Databricks.

## Related Concepts

- dbt Core — The open-source transformation tool that powers dbt projects.
- [dbt-databricks Package](/concepts/dbt-databricks-adapter-package.md) — The recommended adapter for connecting dbt to Databricks.
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The workflow orchestration service for running dbt tasks.
- [Python Models in dbt](/concepts/dbt-python-models-on-databricks.md) — General documentation on writing Python models in dbt.
- SQL Warehouse — The compute type that cannot run Python models.

## Sources

- use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md](/references/use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws-9420061c.md)
