---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 1257c1867c85e082a0ec6b1abe2b06f35fcad6c1c84e314bc3871196f24c94a0
  pageDirectory: concepts
  sources:
    - 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - guidelines-scorer
    - Guidelines scorers
    - Guidelines adherence
  citations:
    - file: 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md
title: Guidelines Scorer
description: An MLflow scorer that evaluates whether LLM responses adhere to user-defined natural language guidelines (e.g., language, tone, safety constraints).
tags:
  - mlflow
  - scorers
  - guidelines
timestamp: "2026-06-19T13:49:15.452Z"
---

# Guidelines Scorer

The **Guidelines Scorer** is a built-in scoring function in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that evaluates model outputs against user-defined textual guidelines using an [LLM Judge](/concepts/llm-judges.md). It is part of `mlflow.genai.scorers` and is designed for rapid quality assessment of GenAI applications.

## Overview

The Guidelines Scorer provides a simple way to define custom evaluation criteria as plain‑language statements. Each scorer instance expresses a single quality rule (e.g., "Response must be in the same language as the input") and returns a structured score indicating whether the output satisfies that rule. Multiple guidelines can be combined in a list and passed to `mlflow.genai.evaluate()` to create a multi‑faceted evaluation harness.^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

The scorer works by invoking an underlying LLM judge that reads the guideline, the input, and the output, then produces a rating and optional rationale. This eliminates the need for hand‑crafted metrics or ground‑truth labels during early development and iteration.

## Usage

### Basic Usage

1. Import `Guidelines` from `mlflow.genai.scorers`.
2. Create one or more `Guidelines` instances, each with a `guidelines` string and a `name`.
3. Pass the list of scorers to the `scorers` argument of `mlflow.genai.evaluate()`.

Example from the quickstart:

```python
from mlflow.genai.scorers import Guidelines

scorers = [
    Guidelines(
        guidelines="Response must be in the same language as the input",
        name="same_language",
    ),
    Guidelines(
        guidelines="Response must be funny or creative",
        name="funny"
    ),
    Guidelines(
        guidelines="Response must be appropriate for children",
        name="child_safe"
    ),
    Guidelines(
        guidelines="Response must follow the input template structure "
                    "from the request – filling in the blanks without "
                    "changing the other words.",
        name="template_match",
    ),
]
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

### Parameters

| Parameter   | Type   | Description |
|-------------|--------|-------------|
| `guidelines` | `str` | A natural‑language statement describing the evaluation criterion. The scorer uses this as the instruction to the LLM judge. |
| `name`       | `str` | A human‑readable identifier for the scorer. This name appears in the evaluation results and the MLflow UI. |

### Combining with Other Scorers

The `scorers` list can mix `Guidelines` instances with other built‑in scorers such as `Safety()` (a built‑in safety evaluator). For example:

```python
scorers = [
    Guidelines(guidelines="Response must be funny", name="funny"),
    Safety(),
]
```

^[10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md]

## Best Practices

- **Be specific and unambiguous.** Write guidelines as clear, testable rules. Vague criteria (e.g., “Be good”) produce inconsistent scores.
- **Use one guideline per scorer.** This allows independent analysis and debugging of each quality dimension.
- **Name scorers meaningfully.** Use the `name` to reflect the criterion so that results are easy to interpret in the [MLflow Experiment UI](/concepts/mlflow-experiment.md).
- **Iterate on guidelines with your data.** After reviewing scores, refine the wording to better capture the desired behavior.

## Related Concepts

- [Scorers and LLM Judges](/concepts/scorers-and-llm-judges.md) – The general framework for evaluating GenAI outputs.
- [Safety Scorer](/concepts/safety-scorer-in-mlflow.md) – A built‑in scorer for content safety evaluation.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API that orchestrates scoring.
- [Custom Judges](/concepts/custom-judges.md) – Creating more advanced judges with `make_judge()`.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using scorers to compare agent variants.

## Sources

- 10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md

# Citations

1. [10-minute-demo-evaluate-a-genai-app-databricks-on-aws.md](/references/10-minute-demo-evaluate-a-genai-app-databricks-on-aws-c90f1438.md)
