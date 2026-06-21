---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1c0ff553b59431a1d66b8ef105955c5821a10fe91beb8cc53af64ac7228f6487
  pageDirectory: concepts
  sources:
    - get-started-mlflow-3-for-genai-databricks-on-aws.md
  confidence: 0.85
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labeling-schemas-and-sessions
    - Sessions and MLflow Labeling Schemas
    - MLSAS
  citations:
    - file: get-started-mlflow-3-for-genai-databricks-on-aws.md
title: MLflow Labeling Schemas and Sessions
description: Programmatic API (create_label_schema, create_labeling_session) to define what feedback to collect from human reviewers and organize traces for review.
tags:
  - mlflow
  - labeling
  - feedback
  - sdk
timestamp: "2026-06-19T10:44:09.670Z"
---

Here is the wiki page for "MLflow Labeling Schemas and Sessions".

---

## MLflow Labeling Schemas and Sessions

**MLflow Labeling Schemas and Sessions** are the mechanisms for collecting structured human feedback on GenAI application traces within MLflow. They enable domain experts and reviewers to evaluate and annotate model outputs, complementing automated [LLM-as-a-Judge](/concepts/llm-as-a-judge.md) evaluation with human judgment.

## Overview

Human feedback is a critical component of GenAI application development. While automated evaluation provides scalable quality assessment, domain experts can confirm quality, provide correct answers, and define guidelines for future evaluation. MLflow provides two key abstractions for collecting this feedback: labeling schemas and labeling sessions.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Labeling Schemas

A **labeling schema** defines the structure of feedback to collect from reviewers. Schemas specify the type of feedback, its format, and the options available to reviewers. They are created using the MLflow GenAI SDK and can be reused across multiple sessions.

### Creating a Labeling Schema

Use `mlflow.genai.label_schemas.create_label_schema()` to define a schema. The schema requires a name, a type (e.g., `"feedback"`), a title for display, and an input specification.

```python
from mlflow.genai.label_schemas import create_label_schema, InputCategorical, InputText

humor_schema = create_label_schema(
    name="response_humor",
    type="feedback",
    title="Rate how funny the response is",
    input=InputCategorical(options=["Very funny", "Slightly funny", "Not funny"]),
    overwrite=True,
)
```

Supported input types include:

- **InputCategorical**: Provides a set of predefined options for reviewers to choose from.
- **InputText**: Allows free-form text input from reviewers.

The `overwrite=True` parameter allows replacing an existing schema with the same name.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Labeling Sessions

A **labeling session** groups together a set of traces and the schemas used to annotate them. Sessions are created programmatically and shared with reviewers via a unique URL. Each session is associated with a specific MLflow experiment.

### Creating a Labeling Session

Use `mlflow.genai.labeling.create_labeling_session()` to create a session. Provide a name and a list of label schemas to use for annotation.

```python
from mlflow.genai.labeling import create_labeling_session

labeling_session = create_labeling_session(
    name="quickstart_review",
    label_schemas=[humor_schema.name],
)
```

### Adding Traces to a Session

Traces are added to a session using `labeling_session.add_traces()`. Traces can be retrieved from the experiment using `mlflow.search_traces()`.

```python
traces = mlflow.search_traces(max_results=10)
labeling_session.add_traces(traces)
```

### Sharing with Reviewers

After creating the session and adding traces, the session URL can be shared with reviewers.

```python
print(f"Share this link with reviewers: {labeling_session.url}")
```

Reviewers access the Review App through this URL, where they can view traces and provide annotations according to the defined schemas.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Accessing the Labeling UI

Users can also create and manage schemas and sessions through the MLflow Experiment UI:

1. Open the experiment in the MLflow UI.
2. Click the **Labeling** tab.
3. Use the **Sessions** and **Schemas** sub-tabs to add new label schemas and create new sessions.

## Retrieving Feedback

### Via MLflow UI

To view collected feedback, open the active experiment and click the **Labeling** tab.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

### Via SDK

Feedback can be retrieved programmatically using `mlflow.log_feedback()` within an application, and analyzed using `mlflow.search_traces()`. For more details, see mlflow.search_traces() API|Search traces programmatically and Collect user feedback.^[get-started-mlflow-3-for-genai-databricks-on-aws.md]

## Workflow Summary

1. Define a [Labeling Schema](/concepts/labeling-schema.md) that specifies what feedback to collect (e.g., categorical rating or free text).
2. Create a [Labeling Session](/concepts/labeling-session.md) and associate it with one or more schemas.
3. Add traces from your experiment to the session.
4. Share the session URL with reviewers.
5. Reviewers annotate traces in the Review App.
6. Retrieve feedback through the UI or SDK for analysis.

## Best Practices

- **Define clear schemas**: Use categorical inputs with well-defined options to ensure consistent annotations.
- **Overwrite schemas during development**: Use `overwrite=True` when iterating on schema definitions.
- **Retrieve traces before session creation**: Use `mlflow.search_traces()` to find the specific traces you want to annotate.
- **Align schemas with evaluation criteria**: Design label schemas that complement the [[scorers]] used in automated evaluation programs.

## Related Concepts

- [MLflow Tracing](/concepts/mlflow-tracing.md) — The mechanism for recording LLM requests, responses, and metrics.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — Automated evaluation using LLM-as-a-judge and custom scorers.
- [Human Feedback Collection](/concepts/mlflow-human-feedback-collection.md) — Broader topic covering both in-app feedback and expert review.
- [MLflow Experiment UI](/concepts/mlflow-experiment.md) — The dashboard for viewing traces, evaluations, and labeling sessions.
- [Review App](/concepts/mlflow-review-app.md) — The interface used by reviewers to provide annotations.

## Sources

- get-started-mlflow-3-for-genai-databricks-on-aws.md

# Citations

1. [get-started-mlflow-3-for-genai-databricks-on-aws.md](/references/get-started-mlflow-3-for-genai-databricks-on-aws-4186f156.md)
