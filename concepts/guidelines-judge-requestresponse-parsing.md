---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: acdcb5e9346f2002bfefb5eb6004cca21e06bca208565b1796eb79baa2d9c74e
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-judge-requestresponse-parsing
    - GJRP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guidelines Judge Request/Response Parsing
description: The automatic extraction rules by which the Guidelines judge parses inputs and outputs into request and response context variables from OpenAI-format traces or arbitrary dicts.
tags:
  - mlflow
  - parsing
  - trace-data
timestamp: "2026-06-18T11:13:50.758Z"
---

#Guidelines Judge Request/Response Parsing

**Guidelines Judge Request/Response Parsing** refers to the automatic extraction of `request` and `response` context variables from evaluation data by the [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) and the [ExpectationsGuidelines](/concepts/expectationsguidelines-judge-per-row-guidelines.md) judge. These context variables are the two keys made available for writing natural-language guidelines. The judge populates them by parsing the `inputs` and `outputs` fields of each row in the evaluation dataset or trace in production monitoring.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## How the `request` Field Is Parsed

The `request` field is extracted from the `inputs` dictionary provided for each evaluation row. The parsing logic depends on the structure of `inputs`:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **If `inputs` contains a `messages` key with an array of OpenAI-format chat messages** (as used by [Chat Completion API](/concepts/chat-completions-api.md)):
  - If the array contains a **single message**, `request` is set to the `content` of that message.
  - If the array contains **more than one message** (multi-turn conversation), `request` is the entire `messages` array serialized to a JSON string.
- **Otherwise**, `request` is the entire `inputs` dictionary serialized to a JSON string.

## How the `response` Field Is Parsed

The `response` field is extracted from the `outputs` field of each evaluation row. The parsing logic is:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **If `outputs` contains an OpenAI-format `ChatCompletion` object** (with a `choices` array):
  - `response` is the `content` of the first choice's message.
- **If `outputs` contains a `messages` key** with an array of OpenAI-format chat messages:
  - `response` is the `content` of the **last** message in the array.
- **Otherwise**, `response` is the entire `outputs` dictionary serialized to a JSON string.

## Examples

### Single Message Input

```python
inputs = {
    "messages": [
        {"role": "user", "content": "How can I reset my password?"}
    ]
}
# Parsed request: "How can I reset my password?"
```

### Multi-Turn Conversation

```python
inputs = {
    "messages": [
        {"role": "user", "content": "What is MLflow?"},
        {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."},
        {"role": "user", "content": "Tell me more about tracing"}
    ]
}
# Parsed request: '[{"role": "user", "content": "What is MLflow?"}, {"role": "assistant", "content": "MLflow is an open source AI engineering platform..."}, {"role": "user", "content": "Tell me more about tracing"}]'
```

### Arbitrary Dict Input

```python
inputs = {"key1": "Explain MLflow evaluation", "key2": "something else"}
# Parsed request: '{"key1": "Explain MLflow evaluation", "key2": "something else"}'
```

### ChatCompletion Output

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

### Messages Format Output

```python
outputs = {
    "messages": [
        {"role": "user", "content": "What are the ..."},
        {"role": "assistant", "content": "Here are the key features..."}
    ]
}
# Parsed response: "Here are the key features..."
```

### Arbitrary Dict Output

```python
outputs = {"result": "success", "value": 42}
# Parsed response: '{"result": "success", "value": 42}'
```

## Using `request` and `response` in Guidelines

Once parsed, the `request` and `response` variables can be referenced directly in guideline text. For example:

```python
guideline = "The response must be in the same language as the request"
```

The judge evaluates the guideline against the provided context, which always contains `request` and `response`. Additional keys from the context dictionary (e.g., `retrieved_documents`, `user_preferences`) can also be referenced if they are present.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Relevant Judges

- [Guidelines() Judge (Global Guidelines)](/concepts/guidelines-judge-global-guidelines.md) — Applies uniform guidelines to all rows; uses the same parsing logic.
- [ExpectationsGuidelines() Judge (Per-Row Guidelines)](/concepts/expectationsguidelines-judge-per-row-guidelines.md) — Evaluates against row-specific guidelines from an `expectations` field; also uses this parsing logic for `request` and `response`.

## Next Steps

- Guidelines LLM Judge — Overview and Best Practices
- Custom Judges vs. Guidelines Judges
- [Production Monitoring for GenAI Applications](/concepts/production-monitoring-for-genai-applications.md)

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
