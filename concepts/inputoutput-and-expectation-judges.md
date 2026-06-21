---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 71d74f473b7bdc6d063e1a47ad59b086cefc0be4834f3ee29b4e6cdcaeb3f13c
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inputoutput-and-expectation-judges
    - Expectation Judges and Input/Output
    - IAEJ
    - input/output judges
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Input/Output and Expectation Judges
description: Judges that evaluate agent responses by analyzing conversation inputs/outputs or comparing outputs against predefined expected behaviors
tags:
  - evaluation
  - quality-assessment
timestamp: "2026-06-19T14:28:39.559Z"
---

# Input/Output and Expectation Judges

**Input/Output and Expectation Judges** are a category of [Custom Judges](/concepts/custom-judges.md) that evaluate GenAI agent responses by analyzing the conversation inputs and outputs, or by comparing outputs against predefined expectations. They are created using the `make_judge()` API from `mlflow.genai.judges`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

Custom judges are LLM‑based scorers that assess agent quality against specific criteria. Input/Output Judges evaluate the conversation history (the `inputs`) and the agent's responses (the `outputs`) to determine metrics such as issue resolution or behavior compliance. Expectation Judges compare the agent's output against an explicit set of expectations provided in the evaluation dataset. Both judge types return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Creating an Input/Output Judge

An Input/Output Judge analyzes the user messages (`{{ inputs }}`) and the agent’s generated responses (`{{ outputs }}`). The following example defines a judge that classifies issue resolution as `fully_resolved`, `partially_resolved`, or `needs_follow_up`: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
from mlflow.genai.judges import make_judge
from typing import Literal

issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions=(
        "Evaluate if the customer's issue was resolved in the conversation.\n\n"
        "User's messages: {{ inputs }}\n"
        "Agent's responses: {{ outputs }}"
    ),
    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],
)
```

The `{{ inputs }}` and `{{ outputs }}` placeholders are substituted with the actual conversation data during evaluation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Creating an Expectation Judge

An Expectation Judge compares the agent’s output (`{{ outputs }}`) against the expectations (`{{ expectations }}`) defined in the evaluation dataset. The following example defines a judge that checks whether responses meet `meets_expectations`, `partially_meets`, or `does_not_meet`: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
expected_behaviors_judge = make_judge(
    name="expected_behaviors",
    instructions=(
        "Compare the agent's response in {{ outputs }} against the expected behaviors in {{ expectations }}.\n\n"
        "User's question: {{ inputs }}"
    ),
    feedback_value_type=Literal["meets_expectations", "partially_meets", "does_not_meet"],
)
```

The `expectations` are optional fields in the evaluation dataset (e.g., `{"should_provide_pricing": True}`) that define desired behaviors for the judge to verify. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Usage in Agent Evaluation

Both judge types are passed as the `scorers` argument to `mlflow.genai.evaluate()`. Multiple judges can be used together in a single evaluation run. The following example evaluates an agent with both an Input/Output judge and an Expectation judge: ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
    ],
)
```

The evaluation dataset must contain an `inputs` field (the conversation history) and may optionally contain an `expectations` field. Each `inputs` entry is passed to the agent’s prediction function, and the outputs are then scored by the judges. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## A/B Comparisons

Input/Output and Expectation Judges are well suited for [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md). By running the same evaluation dataset against two agent variants and applying the same judges, developers can compare score distributions and determine which configuration better satisfies quality criteria. The judges’ structured feedback values (e.g., `fully_resolved` vs. `needs_follow_up`) make the comparison quantitative and reproducible. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) — The overarching category of LLM‑based evaluators.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) — Judges that analyze execution traces using `{{ trace }}`.
- make_judge()|Make Judge API — The `make_judge()` function and its parameters.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) — The `mlflow.genai.evaluate()` function.
- Align judges with human feedback — Improving judge accuracy with expert annotations.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying judges for continuous quality monitoring.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
