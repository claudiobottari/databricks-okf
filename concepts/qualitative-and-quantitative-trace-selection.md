---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 37064647ee302dbb19cb5850e1541fdf32823396528d4e1351f13acb7c1e80fd
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.85
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - qualitative-and-quantitative-trace-selection
    - Quantitative Trace Selection and Qualitative
    - QAQTS
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Qualitative and Quantitative Trace Selection
description: Methods for selecting representative traces for evaluation datasets, combining quantitative analysis (filtering by tags, latency, token usage) with qualitative review (examining inputs, outputs, and edge cases).
tags:
  - mlflow
  - tracing
  - evaluation
  - trace-analysis
timestamp: "2026-06-19T17:41:55.021Z"
---

# Qualitative and Quantitative Trace Selection

**Qualitative and Quantitative Trace Selection** refers to two complementary approaches for choosing representative [traces](/concepts/mlflow-tracing.md) to include in an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md). These methods help practitioners curate a focused set of test cases that reflect real-world usage, quality issues, and edge cases, enabling systematic evaluation and regression testing of GenAI applications. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Quantitative Trace Selection

Quantitative trace selection uses measurable characteristics stored in trace metadata to filter and rank traces. Practitioners can apply filters and sort traces by numeric or categorical attributes such as latency, token usage, quality scores, or response status. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

Two common avenues for applying quantitative selection are:

- **In the MLflow UI**: Filter by tags (e.g., `tag.quality_score < 0.7`), search for specific input/output patterns, or sort by latency or token usage. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]
- **Programmatically with the SDK**: Use `mlflow.search_traces()` with filter strings and `order_by` clauses to retrieve traces meeting specific criteria. For example, to find traces with low quality scores, one can call `mlflow.search_traces(filter_string="tag.quality_score < 0.7", max_results=100)` and then perform further analysis such as checking correlations between token usage and quality. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

This approach is valuable for identifying broad patterns and systematically selecting a statistically representative subset of traces. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Qualitative Trace Selection

Qualitative trace selection relies on human judgment to inspect individual traces and identify patterns that automated metrics might miss. Practitioners are advised to: ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- Examine inputs that led to low-quality outputs.
- Look for patterns in how the application handled edge cases.
- Identify missing context or faulty reasoning in the model’s responses.
- Compare high-quality versus low-quality traces to understand differentiating factors.

This method is especially useful for capturing nuanced failure modes that require deep domain knowledge or subjective assessment. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Combining Both Approaches

For a robust evaluation dataset, it is recommended to use both quantitative and qualitative selection together. Quantitative methods provide scale and objectivity; qualitative methods add depth and contextual understanding. Once representative traces are identified, they can be added to a dataset using the `merge_records()` method in the MLflow SDK. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) – The table or structure where selected traces are stored.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The mechanism that captures application traces for observability.
- mlflow.search_traces() API|Search traces programmatically – The SDK-based method for querying and filtering traces.
- [Evaluate your app](/concepts/evaluation-run.md) – Using evaluation datasets for systematic testing.
- [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) – Adding human labels to traces for ground truth comparison.

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
