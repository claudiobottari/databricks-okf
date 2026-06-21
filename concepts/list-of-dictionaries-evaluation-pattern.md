---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: a88f4f5199d654345ce24118fd1c33447ab207cd375a862c0a7fe4cd3a9c992a
  pageDirectory: concepts
  sources:
    - mlflow-evaluation-examples-for-genai-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - list-of-dictionaries-evaluation-pattern
    - LODEP
    - List of Dictionaries Pattern
  citations:
    - file: mlflow-evaluation-examples-for-genai-databricks-on-aws.md
title: List of Dictionaries Evaluation Pattern
description: Using a simple list of Python dictionaries for quick prototyping and small-scale GenAI evaluation without formal dataset creation.
tags:
  - mlflow
  - evaluation
  - prototyping
timestamp: "2026-06-19T19:38:50.141Z"
---

# List of Dictionaries Evaluation Pattern

The **List of Dictionaries Evaluation Pattern** is a data input pattern for MLflow GenAI evaluation where test data is provided as a Python list of dictionary objects. Each dictionary in the list represents a single evaluation example with `"inputs"` and `"expectations"` keys.

This pattern is recommended for **quick prototyping**, **small datasets (fewer than 100 examples)**, and **informal development testing**. It does not require creating a formal evaluation dataset in Unity Catalog. ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Basic Structure

Each entry in the list contains:
- **`inputs`**: A dictionary with keys representing the input parameters for the `predict_fn` (e.g., `"question"`, `"user_message"`).
- **`expectations`** (optional): A dictionary defining expected outputs or ground truth facts against which scorers can measure correctness or relevance.

```python
# Example structure
eval_data = [
    {
        "inputs": {"question": "What is MLflow?"},
        "expectations": {"expected_facts": ["open source AI engineering platform", "agents, LLMs, and ML models"]}
    },
    {
        "inputs": {"question": "How do I track experiments?"},
        "expectations": {"expected_facts": ["mlflow.start_run()", "log metrics", "log parameters"]}
    }
]
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Usage in Evaluation

Pass the list directly to `mlflow.genai.evaluate()` as the `data` argument, alongside a `predict_fn` and one or more scorers:

```python
import mlflow
from mlflow.genai.scorers import Correctness, RelevanceToQuery

eval_data = [
    {"inputs": {"question": "What is MLflow?"}},
    {"inputs": {"question": "How do I track experiments?"}}
]

results = mlflow.genai.evaluate(
    data=eval_data,
    predict_fn=my_chatbot_app,
    scorers=[Correctness(), RelevanceToQuery()]
)
```

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Comparison with Other Data Patterns

| Data Pattern | When to Use |
|--------------|-------------|
| **List of Dictionaries** | Quick prototyping, small datasets (<100 examples), informal development testing |
| **[MLflow Evaluation Dataset](https://docs.databricks.com/aws/en/mlflow3/genai/eval-monitor/build-eval-dataset)** | Production use with versioning, lineage tracking, and Unity Catalog integration |
| **Pandas DataFrame** | When data is already in CSV or existing data science workflows |
| **Spark DataFrame** | Large-scale evaluations or when data is already in Delta Lake |

^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Limitations

While this pattern is convenient for prototyping, it lacks **versioning**, **lineage tracking**, and **Unity Catalog integration**. For production evaluation, the documentation recommends converting to an [MLflow Evaluation Dataset](/concepts/mlflow-evaluation-dataset.md). ^[mlflow-evaluation-examples-for-genai-databricks-on-aws.md]

## Related Concepts

- [MLflow Evaluation Datasets](/concepts/mlflow-evaluation-datasets.md)
- [GenAI Evaluation](/concepts/mlflow-genai-evaluation.md)
- predict_fn
- [Correctness Scorer](/concepts/correctness-scorer.md)
- [RelevanceToQuery Scorer](/concepts/relevancetoquery.md)

## Sources

- mlflow-evaluation-examples-for-genai-databricks-on-aws.md

# Citations

1. [mlflow-evaluation-examples-for-genai-databricks-on-aws.md](/references/mlflow-evaluation-examples-for-genai-databricks-on-aws-2da85b83.md)
