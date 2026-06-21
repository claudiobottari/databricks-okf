---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 94190e8cf0f3aaffb1731385f7d677ec1488c6809e0db1a2fbfbc2ee8eceb89a
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-assessments
    - MTA
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
    - file: access-trace-data-databricks-on-aws.md
    - file: |-
        10-minute-demo-collect-human-feedback-databricks-on-aws.md
        - **span_id** – Optional identifier linking the assessment to a specific span within the trace. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Trace Assessments
description: Evaluations and feedback attached to traces, searchable by name, type (feedback/expectation), span ID, and source, with support for overrides and rationales.
tags:
  - mlflow
  - tracing
  - evaluation
timestamp: "2026-06-19T17:26:11.190Z"
---



# MLflow Trace Assessments

**MLflow Trace Assessments** are structured evaluations attached to individual [[MLflow Trace|MLflow Traces]] that capture human feedback, developer annotations, and expert judgments about the quality of a GenAI application's responses. Assessments provide the ground truth data needed to evaluate, debug, and improve AI applications throughout the development lifecycle. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Each assessment includes a name, value, rationale, and source information that identifies who provided the feedback. Assessments can be searched programmatically using `trace.search_assessments()` with filter criteria such as name, type, span ID, or source. ^[access-trace-data-databricks-on-aws.md]

## Assessment Data Model

An assessment is represented by the `Assessment` class from `mlflow.entities.assessment`, which contains the following fields: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

- **name** – A human-readable label for the assessment (e.g., "helpfulness", "accuracy"). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **value** – The actual feedback score, rating, or categorical judgment. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **source** – An `AssessmentSource` object with `source_type` (from `AssessmentSourceType` enum) and `source_id` (a string identifier for the reviewer). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **rationale** – Optional free-text explanation providing context for the evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **metadata** – Optional dictionary for additional structured information. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **error** – Optional error message if the assessment collection failed. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md
- **span_id** – Optional identifier linking the assessment to a specific span within the trace. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

The `AssessmentSourceType` enum defines two source types: `HUMAN` for human-provided feedback and `SYSTEM` for automated or programmatic assessments. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Searching Assessments

The `search_assessments()` method on `Trace` objects supports multiple filtering criteria: ^[access-trace-data-databricks-on-aws.md]

```python
# Get all assessments for a trace
all_assessments = trace.search_assessments()

# Filter by name
helpfulness = trace.search_assessments(name="helpfulness")

# Filter by assessment type
feedback_only = trace.search_assessments(type="feedback")
expectations_only = trace.search_assessments(type="expectation")

# Filter by span ID
span_assessments = trace.search_assessments(span_id=retriever_span.span_id)

# Include overridden assessments
all_including_invalid = trace.search_assessments(all=True)

# Combine criteria
human_feedback = trace.search_assessments(type="feedback", name="helpfulness")
```

## Accessing Assessment Details

Detailed assessment information can be accessed through `trace.info.assessments`: ^[access-trace-data-databricks-on-aws.md]

```python
for assessment in trace.info.assessments:
    print(f"Name: {assessment.name}")
    print(f"Type: {type(assessment).__name__}")
    print(f"Value: {assessment.value}")
    print(f"Source: {assessment.source.source_type.value}")
    print(f"Source ID: {assessment.source.source_id}")
    if assessment.rationale:
        print(f"Rationale: {assessment.rationale}")
    if assessment.metadata:
        print(f"Metadata: {assessment.metadata}")
    if assessment.error:
        print(f"Error: {assessment.error}")
```

## Types of Assessments

### End-User Feedback

End-user feedback captures how actual users perceive the quality of an AI application's responses. This is typically collected through UI elements such as thumbs up/down buttons, star ratings, or other feedback mechanisms embedded in the application interface. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Developer Annotations

Developers can add their own assessments directly through the MLflow UI. These annotations allow developers to evaluate response quality during development, providing scores and rationales that help track progress and identify issues. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expert Review Assessments

Expert review assessments provide authoritative ground truth from domain experts. These are collected through structured [Labeling Sessions](/concepts/labeling-sessions.md) that allow experts to review traces and provide detailed feedback. Expert assessments can include feedback assessments (categorical or numerical evaluations) and expectation assessments (the ideal or correct response). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Using Assessments for Evaluation

Assessments serve as ground truth for evaluating GenAI applications using MLflow's evaluation scorers: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

labeled_traces = mlflow.search_traces(run_id=labeling_session.mlflow_run_id)
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

The `Correctness` scorer compares application outputs against expert-provided `expected_response` assessments. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Viewing Assessments

Assessments appear in the MLflow UI alongside their associated traces. The trace details dialog shows assessments under the **Assessments** section on the right side. The Logs table also displays columns for assessment values after creation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Best Practices

- **Collect feedback from multiple sources.** Combine end-user feedback, developer annotations, and expert reviews for a comprehensive view. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Use structured label schemas.** Define clear, consistent criteria for expert assessments to ensure reliable ground truth data. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Include rationales.** Provide rationale text with assessments to give context for the evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Track assessment sources.** Use `AssessmentSource` to identify who provided each assessment, enabling traceability and accountability. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Use expert assessments as ground truth.** Expert-provided `expected_response` assessments are particularly valuable for evaluating application correctness. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The execution records that assessments are attached to
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured review processes for collecting expert assessments
- [Label Schemas](/concepts/label-schemas.md) — Definitions of what feedback to collect in a labeling session
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The framework for evaluating GenAI applications using assessments
- [Correctness Scorer](/concepts/correctness-scorer.md) — An evaluation scorer that compares outputs to expected responses
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — The broader practice of collecting and using human feedback

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md
- access-trace-data-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
2. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
3. 10-minute-demo-collect-human-feedback-databricks-on-aws.md
- **span_id** – Optional identifier linking the assessment to a specific span within the trace. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md
