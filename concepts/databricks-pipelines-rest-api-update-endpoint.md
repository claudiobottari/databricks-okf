---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cbc02d323aae8b12c073b97678f55e12c8925606fa10a5cec70532df1a187522
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-pipelines-rest-api-update-endpoint
    - DPRAUE
    - Databricks Pipelines REST API Get Update Details Endpoint
    - Pipelines REST API updates
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Databricks Pipelines REST API Update Endpoint
description: The REST API endpoint at /api/2.0/pipelines/{pipeline_id}/updates used to trigger pipeline updates programmatically from external orchestrators.
tags:
  - api
  - pipelines
  - rest
timestamp: "2026-06-19T20:17:48.959Z"
---

# Databricks Pipelines REST API Update Endpoint

The **Databricks Pipelines REST API Update Endpoint** is an asynchronous REST API endpoint used to trigger an update of a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md). When called, it starts a pipeline update and returns immediately before the update completes, allowing callers to continue with other tasks while the pipeline runs in the background. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Endpoint Details

The endpoint uses the following URL structure:

```
https://<databricks-instance>/api/2.0/pipelines/<pipeline-id>/updates
```

It requires a **POST** HTTP method. Replace `<databricks-instance>` with your workspace instance URL and `<pipeline-id>` with the unique identifier of the target pipeline. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Authentication

For authentication, include the `Authorization` header with a Bearer token:

```
Authorization: Bearer <personal-access-token>
```

Databricks recommends using OAuth tokens for automated tools and [personal access tokens](/concepts/databricks-personal-access-token-pat-authentication.md) belonging to service principals instead of workspace users for improved security. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Request Body

Pass additional request parameters as a JSON document in the request body. For example, to trigger an update that reprocesses all data:

```json
{"full_refresh": "true"}
```

If there are no additional parameters, use empty braces (`{}`). ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Asynchronous Behavior

The pipeline update request is asynchronous. The API returns immediately after starting the update, before the pipeline finishes execution. This means that downstream tasks that depend on pipeline completion must implement their own polling logic to wait for the update to finish. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Using the Endpoint with Azure Data Factory

The pipeline update endpoint can be called from an Azure Data Factory **Web activity** to include a pipeline as part of a larger data integration workflow. To set this up:

1. Create or open an Azure Data Factory.
2. Add a **Web activity** to your Azure Data Factory pipeline.
3. Configure the activity with:
   - **URL**: The full endpoint URL with your workspace instance and pipeline ID.
   - **Method**: POST.
   - **Headers**: Include `Authorization` with `Bearer <token>`.
   - **Body**: JSON document with parameters (or empty braces).

To test the integration, use the **Debug** button in the Azure Data Factory pipeline toolbar. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

### Polling for Completion

Because the API is asynchronous, tasks dependent on pipeline completion must wait for the update to finish. One approach in Azure Data Factory is to add an **Until activity** following the Web activity that triggers the update:

1. Add a **Wait activity** to pause for a configured number of seconds.
2. Add a **Web activity** after the Wait activity that calls the [Databricks Pipelines REST API Get Update Details Endpoint](/concepts/databricks-pipelines-rest-api-update-endpoint.md) to check the update status. The `state` field in the response indicates whether the update has completed.
3. Use the `state` value to set the terminating condition for the Until activity, optionally with a **Set Variable activity**. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- [Databricks Jobs](/concepts/dbt-task-in-databricks-jobs.md)
- [Pipeline task for jobs](/concepts/databricks-pipeline-task-for-jobs.md)
- Apache Airflow with Databricks
- Azure Data Factory Orchestration
- OAuth tokens
- Service principals

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
