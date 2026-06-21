---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 13b536669b5e1111cc4f02092cfa6ac96e75dc882c55aec81f78eb765b60a722
  pageDirectory: concepts
  sources:
    - collect-user-feedback-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-tracing-production-package
    - MPP
  citations:
    - file: collect-user-feedback-databricks-on-aws.md
title: mlflow-tracing Production Package
description: A lightweight, optimized pip package for production deployments of MLflow tracing, distinct from the development package and required for feedback collection in MLflow 3.
tags:
  - mlflow
  - tracing
  - production
  - installation
timestamp: "2026-06-19T09:17:01.415Z"
---

# mlflow-tracing Production Package

The **mlflow-tracing production package** is a lightweight, optimized installation of MLflow designed for production deployment of GenAI applications. It provides tracing, feedback collection, and monitoring capabilities with minimal dependencies and improved performance characteristics compared to the full MLflow development package.^[collect-user-feedback-databricks-on-aws.md]

## Overview

The `mlflow-tracing` package is specifically engineered for production use cases where performance, minimal footprint, and reliability are critical. It is installed via pip as a separate package from the full MLflow SDK:^[collect-user-feedback-databricks-on-aws.md]

```bash
pip install --upgrade mlflow-tracing
```

This package is optimized for production environments with reduced dependency overhead and better runtime performance. It supports all essential production tracing features, including trace creation, span management, and feedback collection.^[collect-user-feedback-databricks-on-aws.md]

## Key Features

### Tracing Capabilities

The package enables full tracing of GenAI application requests, allowing you to capture and analyze the complete lifecycle of each interaction, including LLM calls, tool invocations, and retrieval operations. Traces are persisted and can be queried for analysis and monitoring.^[collect-user-feedback-databricks-on-aws.md]

### Feedback Collection

The `log_feedback` API is available in the `mlflow-tracing` package, enabling production feedback collection from end users. This allows you to capture real-world quality signals by linking user feedback to specific traces. The API supports multiple feedback types including boolean (thumbs up/down), numeric ratings, text comments, and structured data.^[collect-user-feedback-databricks-on-aws.md]

### Assessment System

Feedback is stored as assessments on traces using the **Feedback** entity. Each assessment can include:^[collect-user-feedback-databricks-on-aws.md]

- **Value**: The actual feedback (boolean, numeric, text, or structured data)
- **Source**: Information about who or what provided the feedback (human user, LLM judge, or code)
- **Rationale**: Optional explanation for the feedback
- **Metadata**: Additional context like timestamps or custom attributes

## Comparison with Full MLflow Package

| Aspect | mlflow-tracing | Full MLflow (mlflow) |
|--------|----------------|---------------------|
| Use case | Production deployment | Development and experimentation |
| Dependencies | Minimal | Full SDK dependencies |
| Performance | Optimized for production | General-purpose |
| Tracing | Full support | Full support |
| Feedback API | Available (`log_feedback`) | Available (`log_feedback`) |
| Evaluation | Limited | Full `mlflow.genai.evaluate()` |

^[collect-user-feedback-databricks-on-aws.md]

## Prerequisites

MLflow 3 is required for collecting user feedback. MLflow 2.x is not supported due to performance limitations and missing features essential for production use.^[collect-user-feedback-databricks-on-aws.md]

## Usage in Production

### Basic Tracing

The package supports the same tracing APIs as the full MLflow SDK, including `mlflow.start_span()`, `mlflow.update_current_trace()`, and `mlflow.get_current_active_span()`. This allows you to instrument your production GenAI applications with minimal code changes.^[collect-user-feedback-databricks-on-aws.md]

### Feedback Collection

The `log_feedback` API works identically in both packages, so you can collect user feedback regardless of which installation method you choose. This enables a consistent feedback collection pattern across development and production environments.^[collect-user-feedback-databricks-on-aws.md]

```python
import mlflow
from mlflow.entities import AssessmentSource

mlflow.log_feedback(
    trace_id=trace_id,
    name="user_feedback",
    value=True,  # thumbs up
    source=AssessmentSource(
        source_type="HUMAN",
        source_id="user123"
    ),
    rationale="Great response!"
)
```

### Querying Traces

The package supports trace retrieval and analysis using the `MlflowClient`:^[collect-user-feedback-databricks-on-aws.md]

```python
from mlflow.client import MlflowClient

client = MlflowClient()
traces = client.search_traces(
    experiment_names=["/Shared/production-genai-app"],
    filter_string="trace.timestamp_ms > 1700000000000"
)
```

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The core tracing framework for GenAI applications
- Feedback (MLflow) — The structured feedback entity for assessments
- [Production Monitoring](/concepts/production-monitoring.md) — Monitoring quality metrics in production
- [Code-based Scorers](/concepts/code-based-scorers.md) — Custom evaluation functions for GenAI
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The evaluation API for development assessment
- [Accessing Databricks secrets in scorers](/concepts/accessing-databricks-secrets-in-scorers.md) — Secure secret retrieval for production scorers

## Sources

- collect-user-feedback-databricks-on-aws.md

# Citations

1. [collect-user-feedback-databricks-on-aws.md](/references/collect-user-feedback-databricks-on-aws-0b0ba83c.md)
