---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 80c640f83383f9195e4c32b8984943f944bba74d3f0b5caf62ebd6aa73cb26b8
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-scorer-for-factual-accuracy
    - CSFFA
    - factual accuracy
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Correctness Scorer for Factual Accuracy
description: A built-in MLflow scorer that checks whether generated output covers expected facts defined in the evaluation dataset.
tags:
  - evaluation
  - factual-accuracy
  - mlflow
timestamp: "2026-06-19T10:22:25.325Z"
---

# Correctness Scorer for Factual Accuracy

The **Correctness Scorer for Factual Accuracy** is a predefined MLflow GenAI scorer that evaluates whether an LLM-generated response contains all the key facts expected for a given input. It is available through `mlflow.genai.scorers.Correctness` and is commonly used in prompt version comparison and agent evaluation workflows. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

The Correctness scorer checks generated outputs against a set of **expected facts** defined in the evaluation dataset. For each evaluation example, the scorer compares the response to the listed expected facts and computes a score indicating how many of those facts are present in the output. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Usage

### Prerequisites

- MLflow 3.1.0 or higher ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]
- Unity Catalog schema with `CREATE FUNCTION`, `EXECUTE`, and `MANAGE` privileges ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Importing and Instantiating

```python
from mlflow.genai.scorers import Correctness

scorers = [
    Correctness(),  # Checks expected facts
    # Additional scorers can be added to the list
]
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Creating Test Data with Expected Facts

The evaluation dataset must include `expectations` containing an `expected_facts` list for each example: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
evaluation_examples = [
    {
        "inputs": {
            "content": """Remote work has fundamentally changed how teams collaborate..."""
        },
        "expectations": {
            "expected_facts": [
                "remote work changed collaboration",
                "digital tools adoption",
                "productivity remained stable",
                # ... more facts
            ]
        }
    },
]
```

### Running Evaluation

The Correctness scorer is passed to `mlflow.genai.evaluate()` alongside any other scorers: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
eval_results = mlflow.genai.evaluate(
    predict_fn=my_summary_function,
    data=eval_dataset,
    scorers=scorers,  # Includes Correctness()
)
```

## Interpreting Results

The Correctness scorer produces a metric accessible as `correctness/mean` in the evaluation results: ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
correctness_score = eval_results.metrics.get('correctness/mean', 0)
print(f"Correctness score: {correctness_score:.2f}")
# Interpretation: "Captures {correctness_score:.0%} of expected facts"
```

The score represents the percentage of expected facts that the generated response successfully covers. Higher scores indicate better factual completeness. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Common Use Cases

### Comparing Prompt Versions

The Correctness scorer is frequently used in [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) to quantify which prompt version captures more expected facts. For example, version 1 of a summarization prompt can be compared against version 2 to see which produces more factually complete summaries. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Part of a Scorer Suite

Correctness is typically combined with other scorers, such as custom [judges](/concepts/llm-judges.md), to create a comprehensive evaluation. In prompt comparison workflows, it is often weighted more heavily than other metrics (e.g., 70% correctness vs. 30% format compliance). ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Limitations

- The scorer depends entirely on the quality and completeness of the `expected_facts` defined in the evaluation dataset. Missing or incorrect expected facts will produce misleading scores.
- It evaluates factual presence but does not check for factual inaccuracies or hallucinations beyond the expected facts list.

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — User-defined LLM-based scorers for domain-specific evaluation criteria
- make_judge()|Make Judge API — The `make_judge()` function for creating custom evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` API for offline assessment
- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — Other built-in scorers available in MLflow GenAI
- [Evaluation Harness](/concepts/evaluation-harness.md) — Deep dive into the evaluation framework
- [Prompt Registry](/concepts/prompt-registry.md) — Version management for prompts being evaluated

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
