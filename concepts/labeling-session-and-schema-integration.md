---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 824b1781ad9b6d71c6794061473131b0a463dbd984c54f0967cf368357ccf912
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.7
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - labeling-session-and-schema-integration
    - schema integration and Labeling session
    - LSASI
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
    - file: create-and-managing-labeling-schemas-databricks-on-aws.md
title: Labeling session and schema integration
description: How labeling schemas are associated with labeling sessions to organize structured human review workflows in the Review App.
tags:
  - mlflow
  - labeling-sessions
  - workflow
timestamp: "2026-06-18T14:52:03.987Z"
---

# Labeling Session and Schema Integration

**Labeling session and schema integration** refers to the process of associating one or more [Labeling Schemas](/concepts/labeling-schemas.md) with a [Labeling Session](/concepts/labeling-session.md) in [MLflow](/concepts/mlflow.md) to collect structured human feedback on GenAI agent traces. This integration ensures that domain experts provide consistent, relevant information when reviewing agent responses. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overview

When you create a labeling session, you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either `Feedback` or `Expectation`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The schemas control:
- The question shown to reviewers.
- The input method (for example, drop-down menu or text box).
- Validation rules and constraints.
- Optional instructions and comments. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Schema Types

Schemas are one of two types:

- **`feedback`**: Subjective assessments like ratings, preferences, or opinions.
- **`expectation`**: Objective ground truth like correct answers or expected behavior. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Using Schemas in a Session

Schemas are automatically available when creating labeling sessions. The [Review App](/concepts/mlflow-review-app.md) will present questions based on your schema definitions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The following example shows how to specify schemas for a session conceptually:

```python
import mlflow.genai.label_schemas as schemas

# Schemas are automatically available when creating labeling sessions
# The Review App will present questions based on your schema definitions
session_schemas = [
    "service_quality",      # Your custom schema
    "response_issues",      # Your custom schema
    schemas.EXPECTED_FACTS  # Built-in schema
]
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Scope

Schemas are scoped to experiments, so schema names must be unique within your [MLflow Experiment](/concepts/mlflow-experiment.md). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Built-in Schema Integration

MLflow provides predefined schema names for the [Built-in LLM Judges](/concepts/built-in-llm-judges.md) that use expectations. You can create custom schemas using these names to ensure compatibility with the built-in evaluation functionality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Examples of Built-in Schemas

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

## Custom Schema Integration

For more control over the feedback you collect, you can create custom labeling schemas and then use them in labeling sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Input Types for Custom Schemas

MLflow supports the following input types for collecting different kinds of feedback:

| Input Type | Description | Use Case |
|---|---|---|
| `InputCategorical` | Single selection from a list of options | Rating scales, binary choices |
| `InputCategoricalList` | Multiple selection from a list of options | Identifying multiple issues or content types |
| `InputText` | Free-text input with optional character limit | General feedback, improvement suggestions |
| `InputTextList` | Multiple text inputs with count and length limits | Listing factual errors, missing information |
| `InputNumeric` | Numeric input with optional min/max range | Confidence scores, rating scales |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Complete Integration Example

The following example creates multiple schemas and demonstrates how they would be used together in a session:

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import (
    InputCategorical,
    InputCategoricalList,
    InputText,
    InputTextList,
    InputNumeric
)

# Overall quality rating
quality_schema = schemas.create_label_schema(
    name="service_quality",
    type="feedback",
    title="Rate the overall quality of this customer service response",
    input=InputCategorical(options=["Excellent", "Good", "Average", "Poor", "Very Poor"]),
    instruction="Consider helpfulness, accuracy, and professionalism.",
    enable_comment=True
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
    instruction="Select all issues you identify. Choose 'No issues identified' if the response is problem-free."
)

# Expected resolution steps
resolution_schema = schemas.create_label_schema(
    name="expected_resolution",
    type="expectation",
    title="What steps should be included in the ideal resolution?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List the key steps a customer service rep should take to properly resolve this issue."
)

# Confidence in assessment
confidence_schema = schemas.create_label_schema(
    name="assessment_confidence",
    type="feedback",
    title="How confident are you in your assessment?",
    input=InputNumeric(min_value=1, max_value=10),
    instruction="Rate from 1 (not confident) to 10 (very confident)"
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

### Schema Design

- Write questions as clear, specific prompts.
- Provide context to guide reviewers.
- Set reasonable limits on text length and list counts.
- For categorical inputs, ensure options are mutually exclusive and comprehensive.

### Schema Management

- Use descriptive, consistent names across your schemas.
- When updating schemas, consider the impact on existing sessions.
- Delete unused schemas to keep your workspace organized.

^[create-and-managing-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) – Define the specific questions that domain experts answer when labeling traces
- [Labeling Sessions](/concepts/labeling-sessions.md) – Organize review workflows using schemas
- [Review App](/concepts/mlflow-review-app.md) – The interface where domain experts apply schemas to provide feedback
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) – The broader practice of collecting expert annotations
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Using labeled data for automated evaluation
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) – Transform labeled data into test datasets
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous quality monitoring

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
2. create-and-managing-labeling-schemas-databricks-on-aws.md
