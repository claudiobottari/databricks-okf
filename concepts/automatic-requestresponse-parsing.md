---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 328da86dde1c92088bbf53cb2a91e159ef2256baa0400c71bf44a8866eb5c2a6
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - automatic-requestresponse-parsing
    - ARP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
      start: 71
      end: 88
title: Automatic Request/Response Parsing
description: How the Guidelines judge automatically extracts request and response data from traces, handling OpenAI format messages, ChatCompletions, and arbitrary dicts.
tags:
  - llm-evaluation
  - mlflow
  - implementation
timestamp: "2026-06-19T09:29:10.197Z"
---

# Automatic Request/Response Parsing

**Automatic Request/Response Parsing** is a feature of the built-in [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) that automatically extracts and transforms input and output data from [MLflow](/concepts/mlflow.md) traces into standardized context variables (`request` and `response`) for evaluation. This parsing mechanism allows judges to evaluate [GenAI](/concepts/mlflow-genai-evaluate-api.md) application outputs without requiring manual data mapping. ^[create-a-guidelines-llm-judge-databricks-on-aws.md:71-88]

## Overview

The `Guidelines()` judge automatically parses app inputs and outputs from provided data structures to create the evaluation context. The parsed `request` and `response` fields can then be referenced directly in natural language guidelines. ^[create-a-guidelines-llm-judge-databricks-on-aws.md:71-88]

## Request Parsing

The `request` field is extracted from the provided `inputs` data according to the following rules:

- **Single message**: If `inputs` contains a `messages` key with exactly one message, `request` is that message's `content`.
- **Multi-turn conversation**: If there are multiple messages in a `messages` array, `request` is the entire array serialized to a JSON string.
- **Arbitrary dictionary**: For any other `inputs` structure, `request` is the entire `inputs` dictionary serialized to a JSON string.

### Request Examples

For a single message input, the parser extracts the `content` value directly:
```python
inputs = {
    "messages": [{"role": "user", "content": "How can I reset my password?"}]
}
# Parsed request: "How can I reset my password?"
```

For multi-turn conversations, the parser serializes the entire `messages` array:
```python
inputs = {
    "messages": [
        {"role": "user", "content": "What is MLflow?"},
        {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."},
        {"role": "user", "content": "Tell me more about tracing"}
    ]
}
# Parsed request (JSON string): '[{"role": "user", "content": "What is MLflow?"}, ...]'
```

For arbitrary dictionaries, the parser serializes the entire `inputs` dict to JSON:
```python
inputs = {"key1": "Explain MLflow evaluation", "key2": "something else"}
# Parsed request: '{"key1": "Explain MLflow evaluation", "key2": "something else"}'
```

## Response Parsing

The `response` field is extracted from the provided `outputs` data according to the following rules:

- **ChatCompletion output**: If `outputs` contains an OpenAI format ChatCompletions object, `response` is the first choice's `content`.
- **Messages format output**: If `outputs` contains a `messages` key with an array of OpenAI format chat messages, `response` is the last message's `content`.
- **Arbitrary dictionary**: For other structures, `response` is the `outputs` serialized to a JSON string.

### Response Examples

For a standard ChatCompletion structure:
```python
outputs = {
    "choices": [{
        "message": {"content": "MLflow evaluation helps measure GenAI quality..."}
    }]
}
# Parsed response: "MLflow evaluation helps measure GenAI quality..."
```

## Benefits of Automatic Parsing

The automatic request/response parsing provides several benefits for [GenAI](/concepts/mlflow-genai-evaluate-api.md) evaluation:

- **Simplifies evaluation setup**: No need to manually construct context dictionaries for each evaluation call.
- **Works with standard formats**: Automatically handles common data structures used in LLMs and [GenAI](/concepts/mlflow-genai-evaluate-api.md) applications.
- **Enables direct guideline references**: Allows guidelines to reference `request` and `response` directly in natural language criteria.

## Related Concepts

- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) - The judge type that uses parsed request/response data
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) - The evaluation framework that provides automatic parsing
- [LLM Evaluation](/concepts/llm-as-a-judge-evaluation.md) - Broader context for evaluating language model outputs
- GenAI Monitoring - Production monitoring that uses parsed response data

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md:71-88](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
