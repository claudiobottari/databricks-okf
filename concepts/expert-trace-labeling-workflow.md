---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a7c78458e4b5ddf13c3434789ad9412e86b13e4f997b8e4b75b65f29fe674ca7
  pageDirectory: concepts
  sources:
    - collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
  confidence: 1
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - expert-trace-labeling-workflow
    - ETLW
    - Trace Labeling
  citations:
    - file: collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md
title: Expert Trace Labeling Workflow
description: The end-to-end process of identifying traces for expert review, creating labeling sessions with schemas, adding traces, having domain experts label them via the Review App, and retrieving labels for evaluation datasets.
tags:
  - mlflow
  - workflow
  - human-feedback
  - evaluation
timestamp: "2026-06-19T14:16:05.475Z"
---

# Expert Trace Labeling Workflow

The **Expert Trace Labeling Workflow** is a structured process for collecting domain expert feedback on MLflow Traces from GenAI applications. It enables organizations to systematically capture human judgments about agent behavior, response quality, and expected outcomes.

## When to Use Expert Trace Labeling

Expert labeling is most valuable when automated judges are insufficient for evaluating your GenAI application. Key scenarios include:

- **Ambiguous or borderline quality**: Traces where response quality is difficult to assess automatically
- **Edge cases**: Unusual scenarios not covered by your existing automated judges
- **Metric disagreements**: Cases where automated evaluation metrics conflict with human perception of quality
- **Representative sampling**: Capturing diverse user interaction patterns for comprehensive coverage

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Prerequisites

Domain experts must be provisioned in your Databricks account and have `CAN_EDIT` permission on the MLflow experiment where traces are logged. They do not need access to your Databricks workspace. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Required software:
- MLflow version 3.1.0 or higher
- `pip install --upgrade "mlflow[databricks]>=3.1.0" openai "databricks-connect>=16.1"`

## Workflow Steps

### Step 1: Create an Application with Tracing

Before collecting feedback, ensure your GenAI application logs [[MLflow Trace|MLflow Traces]]. Traces capture inputs, outputs, and intermediate steps including tool calls and retriever actions. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

Use `@mlflow.trace(span_type="RETRIEVER")` decorator on retriever functions so documents are rendered properly in the Review App. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 2: Define Labeling Schemas

[Labeling Schemas](/concepts/labeling-schemas.md) define the questions and input types for expert feedback. Two schema types exist:

- **Expectation type (`type="expectation"`)**: Collects ground truth or correct answers (e.g., `expected_facts` for RAG responses)
- **Feedback type (`type="feedback"`)**: Gathers subjective assessments, ratings, or classifications

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

# Collect feedback on summary quality
summary_quality = create_label_schema(
    name="summary_quality",
    type="feedback",
    title="Is this summary concise and helpful?",
    input=InputCategorical(options=["Yes", "No"]),
    enable_comment=True,
    overwrite=True,
)

# Collect expected ground truth
expected_summary = create_label_schema(
    name="expected_summary",
    type="expectation",
    title="Please provide the correct summary for the user's request.",
    input=InputText(),
    overwrite=True,
)
```

### Step 3: Create a Labeling Session

A [Labeling Session](/concepts/labeling-session.md) is an [MLflow Run](/concepts/mlflow-run.md) that organizes traces for expert review. It acts as a queue for the review process. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
from mlflow.genai.labeling import create_labeling_session

label_summaries = create_labeling_session(
    name="label_summaries",
    assigned_users=[],
    label_schemas=[summary_quality.name, expected_summary.name],
)
```

### Step 4: Generate Traces and Add to Labeling Session

Traces are copied into the labeling session so labels don't affect original logged traces. Add traces programmatically or via the UI by selecting traces in the **Trace** tab and clicking **Export Traces**. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

```python
# Add traces to the session
label_summaries.add_traces(traces)

# Share URL with domain experts
print(f"Share this Review App with your team: {label_summaries.url}")
```

### Step 5: Expert Review via Review App

The [MLflow Review App](/concepts/mlflow-review-app.md) renders trace content for domain experts:

- **RETRIEVER spans**: Documents are displayed as retrieved content
- **OpenAI format messages**: Chat conversations are rendered with tool calls
- **Dictionaries**: Pretty-printed JSON

^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Customize the Review App UI (Optional)

For custom trace visualization or specialized workflows, deploy the customizable Review App Template from the [GitHub repository](https://github.com/databricks-solutions/custom-mlflow-review-app). This open-source template uses the same MLflow backend APIs while giving full control over the frontend experience. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

### Step 6: View and Use Collected Labels

Labels are stored as `Assessment` objects on each `Trace`. Retrieve them programmatically:

```python
labeled_traces_df = mlflow.search_traces(run_id=label_summaries.mlflow_run_id)
```

Expectation-type labels (like `expected_summary`) are valuable for creating [Evaluation Datasets](/concepts/evaluation-datasets.md) that can be used with `mlflow.genai.evaluate()` for systematic testing. ^[collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md) - Define criteria and input types for expert feedback
- [Labeling Sessions](/concepts/labeling-sessions.md) - Organize traces for review
- [[MLflow Trace|MLflow Traces]] - Capture application execution data
- [Evaluation Datasets](/concepts/evaluation-datasets.md) - Create test sets from expert labels
- Align Judges with Human Feedback - Improve automated evaluation accuracy

## Sources

- collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md

# Citations

1. [collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws.md](/references/collect-feedback-and-expectations-by-labeling-existing-traces-databricks-on-aws-baf6bcf1.md)
