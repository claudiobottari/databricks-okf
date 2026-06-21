---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e896b0ff8793990ae980a9d8617971870d5dd74f267ae97637327dc3d7d0cb86
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
    - tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - evaluation-runs
    - Evaluations
    - Evaluations|evaluations
    - Quality Evaluations
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
    - file: tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
title: Evaluation Runs
description: Test reports that capture aggregate metrics and all per-row traces annotated with scorer feedback, viewable in the MLflow UI for investigation.
tags:
  - mlflow
  - evaluation
  - reporting
timestamp: "2026-06-19T18:42:25.939Z"
---

# Evaluation Runs

An **Evaluation Run** is a structured test report produced by the MLflow evaluation harness when you call [`mlflow.genai.evaluate()`]. It captures everything about how a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application performed on a specific [EvaluationDataset](/concepts/evaluation-dataset.md), including per‑request traces, scoring results, and aggregate metrics. Evaluation runs are stored in the active [MLflow Experiment](/concepts/mlflow-experiment.md) and provide a consistent way to compare app versions, track improvements, and share results across teams. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Structure of an Evaluation Run

Each evaluation run contains one trace for every row in the evaluation dataset, annotated with feedback from each [[Scorers|scorer]] (or LLM judge) that was applied. The feedback includes a **Pass** or **Fail** label and a rationale explaining the judge’s decision. Users can also manually add additional feedback or expectations to individual traces within the run. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

The run stores aggregate metrics computed across all traces, allowing you to see overall quality scores and quickly identify regressions. ^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Viewing Evaluation Runs

In the Databricks UI, navigate to your MLflow experiment and click **Evaluation runs** in the left sidebar. The right pane displays a table of traces with their assessments. If you do not see the Pass/Fail labels, scroll to the right or expand the pane. Hover over a label to view the judge’s rationale. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

To inspect a specific trace:
1. Click the request identifier in the **Request** column. A detail window opens showing the full trace, including inputs and outputs for every step.
2. Use the arrows at either side of the detail window to step through requests. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Comparing Evaluation Runs

You can compare multiple evaluation runs side by side to verify that app changes improved quality without causing regressions. To compare runs: ^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

1. Open the experiment and click **Evaluation runs** in the left sidebar.
2. Check the boxes for the runs you want to compare.
3. From the **Actions** drop‑down menu, select **Compare**.
4. The right pane displays a comparison table of each trace across the selected runs.
5. Click a request identifier to open a detailed comparison window that shows full traces and assessments for that request from each run. ^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Relationship to the Evaluation Harness

Evaluation runs are created automatically by `mlflow.genai.evaluate()`, which takes an evaluation dataset, a prediction function (or pre‑computed outputs), and a list of scorers. The harness runs the app on each input, captures a trace, scores it, and logs the results as a new evaluation run in the active experiment. This makes it easy to iteratively improve an app: you can run a new evaluation after every change and compare the results with previous runs. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiment](/concepts/mlflow-experiment.md) – The container for evaluation runs.
- [EvaluationDataset](/concepts/evaluation-dataset.md) – Versioned test data used as input to an evaluation run.
- [[Scorers|Scorer]] – Quality metric (built‑in or custom) applied to each trace.
- [Feedback](/concepts/feedback-object.md) – Judge annotations on individual traces within a run.
- [Traces](/concepts/traces.md) – Recorded execution details of each request.
- [Production Monitoring](/concepts/production-monitoring.md) – Reusing the same evaluation logic in production.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md
- tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
2. [tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md](/references/tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws-554c7fbb.md)
