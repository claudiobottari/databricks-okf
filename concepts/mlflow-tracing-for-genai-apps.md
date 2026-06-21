---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: ff447f85fa898083094e894305a53062e9f911dd481fc3041a1679a97b8093b6
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-for-genai-apps
    - MTFGA
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Tracing for GenAI Apps
description: Automatic instrumentation of GenAI applications using MLflow's @mlflow.trace decorator and mlflow.openai.autolog() to capture and visualize traces of LLM calls and retrieval steps.
tags:
  - mlflow
  - tracing
  - observability
  - genai
timestamp: "2026-06-19T08:45:58.062Z"
---

Here is a wiki page for "[MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Apps", written based solely on the provided source material.

---

## [MLflow Tracing](/concepts/mlflow-tracing.md) for GenAI Apps

**MLflow Tracing for GenAI Apps** refers to the mechanism within [MLflow](/concepts/mlflow.md) that captures the full execution path of a [GenAI](/concepts/mlflow-genai-evaluate-api.md) application, including calls to large language models (LLMs), retrieval functions, and tool invocations. This capability is fundamental for debugging, evaluating, and monitoring complex agentic workflows. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Overview

[MLflow](/concepts/mlflow.md) provides tracing APIs to instrument GenAI applications. By enabling automatic tracing (e.g., via `mlflow.openai.autolog()`) or by wrapping custom functions with the `@mlflow.trace` decorator, developers can record the inputs, outputs, and metadata of each component in a call chain. Each traced execution is captured as a trace, which is composed of individual spans representing different operations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Key Concepts

- **Trace**: A record of a single end-to-end invocation of an application. A trace contains one or more spans.
- **Span**: A named, timed operation within a trace. For example, an LLM call or a retrieval step can each be a separate span, with child spans for sub-operations.
- **Span Type**: A label that describes the kind of operation a span represents, such as `RETRIEVER` or defaulting to the function name. This aids in filtering and analysis. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Instrumenting an App

#### Automatic Tracing

MLflow can automatically trace calls to certain libraries, such as the OpenAI client. This captures the request and response of LLM calls without manual instrumentation. For example, calling `mlflow.openai.autolog()` enables this behavior for an OpenAI client. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
import mlflow
mlflow.openai.autolog()
```

#### Manual Tracing

Custom functions within the app can be traced using the `@mlflow.trace` decorator. The `span_type` parameter can classify the operation, such as a `RETRIEVER` for a retrieval function. This allows for granular tracking of internal logic. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

```python
@mlflow.trace
def my_chatbot(user_question: str) -> str:
    # Function logic here
    pass

@mlflow.trace(span_type="RETRIEVER")
def retrieve_context(query: str) -> str:
    # Simulated or real retrieval
    pass
```

### Viewing Traces

Once generated, traces are visible in the MLflow UI under the **Logs** tab of an experiment. Each trace can be opened to inspect its individual spans. The trace details dialog shows each span's inputs, outputs, and metadata, providing a detailed view of the application's behavior. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Use Cases for Tracing

#### Debugging
Tracing allows developers to examine the intermediate steps of an agent, making it easier to diagnose incorrect behavior, such as a retrieval failure or a poorly structured prompt. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Collecting Feedback
Traces serve as the basis for collecting human feedback. By logging feedback (e.g., via `mlflow.log_feedback()`), developers can associate user ratings, developer annotations, or expert assessments directly with a specific trace. This provides the context needed to understand why a user was unsatisfied. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Expert Review
Traces can be sent to an expert labeling session for structured review. This is done by creating a labeling session and adding traces to it. Expert reviewers can then assess the quality of the response and provide ideal answers, creating ground truth data. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

#### Evaluation
Expert-labeled traces can be used as an evaluation dataset to assess the application's quality. For example, MLflow's `Correctness` scorer can compare the application's output to the expert-provided `expected_response` to quantitatively measure alignment with expert expectations. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Related Concepts

- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md)
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)
- [Labeling Sessions and Expert Review](/concepts/labeling-sessions-for-expert-review.md)
- [MLflow Experiments](/concepts/mlflow-experiment.md)

### Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
