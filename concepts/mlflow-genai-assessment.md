---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ac1245e121a9472b22a1a0b12f91f642b62f86f3edd067bffc20629386067e65
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-assessment
    - MGA
    - MLflow Assessment
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: code-based-scorer-reference-databricks-on-aws.md
title: MLflow GenAI Assessment
description: Quality measurements and ground truth labels (feedback or expectations) attached to a trace, added by end users, domain experts, or automated scorers.
tags:
  - mlflow
  - evaluation
  - quality
timestamp: "2026-06-18T11:05:41.226Z"
---

# MLflow GenAI Assessment

**MLflow GenAI Assessment** refers to the suite of tools, SDKs, and data structures provided by MLflow for evaluating the quality of generative AI applications. It encompasses both offline (development) evaluation and online (production) monitoring, using automated scorers and human feedback to attach quality measurements—called **assessments**—to application traces. Assessments are quality measurements and ground truth labels attached to a trace. There are two types: *feedback* (judgments about output quality) and *expectations* (ground truth defining correct output for a given input). Feedback can come from end users, domain experts, or automated scorers; expectations are typically added by domain experts as a gold standard. ^[concepts-data-model-databricks-on-aws.md]

## Scorers

Scorers are functions that analyze a trace’s quality and create feedback assessments. They parse a trace for relevant data fields, evaluate quality using either deterministic code or an LLM judge based on evaluation criteria, and return feedback entities with the results. Scorers act as the “adapter” between traces and evaluation logic — they extract the request, response, and context from a trace and pass them to a judge or custom code. The same scorer can be used for both development evaluation and production monitoring. MLflow provides built-in scorers (e.g., `mlflow.genai.judges.is_correct`) and supports custom scorers. For custom scorers that need API keys or credentials, you can access [Databricks secrets](/concepts/databricks-secret-scopes.md) inside the scorer function by importing `from databricks.sdk.runtime import dbutils`. ^[concepts-data-model-databricks-on-aws.md] ^[code-based-scorer-reference-databricks-on-aws.md]

## Evaluation in Development

MLflow’s `mlflow.genai.evaluate()` SDK systematically evaluates application quality during development. The evaluation harness takes an evaluation dataset, a set of scorers, and the application’s prediction function as input. It runs the app for every record in the dataset — producing [Traces](/concepts/traces.md) — then runs each scorer on the resulting traces to assess quality, creating feedback assessments attached to each trace. The output is an [Evaluation Run](/concepts/evaluation-run.md) containing traces with assessments and aggregated metrics. This process helps validate whether changes improved or regressed quality and identify further improvements. ^[concepts-data-model-databricks-on-aws.md]

## Evaluation in Production

With `mlflow.genai.Scorer.start()`, you can schedule scorers to automatically evaluate traces from a deployed application. The production monitoring service runs the scorers on production traces, produces feedback, and attaches each feedback to the source trace. This enables real-time quality detection, helping teams quickly identify problematic queries or use cases to address in development. The same custom scorer code used in development can be registered and started for production monitoring without modification. ^[concepts-data-model-databricks-on-aws.md] ^[code-based-scorer-reference-databricks-on-aws.md]

## Data Model Entities Related to Assessment

- **Traces**: Capture the complete execution of an app (inputs, outputs, intermediate steps). Assessments are attached to traces.
- **Assessments**: Quality measurements attached to a trace, either feedback (judgments) or expectations (ground truth).
- **Evaluation Datasets**: Curated collections of test cases with inputs and optionally expectations, used as input to `mlflow.genai.evaluate()`.
- **Evaluation Runs**: Results of testing an app version against an evaluation dataset with scorers; contain traces and aggregated metrics.
- **Labeling Sessions**: Organize traces for human review by domain experts, producing assessments via a [Labeling Schema](/concepts/labeling-schema.md).
- **Labeling Schemas**: Define the questions and valid responses for collecting assessments from labelers. ^[concepts-data-model-databricks-on-aws.md]

## User Interfaces

MLflow provides the **MLflow Experiment UI** to view traces, feedback, evaluation results, and manage datasets. The **Review App** is a web interface where domain experts label traces with assessments using defined labeling schemas. These UIs support the assessment workflow by making quality data visible and actionable. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Tracing](/concepts/mlflow-genai-tracing.md) – foundation for capturing execution data
- [Evaluation Harness](/concepts/evaluation-harness.md) – the machinery behind `mlflow.genai.evaluate()`
- Production Quality Monitoring – scheduled evaluation of production traces
- Feedback (MLflow) – structured output from scorers and human reviewers
- [Evaluation Datasets](/concepts/evaluation-datasets.md) – curated test cases for systematic evaluation

## Sources

- concepts-data-model-databricks-on-aws.md
- code-based-scorer-reference-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [code-based-scorer-reference-databricks-on-aws.md](/references/code-based-scorer-reference-databricks-on-aws-b52e32c9.md)
