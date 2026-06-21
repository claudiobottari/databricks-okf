---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 612b2e028c3b9be87a0e7aa469cda1256aa7de045718153baf87447b04aaf246
  pageDirectory: concepts
  sources:
    - human-feedback-in-mlflow-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - human-feedback-for-llm-judge-alignment
    - HFFLJA
    - Human feedback alignment
  citations:
    - file: human-feedback-in-mlflow-databricks-on-aws.md
title: Human Feedback for LLM Judge Alignment
description: Human feedback collected via MLflow can be used to create datasets for LLM judges and scorers, keeping automated evaluation systems aligned with human expert judgment and nuanced business requirements.
tags:
  - mlflow
  - llm-evaluation
  - human-feedback
  - alignment
timestamp: "2026-06-19T19:07:13.119Z"
---

# Human Feedback for LLM Judge Alignment

**Human Feedback for LLM Judge Alignment** refers to the practice of collecting qualitative ratings, comments, and ground‑truth expectations from human annotators and using that data to improve the accuracy and consistency of [LLM Judges](/concepts/llm-judges.md) and automated evaluation scorers. By anchoring automated metrics to human expert judgment, teams can ensure that their evaluation pipelines remain aligned with real‑world quality requirements over time. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Data Model

MLflow stores human feedback as **assessments** attached to individual [[MLflow Trace|MLflow Traces]]. Each assessment is linked to a specific user query and the application’s corresponding outputs and logic. There are two assessment types: ^[human-feedback-in-mlflow-databricks-on-aws.md]

- **Feedback** – evaluates the app’s *actual outputs* or intermediate steps (e.g., “Was the agent’s response good?”). Feedback captures ratings or comments on what the app produced. ^[human-feedback-in-mlflow-databricks-on-aws.md]
- **Expectation** – defines the *desired or correct outcome* (ground truth) that the app *should have produced* (e.g., “the ideal response”). For a given input, the expectation is always the same. ^[human-feedback-in-mlflow-databricks-on-aws.md]

Both assessment types can be attached to the entire trace or to a specific span within it. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Sources of Feedback for Alignment

Human feedback can be collected from three main personas, each serving a different role in the alignment process: ^[human-feedback-in-mlflow-databricks-on-aws.md]

### Developer Feedback

During development, engineers can directly annotate traces to track quality notes and mark specific examples for future reference or regression testing. This lightweight annotation helps flag edge cases and regressions before they reach production. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### Domain Expert Feedback

Subject‑matter experts provide structured feedback on app outputs and define expectations for correct responses. Their detailed evaluations are particularly valuable for aligning LLM judges with nuanced business requirements. MLflow offers two approaches: ^[human-feedback-in-mlflow-databricks-on-aws.md]

- **Interactive testing with Chat UI** – experts interact with the deployed app in real time, providing immediate feedback on responses as they test conversational flows. This is ideal for “vibe checks” and qualitative validation before production deployment. ^[human-feedback-in-mlflow-databricks-on-aws.md]
- **Labeling existing traces** – experts systematically review and label traces already captured from the app, assessing specific examples and defining ground‑truth expectations. This is suited for structured evaluation sessions. ^[human-feedback-in-mlflow-databricks-on-aws.md]

### End‑User Feedback

In production, feedback from live users provides crucial insights into real‑world performance. Identifying problematic queries and highlighting successful interactions helps preserve good behavior during future updates and contributes to ongoing judge alignment. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Role in LLM Judge Alignment

Human feedback complements automated evaluation by providing a ground‑truth signal that can be used to create datasets for LLM judges and scorers. Regularly incorporating human‑labeled examples keeps the evaluation pipeline aligned with expert judgment, preventing drift between automated scores and human quality perception. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Related Concepts

- Automated evaluation harness
- [[MLflow Trace|MLflow Traces]]
- Ground truth data
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- Model monitoring and drift detection

## Sources

- human-feedback-in-mlflow-databricks-on-aws.md

# Citations

1. [human-feedback-in-mlflow-databricks-on-aws.md](/references/human-feedback-in-mlflow-databricks-on-aws-5bbf5fdf.md)
