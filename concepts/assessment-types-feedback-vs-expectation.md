---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: c4a5d985f2b57750f3373fa8e56b6db77141291cd01564d1dfb816181947e4ca
  pageDirectory: concepts
  sources:
    - create-and-manage-labeling-schemas-databricks-on-aws.md
    - label-during-development-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - assessment-types-feedback-vs-expectation
    - ATFVE
  citations:
    - file: label-during-development-databricks-on-aws.md
    - file: create-and-manage-labeling-schemas-databricks-on-aws.md
title: "Assessment types: Feedback vs Expectation"
description: "Two distinct categories of assessments in labeling schemas: subjective feedback (ratings, opinions) and objective ground-truth expectations (correct answers, expected behavior)."
tags:
  - mlflow
  - assessment-types
  - labeling-schemas
timestamp: "2026-06-18T14:50:43.831Z"
---

# Assessment Types: Feedback vs Expectation

**Feedback** and **Expectation** are the two fundamental assessment types in MLflow GenAI for attaching structured evaluations to traces. They capture different kinds of quality information — subjective judgments versus objective ground truth — and serve distinct purposes in model development and evaluation.

## Overview

When labeling traces during development or in structured labeling sessions, each assessment is categorized as either a *Feedback* or an *Expectation*. This classification determines how the data is interpreted, stored, and used in downstream tasks such as building evaluation datasets or fine-tuning judges. Both assessment types are attached to specific spans (or the root span) of a trace. ^[label-during-development-databricks-on-aws.md]

## Feedback

**Feedback** represents a subjective assessment of the model’s output. It captures human opinions, ratings, preferences, or comments about the quality of a response. ^[label-during-development-databricks-on-aws.md] Feedback is inherently evaluator-dependent — different reviewers may assign different ratings to the same trace based on their personal criteria. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Common examples of feedback include:
- A rating scale (e.g., 1–5 stars) for overall response quality.
- A categorical choice on tone (e.g., “Too formal”, “Just right”, “Too casual”).
- A comment box for free-text impressions.
- A numeric confidence score for the reviewer’s own assessment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Feedback is typically used to gauge user satisfaction, identify subjective quality issues, or collect reviewer opinions for later alignment with automated judges. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Expectation

**Expectation** represents an objective ground truth — what the model **should** have produced. It specifies the correct expected output or the desired behavior, independent of any individual opinion. ^[label-during-development-databricks-on-aws.md] Expectations are factual and verifiable; different reviewers should agree on the correct value. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Common examples of expectations include:
- A list of factual claims that a correct response must contain (`EXPECTED_FACTS`).
- Guidelines the output should adhere to (`GUIDELINES`).
- The exact text of a correct response (`EXPECTED_RESPONSE`).
- Steps that should be included in an ideal resolution. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

Expectations are primarily used to define correctness criteria, build evaluation datasets with ground-truth labels, and calibrate automated [judges](/concepts/llm-judges.md) against human-defined standards. Built-in MLflow LLM judges (e.g., for factual consistency) rely on expectation-type schemas. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Key Differences

| Dimension | Feedback | Expectation |
|-----------|----------|-------------|
| Nature | Subjective, opinion-based | Objective, fact-based |
| Consistency across reviewers | May vary | Should be consistent |
| Purpose | Capture quality perception | Define correct output |
| Common data types | Ratings, categories, free-text, boolean | Lists of facts, guidelines, exact text |
| Example use case | "Rate the tone of this response" | "List all facts that must appear" |
| Integration with judges | Used for calibrating custom judges | Used as ground truth for built-in judges |

## When to Use Each

- **Use Feedback** when you want to collect human judgments about aspects that are inherently subjective — helpfulness, tone, preference, or overall satisfaction. This data can later be used to [align judges with human feedback](/concepts/aligning-judges-with-human-experts.md) or to perform [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) based on perceived quality. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- **Use Expectation** when you have a clear, verifiable standard for what a correct response should contain. This is essential for building objective evaluation datasets, defining guidelines for automated judges, and ensuring trace-label data can be used for quantitative assessment. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]
- When [creating custom labeling schemas](/concepts/custom-labeling-schema-creation.md), choose the `type` parameter as `"feedback"` or `"expectation"` accordingly. The type affects how the schema integrates with the Review App and with built-in evaluation workflows. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Integration with Labeling Schemas

In the MLflow UI, when you add an assessment to a trace, you select the **Assessment Type** from a dropdown (Feedback or Expectation). You then provide a name, data type (number, boolean, string), and value. ^[label-during-development-databricks-on-aws.md]

In [Labeling Sessions](/concepts/labeling-sessions.md), each schema is defined with a type. For example, a schema named `"response_quality"` might be of type `"feedback"`, while a schema named `"required_facts"` would be of type `"expectation"`. The same distinction applies to the predefined schemas for built-in LLM judges — they are all of type `expectation`. ^[create-and-manage-labeling-schemas-databricks-on-aws.md]

## Related Concepts

- [Labeling Schemas](/concepts/labeling-schemas.md)
- [Labeling Sessions](/concepts/labeling-sessions.md)
- [Built-in LLM Judges](/concepts/built-in-llm-judges.md)
- [Custom Judges](/concepts/custom-judges.md)
- [Evaluation Datasets](/concepts/evaluation-datasets.md)
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)

## Sources

- create-and-manage-labeling-schemas-databricks-on-aws.md
- label-during-development-databricks-on-aws.md

# Citations

1. [label-during-development-databricks-on-aws.md](/references/label-during-development-databricks-on-aws-8241bcbb.md)
2. [create-and-manage-labeling-schemas-databricks-on-aws.md](/references/create-and-manage-labeling-schemas-databricks-on-aws-c707bbdf.md)
