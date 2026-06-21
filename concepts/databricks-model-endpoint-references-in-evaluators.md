---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3173a5a70981467cf0bd847074d02eed865495b291994447fe93e3fa58aa3f0f
  pageDirectory: concepts
  sources:
    - arize-phoenix-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - databricks-model-endpoint-references-in-evaluators
    - DMERIE
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
    - file: arize-phoenix-scorers-databricks-on-aws.md
title: Databricks model endpoint references in evaluators
description: The pattern of referencing Databricks-hosted foundation models (e.g., databricks-gpt-5-mini) via the 'databricks:/' prefix as the evaluation model for Phoenix scorers in the MLflow GenAI evaluation framework.
tags:
  - databricks
  - model-serving
  - mlflow
timestamp: "2026-06-19T09:03:23.465Z"
---

# Databricks Model Endpoint References in Evaluators

**Databricks model endpoint references in evaluators** refers to the use of the `databricks:/` URI scheme to specify a Databricks Model Serving endpoint as the LLM judge or scorer within MLflow evaluation APIs. This mechanism allows evaluators and custom judges to invoke a deployed model endpoint for scoring outputs during offline evaluation or production monitoring.

## Overview

When using [MLflow GenAI](/concepts/mlflow-3-for-genai.md) evaluators such as `mlflow.genai.evaluate()` or the `make_judge()` API, you must provide a model that acts as the judge to score agent outputs. Databricks supports referencing a Model Serving endpoint by prefixing the endpoint name with `databricks:/`. This directs the evaluator to call the specified endpoint for inference instead of using an external model provider.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, arize-phoenix-scorers-databricks-on-aws.md]

## Usage Patterns

### Custom Judges Created with `make_judge()`

When creating a custom judge via `make_judge()`, the `model` parameter accepts a Databricks endpoint reference. For example:

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions="Analyze the execution {{ trace }} to determine if the agent called appropriate tools.",
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

The referenced endpoint is used for all inference calls made by the judge during evaluation.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Third-Party Scorers (e.g., Arize Phoenix)

Third-party scorers such as Arize Phoenix `Hallucination` and `Relevance` also accept a `model` parameter with a Databricks endpoint reference:

```python
results = mlflow.genai.evaluate(
    data=eval_dataset,
    scorers=[
        Hallucination(model="databricks:/databricks-gpt-5-mini"),
        Relevance(model="databricks:/databricks-gpt-5-mini"),
    ],
)
```

The scorer uses the specified endpoint to compute its quality metric.^[arize-phoenix-scorers-databricks-on-aws.md]

## Model Specification Format

The format for referencing a Databricks model endpoint is:

```
databricks:/<endpoint-name>
```

- `<endpoint-name>` is the name of the Model Serving endpoint as defined in the Databricks workspace.
- The endpoint must be serving a model (e.g., a foundational model like `databricks-gpt-5-mini` or a custom deployed model).
- The endpoint must be accessible by the caller; proper permissions and budget policies must be in place.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Considerations

- **Permissions**: The user or service principal running the evaluation must have permission to query the referenced model endpoint.
- **Budget Policy**: If the endpoint is serverless, the workspace must have an appropriate serverless budget policy configured. Otherwise, a `403 PERMISSION_DENIED` error may occur. See 403 PERMISSION_DENIED Serverless Budget Policy Error.
- **Model Availability**: Ensure the endpoint is deployed and has sufficient capacity to handle evaluation requests, especially for large evaluation datasets.
- **Cost**: Each evaluation call to the endpoint incurs cost according to the endpoint’s pricing model.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The `mlflow.genai.evaluate()` API for offline and online evaluation.
- [Custom Judges](/concepts/custom-judges.md) – Creating LLM-based evaluators with `make_judge()`.
- [Arize Phoenix Scorers](/concepts/arize-phoenix-scorers.md) – Third-party evaluation scorers that support Databricks endpoint references.
- [Model Serving on Databricks](/concepts/model-serving-on-databricks.md) – Deploying and managing model endpoints.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces in judges.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- arize-phoenix-scorers-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
2. [arize-phoenix-scorers-databricks-on-aws.md](/references/arize-phoenix-scorers-databricks-on-aws-53f4b817.md)
