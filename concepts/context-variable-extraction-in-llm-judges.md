---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc8b1349c1dd71abf84619810cfae717a61896d071342928491a2a0531b7e59f
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - context-variable-extraction-in-llm-judges
    - CVEILJ
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Context Variable Extraction in LLM Judges
description: The Guidelines judge automatically parses trace inputs and outputs into `request` and `response` context keys, handling OpenAI-format messages, ChatCompletion objects, and arbitrary dicts with specific extraction rules.
tags:
  - mlflow
  - llm-evaluation
  - data-pipeline
timestamp: "2026-06-19T14:29:57.883Z"
---

# Context Variable Extraction in LLM Judges

**Context Variable Extraction in LLM Judges** refers to the process by which LLM-based judges automatically parse evaluation data — including application inputs, outputs, and execution traces — to create a structured context dictionary. This context is then used by the judge to evaluate whether a GenAI application meets specified criteria.

## Overview

When an LLM judge evaluates a GenAI agent or application, it needs access to the relevant interaction data. Rather than requiring users to manually format all data, judges extract common context variables from standard evaluation dataset fields and execution traces. These variables can be referenced by name directly in the judge’s evaluation criteria (guidelines or instructions).^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Types of Context Variables

### `request` and `response` (Guidelines judges)

The `Guidelines` judge and `ExpectationsGuidelines` judge automatically build a context dictionary with two keys: `request` and `response`. These are extracted from the `inputs` and `outputs` fields of the evaluation data.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

#### Request extraction

The `request` field is extracted from the `inputs` value:

- If `inputs` contains a `messages` key with an array of [OpenAI-format chat messages](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages), then:
  - With a single message, `request` is that message’s `content`.
  - With multiple messages, `request` is the entire messages array serialized to a JSON string.
- Otherwise, `request` is the entire `inputs` dict serialized to a JSON string.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

#### Response extraction

The `response` field is extracted from the `outputs` value:

- If `outputs` contains an OpenAI-format [ChatCompletion](https://platform.openai.com/docs/api-reference/chat/object) object, `response` is the first choice’s `content`.
- If `outputs` contains a `messages` key with an array of OpenAI-format chat messages, `response` is the last message’s `content`.
- Otherwise, `response` is the `outputs` serialized to a JSON string.

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Additional context variables (Guidelines judges)

Guidelines judges allow users to provide arbitrary context variables by including them in the evaluation data or by passing a context dictionary. Any key from the context dictionary can be referenced directly in guidelines. Common examples include `retrieved_documents`, `user_preferences`, `max_allowed_discount`, and `approved_features`.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### `trace` variable (trace-based judges)

When using the `make_judge()` API to create a trace-based judge, the full execution trace can be included as a context variable. By placing `{{ trace }}` in the judge’s instructions, the evaluator gains access to tool invocations, intermediate reasoning steps, and their results. This enables judges to validate whether appropriate tools were called for a given user request.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Referencing Context Variables in Guidelines

Within a guideline string, any context variable key can be used as a plaintext reference. For example:

```python
guideline = "The response must only use facts present in retrieved_documents"
```

Multiple context variables can be combined in a single guideline:

```python
guideline = """
The response must:
- Only mention approved_features
- Not include deprecated_features
"""
```

This allows guidelines to enforce business rules based on dynamic data such as user tier, allowed discounts, or fetched documents.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Best Practices

- **Match variable names exactly**: Context variables are referenced by the exact key name as it appears in the context dictionary (e.g., `retrieved_documents`, not `retrievedDocs`).^[create-a-guidelines-llm-judge-databricks-on-aws.md]
- **Include only necessary context**: To avoid confusion and improve judge focus, limit context variables to those that are actually referenced in the guidelines.
- **Validate context availability**: Before writing guidelines that reference a context variable, ensure the variable is present in the evaluation data or passed explicitly.
- **Use `request` and `response` for standard input/output**: These are automatically extracted, so guidelines can rely on them without additional setup.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) – Judges that use natural language pass/fail criteria.
- [Custom Judges](/concepts/custom-judges.md) – Creating judges with `make_judge()` for specialized evaluation.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The offline evaluation framework that uses these judges.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing agent variants with consistent judges.
- Align Judges with Human Feedback – Improving judge accuracy with expert annotations.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
