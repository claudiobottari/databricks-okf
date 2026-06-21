---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 78859501e4b88256fd511d3b37cbcffa5ea7cb903674441c0c1997dbc16fbd9f
  pageDirectory: concepts
  sources:
    - align-judges-with-humans-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - judge-registration-and-deployment
    - Deployment and Judge Registration
    - JRAD
  citations:
    - file: align-judges-with-humans-databricks-on-aws.md
title: Judge Registration and Deployment
description: The process of registering an aligned judge for production use with distinguishing metadata such as name, alignment date, and number of traces used.
tags:
  - deployment
  - mlflow
  - mlops
timestamp: "2026-06-19T17:32:28.554Z"
---

---

title: Judge Registration and Deployment
summary: The process of registering an aligned judge for production use via the register() method, including specifying experiment ID, name, and metadata tags.
sources:
  - align-judges-with-humans-databricks-on-aws.md
kind: concept
createdAt: "2026-06-19T08:58:28.121Z"
updatedAt: "2026-06-19T08:58:28.121Z"
tags:
  - deployment
  - llm-evaluation
  - mlflow
aliases:
  - judge-registration-and-deployment
  - Deployment and Judge Registration
  - JRAD
confidence: 0.9
provenanceState: extracted
inferredParagraphs: 0
---

# Judge Registration and Deployment

**Judge Registration and Deployment** refers to the process of making an LLM-based judge available for production use within the MLflow ecosystem. After developing or Align judges with humans|aligning a judge, it must be registered to a specific MLflow experiment and then deployed as part of a [Production Monitoring for GenAI|production monitoring](/concepts/production-monitoring-for-genai-applications.md) workflow to continuously evaluate agent outputs.

## Registration

A judge is registered using its `register()` method. Registration stores the judge’s configuration (instructions, model, name) within an MLflow experiment, making it retrievable and reusable for evaluation and monitoring tasks. ^[align-judges-with-humans-databricks-on-aws.md]

The `register()` method accepts the following parameters:

- **`experiment_id`** – The ID of the MLflow experiment where the judge will be stored.
- **`name`** – A unique name for the registered judge (e.g., `relevance_to_query_aligned`). This distinguishes it from the original judge or other variants.
- **`tags`** – Optional metadata such as alignment date or number of training traces.

Example from the source (after alignment): ^[align-judges-with-humans-databricks-on-aws.md]

```python
aligned_judge.register(
    experiment_id=experiment_id,
    name=f"{initial_judge.name}_aligned",
    tags={"alignment_date": "2025-10-23", "num_traces": str(len(traces_for_alignment))}
)
```

### When to Register

- **After alignment**: A newly aligned judge should be registered with a distinct name to differentiate it from the unaligned baseline. ^[align-judges-with-humans-databricks-on-aws.md]
- **For production use**: Even without alignment, a judge must be registered before it can be referenced in production monitoring pipelines.

### Prerequisites

- MLflow 3.4.0 or above. ^[align-judges-with-humans-databricks-on-aws.md]
- An existing judge — either a [built-in judge](/concepts/built-in-judges.md) (e.g., `RelevanceToQuery`, `Correctness`) or a [custom judge](/concepts/custom-judges.md) created with [`make_judge()`](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/custom-judge/). ^[align-judges-with-humans-databricks-on-aws.md]
- The judge must be instantiated and, if desired, aligned with human feedback before registration.

## Deployment

Deployment of a judge refers to its use in production monitoring to evaluate agent outputs continuously. The source documentation directs users to learn about [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) to "deploy aligned judges at scale". ^[align-judges-with-humans-databricks-on-aws.md]

After registration, a judge can be referenced by name in monitoring configurations, allowing teams to automate quality checks on live traffic without requiring ad-hoc evaluations.

### Deployment Workflow

1. **Register** the judge (as described above).
2. **Configure** production monitoring to use the registered judge.
3. **Monitor** judge scores over time and iterate by re-aligning and re-registering improved versions.

## Related Concepts

- [Align judges with humans](/concepts/aligning-judges-with-human-experts.md) – The workflow that produces a judge ready for registration and deployment.
- [Built-in Judges](/concepts/built-in-judges.md) – Pre-built judges that can be registered and deployed.
- [Custom Judges](/concepts/custom-judges.md) – Domain-specific judges created with `make_judge()`.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Continuous evaluation using registered judges.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – Offline evaluation where judges are also used.
- make_judge()|Make Judge API – The `make_judge()` function for constructing custom judges.

## Sources

- align-judges-with-humans-databricks-on-aws.md

# Citations

1. [align-judges-with-humans-databricks-on-aws.md](/references/align-judges-with-humans-databricks-on-aws-03f1583e.md)
