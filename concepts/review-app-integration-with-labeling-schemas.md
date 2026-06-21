---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: efeaa553f180d93928ffd8152c401d5bc56825adfb45991a7eba78597b11c9ec
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - review-app-integration-with-labeling-schemas
    - RAIWLS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Review App Integration with Labeling Schemas
description: Labeling schemas are associated with labeling sessions in the Review App; they control the question shown, input method, validation rules, and optional instructions, and are not used for vibe checks in the Chat UI.
tags:
  - mlflow
  - review-app
  - workflow
timestamp: "2026-06-19T14:34:03.116Z"
---

# Review App Integration with Labeling Schemas

**Review App Integration with Labeling Schemas** refers to the use of [Labeling Schemas](/concepts/labeling-schemas.md) within the [Review App](/concepts/mlflow-review-app.md) to collect structured human feedback on existing [GenAI traces](/concepts/mlflow-genai-trace.md). Labeling schemas define the specific questions that domain experts answer when labeling traces, structuring the feedback collection process to ensure consistent and relevant information for evaluating a GenAI application. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When reviewing traces in the Review App, labelers interact with one or more labeling schemas. Each schema represents an assessment attached to a trace, which can be either `Feedback` (subjective assessments like ratings or opinions) or `Expectation` (objective ground truth like correct answers or expected behavior). The schemas control the question shown to reviewers, the input method (e.g., drop-down menu or text box), validation rules, and optional instructions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Labeling schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## How Integration Works

### Schema Creation Before Review

Schemas must be created before a labeling session begins. They can be created using the [MLflow UI](/concepts/mlflow.md) or the MLflow GenAI API. Schemas are scoped to experiments, so schema names must be unique within an MLflow experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputCategoricalList, InputText, InputTextList, InputNumeric

# Create a feedback schema for rating response quality
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating."
)
```

### Association with Labeling Sessions

When you create a [Labeling Session](/concepts/labeling-session.md), you associate it with one or more labeling schemas. During review, the Review App presents questions to domain experts based on the schema definitions. Schemas are automatically available when creating labeling sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Built-In Schema Compatibility

MLflow provides predefined schema names for built-in [LLM Judges](/concepts/llm-judges.md) that use expectations. You can create custom schemas using these names to ensure compatibility with built-in evaluation functionality: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

- `EXPECTED_FACTS` — Used for collecting expected facts as an `InputTextList`
- `GUIDELINES` — Used for collecting guidelines as an `InputTextList`
- `EXPECTED_RESPONSE` — Used for collecting expected response as an `InputText`

## Input Types in the Review App

The Review App renders different input controls based on the schema's input type: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Input Type | UI Component | Use Case |
|------------|-------------|----------|
| `InputCategorical` | Drop-down menu | Single selection from options |
| `InputCategoricalList` | Multi-select checkboxes | Multiple selections from options |
| `InputText` | Text input field | Free-form text feedback |
| `InputTextList` | List of text fields | Multiple text entries |
| `InputNumeric` | Number input | Numeric ratings or scores |

## Integration Benefits

The integration ensures: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

- **Structured feedback collection** — Consistent question formats across reviewers
- **Validation** — Length limits, option constraints, and numeric ranges enforce quality
- **Context for reviewers** — Instructions and titles guide domain experts
- **Reusable schemas** — Once created, schemas can be used across multiple labeling sessions
- **Built-in compatibility** — Predefined schema names work with existing MLflow evaluation pipelines

## Best Practices for Integration

- Write questions as clear, specific prompts that domain experts can understand without additional context. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Provide detailed instructions to guide reviewers on what constitutes a good assessment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Set reasonable limits on text length and list counts to keep the review process efficient. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- For categorical inputs, ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Use descriptive, consistent names across your schemas to simplify session management. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The schema definition and management system
- [Labeling Sessions](/concepts/labeling-sessions.md) — The organizational unit for review workflows
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts provide feedback
- [Human feedback for GenAI](/concepts/mlflow-human-feedback-collection.md) — The broader workflow of collecting expert annotations
- Label existing traces — The specific workflow for reviewing historical traces
- Build evaluation datasets — Transforming labeled data into test datasets

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
