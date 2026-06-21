---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 883805c9dcd9e0d22867d9d52366dd0fab77b66df6f14e2256e9f1a9398795ca
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-integration-with-sessions
    - LSIWS
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schema integration with sessions
description: How labeling schemas are associated with labeling sessions and presented in the Review App to collect structured feedback.
tags:
  - mlflow
  - labeling-sessions
  - review-app
timestamp: "2026-06-19T09:32:57.643Z"
---

---
title: Labeling Schema Integration with Sessions
summary: How labeling schemas are associated with labeling sessions to collect structured human feedback on GenAI traces in the Review App.
sources:
  - create-and-manage-labeling-schemas-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T10:00:00.000Z"
updatedAt: "2026-06-19T10:00:00.000Z"
tags:
  - mlflow
  - labeling
  - human-feedback
  - sessions
aliases:
  - labeling-schema-integration-with-sessions
  - LSIS
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

# Labeling Schema Integration with Sessions

**Labeling Schema Integration with Sessions** describes how [Labeling Schemas](/concepts/labeling-schemas.md) are attached to [Labeling Sessions](/concepts/labeling-sessions.md) in MLflow to collect structured human feedback on GenAI traces. Schemas define the questions reviewers answer; sessions organize the review workflow and associate one or more schemas with a batch of traces.

## How Integration Works

When you create a labeling session in the [Review App](/concepts/mlflow-review-app.md), you associate it with one or more labeling schemas. Each schema represents an assessment that is attached to a trace. Assessments are either `Feedback` (subjective) or `Expectation` (objective ground truth). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The schemas control the questions shown to reviewers, the input method (e.g., drop-down menu or text box), validation rules, and optional instructions and comments. The Review App then presents these schema-defined questions for each trace in the session. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Labeling schemas apply only when using the Review App to label existing traces. They are not used for vibe checks in the Review App Chat UI. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Associating Schemas with Sessions

Schemas are scoped to [MLflow experiments](/concepts/mlflow-experiment.md). Schema names must be unique within an experiment. When you create a labeling session, you list the schema names that the session will use. The session inherits those schemas from the same experiment where the session is created. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Example

The following conceptual example shows how schemas are referenced when creating a session (actual session creation occurs through the Review App UI or other APIs): ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

```python
import mlflow.genai.label_schemas as schemas

# Schemas are automatically available when creating labeling sessions.
# The Review App will present questions based on your schema definitions.

session_schemas = [
    "service_quality",      # Custom feedback schema
    "response_issues",      # Custom feedback schema
    schemas.EXPECTED_FACTS  # Predefined schema for built-in LLM judges
]
```

You can include both custom schemas and predefined schema names (e.g., `EXPECTED_FACTS`, `GUIDELINES`, `EXPECTED_RESPONSE`) that are compatible with [Built-in LLM Judges](/concepts/built-in-llm-judges.md). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Automatic Availability

Schemas are automatically available when creating labeling sessions — they do not need to be registered or bound at the API level beyond specifying their names. The Review App reads the schema definitions from the experiment and presents the corresponding input forms to reviewers. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices for Session Integration

- **Design schemas per session purpose.** Create dedicated schemas for different evaluation goals (e.g., service quality, safety, factual accuracy) and select only the relevant ones for each session. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Use consistent naming.** Descriptive, consistent schema names make it easier to select the right schemas when creating sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Consider the impact of updates.** When you update a schema (via `overwrite=True`), existing sessions that use that schema are unaffected; the changes apply only to future sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Clean up unused schemas.** Delete schemas no longer needed to keep the experiment organized and avoid confusion when creating sessions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Review App](/concepts/mlflow-review-app.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [MLflow experiments](/concepts/mlflow-experiment.md)
- Label existing traces
- [Feedback types (Feedback vs. Expectation)](/concepts/assessment-types-feedback-vs-expectation.md)

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
