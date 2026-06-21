---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 9dc3bb2882a7afba111293fab8d28638ed0f9ee7c94b4898905cf3524638dac2
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judges-llm-based-scorers
    - CJ(S
    - Custom Judge|custom LLM-based scorers
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Custom Judges (LLM-based Scorers)
description: LLM-based scorers that evaluate GenAI agent outputs for specific quality criteria like issue resolution, expected behaviors, and tool usage
tags:
  - evaluation
  - genai
  - quality-assurance
timestamp: "2026-06-18T14:46:18.679Z"
---

# Custom Judges (LLM-based Scorers)

**Custom Judges** are LLM-based scorers that evaluate GenAI agents against user-defined quality criteria. They are created with the `make_judge()` API and used with `mlflow.genai.evaluate()` to assess agent outputs offline or in production. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

Custom judges allow developers to define evaluation criteria beyond built-in metrics. Each judge is an LLM that receives a prompt containing instructions and contextual data (inputs, outputs, expectations, or traces) and returns a structured feedback value (e.g., a string literal or boolean). Judges return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Types of Custom Judges

### Input/Output Judges

These judges evaluate the agent’s behavior by analyzing the conversation history (`{{ inputs }}`) and the agent’s responses (`{{ outputs }}`). They can also reference `{{ expectations }}` to compare outputs against predefined desired behavior. Common use cases include assessing issue resolution status or whether expected behaviors were exhibited. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Trace-Based Judges

Trace-based judges analyze the full execution trace of an agent call, including tool invocations, intermediate reasoning steps, and their results. To create a trace-based judge, include `{{ trace }}` in the instructions. This enables the judge to explore the trace autonomously. Trace-based judges require a model specification (e.g., `model="databricks:/databricks-gpt-5-mini"`). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Creating a Custom Judge

A judge is defined by calling `make_judge()` with:

- `name` – A unique identifier.
- `instructions` – The prompt sent to the LLM judge. Use Jinja-style placeholders: `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`.
- `feedback_value_type` – The type of feedback returned (e.g., a `Literal` of strings or `bool`).
- `model` – Required only for trace-based judges. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example: Issue Resolution Judge

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

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example: Expected Behaviors Judge

```python
expected_behaviors_judge = make_judge(
    name="expected_behaviors",
    instructions=(
        "Compare the agent's response in {{ outputs }} against the expected behaviors "
        "in {{ expectations }}.\n\nUser's question: {{ inputs }}"
    ),
    feedback_value_type=Literal["meets_expectations", "partially_meets", "does_not_meet"],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example: Trace-Based Tool Call Judge

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent called "
        "appropriate tools for the user's request.\n\n"
        "Examine the trace to:\n"
        "1. Identify what tools were available and their purposes\n"
        "2. Determine which tools were actually called\n"
        "3. Assess whether the tool calls were reasonable for addressing the user's question"
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Using Judges in Evaluation

To evaluate an agent offline, pass a list of judges as `scorers` to `mlflow.genai.evaluate()`. You can evaluate multiple configurations to compare performance (see [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md)). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

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

## Improving Judge Accuracy

The base judge is a starting point. As you gather expert feedback on your application’s outputs, you can Align judges with human feedback to further improve judge accuracy. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Next Steps

- Evaluate and improve a GenAI application – Use custom judges in end-to-end evaluation workflows.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploy custom judges for continuous quality monitoring in production.

## Related Concepts

- make_judge()|Make Judge API – The `make_judge()` function.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – `mlflow.genai.evaluate()` for offline assessment.
- [Trace-Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.
- Human Feedback Alignment – Improving judge accuracy with expert annotations.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md).

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
