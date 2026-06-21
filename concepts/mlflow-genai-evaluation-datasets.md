---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 48fcf978b20052dd0199b77bf5d97978c2dca3b18678f8d43e51f1e9de4ab466
  pageDirectory: concepts
  sources:
    - develop-code-based-scorers-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - mlflow-genai-evaluation-datasets
    - MGED
  citations:
    - file: develop-code-based-scorers-databricks-on-aws.md
title: MLflow GenAI Evaluation Datasets
description: Structured evaluation data for LLM applications, typically a list of dictionaries with an 'inputs' key containing message histories for the AI agent.
tags:
  - mlflow
  - evaluation
  - datasets
  - genai
timestamp: "2026-06-19T15:11:33.253Z"
---

---

title: MLflow GenAI Evaluation Datasets
summary: Structures and methods for defining evaluation datasets in MLflow GenAI, including input data and the use of stored traces for iterative scorer development.
sources:
  - develop-code-based-scorers-databricks-on-aws.md
kind: concept
createdAt: 2026-06-18T08:15:15.689Z
updatedAt: 2026-06-18T08:15:15.689Z
tags:
  - mlflow
  - evaluation
  - datasets
  - traces
aliases:
  - mlflow-genai-evaluation-datasets
confidence: 1
provenanceState: extracted
inferredParagraphs: 0

---

# MLflow GenAI Evaluation Datasets

**MLflow GenAI Evaluation Datasets** are structured inputs used with [`mlflow.genai.evaluate()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.genai.html#mlflow.genai.evaluate) to evaluate AI agents or applications. A dataset can be defined as a list of evaluation examples (each containing an `inputs` field) or as a Pandas DataFrame of previously recorded traces. ^[develop-code-based-scorers-databricks-on-aws.md]

## Overview

Evaluation datasets serve as the ground truth or test cases for running [Code-based Scorers](/concepts/code-based-scorers.md) and other metric computations. They allow you to assess the quality of an AI application without re-running the application each time you update a scorer. The dataset is passed via the `data` parameter of `mlflow.genai.evaluate()`. ^[develop-code-based-scorers-databricks-on-aws.md]

## Structure of Evaluation Data

When defining an evaluation dataset from scratch, use a list of dictionaries. Each dictionary must contain an `"inputs"` key whose value is a dictionary representing the input to the app. For a chat application, the inputs typically include a `"messages"` list where each message has `"role"` and `"content"` keys. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"}
            ]
        }
    },
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "Can I return the microwave I bought 2 months ago?"}
            ]
        }
    },
    # Additional examples...
]
```

Each element in the list corresponds to one evaluation row and one [[MLflow Trace]] when the evaluation generates traces. ^[develop-code-based-scorers-databricks-on-aws.md]

## Using Traces as Datasets

An alternative and recommended approach for iterative scorer development is to use **stored traces** as the evaluation dataset. After an initial evaluation run that generates traces (using a placeholder scorer), you can query those traces with [`mlflow.search_traces()`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html?highlight=search_traces#mlflow.search_traces) and obtain a Pandas DataFrame. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)
```

This DataFrame contains the recorded inputs, outputs, and intermediate steps of your application. You can then pass it directly as the `data` parameter in a subsequent call to `mlflow.genai.evaluate()` — without the `predict_fn` parameter. The evaluation will use the stored traces to compute metrics, allowing you to iterate on your scorers without re-running the app. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
# Evaluate a new scorer on precomputed traces
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[response_length],
)
```

## Developer Workflow Integration

The ability to use traces as datasets is a core part of the recommended developer workflow for code-based scorers:

1. **Define evaluation data** – Create a list of input examples.
2. **Generate traces** – Run `mlflow.genai.evaluate()` with a placeholder scorer to produce traces from your app.
3. **Query and store traces** – Retrieve the traces into a DataFrame.
4. **Iterate on scorers** – Call `evaluate()` again using the stored traces, skipping the `predict_fn` argument, to test new or updated scorers quickly. ^[develop-code-based-scorers-databricks-on-aws.md]

This workflow eliminates the overhead of re-generating model responses and speeds up metric development.

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – Overview of the evaluation framework.
- [Code-based Scorers](/concepts/code-based-scorers.md) – Custom metrics defined with the `@scorer` or `Scorer` API.
- [MLflow Tracing](/concepts/mlflow-tracing.md) – Automatic instrumentation that records traces for evaluation.
- [mlflow.genai.evaluate()](/concepts/mlflowgenaievaluate.md) – The function that consumes datasets and runs scorers.
- [MLflow Experiments](/concepts/mlflow-experiment.md) – The organizational unit under which traces and evaluation results are stored.

## Sources

- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
