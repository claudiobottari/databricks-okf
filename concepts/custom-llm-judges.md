---
type: concept
x-llmwiki:
  schemaVersion: "0.1"
  contentHash: 863a7a0a83ff1c1e13ae4653a8c978207f3ca5740e190fbf242ba3d60da44d23
  pageDirectory: concepts
  sources:
    - scorers-and-llm-judges-databricks-on-aws.md
  confidence: 0.97
  provenanceState: extracted
  freshnessStatus: unverified
  aliases:
    - custom-llm-judges
    - CLJ
    - Custom MLflow Judges
    - Custom Prompt LLM Judges
  citations:
    - file: scorers-and-llm-judges-databricks-on-aws.md
    - file: create-a-custom-judge-using-make_judge-databricks-on-aws.md
title: Custom LLM Judges
description: User-defined judges created with custom prompts and instructions for specialized evaluation tasks, with support for judge alignment to match human standards.
tags:
  - mlflow
  - custom-evaluation
  - llm
timestamp: "2026-06-19T20:20:16.941Z"
---

# Custom LLM Judges

**Custom LLM judges** are user-defined, LLM-based scorers within the MLflow GenAI evaluation framework that evaluate GenAI agents or applications against specific, domain-oriented quality criteria. Unlike [built‑in LLM judges](/concepts/built-in-llm-judges.md), which cover general dimensions such as relevance, safety, and correctness, custom judges let developers define their own prompts, grading rubrics, and feedback types to match bespoke business requirements. ^[scorers-and-llm-judges-databricks-on-aws.md]

## Overview

Scorers form the core of MLflow's GenAI evaluation pipeline. They receive a trace from either `evaluate()` during development or from the production monitoring service, parse the trace to extract relevant fields, perform a quality assessment, and return a [Feedback](/concepts/feedback-object.md) object that is attached to the trace. ^[scorers-and-llm-judges-databricks-on-aws.md]

LLM judges are a specialised type of scorer that leverage a large language model for the assessment. A custom judge extends this concept by allowing full control over the evaluation prompt and the structure of the returned feedback (e.g., categorical labels like `fully_resolved`/`needs_follow_up`, boolean, or free‑form text). ^[scorers-and-llm-judges-databricks-on-aws.md]

Use custom judges when you need to:

- Evaluate domain‑specific criteria not covered by built‑in judges.
- Define a custom grading scale beyond simple pass/fail.
- Validate that an agent made appropriate decisions and tool calls for your particular use case. ^[scorers-and-llm-judges-databricks-on-aws.md]

## How They Work

A custom LLM judge is created with the `make_judge()` function, which accepts a name, instructions, a feedback value type, and optionally a model identifier. When the judge is invoked inside `mlflow.genai.evaluate()`, it:

1. Receives the evaluation trace produced by the agent run.
2. Parses the trace to extract the data referenced in the instructions (e.g., `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`).
3. Sends the prompt and extracted data to the configured LLM.
4. Returns a `Feedback` object containing the LLM's judgement, which is then attached to the trace and visible in the MLflow UI. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md, scorers-and-llm-judges-databricks-on-aws.md]

## Creating a Custom Judge

The `make_judge()` function is the primary API for defining custom judges. It takes the following key arguments:

- **`name`** – A short, human‑readable identifier for the judge.
- **`instructions`** – The prompt that the judge LLM will use. Template variables (`{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}`, `{{ trace }}`) are automatically replaced with data from the trace.
- **`feedback_value_type`** – The expected type of the judgement value. Can be a `Literal` (e.g., `Literal["fully_resolved", "partially_resolved", "needs_follow_up"]`), `bool`, or other Python type. The judge LLM will be instructed to output a value conforming to this type.
- **`model`** (optional) – The LLM to use for evaluation. If omitted, a Databricks‑hosted default judge model is used. Required for trace‑based judges.

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### Example: Input/Output Judge

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

### Example: Trace‑Based Judge

When the instructions contain `{{ trace }}`, the judge becomes **trace‑based** and gains the ability to autonomously explore the full execution trace, including tool calls, intermediate steps, and their results.

```python
tool_call_judge = make_judge(
    name="tool_call_correctness",
    instructions=(
        "Analyze the execution {{ trace }} to determine if the agent "
        "called appropriate tools for the user's request."
    ),
    feedback_value_type=bool,
    model="databricks:/databricks-gpt-5-mini",  # Required for trace‑based judges
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Types of Custom Judges

| Type | Data Sources | Typical Use Cases |
|------|--------------|-------------------|
| **Input/Output Judge** | `{{ inputs }}`, `{{ outputs }}`, `{{ expectations }}` | Evaluating issue resolution, adherence to expected behaviors, tone, politeness |
| **Trace‑Based Judge** | `{{ trace }}` (full execution trace including tool calls) | Validating correct tool usage, decision‑making, multi‑step reasoning |

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Using Custom Judges in Evaluation

Custom judges are passed as the `scorers` argument to `mlflow.genai.evaluate()`. Multiple judges can be used together to assess different quality dimensions simultaneously. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

### A/B Comparison of Agent Configurations

Custom judges are particularly useful for [A/B Comparison of Agent Configurations](/concepts/ab-comparison-of-agent-configurations.md): evaluating two (or more) variants of an agent against the same dataset and judges to quantify the impact of changes. The same set of judges is applied to each configuration, ensuring that score differences reflect changes in agent behavior rather than inconsistencies in evaluation criteria. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

```python
# Evaluate configuration A (e.g., agent that does not attempt to resolve issues)
result_a = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_fn_a,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)

# Evaluate configuration B (agent that does attempt to resolve issues)
result_b = mlflow.genai.evaluate(
    data=eval_dataset,
    predict_fn=agent_fn_b,
    scorers=[issue_resolution_judge, expected_behaviors_judge, tool_call_judge],
)
```

^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Selecting the LLM That Powers the Judge

By default, each judge uses a Databricks‑hosted LLM optimised for quality assessment. You can override this by providing a `model` argument in the format `<provider>:/<model-name>`. For example:

```python
from mlflow.genai.scorers import Correctness
Correctness(model="databricks:/databricks-gpt-5-mini")
```

^[scorers-and-llm-judges-databricks-on-aws.md]

For trace‑based judges, specifying a model is **required** because the judge needs an LLM capable of analysing the full trace structure. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Judge Alignment

Databricks recommends continuously improving custom judges by aligning them with human feedback. As expert annotations on agent outputs are gathered, the judge prompts or models can be updated to better reflect human quality assessments. See Align judges with human feedback. ^[create-a-custom-judge-using-make_judge-databricks-on-aws.md]

## Related Concepts

- [Built‑in LLM judges](/concepts/built-in-llm-judges.md) – Pre‑defined judges for common quality dimensions.
- [[Scorers]] – The general abstraction for evaluation metrics in MLflow GenAI.
- [Code‑based scorers](/concepts/code-based-scorers.md) – A more flexible (but more complex) alternative to LLM judges.
- [MLflow Evaluation](/concepts/mlflow-evaluation-ui.md) – The `mlflow.genai.evaluate()` API used to run judges.
- [Production Monitoring for GenAI](/concepts/production-quality-monitoring-mlflow-genai.md) – Deploying custom judges for continuous monitoring.
- Human Feedback Alignment – Improving judge accuracy with expert annotations.
- [Trace‑Based Evaluation](/concepts/mlflow-trace-based-evaluation.md) – Using execution traces for deeper quality analysis.

## Sources

- create-a-custom-judge-using-make_judge-databricks-on-aws.md
- scorers-and-llm-judges-databricks-on-aws.md

# Citations

1. [scorers-and-llm-judges-databricks-on-aws.md](/references/scorers-and-llm-judges-databricks-on-aws-b2df16f5.md)
2. [create-a-custom-judge-using-make_judge-databricks-on-aws.md](/references/create-a-custom-judge-using-make_judge-databricks-on-aws-956237bf.md)
