---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0de787b1e6ec1747dfa4c454b05c25be512d49f976e444d2fe5ef8502ea641d4
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-3-for-genai
    - DM3FG
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: Databricks MLflow 3 for GenAI
description: Databricks' MLflow 3 platform tailored for Generative AI development, providing tracing, evaluation with LLM-as-a-judge, human feedback collection, and production monitoring capabilities.
tags:
  - databricks
  - mlflow
  - genai
  - platform
timestamp: "2026-06-19T10:44:26.231Z"
---

# Databricks MLflow 3 for GenAI

**Databricks MLflow 3 for GenAI** is the latest major version of MLflow that provides a unified platform for tracing, evaluating, and collecting human feedback on GenAI applications. It offers integrated tooling for developing and monitoring large language model (LLM)-based agents and applications, with deep integration into the Databricks environment. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Environment Setup

To get started, install the required packages:
- `mlflow[databricks]` version 3.1.0 or later, which includes the latest GenAI-specific features.
- `databricks-openai`, an OpenAI-compatible client for calling Databricks-hosted foundation model endpoints.

After installation, you create or connect to an MLflow experiment. If using a Databricks notebook, a default notebook experiment is automatically created. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Tracing

MLflow 3 introduces **Tracing**, which records LLM requests, responses, and metrics (e.g., input/output token counts) for every call made by the application. Tracing is enabled by calling `mlflow.<library>.autolog()` — for example, `mlflow.openai.autolog()` automatically instruments the OpenAI client. Individual functions can be organized with the `@mlflow.trace` decorator, which creates structured trace spans. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

The trace visualization shows the full call stack, including nested spans for more complex agents. [MLflow Tracing](/concepts/mlflow-tracing.md) integrates with more than 20 SDKs, including Anthropic, LangGraph, and others. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Evaluation

MLflow Evaluation uses **scorers** to automatically judge the quality of outputs against defined criteria. Scorers fall into two categories:
- **Built-in LLM-as-a-judge scorers**, such as `Safety`.
- **Custom LLM-as-a-judge scorers**, such as `Guidelines`, which allow you to specify free‑text quality guidelines.

Custom code-based scorers are also supported. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

To run an evaluation, you provide an evaluation dataset (a list of input records), a prediction function (the GenAI application), and a list of scorers. The `mlflow.genai.evaluate()` function executes the application on the dataset and then runs the scorers to produce metrics, which are logged to the active MLflow experiment. Results can be reviewed in the MLflow Experiment UI under the **Evaluations** tab. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Human Feedback

MLflow 3 provides a **Review App** for collecting feedback from domain experts. You define a **label schema** that specifies what feedback to collect (e.g., categorical ratings like "Very funny", "Slightly funny", "Not funny"). Using the `mlflow.genai.labeling` API, you create a labeling session, add traces, and share a link with reviewers. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

Reviewers interact with the Review App to rate traces. Feedback can be viewed in the MLflow UI under the **Labeling** tab. Programmatically, you can retrieve feedback by searching traces with `mlflow.search_traces()` or log user feedback within an application using `mlflow.log_feedback()`. ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Next Steps

After instrumenting an application with tracing, evaluation, and human feedback, you can prepare for production monitoring by deploying the same scorers on live traffic. Further topics include exploring [MLflow Tracing](/concepts/mlflow-tracing.md) integrations, building [MLflow Evaluation Datasets](/concepts/evaluation-datasets.md), and collecting [user feedback](/concepts/multi-dimensional-user-feedback.md). ^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [LLM-as-a-Judge](/concepts/llm-as-a-judge.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Review App](/concepts/mlflow-review-app.md)
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- [[Scorers]]
- [Labeling Session](/concepts/labeling-session.md)

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
