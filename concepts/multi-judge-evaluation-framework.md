---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: d85d09253d5686e560da9a701e31fea7ced01dab80627f33824a5926bc404b08
  pageDirectory: concepts
  sources:
    - create-a-custom-judge-using-make_judge-databricks-on-aws.md
  confidence: 1
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - multi-judge-evaluation-framework
    - MEF
  citations:
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Multi-Judge Evaluation Framework
description: The practice of combining multiple custom judges (e.g., issue resolution, expected behaviors, tool call correctness) in a single `mlflow.genai.evaluate()` call to assess different quality dimensions of a GenAI agent simultaneously.
tags:
  - mlflow
  - genai
  - evaluation
  - testing
timestamp: "2026-06-18T11:12:38.910Z"
---

# Multi-Judge Evaluation Framework

The **Multi-Judge Evaluation Framework** is an approach for evaluating GenAI agents using multiple LLM‑based judges (*custom judges*) in a single evaluation run. Each judge assesses a different quality criterion—such as issue resolution, expected behaviors, or tool‑call correctness—and returns structured feedback. The framework is built on `make_judge()` for defining judges and `mlflow.genai.evaluate()` for running evaluations. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## How It Works

1. **Define custom judges** using `make_judge()`. Each judge specifies a name, evaluation instructions (which can include placeholders like `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, or `{{ trace }}`), and a feedback value type. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
2. **Create an evaluation dataset** containing test cases. Each test case has an `inputs` field (often a conversation history) and optionally an `expectations` field describing desired behaviors. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
3. **Run evaluations** by passing the dataset, a prediction function (the agent), and a list of judges (as `scorers`) to `mlflow.genai.evaluate()`. The framework calls each judge on every test case and collects the results. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
4. **Compare results** across different agent configurations (e.g., toggling a system prompt) to identify strengths and weaknesses. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Example: Three Custom Judges

The following examples, adapted from the official tutorial, show judges for a customer support agent. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Judge 1: Issue Resolution
Assesses whether the conversation resolved the user’s issue. Uses `{{ inputs }}` and `{{ outputs }}` to analyze the conversation.

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

### Judge 2: Expected Behaviors
Compares the agent’s response against a set of desired behaviors defined in `{{ expectations }}`.

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

### Judge 3: Tool‑Call Correctness (Trace‑Based)
Analyzes the execution trace (`{{ trace }}`) to validate that appropriate tools were called. A trace‑based judge must specify a `model` because it requires autonomous exploration of the trace.

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

## Building an Evaluation Dataset

The dataset is a list of dictionaries. Each entry contains an `inputs` field with the conversation history and an optional `expectations` field with boolean flags or other expected properties.

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
    # ... more test cases
]
```
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Running a Multi‑Judge Evaluation

Pass the dataset, the agent function (as `predict_fn`), and a list of judges (as `scorers`) to `mlflow.genai.evaluate()`. You can run the same evaluation twice with different agent configurations to compare results.

```python
# Evaluate when the agent does NOT try to resolve issues
RESOLVE_ISSUES = False
result_unresolved = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)

# Evaluate when the agent DOES try to resolve issues
RESOLVE_ISSUES = True
result_resolved = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=customer_support_agent,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)
```
^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

The evaluation produces per‑judge results for each test case, allowing direct comparison between configurations.

## Next Steps

- **Improve judge accuracy** by aligning judges with human feedback. The base judge is a starting point; as you gather expert feedback, align the LLM judges to further improve accuracy. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]
- Deploy the framework in [Production Monitoring](/concepts/production-monitoring.md) for continuous quality checks.

## Related Concepts

- make_judge() – The API for defining custom judges
- [Custom Judges](/concepts/custom-judges.md) – LLM‑based scorers for GenAI evaluation
- [MLflow evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` function
- [Production monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Using judges in live monitoring
- Feedback (MLflow) – The structured output type returned by judges

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md

# Citations

1. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
