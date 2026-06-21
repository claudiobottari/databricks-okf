---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 8a5cfb41175d5a3df34dd94b13115848e92c5f9e85eb277e98f60c570c61be00
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - prompt-and-model-versioning
    - Model Versioning and Prompt
    - PAMV
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Prompt and Model Versioning
description: Version-controlled prompt templates with Git-like history and dynamic variables, plus logged models that snapshot application configurations, link to traces and evaluation runs, and can package code for deployment.
tags:
  - mlflow
  - versioning
  - deployment
timestamp: "2026-06-19T14:22:13.137Z"
---

##Prompt and Model Versioning

**Prompt and Model Versioning** refers to the practice of tracking and managing changes to the two core artifacts of a generative AI (GenAI) application: the LLM prompt templates and the application model (or “app version”). Versioning enables teams to iterate on application behavior, compare quality across changes, and roll back to known-good configurations.

In the MLflow data model, versioning is part of the **application versioning data** layer. Prompts and logged models are the primary versioned entities, each with their own lifecycle and relationships to other data such as traces and evaluation runs. ^[concepts-data-model-databricks-on-aws.md]

### Prompt Versioning

Prompts are version-controlled templates for LLM prompts. They are tracked with Git-like version history, allowing developers to review, revert, or branch prompt changes over time. ^[concepts-data-model-databricks-on-aws.md]

Key characteristics of prompt versioning:

- **Template variables**: Prompts include `{{variables}}` for dynamic generation, making them reusable across different inputs.
- **Aliases**: Prompts support aliases like `"production"` or `"staging"` for deployment management, enabling smooth promotion of prompt versions.
- **Quality linkage**: Each prompt version is linked to [Evaluation Runs](/concepts/evaluation-runs.md) so that teams can track how prompt changes affect application quality.

Prompt versioning is essential for safe iteration: a team can compare the performance of a new prompt variant against the production prompt using the same evaluation dataset and scorers. ^[concepts-data-model-databricks-on-aws.md]

### Model Versioning (Logged Models)

Logged models represent snapshots of your application at specific points in time. They act as a metadata hub, linking the conceptual application version to the specific prompts, traces, evaluation runs, and application parameters (for example, LLM temperature) that define that version. ^[concepts-data-model-databricks-on-aws.md]

Key characteristics of logged models:

- **Snapshot encapsulation**: A logged model captures the entire application configuration — code, prompts, parameters, and dependencies — at a given moment.
- **Trace & evaluation linkage**: Logged models link to the [Traces](/concepts/traces.md) they generate and to the evaluation runs that measure their quality.
- **Deployable artifact**: Beyond metadata, a logged model can be packaged as a fully deployable artifact containing both code and configuration.

Model versioning is used to:
- Pinpoint which version of an application produced a given trace.
- Compare quality across versions during development.
- Roll back to a previous version if a change regresses quality. ^[concepts-data-model-databricks-on-aws.md]

### Relationship Between Prompt and Model Versioning

While prompts are versioned independently, logged models reference specific prompt versions (and other parameters) to produce a reproducible application state. This dual versioning allows teams to:

- Experiment with prompt changes without redeploying the full application.
- Track how a specific prompt version performed in production by looking at the logged model that used it.
- Audit which combined set of prompt + application config generated a particular trace.

### Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md) — Containers that group all versioned artifacts for an application.
- [Traces](/concepts/traces.md) — Execution logs linked to versioned models and prompts.
- [Evaluation Runs](/concepts/evaluation-runs.md) — Quality results that are linked to specific prompt/model versions.
- GenAI Agent — A common application type that benefits from prompt and model versioning.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — A testing methodology that relies on versioned configurations.

### Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
