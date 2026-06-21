---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4104855192262e3239bc9f6bc6e77320fa54c4cb45d45801aee88fa6117ef202
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-genai-applications
    - MTFGA
    - Trace your application
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Tracing for GenAI Applications
description: Instrumenting generative AI applications with MLflow tracing using @mlflow.trace decorators and automatic OpenAI client tracing via mlflow.openai.autolog()
tags:
  - mlflow
  - tracing
  - genai
  - observability
timestamp: "2026-06-19T21:53:26.779Z"
---

Here is the wiki page for "[MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Applications", written based solely on the provided source material.

---

## [MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Applications

**MLflow Tracing for GenAI Applications** is a framework for instrumenting, recording, and inspecting the execution of [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications, including large language models (LLMs), agents, and multi-step pipelines. It provides visibility into the full lifecycle of a GenAI application call — from input prompts through intermediate reasoning steps and tool calls to final outputs — enabling debugging, evaluation, and monitoring.

### Overview

[MLflow Tracing](/concepts/mlflow-tracing.md) automatically captures execution traces from GenAI applications, recording each step of a call as a structured sequence of spans. Each span represents a unit of work — such as an LLM call, a tool invocation, or a custom function — and contains timing, input/output data, and metadata. Traces are stored in the active MLflow experiment and can be queried, visualized, and reused for evaluation without re-running the application. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### How Tracing Works

#### Automatic Instrumentation

MLflow provides automatic instrumentation for popular GenAI libraries via `autolog()` calls. For example, `mlflow.openai.autolog()` automatically wraps OpenAI client calls to capture traces without modifying application code. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
import mlflow
mlflow.openai.autolog()
```

After enabling autolog, every call through the instrumented client is recorded as a trace. This includes the model name, complete message history, response content, and timing information. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Manual Tracing with Decorators

For custom application logic, use the `@mlflow.trace` decorator to instrument specific functions. This is useful for recording intermediate processing steps, custom tool calls, or any application-specific logic that should appear in the trace:

```python
@mlflow.trace
def my_chatbot(user_question: str) -> str:
    context = retrieve_context(user_question)
    response = client.chat.completions.create(
        model="databricks-claude-sonnet-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Context: {context}\n\nQuestion: {user_question}"}
        ],
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].message.content
```

^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

The decorator also accepts a `span_type` parameter to categorize the span, such as `"RETRIEVER"` for retrieval operations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
@mlflow.trace(span_type="RETRIEVER")
def retrieve_context(query: str) -> str:
    # Simulated retrieval logic
    return context
```

### Trace Structure

A trace consists of a root span (the top-level operation) and child spans representing sub-operations. Spans can be nested to arbitrary depth, reflecting the call graph of the application. Each span includes:

- **Name**: A descriptive label for the operation
- **Start and end time**: Precise timing for performance analysis
- **Inputs**: The data provided to the operation
- **Outputs**: The result of the operation
- **Attributes**: Custom key-value metadata
- **Status**: Success or error information

### Developer Workflow with Tracing

[MLflow Tracing](/concepts/mlflow-tracing.md) supports an iterative development workflow where traces are generated once and then reused for multiple rounds of evaluation. This avoids re-running the full application for every change to evaluation metrics.

### Collecting Feedback on Traces

Traces can be augmented with human feedback at multiple levels, enabling a complete feedback loop for GenAI application quality.

#### End-User Feedback

End-user feedback, such as thumbs up/down ratings, can be logged against a specific trace using `mlflow.log_feedback()`. This captures the user's assessment along with a rationale and source identifier. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.entities.assessment import AssessmentSource, AssessmentSourceType

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=False,
    rationale="Missing details about MLflow's key features",
    source=AssessmentSource(
        source_type=AssessmentSourceType.HUMAN,
        source_id="enduser_123",
    ),
)
```

#### Developer Annotations

Developers can add their own feedback and notes directly in the MLflow UI. By opening a trace and selecting a span, developers can create assessments with a name, numeric value, and rationale. These annotations appear as columns in the Logs table after refreshing the page. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Expert Review via Labeling Sessions

For authoritative feedback, traces can be sent to domain experts through labeling sessions. A labeling session defines a schema for the feedback to collect — such as categorical accuracy ratings or free-text ideal responses — and provides a Review App URL for experts to submit their assessments. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText
from mlflow.genai.labeling import create_labeling_session

accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
    overwrite=True
)

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name],
)

traces = mlflow.search_traces(max_results=1)
labeling_session.add_traces(traces)
```

Expert reviewers can then open the Review App URL, see the trace with the question and response, assess accuracy, and submit their expert assessments as ground truth. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Using Feedback for Evaluation

After experts provide feedback, their labels can be used to evaluate the application with MLflow's built-in scorers. For example, the `Correctness` scorer compares the app's outputs against expert-provided `expected_response` labels. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness

labeled_traces = mlflow.search_traces(
    run_id=labeling_session.mlflow_run_id,
)

eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]
)
```

### Visualization

Traces are visualized in the Databricks Notebook Trace UI and the MLflow Experiment UI. The visualizations display the span hierarchy, input/output data, and timing information for each operation. Feedback and assessments are shown in the **Assessments** panel on the right side of the trace details dialog. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Use Cases

#### Debugging and Development

Tracing helps developers understand how their GenAI application processes inputs, identify incorrect tool calls, detect slow operations, and diagnose unexpected behavior. The detailed span structure reveals exactly what the application did at each step. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Human-in-the-Loop Evaluation

Traces serve as the foundation for collecting human feedback at multiple levels — from end-user ratings to developer annotations to expert review sessions — enabling comprehensive quality assessment. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Trace-Based Evaluation

Trace data serves as input to [Code-based Scorers](/concepts/code-based-scorers.md) and [Custom LLM Judges](/concepts/custom-llm-judges.md), enabling evaluation of tool usage patterns, intermediate reasoning, and other aspects of agent behavior that are not visible in final outputs alone.

### Related Concepts

- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation metrics that process trace data
- [Custom LLM Judges](/concepts/custom-llm-judges.md) — LLM-as-a-judge evaluation using traces
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Collecting end-user, developer, and expert feedback on traces
- [Labeling Sessions](/concepts/labeling-sessions.md) — Structured expert review workflows for trace evaluation
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit for storing and managing traces

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
