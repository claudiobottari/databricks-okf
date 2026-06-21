---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 22f6e803f9962a70623cbd720c9c2ea617649a63c4f9e4591ef28e0f04697322
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-writing-best-practices
    - GWBP
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
title: Guidelines Writing Best Practices
description: "Principles for writing effective guidelines: be specific and measurable, use clear pass/fail conditions, reference context explicitly, and structure complex requirements."
tags:
  - llm-evaluation
  - best-practices
timestamp: "2026-06-19T09:28:04.435Z"
---

# Guidelines Writing Best Practices

**Guidelines Writing Best Practices** refer to the techniques for crafting effective natural‑language criteria used by [LLM Judge|Guidelines LLM judges](/concepts/guidelines-llm-judge.md) to evaluate GenAI outputs. Well‑written guidelines are crucial for accurate evaluation and enable domain experts to define quality standards without writing code. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## How Guidelines Work

A Guidelines judge uses a specially‑tuned LLM to evaluate whether text meets specified criteria. The judge:

1. **Receives context**: Any JSON dictionary containing data to evaluate (e.g., `request`, `response`, `retrieved_documents`). Keys from this context can be referenced directly in guidelines.
2. **Applies guidelines**: Natural‑language rules defining pass/fail conditions.
3. **Makes judgment**: Returns a binary pass/fail score with a detailed rationale. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

For API details see the [`Guidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.Guidelines) and [`ExpectationsGuidelines`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.scorers.ExpectationsGuidelines) documentation.

## Key Principles for Writing Effective Guidelines

### 1. Be Specific and Measurable
Guidelines must define clear, observable behaviors. Avoid vague language.  
✅ *“The response must not include specific pricing amounts or percentages.”*  
❌ *“Don’t talk about money.”* ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### 2. Use Clear Pass/Fail Conditions
Each guideline should unambiguously state what constitutes a pass or fail. Conditional logic helps handle varied scenarios.  
✅ *“If asked about pricing, the response must direct users to the pricing page.”*  
❌ *“Handle pricing questions appropriately.”* ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### 3. Reference Context Variables Explicitly
Incorporate keys from the evaluation context directly into the guideline text. This allows the judge to check outputs against actual data (e.g., retrieved documents, user preferences, business rules).  
Example: `"The response must only include information from retrieved_documents."` ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### 4. Structure Complex Requirements
Break multifaceted rules into numbered lists or bullet points within a single guideline string. This improves readability and judge accuracy.  
```python
guideline = """The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words"""
```^[create-a-guidelines-llm-judge-databricks-on-aws.md]

### 5. Keep Guidelines Business‑Friendly and Iterative
Guidelines should be writable by domain experts without coding. They are inherently **flexible** (update without code changes), **interpretable** (clear pass/fail conditions), and enable **fast iteration** (rapidly test new criteria). ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Applying Guidelines: Two Built‑in Approaches

MLflow provides two judge types:

- **`Guidelines()`** – Applies global guidelines uniformly to all rows. Evaluates app inputs and outputs. Works in offline evaluation and production monitoring. 
- **`ExpectationsGuidelines()`** – Applies per‑row guidelines from an evaluation dataset, allowing different criteria for each example. For offline evaluation only. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

When writing per‑row guidelines, reference `request` and `response` as the app’s inputs and outputs. The expectations field in the dataset contains the guidelines array.

## Real‑World Examples

Practical examples from the source include guidelines for:

- **Customer service tone** – maintaining empathy, avoiding minimization phrases.
- **Compliance** – refund policies, data privacy, commitment limitations.
- **Document extraction** – field completeness, numerical handling, entity recognition.
- **Per‑row scenarios** – urgent package delays, subscription cancellations, billing disputes.

Each example demonstrates how to express precise business rules in natural language that an LLM judge can reliably enforce. ^[create-a-guidelines-llm-judge-databricks-on-aws.md]

## Related Concepts

- [LLM Judge](/concepts/llm-judges.md) – The model‑powered evaluator that interprets guidelines.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying guidelines judges in continuous monitoring.
- Human Feedback Alignment – Improving judge accuracy with expert annotations.
- [Custom Judges](/concepts/custom-judges.md) – Building bespoke evaluators beyond the built‑in guidelines judges.

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
