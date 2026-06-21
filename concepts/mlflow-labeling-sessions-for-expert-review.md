---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 6e250f921c85204fe52bafdbf7b9fd144f86d1466fe4891854f2647054347afe
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-labeling-sessions-for-expert-review
    - MLSFER
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: MLflow Labeling Sessions for Expert Review
description: Structured workflow for sending GenAI app traces to domain experts for review via labeling sessions, enabling authoritative ground-truth feedback collection.
tags:
  - mlflow
  - labeling
  - expert-review
  - genai
timestamp: "2026-06-19T17:22:25.899Z"
---

---
title: MLflow Labeling Sessions for Expert Review
summary: Structured expert review process using labeling sessions (label schemas, session creation, trace assignment) to collect authoritative ground-truth labels on GenAI responses.
sources:
  - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:34:43.272Z"
updatedAt: "2026-06-18T10:34:43.272Z"
tags:
  - mlflow
  - expert-review
  - labeling
aliases:
  - mlflow-labeling-sessions-for-expert-review
  - MLSFER
confidence: 0.95
provenanceState: extracted
inferredParagraphs: 0
---

## MLflow Labeling Sessions for Expert Review

**MLflow Labeling Sessions** provide a structured workflow for collecting expert feedback on [traced](/concepts/mlflow-tracing.md) GenAI application runs. When end-user feedback (e.g., thumbs-down) signals a potential quality issue, a labeling session lets domain experts review specific traces, assess response accuracy, and provide authoritative ground-truth labels that can later drive evaluation. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Creating a Labeling Session

To create a labeling session, you first define one or more **label schemas** using `mlflow.genai.label_schemas.create_label_schema()`. Each schema specifies the type of feedback to collect — for example, a categorical assessment (e.g., “Accurate”, “Partially Accurate”, “Inaccurate”) or a free-text expectation (e.g., “What would be the ideal response?”). Schemas can be set to `overwrite=True` to allow updates. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Once schemas are defined, you create a session with `mlflow.genai.labeling.create_labeling_session()`, passing a session name and the list of schema names. The session is backed by an [MLflow Run](/concepts/mlflow-run.md); its URL can be shared with reviewers. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Labeling sessions can also be created directly in the MLflow 3 UI via the **Labeling** tab on the Experiment page, where you manage sessions and schemas through the **Sessions** and **Schemas** tabs. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Adding Traces to a Session

After creating the session, you add traces to it using the `labeling_session.add_traces()` method. Traces are typically retrieved from the current experiment via `mlflow.search_traces()`. You can add multiple traces at once. The session then becomes the central place where experts review those traces and apply labels. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### Expert Review Workflow

Reviewers open the session’s **Review App URL** to see each trace, including the original question, the app’s response, and any end-user feedback that has been recorded. From there, they:

1. Assess the response against the defined schemas (e.g., choose “Inaccurate” from a categorical list).
2. Provide ideal or corrected responses in free-text fields.
3. Submit their expert assessments as ground truth. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

This workflow gives domain experts a clear, isolated environment to evaluate model outputs without interference from the development team.

### Using Expert Feedback for Evaluation

Once experts have labeled traces, those labels can be used to evaluate the app quantitatively. Retrieve the labeled traces by searching with the session’s `mlflow_run_id`:

```python
labeled_traces = mlflow.search_traces(run_id=labeling_session.mlflow_run_id)
```

Then pass the traces to `mlflow.genai.evaluate()` along with a `predict_fn` and an appropriate scorer — such as the [Correctness Scorer](/concepts/correctness-scorer.md) — which compares the app’s outputs against the expert-provided expectations (e.g., `expected_response`). ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

For production workflows, Databricks recommends adding labeled traces to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) to maintain version tracking and lineage. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

### References

- For more advanced annotation techniques during development, see Label during development.
- To test your app interactively with experts, see Vibe check with domain experts.
- For systematic expert review of existing traces, see [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md).

## Sources

- *10-minute demo: Collect human feedback | Databricks on AWS* (source file: `10-minute-demo-collect-human-feedback-databricks-on-aws.md`)

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
