---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 7859a2d249eb6fd2a9e969798dc32e344522fcb2ae69367d894ee63d4423cb6a
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 0.95
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-based-judges-make_judge
    - CLJ(
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Custom LLM-based Judges (make_judge)
description: Factory function in MLflow for creating LLM-based scorers that evaluate GenAI agents against custom quality criteria.
tags:
  - MLflow
  - GenAI
  - evaluation
  - judges
timestamp: "2026-06-19T17:54:34.164Z"
---

## Custom LLM-based Judges (`make_judge`)

**Custom LLM-based Judges** are programmable, LLM-powered scorers created with the `make_judge()` API in MLflow. They evaluate GenAI agents against specific quality criteria by analyzing conversation history, agent responses, and optionally execution traces. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Overview

Custom judges allow developers to define their own evaluation metrics for GenAI applications using a large language model as the evaluator. Unlike static regex-based checks, LLM judges can understand context, nuance, and multi-turn conversations. They are particularly useful for assessing subjective or complex criteria such as issue resolution quality, expected behaviors, or correctness of tool usage. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

Judges created with `make_judge()` return [`mlflow.entities.Feedback`](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.entities.html#mlflow.entities.Feedback) objects, which integrate seamlessly with MLflow's evaluation and monitoring pipelines. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Creating a Custom Judge

The `make_judge()` function is imported from `mlflow.genai.judges`. Its signature is:

```python
from mlflow.genai.judges import make_judge
from typing import Literal

judge = make_judge(
    name="judge_name",
    instructions="Evaluation instructions with placeholders like {{ inputs }}, {{ outputs }}, {{ expectations }}, or {{ trace }}",
    feedback_value_type=Literal["value1", "value2"]  # or bool, int, float
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

#### Parameters

- **`name`** (str): A human-readable identifier for the judge. This name appears in evaluation results.
- **`instructions`** (str): A prompt template that tells the LLM how to evaluate. It can include Jinja2-style placeholders:
  - `{{ inputs }}` — the conversation history or user inputs.
  - `{{ outputs }}` — the agent's generated responses.
  - `{{ expectations }}` — optional expected behaviors defined in the evaluation dataset.
  - `{{ trace }}` — when included, the judge becomes **trace-based** and gains autonomous trace exploration capabilities.
- **`feedback_value_type`**: Defines the output type of the judge. Options include:
  - A `Literal` type (e.g., `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]`) for categorical ratings.
  - `bool` for binary true/false judgments.
  - `int` or `float` for numeric scores.
- **`model`** (optional, required for trace-based judges): Specifies the LLM to use. For trace-based judges, a model must be explicitly provided, typically in the format `"databricks:/model-name"` (e.g., `"databricks:/databricks-gpt-5-mini"`). ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Types of Custom Judges

#### 1. Input/Output Judge
Evaluates based on the conversation inputs and agent outputs. The `{{ inputs }}` and `{{ outputs }}` placeholders are populated automatically when the judge is used with `mlflow.genai.evaluate()`.

**Example:** Issue resolution judge that classifies conversations into three categories:
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
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

#### 2. Expected Behaviors Judge
Checks agent responses against predefined expectations. The `{{ expectations }}` placeholder is populated from the evaluation dataset where each test case can include an `expectations` dictionary.

**Example:**
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
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

#### 3. Trace-Based Judge
When `{{ trace }}` is included in the instructions, the judge becomes trace-based. It gains the ability to autonomously explore the execution trace — including tool calls, intermediate results, and the control flow — to make a judgment. This is especially useful for evaluating tool usage correctness.

**Example:** Validating that appropriate tools were called:
```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent called appropriate tools for the user's request.\n\n"
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

### Using Judges in Evaluation

Custom judges are passed as a list to the `scorers` parameter of `mlflow.genai.evaluate()`. Multiple judges can be used together to evaluate different aspects of an agent.

**Example workflow:**
1. Create an evaluation dataset with `inputs` (conversation messages) and optionally `expectations`.
2. Define one or more custom judges.
3. Call `mlflow.genai.evaluate()` with the agent's prediction function and the list of judges.
4. Compare results across different agent configurations (e.g., by toggling a global variable that changes the system prompt).

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
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The evaluation results contain a rating for each judge per test case. For example, the `issue_resolution` judge might rate conversations as `'fully_resolved'`, `'partially_resolved'`, or `'needs_follow_up'`, while a bool judge like `tool_call_correctness` returns `True`/`False`. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Improving Judge Accuracy

The base judge created with `make_judge()` is a starting point. To improve accuracy, MLflow provides a mechanism to [align judges with human feedback](/concepts/aligning-judges-with-human-experts.md). By collecting expert ratings on the application's outputs and using them to refine the judge instructions, users can iteratively improve the alignment between automated LLM judgments and human expectations. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Related Concepts

- Evaluation of GenAI applications — End-to-end workflows for evaluating and improving agents.
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) — Deploying custom judges for continuous quality monitoring.
- Align judges with human feedback — Techniques to improve judge accuracy using human annotations.
- [MLflow Tracking](/concepts/mlflow-tracking.md) — The underlying experiment tracking used by `evaluate()`.
- [Trace-based evaluation](/concepts/mlflow-trace-based-evaluation.md) — Evaluation method that analyzes execution traces.

### Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
