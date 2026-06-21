---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: dc3b38da746e2ab462cd10683675ef4b3be29ad2a9038f5a25d774b96dc4db59
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - evaluation-dataset-with-expected-facts
    - EDWEF
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Evaluation Dataset with Expected Facts
description: A structured dataset containing input-output pairs with expected facts that allow measuring correctness of LLM responses by checking fact coverage.
tags:
  - evaluation
  - datasets
  - genai
timestamp: "2026-06-19T18:40:43.867Z"
---

# Evaluation Dataset with Expected Facts

An **Evaluation Dataset with Expected Facts** is a structured collection of test examples used in GenAI evaluation that includes both the input to the model and a set of expected facts that a high-quality response should contain. This dataset format enables automated assessment of how well a generated output covers the key information present in the source content. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

Expected facts serve as ground-truth reference points against which model outputs can be automatically scored. By defining what facts a response should ideally include, developers can objectively measure the completeness and accuracy of generated text without requiring manual human review for every evaluation run. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

Evaluation datasets with expected facts are particularly useful when comparing different [prompt versions](/concepts/prompt-versioning.md) or agent configurations. They enable consistent, reproducible evaluation across variants, ensuring that differences in scores reflect genuine changes in model behavior rather than inconsistencies in the evaluation criteria. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Structure

An evaluation dataset entry with expected facts follows a standard format with two key components:

```python
{
    "inputs": {
        "content": "Text to be processed by the model..."
    },
    "expectations": {
        "expected_facts": [
            "specific fact that should appear",
            "another required fact"
        ]
    }
}
```

The `inputs` field contains the data passed to the model (such as source text for summarization), while the `expectations` field contains the `expected_facts` list that defines what information the model output should cover. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Creating an Evaluation Dataset

In MLflow, evaluation datasets can be created using the `mlflow.genai.datasets.create_dataset()` API, which registers the dataset in [Unity Catalog](/concepts/unity-catalog.md). Examples with expected facts are added by merging records into the dataset:

```python
eval_dataset = mlflow.genai.datasets.create_dataset(
    uc_table_name="catalog.schema.dataset_name"
)

evaluation_examples = [
    {
        "inputs": {"content": "Source text..."},
        "expectations": {
            "expected_facts": [
                "fact one",
                "fact two"
            ]
        }
    }
]

eval_dataset = eval_dataset.merge_records(evaluation_examples)
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Usage in Evaluation

Expected facts are evaluated using predefined scorers such as `Correctness()` (the `mlflow.genai.scorers.Correctness` class). This scorer checks the model's output against the expected facts defined in the dataset and produces a score reflecting how well the output covers those facts. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

During evaluation, the scorer is applied to each example in the dataset:

```python
from mlflow.genai.scorers import Correctness

scorers = [Correctness()]

eval_results = mlflow.genai.evaluate(
    predict_fn=my_agent_function,
    data=eval_dataset,
    scorers=scorers,
)

# Access the overall correctness score
score = eval_results.metrics.get('correctness/mean', 0)
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

- **Cover key facts comprehensively**: Include expected facts that represent the most important information the model should capture, not every possible detail. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Use consistent datasets across evaluations**: Evaluate all prompt or agent versions against the same evaluation dataset for fair comparison. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Include edge cases**: Add challenging examples to your dataset to test model behavior in difficult scenarios. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- **Write clear, atomic facts**: Each expected fact should be a single, verifiable claim that a human or automated system can check against the output. Avoid compound facts that combine multiple claims. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Example Use Case: Summarization Evaluation

In a summarization task, expected facts are used to verify that the generated summary covers the essential information from the source text. For example, given source content about remote work trends, the expected facts might include: "remote work changed collaboration," "digital tools adopted," and "productivity remained stable." The evaluation then scores whether the model's summary includes these facts. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) – Built-in evaluators including `Correctness()` for fact coverage
- Prompt Version Comparison – Comparing different prompt versions using the same evaluation dataset
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Applying consistent datasets and judges across agent variants
- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that can incorporate expected facts in their evaluation criteria
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The broader evaluation framework using `mlflow.genai.evaluate()`

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
