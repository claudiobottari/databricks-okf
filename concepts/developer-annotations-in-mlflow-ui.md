---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f3c53b3cb6d254bba19a1db1c9d6f436bbadf2c935d1c2799717d0b896525620
  pageDirectory: concepts
  sources:
    - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - developer-annotations-in-mlflow-ui
    - DAIMU
  citations:
    - file: 10-minute-demo-collect-human-feedback-databricks-on-aws.md
title: Developer Annotations in MLflow UI
description: Adding developer feedback, ratings, and notes directly through the MLflow UI by creating assessments on trace spans with custom names, numeric values, and rationales
tags:
  - mlflow
  - annotations
  - developer-tools
  - ui
timestamp: "2026-06-19T21:53:12.085Z"
---

```yaml
---
title: Developer Annotations in MLflow UI
summary: Interactive capability for developers to add feedback, scores, and rationales directly on trace spans through the MLflow UI Assessments panel.
sources:
  - 10-minute-demo-collect-human-feedback-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:34:52.682Z"
updatedAt: "2026-06-19T08:46:00.256Z"
tags:
  - mlflow
  - ui
  - annotations
  - developer-tools
aliases:
  - developer-annotations-in-mlflow-ui
  - DAIMU
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 1
---

# Developer Annotations in MLflow UI

**Developer Annotations in MLflow UI** is a feature that allows developers to add assessments and notes directly through the MLflow user interface without writing code. This capability supports internal quality reviews during development by enabling developers to attach feedback, scores, and rationales to specific traces. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Overview

Developer annotations are part of MLflow's [[MLflow Human Feedback Collection]] framework, which supports three feedback types: end-user feedback, developer annotations, and expert feedback via labeling sessions. Annotations are added interactively in the UI and complement automated evaluation metrics by capturing nuanced human assessment. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

Annotations support numeric scores, categorical ratings, and textual rationales. After creation, assessment columns appear in the Logs table for filtering and comparison across traces. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Adding Developer Annotations

To add a developer annotation: ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

1. Navigate to the **Logs** tab of your experiment.
2. Click on a trace to open its details.
3. Click on any span (choose the root span for trace-level feedback).
4. In the **Assessments** tab on the right side, click **Add new assessment**.
5. Specify the **Type** (Feedback), **Name**, **Value**, and **Rationale**.
6. Click **Create** to save the annotation.

![Adding a developer annotation in the MLflow UI](https://assets.docs.databricks.com/_static/images/mlflow3-genai/new-images/human-eval-dev-label.gif) ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Example Annotation

For instance, a developer might create an annotation named `accuracy_score` with a value of `.75` and a rationale explaining why the response only partially covers the topic. After the page is refreshed, columns for the new assessments appear in the Logs table. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Best Practices

- **Use consistent naming**: Choose descriptive names for annotations (e.g., `accuracy_score`, `completeness_rating`) to enable filtering and comparison across traces. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Provide detailed rationales**: Document the reasoning behind each assessment to make annotations useful for team collaboration and future reference. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]
- **Combine with other feedback types**: Developer annotations work alongside [[End-User Feedback Collection via SDK|end-user feedback]] (collected via SDK) and [[Review Apps for Expert Feedback|expert feedback]] (via labeling sessions) to provide a complete picture of application quality. ^[10-minute-demo-collect-human-feedback-databricks-on-aws.md]

## Related Concepts

- [[MLflow Tracing]] — The foundation for associating annotations with specific application runs
- [[MLflow Human Feedback Collection]] — The broader framework for collecting various feedback types
- [[MLflow Evaluation UI|MLflow Evaluation]] — Quantitative evaluation using scorers
- [[MLflow 3 for GenAI|MLflow GenAI]] — MLflow's capabilities for generative AI applications
- [[Labeling Sessions]] — Structured expert review workflows that complement developer annotations

## Sources

- 10-minute-demo-collect-human-feedback-databricks-on-aws.md
```

# Citations

1. [10-minute-demo-collect-human-feedback-databricks-on-aws.md](/references/10-minute-demo-collect-human-feedback-databricks-on-aws-3f033604.md)
