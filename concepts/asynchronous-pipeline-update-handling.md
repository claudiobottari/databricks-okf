---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 68a5a1deb9f42399ecaa6b99dcf1fa40a20b982d4142584f23401033787173ed
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - asynchronous-pipeline-update-handling
    - APUH
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Asynchronous Pipeline Update Handling
description: Managing downstream task dependencies when pipeline update requests return asynchronously, requiring polling or until-loops to wait for completion.
tags:
  - workflow-orchestration
  - async-patterns
  - pipelines
timestamp: "2026-06-19T20:18:01.342Z"
---

# Asynchronous Pipeline Update Handling

**Asynchronous Pipeline Update Handling** refers to the pattern of triggering a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md) update via an API call that returns immediately after starting the update, without waiting for the update to complete. This design enables decoupling between the caller and the pipeline execution, but requires explicit monitoring logic when downstream tasks depend on the pipeline finishing.

## Overview

When a pipeline update is submitted through the REST API (e.g., `POST /api/2.0/pipelines/<pipeline-id>/updates`), the response is returned as soon as the update is accepted, not after the update finishes. The returned payload includes a `update_id` and a `state` field indicating the initial status (e.g., `CREATED`), but the actual data processing runs asynchronously. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

This asynchronous behavior is typical of long-running batch workloads. It means that any task or activity in a workflow that depends on the pipeline update's successful completion must explicitly poll the update status before proceeding. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Handling in Azure Data Factory

A common orchestration scenario is triggering a pipeline update from an Azure Data Factory Web activity and then waiting for the update to finish before running subsequent activities. Because the initial Web activity only confirms that the update was started, a wait-and-poll loop is needed. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

The recommended pattern in Azure Data Factory is to use an Until activity that contains:

1. A Wait activity that pauses for a configurable number of seconds (e.g., 30 seconds) to allow the pipeline to progress.
2. A second Web activity that calls the pipeline update details endpoint (`GET /api/2.0/pipelines/<pipeline-id>/updates/<update-id>`) to retrieve the current `state`.
3. A terminating condition for the Until activity that checks whether the `state` field from the response indicates a terminal status (e.g., `COMPLETED`, `FAILED`, `CANCELED`).

Optionally, a Set Variable activity can be used to store the state value in a pipeline variable and then reference that variable in the Until condition. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Example Sequence

1. **Trigger Web activity**: `POST /api/2.0/pipelines/{pipeline-id}/updates` with an empty body `{}` or `{"full_refresh": "true"}`.
2. **Until activity** (condition: `@equals(pipeline().variables.state, 'COMPLETED')` or similar):
   - **Wait activity** (duration: e.g., `00:01:00`).
   - **Status Web activity**: `GET /api/2.0/pipelines/{pipeline-id}/updates/{update-id}`.
   - **Set Variable activity**: Set `state` variable to the response `state` field.
3. Downstream activities run only after the Until loop exits (i.e., the pipeline update has finished).

Using this pattern ensures that the rest of the workflow executes after the pipeline update has reached a terminal state, not immediately after the update was submitted. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- [Pipeline task for jobs](/concepts/databricks-pipeline-task-for-jobs.md) – How to run a pipeline synchronously inside a Databricks job.
- Apache Airflow – Alternative orchestration tool that can also trigger pipeline updates (asynchronous by default, but operators handle polling).
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md) – The underlying pipeline technology.
- Web activity – Azure Data Factory activity used to make HTTP requests.
- Until activity – Azure Data Factory control flow activity for polling loops.
- Wait activity – Used to introduce a delay between poll iterations.

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
