---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c50659e0a9c75736b960cfcc250928cb8fcaf93d1419b432f7431a5a987e7d1
  pageDirectory: concepts
  sources:
    - use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - dbt-task-artifact-and-output-retrieval
    - Output Retrieval and dbt Task Artifact
    - DTAAOR
  citations:
    - file: use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md
    - file: use-dbttransformations-in-lakeflow-jobs-databricks-on-aws.md
title: dbt Task Artifact and Output Retrieval
description: Retrieving dbt task output, inline logs, and archived artifacts (logs, results, manifests, configuration) programmatically via the Databricks CLI or Jobs API.
tags:
  - dbt
  - databricks-jobs
  - artifacts
  - api
timestamp: "2026-06-19T23:21:16.537Z"
---

# dbt Task Artifact and Output Retrieval

**dbt Task Artifact and Output Retrieval** refers to the methods for programmatically accessing the output and archived files produced by a dbt task that runs as part of a [Lakeflow Jobs](/concepts/lakeflow-jobs.md) on Databricks. After a dbt task completes, the system automatically archives artifacts including logs, results, manifests, and configuration, and makes them available through the Databricks CLI or the Jobs REST API. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

## Retrieval Methods

### Databricks CLI

Use the `databricks jobs get-run-output` command, passing the dbt task's individual run ID and requesting JSON output. The response includes inline logs and a download link for the archived artifacts. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

```bash
databricks jobs get-run-output <task_run_id> --output JSON
```

### Jobs API

Send a `GET` request to the `runs/get-output` endpoint with the dbt task's run ID as a query parameter. ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

```
GET /api/2.0/jobs/runs/get-output?run_id=<task_run_id>
```

## Important Notes

- For multi-task jobs, you **must** use the individual dbt task run ID, not the parent job run ID. Using the parent run ID returns the following error: ^[use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md]

  > Retrieving the output of runs with multiple tasks is not supported. Please retrieve the output of each individual task run instead.

- The output includes both **inline logs** and a **download link** for the archived artifacts. ^[use-dbttransformations-in-lakeflow-jobs-databricks-on-aws.md]

## Related Concepts

- dbt Task – The job task that runs dbt Core commands.
- Databricks CLI – Command-line tool used to retrieve task output.
- Jobs API – REST API for managing and inspecting Databricks jobs.
- [Lakeflow Jobs](/concepts/lakeflow-jobs.md) – The workflow orchestration platform where dbt tasks execute.
- [Databricks Git folders](/concepts/databricks-git-folders-for-cicd.md) – Required repository setup for dbt projects in jobs.
- dbt Artifacts – The automatically archived logs, results, manifests, and configuration files.

## Sources

- use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md

# Citations

1. [use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws.md](/references/use-dbt-transformations-in-lakeflow-jobs-databricks-on-aws-9420061c.md)
2. use-dbttransformations-in-lakeflow-jobs-databricks-on-aws.md
