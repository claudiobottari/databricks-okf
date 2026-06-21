---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37cf7828530e13a6947edcfc99da7b7f47412475b03ae01d207beba82bc66378
  pageDirectory: concepts
  sources:
    - tracing-mistral-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - mlflow-autologging
    - MLflow Auto Logging
    - MLflow Autolog API
    - MLflow Automatic Logging
    - MLflow Logging
    - MLflow automatic logging
    - MLflow logging
    - Autolog
    - Autologging
    - MLflow Autolog
    - MLflow Automatic Logging (autolog)
    - MLflow autolog
    - MLflow automatic logging documentation
    - autolog
    - autologging
    - mlflow.autolog
    - mlflow.autolog()
  citations:
    - file: tracing-mistral-databricks-on-aws.md
title: MLflow Autologging
description: A framework feature that automatically logs ML model parameters, metrics, and artifacts from supported libraries without requiring explicit logging calls in user code.
tags:
  - mlflow
  - machine-learning
  - logging
  - observability
timestamp: "2026-06-19T23:12:40.594Z"
---

# [MLflow](/concepts/mlflow.md) Autologging

**MLflow Autologging** is a feature within [MLflow](/concepts/mlflow.md) that automatically captures and logs model training metadata, including parameters, metrics, and model artifacts, without requiring manual instrumentation. It provides a convenient way to enable [experiment tracking](/concepts/mlflow-experiment-tracking.md) and model monitoring for machine learning workflows.

## Overview

[MLflow](/concepts/mlflow.md) Autologging operates by automatically instrumenting supported machine learning frameworks and libraries. When activated, it captures training parameters, performance metrics, and model outputs during each training run, storing them in the configured [MLflow Tracking Server](/concepts/remote-mlflow-tracking-server.md). This reduces the need for manual logging code and ensures comprehensive tracking of experiments. ^tracing-mistral-databricks-on-aws.md

## Supported Integrations

[MLflow](/concepts/mlflow.md) provides autologging support for various machine learning frameworks and providers. Key integrations include:

- **OpenAI**: Track GPT model training and inference
- **Anthropic**: Monitor Claude model experiments
- **Mistral AI**: Capture Mistral model metrics and parameters
- **LangChain**: Track LangChain workflow execution
- **LlamaIndex**: Monitor LlamaIndex operations
- **Amazon Bedrock**: Track Bedrock model usage

Each integration is invoked through a dedicated autolog function, such as `mlflow.openai.autolog()` or `mlflow.mistral.autolog()`. ^[tracing-mistral-databricks-on-aws.md]

## Usage

### Basic Setup

To enable autologging for a supported provider:

```python
import [[mlflow|MLflow]]

# Enable autologging for Mistral AI
[[mlflow|MLflow]].mistral.autolog()

# Configure [[mlflow-tracking|MLflow Tracking]]
[[mlflow|MLflow]].set_tracking_uri("databricks")
[[mlflow|MLflow]].set_experiment("/Shared/mistral-demo")
```

Once autologging is enabled, subsequent calls to the provider's API automatically generate [MLflow runs](/concepts/mlflow-run.md) with captured data. ^[tracing-mistral-databricks-on-aws.md]

### Provider Configuration

Before using autologging, configure the API key for the respective provider:

```python
from mistralai import Mistral
client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
```

The client initiates requests that [MLflow](/concepts/mlflow.md) automatically [Traces](/concepts/traces.md) when autologging is active. ^[tracing-mistral-databricks-on-aws.md]

## Benefits

- **Reduced Boilerplate**: Eliminates need for manual logging code
- **Comprehensive Tracking**: Captures all relevant training metadata
- **Consistent Logging**: Standardizes experiment tracking across workflows
- **Real-time Monitoring**: Enables live observation of training progress

## Related Concepts

- [MLflow Tracking](/concepts/mlflow-tracking.md)
- Experiment Management
- [Model Registry](/concepts/mlflow-model-registry.md)
- [MLflow Projects](/concepts/mlflow-projects.md)
- Model Monitoring

## Sources

- tracing-mistral-databricks-on-aws.md

# Citations

1. [tracing-mistral-databricks-on-aws.md](/references/tracing-mistral-databricks-on-aws-6af10854.md)
