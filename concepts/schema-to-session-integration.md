---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: e6f6a4b098bb83b5b4fb3e1bd6d4c5f838bcd688466508e80b93fb72b12afd13
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - schema-to-session-integration
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Schema-to-session integration
description: Labeling schemas are associated with labeling sessions in the Review App, and schemas defined in an experiment are automatically available when creating sessions.
tags:
  - mlflow
  - labeling-sessions
  - review-app
  - workflow
timestamp: "2026-06-19T17:58:52.351Z"
---

# Schema-to-Session Integration

**Schema-to-session integration** refers to the process of associating one or more [Labeling Schemas](/concepts/labeling-schemas.md) with a [Labeling Session](/concepts/labeling-session.md) in the MLflow Review App, enabling structured feedback collection from domain experts evaluating GenAI application traces. This integration bridges the gap between question design and review workflows.

## How It Works

When you create a labeling session, you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either `Feedback` (subjective opinions) or `Expectation` (objective ground truth). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The schemas control the question shown to reviewers, the input method (for example, drop-down menu or text box), validation rules and constraints, and optional instructions and comments. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Sessions

Labeling schemas are automatically available when creating labeling sessions. The Review App presents questions based on your schema definitions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The following example shows a conceptual approach to using schemas in a labeling session:

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

## Schema Scope and Uniqueness

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so schema names must be unique within your MLflow experiment. When a schema is associated with a labeling session, it ensures that reviewers see the correct set of questions for the specific evaluation task. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Types of Schemas in Sessions

Labeling schemas come in two types that serve different purposes within a session:

- **Feedback schemas**: Collect subjective assessments like ratings, preferences, or opinions from reviewers.
- **Expectation schemas**: Collect objective ground truth like correct answers or expected behavior.

For details, see Label during development. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Examples of Schema-to-Session Integration

### Customer Service Evaluation Session

The following schemas can be combined in a single labeling session to evaluate customer service responses:

- `service_quality` — Subjective quality rating (feedback schema)
- `response_issues` — Issue identification (feedback schema)
- `expected_resolution` — Expected resolution steps (expectation schema)
- `assessment_confidence` — Confidence rating (feedback schema)

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Medical Information Review Session

For evaluating medical information responses, a session might include:

- `medical_safety` — Safety assessment (feedback schema)
- `required_disclaimers` — Required disclaimers (expectation schema)
- `medical_accuracy` — Accuracy rating (feedback schema)

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined Schemas for Built-in LLM Judges

MLflow provides predefined schema names for the built-in LLM Judges that use expectations. You can create custom schemas using these names to ensure compatibility with the built-in evaluation functionality. The predefined labeling schemas include:

| Schema Name | Type | Description |
|---|---|---|
| `EXPECTED_FACTS` | Expectation | Collects expected facts for a correct response |
| `GUIDELINES` | Expectation | Collects guidelines the model's output should follow |
| `EXPECTED_RESPONSE` | Expectation | Collects the expected correct agent response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Input Types in Integration

When integrating schemas into sessions, the input type determines how reviewers interact with the evaluation question in the Review App. Supported input types include:

- `InputCategorical` — Single selection from options
- `InputCategoricalList` — Multiple selection from options
- `InputText` — Free-form text input
- `InputTextList` — List of text items
- `InputNumeric` — Numeric value within a range

For detailed examples of each input type, see [Labeling schemas input types](/concepts/labeling-schema-input-types.md). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- Write questions as clear, specific prompts for reviewers.
- Provide context to guide reviewers in their assessments.
- Set reasonable limits on text length and list counts.
- For categorical inputs, ensure options are mutually exclusive and comprehensive.
- When updating schemas, consider the impact on existing sessions that already use them.

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The definitions of questions and input methods
- [Labeling Sessions](/concepts/labeling-sessions.md) — Review workflows that use schemas
- [MLflow experiments](/concepts/mlflow-experiment.md) — The scope for schema uniqueness
- Label existing traces — Applying schemas to collect structured feedback
- Build evaluation datasets — Transforming labeled data into test datasets
- Label during development — Distinction between feedback and expectation assessments
- Review App Chat UI — Where labeling schemas are not used

## Next Steps

- Label existing traces — Apply your schemas to collect structured feedback
- [Create labeling sessions](/concepts/labeling-sessions.md) — Organize review workflows using your schemas
- Build evaluation datasets — Transform labeled data into test datasets

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
