---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 4e7014e4f7c370a4191417684983e9da6531b2ee28cefc417ababa91d228560a
  pageDirectory: concepts
  sources:
    - evaluate-and-compare-prompt-versions-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judge-scorers-with-make_judge
    - CJSWM
  citations:
    - file: evaluate-and-compare-prompt-versions-databricks-on-aws.md
title: Custom Judge Scorers with make_judge
description: Creating bespoke evaluation metrics by defining a judge LLM with custom instructions and feedback types via mlflow.genai.make_judge.
tags:
  - evaluation
  - llm-as-judge
  - mlflow
timestamp: "2026-06-19T10:22:04.948Z"
---

# Custom Judge Scorers with `make_judge`

**Custom Judge Scorers with `make_judge`** refers to the ability to create domain-specific LLM-based evaluators using the `mlflow.genai.make_judge()` function. These custom scorers allow users to define arbitrary evaluation criteria for [GenAI](/concepts/mlflow-genai-evaluate-api.md) agent outputs and incorporate them into the [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) framework.

## Overview

The `make_judge()` function creates a judge scorer – an LLM-based evaluator that assesses outputs against user-defined quality criteria.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md] Custom judges enable teams to evaluate specific behaviors that built-in scorers may not cover, such as compliance with format requirements, adherence to instructions, or domain-specific correctness checks.

## Basic Usage

A custom judge is created by calling `make_judge()` with a name, evaluation instructions, and a feedback value type. The following example creates a judge that checks whether a summary respects a two-sentence requirement:^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
from mlflow.genai import make_judge
from typing import Literal

sentence_count_judge = make_judge(
    name="sentence_count_compliance",
    instructions="""Evaluate if this summary follows the 2-sentence requirement.
Summary: {{ outputs }}
Count the sentences carefully and determine if the summary has exactly 2 sentences.""",
    feedback_value_type=Literal["correct", "incorrect"],
)
```

The `instructions` parameter supports the `{{ outputs }}` template variable, which the framework replaces with the model's response at evaluation time. The `feedback_value_type` controls what kind of feedback the judge returns – here a literal type with two categories.

## Using Custom Judges in Evaluation

Custom judges are passed to `mlflow.genai.evaluate()` in the `scorers` parameter alongside built-in scorers:^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

```python
scorers = [
    Correctness(),  # built-in scorer
    sentence_count_judge,
]

eval_results = mlflow.genai.evaluate(
    predict_fn=my_agent_function,
    data=eval_dataset,
    scorers=scorers,
)
```

The evaluation results include metrics for each custom judge, such as `sentence_count_compliance/mean`, which can be used to compare performance across prompt versions or configurations.^[evaluate-and-compare-prompt-versions-databricks-on-aws.md]

## Best Practices

- **Start simple**: Begin with basic criteria and iteratively refine based on evaluation results.
- **Use consistent datasets**: Evaluate all versions against the same data for fair comparison.
- **Test edge cases**: Include challenging examples in your evaluation dataset to validate judge behavior.
- **Track everything**: Log prompt versions, evaluation results, and deployment decisions.

## Related Concepts

- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment
- [Scorers and Judges](/concepts/scorers-and-llm-judges.md) – Overview of built-in and custom evaluators
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Using judges to compare agent variants
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous quality monitoring

## Sources

- evaluate-and-compare-prompt-versions-databricks-on-aws.md

# Citations

1. [evaluate-and-compare-prompt-versions-databricks-on-aws.md](/references/evaluate-and-compare-prompt-versions-databricks-on-aws-bf6e3016.md)
