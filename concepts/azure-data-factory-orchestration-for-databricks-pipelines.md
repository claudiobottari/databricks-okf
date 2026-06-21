---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 87b266af4d8b5a921c34d7d7d55d9a7768288a94b77fa5f6d5d3eb059db8b2ab
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - azure-data-factory-orchestration-for-databricks-pipelines
    - ADFOFDP
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Azure Data Factory Orchestration for Databricks Pipelines
description: Running pipeline updates from Azure Data Factory using Web activities that call the Databricks Pipelines REST API endpoint.
tags:
  - workflow-orchestration
  - azure-data-factory
  - pipelines
timestamp: "2026-06-19T20:17:37.303Z"
---

# Azure Data Factory Orchestration for Databricks Pipelines

**Azure Data Factory Orchestration for Databricks Pipelines** refers to the integration pattern where Azure Data Factory (ADF) is used to trigger and manage updates to [Databricks Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) as part of a broader cloud-based ETL or data transformation workflow. This approach enables organizations to combine Azure's native orchestration services with Databricks' data processing capabilities.

## Overview

Azure Data Factory is a cloud-based ETL service that supports running Databricks tasks in a workflow, including notebooks, JAR tasks, and Python scripts. To include a [Databricks pipeline](/concepts/databricks-pipeline-task-for-jobs.md) in an ADF workflow, users call the pipeline REST API from an Azure Data Factory Web Activity. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Triggering a Pipeline Update

To trigger a pipeline update from Azure Data Factory:

1. **Create or open a data factory** in the Azure portal.
2. **Open Azure Data Factory Studio** and create a new pipeline by selecting **Pipeline** from the **New** drop-down menu.
3. **Add a Web activity** by dragging it from the **Activities** toolbox (under **General**) to the pipeline canvas.
4. **Configure the Web activity** on the **Settings** tab with the following values:

   - **URL**: `https://<databricks-instance>/api/2.0/pipelines/<pipeline-id>/updates`
     - Replace `<databricks-instance>` with your workspace instance name.
     - Replace `<pipeline-id>` with the identifier of your Databricks pipeline.
   - **Method**: Select **POST**.
   - **Headers**: Add a new header with name `Authorization` and value `Bearer <personal-access-token>`.
   - **Body**: Enter a JSON document with request parameters (e.g., `{"full_refresh": "true"}` to reprocess all data) or empty braces (`{}`) if no additional parameters are needed.

^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Authentication

As a security best practice, Databricks recommends using OAuth tokens instead of personal access tokens when authenticating with automated tools. If using personal access token authentication, Databricks recommends using tokens belonging to service principals rather than individual workspace users. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Testing the Integration

To test the Web activity, click **Debug** on the pipeline toolbar in the Azure Data Factory Studio. The output and status of the run, including any errors, are displayed in the **Output** tab. Use the Databricks pipelines UI to view the details of the triggered pipeline update. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Handling Asynchronous Updates

The pipeline `updates` request is **asynchronous** — it returns immediately after starting the update but before the update completes. If downstream tasks in your ADF pipeline depend on the pipeline update finishing, you must add logic to wait for completion. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Polling for Completion with an Until Activity

A recommended approach is to add an Until Activity following the Web activity that triggers the pipeline update:

1. **Add a Wait activity** to pause for a configured number of seconds while the update completes.
2. **Add a second Web activity** after the Wait activity that calls the pipeline update details endpoint to get the current status. The `state` field in the response indicates whether the update has completed.
3. **Use the `state` value** to set the terminating condition for the Until activity. You can also use a Set Variable Activity to store the `state` value in a pipeline variable and reference that variable in the terminating condition.

^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Retry Configuration Considerations

Lakeflow Spark Declarative Pipelines and Azure Data Factory each include options to configure the number of retries when a failure occurs. If retry values are configured on both the pipeline and the ADF activity that calls it, the effective number of retries is the **ADF retry value multiplied by the pipeline retry value**. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Example

If a pipeline update fails, Lakeflow Spark Declarative Pipelines retries the update up to **five times** by default. If the Azure Data Factory retry is set to **three**, and your pipeline uses the default of five retries, a failing pipeline might be retried up to **fifteen times**. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Recommendation

To avoid excessive retry attempts when pipeline updates fail, Databricks recommends limiting the number of retries when configuring either the pipeline or the Azure Data Factory activity. To change the retry configuration for your pipeline, use the `pipelines.numUpdateRetryAttempts` setting. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- [Orchestrate Databricks Pipelines with Jobs](/concepts/databricks-pipeline-task-for-jobs.md) — Using Databricks Jobs for pipeline orchestration
- [Orchestrate Databricks Pipelines with Apache Airflow](/concepts/apache-airflow-orchestration-for-databricks-pipelines.md) — An alternative orchestration approach
- [Databricks REST API](/concepts/databricks-mlflow-rest-api-20.md) — The API used to trigger pipeline updates
- Pipeline Tasks in Databricks Jobs — Running pipelines as tasks in a job workflow
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) — The pipeline type supported by this integration
- Service Principals — Recommended identity for automated authentication

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
