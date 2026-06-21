---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: cc9233dd0f1ff4e933e84b507c932d62528470fbb92389b1a35e5b0dba6e64ce
  pageDirectory: concepts
  sources:
    - human-feedback-in-mlflow-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-review-app-for-domain-expert-feedback
    - MRAFDEF
    - Collect domain expert feedback
    - Domain Expert Feedback
    - Domain expert feedback
    - collect domain expert feedback
    - domain expert feedback
  citations:
    - file: human-feedback-in-mlflow-databricks-on-aws.md
title: MLflow Review App for Domain Expert Feedback
description: "MLflow's Review App provides two approaches for collecting domain expert feedback: interactive testing with a Chat UI (real-time conversational testing of deployed apps) and labeling existing traces (systematic review of captured traces to assess outputs and define ground truth)."
tags:
  - mlflow
  - human-feedback
  - review-app
  - domain-experts
timestamp: "2026-06-19T19:07:24.212Z"
---

# MLflow Review App for Domain Expert Feedback

The **MLflow Review App for Domain Expert Feedback** is a feature within [MLflow](/concepts/mlflow.md) that enables subject matter experts to provide structured feedback on GenAI application outputs. It provides a purpose-built interface for collecting detailed evaluations from domain experts, helping to align [LLM Judges](/concepts/llm-judges.md) and scorers with nuanced business requirements and define what high-quality responses look like for specific use cases. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Overview

The Review App offers two distinct approaches for collecting domain expert feedback, each tailored to different phases of the GenAI application lifecycle. Both approaches leverage MLflow's underlying [Assessment](/concepts/assessments.md) data model, which stores human feedback as structured evaluations attached to [[MLflow Trace|MLflow Traces]]. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Interactive Testing with Chat UI

Experts can interact with a deployed GenAI application in real-time through a chat interface, providing immediate feedback on responses as they test conversational flows. This approach is ideal for "vibe checks" and qualitative validation before deployment to production. Experts can evaluate the app's actual outputs by providing [Feedback](/concepts/feedback-object.md) assessments — such as ratings and comments — that answer questions like, "Was the agent's response good?" ^[human-feedback-in-mlflow-databricks-on-aws.md]

This interactive testing method allows domain experts to assess what the app produces in real-time, offering qualitative insights during the development and pre-production validation stages. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Labeling Existing Traces

Experts can systematically review and label traces that have already been captured from a deployed application. This approach supports structured evaluation sessions where experts assess specific examples and define ground truth expectations. Experts can provide [Expectation](/concepts/feedback-vs-expectation-labels.md) assessments — defining the desired or correct outcome that the app should have produced — which are useful for creating [Evaluation Datasets](/concepts/evaluation-datasets.md) and keeping LLM judges aligned with human expert judgment. ^[human-feedback-in-mlflow-databricks-on-aws.md]

This method is well-suited for structured review sessions where domain experts evaluate specific examples at scale and establish ground truth for future model iterations. ^[human-feedback-in-mlflow-databricks-on-aws.md]

## Data Model

The Review App uses the same underlying data model as other human feedback collection methods in MLflow. Assessments are attached to individual traces or specific spans within a trace, linking feedback directly to a specific user query and the GenAI application's outputs and logic. The two assessment types used are:

- **Feedback**: Evaluates the app's actual outputs or intermediate steps, providing qualitative insights through ratings and comments.
- **Expectation**: Defines the desired or correct outcome (ground truth) that the app should have produced, remaining constant for a given input.

^[human-feedback-in-mlflow-databricks-on-aws.md]

## Use Cases

The Review App serves several key purposes in the GenAI application lifecycle:

- **Qualitative validation**: Performing "vibe checks" before production deployment through interactive chat testing.
- **Structured evaluation**: Conducting systematic review sessions where domain experts assess specific examples at scale.
- **Ground truth collection**: Establishing what high-quality responses look like for specific use cases, enabling the creation of evaluation datasets.
- **LLM judge alignment**: Keeping automated evaluation systems aligned with human expert judgment by providing reference data.

^[human-feedback-in-mlflow-databricks-on-aws.md]

## Related Concepts

- [Human feedback in MLflow](/concepts/human-feedback-collection-in-mlflow.md) — The broader framework for collecting feedback from developers, domain experts, and end users.
- [[MLflow Trace|MLflow Traces]] — The underlying data structure to which assessments are attached.
- [Automated evaluation (Eval Harness)](/concepts/evaluation-harness.md) — Complementary automated evaluation that the Review App enriches with human judgment.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Created from Expectation assessments for training and validating LLM judges.
- [LLM Judges](/concepts/llm-judges.md) — Automated scoring systems that benefit from domain expert feedback for alignment.
- [Collect end user feedback](/concepts/end-user-feedback-collection-via-sdk.md) — Production feedback collection from live application users.
- Label during development — Developer feedback annotation during the development phase.

## Sources

- human-feedback-in-mlflow-databricks-on-aws.md

# Citations

1. [human-feedback-in-mlflow-databricks-on-aws.md](/references/human-feedback-in-mlflow-databricks-on-aws-5bbf5fdf.md)
