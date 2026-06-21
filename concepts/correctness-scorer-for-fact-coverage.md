---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 3e8c5f57bb757ddb0f9bd1e81a5649d20abfae6eb6deda8eca1d568e12938246
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - correctness-scorer-for-fact-coverage
    - CSFFC
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Correctness Scorer for Fact Coverage
description: A built-in MLflow scorer that evaluates whether LLM outputs contain expected facts defined in the evaluation dataset, measuring factual completeness.
tags:
  - evaluation
  - factuality
  - metrics
timestamp: "2026-06-18T12:11:45.750Z"
---

# Correctness Scorer for Fact Coverage

The **Correctness Scorer for Fact Coverage** is a predefined evaluator in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that measures how well a generated response covers the expected facts defined in an [Evaluation Dataset](/concepts/evaluation-dataset.md). The scorer compares the model's output against a list of expected facts and returns a score reflecting the proportion of facts that are present in the response. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Overview

The `Correctness` scorer is one of the predefined scorers available in MLflow GenAI for evaluating the quality of LLM-generated outputs. It is designed to assess factual coverage — whether the key information points that should be included in a response are actually present. The scorer is particularly useful for evaluating summarization tasks, question answering, and other applications where factual completeness is critical. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## How It Works

The Correctness scorer operates by checking the generated output against a set of `expected_facts` provided in the evaluation dataset. For each example in the dataset, the scorer determines which expected facts are covered in the model's response and calculates a coverage score. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Defining Expected Facts

Expected facts are specified in the `expectations` field of each evaluation example as a list of strings. Each string represents a fact that should ideally appear in the generated response. For example:

```python
evaluation_examples = [
    {
        "inputs": {
            "content": "Remote work has fundamentally changed how teams collaborate..."
        },
        "expectations": {
            "expected_facts": [
                "remote work changed collaboration",
                "digital tools adoption",
                "productivity remained stable",
                "challenges with company culture",
                "work-life balance issues",
                "global talent recruitment"
            ]
        }
    }
]
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Usage

### Import and Instantiation

```python
from mlflow.genai.scorers import Correctness

# Create the scorer instance
scorer = Correctness()
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Using in Evaluation

The scorer is passed to `mlflow.genai.evaluate()` as part of the `scorers` list:

```python
eval_results = mlflow.genai.evaluate(
    predict_fn=create_summary_function(PROMPT_NAME, version),
    data=eval_dataset,
    scorers=[
        Correctness(),  # Checks expected facts
        # Additional scorers...
    ],
)
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Interpreting Results

The Correctness scorer returns a metric with the key `correctness/mean`, which represents the average proportion of expected facts covered across all evaluation examples. A score of 1.0 indicates perfect coverage of all expected facts, while 0.0 indicates no coverage. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
# Access the correctness score
correctness_score = eval_results.metrics.get('correctness/mean', 0)
print(f"Correctness score: {correctness_score:.2f}")

# Percentage of expected facts captured
fact_coverage_pct = eval_results.metrics.get('correctness/mean', 0) * 100
print(f"Captures {fact_coverage_pct:.0f}% of expected facts")
```

^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Use Cases

### Prompt Version Comparison

The Correctness scorer is commonly used in [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) and prompt evaluation workflows. By comparing the correctness scores of different prompt versions evaluated against the same dataset, you can identify which prompt produces more factually complete responses. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

### Composite Scoring

The correctness score can be combined with other metrics to create composite evaluation scores. For example, weighting correctness at 70% and another criterion (such as sentence count compliance) at 30% provides a balanced assessment of overall response quality. ^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Related Concepts

- [Predefined Scorers](/concepts/mlflow-genai-predefined-scorers.md) — The complete list of built-in scorers available in MLflow GenAI
- [Evaluation Dataset](/concepts/evaluation-dataset.md) — How to create datasets with expected facts for scoring
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) — Using consistent scorers for comparing agent variants
- [Custom Judges](/concepts/custom-judges.md) — Creating domain-specific evaluation metrics with `make_judge()`
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) — The evaluation framework that integrates with the Correctness scorer

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
