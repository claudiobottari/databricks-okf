---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9a9e59781965b2c25d2f86ea81661d8930bbc0cbdd38e13e4a2d2da95cfdc07f
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-evaluation-ui
    - MEU
    - MLflow 3 Evaluation
    - MLflow Evaluation
    - MLflow Evaluation API
    - MLflow evaluation
    - MLflow Model Evaluation
    - Model evaluation
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: MLflow Evaluation UI
description: Interactive user interface within MLflow for reviewing, comparing, and analyzing GenAI evaluation runs across different prompt versions.
tags:
  - mlflow
  - ui
  - evaluation
timestamp: "2026-06-19T08:46:57.971Z"
---

---
title: MLflow Evaluation UI
summary: Interactive user interface in Databricks/MLflow for reviewing, comparing, and analyzing evaluation results across experiment runs.
sources:
  - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:35:25.328Z"
updatedAt: "2026-06-18T10:35:25.328Z"
tags:
  - mlflow
  - ui
  - experiment-tracking
aliases:
  - mlflow-evaluation-ui
  - MEU
confidence: 1
provenanceState: extracted
inferredParagraphs: 2
---

The **MLflow Evaluation UI** is a web-based interface within the MLflow platform that allows developers to review, compare, and analyze the results of GenAI Application evaluations. It enables users to inspect the outputs of their applications across different prompts, evaluation criteria, and model versions, providing a unified dashboard for understanding application quality. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Overview

The Evaluation UI is a core component of the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation framework. After running an evaluation using the `mlflow.genai.evaluate()` function, the results are logged to an MLflow experiment. The UI provides a centralized view of these results, allowing developers to assess how their application performs against predefined [MLflow Scorer](/concepts/mlflow-scorers.md) metrics and [LLM Judge](/concepts/llm-judges.md) criteria. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Accessing the Evaluation UI

To open the Evaluation UI after a run completes: the cell output from the evaluation function provides a direct link to the results. Alternatively, you can navigate to the **Experiments** page in the left sidebar of the MLflow UI and click the name of your experiment to open it. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Viewing Results

The UI displays a list of all evaluation runs (generations) for a given experiment. For each run, you can inspect the model's **output** and the **scores** assigned by each scorer (e.g., `same_language`, `funny`, `child_safe`). This allows for a quick visual check of which outputs meet the defined guidelines and which do not. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The UI also supports reviewing the [[MLflow Trace|ML trace]] associated with each generation, allowing you to see the exact input and output of the model call, as well as any metadata captured by automatic tracing. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Comparing Runs

A key feature of the Evaluation UI is the ability to **compare** different evaluation runs. When you iterate on your application (for example, by improving a system prompt), you can re-run the evaluation with the same data and scorers. In the UI, you can then select two (or more) runs to compare them side-by-side. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

This "compare runs" view highlights the differences in scores and outputs, making it easy to see which prompt or model version produced better results according to the specified criteria. This iterative workflow—evaluate, review, refine, re-evaluate—is fundamental to improving GenAI Application performance. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The programmatic framework for running evaluations.
- [MLflow Scorers](/concepts/mlflow-scorers.md) – The criteria used to evaluate outputs (e.g., `Guidelines`, `Safety`).
- [[MLflow Trace]] – The record of a single model execution, viewable in the UI.
- [MLflow Experiment](/concepts/mlflow-experiment.md) – The container for organizing evaluation runs.

## Sources

- [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md] - Source document for this page.

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
