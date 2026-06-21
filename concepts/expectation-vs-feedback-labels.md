---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4744e1ff476682e9ed81c72d74335dff9d174b886c864bc451683ca30dc4c411
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectation-vs-feedback-labels
    - EVFL
    - Expectation vs. Feedback
    - expectations
    - expectation-vs-feedback-label-types
    - EVFLT
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Expectation vs Feedback Labels
description: "Two types of labeling schemas: expectation type captures ground truth or correct answers (usable in evaluation datasets), while feedback type captures subjective assessments, ratings, or classifications."
tags:
  - mlflow
  - labeling
  - evaluation
  - genai
timestamp: "2026-06-19T09:16:31.912Z"
---

# Expectation vs Feedback Labels

**Expectation vs Feedback Labels** are two distinct types of labeling schemas in MLflow's Review App that define the kind of input domain experts provide when reviewing traces of a GenAI application. The choice between them depends on whether the expert is supplying a verifiable ground truth (expectation) or a subjective judgment (feedback). ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Expectation Labels

An **expectation label** is used when a domain expert provides a "ground truth" or correct answer for a given trace. For example, in a RAG (Retrieval-Augmented Generation) system, the expert might supply the `expected_facts` that should have been included in the response. Expectation labels are defined by setting `type="expectation"` when creating a [Labeling Schema](/concepts/labeling-schema.md). ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

These labels are particularly valuable because they can be directly repurposed as part of an [Evaluation Dataset](/concepts/evaluation-dataset.md) for systematic testing. When you later run `mlflow.genai.evaluate()`, the expectation labels serve as reference answers against which new model outputs are compared. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Feedback Labels

A **feedback label** captures subjective assessments, ratings, or classifications from the expert. Examples include rating a response on a scale of 1–5 for politeness, or classifying whether a response met certain criteria. Feedback labels are defined by setting `type="feedback"` when creating a labeling schema. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Unlike expectation labels, feedback labels represent human judgment rather than objective correctness. They are useful for understanding quality dimensions that are hard to quantify programmatically, such as tone, helpfulness, or adherence to brand guidelines. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Key Differences

| Aspect | Expectation Label | Feedback Label |
|--------|-------------------|----------------|
| **Purpose** | Provide a correct answer or ground truth | Capture subjective assessment or rating |
| **Type value** | `"expectation"` | `"feedback"` |
| **Use in evaluation** | Directly convertible to evaluation dataset ground truths | Used for qualitative analysis and judge alignment |
| **Typical input method** | Free-form text (e.g., `InputText`) | Categorical choices, numeric scales, or text |
| **Example** | "The correct summary should be: …" | "On a scale of 1–5, how polite is this response?" |

## When to Use Each

Use **expectation labels** when:
- There is a single correct answer or set of facts the agent should have produced.
- You plan to build an evaluation dataset for automated regression testing.
- The expert’s knowledge is authoritative and can serve as a reference standard. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Use **feedback labels** when:
- The quality criteria are subjective or multi-dimensional.
- You want to collect nuanced human opinions that cannot be reduced to a single ground truth.
- You are aligning [Custom Judges](/concepts/custom-judges.md) with human preferences through iterative refinement. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Integration with the Review App

In the MLflow [Review App](/concepts/mlflow-review-app.md), domain experts label traces by answering the questions defined in the labeling schema. Both expectation and feedback labels are stored as `Assessment` objects on the traces within a [Labeling Session](/concepts/labeling-session.md). You can later retrieve these labels programmatically to analyze them or convert expectation labels into [Evaluation Datasets](/concepts/evaluation-datasets.md). ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [Labeling Schema](/concepts/labeling-schema.md) – Defines the questions and input types for expert reviews.
- [Labeling Session](/concepts/labeling-session.md) – Organizes traces for review with selected schemas.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – Structured data used with `mlflow.genai.evaluate()`.
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that can be aligned with human feedback.
- [Trace Labeling](/concepts/expert-trace-labeling-workflow.md) – The overall process of collecting expert annotations on traces.
- Align judges with human feedback – Improving judge quality using expectation and feedback labels.

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
