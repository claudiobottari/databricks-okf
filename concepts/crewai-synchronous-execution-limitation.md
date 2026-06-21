---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f15d71f6ca972b8ce332280cf5b703aa4e49415e7e8795a844dfc228cea6cff5
  pageDirectory: concepts
  sources:
    - tracing-crewai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - crewai-synchronous-execution-limitation
    - CSEL
  citations:
    - file: tracing-crewai-databricks-on-aws.md
title: CrewAI Synchronous Execution Limitation
description: MLflow CrewAI integration only supports synchronous task execution; async tasks and kickoff are not traced
tags:
  - crewai
  - tracing
  - limitation
  - mlflow
timestamp: "2026-06-19T23:11:04.284Z"
---

# CrewAI Synchronous Execution Limitation

The **CrewAI Synchronous Execution Limitation** is a current restriction in the [MLflow](/concepts/mlflow.md) CrewAI integration that limits tracing support to only synchronous task execution within CrewAI workflows. Asynchronous task execution and asynchronous kickoff operations are not supported as of the current [MLflow](/concepts/mlflow.md) version. ^[tracing-crewai-databricks-on-aws.md]

## Overview

When using `mlflow.crewai.autolog()` to enable [Automatic Tracing](/concepts/automatic-tracing.md) for CrewAI, [MLflow](/concepts/mlflow.md) captures detailed [Traces](/concepts/traces.md) of agent operations, including task execution, LLM calls, memory operations, and latency. However, this tracing capability is limited to workflows that execute tasks synchronously. Asynchronous execution patterns are not captured by the current integration. ^[tracing-crewai-databricks-on-aws.md]

## Affected Operations

The following asynchronous operations are not supported:

- **Asynchronous task execution** – Tasks dispatched to run concurrently without blocking
- **Asynchronous kickoff** – The `crew.kickoff()` method when called asynchronously

These operations will not produce trace data in the [MLflow Experiment](/concepts/mlflow-experiment.md) when auto-tracing is enabled. ^[tracing-crewai-databricks-on-aws.md]

## Workaround

To ensure full trace coverage, use only synchronous task execution patterns in your CrewAI workflows. This involves calling `crew.kickoff()` in a blocking manner rather than using concurrent or asynchronous task dispatching mechanisms. ^[tracing-crewai-databricks-on-aws.md]

## Impact on Tracing

Because asynchronous operations are not traced, any LLM calls, memory load and write operations, or exception handling that occur during asynchronous execution will not be captured in [MLflow](/concepts/mlflow.md) [Traces](/concepts/traces.md). This limitation affects the completeness of [MLflow Tracing](/concepts/mlflow-tracing.md) for CrewAI applications that rely on asynchronous execution patterns. ^[tracing-crewai-databricks-on-aws.md]

## Related Concepts

- MLflow CrewAI Integration – The broader tracing framework for CrewAI agents
- Synchronous Task Execution – The supported execution pattern for tracing
- [Asynchronous Task Execution](/concepts/asynchronous-iceberg-metadata-generation.md) – The unsupported pattern
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md) – A workload type that may be affected by this limitation
- Production Monitoring with MLflow – Scheduled scoring workflows that use synchronous execution

## Sources

- tracing-crewai-databricks-on-aws.md

# Citations

1. [tracing-crewai-databricks-on-aws.md](/references/tracing-crewai-databricks-on-aws-c9f44377.md)
