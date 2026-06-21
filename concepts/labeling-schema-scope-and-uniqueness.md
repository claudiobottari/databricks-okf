---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 52a953f3910055263b5144306de9bcf3a448165e6b0ed0d5ba6a092c64e77626
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-scope-and-uniqueness
    - uniqueness and Labeling schema scope
    - LSSAU
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling schema scope and uniqueness
description: Labeling schemas are scoped to MLflow experiments, requiring unique names within each experiment.
tags:
  - mlflow
  - labeling
  - experiments
timestamp: "2026-06-19T09:33:15.154Z"
---

# Labeling schema scope and uniqueness

**Labeling schema scope and uniqueness** defines the constraints that govern where a labeling schema can be used and how its name must be structured within an MLflow experiment. These rules ensure that schemas are uniquely identifiable and consistently applied when collecting feedback from domain experts in the Review App.

## What is a labeling schema?

A [Labeling Schema](/concepts/labeling-schema.md) is a structured definition of the questions that domain experts answer when labeling existing traces in the Review App. It controls the question presented to reviewers, the input method (e.g., drop-down menu or text box), validation rules, and optional instructions. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Schemas are created when setting up a [Labeling Session](/concepts/labeling-session.md) and are associated with one or more schemas that represent assessments attached to traces. Each assessment is either `Feedback` (subjective ratings, preferences) or `Expectation` (objective ground truth). ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Scope: schemas are scoped to experiments

Labeling schemas are **scoped to experiments**. This means that every schema belongs to a single MLflow experiment and cannot be referenced outside of that experiment without being re-created. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

> Schemas are scoped to experiments, so schema names must be unique within your MLflow experiment.

## Uniqueness: schema names must be unique per experiment

Because schemas are scoped to experiments, **schema names must be unique within your MLflow experiment**. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

This uniqueness constraint applies to all schemas — both custom schemas and predefined schemas provided by MLflow. The following table lists predefined schema names that are available for built-in evaluation functionality:

| Schema name | Type | Usage |
|---|---|---|
| `EXPECTED_FACTS` | Expectation | Collect expected facts |
| `GUIDELINES` | Expectation | Collect expected guidelines |
| `EXPECTED_RESPONSE` | Expectation | Collect expected response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

If you attempt to create a second schema with the same name within the same experiment, MLflow will raise an error unless you set the `overwrite=True` parameter. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

### Duplicate names across different experiments

Because scope is per-experiment, two different experiments **can** have schemas with identical names without conflict. A schema named `response_quality` in one experiment will not interfere with a similarly-named schema in another experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Predefined schema names

MLflow provides several predefined schema names that are designed to work with [Built-in LLM Judges](/concepts/built-in-llm-judges.md). These schemas use the `expectation` type and have specific input formats:

| Name | Type | Input type | Description |
|---|----|----|----|
| `EXPECTED_FACTS` | Expectation | `InputTextList` | Collects a list of expected facts |
| `GUIDELINES` | Expectation | `InputTextList` | Collects expected guidelines |
| `EXPECTED_RESPONSE` | Expectation | `InputText` | Collects a single expected response |

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Custom schema creation

When creating a custom schema, you must provide a unique name within the experiment. The following example creates a custom feedback schema:

```python
quality_schema = schemas.create_label_schema(
    name="response_quality",
    type="feedback",
    title="How would you rate the overall quality of this response?",
    input=InputCategorical(options=["Poor", "Fair", "Good", "Excellent"])
)
```

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Overwriting an existing schema

To modify an existing schema, use `create_label_schema` with `overwrite=True`. The existing schema is replaced — this does not change the uniqueness constraint but allows the same name to be reused with updated parameters. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related concepts

- [Labeling Schema](/concepts/labeling-schema.md) — The structural definition of assessment questions
- [MLflow experiments](/concepts/mlflow-experiment.md) — The organizational unit that scopes schemas
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md) — Predefined evaluation tools that use expectation schemas
- [Labeling Session](/concepts/labeling-session.md) — The workflow that associates schemas with traces
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts label traces

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
