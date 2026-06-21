---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f6f662d85be804d56d5e62803ecd396ae348aa964085cbedf5d5a8f02294661d
  pageDirectory: concepts
  sources:
    - run-pipelines-in-a-workflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - pipeline-update-retry-behavior-in-orchestrated-workflows
    - PURBIOW
  citations:
    - file: run-pipelines-in-a-workflow-databricks-on-aws.md
title: Pipeline Update Retry Behavior in Orchestrated Workflows
description: How retry configurations on both the pipeline level and the orchestrator level interact, potentially causing cascading retries.
tags:
  - workflow-orchestration
  - reliability
  - pipelines
timestamp: "2026-06-19T20:17:34.969Z"
---

---

title: Pipeline Update Retry Behavior in Orchestrated Workflows
summary: How retry configurations interact when a pipeline is triggered from an orchestrator like Azure Data Factory, and the recommended best practices to avoid excessive retry attempts.
sources:
  - run-pipelines-in-a-workflow-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T22:00:00.000Z"
updatedAt: "2026-06-19T22:00:00.000Z"
tags:
  - pipelines
  - retries
  - orchestration
  - azure-data-factory
aliases:
  - pipeline-update-retry-behavior
  - PURBOW
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Pipeline Update Retry Behavior in Orchestrated Workflows

When a [Lakeflow Spark Declarative Pipeline](/concepts/lakeflow-spark-declarative-pipelines.md) is called from an external orchestrator—such as Azure Data Factory—both the pipeline itself and the orchestrator activity can independently define retry policies. Understanding how these two retry layers interact is critical to avoiding unintended behavior, particularly excessive retry attempts on failure. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Retry Multiplication

If retry values are configured on the pipeline **and** on the Azure Data Factory activity that triggers the pipeline, the effective number of retries is the product of the two values. For example:

- A pipeline update fails.
- The pipeline is configured with the default of 5 retries (`pipelines.numUpdateRetryAttempts = 5`).
- The Azure Data Factory activity is configured with 3 retries.

In this scenario, the failing update might be retried up to 5 × 3 = **15 times**. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Configuration

The pipeline retry count can be changed using the `pipelines.numUpdateRetryAttempts` setting when configuring the pipeline. The default value is 5. The Azure Data Factory retry count is set on the activity’s **Retry** property in the Data Factory user interface. ^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Recommendations

To avoid excessive retry attempts when pipeline updates fail, Databricks recommends limiting retries on **either** the pipeline side or the orchestrator side:

- Reduce the pipeline `pipelines.numUpdateRetryAttempts` value below the default of 5.
- Or reduce the Azure Data Factory activity retry count.
- Prefer setting retries in only one layer to keep the multiplication effect predictable.

^[run-pipelines-in-a-workflow-databricks-on-aws.md]

## Related Concepts

- Pipeline configuration settings
- [Lakeflow Spark Declarative Pipelines](/concepts/lakeflow-spark-declarative-pipelines.md)
- Azure Data Factory integration
- Orchestrating pipelines with jobs
- [Pipelines REST API updates](/concepts/databricks-pipelines-rest-api-update-endpoint.md)

## Sources

- run-pipelines-in-a-workflow-databricks-on-aws.md

# Citations

1. [run-pipelines-in-a-workflow-databricks-on-aws.md](/references/run-pipelines-in-a-workflow-databricks-on-aws-0fa705f7.md)
