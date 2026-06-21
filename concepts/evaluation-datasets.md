---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d2a08699aaf79e8bcdd2b673d7637143432d996b3c2927ac5b407b4851206268
  pageDirectory: concepts
  sources:
    - evaluate-genai-apps-during-development-databricks-on-aws.md
    - tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
  confidence: 0.92
  provenanceState: merged
  freshnessStatus: unverified
  aliases:
    - evaluation-datasets
    - Build Evaluation Datasets
    - Build evaluation datasets
    - Sync to Evaluation Datasets
    - build evaluation datasets
    - Build Evaluation Datasets from Traces
    - Build evaluation datasets from traces
  citations:
    - file: evaluate-genai-apps-during-development-databricks-on-aws.md
    - file: tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md
title: Evaluation Datasets
description: Structured test data used as input to `mlflow.genai.evaluate()`, supporting EvaluationDataset objects, lists of dicts, Pandas DataFrames, and Spark DataFrames.
tags:
  - mlflow
  - data
  - testing
timestamp: "2026-06-19T18:42:38.426Z"
---

# Evaluation Datasets

**Evaluation datasets** are structured collections of test inputs (and optionally expected outputs) used with [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) to systematically assess the quality of a generative AI application. They serve as the foundation for offline evaluation, enabling consistent, repeatable testing across app versions and connecting development workflows to production monitoring. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Purpose and role in evaluation

The `mlflow.genai.evaluate()` function feeds an evaluation dataset into a GenAI app, runs the app (or uses pre‑computed outputs), and automatically scores the results using [[scorers]] or [LLM Judges](/concepts/llm-judges.md). This replaces manual, one‑by‑one checking with a structured, automated process. The same evaluation logic used in development can be reused in production monitoring, giving a consistent view of quality across the AI lifecycle. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

Evaluation datasets are central to both evaluation modes:

- **Direct evaluation**: the dataset supplies inputs; the app is called via `predict_fn` for each row, generating traces that are then scored.
- **Answer sheet evaluation**: the dataset supplies both inputs and pre‑computed outputs (or existing traces); scoring is applied directly to those outputs. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Supported formats and schema

The `data` parameter of `mlflow.genai.evaluate()` accepts the following formats:

- `EvaluationDataset` (recommended) – a versioned object that enforces schema validation and tracks lineage of each record.
- List of dictionaries.
- Pandas DataFrame.
- Spark DataFrame.

When using a DataFrame or list of dictionaries, the data must follow the same schema used by `EvaluationDataset`. Databricks recommends using `EvaluationDataset` because it provides built‑in validation and lineage tracking. ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

For **direct evaluation**, each record must contain an `"inputs"` dictionary whose keys match the keyword arguments expected by `predict_fn`. The app returns a dictionary (e.g., `{"response": ...}`).  
For **answer sheet evaluation**, each record must include an `"inputs"` dictionary and either an `"outputs"` dictionary (pre‑computed results) or a `"trace"` object (existing MLflow trace). ^[evaluate-genai-apps-during-development-databricks-on-aws.md]

## Creating evaluation datasets

Evaluation datasets can be created in two primary ways:

### From production traces

In the Databricks UI, you select traces from an experiment’s **Traces** tab and export them to an evaluation dataset. This captures real usage patterns and allows you to later re‑evaluate the same test cases after app changes. The dataset is stored in [Unity Catalog](/concepts/unity-catalog.md) and requires `CREATE TABLE` permission on the target schema. ^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

The process is:
1. Open the experiment and navigate to the **Traces** tab.
2. Select the traces to include (checkboxes).
3. Click **Actions** → **Add to evaluation dataset**.
4. Either create a new dataset (specifying a Unity Catalog schema and name) or export to an existing dataset.
5. Click **Export** and then **Done**.

^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

### Programmatically from scratch

You can build an `EvaluationDataset` directly from code, for example by constructing a list of dictionaries following the required schema. This is useful for synthetic test data or curated edge cases. The dataset can then be passed to `mlflow.genai.evaluate()`. ^[evaluate-genai-apps-during-development-databricks-on-aws.md, tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Versioning and reuse

Because evaluation datasets are versioned (when stored in Unity Catalog), you can link multiple evaluation runs to the same dataset. This enables direct comparison of different app versions against identical test cases, helping to verify that improvements do not cause regressions. The dataset acts as a stable benchmark across the iteration cycle. ^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Practical example

The following snippet, adapted from the [tutorial], shows how a dataset is built from simulated traffic traces and used in an evaluation:

```python
# Simulated test requests
test_requests = [
    {"customer_name": "Acme Corp", "user_instructions": "Follow up after product demo"},
    {"customer_name": "TechStart", "user_instructions": "Check on support ticket status"},
    # ... more requests
]

# Run requests to generate traces
for req in test_requests:
    generate_sales_email(**req)

# Traces are then exported to an evaluation dataset via the UI
# (see Step 3 in the tutorial)

# Later, the dataset is passed to mlflow.genai.evaluate()
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=generate_sales_email,
    scorers=email_judges,  # list of LLM judges
)
```

^[tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md]

## Related concepts

- [Evaluation Harness](/concepts/evaluation-harness.md) – the `mlflow.genai.evaluate()` function that consumes evaluation datasets.
- [[Scorers]] and [LLM Judges](/concepts/llm-judges.md) – the quality metrics applied to each record in the dataset.
- [Evaluation Runs](/concepts/evaluation-runs.md) – test reports that capture scores and traces for each dataset record.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – mechanism that captures app traces, which can be exported to evaluation datasets.
- [Unity Catalog](/concepts/unity-catalog.md) – storage location for versioned evaluation datasets.
- [Production quality monitoring](/concepts/production-monitoring.md) – reuse of evaluation datasets and scorers for continuous monitoring.

## Sources

- evaluate-genai-apps-during-development-databricks-on-aws.md
- tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md

# Citations

1. [evaluate-genai-apps-during-development-databricks-on-aws.md](/references/evaluate-genai-apps-during-development-databricks-on-aws-373c1693.md)
2. [tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws.md](/references/tutorial-evaluate-and-improve-a-genai-application-databricks-on-aws-554c7fbb.md)
