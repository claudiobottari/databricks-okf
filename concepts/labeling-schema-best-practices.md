---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e50666aa24683a390809f1ae41d3a6b656f4510d26ba698f7f79c650c37124d
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.93
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-best-practices
    - LSBP
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schema best practices
description: Guidelines for effective schema design including clear questions, specific prompts, reasonable limits, mutually exclusive options, descriptive naming, and lifecycle management.
tags:
  - mlflow
  - best-practices
  - labeling
  - schema-design
timestamp: "2026-06-19T17:58:56.566Z"
---

---
title: Labeling Schema Best Practices
summary: Guidelines for effective schema design including clear question writing, providing context, reasonable length limits, mutually exclusive categorical options, descriptive naming, and considering impact on existing sessions when updating.
sources:
  - create-and-manage-labeling-schemas-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T14:33:23.143Z"
updatedAt: "2026-06-19T14:33:23.143Z"
tags:
  - mlflow
  - best-practices
  - schema-design
aliases:
  - labeling-schema-best-practices
  - LSBP
confidence: 0.96
provenanceState: extracted
inferredParagraphs: 0
---

## Labeling Schema Best Practices

Labeling schemas define the questions that domain experts answer when labeling existing traces in the Review App. Well-designed schemas ensure that the collected feedback is consistent, actionable, and aligned with evaluation goals. The following best practices help create effective schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Design

Write questions as clear, specific prompts. The title should be an unambiguous question, and the instruction field should provide context to guide reviewers—for example, specifying which aspects to consider when rating. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

For categorical inputs, ensure options are mutually exclusive and collectively comprehensive. If reviewers need to select multiple applicable items, use `InputCategoricalList` instead of `InputCategorical`. For binary assessments, use clear options like `["Safe", "Unsafe"]` to avoid confusion. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Set reasonable limits on text length and list counts. For text inputs, use `max_length` to constrain verbosity; for text lists, use `max_count` and `max_length_each` to keep feedback focused. Numeric ranges should reflect the intended scale (e.g., 1–10 for ratings, 0.0–1.0 for confidence scores). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Consider enabling comments (`enable_comment=True`) on feedback schemas when reviewers may need to justify their choice or provide additional nuance. Avoid enabling comments on expectation schemas where objective data is sufficient. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Management

Use descriptive, consistent names across your schemas. Schema names must be unique within an MLflow experiment. When updating an existing schema using the API, set `overwrite=True` and consider the impact on existing labeling sessions—changing options or input types may break previously collected data. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Delete unused schemas to keep the workspace organized and prevent accidental reuse. Use `delete_label_schema()` to remove schemas that are no longer needed. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Schema Type Selection

Choose the correct schema type:
- `feedback` for subjective assessments (e.g., ratings, preferences, opinions).
- `expectation` for objective ground truth (e.g., correct answers, required disclaimers).

This distinction helps downstream processes—such as generating evaluation datasets or aligning with built-in [LLM Judges](/concepts/llm-judges.md)—interpret the labels correctly. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Compatibility with Built-in Judges

MLflow provides predefined schema names (e.g., `EXPECTED_FACTS`, `GUIDELINES`, `EXPECTED_RESPONSE`) for [Built-in LLM Judges](/concepts/built-in-llm-judges.md). When creating custom schemas that should work with automated evaluation, reuse these predefined names with the `overwrite=True` flag to ensure compatibility. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — Definition and lifecycle
- [Review App](/concepts/mlflow-review-app.md) — Where schemas are used for trace labeling
- [Labeling Sessions](/concepts/labeling-sessions.md) — How schemas are associated with review workflows
- [Input types for labeling schemas](/concepts/input-types-for-custom-schemas.md) — Available input widgets and their parameters
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined evaluation functions that use expectation schemas
- [Build Evaluation Datasets](/concepts/evaluation-datasets.md) — Transform labeled data into test datasets

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
