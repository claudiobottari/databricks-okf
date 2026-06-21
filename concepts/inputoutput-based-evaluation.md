---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 992b488aabdec6a695cfda6021ed6e7f3d4a5611a2e123a9a2d10b6e41142f2d
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.9
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - inputoutput-based-evaluation
    - Input/Output Evaluation
    - Input validation
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Input/Output-based Evaluation
description: Evaluation approach where judges assess agent performance by analyzing conversation history (inputs) and agent responses (outputs).
tags:
  - MLflow
  - GenAI
  - evaluation
  - judges
timestamp: "2026-06-19T17:54:35.355Z"
---

# Input/Output-based Evaluation

**Input/Output-based Evaluation** is a method for assessing a GenAI agent’s quality by analyzing only the conversation history (the user’s inputs) and the agent’s responses (the outputs). It is one of several evaluation strategies that can be implemented using custom LLM-based judges created with `make_judge()`.

## Overview

In input/output-based evaluation, a judge receives the conversation context and the agent’s reply and determines whether the agent met a specific criterion, such as resolving a customer issue. The judge does not inspect the internal execution trace or any external expectations; it relies solely on the visible dialog. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

This approach is useful when the evaluation criterion can be assessed from the final conversation alone. For example, a judge that checks whether a customer’s issue was resolved can be written to examine the user messages and the assistant’s final response. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Implementation with `make_judge()`

Judges that use input/output-based evaluation are defined by including the placeholders `{{ inputs }}` and `{{ outputs }}` in the judge’s instructions. `{{ inputs }}` is replaced with the user’s messages in the evaluation dataset, and `{{ outputs }}` is replaced with the agent’s generated response. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

For example, the following judge evaluates whether a customer issue was resolved:

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

This judge returns a categorical rating based solely on the visible dialog. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Distinction from Other Evaluation Types

Input/output-based evaluation is one of several strategies available with `make_judge()`. The source material highlights the following distinction: when `{{ trace }}` is included in the instructions instead of or in addition to `{{ inputs }}` and `{{ outputs }}`, the judge becomes **trace-based** and gains autonomous trace exploration capabilities. In contrast, input/output-based judges do not analyze execution traces; they only evaluate the surface-level conversation. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Another related variant includes the `{{ expectations }}` placeholder, which allows the judge to compare the agent’s output against predefined expected behaviors. The `expected_behaviors_judge` example in the source material uses both `{{ outputs }}` and `{{ expectations }}`, and also references `{{ inputs }}` for the user’s question, making it a hybrid approach rather than a pure input/output judge. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Use Cases

Input/output-based evaluation is well-suited for criteria that depend only on what was said and replied, such as:

- Issue resolution (fully resolved, partially resolved, needs follow-up)
- Politeness or tone
- Completeness of the answer based on the question

These judges can be combined with other judges (e.g., trace-based or expectations-based) to provide a comprehensive evaluation of an agent. For instance, the source material shows an evaluation that runs both `issue_resolution_judge` (input/output-based) and `tool_call_judge` (trace-based) together on the same dataset. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- Custom Judges (make_judge)|Custom judge using make_judge() – The general API for creating LLM-based judges.
- [Trace-based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Judges that analyze execution traces via the `{{ trace }}` placeholder.
- [Expectations-Based Evaluation](/concepts/expectations-based-evaluation.md) – Judges that compare outputs against predefined expectations using the `{{ expectations }}` placeholder.
- [MLflow GenAI Evaluation](/concepts/mlflow-genai-evaluation.md) – The broader framework for evaluating GenAI agents.
- [Evaluation Dataset](/concepts/evaluation-dataset.md) – The data structure containing inputs and optional expectations for scoring.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
