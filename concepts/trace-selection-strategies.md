---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0532cb8dc790fd4d81350c2d5ce23e60210136a3ec8b5ede65346e4627697d55
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - trace-selection-strategies
    - TSS
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Trace Selection Strategies
description: Quantitative and qualitative methods for identifying representative traces from production logs to curate evaluation datasets, including filtering by quality scores, token usage, latency, and manual review of patterns.
tags:
  - traces
  - evaluation
  - workflow
timestamp: "2026-06-18T14:34:21.632Z"
---

## Trace Selection Strategies

**Trace Selection Strategies** refers to the systematic methods used to choose representative [[MLflow Trace|MLflow Traces]] from a GenAI application’s historical interactions when building an [evaluation dataset](/concepts/mlflow-evaluation-dataset.md). Selecting the right traces ensures that the dataset covers real‑world scenarios, edge cases, and quality issues, enabling effective evaluation and iterative improvement of the application. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Overview

An evaluation dataset should reflect the range of inputs the application will encounter in production. Curating traces directly from the application’s logged interactions is one of the most effective ways to build a relevant dataset. Two complementary approaches are commonly used: **quantitative** filtering based on measurable characteristics and **qualitative** inspection of individual traces. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Quantitative Trace Selection

Quantitative selection uses filters, tags, and metrics to identify traces that match specific criteria. You can perform this analysis both in the MLflow UI and programmatically via the SDK. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- **In the MLflow UI**: Filter traces by tags (e.g., `tag.quality_score < 0.7`), search for specific input/output patterns, or sort traces by latency or token usage.
- **Programmatically**: Use `mlflow.search_traces()` with `filter_string` to query traces based on attributes (e.g., status, timestamp) and tags. For example, to find all successful traces from production with low quality scores:

```python
traces_df = mlflow.search_traces(
    filter_string="tag.quality_score < 0.7",
    tags.environment = 'production',
    max_results=100
)
```

This approach allows you to quickly isolate traces that may require attention, such as those with high latency, low quality scores, or errors. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Qualitative Trace Selection

Qualitative selection involves manually reviewing individual traces to identify patterns that require human judgment. This step is essential for understanding the underlying causes of poor outputs and for capturing edge cases that automated filters might miss. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

Common qualitative criteria include:

- Inputs that led to low‑quality outputs.
- Patterns in how the application handled edge cases (e.g., missing context, faulty reasoning).
- Comparing high‑quality and low‑quality traces to understand differentiating factors.

Once identified, these traces can be added to the evaluation dataset using the UI or SDK. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Combining Strategies

For a robust evaluation dataset, combine quantitative and qualitative approaches. Start with quantitative filters to narrow down a large trace set, then qualitatively review the results to ensure coverage of important scenarios. You can also enrich selected traces with human‑labeled expected outputs or quality indicators to enable ground‑truth comparison (see Human Feedback Alignment). ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Adding Selected Traces to a Dataset

After selecting traces, add them to the evaluation dataset:

- **UI**: In the experiment’s **Traces** page, select traces using checkboxes, click **Actions** > **Add to evaluation dataset**, and choose a destination dataset.
- **SDK**: Merge selected traces into the dataset using `eval_dataset.merge_records(traces)`. ^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Related Concepts

- [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md) – The storage and versioning of test examples for GenAI evaluation.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – The system that captures application execution traces.
- [Custom Judges](/concepts/custom-judges.md) – LLM‑based scorers used to evaluate outputs from traces.
- Evaluation Metrics for GenAI – Quantitative measures derived from traces.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Ongoing monitoring that can surface traces for dataset curation.

### Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
