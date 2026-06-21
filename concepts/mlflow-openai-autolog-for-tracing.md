---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0babec669f9fb49d375b70c9272740013299649473dc2afcd384e82ef9b351f8
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-openai-autolog-for-tracing
    - MOAFT
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow OpenAI Autolog for Tracing
description: Automatic instrumentation of OpenAI client calls via mlflow.openai.autolog() to capture traces without manual instrumentation, enabling trace-based evaluation workflows.
tags:
  - mlflow
  - openai
  - tracing
  - instrumentation
timestamp: "2026-06-18T15:27:47.749Z"
---

# MLflow OpenAI Autolog for Tracing

**MLflow OpenAI Autolog for Tracing** refers to the automatic instrumentation of OpenAI API calls using `mlflow.openai.autolog()`, which enables MLflow to capture and record traces of all OpenAI client interactions without requiring manual instrumentation of each call. This feature simplifies observability for applications that use OpenAI models, making it easier to debug, evaluate, and monitor AI agent behavior.

## Overview

The `mlflow.openai.autolog()` function automatically instruments the OpenAI client to record MLflow traces for every API call made through the client. When enabled, MLflow automatically captures the inputs, outputs, and metadata of OpenAI model invocations without requiring developers to add explicit tracing decorators to each function call. ^[develop-code-based-scorers-databricks-on-aws.md]

This autologging capability is particularly useful for developers building GenAI applications who want to leverage [MLflow Tracing](/concepts/mlflow-tracing.md) for evaluation and debugging without modifying their existing application code.

## Usage

### Basic Setup

To enable OpenAI autologging, call `mlflow.openai.autolog()` before making any OpenAI API calls: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
import mlflow

# Enable automatic tracing of OpenAI calls
mlflow.openai.autolog()

# Create an OpenAI client
client = DatabricksOpenAI()

# All subsequent API calls will be automatically traced
response = client.chat.completions.create(
    model="databricks-claude-sonnet-4",
    messages=[{"role": "user", "content": "What is the capital of France?"}]
)
```

### Integration with Databricks-Hosted LLMs

When using the `databricks-openai` package (`DatabricksOpenAI`) to connect to Databricks-hosted foundation models, OpenAI autologging instruments these calls as well, enabling seamless tracing across both standard OpenAI endpoints and Databricks-hosted LLM endpoints. ^[develop-code-based-scorers-databricks-on-aws.md]

### Prerequisites

To use MLflow OpenAI autologging effectively, ensure you have the latest version of `mlflow[databricks]` installed: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
%pip install -q --upgrade "mlflow[databricks]>=3.1" openai
```

## Key Benefits

### Automatic Trace Capture

When `mlflow.openai.autolog()` is enabled, every OpenAI API call automatically produces a trace that captures: ^[develop-code-based-scorers-databricks-on-aws.md]

- The input messages sent to the model
- The model's response
- Request metadata (model name, parameters, etc.)
- Latency information

These traces are automatically logged to the active [MLflow Experiment](/concepts/mlflow-experiment.md) and appear in both the notebook Trace UI and the MLflow Experiment UI.

### Iterative Scorer Development

The autologged traces serve as input data for [Code-based Scorers](/concepts/code-based-scorers.md) during evaluation. A common development workflow involves: ^[develop-code-based-scorers-databricks-on-aws.md]

1. Running `mlflow.genai.evaluate()` with a placeholder scorer to generate traces from the application
2. Querying the stored traces using `mlflow.search_traces()`
3. Iterating on custom scorers by evaluating against the stored traces without re-running the entire application

This pattern significantly accelerates the development cycle for custom evaluation metrics.

### Seamless Integration with MLflow Evaluation

Autologged traces work directly with MLflow Evaluation for GenAI. The traces become the evaluation dataset for `mlflow.genai.evaluate()`, allowing developers to: ^[develop-code-based-scorers-databricks-on-aws.md]

- Pass stored traces as the `data` parameter to `evaluate()`
- Apply custom scorers to previously generated traces
- Compare different application configurations side-by-side using the same trace data

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing infrastructure that captures execution details
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation metrics that operate on traced data
- MLflow Evaluation for GenAI — The evaluation framework that consumes traces
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The organizational unit where traces are stored
- Databricks Notebooks — Environment where trace visualizations appear in cell results
- [DatabricksHosted Foundation Models](/concepts/databricks-hosted-foundation-models.md) — Models accessible through the OpenAI-compatible interface

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
