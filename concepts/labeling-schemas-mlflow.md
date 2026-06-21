---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a06234f630d710dbf2a9583c699ff967108a4e13645863024e380135204f45d8
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schemas-mlflow
    - LS(
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schemas (MLflow)
description: Structured question definitions that domain experts answer when labeling existing traces in the MLflow Review App for GenAI evaluation.
tags:
  - mlflow
  - human-feedback
  - labeling
  - genai
timestamp: "2026-06-19T17:58:35.941Z"
---

# Labeling schemas (MLflow)

**Labeling schemas** define the specific questions or assessments that domain experts answer when labeling existing traces in the Review App. They structure the feedback collection process, ensuring consistent and relevant information for evaluating a GenAI application. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Labeling schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## How labeling schemas work

When a labeling session is created, it is associated with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either `Feedback` (subjective ratings, preferences, opinions) or `Expectation` (objective ground truth like correct answers or expected behavior). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Schemas control:
- The question shown to reviewers.
- The input method (e.g., drop-down menu, text box).
- Validation rules and constraints.
- Optional instructions and comments.

## Labeling schemas for built-in LLM judges

MLflow provides predefined schema names for the built-in LLM judges that use expectations. You can create custom schemas using these names to ensure compatibility with built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Examples of predefined schemas include `EXPECTED_FACTS`, `GUIDELINES`, and `EXPECTED_RESPONSE`. For the full list, see the API reference. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Create custom labeling schemas

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so schema names must be unique within an experiment. They have two types: `feedback` and `expectation`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Create custom schemas using the UI

To create a custom schema in the MLflow UI: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

1. In the Databricks workspace, click **Experiments**.
2. Click the experiment name to open it.
3. Click **Labeling schemas** in the sidebar.
4. Click **Add Label Schema** and edit the fields (name, type, title, input type, instructions).
   - When you select the **Input type**, fields appear for detailed requirements (length limits, categorical options, numeric range).
5. Click **Save**.

### Create custom schemas using the API

Use `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type, title, and input specification. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating.",
)
```

## Manage labeling schemas

Using the API, you can list, update, and delete labeling schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### List schemas

Use `get_label_schema(name)` to retrieve an existing schema’s information. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schema = schemas.get_label_schema("response_quality")
```

### Update schemas

Use `create_label_schema()` with `overwrite=True` to replace an existing schema. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    overwrite=True,
)
```

### Delete schemas

Use `delete_label_schema(name)` to remove a schema. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

## Input types for custom schemas

MLflow supports several input types for collecting different kinds of feedback. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputCategorical`

For single-choice selection from a list of options.

```python
rating_input = InputCategorical(options=["1 - Poor", "2 - Below Average", "3 - Average", "4 - Good", "5 - Excellent"])
```

### `InputCategoricalList`

For multiple-choice selection (select all that apply).

```python
errors_input = InputCategoricalList(options=["Factual inaccuracy", "Missing context", "Inappropriate tone"])
```

### `InputText`

For free-text input with optional maximum length.

```python
feedback_input = InputText(max_length=500)
```

### `InputTextList`

For a list of free-text items, with optional maximum count and per-item length.

```python
errors_input = InputTextList(max_count=10, max_length_each=150)
```

### `InputNumeric`

For numeric ratings or scores within a defined range.

```python
confidence_input = InputNumeric(min_value=0.0, max_value=1.0)
```

## Complete examples

The source material includes full examples for customer service evaluation and medical information review, demonstrating combinations of input types and both `feedback` and `expectation` schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with labeling sessions

Schemas are automatically available when creating labeling sessions. The Review App presents questions based on the schema definitions associated with the session. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
session_schemas = [
    "service_quality",
    "response_issues",
    schemas.EXPECTED_FACTS
]
```

## Best practices

- Write questions as clear, specific prompts. Provide context to guide reviewers. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- Set reasonable limits on text length and list counts.
- For categorical inputs, ensure options are mutually exclusive and comprehensive.
- Use descriptive, consistent schema names. When updating schemas, consider the impact on existing sessions.
- Delete unused schemas to keep the workspace organized.

## Related concepts

- [Review App](/concepts/mlflow-review-app.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [Human feedback](/concepts/mlflow-human-feedback-collection.md)

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
