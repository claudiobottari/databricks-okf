---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3c09e4331fc9a579f2f637aa36b7e55f755d918584e8a7473fed0fcb8f595b30
  pageDirectory: concepts
  sources:
    - access-trace-data-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-assessments
    - mlflow-trace-assessments
    - MTA
  citations:
    - file: access-trace-data-databricks-on-aws.md
title: Trace Assessments
description: Evaluations and feedback attached to traces, searchable by name, type (feedback/expectation), span ID, and source, with details like value, rationale, and metadata.
tags:
  - mlflow
  - tracing
  - evaluation
timestamp: "2026-06-19T21:57:17.473Z"
---

# Trace Assessments

**Trace Assessments** are quality evaluations attached to [Trace](/concepts/traces.md) objects or individual Span objects in MLflow. They represent ratings, feedback, or expectation checks (e.g., helpfulness scores, correctness evaluations) that can be collected from human annotators, automated judges, or external systems. Assessments are stored as part of the trace metadata and can be retrieved and filtered programmatically. ^[access-trace-data-databricks-on-aws.md]

## Retrieving Assessments

Assessments are accessed via the `search_assessments()` method on a `Trace` object. This method returns a list of assessment objects, which can be filtered by name, type, span ID, or a combination of criteria. By default, only active (non-overridden) assessments are returned; passing `all=True` includes overridden assessments as well. ^[access-trace-data-databricks-on-aws.md]

```python
# Get all assessments on a trace
all_assessments = trace.search_assessments()
```

Assessments are also available directly on the `TraceInfo` object via the `assessments` property, which provides a list of all assessments attached to that trace. ^[access-trace-data-databricks-on-aws.md]

## Filtering Assessments

The `search_assessments()` method supports several filter parameters: ^[access-trace-data-databricks-on-aws.md]

- **`name`** – Filter by the assessment name (e.g., `"helpfulness"`).
- **`type`** – Filter by assessment type: `"feedback"` or `"expectation"`.
- **`span_id`** – Filter to only assessments attached to a specific span.
- **`all`** – When set to `True`, returns assessments that have been overridden or invalidated.

Multiple filter parameters can be combined. For example, to find only human feedback assessments with the name `"helpfulness"`: ^[access-trace-data-databricks-on-aws.md]

```python
human_feedback = trace.search_assessments(
    type="feedback",
    name="helpfulness"
)
```

## Assessment Properties

Each assessment object exposes the following properties: ^[access-trace-data-databricks-on-aws.md]

| Property     | Description |
|--------------|-------------|
| `name`       | The name of the assessment (e.g., `"helpfulness"`, `"correctness"`). |
| `value`      | The assessment value (e.g., a score, boolean, or categorical label). |
| `source`     | A `Source` object containing `source_type` (e.g., `"HUMAN"`, `"AUTOMATED"`) and `source_id`. |
| `rationale`  | Optional textual explanation for the assessment. |
| `metadata`   | Optional dictionary of additional metadata. |
| `error`      | Optional error message if the assessment generation failed. |
| `span_id`    | The ID of the span this assessment is attached to, if any. |

```python
for assessment in trace.search_assessments():
    print(f"Name: {assessment.name}")
    print(f"Value: {assessment.value}")
    print(f"Source: {assessment.source.source_type} - {assessment.source.source_id}")
    if assessment.rationale:
        print(f"Rationale: {assessment.rationale}")
```

## Working with Assessment Details

To examine all assessments on a trace, including those not returned by the default filter, iterate over `trace.info.assessments`. This property gives access to the complete list of assessment objects with all their attributes. ^[access-trace-data-databricks-on-aws.md]

```python
for assessment in trace.info.assessments:
    print(f"{assessment.name}: {assessment.value}")
    if assessment.span_id:
        print(f"  Attached to span: {assessment.span_id}")
```

Assessments can be used to compare different agent configurations, monitor quality over time, or surface problematic traces for further investigation.

## Related Concepts

- [Trace](/concepts/traces.md) – The execution record that contains assessments.
- Span – Individual units of work within a trace that can carry assessments.
- [TraceInfo](/concepts/traceinfo.md) – Metadata object that exposes the `assessments` property.
- Feedback Assessments – Assessments of type `"feedback"` from human or automated sources.
- [Expectation Assessments](/concepts/feedback-vs-expectation-assessment-types.md) – Assessments of type `"expectation"` evaluating whether predefined criteria were met.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using assessments to compare different agent versions.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Real-time assessment collection in deployed applications.

## Sources

- access-trace-data-databricks-on-aws.md

# Citations

1. [access-trace-data-databricks-on-aws.md](/references/access-trace-data-databricks-on-aws-0c458734.md)
