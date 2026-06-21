---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e5a501d004ec654ce3909a5c276fd2b288be012acbd2bc3e917bac4c8e02aed6
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessments-mlflow-genai
    - A(G
    - Assessment (MLflow GenAI)
    - Assessment (MLflow)
    - Assessments (MLflow)
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Assessments (MLflow GenAI)
description: Quality measurements and ground truth labels attached to traces, divided into feedback (judgments) and expectations (ground truth).
tags:
  - mlflow
  - evaluation
  - quality
timestamp: "2026-06-18T14:41:34.006Z"
---

# Assessments (MLflow GenAI)

**Assessments** are quality measurements and ground truth labels that are attached to a trace in the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) data model. They represent the core mechanism for capturing evaluation results, user feedback, and expert judgments about the quality of a generative AI application's outputs. ^[concepts-data-model-databricks-on-aws.md]

## Overview

In MLflow's GenAI data model, every trace — the complete execution log of a generative AI application — can have one or more assessments attached to it. Assessments serve as the bridge between raw execution data and quality insights, enabling developers to measure, track, and improve application performance over time. ^[concepts-data-model-databricks-on-aws.md]

Assessments are created through multiple channels:

- **Automated evaluation**: [[Scorers]] and [LLM Judges](/concepts/llm-judges.md) generate assessments when evaluating traces during development or production monitoring.
- **End-user feedback**: Users of the deployed application can provide ratings or comments that become assessments.
- **Domain expert labeling**: Subject matter experts working through [Labeling Sessions](/concepts/labeling-sessions.md) in the [review app](/concepts/mlflow-review-app.md) contribute assessments based on [Labeling Schemas](/concepts/labeling-schemas.md).

## Types of Assessments

Assessments fall into two distinct categories: feedback and expectations. ^[concepts-data-model-databricks-on-aws.md]

### Feedback

Feedback refers to judgments about the quality of an application's outputs. It is added by end users, domain experts, or automated scorers and is used to identify quality issues. Feedback includes both human-provided judgments (such as thumbs up or thumbs down ratings) and automated evaluations (such as an LLM judge's assessment of a response's correctness). ^[concepts-data-model-databricks-on-aws.md]

### Expectations

Expectations are ground truth labels that define the correct output for a given input. They are added by domain experts and serve as a "gold standard" for evaluating whether the application produced the right response. Examples include the expected answer to a question or the required facts that must be present in a response. ^[concepts-data-model-databricks-on-aws.md]

Note that ground truth labels (expectations) are not required to measure quality with MLflow. Most applications will not have ground truth labels or will have only a small set. ^[concepts-data-model-databricks-on-aws.md]

## How Assessments Are Created

### Through Evaluation

When using [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) to systematically test an application version against an evaluation dataset, the evaluation harness runs each [[Scorers|scorer]] on the resulting traces. Each scorer produces feedback assessments that are automatically attached to the corresponding trace. ^[concepts-data-model-databricks-on-aws.md]

### Through Production Monitoring

Production monitoring with mlflow.genai.Scorer.start() schedules scorers to automatically evaluate traces from a deployed application. The production monitoring service runs the scorers on production traces, creating feedback assessments and attaching each feedback to the source trace. ^[concepts-data-model-databricks-on-aws.md]

### Through Human Labeling

Domain experts can create assessments through [Labeling Sessions](/concepts/labeling-sessions.md), which organize traces for human review. The review app presents traces from labeling sessions and collects assessments based on [Labeling Schemas](/concepts/labeling-schemas.md) that define what questions to ask and what valid responses are expected. ^[concepts-data-model-databricks-on-aws.md]

### Through Direct API Calls

Developers can programmatically log assessments using the assessment logging API, which allows attaching feedback and expectations directly to traces without going through the evaluation pipeline. ^[concepts-data-model-databricks-on-aws.md]

## Role in the Data Model

Assessments are a key component of the [MLflow GenAI Data Model](/concepts/mlflow-genai-data-model.md), connecting traces to quality insights:

- [Traces](/concepts/traces.md) capture the complete execution of a GenAI application.
- Assessments attached to traces contain quality feedback and ground truth expectations.
- [Evaluation Runs](/concepts/evaluation-runs.md) contain traces and their assessments, along with aggregated metrics based on those assessments.

This structure enables developers to trace the provenance of quality measurements back to specific application executions, scorers, and evaluators. ^[concepts-data-model-databricks-on-aws.md]

## Best Practices

- **Use automated scorers for consistent, scalable quality measurement.** Scorers can evaluate both development and production traces, providing continuous quality monitoring.
- **Collect ground truth expectations for critical use cases.** While not required, expectations provide a gold standard for validating changes and preventing regressions.
- **Leverage domain experts for complex assessments.** Human judgments remain valuable for evaluating nuanced or ambiguous outputs that automated scorers may struggle with.
- **Combine multiple assessment sources.** Correlating feedback from scorers, end users, and domain experts provides a more complete picture of application quality.

## Related Concepts

- [Traces](/concepts/traces.md) — The execution logs that assessments are attached to
- [[Scorers]] — Functions that evaluate trace quality to create feedback assessments
- [LLM Judges](/concepts/llm-judges.md) — LLM-based evaluation criteria used by scorers
- [Labeling Sessions](/concepts/labeling-sessions.md) — Queues of traces organized for human expert review
- [Labeling Schemas](/concepts/labeling-schemas.md) — Structured questions that define what assessments to collect
- Review app — Web UI where domain experts label traces with assessments
- [MLflow GenAI Data Model](/concepts/mlflow-genai-data-model.md) — The overall framework for organizing GenAI application data

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
