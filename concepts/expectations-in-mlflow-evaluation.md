---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3f7be6fe3f20cfd8b420d714496348a0b5aeee76e9b0dd8bbf736cd35aa91e82
  pageDirectory: concepts
  sources:
    - code-based-scorer-examples-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expectations-in-mlflow-evaluation
    - EIME
    - Expectations in Evaluation
    - expectations (ground truth)
  citations:
    - file: code-based-scorer-examples-databricks-on-aws.md
title: Expectations in MLflow evaluation
description: Ground-truth values or labels provided in evaluation datasets (via an 'expectations' column) that scorers can use for offline evaluation, with graceful degradation for production monitoring where expectations are absent.
tags:
  - mlflow
  - evaluation
  - datasets
timestamp: "2026-06-19T17:43:56.724Z"
---

# Expectations in MLflow Evaluation

**Expectations** are ground‑truth values or labels that you provide as part of an evaluation dataset. They enable you to compare an AI application's outputs against known correct answers or desired properties during offline evaluation. Expectations are a central mechanism for measuring factual accuracy, keyword coverage, and other quality dimensions in [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) for [GenAI](/concepts/mlflow-genai-evaluate-api.md). ^[code-based-scorer-examples-databricks-on-aws.md]

## Specifying Expectations in Evaluation Data

When calling [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate), you include expectations in the `data` argument in one of two ways: ^[code-based-scorer-examples-databricks-on-aws.md]

- **`expectations` column or field** – If `data` is a list of dictionaries or a Pandas DataFrame, each record can contain an `expectations` key. The value of that key is passed directly to your custom scorer. ^[code-based-scorer-examples-databricks-on-aws.md]
- **`trace` column or field** – If `data` is the DataFrame returned by [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html#mlflow.search_traces), it will include a `trace` field that already contains any `Expectation` data associated with the traces. ^[code-based-scorer-examples-databricks-on-aws.md]

The expectations are then available inside a custom scorer as the `expectations` parameter (see [Custom scorers](/concepts/custom-scorers-mlflow-genai.md)). ^[code-based-scorer-examples-databricks-on-aws.md]

## Design Notes

Production monitoring, which evaluates live traffic, typically does **not** have expectations because ground truth is not available in real time. If you intend to use the same scorer for both offline and online evaluation, design it to handle expectations gracefully — for example, by checking whether an expectations value exists before using it. ^[code-based-scorer-examples-databricks-on-aws.md]

## Example Usage

The following patterns illustrate how expectations are used in practice:

**Exact‑match scorer** – A scorer that checks whether the model's response exactly equals an `expected_response` string provided in the expectations. This is a simple correctness check. ^[code-based-scorer-examples-databricks-on-aws.md]

**Keyword‑presence scorer** – A scorer that verifies that all `expected_keywords` from the expectations appear in the model's output (case‑insensitive). If any keyword is missing, the scorer returns a negative result with a rationale listing the missing terms. ^[code-based-scorer-examples-databricks-on-aws.md]

Both examples receive the `expectations` dictionary as a parameter to the custom scorer function and return either a primitive value (e.g., `bool`) or a `Feedback` object. For the full code, see the [Code-based scorer examples](/concepts/code-based-scorers.md) page.

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The overall evaluation framework for GenAI applications
- [Custom scorers](/concepts/custom-scorers-mlflow-genai.md) – How to define your own scoring functions, including those that use expectations
- [GenAI](/concepts/mlflow-genai-evaluate-api.md) – Overview of MLflow's generative AI capabilities
- [Traces](/concepts/traces.md) – Structured records of AI agent execution that can carry expectation data

## Sources

- code-based-scorer-examples-databricks-on-aws.md

# Citations

1. [code-based-scorer-examples-databricks-on-aws.md](/references/code-based-scorer-examples-databricks-on-aws-de913078.md)
