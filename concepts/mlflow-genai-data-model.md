---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c93d0118fca0c2b9aef69cff737491856177524df8ed441935e2de4f06331dd6
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-data-model
    - MGDM
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: MLflow GenAI Data Model
description: Hierarchical data model for organizing generative AI application data within experiments, covering traces, evaluations, human labeling, and versioning.
tags:
  - mlflow
  - data-model
  - generative-ai
timestamp: "2026-06-18T14:41:26.317Z"
---

## MLflow GenAI Data Model

The **MLflow GenAI Data Model** defines how generative AI applications (agents, RAG pipelines, chat bots) are represented, evaluated, and monitored within [MLflow for GenAI](/concepts/mlflow-3-for-genai.md). It organizes all application data inside a single container—the [MLflow Experiment](/concepts/mlflow-experiment.md)—and provides structured entities for observability, evaluation, human labeling, and versioning. Only [Traces](/concepts/traces.md) are required; all other entities are optional but recommended. ^[concepts-data-model-databricks-on-aws.md]

### Core Entities

#### Experiment
An experiment is a named container that groups all artifacts related to one GenAI application: traces, evaluation runs, app versions, prompts, and quality assessments. Experiments in GenAI work the same way as in classic MLflow. ^[concepts-data-model-databricks-on-aws.md]

#### Traces
[Traces](/concepts/traces.md) capture the complete execution of an application, including inputs, outputs, and every intermediate step (LLM calls, retrievals, tool use). Traces are created automatically for every execution in development and production. They can be optionally linked to the application version that generated them and have attached [Assessments](/concepts/assessments.md) that contain quality feedback and ground truth expectations. Traces are used to observe and debug behavior, and to create evaluation datasets from production logs. ^[concepts-data-model-databricks-on-aws.md]

#### Assessments
[Assessments](/concepts/assessments.md) are quality measurements and ground truth labels attached to a trace. There are two types:
- **Feedback** – judgments about output quality (e.g., thumbs up/down, LLM judge scores).
- **Expectations** – ground truth labels defining the correct output for a given input (e.g., expected answer, required facts).

Feedback is added by end users, domain experts, or automated scorers. Expectations are added by domain experts and serve as a “gold standard” for evaluation. Most applications will not have ground truth labels or will have only a small set. ^[concepts-data-model-databricks-on-aws.md]

#### Evaluation Datasets
[Evaluation Datasets](/concepts/evaluation-datasets.md) are curated collections of test cases for systematic testing. They are typically created by selecting representative traces from production or development. Datasets include inputs and optionally expectations (ground truth). They are versioned over time to track how the test suite evolves. ^[concepts-data-model-databricks-on-aws.md]

#### Evaluation Runs
[Evaluation Runs](/concepts/evaluation-runs.md) are the results of testing an application version against an evaluation dataset using a set of scorers. Each evaluation run contains the traces (and their assessments) generated during evaluation, along with aggregated metrics. Evaluation runs are used to determine whether changes improved or regressed quality, compare versions side-by-side, and track quality over time. ^[concepts-data-model-databricks-on-aws.md]

#### Labeling Sessions and Labeling Schemas
[Labeling Sessions](/concepts/labeling-sessions.md) organize traces for human review by domain experts. They queue selected traces for expert review and store the resulting assessments. [Labeling Schemas](/concepts/labeling-schemas.md) define the structure of those assessments—what questions to ask and what response formats are valid (e.g., thumbs up/down, 1–5 scales, free text). Schemas ensure consistent label collection across experts. ^[concepts-data-model-databricks-on-aws.md]

#### Prompts
[Prompts](/concepts/prompt-versioning.md) are version-controlled templates for LLM prompts. They are tracked with Git-like version history, support `{{variables}}` for dynamic generation, and can be linked to evaluation runs to track quality over time. Aliases such as `"production"` are supported for deployment management. ^[concepts-data-model-databricks-on-aws.md]

#### Logged Models
[Logged Models](/concepts/logged-models.md) are snapshots of the application at specific points in time. They link to the traces they generate, the prompts they use, and evaluation runs that measure their quality. Logged models can act as a metadata hub, connecting a conceptual application version to its specific external code (e.g., a Git commit), or they can package the application’s code and configuration as a fully deployable artifact. ^[concepts-data-model-databricks-on-aws.md]

### SDKs for Evaluating Quality

#### Scorers
`mlflow.genai.scorers.*` are functions that evaluate a trace’s quality. They parse the trace for relevant data fields, evaluate quality using deterministic code or an LLM judge, and return feedback entities. In MLflow, a judge is a callable SDK (e.g., `mlflow.genai.judges.is_correct`) that evaluates text. Scorers act as an adapter, extracting the relevant data from a trace and passing it to the judge. The same scorer can be used for evaluation in both development and production. ^[concepts-data-model-databricks-on-aws.md]

#### Evaluation in Development
`mlflow.genai.evaluate()` is the SDK for systematically evaluating application quality. The evaluation harness takes an evaluation dataset, a set of scorers, and the application’s prediction function. It runs the app for every record in the dataset to produce traces, runs each scorer on those traces to produce feedback, and attaches the feedback to the appropriate trace. This is used to iteratively test improvements and validate whether changes improve or regress quality. ^[concepts-data-model-databricks-on-aws.md]

#### Evaluation in Production
`mlflow.genai.Scorer.start()` schedules scorers to automatically evaluate traces from a deployed application. The production monitoring service runs the scorers on production traces, producing feedback, and attaches each feedback to the source trace. This enables detection of quality issues quickly and identification of problematic queries for improvement in development. ^[concepts-data-model-databricks-on-aws.md]

### User Interfaces

#### Review App
The review app is a web UI where domain experts label traces with assessments. It presents traces from labeling sessions and collects assessments based on labeling schemas. ^[concepts-data-model-databricks-on-aws.md]

#### MLflow Experiment UI
The MLflow experiment UI provides visual access to search and view traces, review feedback and expectations, analyze evaluation results, manage evaluation datasets, and manage versions and prompts. ^[concepts-data-model-databricks-on-aws.md]

### Related Concepts
- [MLflow for GenAI](/concepts/mlflow-3-for-genai.md)
- Generative AI Evaluation
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md)
- [Prompt Version Management](/concepts/prompt-version-management.md)

### Sources
- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
