---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 0911cf34ed7bb1f2e2ee8ff489e8a1c9b0d2e423a5c7352ee1a3802661f4845f
  pageDirectory: concepts
  sources:
    - correctness-judge-databricks-on-aws.md
  confidence: 0.8
  provenanceState: inferred
  freshnessStatus: unverified
  aliases:
    - databricks-mlflow-genai-evaluation-framework
    - DMGEF
  citations:
    - file: correctness-judge-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Databricks MLflow GenAI Evaluation Framework
description: A comprehensive evaluation framework on Databricks that includes built-in LLM judges, custom judge creation, and the mlflow.genai.evaluate() API for running evaluations.
tags:
  - databricks
  - mlflow
  - genai
  - evaluation-framework
timestamp: "2026-06-19T14:28:22.148Z"
---

# Databricks MLflow GenAI Evaluation Framework

The **Databricks MLflow GenAI Evaluation Framework** is a set of tools within [MLflow](/concepts/mlflow.md) for assessing the quality of generative AI applications, including agents, LLMs, and other GenAI systems. It provides built-in and custom [judges](/concepts/llm-judges.md) (LLM-based scorers), a standardized evaluation API, and support for offline and online monitoring.

## Overview

The framework is built around `mlflow.genai.evaluate()`, which takes an evaluation dataset with inputs and optional expectations, applies one or more scorers (judges) to the outputs, and returns structured feedback. This allows teams to systematically measure factual correctness, adherence to expected behaviors, tool call quality, and other domain-specific criteria.^[correctness-judge-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

A key use case is the [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md), where the same dataset is run against different agent variants with consistent scorers to quantify the impact of a change before promoting to production.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Judges

Judges are LLM-based evaluators that analyze the conversation history (inputs), agent responses (outputs), and optionally the full execution trace or ground-truth expectations. They return a feedback value (e.g., `"yes"/"no"`, categorical, or boolean) along with a rationale.^[correctness-judge-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Built-in Judges

The framework includes pre-configured judges. For example:

- **Correctness judge** — Assesses whether the response is factually correct by comparing against provided `expected_facts` or `expected_response`. It returns `"yes"` if correct, `"no"` if incorrect, with a rationale explaining supported or missing facts.^[correctness-judge-databricks-on-aws.md]

Usage:

```python
from mlflow.genai.scorers import Correctness

correctness_judge = Correctness()
feedback = correctness_judge(
    inputs={"request": "What is MLflow?"},
    outputs={"response": "MLflow is the largest open source AI engineering platform..."},
    expectations={"expected_facts": ["MLflow is open-source", "MLflow is an AI engineering platform"]}
)
print(feedback.value)  # "yes"
```

^[correctness-judge-databricks-on-aws.md]

The judge model can be customized via the `model` argument (e.g., `"databricks:/databricks-gpt-5-mini"`).^[correctness-judge-databricks-on-aws.md]

### Custom Judges with `make_judge`

The `make_judge()` API allows creating domain-specific judges. A judge can be:

- **Input/output judge** — evaluates based on conversation history and response.
- **Trace-based judge** — analyzes the full execution trace, including tool calls and intermediate steps. To enable this, include `{{ trace }}` in the judge’s instructions.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Example trace-based judge:

```python
from mlflow.genai import make_judge

tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Evaluation API

Use `mlflow.genai.evaluate()` to run offline evaluations. The `data` parameter accepts a list of dictionaries with `inputs`, `outputs`, and optional `expectations`. The `scorers` parameter lists the judges to apply.^[correctness-judge-databricks-on-aws.md, create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
eval_results = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=my_agent,   # or provide static outputs
    scorers=[correctness_judge, tool_call_judge],
)
```

## A/B Comparison

To compare two agent configurations:

1. Define a shared evaluation dataset.
2. Run `mlflow.genai.evaluate()` separately for each configuration, using identical scorers.
3. Compare the feedback values (e.g., `fully_resolved` vs `partially_resolved`) across runs.

This method isolates the effect of the configuration change.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Aligning Judges with Human Feedback

As expert annotations become available, custom judges should be fine-tuned to better reflect human quality assessments. This iterative process improves the correlation between automated scores and human judgment.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow GenAI](/concepts/mlflow-3-for-genai.md) – The broader MLflow module for generative AI applications.
- [Correctness Judge](/concepts/correctness-judge.md) – Built-in judge for factual accuracy.
- make_judge()|Make Judge API – Tool for creating domain-specific evaluators.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Methodology for comparing agent variants.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous monitoring.

## Sources

- correctness-judge-databricks-on-aws.md
- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [correctness-judge-databricks-on-aws.md](/references/correctness-judge-databricks-on-aws-85181199.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
