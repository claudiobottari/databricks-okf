---
title: Label during development | Databricks on AWS
source: https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/dev-annotations
ingestedAt: "2026-06-18T08:16:02.098Z"
---

As you build your GenAI app, [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/) lets you add feedback or expectations directly to traces. You can record quality issues, mark successful examples, or add notes for future reference. This allows you to track quality during development, before setting up formal evaluation.

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

*   Your application is instrumented with [MLflow Tracing](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/)
*   You have generated traces by running your application

## Add assessment labels[​](#add-assessment-labels "Direct link to Add assessment labels")

Assessments attach structured feedback, scores, or ground truth to traces and spans for quality evaluation and improvement in MLflow.

*   Databricks UI
*   MLflow SDK
*   Databricks REST API

You can add annotations (labels) directly to traces through the MLflow UI.

note

If you are using a Databricks notebook, you can also perform these steps from the Trace UI that renders inline in the notebook.

![human feedback](https://assets.docs.databricks.com/_static/images/mlflow3/human-feedback-quickstart.gif)

1.  Navigate to the Traces tab in the MLflow Experiment UI.
2.  Open an individual trace.
3.  Within the trace UI, click the specific span you want to label.
    *   Selecting the root span attaches feedback to the entire trace.
4.  Expand the Assessments tab at the far right.
5.  Fill in the form to add your feedback.
    *   **Assessment Type**
        *   _Feedback_: Subjective assessment of quality (ratings, comments)
        *   _Expectation_: The expected output or value (what should have been produced)
    *   **Assessment Name**
        *   A unique name for what the feedback is about
    *   **Data Type**
        *   Number
        *   Boolean
        *   String
    *   **Value**
        *   Your assessment
    *   **Rationale**
        *   Optional notes about the value
6.  Click **Create** to save your label.
7.  When you return to the Traces tab, your label appears as a new column.

## Next steps[​](#next-steps "Direct link to Next steps")

Continue your journey with these recommended actions and tutorials.

*   [Collect domain expert feedback](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/expert-feedback/label-existing-traces) - Set up structured labeling sessions
*   [Build evaluation datasets](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset) - Use your labeled traces to create test datasets
*   [Collect end-user feedback](https://docs.databricks.com/aws/en/mlflow3/genai/tracing/collect-user-feedback/) - Capture feedback from deployed applications

## Reference guides[​](#reference-guides "Direct link to Reference guides")

Explore detailed documentation for concepts and features mentioned in this guide.

*   [Labeling schemas](https://docs.databricks.com/aws/en/mlflow3/genai/human-feedback/concepts/labeling-schemas) - Learn about structured feedback collection
