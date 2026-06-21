---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c8e93c5c10f49756abbc9ac203a153b66637cc22f9159056082638325eb2a35
  pageDirectory: concepts
  sources:
    - examples-analyzing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-assessments-and-feedback-logging
    - Feedback Logging and Trace Assessments
    - TAAFL
  citations:
    - file: examples-analyzing-traces-databricks-on-aws.md
title: Trace Assessments and Feedback Logging
description: Pattern for attaching human feedback, LLM judge evaluations, ground truth expectations, and span-specific assessments to traces using mlflow.log_feedback() and mlflow.log_expectation().
tags:
  - mlflow
  - tracing
  - evaluation
  - feedback
timestamp: "2026-06-19T18:44:42.197Z"
---

```markdown
---
title: Trace assessments and feedback logging
summary: Method for attaching human feedback, LLM judge evaluations, ground truth expectations, and span-specific assessments to MLflow traces using log_feedback() and log_expectation().
sources:
  - examples-analyzing-traces-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T12:14:30.779Z"
updatedAt: "2026-06-18T12:14:30.779Z"
tags:
  - mlflow
  - feedback
  - evaluation
  - genai-tracing
aliases:
  - trace-assessments-and-feedback-logging
  - feedback logging and Trace assessments
  - TAAFL
confidence: 0.98
provenanceState: extracted
inferredParagraphs: 0
---

# Trace Assessments and Feedback Logging

**Trace assessments and feedback logging** refers to the practice of attaching structured evaluations, human annotations, and expected outcomes to [[MLflow Trace|MLflow Traces]] for the purpose of monitoring, debugging, and improving GenAI agent performance. Assessments provide a mechanism to record quality signals directly on traces and their constituent spans, enabling both offline analysis and continuous production monitoring.

## Overview

Assessments are metadata that capture judgments about a trace's quality or correctness. They can originate from multiple sources — human reviewers, LLM-based judges, automated code, or ground-truth expectations — and can be attached at the trace level or to individual spans. ^[examples-analyzing-traces-databricks-on-aws.md]

By logging assessments to traces, teams can build a historical record of agent behavior, correlate performance with specific configurations, and identify regressions over time.

## Types of Assessments

### Human Feedback

Human feedback captures ratings, scores, or qualitative judgments provided by people reviewing agent outputs. Each feedback entry includes a name, a value (numeric or categorical), a source identifier (e.g., the reviewer's email), and an optional rationale. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="helpfulness",
    value=4,
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="reviewer_alice@company.com"
    ),
    rationale="Clear and accurate response with good context usage"
)
```

### LLM Judge Assessments

LLM judge assessments are scores produced by an automated evaluator (e.g., GPT-4, a custom [[Custom Judges|judge]]). These typically include a score value and may reference the evaluation prompt or model version used. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="relevance_score",
    value=0.92,
    source=AssessmentSource(
        source_type=AssessmentSourceType.LLM_JUDGE,
        source_id="gpt-4-evaluator"
    ),
    metadata={"evaluation_prompt_version": "v2.1"}
)
```

### Ground Truth Expectations

Expectations define the known-correct answer or behavior for a given input. They serve as a reference for evaluating whether the agent's actual output matches what was expected. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
mlflow.log_expectation(
    trace_id=trace_id,
    name="expected_facts",
    value=["observability", "spans", "GenAI applications"],
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="subject_matter_expert"
    )
)
```

### Span-Level Feedback

Assessments can be scoped to a specific span rather than the entire trace. This enables granular quality tracking — for example, evaluating the quality of a retrieval step or the correctness of a specific tool call. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
retriever_span = trace.search_spans(name="retrieve_documents")[0]
mlflow.log_feedback(
    trace_id=trace_id,
    span_id=retriever_span.span_id,
    name="retrieval_quality",
    value="excellent",
    source=AssessmentSource(
        source_type=AssessmentSourceType.CODE,
        source_id="retrieval_evaluator.py"
    )
)
```

## Retrieving and Analyzing Assessments

### Searching Assessments on a Trace

Use `trace.search_assessments()` to retrieve all assessments attached to a trace. Results can be grouped by source type (``HUMAN``, ``LLM_JUDGE``, ``CODE``) for aggregated analysis. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
assessments = trace.search_assessments()

# Group by source type
by_source = {}
for assessment in assessments:
    source_type = assessment.source.source_type
    if source_type not in by_source:
        by_source[source_type] = []
    by_source[source_type].append(assessment)
```

### Checking for Assessment Errors

Assessments that encountered errors during logging can be identified by checking the `error` field. This is useful for monitoring the health of evaluation pipelines. ^[examples-analyzing-traces-databricks-on-aws.md]

```python
for assessment in trace.info.assessments:
    if assessment.error:
        print(f"Assessment error: {assessment.error}")
```

## Best Practices

- **Log assessments immediately after trace execution.** Up-to-date assessments provide the most accurate picture for real-time monitoring dashboards. ^[examples-analyzing-traces-databricks-on-aws.md]
- **Use consistent naming conventions.** Assessment names like `"helpfulness"`, `"relevance_score"`, and `"retrieval_quality"` make cross-trace aggregation straightforward.
- **Include source metadata.** Recording the evaluator identity, prompt version, or scoring rubric (via the `source` and `metadata` fields) enables traceability and debugging when assessment values change over time.
- **Attach span-level assessments for granular debugging.** A trace may pass overall quality checks while an individual span (e.g., a retrieval step) fails. Span-level assessments isolate the issue.
- **Combine expectations with live feedback.** Expectations define the ideal answer; live feedback captures real-world user perception. Comparing the two reveals gaps between intended and actual performance.

## Related Concepts

- [[MLflow Trace|MLflow Traces]] — The execution records to which assessments are attached
- [[Custom Judges]] — Automated LLM-based evaluators that produce assessment values
- [[A/B Comparison of Agent Configurations]] — Comparing assessment scores across agent variants
- [[MLflow Trace-based Evaluation|Trace-Based Evaluation]] — Using execution traces for deeper quality analysis
- [[Production Quality Monitoring (MLflow GenAI)|Production Monitoring for GenAI]] — Deploying assessments for continuous quality monitoring
- Build Eval Datasets from Traces — Converting trace data into evaluation datasets

## Sources

- examples-analyzing-traces-databricks-on-aws.md
```

# Citations

1. [examples-analyzing-traces-databricks-on-aws.md](/references/examples-analyzing-traces-databricks-on-aws-ebc17f1a.md)
