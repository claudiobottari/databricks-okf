---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6f81ea2a3d065a0649111e7fbe388ba0cda055edf956708c5c6f40b95d995ccf
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - best-practices-for-writing-evaluation-guidelines
    - BPFWEG
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Best Practices for Writing Evaluation Guidelines
description: Principles for crafting effective pass/fail natural language criteria including specificity, clear conditions, context references, and structured multi-constraint guidelines.
tags:
  - best-practices
  - llm-evaluation
  - guidelines
timestamp: "2026-06-18T11:15:50.539Z"
---

# Best Practices for Writing Evaluation Guidelines

**Best Practices for Writing Evaluation Guidelines** describes the set of principles and techniques for crafting effective natural language criteria that LLM-based judges use to evaluate GenAI outputs. Well-written guidelines are crucial for accurate evaluation and ensure that automated assessments produce consistent, interpretable, and business-relevant results.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Core Principles

### Be Specific and Measurable

Guidelines must define clear, testable conditions rather than vague preferences. Specific criteria yield more consistent judge output than ambiguous instructions.

| Avoid | Prefer |
|-------|--------|
| "Don't talk about money" | "The response must not include specific pricing amounts or percentages" |
| "Handle pricing questions appropriately" | "If asked about pricing, the response must direct users to the pricing page" |
| "Be factual" | "The response must only use facts present in retrieved_context" |

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Use Clear Pass/Fail Conditions

Each guideline should express a binary condition that the judge can evaluate definitively. The judge returns `"yes"` when the output meets the guideline and `"no"` when it fails, accompanied by a detailed rationale.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Structure Complex Requirements

When a guideline must enforce multiple conditions, use a structured bullet-list format within a single guideline string to improve clarity and evaluator accuracy.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

```
guideline = """The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words"""
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Reference Context Variables

The evaluation context is a JSON dictionary that contains the data available for judgment. Guidelines can reference any key from this context directly by name. The most common keys are `request` (the app's inputs) and `response` (the app's outputs). Additional context keys like `retrieved_documents`, `user_preferences`, or business-rule variables become available depending on the data passed to the evaluation.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Examples of Context Variable Usage

**Validate against retrieved documents:**
```python
guideline = "The response must only include information from retrieved_documents"
```

**Check user preferences:**
```python
guideline = "The response must respect user_preferences when making recommendations"
```

**Enforce business rules:**
```python
guideline = "The response must not exceed max_allowed_discount for the user_tier"
```

**Multiple constraints with context variables:**
```python
guideline = """The response must:
- Only mention approved_features
- Not include deprecated_features"""
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Guidelines Judge Types

### `Guidelines()` — Global Guidelines

Use the `Guidelines` judge to apply uniform criteria across all rows in an evaluation dataset or all traces in production monitoring. The judge automatically extracts `request` and `response` data from the trace and evaluates every row against the same set of guidelines.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Global guidelines work in both offline evaluation and [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md). They are ideal for enforcing company-wide standards such as tone, compliance rules, and output format requirements.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### `ExpectationsGuidelines()` — Per-Row Guidelines

Use the `ExpectationsGuidelines` judge when different rows require different evaluation criteria. Each row in the evaluation dataset can specify its own set of guidelines under the `expectations` key. This is useful when domain experts have labeled specific examples with custom guidelines.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

Per-row guidelines are only available for offline evaluation, not production monitoring.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Common Use Cases

### Compliance and Policy Enforcement

Guidelines can enforce regulatory or business policy requirements such as:
- Refund and return policies (e.g., 30-day window, restocking fees)
- Data privacy rules (e.g., no full credit card numbers, no SSNs)
- Commitment limitations (e.g., no guaranteed delivery dates without verification)

### Style and Tone Guidelines

Guidelines can define brand voice expectations:
- Professional yet warm and conversational tone
- Empathetic acknowledgment before jumping to solutions
- Proactive offers to help without being pushy
- Avoidance of minimizing phrases like "simply" or "just"

### Accuracy and Factuality

Guidelines can constrain responses to source material:
- Use only facts from provided context
- Include specific disclaimers when required
- Maintain exact numerical values from source documents

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Real-World Examples

### Customer Service Chatbot

**Global tone guidelines:**
```
The response must maintain our brand voice which is:
- Professional yet warm and conversational (avoid corporate jargon)
- Empathetic, acknowledging emotional context before jumping to solutions
- Proactive in offering help without being pushy
Specifically:
- If the customer expresses frustration, anger, or disappointment, the first sentence must acknowledge their emotion
- The response must use "I" statements to take ownership
- The response must avoid phrases that minimize concerns like "simply", "just", or "obviously"
```

### Document Extraction Accuracy

**Field extraction guidelines:**
```
Field extraction completeness and accuracy:
- The response must extract ALL requested fields, using exact values from source
- For ambiguous data, extract the most likely value and include a confidence score
- Preserve original formatting for IDs, reference numbers, and codes (including leading zeros)
- For missing fields, use null with reason: {"field": null, "reason": "not_found"}
```

### Compliance Guidelines (Multiple Rules)

```python
compliance_guidelines = Guidelines(
    name="policy_compliance",
    guidelines=[
        """Refund and return policies:
        - Must not promise refunds beyond 30-day return window
        - Must mention restocking fees for electronics (15%)
        - For items over $500, must note manager approval is required""",
        """Data privacy and security:
        - Must never ask for full credit card numbers, SSN, or passwords
        - Must not reference other customers' orders or information
        - When discussing order details, only reference last 4 digits of payment methods""",
    ]
)
```

^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Iterative Improvement

### Rapid Iteration Cycle

Guidelines can be updated without code changes, allowing domain experts to refine criteria rapidly. The recommended workflow is:

1. Write initial guidelines based on domain knowledge
2. Run evaluation against representative data
3. Review judge outputs and rationales for consistency
4. Adjust guidelines to correct false passes or false failures
5. Repeat until guidelines match human quality standards

See Align Judges with Human Feedback for guidance on improving judge accuracy with expert annotations.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### Testing New Criteria

Because guidelines are natural language and require no coding, teams can rapidly prototype and test new criteria. Add or modify guidelines in a new evaluation run to quickly assess whether the revised criteria capture the intended quality dimensions.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [Guidelines LLM Judge](/concepts/guidelines-llm-judge.md) — Overview of pass/fail natural language evaluation
- [Custom Judges](/concepts/custom-judges.md) — Building custom evaluators beyond built-in guidelines
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that uses guidelines judges
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying guidelines judges for continuous monitoring
- Align Judges with Human Feedback — Improving judge accuracy with expert annotations
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Comparing agent versions with consistent judges

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
