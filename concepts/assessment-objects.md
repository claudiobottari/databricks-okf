---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f78968d8d91571c82ae0273ca7367a432b9edf7860fb9f5a6a98061716028b6
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessment-objects
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Assessment Objects
description: MLflow entity objects that store collected labels as structured assessments attached to traces within labeling sessions, retrievable via the MLflow SDK.
tags:
  - mlflow
  - entities
  - data-model
  - assessments
timestamp: "2026-06-19T09:17:10.613Z"
---

# Assessment Objects

**Assessment Objects** are the data structure in MLflow that stores labels—feedback or expectations—collected from domain experts during a [Labeling Session](/concepts/labeling-session.md). Each assessment is attached to an individual [Trace](/concepts/traces.md) and captures the expert’s response to a [Labeling Schema](/concepts/labeling-schema.md) question.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Overview

When a domain expert reviews a trace in the [Review App](/concepts/mlflow-review-app.md) and submits a label, MLflow records that label as an `Assessment` object on the trace within the labeling session. Assessments are the bridge between human expert judgment and automated evaluation workflows: they can be retrieved programmatically and used as ground truth for evaluation datasets or as feedback to improve the application.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Creation

Assessment objects are created in the context of a labeling session, which is a special [MLflow Run](/concepts/mlflow-run.md) that organizes traces for review. Each labeling session is configured with one or more labeling schemas. Each schema defines a question, an input type (categorical, numeric, free‑text, etc.), and whether the label is an *expectation* (a ground‑truth answer) or *feedback* (a subjective rating or classification). When the expert completes a label for a given trace, an `Assessment` object is generated and linked to that trace.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Properties

While the source material does not enumerate every field, the `Assessment` object is documented in the MLflow Python API reference as `mlflow.entities.Assessment`. Key characteristics include:

- **Trace attachment**: The assessment belongs to a specific trace within a labeling session.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
- **Schema‑driven**: The assessment’s structure (question, value type) is determined by the labeling schema that produced it.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
- **Value types**: The label value can be a categorical choice, a numeric rating, or free‑form text, depending on the schema’s input definition.
- **Type**: The assessment reflects either an `expectation` (ground truth) or `feedback` (subjective evaluation).^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Retrieval

Assessments are retrieved by searching the traces within a labeling session’s run. The `mlflow.search_traces()` function, when given the labeling session’s run ID, returns a pandas DataFrame that includes all traces and their associated assessments. From this data, you can extract and analyze the labels programmatically.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
labeled_traces_df = mlflow.search_traces(run_id=label_summaries.mlflow_run_id)
```

## Use Cases

- **Creating evaluation datasets**: Expectation‑type assessments provide ground‑truth answers that can be used to build evaluation datasets for `mlflow.genai.evaluate()`.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]
- **Analyzing feedback**: Feedback‑type assessments can be aggregated to measure quality trends, identify common failure modes, or align [Custom Judges](/concepts/custom-judges.md) with human preferences.
- **Iterative improvement**: By reviewing assessments across multiple labeling sessions, teams can track how changes to agent configuration affect expert‑perceived quality.

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) – Organizes traces for review and stores assessments.
- [Labeling Schemas](/concepts/labeling-schemas.md) – Defines the questions and input types that produce assessments.
- [Traces](/concepts/traces.md) – Record of a GenAI application execution; assessments are attached to them.
- [Review App](/concepts/mlflow-review-app.md) – UI through which domain experts create assessments.
- Align judges with human feedback – Using assessments to improve automated judges.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
