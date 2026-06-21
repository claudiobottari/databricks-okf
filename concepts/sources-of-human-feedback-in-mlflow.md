---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2ed68a1a777bfffcf8935739b628eaffa0b6702678e52cef04a8a561fb328fa4
  pageDirectory: concepts
  sources:
    - human-feedback-in-mlflow-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - sources-of-human-feedback-in-mlflow
    - SOHFIM
  citations:
    - file: human-feedback-in-mlflow-databricks-on-aws.md
title: Sources of Human Feedback in MLflow
description: MLflow collects human feedback from three distinct sources — developers (during development via direct trace annotation), domain experts (via Review App with Chat UI or labeling existing traces), and end users (in production from live applications).
tags:
  - mlflow
  - human-feedback
  - workflows
  - generative-ai
timestamp: "2026-06-19T19:07:07.418Z"
---

# Sources of Human Feedback in MLflow

MLflow captures human feedback as assessments attached to your GenAI app’s traces, enabling you to collect ratings, comments, and ground‑truth expectations from developers, domain experts, and end users. This feedback complements automated evaluation and helps create datasets for LLM judges and scorers while keeping them aligned with human expert judgment. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Data Model Overview

Human feedback is stored as **Assessments** attached to individual [[MLflow Trace|MLflow Traces]]. There are two assessment types: **Feedback**, which evaluates the app’s actual outputs (e.g., “Was the agent’s response good?”), and **Expectation**, which defines the desired or correct outcome (ground truth) that the app *should have produced*. Assessments can be attached to the entire trace or to a specific span within it. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## How Feedback Is Collected

MLflow collects feedback from three main sources, each tailored for a different stage of the GenAI app lifecycle. Although the personas differ, the underlying data model is the same for all sources. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### Developer Feedback

During development, you can directly annotate traces to track quality notes and mark specific examples for future reference or regression testing. This is useful for quick manual checks as you build and iterate on the app. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### Domain Expert Feedback

Subject matter experts provide structured feedback on the app’s outputs and define expectations for correct responses. MLflow offers two approaches for collecting domain expert feedback using the Review App:

- **Interactive testing with Chat UI**: Experts interact with the deployed app in real time through a chat interface, providing immediate feedback on responses as they test conversational flows. This is ideal for “vibe checks” and qualitative validation before production deployment.
- **Labeling existing traces**: Experts systematically review and label traces that have already been captured from the app. This is suited for structured evaluation sessions where experts assess specific examples and define ground truth expectations.

Domain expert evaluations are invaluable for aligning LLM judges with nuanced business requirements. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### End‑User Feedback

In production, feedback is captured directly from users interacting with the live application. This provides crucial insights into real‑world performance, helping identify problematic queries that need fixing and highlighting successful interactions to preserve during future updates. MLflow provides tools to capture, store, and analyze feedback from the users of deployed applications. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] – The data structure to which assessments are attached.
- [Automated Evaluation](/concepts/automated-evaluation-and-monitoring.md) – The automated counterpart of human feedback.
- [LLM Judges and Scorers](/concepts/llm-judges-and-scorers.md) – Evaluators that can be trained or aligned using human feedback.
- [Review App](/concepts/mlflow-review-app.md) – The interface used for domain expert feedback collection.
- Chat UI – The interactive interface for live testing of deployed apps.

## Sources

- human-feedback-in-mlflow-databricks-on-aws.md

# Citations

1. [human-feedback-in-mlflow-databricks-on-aws.md](/references/human-feedback-in-mlflow-databricks-on-aws-5bbf5fdf.md)
