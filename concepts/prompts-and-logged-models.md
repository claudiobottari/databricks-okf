---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0cb90199d2794af1c717879642edb43eefbe9865fb02065ac5089d8c41cdde1c
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - prompts-and-logged-models
    - Logged Models and Prompts
    - PALM
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Prompts and Logged Models
description: Prompts are version-controlled LLM templates with variables and aliases; logged models are application snapshots linking traces, prompts, and evaluation runs, serving as a metadata hub or deployable artifact.
tags:
  - mlflow
  - prompts
  - versioning
  - models
timestamp: "2026-06-19T17:49:28.130Z"
---

# Prompts and Logged Models

**Prompts** and **Logged Models** are two core entities in the [MLflow for GenAI](/concepts/mlflow-3-for-genai.md) data model that support application versioning. Together, they provide a structured way to track, version, and deploy generative AI applications over their lifecycle.

## Prompts

**Prompts** are version-controlled templates for LLM prompts. They encapsulate the instructions and context sent to a large language model and are tracked with Git-like version history. Prompts include `{{variables}}` placeholders for dynamic content generation, enabling reusable templates that adapt to different inputs at runtime. ^[concepts-data-model-databricks-on-aws.md]

Prompts are linked to [Evaluation Runs](/concepts/evaluation-runs.md) to track quality metrics over time. They also support aliases—such as `"production"` or `"staging"`—for deployment management, making it straightforward to promote a prompt version through different stages. ^[concepts-data-model-databricks-on-aws.md]

## Logged Models

**Logged Models** represent snapshots of an application at specific points in time. A logged model links to the [Traces](/concepts/traces.md) it generates and the prompts it uses, creating a complete record of the application's behavior for a given version. They also link to evaluation runs, enabling teams to track quality changes across versions. ^[concepts-data-model-databricks-on-aws.md]

Beyond acting as a metadata hub—connecting an application version to its external code, such as a Git commit—logged models can package the application's code and configuration as a fully deployable artifact. This allows teams to reproduce, audit, or redeploy any historical version of their application. Application parameters such as LLM temperature are also tracked within the logged model. ^[concepts-data-model-databricks-on-aws.md]

## Relationship to Other Entities

Both prompts and logged models are organized within an [Experiment](/concepts/mlflow-experiment.md). Together with evaluation data and observability data (traces and assessments), they form the complete data model for developing and monitoring GenAI applications. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Experiment](/concepts/mlflow-experiment.md)
- [Traces](/concepts/traces.md)
- [Assessments](/concepts/assessments.md)
- [Evaluation Runs](/concepts/evaluation-runs.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [MLflow for GenAI](/concepts/mlflow-3-for-genai.md)
- [Prompt Registry](/concepts/prompt-registry.md)

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
