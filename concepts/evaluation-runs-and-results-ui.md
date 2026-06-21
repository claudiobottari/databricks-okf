---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d7c08e1c26db0a95d06da554031c4a1464b98eebbbc2981651f546ed9d04e8a
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-runs-and-results-ui
    - Results UI and Evaluation Runs
    - ERARU
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
title: Evaluation Runs and Results UI
description: The structured test report that captures all evaluation results, including per-row traces annotated with feedback from scorers, viewable in the Databricks UI with pass/fail assessments.
tags:
  - mlflow
  - evaluation
  - ui
  - results
timestamp: "2026-06-19T10:24:18.001Z"
---

## Evaluation Runs and Results UI

An **evaluation run** is a structured test report that captures everything about how a GenAI application performed on a specific [Evaluation Dataset](/concepts/evaluation-dataset.md). It contains a trace for each row in the dataset, annotated with feedback from each [[Scorers|scorer]] (LLM judge) applied during evaluation. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Accessing Evaluation Runs

1. Click **Experiments** in the sidebar to display the Experiments page.
2. Click the name of your experiment to open it.
3. In the left sidebar, click **Evaluation runs**. The right pane shows a table of traces.

If you do not see the pass/fail labels for each assessment, scroll to the right or hover over the pane separator and click the left-pointing arrow to expand the table. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Assessment Summary

The evaluation runs table displays each row from the dataset with columns for each scorer used. Assessments appear as **Pass** or **Fail** labels. To see the rationale behind a label, hover over the label; a tooltip appears showing the judge’s reasoning. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Trace Details and Adding Feedback

To inspect a single trace in detail:

1. Click the request identifier in the **Request** column. A window opens showing the full trace, including inputs and outputs for each step.
2. On the right side of this window you can add **Feedback** or **Expectations** to annotate the response. If the Assessments pane is not visible, click the assessments button (icon shown in the source) to expand it.
3. To add a new assessment, scroll down and click the **Add new assessment** button.

You can step through the requests in the dataset using the arrow buttons at either side of the detail window. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

### Related Concepts

- [MLflow genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The function that creates evaluation runs.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The structured test data used as input.
- [[Scorers]] – Quality metrics (built-in or custom) applied per row.
- [Traces](/concepts/traces.md) – Recorded execution paths of the GenAI app.
- [Feedback](/concepts/feedback-object.md) – Annotations added by judges or human reviewers.

### Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
