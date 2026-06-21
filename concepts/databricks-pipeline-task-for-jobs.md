---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b7519711e357f4323d09225fddb721d8298e6b655140ae20883f404be9ac4a33
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-pipeline-task-for-jobs
    - DPTFJ
    - Databricks Pipelines
    - Databricks pipeline
    - Orchestrate Databricks Pipelines with Jobs
    - Pipeline task for jobs
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Databricks Pipeline Task for Jobs
description: Using the Pipeline task type in Databricks Jobs to include a Lakeflow Spark Declarative Pipeline as a step in a multi-task job workflow.
tags:
  - workflow-orchestration
  - databricks-jobs
  - pipelines
timestamp: "2026-06-19T20:17:36.287Z"
---

# Databricks Pipeline Task for Jobs

The **Databricks Pipeline Task** is a task type available within [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) that allows you to include a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md) as part of a data processing workflow. By using the Pipeline task, you can orchestrate multiple tasks in a single job, including a pipeline update as one step in a larger workflow. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Overview

A pipeline task enables you to trigger a pipeline update as a task within a Databricks job. When you create a job, you add a task of type "Pipeline" and specify the pipeline ID to run. This task can be combined with other task types—such as notebooks, Python scripts, or JAR tasks—to build a comprehensive data processing workflow. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

The Pipeline task is one of several ways to run a pipeline in a workflow. Other orchestration options include Apache Airflow and Azure Data Factory. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Using the Pipeline Task in a Job

To include a pipeline in a job:

1. Create or open a Databricks Job in the Jobs UI.
2. Add a new task to the job.
3. Select **Pipeline** as the task type.
4. Provide the pipeline ID for the pipeline you want to run.
5. Configure any additional task settings (such as retries, dependencies on other tasks, or notifications). ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

The pipeline task triggers an update for the specified pipeline each time the job runs. You can view the details of the pipeline update in the pipeline UI. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md) — The job execution platform that orchestrates multiple tasks.
- [Pipeline task for jobs](/concepts/databricks-pipeline-task-for-jobs.md) — The specific task type documentation for configuring pipeline tasks in jobs.
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — The pipeline definition format used by the Pipeline task.
- Job task orchestration — Combining multiple task types in a single job.
- Apache Airflow — Alternative orchestration method for running pipelines.
- Azure Data Factory — Alternative orchestration method for running pipelines.

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
