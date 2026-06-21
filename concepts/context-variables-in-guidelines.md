---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5c983712de391f5081def352966b6cf1f4724d2a66fb6cbc5d787adfca46cbd2
  pageDirectory: concepts
  sources:
    - create-a-guidelines-llm-judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - context-variables-in-guidelines
    - CVIG
    - Context Variables
  citations:
    - file: create-a-guidelines-llm-judge-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Context Variables in Guidelines
description: A mechanism allowing guidelines to reference any key from the evaluation context dictionary (e.g. request, response, retrieved_documents, user_preferences) directly in natural language criteria.
tags:
  - mlflow
  - context
  - guidelines
timestamp: "2026-06-18T11:13:56.464Z"
---

# Context Variables in Guidelines

**Context Variables in Guidelines** are named placeholders used within [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) that allow you to reference specific data fields from your evaluation dictionary directly in natural-language evaluation criteria. They transform abstract guidelines into testable conditions by explicitly connecting evaluation rules to the data being analyzed.

## How context variables work

Guidelines judges receive a context dictionary—a JSON object containing the data to evaluate—and use context variable names to reference specific fields within that dictionary. When you write a guideline like `"The response must only use facts from retrieved_documents"`, the judge identifies `retrieved_documents` as a context variable and checks whether the model's output is consistent with that field's value.^[create-a-guidelines-llm-judge-databricks-on-aws.md]

The judge automatically extracts two default context variables from every evaluation:

- `request` — the user's input to the application
- `response` — the application's output

You can also add any custom context variables by including them as keys in your evaluation dictionary.

### Example: Referencing context variables in guidelines

**Single context variable** — Validate against a specific field:

```python
context = {
    "request": "What is the refund policy?",
    "response": "You can return items within 30 days for a full refund.",
    "retrieved_documents": ["Policy: Returns accepted within 30 days", "Policy: No refunds after 30 days"]
}
guideline = "The response must only include information from retrieved_documents"
```

**Multiple context variables** — Enforce business rules:

```python
context = {
    "request": "Can you apply a discount?",
    "response": "I've applied a 15% discount to your order",
    "max_allowed_discount": 10,
    "user_tier": "silver"
}
guideline = "The response must not exceed max_allowed_discount for the user_tier"
```

**Multiple constraints** — Combine several context variables:

```python
context = {
    "request": "Tell me about product features",
    "response": "This product includes features A, B, and C",
    "approved_features": ["A", "B", "C", "D"],
    "deprecated_features": ["X", "Y", "Z"]
}
guideline = """The response must:
- Only mention approved_features
- Not include deprecated_features"""
```

## How the Guidelines judge parses context variables from inputs and outputs

The Guidelines judge and [ExpectationsGuidelines](/concepts/expectationsguidelines-judge-per-row-guidelines.md) judge automatically extract context variables from your application's trace data. They parse the `inputs` and `outputs` fields to create the `request` and `response` context variables.

### Request context variable

The `request` field is extracted from `inputs`:

- If `inputs` contains a `messages` key with an array of OpenAI-format chat messages:
  - A single message: `request` is that message's `content`
  - Multiple messages: `request` is the entire messages array serialized to a JSON string
- Otherwise: `request` is the `inputs` dictionary serialized to a JSON string

### Response context variable

The `response` field is extracted from `outputs`:

- If `outputs` contains an OpenAI-format ChatCompletion object: `response` is the first choice's `content`
- If `outputs` contains a `messages` key with an array of OpenAI-format chat messages: `response` is the last message's `content`
- Otherwise: `response` is the `outputs` serialized to a JSON string

## Best practices for using context variables in guidelines

**Reference context explicitly** — Include the context variable name directly in your guideline:

- ✅ `"The response must only use facts present in retrieved_context"`
- ❌ `"Be factual"`

**Use clear variable names** — Choose descriptive names that match your data schema:

- ✅ `"approved_features"`, `"deprecated_features"`
- ❌ `"features"`, `"unused_features"`

**Structure complex requirements** — When multiple context variables are involved, write clear, sequential conditions:

```python
guideline = """The response must:
- Include a greeting if first message
- Address the user's specific question
- End with an offer to help further
- Not exceed 150 words"""
```

Note: The `request`, `response`, and user-defined context variables are available by default in the context dictionary when using built-in Guidelines judges. For Custom Judge Creation with make_judge|custom judges created with `make_judge()`, you must specify which context variables are available by including `{{ trace }}` in the judge's instructions.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related concepts

- [Guidelines LLM Judges](/concepts/guidelines-llm-judges.md) — The judge type that uses context variables in its evaluation criteria
- [ExpectationsGuidelines judge](/concepts/expectationsguidelines-judge-per-row-guidelines.md) — A variant that applies per-row context variables from an evaluation dataset
- [Custom Judges](/concepts/custom-judges.md) — User-defined judges that can reference custom context variables
- [Trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) — Evaluation that analyzes execution traces to set context variables

## Sources

- create-a-guidelines-llm-judge-databricks-on-aws.md

# Citations

1. [create-a-guidelines-llm-judge-databricks-on-aws.md](/references/create-a-guidelines-llm-judge-databricks-on-aws-0e433eae.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
