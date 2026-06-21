---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 5b2a17d40b258052e1358f54f31d5ad80b1284152edbb2ee7f85a260cad2d581
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - labeling-schema-scoping-to-experiments
    - LSSTE
  citations:
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: Labeling Schema Scoping to Experiments
description: Labeling schemas are scoped to MLflow experiments, requiring unique names within an experiment and enabling organized, experiment-specific feedback collection.
tags:
  - genai
  - mlflow
  - experiments
timestamp: "2026-06-18T11:18:07.597Z"
---

# Labeling Schema Scoping to Experiments

**Labeling Schema Scoping to Experiments** refers to the design principle that each [Labeling Schema](/concepts/labeling-schema.md) is defined within the context of a single [MLflow Experiment](/concepts/mlflow-experiment.md) and is not shared across experiments. This rule governs how schemas are created, named, and managed in the [Review App](/concepts/mlflow-review-app.md) workflow for human-feedback collection on GenAI traces.

## How Scoping Works

When you create a custom labeling schema using either the MLflow UI or the [`mlflow.genai.label_schemas.create_label_schema()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.label_schemas.create_label_schema) API, the schema is stored under the current active experiment. All subsequent operations on that schema — such as listing, updating, or deleting — are also scoped to that same experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Scoping to experiments means that schemas created in one experiment are invisible to other experiments. This allows different teams or projects to define their own feedback criteria without conflict. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Name Uniqueness Requirement

Because schemas are scoped to an experiment, **schema names must be unique within that experiment**. You cannot create two schemas with identical names in the same experiment. If you attempt to create a schema with a name that already exists, the API call will fail unless you set the `overwrite=True` parameter to replace the existing schema. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

The same name can be used in different experiments without conflict, since each experiment maintains its own namespace for schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Implications for Schema Management

- **Creation**: The `create_label_schema()` API associates the schema with the experiment that is currently active in the MLflow client context or set via `mlflow.set_experiment()`.
- **Retrieval**: The `get_label_schema()` API returns the schema only if it exists in the experiment that is active at the time of the call.
- **Deletion**: The `delete_label_schema()` API removes the schema from its experiment, not from any other experiment.
- **Updates**: Updating a schema (via `overwrite=True`) affects only the copy stored in the experiment where the update occurs.

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Best Practices

- **Use descriptive, consistent names** within each experiment to avoid confusion. Since names must be unique per experiment, prefixing schema names with a project or team identifier is optional but can help when multiple teams share an experiment.
- **Delete unused schemas** to keep the experiment’s schema list organized and avoid hitting any internal limits on schema count.
- **Document the experiment-to-schema mapping** in a shared governance document so that colleagues know which experiment contains the schemas relevant to their work.

^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Relationship to Labeling Sessions

Labeling schemas are associated with a [Labeling Session](/concepts/labeling-session.md) when the session is created. The session, in turn, is linked to the experiment that owns the schemas. When reviewers label traces in the Review App, the questions they see come from the schemas that are attached to the session, all of which are scoped to the same experiment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [MLflow Experiments](/concepts/mlflow-experiment.md)
- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Review App](/concepts/mlflow-review-app.md)
- [Create custom labeling schemas](/concepts/custom-labeling-schema-creation.md)

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md

# Citations

1. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
