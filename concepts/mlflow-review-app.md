---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b8e9bdf8d67ebadd52b4c6094859c3d08bd9d7718c9d72d40373c0758aea7847
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - create-and-manage-labeling-sessions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-review-app
    - MRA
    - Review App
    - Review apps
    - review app
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
    - file: create-and-manage-labeling-sessions-databricks-on-aws.md
title: MLflow Review App
description: A structured UI tool within MLflow for collecting domain expert feedback and expectations on GenAI application traces via labeling sessions and schemas.
tags:
  - mlflow
  - human-feedback
  - genai
  - evaluation
timestamp: "2026-06-19T17:45:47.345Z"
---

# MLflow Review App

**MLflow Review App** is a web-based interface within the [MLflow](/concepts/mlflow.md) ecosystem that enables domain experts to review and label existing [traces](/concepts/mlflow-tracing.md) from GenAI applications. It provides a structured process for collecting human feedback—both subjective assessments (`Feedback`) and ground-truth references (`Expectation`)—on real interactions captured in [labeling sessions](/concepts/labeling-sessions.md). The Review App is a core part of the MLflow human-feedback workflow, bridging automated evaluation with expert judgment. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Overview

The Review App is designed to collect domain-expert annotations on production or development traces. Experts can view the inputs, outputs, and intermediate steps of a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application, including tool calls and retrieved documents, and then answer questions defined in a [labeling schema](/concepts/labeling-schemas.md). The collected labels are stored as `Assessment` objects on the traces within a labeling session and can later be used to create [evaluation datasets](/concepts/evaluation-datasets.md), align automated LLM judges, or improve the application through iterative optimization. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md] ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

The Review App is accessed through a URL generated when a labeling session is created. Domain experts do not need Databricks workspace access—they only need to be provisioned in the Databricks account and have `CAN_EDIT` permission on the MLflow experiment containing the session. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Key Capabilities

### Label Existing Traces

The primary workflow: domain experts review traces that have already been logged from a GenAI application. The Review App renders the trace content (see [#Content Rendering in the Review App](/concepts/review-app-content-rendering.md)) and presents the labeling questions defined in the session's schemas. Experts provide ratings, classifications, free-text expectations, or comments. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Live App Testing (Chat UI)

When a labeling session is connected to an agent deployed on a [Model Serving](/concepts/model-serving.md) endpoint, the Review App provides a Chat UI for interactive testing. Experts can converse with the agent in real time, and the resulting traces are automatically added to the labeling session for review. This capability is enabled by setting the optional **Agent** field when creating the session. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

### Customizable UI Template

For teams that need specialized trace visualization or tailored labeling workflows, an open-source, customizable Review App template is available on GitHub. It uses the same MLflow backend APIs and data model, giving full control over the frontend experience while integrating with existing experiments and labeling sessions. The template deploys as a Databricks App. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Content Rendering in the Review App

The Review App automatically renders different content types from an MLflow trace to help experts understand each interaction: ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

- **Retrieved documents**: Spans of type `RETRIEVER` are displayed as documents, showing their `page_content` and metadata.
- **OpenAI-format messages**: Outputs of type `ChatCompletions` and inputs/outputs that contain a `messages` key with an array of OpenAI-format chat messages are rendered as a conversational interface. Tool calls within messages are also rendered.
- **Dictionaries**: Inputs and outputs that are plain dicts are displayed as pretty-printed JSON.
- **Fallback**: If none of the above apply, the `input` and `output` of the root span are shown as the primary content for review.

## Prerequisites and Permissions

To use the Review App for labeling existing traces: ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

- MLflow version 3.1.0 or above must be installed: `pip install --upgrade "mlflow[databricks]>=3.1.0"`
- The development environment must be connected to an MLflow experiment where traces are logged.
- Domain experts must be provisioned in the Databricks account (via account-level SCIM or manual registration) and have `CAN_EDIT` permission on the MLflow experiment. They do not need workspace access.

## Usage Workflow

1. **Create a labeling session** – Define a name, assign users, and select labeling schemas (built-in or custom). Use the MLflow UI or the `create_labeling_session()` API. ^[create-and-manage-labeling-sessions-databricks-on-aws.md] ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
2. **Generate or select traces** – Run the GenAI application to produce traces, or search existing traces using the MLflow UI or `mlflow.search_traces()`. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
3. **Add traces to the session** – Use the "Add to labeling session" action in the UI, or call `session.add_traces()`. Traces are copied into the session so labels do not affect the original traces. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md] ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
4. **Share the URL** – Provide the session URL to domain experts. They access the Review App to view traces and provide labels. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
5. **Retrieve feedback** – Labels are stored as `Assessment` objects on each trace in the session. Retrieve them via the MLflow UI or SDK (e.g., `mlflow.search_traces(run_id=session.mlflow_run_id)`). ^[create-and-manage-labeling-sessions-databricks-on-aws.md]
6. **(Optional) Sync to evaluation datasets** – Use the `session.sync()` method to upsert `Expectation` labels into an [Evaluation Dataset](/concepts/evaluation-dataset.md) for systematic testing. ^[create-and-manage-labeling-sessions-databricks-on-aws.md]

## Customization Options

The standard Review App is suitable for most workflows. For advanced needs—such as specialized trace renderers, custom labeling layouts, or domain-specific visualizations—deploy the open-source [custom-mlflow-review-app](https://github.com/databricks-solutions/custom-mlflow-review-app) template. This template includes command-line tools and an AI assistant for interactive customization. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – The container that organizes traces, schemas, and users for Review App workflows.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Define the questions and input types presented to reviewers.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The telemetry system that captures the inputs, outputs, and intermediate steps displayed in the Review App.
- Human Feedback in MLflow – Broader concept covering development-time annotations and production feedback.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom evaluation functions that can complement or replace human feedback.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for automated testing, often using expert-labeled datasets.
- [Production Monitoring](/concepts/production-monitoring.md) – Continuous evaluation using inference tables, which can reuse the same scorers and judges.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
- create-and-manage-labeling-sessions-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
2. [create-and-manage-labeling-sessions-databricks-on-aws.md](/references/create-and-manage-labeling-sessions-databricks-on-aws-6716f1fc.md)
