---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c0556f8d26ae8e25884a24e2346ba8c4d639b4e2d69c11976b59efe5cd3e6cd0
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-inputoutput-parsing-for-evaluation
    - AIPFE
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Automatic Input/Output Parsing for Evaluation
description: How the Guidelines judge automatically extracts request and response fields from traces, supporting OpenAI-format messages, ChatCompletion objects, and arbitrary dicts.
tags:
  - mlflow
  - data-parsing
  - evalution
timestamp: "2026-06-19T17:56:28.849Z"
---

# Automatic Input/Output Parsing for Evaluation

**Automatic Input/Output Parsing for Evaluation** refers to the mechanism by which MLflow's built-in LLM judges, such as the `Guidelines()` judge, automatically extract `request` and `response` fields from evaluation data to construct the context used for scoring. This eliminates the need for users to manually map their data structures when running evaluations.

## Overview

When using built-in LLM judges like `Guidelines()`, MLflow automatically parses the provided `inputs` and `outputs` from the evaluation dataset or trace. The judge then creates a context dictionary with two keys: `request` (representing the app's input) and `response` (representing the app's output). Users can reference these keys directly by name in their scoring criteria. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

This automatic parsing works for both offline evaluation and production monitoring scenarios. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Request Parsing Behavior

MLflow extracts the `request` field from the provided `inputs` using the following rules:

- If `inputs` contains a `messages` key with an array of OpenAI format chat messages:
  - If there is a **single message**, `request` is that message's `content`.
  - If there is **more than one message**, `request` is the entire messages array serialized to a JSON string.
- Otherwise, `request` is the entire `inputs` dictionary serialized to a JSON string.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Request Examples

**Single message input:**

```python
inputs = {
    "messages": [
        {"role": "user", "content": "How can I reset my password?"}
    ]
}
# Parsed request: "How can I reset my password?"
```

**Multi-turn conversation:**

```python
inputs = {
    "messages": [
        {"role": "user", "content": "What is MLflow?"},
        {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."},
        {"role": "user", "content": "Tell me more about tracing"}
    ]
}
# Parsed request: '[{"role": "user", "content": "What is MLflow?"}, ...]'
```

**Arbitrary dictionary:**

```python
inputs = {"key1": "Explain MLflow evaluation", "key2": "something else"}
# Parsed request: '{"key1": "Explain MLflow evaluation", "key2": "something else"}'
```

## Response Parsing Behavior

MLflow extracts the `response` field from the provided `outputs` using the following rules:

- If `outputs` contains an OpenAI format ChatCompletion object, `response` is the first choice's `content`.
- If `outputs` contains a `messages` key with an array of OpenAI format chat messages, `response` is the last message's `content`.
- Otherwise, `response` is the `outputs` serialized to a JSON string.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Response Examples

**ChatCompletion output:**

```python
outputs = {
    "choices": [{
        "message": {
            "content": "MLflow evaluation helps measure GenAI quality..."
        }
    }]
}
# Parsed response: "MLflow evaluation helps measure GenAI quality..."
```

**Messages format output:**

```python
outputs = {
    "messages": [
        {"role": "user", "content": "What are the ..."},
        {"role": "assistant", "content": "Here are the key features..."}
    ]
}
# Parsed response: "Here are the key features..."
```

**Arbitrary dictionary:**

```python
outputs = {"key1": "some value", "key2": "another value"}
# Parsed response: '{"key1": "some value", "key2": "another value"}'
```

## Context Variables in Guidelines

The automatically parsed `request` and `response` keys can be referenced directly in guidelines. For example:

```python
guideline = "The response must maintain a courteous, respectful tone throughout."
```

The judge also includes additional context variables from the evaluation data, such as `retrieved_documents` or `user_preferences`, which can be referenced in the same way. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Relevance to Built-in Judges

The automatic input/output parsing is specifically used by **built-in guidelines judges**:

- **`Guidelines()` judge** — Applies global guidelines uniformly to all rows across both offline evaluation and production monitoring. Evaluates app inputs and outputs only. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **`ExpectationsGuidelines()` judge** — Applies per-row guidelines labeled by domain experts in an evaluation dataset. For offline evaluation only. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

For custom judges, users may need to define their own parsing logic. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Judge](/concepts/llm-judges.md) — The scoring mechanism that uses LLMs to evaluate GenAI outputs.
- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) — A type of judge that uses pass/fail natural language criteria.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The MLflow framework for evaluating GenAI applications.
- [Production Monitoring](/concepts/production-monitoring.md) — Ongoing evaluation of deployed models, supported by automatic parsing.
- Offline Evaluation — Evaluation using pre-collected datasets.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
