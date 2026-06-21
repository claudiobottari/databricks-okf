---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 2c1f506823f1ad5c6d3076023e606ff0e5772c3fd67697559bfed9d3707148cd
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 0.85
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - offline-to-production-monitoring-consistency
    - OMC
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Offline-to-Production Monitoring Consistency
description: The principle that the same scorers and evaluation logic used in offline development can be reused in production monitoring, providing consistent quality metrics across the AI lifecycle.
tags:
  - mlflow
  - monitoring
  - mlops
timestamp: "2026-06-19T18:42:39.729Z"
---

# Offline-to-Production Monitoring Consistency

**Offline-to-Production Monitoring Consistency** is a design principle in MLflow's evaluation framework that ensures the same evaluation logic used during development can also run in production. This creates a consistent view of quality across the entire AI lifecycle, from offline testing to production monitoring. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Overview

The `mlflow.genai.evaluate()` function provides an evaluation harness for GenAI applications that connects offline testing with production monitoring. Instead of manually running an app and checking outputs one by one, MLflow Evaluation provides a structured way to feed in test data, run the app, and automatically score the results. This makes it easier to compare versions, track improvements, and share results across teams. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

The key consistency guarantee is that the same scorers defined for offline evaluation can be reused in Production Quality Monitoring. This is possible because the [Traces](/concepts/traces.md) generated during direct evaluation are identical to those produced in production. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Direct Evaluation (Recommended)

MLflow calls the GenAI app directly to generate and evaluate traces. By calling the app directly, this mode enables reuse of the scorers defined for offline evaluation in production monitoring, since the resulting traces will be identical. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

The app's entry point is wrapped in a Python function (`predict_fn`) or, if the app is deployed as a Databricks Model Serving endpoint, wrapped using `to_predict_fn`. During evaluation, MLflow runs the app and scorers in parallel and records output as traces and feedback. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Answer Sheet Evaluation

Use this mode when the GenAI app cannot be run directly during evaluation (for example, with outputs from external systems, historical traces, or batch jobs). The user provides inputs and pre-computed outputs, and `evaluate()` runs scorers and logs an evaluation run. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

When an answer sheet uses different traces than the production environment, scorers may need to be rewritten for use in production monitoring. This is the key trade-off against the consistency achieved with direct evaluation. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Benefits

- **Compare versions** — Track improvements and regressions across app versions. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- **Prevent regressions** — Validate prompt or model changes before a release or pull request. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- **Share results** — Evaluation runs act as structured test reports that teams can review together. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]
- **Consistent scoring** — The same scorers evaluate quality offline and in production, eliminating discrepancies between development and live environments. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Related Concepts

- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) — The evaluation harness function that connects offline and production monitoring.
- [[Scorers]] — Quality metrics (built-in or custom) shared between development and production.
- [Traces](/concepts/traces.md) — Captured execution records that remain identical between direct evaluation and production.
- Production Quality Monitoring — The production monitoring system that reuses offline scorers.
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Structured test data for running evaluations.
- [Feedback](/concepts/feedback-object.md) — Annotations created by scorers during evaluation.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
