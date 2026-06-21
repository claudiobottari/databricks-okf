---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1e05c3a1dfdd6121a44574b397afcf89fce0f797e58f6dd9f983e14eb3c4a14b
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - apache-airflow-orchestration-for-databricks-pipelines
    - AAOFDP
    - Orchestrate Databricks Pipelines with Apache Airflow
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Apache Airflow Orchestration for Databricks Pipelines
description: Triggering pipeline updates from Apache Airflow DAGs using the DatabricksSubmitRunOperator with a pipeline_task configuration.
tags:
  - workflow-orchestration
  - apache-airflow
  - pipelines
timestamp: "2026-06-19T20:17:32.712Z"
---

# Apache Airflow Orchestration for Databricks Pipelines

**Apache Airflow Orchestration for Databricks Pipelines** describes how to use Apache Airflow to schedule and manage the execution of [Databricks Pipelines](/concepts/databricks-pipeline-task-for-jobs.md) (Lakeflow Spark Declarative Pipelines) as part of a larger data processing workflow. Airflow represents workflows as directed acyclic graphs (DAGs) defined in Python files, and it handles scheduling and execution. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## How It Works

To run a pipeline within an Airflow DAG, use the `DatabricksSubmitRunOperator` from the [Databricks provider for Airflow](https://airflow.apache.org/docs/apache-airflow-providers-databricks/stable/). This operator submits a pipeline run by specifying the pipeline’s identifier inside a `pipeline_task` dictionary. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Requirements

- Apache Airflow version **2.1.0** or later.
- The `apache-airflow-providers-databricks` package version **2.1.0** or later. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Example

The following example creates an Airflow DAG that triggers an update for the pipeline with ID `8279d543-063c-4d63-9926-dae38e35ce8b`:

```python
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
}

with DAG('ldp',
         start_date=days_ago(2),
         schedule_interval="@once",
         default_args=default_args
         ) as dag:

    opr_run_now = DatabricksSubmitRunOperator(
        task_id='run_now',
        databricks_conn_id='CONNECTION_ID',
        pipeline_task={"pipeline_id": "8279d543-063c-4d63-9926-dae38e35ce8b"}
    )
```

Replace `CONNECTION_ID` with the identifier of an Airflow connection to Databricks. Save the file in the `airflow/dags` directory, then use the Airflow UI to view and trigger the DAG. Pipeline update details can be viewed in the Databricks pipeline UI. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – Alternative orchestration method for Databricks pipelines using job tasks.
- [Pipeline task for jobs](/concepts/databricks-pipeline-task-for-jobs.md) – How to include a pipeline in a Databricks job.
- Orchestrate Lakeflow Jobs with Apache Airflow – General guide for using Airflow with Databricks.
- Azure Data Factory – Another orchestration option for Databricks pipelines.
- DatabricksSubmitRunOperator – The specific Airflow operator used for pipeline submissions.

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
