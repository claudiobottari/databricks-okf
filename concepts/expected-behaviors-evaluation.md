---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d326f379dafca66e6dbee03318c50af57079bf4d3c41f3f477d92e46c4c47505
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - expected-behaviors-evaluation
    - EBE
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Expected Behaviors Evaluation
description: Evaluation technique where judges verify that agent responses demonstrate predefined expected behaviors by comparing outputs against expectations.
tags:
  - MLflow
  - GenAI
  - evaluation
  - judges
timestamp: "2026-06-19T17:55:13.215Z"
---

# Expected Behaviors Evaluation

**Expected Behaviors Evaluation** is a quality assessment method in [MLflow GenAI](/concepts/mlflow-3-for-genai.md) that uses a [custom judge](/concepts/custom-judges.md) to verify whether a GenAI agent's responses exhibit predefined behaviors as specified by the evaluation dataset. It allows developers to systematically check that agent outputs align with desired characteristics such as providing pricing information, mentioning return policies, or offering troubleshooting steps.

## Overview

An expected behaviors judge is an LLM-based scorer built with `make_judge()` that compares the agent's output against a set of expectations provided in the evaluation data. The judge analyzes both the input (user messages) and the output (agent responses), and sometimes the expectations field, to produce a qualitative rating. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

This type of evaluation is commonly used in [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) side-by-side to measure how changes to the agent (e.g., system prompt, tool set, or model) affect its adherence to desired behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How It Works

The judge uses an instruction template that includes placeholders for the inputs (`{{ inputs }}`), outputs (`{{ outputs }}`), and expectations (`{{ expectations }}`). At evaluation time, the template is rendered with the actual data from each test case, and an LLM scores the output. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The evaluation dataset can contain an `expectations` dictionary alongside each test case's `inputs`. For example:

```python
{
    "inputs": {
        "messages": [
            {"role": "user", "content": "How much does a microwave cost?"}
        ]
    },
    "expectations": {
        "should_provide_pricing": True,
        "should_offer_alternatives": True
    }
}
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The judge's instruction references both the user's question and the expected behaviors to determine if the output meets them.

## Defining the Judge

An expected behaviors judge is created using `make_judge()` with:

- `name`: A string identifier for the judge.
- `instructions`: A template that includes placeholders such as `{{ outputs }}`, `{{ expectations }}`, and `{{ inputs }}`.
- `feedback_value_type`: A `Literal` or `bool` type specifying the possible ratings.

Example definition:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

expected_behaviors_judge = make_judge(
    name="expected_behaviors",
    instructions=(
        "Compare the agent's response in {{ outputs }} against the expected "
        "behaviors in {{ expectations }}.\n\n"
        "User's question: {{ inputs }}"
    ),
    feedback_value_type=Literal[
        "meets_expectations", "partially_meets", "does_not_meet"
    ],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Usage in Evaluation

The judge is passed as a scorer to `mlflow.genai.evaluate()`. It can be combined with other judges (e.g., issue resolution, tool call correctness) to produce a multi‑dimensional assessment. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
result = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[expected_behaviors_judge, ...]
)
```

### A/B Comparison Example

When comparing two agent configurations, the same `expected_behaviors_judge` is used on both evaluation runs. The ratings can then be compared to see which configuration better meets the defined behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Feedback Values

The `feedback_value_type` defines the possible ratings the judge can return. For expected behaviors evaluation, common values are:

| Value | Meaning |
|-------|---------|
| `meets_expectations` | The agent's output fulfills all expected behaviors. |
| `partially_meets` | Some expectations are met, but not all. |
| `does_not_meet` | The output fails to satisfy the expected behaviors. |

## Input/Output Judge Classification

Expected behaviors evaluation is an **input/output judge**, meaning it relies solely on the conversation history (inputs) and the agent's responses (outputs). It does not require access to the execution trace. This contrasts with [Trace-based Judges](/concepts/trace-based-judges.md) that analyze intermediate tool calls and reasoning steps. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Custom Judges](/concepts/custom-judges.md) – General framework for LLM‑based scoring in MLflow GenAI.
- make_judge()|Make Judge API – The `make_judge()` function used to define judges.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API for offline assessment.
- [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md) – Side‑by‑side testing using judges.
- [Input/Output Evaluation](/concepts/inputoutput-based-evaluation.md) – Assessment based on agent inputs and outputs only.
- Align judges with human feedback – Method to improve judge accuracy using expert annotations.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
