---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 445d3a199176fd26a42a169b0822d853ed7c7f685351f4e6253bd648d5dc618b
  pageDirectory: concepts
  sources:
    - get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - databricks-genai-notebook-development
    - DGND
    - Databricks notebook development
    - GenAI App Development
  citations:
    - file: get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md
title: Databricks GenAI notebook development
description: A development workflow pattern where Databricks notebooks serve as the IDE for building GenAI applications with built-in MLflow experiment tracking, auto-linked experiments, and inline trace visualization.
tags:
  - databricks
  - notebook
  - genai
  - development-workflow
timestamp: "2026-06-19T10:44:23.790Z"
---

## Databricks GenAI Notebook Development

**Databricks GenAI notebook development** refers to the practice of building, instrumenting, and evaluating generative AI applications directly within a Databricks notebook, using [MLflow Tracing](/concepts/mlflow-tracing.md) to capture detailed execution traces for observability and debugging. This development workflow is the recommended starting point for teams that want to prototype GenAI apps on the Databricks platform. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Environment Setup

When using a Databricks notebook as the development environment, a default [MLflow Experiment](/concepts/mlflow-experiment.md) is automatically associated with the notebook. This experiment serves as the container for the GenAI application's traces and metadata. To begin, create a new notebook in the Databricks workspace. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

The required packages must be installed:

- `mlflow[databricks]`: The latest version of MLflow provides full tracing capabilities.
- `openai`: Used to call either Databricks-hosted foundation models or OpenAI-hosted models via the OpenAI API client.

After installation, restart the Python kernel with `dbutils.library.restartPython()`. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Instrumenting the Application with Tracing

Two primary mechanisms are used to instrument GenAI apps for tracing: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

- **`mlflow.openai.autolog()`** – Automatic instrumentation that captures the details of calls to the OpenAI SDK without manual code changes.
- **`@mlflow.trace`** – A decorator that wraps any Python function and records its inputs, outputs, and timing. It is typically applied to the application's entry point.

Standard setup steps in a notebook include:

1. Creating an OpenAI client. For Databricks-hosted models, use `DatabricksOpenAI` from `databricks_openai`; for OpenAI-hosted models, use the standard `openai.OpenAI` client with the API key set.
2. Setting the tracking URI to `"databricks"` and specifying an experiment name via `mlflow.set_experiment()`.
3. Enabling `mlflow.openai.autolog()`.
4. Defining the main function with the `@mlflow.trace` decorator.

A typical application sends a chat completion request to an LLM and returns the response. The decorator captures the function's input and output, while the autolog integration captures the underlying API call as a child span. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Viewing Traces

After running the instrumented application, the generated trace appears directly below the notebook cell. To explore it further: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

1. Click the experiments icon on the right sidebar.
2. Click the new window icon next to experiment runs.
3. Navigate to the **Traces** tab.
4. Click on a trace to view its details.

The trace structure consists of a root span (the `@mlflow.trace` function) and a child span (the OpenAI API call). Attributes include model name, token counts, and timing. The trace reveals the inputs, outputs, and performance metrics such as latency and token usage. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

For more complex applications—such as retrieval-augmented generation (RAG) systems or multi-step agents—MLflow tracing provides deeper visibility into each component's behavior. ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

### Next Steps

After completing a basic trace, developers are directed to more advanced resources: ^[get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md]

- MLflow Tracing Guide for in-depth learning about tracing concepts and configuration.
- [MLflow Tracing Integrations](/concepts/mlflow-tracing-integrations.md) for over 20 libraries with automatic tracing support.
- [Tracing Concepts](/concepts/mlflow-tracing-concepts-and-workflow.md) to understand the fundamentals of spans, attributes, and trace trees.

### Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [MLflow Experiment](/concepts/mlflow-experiment.md)
- [Autolog](/concepts/mlflow-autologging.md)
- [@mlflow.trace decorator](/concepts/mlflowtrace-decorator.md)
- [Foundation Model APIs](/concepts/foundation-model-apis.md)
- GenAI Agent Development
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md)

### Sources

- get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md

# Citations

1. [get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws.md](/references/get-started-mlflow-tracing-for-genai-databricks-notebook-databricks-on-aws-860f2761.md)
