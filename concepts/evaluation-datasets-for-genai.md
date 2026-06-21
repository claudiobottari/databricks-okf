---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: f71266fc9f9a22f535cedb2040dc4a02d3a1a5cdd88cb784d3074817ca631019
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-datasets-for-genai
    - EDFG
    - Build Evaluation Datasets for GenAI
    - Build evaluation datasets from user feedback
    - Quality Evaluations for GenAI
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
    - file: develop-code-based-scorers-databricks-on-aws.md
title: Evaluation Datasets for GenAI
description: Structured datasets used to evaluate GenAI applications, consisting of input templates or prompts organized as records with consistent schema for batch evaluation.
tags:
  - llm-evaluation
  - datasets
  - testing
timestamp: "2026-06-19T17:23:05.750Z"
---

Here is the updated wiki page for "Evaluation Datasets for GenAI", incorporating the new source material.

---

# Evaluation Datasets for GenAI

**Evaluation datasets** are structured collections of input examples used to systematically assess the quality of a generative AI application within the [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) framework. Each dataset is passed to `mlflow.genai.evaluate()` alongside a prediction function and one or more scorers, enabling reproducible, quantitative evaluation across multiple test cases and iterations. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]

## Structure

An evaluation dataset is defined as a list of dictionaries. Each dictionary represents one evaluation example and must contain an `"inputs"` key whose value is itself a dictionary of arguments. The keys inside this nested dictionary must exactly match the parameter names of the prediction function that will be passed to `evaluate()`. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]

### Example: Template-based app

For an app that fills in sentence templates, each entry provides a `"template"` string: ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
{
    "inputs": {
        "template": "Yesterday, ____ (person) brought a ____ (item) and used it to ____ (verb) a ____ (object)"
    }
}
```

### Example: Conversational app

For a conversational app that accepts a list of messages, each entry provides a `"messages"` list inside `"inputs"`: ^[develop-code-based-scorers-databricks-on-aws.md]

```python
{
    "inputs": {
        "messages": [
            {"role": "user", "content": "How much does a microwave cost?"}
        ]
    }
}
```

The evaluation harness unpacks the `"inputs"` dictionary as keyword arguments to the prediction function for each row.

## Creating an Evaluation Dataset

Datasets can be constructed manually as Python lists. This approach is straightforward for small experiments and rapid prototyping. The list is passed to `mlflow.genai.evaluate()` via the `data` parameter: ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

```python
results = mlflow.genai.evaluate(
    data=eval_data,          # list of dicts
    predict_fn=my_app,       # callable
    scorers=[scorer1, scorer2]
)
```

For larger or version-controlled datasets, consider storing them as JSON or CSV and loading them into a list before evaluation. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Using Stored Traces as Evaluation Datasets

After an initial evaluation run, the traces generated for each row are saved in the experiment. These traces can be retrieved with `mlflow.search_traces()` and reused as an evaluation dataset. This technique enables rapid iteration on scorers without re-running the application — a significant time savings when LLM inference is costly or slow. ^[develop-code-based-scorers-databricks-on-aws.md]

```python
# Retrieve traces from a previous evaluation run
generated_traces = mlflow.search_traces(run_id=eval_results.run_id)

# Pass the traces as data; no predict_fn needed
mlflow.genai.evaluate(
    data=generated_traces,
    scorers=[my_new_scorer]
)
```

When a Pandas DataFrame of traces is used as the `data` parameter, the evaluation harness reads the recorded inputs and outputs directly from the traces. Consequently, no `predict_fn` is required. This is the recommended approach for iterative scorer development. ^[develop-code-based-scorers-databricks-on-aws.md]

## Best Practices

- **Match `inputs` keys to function parameters.** Ensure the dictionary inside `"inputs"` has keys that correspond exactly to the argument names of the prediction function. Mismatches will cause runtime errors. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md, develop-code-based-scorers-databricks-on-aws.md]
- **Version datasets for reproducibility.** Store evaluation datasets as files (e.g., JSON) and track them under version control to enable consistent comparisons across runs. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Leverage stored traces for scoring development.** When prototyping new scorers, reuse existing traces as the evaluation dataset to avoid waiting for LLM inference on every iteration. ^[develop-code-based-scorers-databricks-on-aws.md]

## Relationship to MLflow Evaluation

Evaluation datasets are a core input to the [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) workflow. They work together with:

- **Scorers** (e.g., built-in Guidelines, Safety, or custom [Code-based Scorers](/concepts/code-based-scorers.md)) that assess each row. ^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]
- **Traces** — recorded execution data that can itself become an evaluation dataset. ^[develop-code-based-scorers-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- [MLflow Tracing](/concepts/mlflow-tracing.md)
- [Code-based Scorers](/concepts/code-based-scorers.md)
- [LLM-as-Judge Scorers](/concepts/llm-judges-and-scorers.md)
- Evaluation Dataset Versioning

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
- develop-code-based-scorers-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
2. [develop-code-based-scorers-databricks-on-aws.md](/references/develop-code-based-scorers-databricks-on-aws-4fba7668.md)
