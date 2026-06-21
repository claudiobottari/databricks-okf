---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 657fee5a164b9f70430318ab3dcda9e0631983e66e0b8942135e57484a9c37ee
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-results-comparison
    - MGERC
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 186
      end: 201
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 195
      end: 201
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
      start: 169
      end: 201
title: MLflow GenAI Evaluation Results Comparison
description: The ability to compare multiple evaluation runs side-by-side in the MLflow UI to measure the impact of prompt changes or model updates.
tags:
  - mlflow
  - comparison
  - evaluation
  - ui
timestamp: "2026-06-19T21:54:04.062Z"
---

# MLflow GenAI Evaluation Results Comparison

**MLflow GenAI Evaluation Results Comparison** is a feature in the MLflow UI that allows users to compare the evaluation results of different runs of a GenAI application. This comparison enables developers to assess the impact of changes—such as prompt modifications—on the quality, safety, and performance of their generative AI applications. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

When iterating on a GenAI application, it is common to modify prompts, models, or evaluation criteria and re-run evaluations. MLflow GenAI provides a comparison view that displays the results of multiple evaluation runs side-by-side, showing metrics from the [MLflow Scorers](/concepts/mlflow-scorers.md) used during evaluation. This allows developers to quickly identify which version of their application performs best across the defined criteria. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:186-201]

## Workflow for Comparing Results

### Running Evaluations

To compare results, you first run at least two evaluations of your GenAI application. For example, a typical workflow might involve:

1. Creating a baseline evaluation with an initial prompt.
2. Modifying the system prompt or other application parameters.
3. Re-running the evaluation with the same dataset and scorers.

Each evaluation run is recorded as a separate run within an [MLflow Experiment](/concepts/mlflow-experiment.md). ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:186-201]

### Accessing the Comparison View

To compare evaluation runs in the MLflow UI:

1. Navigate to the **Evaluation UI** by clicking the link in the evaluation cell output or by selecting **Experiments** from the left sidebar and clicking the experiment name.
2. Locate the two or more runs you wish to compare.
3. Select the runs and use the comparison feature to view their results side-by-side.

The comparison view shows the scores for each [Guidelines Scorer](/concepts/guidelines-scorer.md) and [Safety Scorer](/concepts/safety-scorer-in-mlflow.md), making it easy to see how changes affect criteria such as child-appropriateness, humor, template-matching, or safety. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:195-201]

## Example Use Case

In the standard quickstart tutorial, a GenAI application is built to complete sentence templates (similar to Mad Libs) with funny, child-appropriate content. After an initial evaluation reveals that some responses are not appropriate for children, the system prompt is revised with more specific guidelines. Re-running the evaluation and comparing the results in the MLflow UI shows the improved scores for child-safety and humor criteria, validating the prompt change. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:169-201]

## Benefits

MLflow GenAI Evaluation Results Comparison enables:

- **Prompt engineering iteration**: Quickly validate whether a new prompt produces better evaluation scores.
- **Model selection**: Compare the performance of different underlying models (e.g., different LLM versions or providers) against the same criteria.
- **Regression detection**: Identify when a change degrades performance on specific evaluation criteria.
- **Documentation and reproducibility**: Each evaluation run is logged, providing a historical record of application quality over time.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that generates the results being compared.
- [MLflow Scorers](/concepts/mlflow-scorers.md) — The scoring components (Guidelines, Safety, etc.) that produce the metrics shown in the comparison.
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit that groups related evaluation runs together for comparison.
- Prompt Engineering — The practice of iterating on prompts to improve GenAI outputs.
- GenAI Application Lifecycle — The broader process of developing, evaluating, and deploying generative AI applications.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:186-201](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
3. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:195-201](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
4. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md:169-201](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
