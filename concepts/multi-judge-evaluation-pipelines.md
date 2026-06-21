---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d94008acd438b5a7f75ab950fbcaf76e4beee86f198213b83992e6de14ceaa8e
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-judge-evaluation-pipelines
    - MEP
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Multi-Judge Evaluation Pipelines
description: The pattern of passing multiple custom judges as scorers to mlflow.genai.evaluate() to evaluate different aspects of an agent (issue resolution, expected behaviors, tool correctness) in a single run.
tags:
  - mlflow
  - evaluation
  - pipelines
  - genai
timestamp: "2026-06-19T09:27:05.758Z"
---

# Multi-Judge Evaluation Pipelines

**Multi-Judge Evaluation Pipelines** refer to the practice of using multiple [Custom Judges](/concepts/custom-judges.md) in a single evaluation run to assess different quality dimensions of a GenAI agent. By combining input/output judges, trace-based judges, and other custom scorers, teams can obtain a comprehensive, multi-faceted view of agent behavior during offline evaluation.

## Overview

A single judge can only evaluate one aspect of agent performance, such as issue resolution or factual correctness. A multi-judge pipeline allows you to run several judges simultaneously against the same set of agent outputs, giving you a richer picture of quality. In [MLflow GenAI](/concepts/mlflow-3-for-genai.md), you specify multiple judges as a list of `scorers` in the `mlflow.genai.evaluate()` call.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Components of a Multi-Judge Pipeline

A pipeline typically contains two or more judges, each targeting a distinct quality criterion:

- **Input/Output judges** evaluate the agent's conversation history (`{{ inputs }}`) and final responses (`{{ outputs }}`).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Trace-based judges** analyze the full execution trace (`{{ trace }}`), including tool invocations, intermediate reasoning, and their results.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Expectation judges** compare agent outputs against predefined expectations (`{{ expectations }}`) in the evaluation dataset.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Defining Judges for a Pipeline

Each judge is created using the make_judge()|Make Judge API (`make_judge()`). A judge includes:

- A `name` (e.g., `issue_resolution`, `tool_call_correctness`)
- `instructions` that describe the evaluation criteria and reference template variables (`{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`)
- A `feedback_value_type` that defines the set of possible ratings (e.g., `bool` or a `Literal` of strings)

Trace-based judges require a `model` specification because they need an LLM to explore the execution trace autonomously.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example: Three-Judge Pipeline

```python
from mlflow.genai.judges import make_judge
from typing import Literal

# Input/output judge
issue_resolution_judge = make_judge(
    name="issue_resolution",
    instructions=(
        "Evaluate if the customer's issue was resolved in the conversation.\n\n"
        "User's messages: {{ inputs }}\n"
        "Agent's responses: {{ outputs }}"
    ),
    feedback_value_type=Literal["fully_resolved", "partially_resolved", "needs_follow_up"],
)

# Expectation judge
expected_behaviors_judge = make_judge(
    name="expected_behaviors",
    instructions=(
        "Compare the agent's response in {{ outputs }} "
        "against the expected behaviors in {{ expectations }}.\n\n"
        "User's question: {{ inputs }}"
    ),
    feedback_value_type=Literal["meets_expectations", "partially_meets", "does_not_meet"],
)

# Trace-based judge
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

## Running the Pipeline

Pass the list of judges as the `scorers` argument to `mlflow.genai.evaluate()`:

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[
        issue_resolution_judge,
        expected_behaviors_judge,
        tool_call_judge,
    ],
)
```

Each judge returns an [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) object containing the rating and rationale. The evaluation results can be compared across different agent configurations (see [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md)).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Applications

- **Comprehensive quality assessment** – Evaluate multiple dimensions (e.g., resolution, behavior, tool usage) in a single run.
- **A/B comparison** – Run the same multi-judge pipeline against two agent versions to compare their scores.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- **Regression detection** – Monitor quality over time by consistently applying a fixed set of judges to new versions.
- **Production monitoring** – Deploy the same judges used offline to continuously evaluate live agent performance (see [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md)).

## Best Practices

- **Choose complementary judges** – Cover different aspects of quality to avoid overlapping evaluations.
- **Keep judge instructions consistent** – When comparing configurations, use identical judge definitions across runs.
- **Align judges with human feedback** – Refine judge instructions based on expert annotations to improve accuracy over time (see Align judges with human feedback).
- **Use trace-based judges for tool-heavy agents** – Trace judges provide visibility into tool calls that input/output judges cannot capture.

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – LLM-based scorers that define quality criteria
- make_judge()|Make Judge API – The `make_judge()` function for creating evaluators
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Comparing configurations using the same judges
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying judges for continuous quality monitoring
- Align judges with human feedback – Improving judge accuracy with expert annotations

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
