---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6c68b4bb69cd83b1a783ab6dbf88c7c9b3d6811616af092fe87334095184aeb7
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-labeling-schema-creation
    - CLSC
    - Create custom labeling schemas
    - Custom Labeling Schemas
    - creating custom labeling schemas
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Custom Labeling Schema Creation
description: The process of defining custom labeling schemas via the MLflow UI or Python API, specifying name, type, title, input type, and optional instructions for tailored human feedback collection.
tags:
  - genai
  - mlflow
  - api
timestamp: "2026-06-18T11:17:53.454Z"
---

# Custom Labeling Schema Creation

Custom labeling schemas define the specific questions that domain experts answer when labeling existing traces in the [Review App](/concepts/mlflow-review-app.md). They structure the feedback collection process, ensuring consistent and relevant information for evaluating a GenAI agent. Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so schema names must be unique within an experiment.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## How Labeling Schemas Work

When you create a labeling session, you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either **Feedback** (subjective assessments like ratings, preferences, or opinions) or **Expectation** (objective ground truth like correct answers or expected behavior).^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The schema controls:
- The question shown to reviewers.
- The input method (e.g., drop-down menu, text box, numeric range).
- Validation rules and constraints.
- Optional instructions and comments.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Labeling schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined Labeling Schemas for Built-in LLM Judges

MLflow provides predefined schema names for the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations. You can create custom schemas using these names to ensure compatibility with built-in evaluation functionality. The predefined schemas include `EXPECTED_FACTS`, `GUIDELINES`, and `EXPECTED_RESPONSE`.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList, InputText

expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,
    type=LabelSchemaType.EXPECTATION,
    title="Expected facts",
    input=InputTextList(max_length_each=1000),
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True)
```

## Create Custom Labeling Schemas

For more control over the feedback you collect, create a custom labeling schema using the MLflow UI or the API.

### Using the UI

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Open your experiment.
3. Click **Labeling schemas** in the sidebar.
4. Click **Add Label Schema** and edit the fields. When you select an input type, additional fields appear to specify length limits, categorical options, or numeric ranges.
5. Click **Save**.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Using the API

Use `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type (`"feedback"` or `"expectation"`), title, and input specification.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

#### Basic feedback schema example

```python
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating.")
```

#### Custom expectation schema example

```python
facts_schema = schemas.create_label_schema(
    name="required_facts",
    type="expectation",
    title="What facts must be included in a correct response?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List key facts that any correct response must contain.")
```

## Input Types for Custom Schemas

MLflow supports five input types for collecting different kinds of feedback. Each is a class in `mlflow.genai.label_schemas`.

### `InputCategorical`

A single-select dropdown for rating scales, binary choices, or multiple categories.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
rating_input = InputCategorical(options=["1 - Poor", "2 - Below Average", "3 - Average", "4 - Good", "5 - Excellent"])
```

### `InputCategoricalList`

A multi-select checklist for selecting multiple issues or content types.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
errors_input = InputCategoricalList(options=["Factual inaccuracy", "Missing context", "Inappropriate tone", "Formatting issues", "Off-topic content"])
```

### `InputText`

A free-form text box for general feedback, improvement suggestions, or short answers. Specify `max_length` to limit length.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
feedback_input = InputText(max_length=500)
```

### `InputTextList`

A list of text entries, each with an optional `max_length_each` and a maximum number of entries (`max_count`).^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
errors_input = InputTextList(max_count=10, max_length_each=150)
```

### `InputNumeric`

A numeric input for ratings, confidence scores, or cost estimates. Specify `min_value` and `max_value`.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
confidence_input = InputNumeric(min_value=0.0, max_value=1.0)
```

## Manage Labeling Schemas

The API provides methods to list, update, and delete schemas.

### List a Schema

Use `get_label_schema(schema_name)` to retrieve schema details.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schema = schemas.get_label_schema("response_quality")
print(f"Name: {schema.name}, Type: {schema.type}, Title: {schema.title}")
```

### Update a Schema

Use `create_label_schema` with the same name and set `overwrite=True` to replace an existing schema.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True)
```

### Delete a Schema

Use `delete_label_schema(schema_name)` to remove a schema that is no longer needed.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

## Integration with Labeling Sessions

Schemas are automatically available when creating labeling sessions. The Review App presents questions based on your schema definitions. You can reference schemas by name when setting up a session.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
session_schemas = ["service_quality", "response_issues", schemas.EXPECTED_FACTS]
```

## Best Practices

- **Schema design**: Write questions as clear, specific prompts. Provide context (instruction field) to guide reviewers. Set reasonable limits on text length and list counts. For categorical inputs, ensure options are mutually exclusive and comprehensive.^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Schema management**: Use descriptive, consistent names across your schemas. When updating schemas, consider the impact on existing sessions. Delete unused schemas to keep the workspace organized.^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Organize review workflows using schemas
- Human Feedback Alignment — Improving judge accuracy with expert annotations
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined judges that can be paired with built-in schema names
- GenAI Agent Evaluation — Using custom judges and human feedback for agent evaluation
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts apply labeling schemas

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
