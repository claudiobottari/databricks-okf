---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d387769c9f543559143b3e0ca8e09ffffead2f30078005b94aae45275aa978ff
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - label-schemas
    - Label Schema Types
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Label Schemas
description: Definition of structured feedback fields (categorical or text) used in labeling sessions to collect targeted expert assessments.
tags:
  - mlflow
  - schemas
  - labeling
  - feedback
timestamp: "2026-06-19T13:49:08.397Z"
---

# Label Schemas

**Label Schemas** define the structure and type of feedback collected during expert review sessions in the [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluation workflow. They specify what kind of data reviewers should provide — such as categorical assessments, free-text explanations, or numeric scores — and serve as templates for creating [Labeling Sessions](/concepts/labeling-sessions.md).

## Overview

Label schemas are created using the `create_label_schema()` function from the `mlflow.genai.label_schemas` module. Each schema has a name, a feedback type (either `"feedback"` or `"expectation"`), a human-readable title, and an input type that determines the format of the collected data.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Label schemas are reusable definitions that can be attached to multiple labeling sessions, enabling consistent evaluation criteria across different review rounds. They are also the mechanism by which expert reviewers provide ground truth assessments that can later be used for automated evaluation.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Schema Types

Label schemas support two primary types of feedback:

### Feedback Schemas

Feedback schemas collect reviewer assessments about a trace's quality. For example, a `response_accuracy` feedback schema might ask reviewers to categorize responses as `"Accurate"`, `"Partially Accurate"`, or `"Inaccurate"`.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expectation Schemas

Expectation schemas collect ideal or correct responses from expert reviewers. For example, an `expected_response` expectation schema asks reviewers to provide the correct answer to a question, which can later be used as ground truth for automated scoring.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Input Types

Label schemas define the format of input reviewers will provide:

### InputCategorical

Used for multiple-choice assessments. Reviewers select from a predefined set of options. This input type is commonly used for feedback schemas where reviewers rate responses against fixed quality tiers.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### InputText

Used for free-text responses. Reviewers type their assessment or ideal answer. This input type is commonly used for expectation schemas where reviewers provide the correct answer in their own words.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Creating a Label Schema

Schemas are created using the `create_label_schema()` function:

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

# Create a feedback schema with categorical options
accuracy_schema = create_label_schema(
    name="response_accuracy",
    type="feedback",
    title="Is the response factually accurate?",
    input=InputCategorical(options=["Accurate", "Partially Accurate", "Inaccurate"]),
    overwrite=True
)

# Create an expectation schema with free-text input
ideal_response_schema = create_label_schema(
    name="expected_response",
    type="expectation",
    title="What would be the ideal response?",
    input=InputText(),
    overwrite=True
)
```

The `overwrite=True` parameter allows re-creating or updating a schema with the same name.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Using Schemas in Labeling Sessions

Once defined, label schemas are referenced by name when creating a [Labeling Session](/concepts/labeling-session.md):

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[accuracy_schema.name, ideal_response_schema.name],
)
```

Multiple schemas can be attached to a single session, allowing reviewers to provide both categorical assessments and free-text corrections in one review.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Integration with Evaluation

Expert feedback collected through label schemas can be used for automated evaluation. For example, an `expected_response` expectation schema provides ground truth that the [Correctness Scorer](/concepts/correctness-scorer.md) uses to evaluate the quality of LLM responses:

```python
from mlflow.genai.scorers import Correctness

eval_results = mlflow.genai.evaluate(
    data=labeled_traces,
    predict_fn=my_chatbot,
    scorers=[Correctness()]  # Compares outputs to expected_response
)
```

The Correctness scorer compares the model's output against the expert-provided `expected_response`, giving quantitative feedback on alignment with expert expectations.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Managing Schemas in the UI

Label schemas can also be managed through the MLflow 3 UI:

1. On the Experiment page, navigate to the **Labeling** tab.
2. Use the **Schemas** tab to add new label schemas.
3. Use the **Sessions** tab to create new labeling sessions that reference your schemas.

This provides a visual interface for schema management alongside the programmatic API.^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [Labeling Sessions](/concepts/labeling-sessions.md) — Review sessions that use label schemas to collect expert feedback
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Collecting end-user and expert feedback for GenAI evaluation
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that consumes expert assessments
- [Correctness Scorer](/concepts/correctness-scorer.md) — An automated scorer that uses expert-provided expected responses
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying evaluation criteria to production environments

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
