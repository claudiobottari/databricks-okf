---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37ab0bb47c6c36a368fed89a53040fad356518ca122f867aaff5f86b7ac2ed16
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-assessment-and-feedback-api
    - Feedback API and MLflow Assessment
    - MAAFA
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: MLflow Assessment and Feedback API
description: Programmatic API for logging feedback on traces using mlflow.log_feedback() with AssessmentSource and AssessmentSourceType, enabling structured attribution of human evaluations.
tags:
  - mlflow
  - api
  - feedback
  - assessments
timestamp: "2026-06-19T08:45:47.144Z"
---

# MLflow Assessment and Feedback API

The **MLflow Assessment and Feedback API** is a set of tools in [MLflow](/concepts/mlflow.md) that enables developers to collect, manage, and act on human feedback for GenAI applications. It supports end-user ratings, developer annotations, expert labeling sessions, and automated LLM-based judges, all integrated with [MLflow Tracing](/concepts/mlflow-tracing.md). By combining human and automated assessments, teams can evaluate, debug, and improve the quality of their agents and models.

## Key Components

### Assessments

An **assessment** is a piece of feedback (a name, value, and rationale) attached to a trace or span. Assessments can be logged programmatically or via the MLflow UI. They can represent end-user signals (e.g., thumbs up/down), developer scores (e.g., accuracy), or expert expectations. Each assessment carries a source type (`HUMAN`, `SYSTEM`, etc.) and a source ID (e.g., the user ID). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Labeling Sessions

A **labeling session** groups traces for structured expert review. Developers define a schema (categorical feedback or free-text expectations) and invite reviewers through a shareable URL. Reviewers assess each trace against the schema; labels become ground truth that can later be used for evaluation. Labeling sessions are MLflow runs, and their labeled traces can be queried with `mlflow.search_traces()`. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Judges

**Judges** are LLM-based scorers that evaluate agent outputs automatically. They can be built-in (e.g., `Correctness()`) or custom via `make_judge()`. Judges analyze either the input/output pair or the full execution trace (including tool calls). They return structured feedback values such as boolean, categorical, or numeric scores. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Collecting Human Feedback

### End-User Feedback

Instrument your GenAI app to log end-user feedback. For example, when a user clicks thumbs down, call `mlflow.log_feedback()` with the trace ID, a name (e.g., `"user_feedback"`), a boolean value, and rationale. The source type should be `HUMAN` and the source ID should identify the user. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,
    rationale="Missing details about MLflow's key features",
    source=AssessmentSource(source_type=AssessmentSourceType.HUMAN, source_id="enduser_123"),
)
```

### Developer Annotations

Developers can add assessments directly in the MLflow UI. Open a trace, select a span, click **Add new assessment**, and provide a type (Feedback), name, value (e.g., `0.75`), and rationale. This is useful for quick quality checks during development. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expert Review (Labeling Sessions)

To get authoritative ground truth, create a labeling session with custom schemas (e.g., a categorical `response_accuracy` and a text `expected_response`). Add traces to the session, share the URL with domain experts, and collect their assessments. The labeled traces can then be retrieved and used for automated evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Using Feedback for Evaluation

### Correctness Scorer

The `Correctness()` scorer in `mlflow.genai.scorers` compares an agent’s output against an expert-provided `expected_response` label. After a labeling session, search for labeled traces and pass them to `mlflow.genai.evaluate()` with the scorer:

```python
from mlflow.genai.scorers import Correctness
labeled_traces = mlflow.search_traces(run_id=labeling_session.mlflow_run_id)
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

This gives a quantitative measure of alignment with expert expectations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### A/B Comparison with Custom Judges

To compare two agent configurations (e.g., with and without a feature flag), run `mlflow.genai.evaluate()` on each configuration using the same evaluation dataset and the same set of [Custom Judges](/concepts/custom-judges.md). Judges can be input/output-based or trace-based. Trace-based judges include `{{ trace }}` in their instructions to analyze tool calls and reasoning. By comparing score distributions across runs, you can determine which configuration performs better. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Best Practices

- **Align judges with human feedback**: As you gather expert annotations, fine-tune your judges to better reflect human quality assessments. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Use a representative evaluation dataset**: The test cases should cover the range of real-world inputs. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Document configurations**: Record the exact parameters, prompts, and code versions for each configuration. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Control one variable at a time** when performing A/B comparisons. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Custom Judges](/concepts/custom-judges.md)
- make_judge()|Make Judge API
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)
- Human Feedback Alignment
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
