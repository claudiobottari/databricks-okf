---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 18be3767be949ad222889f285dcf6ba46a392cfc2085e03a4d0c65cdc6fa1340
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.98
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-lifecycle-management
    - LSLM
    - LLM
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling Schema Lifecycle Management
description: "CRUD operations for labeling schemas using the MLflow API: listing (get_label_schema), creating/updating (create_label_schema with overwrite=True), and deleting (delete_label_schema), with schemas scoped to experiments."
tags:
  - mlflow
  - api
  - management
timestamp: "2026-06-19T14:33:57.345Z"
---

---  
title: Labeling schema lifecycle management  
summary: "API operations for managing labeling schemas: creating (with overwrite), listing, updating, and deleting schemas scoped to MLflow experiments."  
sources:  
  - create-and-manage-labeling-schemas-databricks-on-aws.md  
kind: concept  
createdAt: "2026-06-18T11:18:20.347Z"  
updatedAt: "2026-06-19T09:32:50.945Z"  
tags:  
  - mlflow  
  - api  
  - schema-management  
aliases:  
  - labeling-schema-lifecycle-management  
  - LSLM  
confidence: 1  
provenanceState: extracted  
inferredParagraphs: 0  
---

# Labeling Schema Lifecycle Management

**Labeling Schema Lifecycle Management** refers to the complete process of creating, updating, deleting, and governing [Labeling Schemas](/concepts/labeling-schemas.md) throughout their use in the [Review App](/concepts/mlflow-review-app.md). A labeling schema defines the specific question, input method, validation rules, and instructions that domain experts see when labeling existing traces. Proper lifecycle management ensures that schemas remain accurate, consistent, and aligned with evolving evaluation goals. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## How Labeling Schemas Work

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md), so their names must be unique within the experiment. Each schema is one of two types: `feedback` for subjective assessments (ratings, preferences, opinions) or `expectation` for objective ground truth (correct answers, expected behaviors). When you create a labeling session, you associate it with one or more schemas; each schema represents an assessment that is attached to a trace. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Creating Labeling Schemas

### Creating via the UI

1. In the Databricks workspace, click **Experiments** in the left sidebar.
2. Click the experiment name to open it.
3. Click **Labeling schemas** in the sidebar.
4. To edit an existing schema, select it. To create a new one, click **Add Label Schema** and fill in the fields.
5. When you select an **Input type**, additional fields appear for constraints (e.g., length limits, categorical options, numeric range).
6. A preview panel on the right updates as you configure the schema.
7. Click **Save** when finished. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Creating via the API

Use `mlflow.genai.label_schemas.create_label_schema()`. Every schema requires a `name`, `type`, `title`, and an input specification object. Optional parameters include `instruction` and `enable_comment`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The following example creates a feedback schema for rating response quality using a categorical input:

```python
import mlflow.genai.label_schemas as schemas
from mlflow.genai.label_schemas import InputCategorical, InputText

quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"]),
    instruction="Consider accuracy, relevance, and helpfulness when rating.",
)
```

To create an expectation schema that collects ground truth facts as a list of text entries:

```python
facts_schema = schemas.create_label_schema(
    name="required_facts",
    type="expectation",
    title="What facts must be included in a correct response?",
    input=InputTextList(max_count=5, max_length_each=200),
    instruction="List key facts that any correct response must contain.",
)
```

The `enable_comment` parameter can be added to any input type to allow reviewers to attach an additional free-text comment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Predefined Schema Names for Built-in LLM Judges

MLflow provides predefined schema names for the [LLM Judges](/concepts/llm-judges.md) that use expectations. You can create custom schemas using these names to ensure compatibility with built-in evaluation functionality. The predefined names include `EXPECTED_FACTS`, `GUIDELINES`, and `EXPECTED_RESPONSE`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Listing Schemas

To retrieve information about an existing schema by name, use `mlflow.genai.label_schemas.get_label_schema()`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schema = schemas.get_label_schema("response_quality")
print(f"Schema: {schema.name}")
print(f"Type: {schema.type}")
print(f"Title: {schema.title}")
```

## Updating Schemas

There is no separate update method. Instead, call `create_label_schema()` with the same name and set `overwrite=True`. This replaces the existing schema definition. All parameters except the name can be changed. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
updated_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="Rate the response quality (updated question)",
    input=InputCategorical(options=["Excellent", "Good", "Fair", "Poor", "Very Poor"]),
    instruction="Updated: Focus on factual accuracy above all else.",
    overwrite=True,
)
```

## Deleting Schemas

To remove a schema that is no longer needed, use `mlflow.genai.label_schemas.delete_label_schema()`. Provide the schema name as the argument. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
schemas.delete_label_schema("old_schema_name")
```

## Input Types for Custom Schemas

MLflow supports several input types, each with configurable constraints. The choice of input type determines how reviewers provide their feedback. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

| Input Type | Description | Key Parameters |
|-----------|-------------|----------------|
| `InputCategorical` | Single selection from a list of options | `options` |
| `InputCategoricalList` | Multiple selections from a list of options | `options` |
| `InputText` | Free-text input | `max_length` |
| `InputTextList` | A list of text entries | `max_count`, `max_length_each` |
| `InputNumeric` | Numeric value within a range | `min_value`, `max_value` |

`enable_comment` can be added to any input type to allow reviewers to attach an additional free-text comment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Sessions

Schemas are associated with a [Labeling Session](/concepts/labeling-session.md) when the session is created. The Review App presents each configured schema's question and input widget to the reviewer. Schema names are passed as a list to the session creation workflow (typically through the Review App UI or a separate API). Built-in schema names can be mixed with custom schema names in the same session. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices for Lifecycle Management

- **Write clear, specific prompts.** The title and instruction should leave no ambiguity about what the reviewer should evaluate.
- **Set reasonable limits.** For `InputTextList` and `InputText`, use `max_count` and `max_length` to keep responses focused and consistent.
- **Ensure categorical options are exhaustive and mutually exclusive.** Reviewers should not have to choose between overlapping or incomplete options.
- **Use descriptive, consistent naming.** Schema names should be stable across experiments so they can be reused in multiple sessions.
- **Consider the impact of updates on existing sessions.** Overwriting a schema does not retroactively change the data already collected; reviews in progress may use the previous definition until the session is closed.
- **Delete unused schemas** to keep the experiment's schema list clean and avoid confusion. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schema](/concepts/labeling-schema.md) — The core definition of a feedback question and input type
- [Labeling Sessions](/concepts/labeling-sessions.md) — Workflows that apply schemas to reviewed traces
- [Review App](/concepts/mlflow-review-app.md) — The UI where reviewers interact with schemas
- [LLM Judges](/concepts/llm-judges.md) — Built-in evaluators that can use predefined schema names
- [MLflow Experiments](/concepts/mlflow-experiment.md) — The scoping container for schemas and runs

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
