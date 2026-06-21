---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: fb8a925f12f2764cf728b8f170adf703aff9add5b35e56f35f84265218da8de0
  pageDirectory: concepts
  sources:
    - human-feedback-in-mlflow-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-human-feedback-assessments
    - MHFA
    - feedback assessments
  citations:
    - file: human-feedback-in-mlflow-databricks-on-aws.md
title: MLflow Human Feedback Assessments
description: MLflow stores human feedback as Assessments — structured objects (Feedback or Expectation types) attached to individual MLflow Traces or spans within a trace, enabling collection of ratings, comments, and ground-truth expectations from developers, domain experts, and end users.
tags:
  - mlflow
  - human-feedback
  - data-model
  - generative-ai
timestamp: "2026-06-19T19:07:43.656Z"
---

# MLflow Human Feedback Assessments

**MLflow Human Feedback Assessments** is a mechanism within MLflow that captures human-generated evaluations — including ratings, comments, and ground-truth expectations — and attaches them as assessments to traces produced by a GenAI application. This allows developers, domain experts, and end users to provide qualitative and quantitative feedback that complements [Automated Evaluation](/concepts/automated-evaluation-and-monitoring.md) tools. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Overview

Human feedback is captured as assessments that are linked to individual [[MLflow Trace|MLflow Traces]]. This design connects each piece of feedback directly to a specific user query and the app's corresponding outputs and logic. The collected assessments can be used to create datasets for LLM judges and scorers, and to keep automated evaluation aligned with human expert judgment. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Assessment Types

There are two types of assessments in the MLflow human feedback data model: ^[human-feedback-in-mlflow-databricks-on-aws.md]

- **Feedback**: Evaluates the app's *actual outputs* or intermediate steps. It answers questions such as "Was the agent's response good?" Feedback assesses what the app produced — for example, ratings or comments — and provides qualitative insights about the generated output. ^[human-feedback-in-mlflow-databricks-on-aws.md]

- **Expectation**: Defines the *desired or correct outcome* (ground truth) that the app *should have produced*. For a given input, the expectation is always the same. Expectations define what the app should generate and are useful for creating [Evaluation Datasets](/concepts/evaluation-datasets.md). ^[human-feedback-in-mlflow-databricks-on-aws.md]

Assessments can be attached to the entire trace or to a specific span within the trace. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Feedback Sources

MLflow supports collecting human feedback from three main personas, each suited to a different phase of the GenAI application lifecycle. While the sources differ, the underlying data model remains the same across all personas. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### Developer Feedback

During development, developers can directly annotate traces. This is useful for tracking quality notes during the build process and marking specific examples for future reference or regression testing. For more information, see Label During Development.

^[human-feedback-in-mlflow-databricks-on-aws.md]

### Domain Expert Feedback

Subject matter experts can provide structured feedback on the app's outputs and define expectations for correct responses. Their detailed evaluations help define what high-quality responses look like for a specific use case and are valuable for aligning LLM judges with nuanced business requirements. ^[human-feedback-in-mlflow-databricks-on-aws.md]

MLflow provides two approaches for collecting domain expert feedback using the [Review App](/concepts/mlflow-review-app.md):

- **Interactive testing with Chat UI**: Experts interact with the deployed app in real-time through a chat interface, providing immediate feedback on responses as they test conversational flows. This approach is ideal for "vibe checks" and qualitative validation before production deployment. For more information, see Test an App Version with the Chat UI. ^[human-feedback-in-mlflow-databricks-on-aws.md]

- **Labeling existing traces**: Experts systematically review and label traces that have already been captured from the app. This approach is ideal for structured evaluation sessions where experts assess specific examples and define ground-truth expectations. For more information, see Label Existing Traces. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### End-User Feedback

In production, feedback can be captured from users interacting with the live application. This provides insights into real-world performance, helping to identify problematic queries that need fixing and highlighting successful interactions to preserve during future updates. MLflow provides tools to capture, store, and analyze feedback directly from users of deployed applications. For more information, see [Collect End-User Feedback](/concepts/end-user-feedback-collection-via-sdk.md). ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Use Cases

Collected human feedback assessments serve several purposes: ^[human-feedback-in-mlflow-databricks-on-aws.md]

- Creating datasets for [LLM Judges](/concepts/llm-judges.md) and scorers
- Keeping automated evaluation systems aligned with human expert judgment
- Tracking quality notes during development
- Marking specific examples for regression testing
- Identifying problematic queries in production
- Preserving successful interactions during app updates

## Related Concepts

- [[MLflow Trace|MLflow Traces]]
- [Automated Evaluation](/concepts/automated-evaluation-and-monitoring.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [Review App](/concepts/mlflow-review-app.md)
- [LLM Judges](/concepts/llm-judges.md)
- Label During Development
- Label Existing Traces
- Test an App Version with the Chat UI
- [Collect End-User Feedback](/concepts/end-user-feedback-collection-via-sdk.md)

## Sources

- human-feedback-in-mlflow-databricks-on-aws.md

# Citations

1. [human-feedback-in-mlflow-databricks-on-aws.md](/references/human-feedback-in-mlflow-databricks-on-aws-5bbf5fdf.md)
