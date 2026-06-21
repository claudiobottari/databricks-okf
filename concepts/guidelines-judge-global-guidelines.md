---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 66d182127127603576591e9f48bf99625bcd2a7fd8255290a606111483756d4e
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.96
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-judge-global-guidelines
    - GJ(G
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guidelines() Judge (Global Guidelines)
description: A built-in MLflow scorer that applies uniform natural-language guidelines across all evaluation rows or production traces, automatically extracting request/response data.
tags:
  - mlflow
  - llm-evaluation
  - scoring
  - global-guidelines
timestamp: "2026-06-18T14:47:22.032Z"
---

# `Guidelines()` Judge (Global Guidelines)

The **`Guidelines()` judge** is a built-in [LLM judge](/concepts/llm-judges.md) in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that applies uniform, pass/fail natural language guidelines across all rows in an evaluation dataset or all traces in production monitoring. It evaluates only the app's inputs and outputs, making it suitable for consistent quality checks such as compliance, tone, or accuracy requirements.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Uses

Guidelines LLM judges excel at evaluating:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Compliance**: "Must not include pricing information"
- **Style/tone**: "Maintain professional, empathetic tone"
- **Requirements**: "Must include specific disclaimers"
- **Accuracy**: "Use only facts from provided context"

## How It Works

The `Guidelines()` judge uses a specially-tuned LLM to determine whether the app's response meets the specified criteria. The process involves three steps:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

1. **Receive context** – The judge extracts the app's inputs (as `request`) and outputs (as `response`) from each trace or row. You can reference these keys directly in your guidelines.
2. **Apply guidelines** – Your natural language rules define clear pass/fail conditions.
3. **Make judgment** – The judge returns a binary result (`"yes"` or `"no"`) along with a detailed rationale.

By default, the judge uses a Databricks-managed model. You can change the underlying model by passing the `model` argument in the format `<provider>:/<model-name>` (e.g., `databricks:/databricks-gpt-oss-120b`).^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Parsing Inputs and Outputs

The `Guidelines()` judge automatically interprets the data provided in `inputs` and `outputs` to create the context dictionary with keys `request` and `response`. The exact parsing rules are:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Request

- If `inputs` contains a `messages` key with an array of OpenAI-format chat messages:
  - For a single message, `request` is that message's `content`.
  - For multiple messages, `request` is the entire array serialized to a JSON string.
- Otherwise, `request` is the entire `inputs` dict serialized to a JSON string.

### Response

- If `outputs` contains an OpenAI-format `ChatCompletions` object, `response` is the first choice's `content`.
- If `outputs` contains a `messages` key with an array of OpenAI-format chat messages, `response` is the last message's `content`.
- Otherwise, `response` is the `outputs` dict serialized to a JSON string.

This automatic extraction enables guidelines to reference the app's request and response by name.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `name` | `str` | A label for the assessment (used in results). |
| `guidelines` | `list[str]` or `str` | One or more natural language rules that define pass/fail conditions. |
| `model` | `str` (optional) | The LLM to use for judgment, specified as `<provider>:/<model-name>`. Defaults to a Databricks-managed model. |

The guidelines can include any key from the context dictionary (such as `request`, `response`, or custom keys like `retrieved_documents`).^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Return Values

The `Guidelines()` judge returns an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- `value`: `"yes"` (meets guidelines) or `"no"` (fails guidelines)
- `rationale`: Detailed explanation of why the content passed or failed
- `name`: The assessment name (either provided or auto-generated)
- `error`: Error details if evaluation failed

## Best Practices for Writing Guidelines

Effective guidelines improve the accuracy and reliability of the judge:^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Be specific and measurable.**  
  ✅ "The response must not include specific pricing amounts or percentages"  
  ❌ "Don't talk about money"

- **Use clear pass/fail conditions.**  
  ✅ "If asked about pricing, the response must direct users to the pricing page"  
  ❌ "Handle pricing questions appropriately"

- **Reference context variables explicitly.**  
  ✅ "The response must only use facts present in `retrieved_documents`"  
  ❌ "Be factual"

- **Structure complex requirements.**  
  ```
  The response must:
  - Include a greeting if first message
  - Address the user's specific question
  - End with an offer to help further
  - Not exceed 150 words
  ```

## Examples

### Basic Global Guidelines

```python
from mlflow.genai.scorers import Guidelines

english = Guidelines(
    name="english",
    guidelines=["The response must be in English"]
)

clarity = Guidelines(
    name="clarity",
    guidelines=["The response must be clear, coherent, and concise"],
    model="databricks:/databricks-gpt-oss-120b"  # optional custom judge model
)
```

### Tone and Compliance for Customer Service

```python
tone_guidelines = Guidelines(
    name="customer_service_tone",
    guidelines="""The response must maintain our brand voice which is:
    - Professional yet warm and conversational...
    - Empathetic, acknowledging emotional context before jumping to solutions
    - Proactive in offering help without being pushy..."""
)

compliance_guidelines = Guidelines(
    name="policy_compliance",
    guidelines=[
        """Refund and return policies:
        - The response must not promise refunds beyond the 30-day return window
        - The response must mention restocking fees for electronics (15%)...
        ...""",
        """Data privacy and security:
        - The response must never ask for full credit card numbers..."""
    ]
)
```

Both examples are complete judge definitions that can be passed to `mlflow.genai.evaluate()`.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Model Information

LLM judges might use third-party services to evaluate your GenAI applications, including Azure OpenAI operated by Microsoft. For Azure OpenAI, Databricks has opted out of Abuse Monitoring so no prompts or responses are stored with Azure OpenAI. For European Union (EU) workspaces, LLM judges use models hosted in the EU. All other regions use models hosted in the US. Disabling Partner-powered AI features prevents the LLM judge from calling partner-powered models — you can still use LLM judges by providing your own model. LLM judge outputs should not be used to train, improve, or fine-tune an LLM.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [ExpectationsGuidelines() Judge](/concepts/expectationsguidelines-judge-per-row-guidelines.md) – Per-row guidelines for offline evaluation.
- [Custom Judges](/concepts/custom-judges.md) – Build your own LLM-based scorers.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The `mlflow.genai.evaluate()` API.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Continuous evaluation with the same judges.
- [LLM Judges](/concepts/llm-judges.md) – Overview of all built-in and custom judge types.
- Align judges with human feedback – Improving judge accuracy with expert annotations.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
