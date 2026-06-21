---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 82222980a7e8a863dbd817ad84f571bb42ff87bd68b089401569fecfe62a1d82
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - mlflow-trace-based-evaluation-workflow
    - MTEW
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Trace-Based Evaluation Workflow
description: "End-to-end workflow: instrument GenAI apps with MLflow tracing, collect human feedback on traces, route traces to expert labeling sessions, and use labeled traces for automated evaluation."
tags:
  - mlflow
  - workflow
  - evaluation
  - tracing
timestamp: "2026-06-18T10:34:51.017Z"
---

## MLflow Trace-Based Evaluation Workflow

The **MLflow Trace-Based Evaluation Workflow** is a structured approach to collect and leverage human feedback—from end users, developers, and domain experts—to evaluate and improve the quality of Generative AI (GenAI) applications. By combining [MLflow Tracing](/concepts/mlflow-tracing.md)](mlflow-tracing.md) with feedback logging, annotation, and expert review sessions, teams can systematically assess model outputs and align them with expected behaviour.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Overview

The workflow integrates human judgment at three levels during the development and deployment lifecycle:
- **End‑user feedback** captured through UI elements (e.g., thumbs up/down).
- **Developer annotations** added interactively in the MLflow UI.
- **Expert review sessions** (labeling sessions) that produce ground‑truth assessments.

These human signals are then used with [MLflow Evaluation](mlflow-evaluation.md) scorers—such as the `Correctness` scorer—to produce quantitative metrics that reflect alignment with expert expectations.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Workflow Steps

#### 1. Instrument a GenAI app with tracing

Enable automatic tracing for OpenAI API calls (or other supported providers) and manually trace retrieval or other custom logic using the `@mlflow.trace` decorator. Each invocation produces a trace that records inputs, outputs, and span metadata.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
import mlflow
mlflow.openai.autolog()
@mlflow.trace
def my_chatbot(question: str) -> str:
    context = retrieve_context(question)
    response = client.chat.completions.create(...)
    return response.choices[0].message.content
```

#### 2. Collect end‑user feedback

After generating a response, the application can log feedback from end users via `mlflow.log_feedback()`. Feedback is attached to a specific trace and can include a boolean value (e.g., `False` for thumbs‑down), a rationale, and a source identifier. In production, this would be triggered by UI interactions such as thumbs‑up/thumbs‑down buttons.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,
    rationale="Missing details about key features...",
    source=AssessmentSource(source_type=AssessmentSourceType.HUMAN, source_id="enduser_123")
)
```

#### 3. View feedback in the MLflow UI

The MLflow UI displays traces alongside their assessments. Navigate to the experiment’s **Logs** tab, click a trace, and find the **Assessments** pane. Here, end‑user feedback appears (e.g., `user_feedback: false`) alongside any developer annotations. Columns for assessments also appear in the trace table.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### 4. Add developer annotations

Developers can directly add feedback or scores to a trace in the UI. For example, an `accuracy_score` feedback with a numeric value (0.75) and a textual rationale can be created via the **Add new assessment** button in the span’s **Assessments** tab. This allows iterative annotation during development.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### 5. Create expert review sessions

When end‑user feedback indicates a potential quality issue, domain experts can provide authoritative assessments through a **labeling session**. A labeling session defines one or more label schemas (e.g., categorical accuracy assessment, free‑text expected response) and groups selected traces for structured review.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema
from mlflow.genai.labeling import create_labeling_session

accuracy_schema = create_label_schema(name="response_accuracy", ...)
expected_schema = create_label_schema(name="expected_response", ...)
labeling_session = create_labeling_session(name="quickstart_review",
                                           label_schemas=[accuracy_schema.name, expected_schema.name])
labeling_session.add_traces(traces)
```

Reviewers open the generated URL, view the trace (including end‑user feedback), and submit their expert labels. The session is stored as an [MLflow Run](/concepts/mlflow-run.md), enabling traceability.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### 6. Evaluate using expert feedback

The expert‑provided labels (e.g., `expected_response`) can be used as ground truth to evaluate the application’s outputs. The `Correctness` scorer from `mlflow.genai.scorers` compares the app’s predictions against the expected responses, producing quantitative quality metrics.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness
labeled_traces = mlflow.search_traces(run_id=labeling_session.mlflow_run_id)
eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

This evaluation can be versioned by adding labeled traces to an [MLflow Evaluation Dataset](mlflow-evaluation-datasets.md) for ongoing monitoring and regression testing.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Sources

- [10‑minute demo: Collect human feedback | Databricks on AWS](https://docs.databricks.com/aws/en/mlflow3/genai/getting-started/human-feedback) (ingested 2026‑06‑18) – source file `10-minute-demo-collect-human-feedback-databricks-on-aws.md`

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
