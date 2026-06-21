---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c48c1233a3926f3980fd480c88ff048aca542aaffdf58e2f6524629f5cd4d8a8
  pageDirectory: concepts
  sources:
    - monitor-genai-apps-in-production-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-llm-judges
    - GLJ
    - Guidelines judges
  citations:
    - file: monitor-genai-apps-in-production-databricks-on-aws.md
title: Guidelines LLM Judges
description: Pass/fail natural language criteria judges that evaluate whether inputs and outputs comply with specified guidelines, configurable with Databricks-hosted or custom model endpoints.
tags:
  - mlflow
  - judges
  - guidelines
  - evaluation
timestamp: "2026-06-19T19:46:34.381Z"
---

# Guidelines LLM Judges

**Guidelines LLM Judges** are a type of [LLM Judge](/concepts/llm-judges.md) used in [MLflow](/concepts/mlflow.md) production monitoring that evaluate inputs and outputs against pass/fail natural language criteria. They provide a simple, rule-based approach to quality assessment by checking whether a response satisfies specified guidelines. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Overview

Guidelines LLM Judges are designed for straightforward quality checks where the evaluation criteria can be expressed as clear, binary conditions. Unlike [Custom Prompt LLM Judges](/concepts/custom-llm-judges.md) which support multi-level quality assessment with customizable choice categories, Guidelines judges use a simple pass/fail evaluation model based on natural language rules. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Usage

To use a Guidelines LLM Judge, create a `Guidelines` scorer instance with a name and a list of guideline strings, then register and start it with a sampling configuration. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Guidelines

# Create and register the guidelines scorer
english_judge = Guidelines(
  name="english",
  guidelines=["The response must be in English"]
).register(name="is_english")  # name must be unique to experiment

# Start monitoring with the specified sample rate
english_judge = english_judge.start(sampling_config=ScorerSamplingConfig(sample_rate=0.7))
```

## Custom Model Selection

By default, each judge uses a Databricks-hosted LLM designed to perform GenAI quality assessments. You can change the judge model to instead use a [Databricks Model Serving](/concepts/databricks-model-serving.md) endpoint by using the `model` argument. The model must be specified in the format `databricks:/<databricks-serving-endpoint-name>`. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

```python
english_judge = Guidelines(
  name="english",
  guidelines=["The response must be in English"],
  model="databricks:/databricks-gpt-oss-20b",
).register(name="custom_is_english")
```

## Key Characteristics

- **Pass/Fail Evaluation**: Guidelines judges evaluate inputs and outputs against natural language criteria, returning a binary pass/fail result. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Natural Language Criteria**: Guidelines are expressed as plain text rules, making them easy to define and understand without complex configuration. ^[monitor-genai-apps-in-production-databricks-on-aws.md]
- **Simple Quality Checks**: Best suited for straightforward quality assessments where the evaluation criteria are clear and unambiguous. ^[monitor-genai-apps-in-production-databricks-on-aws.md]

## Related Concepts

- [LLM Judges](/concepts/llm-judges.md) — The broader category of AI-powered quality assessment tools
- [Custom Prompt LLM Judges](/concepts/custom-llm-judges.md) — More flexible judges with multi-level quality assessment
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Pre-configured judges for common quality dimensions
- [Production Monitoring](/concepts/production-monitoring.md) — The system that runs scorers on production traces
- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) — Overview of all scorer types available in MLflow
- [Scorer Sampling Configuration](/concepts/scorer-sampling-configuration.md) — Controls for sampling rate and trace filtering

## Sources

- monitor-genai-apps-in-production-databricks-on-aws.md

# Citations

1. [monitor-genai-apps-in-production-databricks-on-aws.md](/references/monitor-genai-apps-in-production-databricks-on-aws-41428693.md)
