---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: bc8179abd9ee8c00c406c603462cd513eaff5249866fb75b4c611db1f82bb550
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - feedback-vs-expectation-schema-types
    - FVEST
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Feedback vs Expectation schema types
description: "Two distinct schema types: feedback for subjective assessments (ratings, preferences) and expectation for objective ground truth (correct answers, required facts)."
tags:
  - mlflow
  - schema-types
  - labeling
timestamp: "2026-06-19T17:58:47.157Z"
---

# Feedback vs Expectation Schema Types

**Feedback vs Expectation Schema Types** refers to the two fundamental categories of labeling schemas: `feedback` (subjective assessments) and `expectation` (objective ground truth). These schema types determine the nature of the assessment that is attached to a trace when using the [Review App](/concepts/mlflow-review-app.md) for human evaluation of GenAI applications. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

Labeling schemas define the specific questions that domain experts answer when labeling existing traces in the Review App. They structure the feedback collection process, ensuring consistent and relevant information for evaluating your GenAI app. Every schema is one of two types: `feedback` or `expectation`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Type | Purpose | Example Use Cases |
|------|---------|-------------------|
| `feedback` | Subjective assessments like ratings, preferences, or opinions | Response quality ratings, tone appropriateness, confidence assessments |
| `expectation` | Objective ground truth like correct answers or expected behavior | Required facts, guidelines, expected responses, required disclaimers |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Feedback Schema Type

Feedback schemas capture subjective assessments from human reviewers. These are opinions, preferences, or evaluations that may vary between reviewers based on their perspective. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Characteristics

- **Subjective**: Based on reviewer judgment and opinion
- **Scalable**: Can use categorical, numeric, or text inputs
- **Context-dependent**: May include comments for additional context

### Common Input Methods

- InputCategorical — For discrete choices like "Good", "Fair", "Poor"
- InputCategoricalList — For multiple selections like error categories
- InputNumeric — For numeric ratings or confidence scores
- InputText — For open-ended comments

### Example: Feedback Schema

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

# Rating quality
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating."
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Expectation Schema Type

Expectation schemas capture objective ground truth. These are facts, rules, or behaviors that the model's output should meet — not opinions about the output. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Characteristics

- **Objective**: Based on verifiable facts or defined requirements
- **Deterministic**: Should produce consistent results across reviewers
- **Ground Truth**: Represents correct answers or expected behaviors

### Common Input Methods

- InputTextList — For listing expected facts or required elements
- InputText — For single expected responses
- InputCategorical — For binary choices (present/absent)

### Example: Expectation Schema

```python
# Expected facts
expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,
    type="expectation",
    title="Expected facts",
    input=InputTextList(max_length_each=1000),
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Relationship to Built-in LLM Judges

MLflow provides predefined schema names for [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations. These predefined schemas ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Predefined Schema | Type | Usage |
|-------------------|------|-------|
| `EXPECTED_FACTS` | Expectation | Collecting expected facts for judge evaluation |
| `GUIDELINES` | Expectation | Defining guidelines for model behavior |
| `EXPECTED_RESPONSE` | Expectation | Specifying correct agent responses |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Scope and Management

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so schema names must be unique within your experiment. When creating labeling sessions, you associate them with one or more schemas — each representing an assessment attached to a trace. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Best Practices

- **Feedback schemas**: Write questions as clear, specific prompts. Provide context to guide reviewers. Ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Expectation schemas**: Keep instructions objective and verifiable. Use InputTextList for lists of multiple items. Set reasonable length limits. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Management

- Use descriptive, consistent names across your schemas
- When updating schemas, consider the impact on existing sessions
- Delete unused schemas to keep your workspace organized
- When updating, use the `overwrite=True` parameter to replace existing schemas

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Sessions

When you create a [Labeling Session](/concepts/labeling-session.md), you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. The Review App presents questions based on your schema definitions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
# Schemas are automatically available when creating labeling sessions
# The Review App will present questions based on your schema definitions
session_schemas = [
    "response_quality",      # Your feedback schema
    "expected_facts",         # Your expectation schema
    schemas.EXPECTED_FACTS   # Built-in expectation schema
]
```

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The overall schema system for structuring feedback
- [Review App](/concepts/mlflow-review-app.md) — The interface where schemas are applied
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) — The evaluation platform using schemas
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined judges using expectation schemas
- InputCategorical — Categorical input type for feedback schemas
- InputTextList — Text list input type for expectation schemas
- [Labeling Sessions](/concepts/labeling-sessions.md) — Sessions that associate schemas with traces

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
