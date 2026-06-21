---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: aa6555e6d2156f484c49b76347931228db5fc6b6f0dedf54322700dee322a62c
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-experiment
    - MGE
  citations:
    - file: concepts-data-model-databricks-on-aws.md
    - file: get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md
title: MLflow GenAI Experiment
description: A named container that organizes all artifacts related to a single GenAI application, including traces, evaluations, prompts, and model versions.
tags:
  - mlflow
  - experiment
  - genai
  - data-model
timestamp: "2026-06-19T17:49:05.782Z"
---

# MLflow GenAI Experiment

**MLflow GenAI Experiment** (also referred to as a GenAI app experiment) is a named container in MLflow that organizes and groups together all artifacts related to a single [Generative AI](/concepts/mlflow-tracing-for-generative-ai.md) application.^[concepts-data-model-databricks-on-aws.md] An experiment contains every trace, evaluation run, app version, prompt, and quality assessment from throughout an app's lifecycle.^[concepts-data-model-databricks-on-aws.md] If you are familiar with MLflow for classic machine learning, the experiment container is the same between classic ML and GenAI.^[concepts-data-model-databricks-on-aws.md]

## Data Model Within an Experiment

An experiment organizes application data into several categories:^[concepts-data-model-databricks-on-aws.md]

- **Observability data**: [Traces (MLflow)](/concepts/trace-tags-mlflow.md) capture the complete execution of a GenAI application, including inputs, outputs, and every intermediate step (LLM calls, retrievals, tool use). [Assessments (MLflow)](/concepts/assessments-mlflow-genai.md) are quality measurements and ground truth labels attached to a trace.^[concepts-data-model-databricks-on-aws.md]
- **Evaluation data**: [Evaluation Datasets](/concepts/evaluation-datasets.md) are curated collections of test cases for systematically testing an application. [Evaluation Runs](/concepts/evaluation-runs.md) are the results of testing an application version against an evaluation dataset using a set of scorers.^[concepts-data-model-databricks-on-aws.md]
- **Human labeling data**: [Labeling Sessions](/concepts/labeling-sessions.md) organize traces for human review by domain experts. [Labeling Schemas](/concepts/labeling-schemas.md) define the assessments collected in a labeling session.^[concepts-data-model-databricks-on-aws.md]
- **Application versioning data**: [Logged Models](/concepts/logged-models.md) represent snapshots of an application at specific points in time. [Prompts](/concepts/prompt-versioning.md) are version-controlled templates for LLM prompts.^[concepts-data-model-databricks-on-aws.md]

## Creating an Experiment

In a Databricks workspace:^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

1. In the left sidebar, under **AI/ML**, click **Experiments**.
2. At the top of the Experiments page, click **GenAI apps & agents**.
3. To get the experiment ID and path, click the information icon in the upper-left.

## Connecting to an Experiment

MLflow requires only that you use [Traces (MLflow)](/concepts/trace-tags-mlflow.md) — all other aspects of the data model are optional but highly recommended.^[concepts-data-model-databricks-on-aws.md] To connect a local development environment to an experiment, set the `MLFLOW_EXPERIMENT_ID` environment variable and configure authentication with Databricks:^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```bash
export DATABRICKS_TOKEN=<databricks-personal-access-token>
export DATABRICKS_HOST=https://<workspace-name>.cloud.databricks.com
export MLFLOW_TRACKING_URI=databricks
export MLFLOW_REGISTRY_URI=databricks-uc
export MLFLOW_EXPERIMENT_ID=<experiment-id>
```

From code, use `mlflow.set_experiment()` to specify the experiment by name or path:^[get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md]

```python
mlflow.set_experiment("/Shared/docs-demo")
```

## Using the Experiment UI

The MLflow experiment UI provides visual access to many elements of the data model. Using the UI, you can do the following:^[concepts-data-model-databricks-on-aws.md]

- Search for and view traces.
- Review feedback and expectations.
- View and analyze evaluation results.
- Manage evaluation datasets.
- Manage versions and prompts.

## SDKs for Evaluating Quality Within an Experiment

Experiments support two key evaluation workflows:^[concepts-data-model-databricks-on-aws.md]

- **Evaluation in development**: [`mlflow.genai.evaluate()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/eval-harness) systematically evaluates application quality by running an evaluation dataset through the app and applying scorers to the resulting traces.
- **Evaluation in production**: [`mlflow.genai.Scorer.start()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/concepts/production-quality-monitoring) schedules scorers to automatically evaluate traces from a deployed application.

## Next Steps

- Follow the [quickstart guide](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/) to trace a first application.
- Explore detailed guides for [Tracing (MLflow GenAI)](/concepts/traces-mlflow-genai.md), [Evaluation (MLflow GenAI)](/concepts/evaluation-harness-mlflow-genai.md), or [Human Feedback (MLflow GenAI)](/concepts/human-feedback-collection-in-mlflow.md).

## Related Concepts

- [MLflow](/concepts/mlflow.md) — The open-source platform for machine learning lifecycle management
- [Traces (MLflow)](/concepts/trace-tags-mlflow.md) — Execution logs captured within an experiment
- [Evaluation Datasets](/concepts/evaluation-datasets.md) — Test cases used within an experiment
- [Evaluation Runs](/concepts/evaluation-runs.md) — Results of quality evaluation within an experiment
- [Logged Models](/concepts/logged-models.md) — Application version snapshots
- [Prompts](/concepts/prompt-versioning.md) — Version-controlled LLM prompt templates
- 403 PERMISSION_DENIED Serverless Budget Policy Error — An error that can occur when running serverless workloads against an experiment without a configured budget policy

## Sources

- concepts-data-model-databricks-on-aws.md
- get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
2. [get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-in-a-local-ide-databricks-on-aws-58181913.md)
