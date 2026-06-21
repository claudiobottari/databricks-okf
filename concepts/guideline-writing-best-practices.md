---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 06a233224b12da26cd903791728a5062c73de915b1e3adb0a66b41f28356b39c
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - guideline-writing-best-practices
    - GWBP
    - guidelines-writing-best-practices
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guideline Writing Best Practices
description: "Principles for authoring effective natural language evaluation criteria: be specific and measurable, use clear pass/fail conditions, reference context explicitly, and structure complex requirements."
tags:
  - best-practices
  - llm-evaluation
  - genai
timestamp: "2026-06-19T17:55:48.785Z"
---

# Guideline Writing Best Practices

**Guideline Writing Best Practices** describes the principles and techniques for creating effective natural language criteria used by [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) to evaluate GenAI outputs. Well-written guidelines are crucial for accurate evaluation, as they directly determine whether a judge can correctly assess compliance, style, accuracy, and other quality dimensions. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Core Principles

### Be Specific and Measurable

Guidelines should define clear, observable conditions that can be objectively evaluated. Vague or subjective language leads to inconsistent judgments. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

✅ **Good:** "The response must not include specific pricing amounts or percentages"
❌ **Poor:** "Don't talk about money"

### Use Clear Pass/Fail Conditions

Each guideline should establish an unambiguous binary outcome. The judge must be able to determine definitively whether the output passes or fails. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

✅ **Good:** "If asked about pricing, the response must direct users to the pricing page"
❌ **Poor:** "Handle pricing questions appropriately"

### Reference Context Variables Explicitly

Guidelines can reference any key from the evaluation context dictionary directly by name. This allows judges to validate outputs against specific data such as retrieved documents, user preferences, or business rules. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

```python
# Example: Validate against retrieved documents
guideline = "The response must only include information from retrieved_documents"

# Example: Check user preferences
guideline = "The response must respect user_preferences when making recommendations"

# Example: Enforce business rules
guideline = "The response must not exceed max_allowed_discount for the user_tier"
```

### Structure Complex Requirements

When a guideline involves multiple conditions, use a structured list format to make each requirement distinct and independently evaluable. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

```python
guideline = """The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words"""
```

## Common Use Cases

Guidelines judges excel at evaluating several categories of criteria: ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

| Category | Example |
|----------|---------|
| **Compliance** | "Must not include pricing information" |
| **Style/Tone** | "Maintain professional, empathetic tone" |
| **Requirements** | "Must include specific disclaimers" |
| **Accuracy** | "Use only facts from provided context" |

## Context Variable Reference

The `Guidelines` judge automatically extracts `request` and `response` keys from the trace data. Additional context variables can be included in the evaluation dataset and referenced directly in guidelines. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Request Parsing

The `request` field is extracted from the provided `inputs`: ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- If `inputs` contains a `messages` key with an array of OpenAI format chat messages:
  - Single message: `request` is that message's `content`
  - Multiple messages: `request` is the entire messages array serialized to JSON
- Otherwise: `request` is the entire `inputs` dict serialized to JSON

### Response Parsing

The `response` field is extracted from the provided `outputs`: ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- If `outputs` contains an OpenAI format ChatCompletions object: `response` is the first choice's `content`
- If `outputs` contains a `messages` key: `response` is the last message's `content`
- Otherwise: `response` is the `outputs` serialized to JSON

## Real-World Examples

### Customer Service Tone Guidelines

```python
guideline = """The response must maintain our brand voice which is:
- Professional yet warm and conversational (avoid corporate jargon)
- Empathetic, acknowledging emotional context before jumping to solutions
- Proactive in offering help without being pushy
Specifically:
- If the customer expresses frustration, anger, or disappointment, the first sentence must acknowledge their emotion
- The response must use "I" statements to take ownership (e.g., "I understand" not "We understand")
- The response must avoid phrases that minimize concerns like "simply", "just", or "obviously"
- The response must end with a specific next step or open-ended offer to help, not generic closings"""
```

### Policy Compliance Guidelines

```python
guidelines = [
    """Refund and return policies:
    - The response must not promise refunds beyond the 30-day return window
    - The response must mention restocking fees for electronics (15%) if discussing returns
    - For items over $500, the response must note that manager approval is required
    - The response must not waive shipping fees without checking customer loyalty tier""",
    """Data privacy and security:
    - The response must never ask for full credit card numbers, SSN, or passwords
    - The response must not reference other customers' orders or information
    - When discussing order details, the response must only reference the last 4 digits of payment methods
    - The response must direct customers to secure portal for updating payment information""",
]
```

### Document Extraction Accuracy Guidelines

```python
guidelines = [
    """Field extraction completeness and accuracy:
    - The response must extract ALL requested fields, using exact values from source
    - For ambiguous data, the response must extract the most likely value and include a confidence score
    - When multiple values exist for one field (e.g., multiple addresses), extract all and label them
    - Preserve original formatting for IDs, reference numbers, and codes (including leading zeros)
    - For missing fields, use null with reason: {"field": null, "reason": "not_found"}""",
    """Numerical and financial data handling:
    - Currency values must preserve exact decimal places as shown in source
    - Must differentiate between currencies if multiple are present (USD, EUR, etc.)
    - Percentage values must clarify if they're decimals (0.15) or percentages (15%)
    - For calculated fields (totals, tax), must match source exactly - no recalculation
    - Negative values must be preserved with proper notation (-$100 or ($100))""",
]
```

## Benefits of Well-Written Guidelines

Effective guidelines provide several advantages: ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

- **Business-friendly**: Domain experts can write criteria without coding
- **Flexible**: Criteria can be updated without code changes
- **Interpretable**: Clear pass/fail conditions make results understandable
- **Fast iteration**: New criteria can be rapidly tested and refined

## Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) — The judge type that evaluates against natural language criteria
- [Custom Judges](/concepts/custom-judges.md) — Building judges for specific evaluation needs
- Align Judges with Human Feedback — Improving judge accuracy with expert annotations
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework for GenAI applications
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
