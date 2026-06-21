---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3ccd36fbbe578eed1e0949b6a983d0f4c5c58afa7e7b675ec0d8035d1cf75d34
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - evaluation-harness-and-production-monitoring
    - Production Monitoring and Evaluation Harness
    - EHAPM
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md
title: Evaluation Harness and Production Monitoring
description: The evaluation harness (mlflow.genai.evaluate()) runs applications against evaluation datasets with scorers for iterative quality improvement; production monitoring schedules scorers on live traces for ongoing quality oversight.
tags:
  - mlflow
  - evaluation
  - monitoring
  - production
timestamp: "2026-06-19T17:49:49.630Z"
---

# Evaluation Harness and Production Monitoring

**Evaluation Harness** and **Production Monitoring** are two complementary processes in MLflow for GenAI that assess the quality of generative AI applications. Both processes rely on [[Scorers]] to analyze traces and produce quality assessments, but they operate in different lifecycle stages: evaluation harness is used during development to iteratively improve quality, while production monitoring continuously evaluates traces from deployed applications. ^[concepts-data-model-databricks-on-aws.md]

## Evaluation Harness (Development)

The evaluation harness is exposed through the [`mlflow.genai.evaluate()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) SDK. It systematically evaluates an application version by taking an evaluation dataset, a set of scorers, and the application’s prediction function as input. The harness runs the application for every record in the dataset, produces traces, runs each scorer on those traces to assess quality, and attaches the resulting feedback assessments to the appropriate trace. The output is an evaluation run containing traces with feedback and aggregated metrics. ^[concepts-data-model-databricks-on-aws.md]

The evaluation harness is designed for iterative quality improvement during development. It helps validate whether a change improves or regresses quality and identifies further improvements. ^[concepts-data-model-databricks-on-aws.md]

Evaluation datasets used with the harness are curated collections of test cases, typically created by selecting representative traces from production or development. They may optionally include ground‑truth expectations. The datasets are versioned over time to track how the test suite evolves. ^[concepts-data-model-databricks-on-aws.md]

## Production Monitoring (Evaluation in Production)

Production monitoring is enabled through [`mlflow.genai.Scorer.start()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring), which schedules scorers to automatically evaluate traces from a deployed application. The production monitoring service runs the scorers on production traces, producing feedback assessments that are attached to the source trace. ^[concepts-data-model-databricks-on-aws.md]

The primary goal of production monitoring is to detect quality issues quickly and to identify problematic queries or use cases that can be improved during development. ^[concepts-data-model-databricks-on-aws.md]

Common production monitoring workloads include scheduled scorers, synthetic evaluation set generation, and agent evaluation. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md] These workloads may require a serverless budget policy to be set on the MLflow experiment; if the default policy is disabled and no fallback is available, a `403 PERMISSION_DENIED` error can occur. ^[configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md]

## Scorers: The Common Component

Both the evaluation harness and production monitoring use [[Scorers]] to evaluate trace quality. A scorer is a function that:
- Parses a trace to extract the relevant data fields to be evaluated.
- Uses that data to evaluate quality, either through deterministic code or via an LLM judge–based evaluation criteria.
- Returns feedback entities containing the evaluation results. ^[concepts-data-model-databricks-on-aws.md]

The same scorer can be used for both development evaluation and production monitoring, providing consistency across the application lifecycle. ^[concepts-data-model-databricks-on-aws.md]

Scorers act as an adapter between traces and judges. A judge (such as `mlflow.genai.judges.is_correct`) evaluates text based on specific criteria but cannot directly process traces. The scorer extracts the relevant data from a trace (request, response, retrieved context) and passes it to the judge. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [[Scorers]]
- [Evaluation Runs](/concepts/evaluation-runs.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [Traces](/concepts/traces.md)
- [Assessments](/concepts/assessments.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Serverless Budget Policy](/concepts/serverless-budget-policy.md)

## Sources

- concepts-data-model-databricks-on-aws.md
- configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws.md](/references/configure-a-serverless-budget-policy-for-an-mlflow-experiment-databricks-on-aws-cb1d8a65.md)
