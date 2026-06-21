---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37347030673344dab98de772418b4a7640cd1292987cab4e066f7cc9dc013b03
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectation-vs-feedback-label-types
    - EVFLT
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Expectation vs Feedback Label Types
description: "Two distinct label types in MLflow labeling: 'expectation' labels capture ground truth / correct answers for evaluation datasets, while 'feedback' labels capture subjective ratings, classifications, or assessments."
tags:
  - mlflow
  - labeling
  - evaluation
timestamp: "2026-06-19T17:45:53.407Z"
---

# Expectation vs Feedback Label Types

In MLflow's GenAI evaluation and labeling system, there are two distinct types of labeling schemas that domain experts use when reviewing traces: **Expectation** labels and **Feedback** labels. These label types serve different purposes in the evaluation workflow and are defined using the `type` parameter when creating a labeling schema.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Expectation Labels (`type="expectation"`)

**Expectation labels** capture a "ground truth" or correct answer for a given trace. These labels represent what the ideal response should have been, as determined by a domain expert.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Characteristics

- Used when the expert provides a definitive correct answer or reference standard.
- Often take the form of expected facts, ideal responses, or correct classifications.
- Can be directly used to create [Evaluation Datasets](/concepts/evaluation-datasets.md) for systematic testing.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Common Use Cases

- Providing the `expected_facts` for a [Retrieval Augmented Generation (RAG)](/concepts/retrieval-augmented-generation-rag.md) system's response.
- Supplying the correct summary for a user's request.
- Defining the ideal answer against which model outputs can be compared programmatically.

### Example Definition

```python
from mlflow.genai.label_schemas import create_label_schema, InputText

expected_summary = create_label_schema(
    name="expected_summary",
    type="expectation",
    title="Please provide the correct summary for the user's request.",
    input=InputText(),
    overwrite=True,
)
```

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Feedback Labels (`type="feedback"`)

**Feedback labels** capture subjective assessments, ratings, or classifications from domain experts rather than definitive ground truth values.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Characteristics

- Used for subjective evaluations where there may not be a single correct answer.
- Common input types include categorical choices (yes/no), numeric scales, or free-form text.
- Represent human judgment about quality, appropriateness, or adherence to criteria.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Common Use Cases

- Rating a response on a scale of 1-5 for politeness, helpfulness, or accuracy.
- Classifying whether a response met specific criteria (e.g., "Does this answer include a disclaimer?").
- Collecting open-ended qualitative feedback about model behavior.

### Example Definition

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical

summary_quality = create_label_schema(
    name="summary_quality",
    type="feedback",
    title="Is this summary concise and helpful?",
    input=InputCategorical(options=["Yes", "No"]),
    instruction="Please provide a rationale below.",
    enable_comment=True,
    overwrite=True,
)
```

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Key Differences

| Aspect | Expectation Labels | Feedback Labels |
|--------|-------------------|-----------------|
| **Purpose** | Capture ground truth or correct answer | Capture subjective assessment or rating |
| **Objectivity** | Objective (single correct answer expected) | Subjective (variance across reviewers expected) |
| **Reusability** | Can be used directly in evaluation datasets | Used for quality analysis and improvement |
| **Typical Inputs** | Free-form text, structured data | Categorical choices, numeric scales, comments |

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Using Labels in Evaluation Workflows

Both expectation and feedback labels are stored as [Assessment](/concepts/assessments.md) objects on each [Trace](/concepts/traces.md) within a [Labeling Session](/concepts/labeling-session.md). They can be retrieved programmatically for analysis.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Converting to Evaluation Datasets

Expectation labels are particularly valuable for creating [Evaluation Datasets](/concepts/evaluation-datasets.md). These datasets can be used with `mlflow.genai.evaluate()` to systematically test new versions of a GenAI application against expert-defined ground truth. Feedback labels, while not typically used as direct evaluation criteria, provide qualitative insights that can inform model improvements and judge alignment.^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) — The configuration that defines how labels are collected
- [Labeling Sessions](/concepts/labeling-sessions.md) — Organizes traces for review with selected schemas
- [Review App](/concepts/mlflow-review-app.md) — The interface where domain experts provide labels
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Systematic testing using evaluation datasets
- [Human Feedback](/concepts/mlflow-human-feedback-collection.md) — The broader process of collecting expert input

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
