---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f26fefb4ca04486b1cd4de222cb7a3552d32f6c304df1a41e48beba217b9ea08
  pageDirectory: concepts
  sources:
    - concepts-data-model-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - assessments
    - Assessment
    - Log Assessments
    - Log assessments
    - assessment
    - assessment report
  citations:
    - file: concepts-data-model-databricks-on-aws.md
title: Assessments
description: Quality measurements attached to a trace, comprising feedback (judgments from scorers, users, or experts) and expectations (ground-truth labels from domain experts).
tags:
  - mlflow
  - assessments
  - quality
  - evaluation
timestamp: "2026-06-19T17:49:24.261Z"
---

---
title: Assessments
summary: Quality measurements and ground truth labels attached to traces, divided into feedback (judgments about output quality) and expectations (ground truth correct outputs).
sources:
  - concepts-data-model-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T09:21:06.192Z"
updatedAt: "2026-06-19T14:21:14.705Z"
tags:
  - mlflow
  - evaluation
  - quality
aliases:
  - assessments
confidence: 1
provenanceState: extracted
inferredParagraphs: 0
---

# Assessments

**Assessments** are quality measurements and ground truth labels that are attached to a [trace](/concepts/traces.md) in the [MLflow for GenAI](/concepts/mlflow-3-for-genai.md) data model. They capture information about the quality of an application's outputs, enabling both automated and human-driven evaluation throughout the development and production lifecycle. ^[concepts-data-model-databricks-on-aws.md]

## Types of Assessments

There are two types of assessments: **feedback** and **expectations**. ^[concepts-data-model-databricks-on-aws.md]

### Feedback

Feedback refers to judgments about the quality of an application's outputs. It is added by end users, domain experts, or automated [[scorers]] and is used to identify quality issues. Examples include thumbs up or thumbs down ratings from end users and an [LLM judge](/concepts/llm-judges.md)'s assessment of a response's correctness. ^[concepts-data-model-databricks-on-aws.md]

### Expectations

Expectations are ground truth labels that define the correct output for a given input. They are added by domain experts and serve as a "gold standard" to evaluate if an application produced the right response. Examples include the expected response to a question or the required facts that must be present in a response. ^[concepts-data-model-databricks-on-aws.md]

Ground truth labels (expectations) are not required to measure quality with MLflow; most applications will not have them or will have only a small set. ^[concepts-data-model-databricks-on-aws.md]

## Sources of Assessments

Assessments can be created through several mechanisms:

- **Automated scorers**: Functions that evaluate a trace's quality and produce feedback assessments. Scorers can use deterministic code or LLM judge-based evaluation criteria. The same scorer can be used for evaluation in both development and production. ^[concepts-data-model-databricks-on-aws.md]
- **End-user feedback**: Direct ratings provided by users of the application, such as thumbs up/down. ^[concepts-data-model-databricks-on-aws.md]
- **Domain experts**: Human reviewers who label traces with assessments through [Labeling Sessions](/concepts/labeling-sessions.md) or the [review app](/concepts/mlflow-review-app.md). ^[concepts-data-model-databricks-on-aws.md]

## How Assessments Are Used

Assessments are central to several MLflow workflows:

- **Evaluation in development**: The `mlflow.genai.evaluate()` SDK runs an application against an [Evaluation Dataset](/concepts/evaluation-dataset.md) and applies scorers to the resulting traces, producing feedback assessments. Evaluation runs contain traces with their assessments and aggregated metrics based on those assessments. ^[concepts-data-model-databricks-on-aws.md]
- **Evaluation in production**: Scheduled scorers automatically evaluate traces from deployed applications, producing feedback that is attached to the source trace for ongoing quality monitoring. ^[concepts-data-model-databricks-on-aws.md]
- **Human labeling**: Domain experts label traces with assessments via labeling sessions, which use [Labeling Schemas](/concepts/labeling-schemas.md) to structure the assessments collected. ^[concepts-data-model-databricks-on-aws.md]

## Related Concepts

- [Traces](/concepts/traces.md) — The execution logs to which assessments are attached
- [[Scorers]] — Functions that evaluate trace quality and produce feedback assessments
- [Evaluation Runs](/concepts/evaluation-runs.md) — Results of systematic evaluation, containing traces and their assessments
- [Labeling Sessions](/concepts/labeling-sessions.md) — Queues of traces organized for human expert review
- [Labeling Schemas](/concepts/labeling-schemas.md) — Structured definitions of what assessments to collect from reviewers
- Review app — Web UI for domain experts to label traces with assessments

## Sources

- concepts-data-model-databricks-on-aws.md

# Citations

1. [concepts-data-model-databricks-on-aws.md](/references/concepts-data-model-databricks-on-aws-1534caf0.md)
