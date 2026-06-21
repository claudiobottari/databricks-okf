---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8d4468a6a8e783eb6aea412f98851959f059b839e381ca7d088783897b61576c
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-based-evaluation-via-expert-review
    - TEVER
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - file: |-
        collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md>

        Additionally
    - file: you can add existing traces from the MLflow UI by selecting traces in the **Trace** tab
    - file: clicking **Export Traces**
    - file: and choosing the labeling session.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Trace-Based Evaluation via Expert Review
description: The practice of having domain experts label existing production traces to understand high-quality responses, align LLM judges with business requirements, and create evaluation datasets from real interactions.
tags:
  - evaluation
  - genai
  - mlflow
  - best-practices
timestamp: "2026-06-18T11:00:02.411Z"
---

# Trace-Based Evaluation via Expert Review

**Trace-Based Evaluation via Expert Review** is a structured process for collecting human judgment on real interactions with your GenAI application. By having domain experts review and label existing [[MLflow Trace|MLflow Traces]] using the MLflow Review App, teams can capture high-quality feedback, align automated evaluation with business requirements, and create ground-truth datasets for systematic testing.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## When to Use Expert Review

Expert review is most valuable for traces that require human judgment — cases such as ambiguous or borderline response quality, edge cases not covered by automated judges, instances where automated metrics disagree with expected quality, and representative samples of different user interaction patterns.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

The Review App serves three primary purposes: understanding what high-quality, correct responses look like for specific queries; collecting input to align [LLM Judges](/concepts/llm-judges.md) with business requirements; and creating [Evaluation Datasets](/concepts/evaluation-datasets.md) from production traces.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Prerequisites

| Requirement | Details |
|-------------|---------|
| MLflow version | 3.1.0 or above, installed with extras: `pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"` |
| Development environment | Must be connected to the [MLflow Experiment](/concepts/mlflow-experiment.md) where traces are logged (see [Tutorial: Connect your development environment to MLflow](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/connect-environment)) |
| Domain expert permissions | Experts must be provisioned in the Databricks account (they do not need workspace access) and have `CAN_EDIT` permission on the MLflow experiment |

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Workflow Overview

The process consists of six steps:

1. Create an application that logs traces
2. Define [Labeling Schemas](/concepts/labeling-schemas.md) for the feedback you want to collect
3. Create a [Labeling Session](/concepts/labeling-session.md) to organize the review queue
4. Generate traces and add them to the session
5. (Optional) Customize the Review App UI
6. View and use the collected labels

### Step 1: Create an App with Tracing

Before collecting feedback, you must have traces logged from your GenAI application. Traces capture inputs, outputs, and intermediate steps — including any tool calls or retriever actions. The example in the source material shows a sample app that uses a fake retriever and an LLM to generate summaries, instrumented with `@mlflow.trace` and `mlflow.openai.autolog()`.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 2: Define Labeling Schemas

Labeling schemas specify the questions and input types that experts will use. There are two main types:

- **Expectation type (`type="expectation"`)**: Used when the expert provides a ground-truth or correct answer (e.g., the expected set of facts a response should contain). These labels can be directly used in evaluation datasets.
- **Feedback type (`type="feedback"`)**: Used for subjective assessments, ratings, or classifications (e.g., rating politeness on a scale of 1–5, or classifying if a response met criteria).

The source material provides an example of creating a feedback schema (a categorical "Yes"/"No" question) and an expectation schema (free-text input for the correct summary). Both are created using `mlflow.genai.label_schemas.create_label_schema()`.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 3: Create a Labeling Session

A labeling session is a special type of [MLflow Run](/concepts/mlflow-run.md) that organizes a set of traces for review by specific experts using selected labeling schemas. It acts as a queue for the review process. You create it with `mlflow.genai.labeling.create_labeling_session()`, providing a name, assigned users, and the list of label schema names.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 4: Generate Traces and Add Them to the Labeling Session

After creating the session, you generate traces by running your application and then add them to the session using `label_summaries.add_traces(traces)`. Traces are copied into the session, so labels or modifications made during review do not affect the original logged traces. The session object provides a `url` that you can share with domain experts.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md>

Additionally, you can add existing traces from the MLflow UI by selecting traces in the **Trace** tab, clicking **Export Traces**, and choosing the labeling session.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 5: (Optional) Customize the Review App UI

For use cases that require custom trace visualization, tailored labeling interfaces, or specific workflows, you can deploy a customizable Review App template. This open-source template (available on GitHub at [databricks-solutions/custom-mlflow-review-app](https://github.com/databricks-solutions/custom-mlflow-review-app)) uses the same MLflow backend APIs and data model while giving full control over the frontend. Customization options include specialized trace renderers for agent types, custom labeling interface layouts, and domain-specific visualizations. The template includes command-line tools for programmatic setup or an AI assistant (Claude Code) for interactive customization. The customized Review App deploys as a Databricks App and integrates directly with your existing MLflow experiments and labeling sessions.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 6: View and Use Collected Labels

After experts complete their reviews, labels are stored as [Assessment](/concepts/assessments.md) objects on each trace within the labeling session. You can retrieve all labeled traces by querying the labeling session's [MLflow Run](/concepts/mlflow-run.md) ID using `mlflow.search_traces(run_id=label_summaries.mlflow_run_id)`, which returns a pandas DataFrame. The MLflow UI also provides a visual overview of the collected feedback.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Labels of type `expectation` are particularly useful for creating evaluation datasets that can be used with `mlflow.genai.evaluate()` to systematically test new versions of your GenAI application against expert-defined ground truth.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Review App Content Rendering

The Review App automatically renders different content types from MLflow Traces:

- **Retrieved documents**: Documents within a `RETRIEVER` span are rendered for display.
- **OpenAI format messages**: Inputs and outputs following OpenAI chat conversation format are rendered. This includes `outputs` containing a `ChatCompletions` object, or `inputs`/`outputs` dicts with a `messages` key containing an array of OpenAI chat messages (including tool calls).
- **Dictionaries**: Inputs and outputs that are dicts are rendered as pretty-printed JSON.

Otherwise, the `input` and `output` from the root span of each trace are used as the primary content for review.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- Human Feedback in MLflow — The broader system for collecting and managing human annotations
- [Labeling Sessions](/concepts/labeling-sessions.md) — Organizing traces for expert review
- [Labeling Schemas](/concepts/labeling-schemas.md) — Defining questions and input types for feedback
- [Assessment (MLflow)](/concepts/assessments.md) — The entity that stores collected labels
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Converting expert labels into test datasets for automated evaluation
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for automated assessment
- Trace (MLflow) — The unit of execution captured for observability
- Span Concepts (MLflow) — Spans as building blocks of traces
- Human Feedback in MLflow — End-to-end guide for collecting and using human feedback
- [ABAC Policy Scoping and Sprawl Prevention](/concepts/abac-policy-scoping-and-sprawl-prevention.md) — Best practices for managing ABAC policies (related as a governance concept)

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
2. collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md>

Additionally
3. you can add existing traces from the MLflow UI by selecting traces in the **Trace** tab
4. clicking **Export Traces**
5. and choosing the labeling session.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
