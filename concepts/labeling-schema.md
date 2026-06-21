---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 942b41f4d5049ea6e5f9a9be07b9c9a366ed034f5f52a153c293489ef756c602
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.99
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema
    - Table Schema
    - labeling-schemas-mlflow
    - LS(
    - labeling-schemas-mlflow-review-app
    - LS(RA
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling Schema
description: A structured definition of questions, input types, validation rules, and instructions that domain experts answer when labeling traces in the Review App for GenAI evaluation.
tags:
  - mlflow
  - human-feedback
  - genai
timestamp: "2026-06-19T14:35:37.338Z"
---

Here is the wiki page for "Labeling Schema" based on the provided source material.

# Labeling Schema

A **Labeling Schema** defines the specific questions that domain experts answer when labeling existing traces in the MLflow Review App. It structures the feedback collection process, ensuring consistent and relevant information for evaluating GenAI applications. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Labeling schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## How Labeling Schemas Work

When you create a [Labeling Session](/concepts/labeling-session.md), you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either **Feedback** or **Expectation**. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Schemas control:

- The question shown to reviewers.
- The input method (for example, drop-down menu or text box).
- Validation rules and constraints.
- Optional instructions and comments. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Types

Schemas are one of two types:

- **Feedback**: Subjective assessments like ratings, preferences, or opinions.
- **Expectation**: Objective ground truth like correct answers or expected behavior. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Type Comparison

| Type | Purpose | Example |
|------|---------|---------|
| `feedback` | Subjective quality assessment | "How would you rate the overall quality of this response?" |
| `expectation` | Objective ground truth | "What facts must be included in a correct response?" |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Built-in LLM Judges

MLflow provides predefined schema names for the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations. You can create custom schemas using these names to ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import LabelSchemaType, InputTextList, InputText

# Schema for collecting expected facts
expected_facts_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_FACTS,
    type=LabelSchemaType.EXPECTATION,
    title="Expected facts",
    input=InputTextList(max_length_each=1000),
    instruction="Please provide a list of facts that you expect to see in a correct response.",
    overwrite=True
)

# Schema for collecting guidelines
guidelines_schema = schemas.create_label_schema(
    name=schemas.GUIDELINES,
    type=LabelSchemaType.EXPECTATION,
    title="Guidelines",
    input=InputTextList(max_length_each=500),
    instruction="Please provide guidelines that the model's output is expected to adhere to.",
    overwrite=True
)

# Schema for collecting expected response
expected_response_schema = schemas.create_label_schema(
    name=schemas.EXPECTED_RESPONSE,
    type=LabelSchemaType.EXPECTATION,
    title="Expected response",
    input=InputText(),
    instruction="Please provide a correct agent response.",
    overwrite=True
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Custom Labeling Schemas

For more control over the feedback you collect, create a custom labeling schema using the [MLflow UI](/concepts/mlflow.md) or API. Schemas are scoped to experiments, so schema names must be unique within your MLflow experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Using the UI

1. In the Databricks workspace, in the left sidebar, click **Experiments**.
2. Click the name of your experiment to open it.
3. Click **Labeling schemas** in the sidebar.
4. If an existing labeling schema appears, you can edit it. To create or add a new labeling schema, click **Add Label Schema**, and edit the fields.
5. When you are done, click **Save**. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

When you select the **Input type**, the fields below it change to let you specify detailed requirements, such as length limits for text, options for categorical choices, or a numeric range. As you enter information in the fields, the box at the right updates to reflect the schema you're creating. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Using the API

You can create schemas using `mlflow.genai.label_schemas.create_label_schema()`. All schemas require a name, type, title, and input specification. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputText

# Create a feedback schema for rating response quality
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating."
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Feedback Schema Example

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

# Feedback schema for subjective assessment
tone_schema = schemas.create_label_schema(
    name="response_tone",
    type="feedback",
    title="Is the response tone appropriate for the context?",
    input=InputCategorical(options=["Too formal", "Just right", "Too casual"]),
    enable_comment=True  # Allow additional comments
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Expectation Schema Example

```python
# Expectation schema for ground truth
facts_schema = schemas.create_label_schema(
    name="required_facts",
    type="expectation",
    title="What facts must be included in a correct response?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List key facts that any correct response must contain."
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Types

MLflow supports the following input types for collecting different kinds of feedback:

### `InputCategorical`

```python
from mlflow.genai.label_schemas import InputCategorical

# Rating scale
rating_input = InputCategorical(
    options=["1 - Poor", "2 - Below Average", "3 - Average", "4 - Good", "5 - Excellent"]
)

# Binary choice
safety_input = InputCategorical(options=["Safe", "Unsafe"])

# Multiple categories
error_type_input = InputCategorical(
    options=["Factual Error", "Logical Error", "Formatting Error", "No Error"]
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputCategoricalList`

```python
from mlflow.genai.label_schemas import InputCategoricalList

# Multiple error types can be present
errors_input = InputCategoricalList(
    options=[
        "Factual inaccuracy",
        "Missing context",
        "Inappropriate tone",
        "Formatting issues",
        "Off-topic content"
    ]
)

# Multiple content types
content_input = InputCategoricalList(
    options=["Technical details", "Examples", "References", "Code samples"]
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputText`

```python
from mlflow.genai.label_schemas import InputText

# General feedback
feedback_input = InputText(max_length=500)

# Specific improvement suggestions
improvement_input = InputText(
    max_length=200  # Limit length for focused feedback
)

# Short answers
summary_input = InputText(max_length=100)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputTextList`

```python
from mlflow.genai.label_schemas import InputTextList

# List of factual errors
errors_input = InputTextList(
    max_count=10,        # Maximum 10 errors
    max_length_each=150  # Each error description limited to 150 chars
)

# Missing information
missing_input = InputTextList(
    max_count=5,
    max_length_each=200
)

# Improvement suggestions
suggestions_input = InputTextList(max_count=3)  # No length limit per item
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### `InputNumeric`

```python
from mlflow.genai.label_schemas import InputNumeric

# Confidence score
confidence_input = InputNumeric(
    min_value=0.0,
    max_value=1.0
)

# Rating scale
rating_input = InputNumeric(
    min_value=1,
    max_value=10
)

# Cost estimate
cost_input = InputNumeric(min_value=0)  # No maximum limit
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Managing Labeling Schemas

Using the API, you can list, update, and delete labeling schemas.

### List Schemas

To get information about an existing schema, use the API `get_label_schema`. You must provide the name of the schema. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

# Get an existing schema
schema = schemas.get_label_schema("response_quality")
print(f"Schema: {schema.name}")
print(f"Type: {schema.type}")
print(f"Title: {schema.title}")
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Update Schemas

To update an existing schema, use the API `create_label_schema` and set the `overwrite` parameter to `True`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical

# Update by recreating with overwrite=True
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True  # Replace existing schema
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Delete Schemas

The following example shows how to delete a labeling schema: ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

# Remove a schema that's no longer needed
schemas.delete_label_schema("old_schema_name")
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Sessions

Schemas are automatically available when creating labeling sessions. The Review App presents questions based on your schema definitions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

# Using schemas in a session (conceptual)
session_schemas = [
    "service_quality",      # Your custom schema
    "response_issues",      # Your custom schema
    schemas.EXPECTED_FACTS  # Built-in schema
]
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

### Schema Design

- Write questions as clear, specific prompts.
- Provide context to guide reviewers.
- Set reasonable limits on text length and list counts.
- For categorical inputs, ensure options are mutually exclusive and comprehensive. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Management

- Use descriptive, consistent names across your schemas.
- When updating schemas, consider the impact on existing sessions.
- Delete unused schemas to keep your workspace organized. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Complete Examples

### Customer Service Evaluation

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import (
    InputCategorical,
    InputCategoricalList,
    InputText,
    InputTextList,
    InputNumeric,
)

# Overall quality rating
quality_schema = schemas.create_label_schema(
    name="service_quality",
    type="feedback",
    title="Rate the overall quality of this customer service response",
    input=InputCategorical(options=["Excellent", "Good", "Average", "Poor", "Very Poor"]),
    instruction="Consider helpfulness, accuracy, and professionalism.",
    enable_comment=True,
)

# Issues identification
issues_schema = schemas.create_label_schema(
    name="response_issues",
    type="feedback",
    title="What issues are present in this response? (Select all that apply)",
    input=InputCategoricalList(options=[
        "Factually incorrect information",
        "Unprofessional tone",
        "Doesn't address the question",
        "Too vague or generic",
        "Contains harmful content",
        "No issues identified"
    ]),
    instruction="Select all issues you identify. Choose 'No issues identified' if the response is problem-free.",
)

# Expected resolution steps
resolution_schema = schemas.create_label_schema(
    name="expected_resolution",
    type="expectation",
    title="What steps should be included in the ideal resolution?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List the key steps a customer service rep should take to properly resolve this issue.",
)

# Confidence in assessment
confidence_schema = schemas.create_label_schema(
    name="assessment_confidence",
    type="feedback",
    title="How confident are you in your assessment?",
    input=InputNumeric(min_value=1, max_value=10),
    instruction="Rate from 1 (not confident) to 10 (very confident)",
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Medical Information Review

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputTextList, InputNumeric

# Safety assessment
safety_schema = schemas.create_label_schema(
    name="medical_safety",
    type="feedback",
    title="Is this medical information safe and appropriate?",
    input=InputCategorical(options=[
        "Safe - appropriate general information",
        "Concerning - may mislead patients",
        "Dangerous - could cause harm if followed"
    ]),
    instruction="Assess whether the information could be safely consumed by patients.",
)

# Required disclaimers
disclaimers_schema = schemas.create_label_schema(
    name="required_disclaimers",
    type="expectation",
    title="What medical disclaimers should be included?",
    input=InputTextList(max_count=3, max_length_each=300),
    instruction="List disclaimers that should be present (e.g., 'consult your doctor', 'not professional medical advice').",
)

# Accuracy of medical facts
accuracy_schema = schemas.create_label_schema(
    name="medical_accuracy",
    type="feedback",
    title="Rate the factual accuracy of the medical information",
    input=InputNumeric(min_value=0, max_value=100),
    instruction="Score from 0 (completely inaccurate) to 100 (completely accurate)",
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
