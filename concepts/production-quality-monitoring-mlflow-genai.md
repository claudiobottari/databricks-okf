---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f5769098faab7906ed293f80d6a91a3d115e68f18be81d674b743253a55fff05
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - production-quality-monitoring-mlflow-genai
    - PQM(G
    - Production Monitoring (MLflow GenAI)
    - Production monitoring (MLflow GenAI)
    - Production Monitoring for GenAI
    - Production monitoring for GenAI
    - production monitoring for GenAI
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Production Quality Monitoring (MLflow GenAI)
description: Scheduled evaluation of production traces using scorers via mlflow.genai.Scorer.start() to detect quality issues in deployed applications.
tags:
  - mlflow
  - monitoring
  - production
timestamp: "2026-06-18T14:41:43.005Z"
---

# Production Quality Monitoring (MLflow GenAI)

**Production Quality Monitoring** in MLflow GenAI refers to the practice of continuously evaluating the quality of a deployed generative AI application by running automated scorers on production traces. This enables teams to detect quality regressions, identify problematic queries, and gather feedback that can be used to improve the application in development. ^[concepts-data-model-databricks-on-aws.md]

## Overview

Production monitoring is a critical component of the MLflow GenAI lifecycle. While evaluation in development helps validate changes before deployment, production monitoring ensures that quality remains acceptable once the application is serving real users. The same [[scorers]] used during development can be deployed to production, providing consistent quality metrics across the entire application lifecycle. ^[concepts-data-model-databricks-on-aws.md]

## How Production Monitoring Works

### The Scorer Scheduling Mechanism

Production monitoring is enabled through the [`mlflow.genai.Scorer.start()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring) API, which allows you to schedule scorers to automatically evaluate traces from your deployed application. When a scorer is scheduled, the production monitoring service performs the following steps: ^[concepts-data-model-databricks-on-aws.md]

1. **Retrieves production traces** from the deployed application's execution logs.
2. **Runs the configured scorers** on each trace to assess quality.
3. **Produces feedback assessments** based on the scorer evaluations.
4. **Attaches each feedback** to the source trace for later analysis.

### Scorers vs. Judges in Production

In MLflow, a *judge* is a callable SDK (such as `mlflow.genai.judges.is_correct`) that evaluates text based on specific criteria. However, judges cannot directly process traces — they only understand text inputs. *Scorers* act as the "adapter" that connects traces to evaluation logic by extracting relevant data from a trace (such as the request, response, and retrieved context) and passing it to the judge for evaluation. The same scorer can be used for both development evaluation and production monitoring. ^[concepts-data-model-databricks-on-aws.md]

## Benefits of Production Monitoring

Production monitoring provides several key benefits for GenAI application teams: ^[concepts-data-model-databricks-on-aws.md]

- **Early detection of quality issues**: Scorers can identify regressions or degradation in response quality as soon as they occur.
- **Problematic query identification**: By analyzing which inputs produce low-quality outputs, teams can identify problematic use cases or edge cases.
- **Continuous improvement feedback loop**: Feedback from production monitoring can be used to create [Evaluation Datasets](/concepts/evaluation-datasets.md) for development, enabling targeted improvements.
- **Consistent quality metrics**: Using the same scorers in development and production ensures that quality measurements are comparable across the lifecycle.

## Related Concepts

- [[Scorers]] — Functions that evaluate a trace's quality and return feedback assessments
- [Traces](/concepts/traces.md) — Execution logs that capture the complete run of a GenAI application
- [Assessments](/concepts/assessments.md) — Quality measurements and ground truth labels attached to traces
- Evaluation in Development — Using `mlflow.genai.evaluate()` to test application versions before deployment
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Curated collections of test cases for systematic quality evaluation
- [MLflow Experiment UI](/concepts/mlflow-experiment.md) — Visual interface for viewing traces, feedback, and evaluation results

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
