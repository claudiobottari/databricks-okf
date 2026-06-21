---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: b06d58e04be51979479794c4a1375b15c2d6d77606303259405922afff04b397
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-judges-make_judge
    - CJ(
    - Custom Judges (make_judge)
    - Custom Judges Using Make Judge
    - Custom judge using make_judge()
    - Custom judges using make_judge
    - Custom judges using make_judge()
    - custom judges using make_judge()
    - Create a custom judge using make_judge()
    - custom judge|custom judges
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Custom Judges (make_judge)
description: LLM-based scorers created with `make_judge()` that evaluate GenAI agent outputs against user-defined quality criteria, returning `mlflow.entities.Feedback` objects.
tags:
  - mlflow
  - genai
  - evaluation
  - llm-as-judge
timestamp: "2026-06-18T11:12:10.011Z"
---

# Custom Judges (make_judge)

**Custom judges** are LLM-based scorers created with `make_judge()` that evaluate GenAI agents against specific quality criteria. They return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects and can be used with both [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) (via `mlflow.genai.evaluate()`) and [Production Monitoring](/concepts/production-monitoring.md).^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Overview

`make_judge()` is a factory function in the `mlflow.genai.judges` module that creates custom LLM-based judges. Each judge evaluates a specific quality criterion by analyzing inputs, outputs, expectations, or execution traces. Judges can be combined to assess different aspects of an agent's behavior in a single evaluation run.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Creating a Custom Judge

### Basic Syntax

```python
from mlflow.genai.judges import make_judge
from typing import Literal

judge = make_judge(
    name="judge_name",
    instructions="Evaluation instructions with {{ template_variables }}",
    feedback_value_type=Literal["value1", "value2"],
    model="model_uri",  # Optional, required for trace-based judges
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Parameters

| Parameter | Description |
|-----------|-------------|
| `name` | A unique identifier for the judge |
| `instructions` | Evaluation criteria using Jinja-style template variables (`{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`) |
| `feedback_value_type` | The type of feedback values the judge returns — can be `bool`, `Literal[...]`, or other types |
| `model` | The model to use for evaluation (required for trace-based judges that use `{{ trace }}`) |

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Template Variables

Custom judges support several template variables in their instructions:

- **`{{ inputs }}`** — The conversation history or user inputs passed to the agent
- **`{{ outputs }}`** — The agent's responses
- **`{{ expectations }}`** — Expected behaviors defined in the evaluation dataset
- **`{{ trace }}`** — The execution trace of the agent (makes the judge trace-based)

When `{{ trace }}` is included in instructions, the judge becomes trace-based and gains autonomous trace exploration capabilities. Trace-based judges require a `model` parameter to be specified.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Types of Custom Judges

### Input/Output Judges

These judges evaluate agent performance by analyzing the conversation history and agent responses. They are useful for assessing outcomes like issue resolution or response quality.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
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

### Expected Behavior Judges

These judges verify that agent responses demonstrate specific expected behaviors by comparing outputs against predefined expectations in the evaluation dataset.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
expected_behaviors_judge = make_judge(
    name="expected_behaviors",
    instructions=(
        "Compare the agent's response in {{ outputs }} against the expected behaviors "
        "in {{ expectations }}.\n\n"
        "User's question: {{ inputs }}"
    ),
    feedback_value_type=Literal["meets_expectations", "partially_meets", "does_not_meet"],
)
```

### Trace-Based Judges

These judges analyze execution traces to validate tool calls, workflow steps, or other runtime behavior. They require a model specification and use `{{ trace }}` in their instructions.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

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

## Using Custom Judges in Evaluation

Custom judges are passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`. Multiple judges can be used together to evaluate different aspects of an agent.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

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

### Evaluation Dataset

The evaluation dataset should include `inputs` (conversation messages) and optionally `expectations` (expected behaviors for correctness checking). Each `inputs` entry is passed to the agent by `mlflow.genai.evaluate()`.^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
eval_dataset = [
    {
        "inputs": {
            "messages": [
                {"role": "user", "content": "How much does a microwave cost?"},
            ],
        },
        "expectations": {
            "should_provide_pricing": True,
            "should_offer_alternatives": True,
        },
    },
]
```

## Best Practices

- **Use multiple judges** to evaluate different quality dimensions (resolution, behavior, tool usage) in a single evaluation run
- **Define clear feedback types** using `Literal` or `bool` to make results interpretable
- **Include expectations** in your evaluation dataset to enable more nuanced correctness checking
- **Specify a model** for trace-based judges to enable autonomous trace exploration
- **Align judges with human feedback** over time to improve accuracy — the base judge is a starting point that can be refined as you gather expert feedback on your application's outputs^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) — Using custom judges in end-to-end evaluation workflows
- [Production Monitoring](/concepts/production-monitoring.md) — Deploying custom judges for continuous quality monitoring
- Align judges with human feedback — Improving judge accuracy with expert feedback
- [Code-based Scorers](/concepts/code-based-scorers.md) — Alternative approach for defining custom scorers
- Feedback (MLflow) — The structured output object returned by judges
- MLflow Models — Models that can be evaluated using custom judges

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
