---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5d2e0eedaca78596c5530a34eb5d098696abb58284c66110697ccc27538fe5d2
  pageDirectory: concepts
  sources:
    - get-started-with-mlflow-3-for-models-databricks-on-aws.md
    - mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-3-for-genai
    - M3FG
    - MLflow 3 GenAI
    - MLflow GenAI
    - MLflow for GenAI
  citations:
    - file: mlflow-3-for-genai-databricks-on-aws.md
    - file: get-started-with-mlflow-3-for-models-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow 3 for GenAI
description: A comprehensive set of features in MLflow 3 for generative AI application development including tracing, evaluation with LLM judges, human feedback collection, and a centralized Prompt Registry.
tags:
  - mlflow
  - genai
  - llm
  - evaluation
timestamp: "2026-06-19T19:00:45.694Z"
---

# MLflow 3 for GenAI

**MLflow 3 for GenAI** is an open platform that unifies tracking, evaluation, and observability for GenAI applications and agents throughout the development and production lifecycle. ^[mlflow-3-for-genai-databricks-on-aws.md] It includes real-time trace logging, built-in and custom scorers, incorporation of human feedback, and version tracking to help efficiently evaluate and improve app quality during development and continue tracking and improving quality in production. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Overview

Evaluating GenAI applications and agents is more complex than traditional software. Inputs and outputs are often free-form text, many different outputs can be considered correct, and quality depends on factors like correctness, precision, length, completeness, and appropriateness. ^[mlflow-3-for-genai-databricks-on-aws.md] Because LLMs are non-deterministic and GenAI agents include retrievers and tools, responses can vary from run to run. ^[mlflow-3-for-genai-databricks-on-aws.md] MLflow 3 for GenAI provides concrete quality metrics, automated evaluation, and continuous monitoring to build and deploy robust AI apps. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Core Features

### Tracing and Observability

[MLflow Tracing](/concepts/mlflow-tracing.md) provides end-to-end observability for GenAI applications, with automatic instrumentation for over 20 frameworks including OpenAI, LangChain, LlamaIndex, and Anthropic. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md] It logs the trace data required for evaluation and monitoring, automatically capturing inputs, intermediate steps, and outputs. ^[mlflow-3-for-genai-databricks-on-aws.md] This forms the data foundation for all downstream evaluation. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Evaluation and Monitoring

MLflow 3 replaces manual testing with automated evaluation using built-in and custom [LLM Judges](/concepts/llm-judges.md) and scorers. ^[mlflow-3-for-genai-databricks-on-aws.md] These judges match human expertise and can be applied in both development and production. ^[mlflow-3-for-genai-databricks-on-aws.md] The evaluation and monitoring capabilities include:

- Built-in LLM judges for common quality criteria. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- Customizable judges created with the `make_judge()` API. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- Evaluation dataset management for systematic testing. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]
- Real-time monitoring in production. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

Every production interaction becomes an opportunity to improve with integrated feedback and evaluation workflows. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Human Feedback Collection

MLflow 3 provides a customizable Review UI for collecting domain expert feedback and interactively testing agents. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md] It includes structured [Labeling Sessions](/concepts/labeling-sessions.md) for organizing and tracking review progress. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md] This feedback can be used to align automated judges with expert judgment. ^[mlflow-3-for-genai-databricks-on-aws.md]

### Prompt Registry

The [Prompt Registry](/concepts/prompt-registry.md) provides centralized prompt versioning, management, and A/B testing with [Unity Catalog](/concepts/unity-catalog.md) integration. ^[get-started-with-mlflow-3-for-models-databricks-on-aws.md]

### Lifecycle Management

MLflow 3 for GenAI enables versioning, tracking, and governance of the entire GenAI application with enterprise-grade lifecycle management and governance tools. ^[mlflow-3-for-genai-databricks-on-aws.md] This includes app and prompt versioning to allow comparison across iterations and track improvements over time. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Managed MLflow on Databricks

Managed MLflow on Databricks extends open source MLflow with capabilities designed for production GenAI applications, including enterprise-ready governance, fully managed hosting, production-level scaling, and integration with data in the Databricks lakehouse and Unity Catalog. ^[mlflow-3-for-genai-databricks-on-aws.md] Unity Catalog provides consistent governance for prompts, apps, and traces. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Getting Started

For information about agent evaluation in MLflow 2, see Agent Evaluation (MLflow 2) and the migration guide. In MLflow 3, the Agent Evaluation SDK methods have been integrated with Databricks-managed MLflow. ^[mlflow-3-for-genai-databricks-on-aws.md]

## Related Concepts

- [Tracing and observability](/concepts/mlflow-tracing-for-genai-observability.md)
- [LLM Judges](/concepts/llm-judges.md)
- [Custom Judges](/concepts/custom-judges.md)
- [Human feedback collection](/concepts/mlflow-human-feedback-collection.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Prompt Registry](/concepts/prompt-registry.md)
- [Unity Catalog](/concepts/unity-catalog.md)
- [Agent Evaluation](/concepts/mlflow-agent-evaluation.md)
- [MLflow 3 for Models](/concepts/mlflow-3-for-models.md)
- Evaluation dataset management
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)

## Sources

- mlflow-3-for-genai-databricks-on-aws.md
- get-started-with-mlflow-3-for-models-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [mlflow-3-for-genai-databricks-on-aws.md](/references/mlflow-3-for-genai-databricks-on-aws-ac0de02b.md)
2. [get-started-with-mlflow-3-for-models-databricks-on-aws.md](/references/get-started-with-mlflow-3-for-models-databricks-on-aws-288527af.md)
3. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
