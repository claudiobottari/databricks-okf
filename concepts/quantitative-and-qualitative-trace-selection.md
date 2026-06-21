---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78166752abc746518524ddf12e105bdaba1bd09826973509b7225a1f133cb93e
  pageDirectory: concepts
  sources:
    - building-mlflow-evaluation-datasets-databricks-on-aws.md
  confidence: 0.95
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - quantitative-and-qualitative-trace-selection
    - Qualitative Trace Selection and Quantitative
    - QAQTS
  citations:
    - file: building-mlflow-evaluation-datasets-databricks-on-aws.md
title: Quantitative and Qualitative Trace Selection
description: Methodologies for selecting representative traces for evaluation datasets using measurable filters (tags, latency, token usage) and human judgment (reviewing edge cases, low-quality outputs, patterns).
tags:
  - evaluation
  - tracing
  - quality-analysis
timestamp: "2026-06-19T14:10:34.670Z"
---

---

title: Quantitative and Qualitative Trace Selection
summary: Methodology for selecting representative traces for evaluation datasets using both quantitative filters (tags, latency, token usage, success/failure) and qualitative human review (edge cases, faulty reasoning, identifying patterns).
sources:
  - building-mlflow-evaluation-datasets-databricks-on-aws.md
kind: concept
createdAt: "2026-06-18T10:54:31.085Z"
updatedAt: "2026-06-19T09:10:59.917Z"
tags:
  - evaluation
  - tracing
  - methodology
aliases:
  - quantitative-and-qualitative-trace-selection
  - Qualitative Trace Selection and Quantitative
  - QAQTS
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Quantitative and Qualitative Trace Selection

**Quantitative and Qualitative Trace Selection** refers to the process of identifying and curating representative traces from [MLflow Tracing](/concepts/mlflow-tracing.md) to build evaluation datasets for GenAI applications. Before adding traces to an evaluation dataset, you should identify which traces represent important test cases for your evaluation needs using both quantitative analysis and qualitative review.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Quantitative Trace Selection

Quantitative trace selection uses the MLflow UI or SDK to filter and analyze traces based on measurable characteristics.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Using the MLflow UI

In the MLflow UI, you can filter by tags (e.g., `tag.quality_score < 0.7`), search for specific inputs or outputs, and sort by latency or token usage to identify traces of interest.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Programmatic Analysis

You can query traces programmatically to perform advanced analysis. For example, you might search for traces with potential quality issues and analyze whether those issues correlate with other metrics like token usage:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

```python
import mlflow
import pandas as pd

# Search for traces with potential quality issues
traces_df = mlflow.search_traces(
    filter_string="tag.quality_score < 0.7",
    max_results=100
)

# Analyze patterns
# For example, check if quality issues correlate with token usage
correlation = traces_df["span.attributes.usage.total_tokens"].corr(traces_df["tag.quality_score"])
print(f"Correlation between token usage and quality: {correlation}")
```

For complete trace query syntax and examples, see mlflow.search_traces() API|Search traces programmatically.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Qualitative Trace Selection

Qualitative trace selection involves reviewing individual traces to identify patterns that require human judgment. This approach helps surface issues that quantitative metrics alone might miss.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

Key activities in qualitative trace selection include:^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

- Examining inputs that led to low-quality outputs
- Looking for patterns in how your application handled edge cases
- Identifying missing context or faulty reasoning in responses
- Comparing high-quality vs. low-quality traces to understand differentiating factors

## Combining Both Approaches

Once you have identified representative traces through quantitative and qualitative analysis, you can add them to your evaluation dataset using the search and merge methods provided by the MLflow SDK.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

### Enriching Traces

You can enrich your traces with expected outputs or quality indicators to enable ground truth comparison. See [Collect domain expert feedback](/concepts/mlflow-review-app-for-domain-expert-feedback.md) to add human labels to existing traces.^[building-mlflow-evaluation-datasets-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md) — The datasets that traces are selected for
- [MLflow Tracing](/concepts/mlflow-tracing.md) — The tracing system that captures application interactions
- mlflow.search_traces() API|Search Traces Programmatically — SDK methods for querying traces
- [GenAI Application Evaluation](/concepts/genai-application-evaluation-lifecycle.md) — The broader evaluation workflow
- Collect Domain Expert Feedback — Adding human labels to traces

## Sources

- building-mlflow-evaluation-datasets-databricks-on-aws.md

# Citations

1. [building-mlflow-evaluation-datasets-databricks-on-aws.md](/references/building-mlflow-evaluation-datasets-databricks-on-aws-a5b14a92.md)
