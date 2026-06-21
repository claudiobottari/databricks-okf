---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dae8fc2c2e211a9bc90a70e09cb5b0e69aaa01988ee43e2b9e639771cefde3ea
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-trace
    - MGT
    - GenAI Trace
    - GenAI trace
    - GenAI traces
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: MLflow GenAI Trace
description: A record of the complete execution of a GenAI application, capturing inputs, outputs, and every intermediate step such as LLM calls, retrievals, and tool use.
tags:
  - mlflow
  - observability
  - tracing
timestamp: "2026-06-18T11:05:21.352Z"
---

# MLflow GenAI Trace

**MLflow GenAI Traces** capture the complete execution of a generative AI (GenAI) application, recording inputs, outputs, and every intermediate step — including LLM calls, retrievals, tool use, and other operations. Traces are the core observability primitive in the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) data model and are created automatically for every execution of a traced application, both in development and production. ^[concepts-data-model-databricks-on-aws.md]

## Overview

A trace is an execution log that records the full path of a single request through a GenAI system. Unlike traditional MLflow logging, which captures only final model inputs and outputs, GenAI traces preserve the multi-step, agentic nature of modern LLM applications: they record every LLM call, retrieval from a vector store, tool invocation, and any other intermediate step that the application performs. ^[concepts-data-model-databricks-on-aws.md]

Traces are associated with [Assessments](/concepts/assessments.md) that capture quality feedback — either from automated scorers, end users, or domain experts — and may also carry ground-truth expectations. Each trace can optionally be linked to the specific [application version](/concepts/mlflow-application-versioning.md) that generated it, enabling side-by-side quality comparisons across iterations. ^[concepts-data-model-databricks-on-aws.md]

## Use Cases

Traces serve several purposes in the GenAI development lifecycle:

- **Debugging and observability:** Developers inspect traces to understand app behavior, diagnose latency issues, and identify problematic retrieval or reasoning paths. ^[concepts-data-model-databricks-on-aws.md]
- **Quality evaluation:** Traces are evaluated offline against [Evaluation Datasets](/concepts/evaluation-datasets.md) using [[scorers]] (including [LLM Judges](/concepts/llm-judges.md)), producing quality assessments that feed into [Evaluation Runs](/concepts/evaluation-runs.md). ^[concepts-data-model-databricks-on-aws.md]
- **Production monitoring:** Registered scorers can be scheduled to automatically evaluate production traces, producing feedback assessments that attach to the source trace. ^[concepts-data-model-databricks-on-aws.md]
- **Creating evaluation datasets:** Representative traces from production can be selected to build curated test suites for iterative quality improvement. ^[concepts-data-model-databricks-on-aws.md]
- **Human labeling:** Traces can be queued into [Labeling Sessions](/concepts/labeling-sessions.md) for review by domain experts using [Labeling Schemas](/concepts/labeling-schemas.md) that structure the assessment questions. ^[concepts-data-model-databricks-on-aws.md]

## Relationship to Other Entities

Every trace belongs to an [experiment](/concepts/mlflow-experiment.md), which is the named container for all data related to a single GenAI application. Traces are linked to:

- [Assessments](/concepts/assessments.md) — quality measurements and ground truth labels attached to the trace.
- [Logged Models](/concepts/logged-models.md) — snapshots of the application version that produced the trace.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — traces from production can be sampled to build these test suites.
- [Prompts](/concepts/prompt-versioning.md) — the version-controlled prompt templates used during trace generation.

Traces are the only required entity in the MLflow GenAI data model. All other concepts — evaluation runs, labeling sessions, app versions — are optional but recommended. ^[concepts-data-model-databricks-on-aws.md]

## Creating Traces

Traces are created automatically when you instrument your application with [MLflow Tracing](/concepts/mlflow-tracing.md). The SDK integrates with popular frameworks and can be added to custom code. Traces are generated for every invocation of the application in both development (when running locally or in notebooks) and production (when deployed as a model serving endpoint).

To instrument an application, follow the [instrument your app](/concepts/mlflow-instrumentation-guidance.md) guide.

## Trace Contents

A typical trace contains:

- **Request:** The input provided to the application (e.g., a user query).
- **Response:** The final output produced by the application.
- **Intermediate steps:** Each LLM call, retrieval operation, tool invocation, or other action, along with the inputs and outputs of each step.
- **Metadata:** Timing information, token counts, model names, and other execution details.
- **Assessments:** Feedback and expectations attached to the trace by scorers, users, or labelers.

## Viewing Traces

Traces can be viewed in the [MLflow Experiment UI](/concepts/mlflow-experiment.md), which provides search, filtering, and visual inspection of trace contents. The UI also shows attached assessments and links to related application versions and evaluation runs.

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The overall framework for GenAI application development
- [Assessments (MLflow)](/concepts/assessments.md) — Quality measurements attached to traces
- [[Scorers]] — Functions that evaluate trace quality and produce assessments
- [LLM Judges](/concepts/llm-judges.md) — Evaluation criteria that assess text quality
- [Evaluation Harness](/concepts/evaluation-harness.md) — The SDK for systematic quality evaluation
- Production Quality Monitoring — Scheduled evaluation of production traces
- [Labeling Sessions](/concepts/labeling-sessions.md) — Queues of traces for human review
- Experiment (MLflow) — The container for all GenAI application data

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
