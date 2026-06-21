---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 153cfdeee34ddcf1a31cce3a18cef504bb275ded30570a64d84441da4606f615
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-for-prompts
    - EDFP
    - Evaluation dataset formats
    - Evaluation dataset from traces
    - Evaluate Prompts
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
    - file: evaluate-and-compar-prompt-versions-databricks-on-aws.md
title: Evaluation Dataset for Prompts
description: Structured dataset containing input examples and expected facts used to objectively measure prompt quality and fact coverage across different versions.
tags:
  - evaluation
  - datasets
  - testing
timestamp: "2026-06-18T12:11:18.682Z"
---

# Evaluation Dataset for Prompts

An **evaluation dataset for prompts** is a structured collection of input examples and expected outcomes used to systematically assess and compare the performance of different prompt versions in GenAI applications. It ensures that every prompt version is tested against the same criteria, enabling fair, reproducible evaluation. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Creating an Evaluation Dataset

Evaluation datasets for prompts are created using the `mlflow.genai.datasets.create_dataset()` API, which registers a table in [Unity Catalog](/concepts/unity-catalog.md). The dataset is then populated with records that contain at minimum an `inputs` dictionary and an optional `expectations` dictionary. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
eval_dataset = mlflow.genai.datasets.create_dataset(
    uc_table_name="<catalog>.<schema>.<dataset_name>"
)
```

After creating the dataset, examples are added by calling `merge_records()`. Each example is itself a dictionary with the required keys `inputs` and optional `expectations`. ^[evaluate-and-compar-prompt-versions-databricks-on-aws.md]

## Dataset Structure

Each record in an evaluation dataset must contain an `inputs` field. For summarization tasks, a typical input is a text string under the key `content`. The dataset may also include an `expectations` field that holds structured expected outcomes—such as a list of `expected_facts`—which can be used by scorers like the built-in `Correctness` scorer. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Example record:

```python
{
    "inputs": {
        "content": "Remote work has fundamentally changed..."
    },
    "expectations": {
        "expected_facts": [
            "remote work changed collaboration",
            "digital tools adoption",
            "productivity remained stable"
        ]
    }
}
```

## Using the Dataset in Evaluation

The evaluation dataset is passed to the `data` parameter of `mlflow.genai.evaluate()`. The function also accepts a prediction function (the prompt version being tested) and a list of scorers. The built-in `Correctness` scorer checks how well the generated output covers the `expected_facts` from the dataset. Custom scorers, such as those created with `make_judge`, can also reference fields in the dataset. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from mlflow.genai.scorers import Correctness
scorers = [Correctness()]
with mlflow.start_run():
    eval_results = mlflow.genai.evaluate(
        predict_fn=my_summary_function,
        data=eval_dataset,
        scorers=scorers,
    )
```

## Best Practices

- **Use consistent datasets across all prompt versions** to ensure valid comparisons. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Include edge cases and challenging examples** in the dataset to stress-test prompt behavior. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Track evaluation datasets alongside prompts** by logging dataset names and versions in MLflow runs. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Start with simple prompts and iterate**; the dataset helps measure improvement over successive versions. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Prompt Versioning](/concepts/prompt-versioning.md) – Managing iterative changes to prompts.
- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The framework that provides evaluation APIs.
- [Scorers and judges](/concepts/scorers-and-llm-judges.md) – Metrics and LLM-based evaluators that use the dataset.
- [Unity Catalog](/concepts/unity-catalog.md) – The governance layer that stores evaluation dataset tables.

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
2. evaluate-and-compar-prompt-versions-databricks-on-aws.md
